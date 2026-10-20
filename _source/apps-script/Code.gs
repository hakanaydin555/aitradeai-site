/**
 * AI Trade — check-up form receiver (v2, with lead scoring).
 * Bound to the Google Sheet "AI Trade – Check-up talepleri".
 * Each submission adds one row to the "Başvurular" tab and sends a notification email
 * whose subject starts with the priority label.
 */
var NOTIFY_TO = 'hakan.aydin@aitradeai.net';
var SHEET_NAME = 'Başvurular';
var COLUMNS = ['Tarih', 'Etiket', 'Puan', 'Ad soyad', 'Şirket', 'E-posta', 'Telefon', 'Web sitesi', 'Satış kanalı', 'Aylık sipariş', 'Ana sorun', 'Başlama zamanı', 'Rol', 'Not', 'Dil', 'Sayfa'];
var FIELDS  = ['_date', '_label', '_score', 'name',   'company', 'email',  'phone',  'website',   'channel',      'orders',        'concern',   'timing',          'role', 'note', 'lang', 'page'];

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

function label_(s) {
  if (s >= 10) return '🟢 Öncelikli';
  if (s >= 6) return '🟡 İncele';
  return '⚪ Düşük';
}

function doPost(e) {
  var p = (e && e.parameter) || {};
  if (p.website2) return ok_(); // spam trap
  var s = score_(p);
  var values = { _date: new Date(), _score: s, _label: label_(s) };
  var row = FIELDS.map(function (f) { return f.charAt(0) === '_' ? values[f] : clean_(p[f]); });

  var lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    getSheet_().appendRow(row);
  } finally {
    lock.releaseLock();
  }

  var lines = COLUMNS.map(function (c, i) { return c + ': ' + (row[i] === '' ? '—' : row[i]); }).slice(1);
  MailApp.sendEmail({
    to: NOTIFY_TO,
    replyTo: clean_(p.email),
    subject: values._label + ' · Check-up talebi: ' + (clean_(p.company) || clean_(p.name) || 'web sitesi') + ' (' + s + '/13)',
    body: lines.join('\n')
  });
  return ok_();
}

function getSheet_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(SHEET_NAME) || ss.insertSheet(SHEET_NAME, 0);
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(COLUMNS);
    sheet.setFrozenRows(1);
    sheet.getRange(1, 1, 1, COLUMNS.length).setFontWeight('bold');
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

/** Run once from the editor: adds a high-score sample row and sends a test email. */
function testSubmit() {
  doPost({ parameter: {
    lang: 'tr', page: '/tr/check-up', name: 'Test Kişi', email: NOTIFY_TO, company: 'TEST A.Ş.', website: 'example.com',
    channel: 'İkisi de', channel_i: '2', orders: '5.000–20.000', orders_i: '2', concern: 'Reklam verimliliği', concern_i: '1',
    timing: 'Bu ay', timing_i: '0', role: 'Şirket sahibi / Genel müdür', role_i: '0', note: 'Deneme'
  } });
}
