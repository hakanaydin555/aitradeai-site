/**
 * AI Trade — form receiver (v3: check-up + ad review, lead scoring, ad click IDs).
 * Bound to the Google Sheet "AI Trade – Check-up talepleri".
 * Each submission adds one row to the "Başvurular" tab, sends you a notification email
 * whose subject starts with the priority label, and sends the applicant a confirmation.
 */
var NOTIFY_TO = 'hakan.aydin@aitradeai.net';
var CAL_URL = 'https://calendar.app.google/qvtHpnCi4qVszRdK8';
var SHEET_NAME = 'Başvurular';
// v3 adds the last 8 columns; existing rows keep their place, headers are added to the right automatically.
var COLUMNS = ['Tarih', 'Etiket', 'Puan', 'Ad soyad', 'Şirket', 'E-posta', 'Telefon', 'Web sitesi', 'Satış kanalı', 'Aylık sipariş', 'Ana sorun', 'Başlama zamanı', 'Rol', 'Not', 'Dil', 'Sayfa',
               'Form', 'Kaynak', 'gclid', 'utm_campaign', 'Uygun mu', 'Not gönderildi', 'Check-up yapıldı'];
var FIELDS  = ['_date', '_label', '_score', 'name',   'company', 'email',  'phone',  'website',   'channel',      'orders',        'concern',   'timing',          'role', 'note', 'lang', 'page',
               '_form', '_source', 'gclid', 'utm_campaign', '', '', ''];
var FORM_NAMES = { checkup: 'Check-up', ad_review: 'Reklam değerlendirmesi' };

// Points per answer, by option position in the form (same order in EN and TR).
var POINTS = {
  orders:  [0, 2, 3, 3],    // <1k, 1-5k, 5-20k, 20k+
  timing:  [3, 2, 0],       // this month, 1-3 months, just exploring
  role:    [3, 2, 1, 0],    // owner/GM, e-com manager, marketing, other
  concern: [1, 1, 1, 1, 0]  // any concrete problem vs "not sure yet"
};
var FREE_MAIL = /@(gmail|googlemail|hotmail|outlook|live|msn|yahoo|ymail|yandex|icloud|me|mac|aol|gmx|mail|protonmail|proton|mynet|windowslive)\.[a-z.]+$/i;

function score_(p) {
  var s = 0;
  Object.keys(POINTS).forEach(function (k) {
    var i = parseInt(p[k + '_i'], 10);
    if (!isNaN(i) && POINTS[k][i] !== undefined) s += POINTS[k][i];
  });
  if (p.email && !FREE_MAIL.test(p.email)) s += 2;
  if (p.website) s += 1;
  return s; // max 13
}

/** Ad review: owner / GM / e-commerce manager with 1,000+ orders = priority; agency or <1,000 orders = low. */
function adScore_(p) {
  var role = parseInt(p.role_i, 10), orders = parseInt(p.orders_i, 10);
  var s = ([3, 3, 1, 0, 0][role] || 0) + ([0, 2, 3, 3][orders] || 0);
  if (p.email && !FREE_MAIL.test(p.email)) s += 2;
  if (p.website) s += 1;
  return s; // max 9
}

function adLabel_(p, s) {
  var role = parseInt(p.role_i, 10), orders = parseInt(p.orders_i, 10);
  if (role === 3 || orders === 0) return '⚪ Düşük';
  if (s >= 7) return '🟢 Öncelikli';
  return '🟡 İncele';
}

function source_(p) {
  if (p.utm_source) return clean_(p.utm_source);
  if (p.gclid) return 'google (gclid)';
  return 'organik / doğrudan';
}

function label_(s) {
  if (s >= 10) return '🟢 Öncelikli';
  if (s >= 6) return '🟡 İncele';
  return '⚪ Düşük';
}

function doPost(e) {
  var p = (e && e.parameter) || {};
  if (p.website2) return ok_(); // spam trap
  var isAd = p.form === 'ad_review';
  var s = isAd ? adScore_(p) : score_(p);
  var max = isAd ? 9 : 13;
  var values = { _date: new Date(), _score: s, _label: isAd ? adLabel_(p, s) : label_(s),
                 _form: FORM_NAMES[p.form] || 'Check-up', _source: source_(p) };
  var row = FIELDS.map(function (f) { return f === '' ? '' : f.charAt(0) === '_' ? values[f] : clean_(p[f]); });

  var lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    getSheet_().appendRow(row);
  } finally {
    lock.releaseLock();
  }

  var lines = COLUMNS.map(function (c, i) { return c + ': ' + (row[i] === '' ? '—' : row[i]); }).slice(1, 20);
  MailApp.sendEmail({
    to: NOTIFY_TO,
    replyTo: clean_(p.email),
    subject: values._label + ' · ' + (isAd ? 'Reklam değerlendirmesi: ' : 'Check-up talebi: ') + (clean_(p.company) || clean_(p.website) || clean_(p.name) || 'web sitesi') + ' (' + s + '/' + max + ')',
    body: lines.join('\n')
  });
  autoReply_(p);
  return ok_();
}

