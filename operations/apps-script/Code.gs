/**
 * ImplementAI: applications and enquiries
 *
 * Paste this file and Templates.gs into the Apps Script project of the Google Sheet
 * "ImplementAI – Pilot applications" (Extensions > Apps Script). Setup steps: operations/SETUP.md.
 *
 * What it does
 *  - doPost: receives the website forms and adds a row to "Applicants" (pilot) or "Enquiries" (Quick-Check, contact).
 *  - sendPendingConfirmations: sends the confirmation email to every row with status "New"
 *    (website rows straight away, Facebook rows added by Zapier/Make within 10 minutes).
 *  - Menu "ImplementAI > Create email draft": writes a Gmail draft for the selected applicant
 *    that matches its status. Drafts are never sent automatically.
 */

// ---------- Settings: fill these in ----------
var CONFIG = {
  SPREADSHEET_ID: '1rBI76hgVDs0AlgDZo-9r6d9259FILZjBvhjEaBE-X7A',
  REPLY_TO: 'implementsai@gmail.com',            // e.g. 'hello@implementai.at' (replies go here); empty = the sending account
  SENDER_NAME: 'ImplementAI',
  SELECTION_DATE_EN: '',     // e.g. '15 December' -> "by 15 December"; empty -> "before we launch"
  SELECTION_DATE_DE: '',     // e.g. '15. Dezember' -> "bis 15. Dezember"; empty -> "vor unserem Start"
  BOOKING_LINK: '',          // e.g. a Google Calendar booking page; empty -> ask for times by reply
  NOTIFY_TEAM: '',           // optional: comma-separated addresses that get a short notice per new application
};
// ----------------------------------------------

var TZ = 'Europe/Vienna';
var APPLICANTS = 'Applicants';
var ENQUIRIES = 'Enquiries';
// Applicants columns (1-based)
var A = { id: 1, received: 2, source: 3, lang: 4, name: 5, business: 6, email: 7, phone: 8, industry: 9, team: 10,
          software: 11, problem: 12, often: 13, who: 14, cost: 15, solved: 16, problem2: 17, caseStudy: 18,
          status: 19, confirmed: 20, nextDate: 28, notes: 29, timing: 30, perk: 31, hook: 32 };
// Enquiries columns (1-based)
var E = { id: 1, received: 2, form: 3, source: 4, lang: 5, name: 6, business: 7, email: 8, phone: 9, industry: 10,
          team: 11, message: 12, status: 13, confirmed: 14, notes: 18 };

// ---------- Website forms ----------
function doPost(e) {
  var p = (e && e.parameter) || {};
  if (p.website) return json_({ ok: true });            // honeypot field filled in: a bot
  var lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    var form = (p.form || '').toLowerCase();
    if (form === 'pilot') addApplicant_(p); else addEnquiry_(p, form);
  } finally {
    lock.releaseLock();
  }
  try { sendPendingConfirmations(); } catch (err) { console.error(err); }
  return json_({ ok: true });
}

function doGet() {
  return json_({ ok: true, service: 'ImplementAI forms' });
}

function addApplicant_(p) {
  var sh = sheet_(APPLICANTS);
  var industry = pick_(p, 'industry', 'branche');
  var row = [];
  row[A.id - 1] = nextId_(sh, 'A-');
  row[A.received - 1] = now_();
  row[A.source - 1] = source_(p);
  row[A.lang - 1] = lang_(p);
  row[A.name - 1] = pick_(p, 'name');
  row[A.business - 1] = pick_(p, 'business', 'betrieb');
  row[A.email - 1] = pick_(p, 'email');
  row[A.phone - 1] = text_(pick_(p, 'phone', 'telefon'));
  row[A.industry - 1] = industry_(industry);
  row[A.team - 1] = text_(pick_(p, 'team_size', 'teamgroesse'));
  row[A.software - 1] = pick_(p, 'current_tools', 'software');
  row[A.problem - 1] = pick_(p, 'pain_what', 'problem');
  row[A.often - 1] = pick_(p, 'pain_frequency', 'haeufigkeit');
  row[A.who - 1] = pick_(p, 'pain_who', 'betroffene');
  row[A.cost - 1] = pick_(p, 'pain_cost', 'kosten');
  row[A.solved - 1] = pick_(p, 'pain_solved', 'ziel');
  row[A.problem2 - 1] = pick_(p, 'pain_2', 'problem_2');
  row[A.caseStudy - 1] = pick_(p, 'case_study_ok', 'fallstudie_ok') ? 'Yes' : 'No';
  row[A.status - 1] = 'New';
  row[A.confirmed - 1] = '';
  for (var i = A.confirmed; i < A.notes - 1; i++) row[i] = '';
  row[A.notes - 1] = industry ? 'Industry as entered: ' + industry : '';
  row[A.timing - 1] = timing_(pick_(p, 'timing', 'zeitplan'));
  row[A.perk - 1] = pick_(p, 'founding_perk', 'gruender_vorteil') ? 'Yes' : 'No';
  row[A.hook - 1] = hook_(p.utm_content);
  writeRow_(sh, row);
  notifyTeam_('New pilot application: ' + row[A.business - 1] + ' (' + row[A.industry - 1] + ')', row[A.problem - 1]);
}

