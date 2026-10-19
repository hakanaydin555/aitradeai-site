/**
 * AI Trade — check-up form receiver.
 * Bound to the Google Sheet "AI Trade – Check-up talepleri".
 * Each form submission adds one row and sends a notification email.
 */
var NOTIFY_TO = 'hakan.aydin@aitradeai.net';
var SHEET_NAME = 'Talepler';
var COLUMNS = ['Tarih', 'Dil', 'Ad soyad', 'E-posta', 'Şirket', 'Telefon', 'Satış kanalı', 'Aylık sipariş', 'Ana sorun', 'Rol', 'Not', 'Sayfa'];
var FIELDS  = [null,    'lang', 'name',     'email',   'company', 'phone',  'channel',      'orders',        'concern',   'role', 'note', 'page'];

function doPost(e) {
  var p = (e && e.parameter) || {};
  if (p.website2) return ok_(); // spam trap
  var lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    var sheet = getSheet_();
    var row = FIELDS.map(function (f) { return f ? clean_(p[f]) : new Date(); });
    sheet.appendRow(row);
  } finally {
    lock.releaseLock();
  }
  var lines = COLUMNS.slice(1).map(function (c, i) { return c + ': ' + (clean_(p[FIELDS[i + 1]]) || '—'); });
  MailApp.sendEmail({
    to: NOTIFY_TO,
    replyTo: clean_(p.email),
    subject: 'Yeni check-up talebi: ' + (clean_(p.company) || clean_(p.name) || 'web sitesi'),
    body: lines.join('\n')
  });
  return ok_();
}

function getSheet_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(SHEET_NAME) || ss.insertSheet(SHEET_NAME);
  if (sheet.getLastRow() === 0) {
    sheet.appendRow(COLUMNS);
    sheet.setFrozenRows(1);
  }
  return sheet;
}

function clean_(v) {
  v = String(v || '').slice(0, 2000).trim();
  // stop formulas being injected into the sheet
  return /^[=+\-@]/.test(v) ? "'" + v : v;
}

function ok_() {
  return ContentService.createTextOutput('ok').setMimeType(ContentService.MimeType.TEXT);
}

/** Run once from the editor to test: adds a sample row and sends a test email. */
function testSubmit() {
  doPost({ parameter: { lang: 'tr', name: 'Test Kişi', email: NOTIFY_TO, company: 'Test A.Ş.', channel: 'Pazar yerleri', orders: '1.000–5.000', concern: 'Reklam verimliliği', role: 'E-ticaret müdürü', note: 'Deneme', page: '/tr/check-up' } });
}