/** Confirmation email to the applicant (max one per address per day). */
function autoReply_(p) {
  var to = String(p.email || '').trim();
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(to)) return;
  var cache = CacheService.getScriptCache();
  var key = 'ar_' + to.toLowerCase();
  if (cache.get(key)) return;
  cache.put(key, '1', 21600);
  var name = String(p.name || '').trim().split(' ')[0];
  var tr = p.lang === 'tr';
  if (p.form === 'ad_review') {
    MailApp.sendEmail({
      to: to, name: 'AI Trade', replyTo: NOTIFY_TO,
      subject: 'Reklam değerlendirmesi talebinizi aldık — AI Trade',
      body: 'Merhaba ' + name + ',\n\nTalebinizi aldık, teşekkürler. ' + (clean_(p.website) || 'Web siteniz') + ' için aktif reklamlarınızı inceleyip tek sayfalık değerlendirme notunu 1 iş günü içinde bu adrese gönderiyoruz.\n\nNotu aldıktan sonra, gözlemlerin kârınıza etkisini 30 dakikalık check-up görüşmesinde birlikte ölçebiliriz:\n' + CAL_URL + '\n\nAI Trade\nhttps://aitradeai.net'
    });
    return;
  }
  var body = tr
    ? 'Merhaba ' + name + ',\n\nCheck-up talebinizi aldık, teşekkürler. İnceleyip bir iş günü içinde size dönüyoruz.\n\nDaha önce konuşmak isterseniz 30 dakikalık görüşme için saat seçebilirsiniz:\n' + CAL_URL + '\n\nAI Trade\nhttps://aitradeai.net'
    : 'Hello ' + name + ',\n\nThank you, we have received your check-up request. We will review it and reply within one business day.\n\nIf you would like to talk sooner, pick a time for a 30-minute call:\n' + CAL_URL + '\n\nAI Trade\nhttps://aitradeai.net';
  MailApp.sendEmail({
    to: to,
    name: 'AI Trade',
    replyTo: NOTIFY_TO,
    subject: tr ? 'Check-up talebinizi aldık — AI Trade' : 'We received your check-up request — AI Trade',
    body: body
  });
}

function getSheet_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(SHEET_NAME) || ss.insertSheet(SHEET_NAME, 0);
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(COLUMNS);
    sheet.setFrozenRows(1);
    sheet.getRange(1, 1, 1, COLUMNS.length).setFontWeight('bold');
  } else if (sheet.getLastColumn() < COLUMNS.length) {
    // v2 sheet: add the new v3 headers to the right, keep existing rows as they are
    sheet.getRange(1, 1, 1, COLUMNS.length).setValues([COLUMNS]).setFontWeight('bold');
  }
  return sheet;
}

function clean_(v) {
  v = String(v || '').slice(0, 2000).trim();
  return /^[=+\-@]/.test(v) ? "'" + v : v; // stop formulas being injected into the sheet
}

function ok_() {
  return ContentService.createTextOutput('ok').setMimeType(ContentService.MimeType.TEXT);
}

/** Run once from the editor after updating: adds an ad-review sample row (with a test gclid). */
function testAdReview() {
  doPost({ parameter: {
    form: 'ad_review', lang: 'tr', page: '/tr/reklam-degerlendirmesi', website: 'example.com', name: 'Test Kişi', email: NOTIFY_TO,
    role: 'E-ticaret yöneticisi', role_i: '1', orders: '5.000–20.000', orders_i: '2',
    gclid: 'TEST-GCLID', utm_source: 'google', utm_campaign: 'reklam-degerlendirmesi-test'
  } });
}

/** Run once from the editor: adds a high-score sample row and sends a test email. */
function testSubmit() {
  doPost({ parameter: {
    lang: 'tr', page: '/tr/check-up', name: 'Test Kişi', email: NOTIFY_TO, company: 'TEST A.Ş.', website: 'example.com',
    channel: 'İkisi de', channel_i: '2', orders: '5.000–20.000', orders_i: '2', concern: 'Reklam verimliliği', concern_i: '1',
    timing: 'Bu ay', timing_i: '0', role: 'Şirket sahibi / Genel müdür', role_i: '0', note: 'Deneme'
  } });
}