function addEnquiry_(p, form) {
  var sh = sheet_(ENQUIRIES);
  var industry = pick_(p, 'industry', 'branche');
  var row = [];
  row[E.id - 1] = nextId_(sh, 'EQ-');
  row[E.received - 1] = now_();
  row[E.form - 1] = form === 'quickcheck' ? 'Quick-Check' : 'Contact';
  row[E.source - 1] = source_(p);
  row[E.lang - 1] = lang_(p);
  row[E.name - 1] = pick_(p, 'name');
  row[E.business - 1] = pick_(p, 'business', 'betrieb');
  row[E.email - 1] = pick_(p, 'email');
  row[E.phone - 1] = text_(pick_(p, 'phone', 'telefon'));
  row[E.industry - 1] = industry_(industry);
  row[E.team - 1] = text_(pick_(p, 'team_size', 'teamgroesse'));
  row[E.message - 1] = pick_(p, 'challenge', 'herausforderung', 'message', 'nachricht');
  row[E.status - 1] = 'New';
  for (var i = E.status; i < E.notes - 1; i++) row[i] = '';
  row[E.notes - 1] = industry ? 'Industry as entered: ' + industry : '';
  writeRow_(sh, row);
  notifyTeam_('New ' + row[E.form - 1] + ' enquiry: ' + (row[E.business - 1] || row[E.name - 1]), row[E.message - 1]);
}

// ---------- Confirmation emails ----------
function sendPendingConfirmations() {
  confirm_(sheet_(APPLICANTS), A, 'pilot_confirmation');
  confirm_(sheet_(ENQUIRIES), E, 'enquiry_confirmation');
}

function confirm_(sh, C, templateKey) {
  var last = sh.getLastRow();
  if (last < 2) return;
  var values = sh.getRange(2, 1, last - 1, sh.getLastColumn()).getValues();
  for (var r = 0; r < values.length; r++) {
    var v = values[r];
    var status = String(v[C.status - 1]);
    var email = String(v[C.email - 1]).trim();
    if (status !== 'New' || !email || String(v[C.source - 1]) === 'Example') continue;
    var lang = String(v[C.lang - 1]).toUpperCase() === 'DE' ? 'DE' : 'EN';
    var data = { Name: v[C.name - 1], Business: v[C.business - 1], Problem: C.problem ? v[C.problem - 1] : '' };
    var mail = render_(templateKey, lang, data);
    GmailApp.sendEmail(email, mail.subject, mail.body, mailOptions_());
    sh.getRange(r + 2, C.status).setValue('Confirmation sent');
    sh.getRange(r + 2, C.confirmed).setValue(now_());
  }
}

// ---------- Menu and email drafts ----------
function onOpen() {
  SpreadsheetApp.getUi().createMenu('ImplementAI')
    .addItem('Create email draft for selected applicant', 'createDraftForSelection')
    .addItem('Send pending confirmations now', 'sendPendingConfirmations')
    .addSeparator()
    .addItem('Set up automatic confirmations (every 10 minutes)', 'setup')
    .addToUi();
}

var DRAFT_FOR_STATUS = {
  'Needs more info': 'pilot_more_info',
  'Shortlisted': 'pilot_shortlisted',
  'Selected': 'pilot_selected',
  'Not selected': 'pilot_not_selected',
  'Discovery booked': 'discovery_prep'
};

function createDraftForSelection() {
  var ui = SpreadsheetApp.getUi();
  var sh = SpreadsheetApp.getActiveSheet();
  var row = sh.getActiveRange().getRow();
  if (sh.getName() !== APPLICANTS || row < 2) {
    ui.alert('Select a row in the Applicants tab first.');
    return;
  }
  var v = sh.getRange(row, 1, 1, sh.getLastColumn()).getValues()[0];
  var status = String(v[A.status - 1]);
  var key = DRAFT_FOR_STATUS[status];
  if (!key) {
    ui.alert('No email for status "' + status + '". Drafts exist for: ' + Object.keys(DRAFT_FOR_STATUS).join(', ') + '.');
    return;
  }
  var lang = String(v[A.lang - 1]).toUpperCase() === 'DE' ? 'DE' : 'EN';
  var date = v[A.nextDate - 1];
  var dateText = date instanceof Date ? formatDate_(date, lang) : (date ? String(date) : '[date]');
  var mail = render_(key, lang, { Name: v[A.name - 1], Business: v[A.business - 1], Problem: v[A.problem - 1], DiscoveryDate: dateText });
  var opts = mailOptions_();
  GmailApp.createDraft(String(v[A.email - 1]), mail.subject, mail.body, opts);
  ui.alert('Draft created in Gmail for ' + v[A.name - 1] + ' (' + status + '). Check it and send it from Gmail.');
}

function setup() {
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (t.getHandlerFunction() === 'sendPendingConfirmations') ScriptApp.deleteTrigger(t);
  });
  ScriptApp.newTrigger('sendPendingConfirmations').timeBased().everyMinutes(10).create();
  SpreadsheetApp.getActive().toast('Automatic confirmations are on (every 10 minutes).');
}

// ---------- Helpers ----------
function render_(key, lang, data) {
  var t = TEMPLATES[key][lang];
  var vars = {
    Name: data.Name || (lang === 'DE' ? '' : 'there'),
    Business: data.Business || (lang === 'DE' ? 'Ihren Betrieb' : 'your business'),
    Problem: data.Problem || '',
    DiscoveryDate: data.DiscoveryDate || '[date]',
    Signature: TEMPLATE_VARS.Signature[lang],
    SelectionWhen: lang === 'DE'
      ? (CONFIG.SELECTION_DATE_DE ? 'bis ' + CONFIG.SELECTION_DATE_DE : 'vor unserem Start')
      : (CONFIG.SELECTION_DATE_EN ? 'by ' + CONFIG.SELECTION_DATE_EN : 'before we launch'),
    BookingSentence: lang === 'DE'
      ? (CONFIG.BOOKING_LINK ? 'Bitte wählen Sie hier einen passenden Termin: ' + CONFIG.BOOKING_LINK
                             : 'Bitte antworten Sie mit zwei oder drei Terminen, die Ihnen diese oder nächste Woche passen.')
      : (CONFIG.BOOKING_LINK ? 'Please pick a time that suits you here: ' + CONFIG.BOOKING_LINK
                             : 'Please reply with two or three times that suit you this week or next.')
  };
  var fill = function (s) { return s.replace(/\{\{(\w+)\}\}/g, function (_, k) { return vars[k] !== undefined ? vars[k] : ''; }); };
  var body = fill(t.body);
  if (!vars.Problem) body = body.replace(/\n(The problem you described|Das Problem, das Sie beschrieben haben):\n.*\n/, '\n');
  return { subject: fill(t.subject), body: body };
}

function mailOptions_() {
  var o = { name: CONFIG.SENDER_NAME };
  if (CONFIG.REPLY_TO) o.replyTo = CONFIG.REPLY_TO;
  return o;
}

function notifyTeam_(subject, text) {
  if (!CONFIG.NOTIFY_TEAM) return;
  GmailApp.sendEmail(CONFIG.NOTIFY_TEAM, subject, (text || '') + '\n\n' + SpreadsheetApp.openById(CONFIG.SPREADSHEET_ID).getUrl());
}

function sheet_(name) {
  return SpreadsheetApp.openById(CONFIG.SPREADSHEET_ID).getSheetByName(name);
}

function writeRow_(sh, row) {
  // Write below the last row that has any content (website rows, Facebook rows from Zapier/Make, manual rows).
  var r = sh.getLastRow();
  // Write only up to "Confirmation sent", then the filled cells after it (Notes, Timing, Founding benefits):
  // the Score column holds a formula that fills the whole column, and writing into it (even an empty value) would break it.
  var start = sh.getName() === APPLICANTS ? A.confirmed : E.confirmed;
  var firstPart = row.slice(0, start);
  sh.getRange(r + 1, 1, 1, firstPart.length).setValues([firstPart]);
  for (var c = start; c < row.length; c++) if (row[c]) sh.getRange(r + 1, c + 1).setValue(row[c]);
}

// Which ad brought the registration: utm_content of the ad link (hook1 ... hook5), stored as "Hook 1" ... "Hook 5".
function hook_(v) {
  var m = String(v || '').match(/hook\s*-?\s*(\d)/i);
  return m ? 'Hook ' + m[1] : String(v || '');
}

// Website answers come in English or German; the Sheet always stores the English wording.
function timing_(v) {
  var map = { 'So bald wie möglich': 'As soon as possible', 'In den nächsten 3 Monaten': 'In the next 3 months',
              'Dieses Jahr': 'This year', 'Erst einmal nur neugierig': 'Just curious for now' };
  return map[v] || v || '';
}

function nextId_(sh, prefix) {
  var ids = sh.getRange(1, 1, Math.max(sh.getLastRow(), 1), 1).getValues();
  var max = 0;
  ids.forEach(function (x) {
    var m = String(x[0]).match(new RegExp('^' + prefix + '(\\d+)$'));
    if (m) max = Math.max(max, parseInt(m[1], 10));
  });
  return prefix + ('000' + (max + 1)).slice(-4);
}

function pick_(p) {
  for (var i = 1; i < arguments.length; i++) {
    var v = p[arguments[i]];
    if (v !== undefined && String(v).trim() !== '') return String(v).trim();
  }
  return '';
}

function lang_(p) { return String(p.lang || '').toLowerCase().indexOf('de') === 0 ? 'DE' : 'EN'; }

function source_(p) {
  var s = String(p.utm_source || '').toLowerCase();
  if (s.indexOf('facebook') >= 0 || s === 'fb') return 'Facebook';
  if (s.indexOf('instagram') >= 0 || s === 'ig') return 'Instagram';
  return 'Website';
}

function industry_(v) {
  var s = String(v || '').toLowerCase();
  if (!s) return '';
  if (/restaurant|caf|bar|gastro|catering/.test(s)) return 'Gastronomy';
  if (/hotel|pension|guest|hospitality|hotellerie|apartment/.test(s)) return 'Hospitality';
  if (/practice|clinic|ordination|arzt|beauty|kosmetik|friseur|hair|salon|spa|sthetik|aesthetic|wellness|health|gesundheit/.test(s)) return 'Wellness & Beauty';
  return 'Other';
}

function text_(v) { return v ? "'" + v : ''; }   // keeps phone numbers and "1–10" as text

function now_() { return Utilities.formatDate(new Date(), TZ, 'yyyy-MM-dd HH:mm'); }

function formatDate_(d, lang) {
  return lang === 'DE' ? Utilities.formatDate(d, TZ, 'd.M.yyyy') : Utilities.formatDate(d, TZ, 'd MMMM yyyy');
}

function json_(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}

// ---------- Test without the website ----------
function testWebsiteApplication() {
  doPost({ parameter: {
    form: 'pilot', lang: 'en', name: 'Test Person', business: 'Test Restaurant', email: Session.getActiveUser().getEmail(),
    industry: 'Restaurant / café / bar', team_size: '1–10', current_tools: 'Excel', pain_what: 'Test: we miss booking calls.',
    pain_frequency: '20 a week', pain_who: 'Owner', pain_cost: '5 lost bookings a week', consent: 'on'
  } });
}
