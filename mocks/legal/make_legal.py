"""Drafts of the imprint and privacy policy pages (EN + DE) in the Atelier design.
Placeholders are <mark>ed. Run: python3 mocks/legal/make_legal.py"""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
A = '../../assets'
T = lambda s: f'<mark>{s}</mark>'   # placeholder still to fill in

STYLE = """
<style>
.legal-hero{padding:72px 0 40px}
.legal-hero h1{font-size:clamp(2.6rem,6vw,4.8rem)}
.legal-hero p{max-width:640px;font-size:1.1rem}
.legal{display:grid;grid-template-columns:240px 1fr;gap:64px;padding:0 0 110px;align-items:start}
.legal nav{position:sticky;top:100px;font-size:.92rem}
.legal nav b{display:block;font-size:.75rem;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-2);margin-bottom:12px}
.legal nav a{display:block;padding:6px 0;color:var(--ink-2);text-decoration:none;border-bottom:1px solid var(--line)}
.legal nav a:hover{color:var(--terra)}
.legal-body{max-width:760px}
.legal-body h2{font-size:1.9rem;margin:48px 0 14px;scroll-margin-top:100px}
.legal-body h2:first-child{margin-top:0}
.legal-body h3{font-family:var(--sans);font-weight:700;font-size:1rem;letter-spacing:0;margin:24px 0 6px}
.legal-body p,.legal-body li{line-height:1.7;color:var(--ink)}
.legal-body ul{padding-left:20px}
.legal-body a{color:var(--terra-d)}
.facts{display:grid;grid-template-columns:repeat(2,1fr);gap:1px;background:var(--line);border:1px solid var(--line);border-radius:18px;overflow:hidden;margin:0 0 8px}
.facts div{background:var(--paper);padding:20px 22px}
.facts b{display:block;font-family:var(--serif);font-weight:400;font-size:1.25rem;margin-bottom:4px}
.facts span{color:var(--ink-2);font-size:.95rem;line-height:1.5}
dl.kv{display:grid;grid-template-columns:220px 1fr;margin:0;border-top:1px solid var(--line)}
dl.kv dt,dl.kv dd{margin:0;padding:12px 0;border-bottom:1px solid var(--line);line-height:1.55}
dl.kv dt{color:var(--ink-2);font-size:.92rem;padding-right:16px}
mark{background:var(--butter);padding:0 4px;border-radius:4px;color:var(--ink)}
.draft{background:var(--forest);color:var(--cream);font-size:.9rem;padding:12px 0}
.draft .wrap{display:flex;gap:12px;align-items:center}
.draft mark{font-size:.85rem}
.updated{color:var(--ink-3);font-size:.9rem;margin-top:48px}
@media (max-width:860px){.legal{grid-template-columns:1fr;gap:28px}.legal nav{position:static}.facts{grid-template-columns:1fr}dl.kv{grid-template-columns:1fr}dl.kv dt{border-bottom:0;padding-bottom:0}}
</style>"""

def page(lang, title, eyebrow, h1, intro, sections, other_href, other_label, home, draft_note, toc_label, updated, before=''):
    toc = ''.join(f'<a href="#{i}">{h}</a>' for i, h, _ in sections)
    body = before + ''.join(f'<h2 id="{i}">{h}</h2>{c}' for i, h, c in sections)
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — ImplementAI</title>
<meta name="robots" content="noindex">
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Newsreader:ital,opsz,wght@0,6..72,400;1,6..72,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{A}/style.css">{STYLE}
</head>
<body>
<div class="draft"><div class="wrap">{draft_note}</div></div>
<header class="header">
  <div class="wrap nav">
    <a href="{home}" class="brand"><img src="{A}/img/logo.svg" alt="ImplementAI" class="brand-logo"></a>
    <div class="nav-actions"><a href="{other_href}" class="lang">{other_label}</a></div>
  </div>
</header>
<main>
<section class="legal-hero"><div class="wrap"><span class="eyebrow"><b>§</b> {eyebrow}</span><h1>{h1}</h1><p class="muted">{intro}</p></div></section>
<div class="wrap legal">
  <nav><b>{toc_label}</b>{toc}</nav>
  <div class="legal-body">{body}<p class="updated">{updated}</p></div>
</div>
</main>
<footer class="footer"><div class="wrap"><div class="footer-bottom"><span>© 2026 ImplementAI</span><span>{other_label_footer(lang)}</span></div></div></footer>
</body></html>"""

def other_label_footer(lang):
    return ('<a href="imprint.html">Imprint</a> · <a href="privacy.html">Privacy</a>' if lang == 'en'
            else '<a href="impressum.html">Impressum</a> · <a href="datenschutz.html">Datenschutz</a>')

def kv(rows): return '<dl class="kv">' + ''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in rows) + '</dl>'

# ---------------- shared facts (fill in once) ----------------
CO, ADDR, EMAIL, PHONE = T('Company name and legal form'), T('Street and number, 10xx Vienna'), T('hello@…'), T('+43 …')
CO_DE, ADDR_DE = T('Firmenname und Rechtsform'), T('Straße und Hausnummer, 10xx Wien')
HOST = T('Hosting provider, address')
TRANSFER = T('Zapier, Inc. (USA) or Make / Celonis s.r.o. (Czech Republic)')
TRANSFER_DE = T('Zapier, Inc. (USA) oder Make / Celonis s.r.o. (Tschechien)')

# ================= IMPRINT EN =================
imprint_en = [
 ('provider', 'Service provider', '<p>Information under § 5 E-Commerce Act (ECG), § 14 Commercial Code (UGB) and § 63 Trade Regulation Act (GewO), and disclosure under § 25 Media Act (MedienG).</p>' + kv([
   ('Company', CO), ('Registered office', 'Vienna, Austria'), ('Address', ADDR),
   ('Email', EMAIL), ('Phone', PHONE),
   ('Managing partners / directors', 'Daniel Sheccoury, Dr. Tibor Sekera, Jean Christoph Leob ' + T('as applicable')),
   ('Company register number', T('FN … (only for a GmbH, OG or KG)')), ('Register court', 'Commercial Court Vienna (Handelsgericht Wien)'),
   ('VAT number', T('ATU… (omit if exempt as a small business)'))])),
 ('trade', 'Trade licence', kv([
   ('Trade', T('e.g. Management consultancy including business organisation (Unternehmensberatung einschließlich der Unternehmensorganisation)')),
   ('GISA number', T('…')), ('Trade authority', T('Municipal District Office for the …th district of Vienna (Magistratisches Bezirksamt)')),
   ('Chamber', 'Member of the Vienna Economic Chamber (Wirtschaftskammer Wien), ' + T('trade group UBIT')),
   ('Trade law', 'Trade Regulation Act (Gewerbeordnung), available at <a href="https://www.ris.bka.gv.at">www.ris.bka.gv.at</a>')])),
 ('media', 'Disclosure under § 25 MedienG', kv([
   ('Media owner', CO + ', ' + ADDR),
   ('Line of business', 'Consulting on and implementation of AI tools for small and medium-sized businesses in gastronomy, hospitality and wellness &amp; beauty'),
   ('Editorial line', 'Information about the services of ImplementAI')])),
 ('liability', 'Liability and copyright', '<p>We write the content of this website with care, but we cannot guarantee that it is complete, correct and up to date at all times. Prices and offers on this website are not binding until confirmed in writing.</p><p>We are not responsible for the content of external websites we link to. If we learn that a linked page breaks the law, we remove the link.</p><p>Texts, images and the logo on this website are protected by copyright. Please ask us before using them.</p>'),
]
# ================= IMPRINT DE =================
imprint_de = [
 ('anbieter', 'Diensteanbieter', '<p>Informationen gemäß § 5 E-Commerce-Gesetz (ECG), § 14 Unternehmensgesetzbuch (UGB) und § 63 Gewerbeordnung (GewO) sowie Offenlegung gemäß § 25 Mediengesetz (MedienG).</p>' + kv([
   ('Unternehmen', CO_DE), ('Sitz', 'Wien, Österreich'), ('Anschrift', ADDR_DE),
   ('E-Mail', EMAIL), ('Telefon', PHONE),
   ('Gesellschafter / Geschäftsführung', 'Daniel Sheccoury, Dr. Tibor Sekera, Jean Christoph Leob ' + T('je nach Rechtsform')),
   ('Firmenbuchnummer', T('FN … (nur bei GmbH, OG oder KG)')), ('Firmenbuchgericht', 'Handelsgericht Wien'),
   ('UID-Nummer', T('ATU… (entfällt bei Kleinunternehmerregelung)'))])),
 ('gewerbe', 'Gewerbeberechtigung', kv([
   ('Gewerbe', T('z. B. Unternehmensberatung einschließlich der Unternehmensorganisation')),
   ('GISA-Zahl', T('…')), ('Gewerbebehörde', T('Magistratisches Bezirksamt für den … Bezirk')),
   ('Kammer', 'Mitglied der Wirtschaftskammer Wien, ' + T('Fachgruppe UBIT')),
   ('Berufsrecht', 'Gewerbeordnung, abrufbar unter <a href="https://www.ris.bka.gv.at">www.ris.bka.gv.at</a>')])),
 ('medien', 'Offenlegung gemäß § 25 MedienG', kv([
   ('Medieninhaber', CO_DE + ', ' + ADDR_DE),
   ('Unternehmensgegenstand', 'Beratung zu und Einführung von KI-Tools für kleine und mittlere Betriebe in Gastronomie, Hotellerie sowie Wellness &amp; Beauty'),
   ('Grundlegende Richtung', 'Information über die Leistungen von ImplementAI')])),
 ('haftung', 'Haftung und Urheberrecht', '<p>Wir erstellen die Inhalte dieser Website mit Sorgfalt, können aber nicht garantieren, dass sie jederzeit vollständig, richtig und aktuell sind. Preise und Angebote auf dieser Website sind erst mit schriftlicher Bestätigung verbindlich.</p><p>Für die Inhalte externer Websites, auf die wir verlinken, sind wir nicht verantwortlich. Erfahren wir von rechtswidrigen Inhalten auf einer verlinkten Seite, entfernen wir den Link.</p><p>Texte, Bilder und das Logo dieser Website sind urheberrechtlich geschützt. Bitte fragen Sie uns, bevor Sie sie verwenden.</p>'),
]

# ================= PRIVACY EN =================
facts_en = '<div class="facts">' + ''.join(f'<div><b>{b}</b><span>{s}</span></div>' for b, s in [
  ('No cookies, no tracking', 'No analytics, no advertising pixels, no cookie banner needed.'),
  ('Only what you send us', 'We store what you enter in a form, to reply and to assess your application.'),
  ('Deleted on schedule', 'Applications that are not selected are deleted 6 months after the selection.'),
  ('People decide', 'Applications are read and scored by our team, not by an automated system.')]) + '</div>'
privacy_en = [
 ('controller', 'Who is responsible', '<p>The controller under the General Data Protection Regulation (GDPR) is:</p>' + kv([('Company', CO), ('Address', ADDR), ('Email', EMAIL)]) + '<p>For any question about your data, write to us at the address above. We do not need to appoint a data protection officer.</p>'),
 ('website', 'Visiting this website', f'<p>When you open this website, our hosting provider ({HOST}) automatically processes the technical data your browser sends: IP address, date and time, the page requested, and browser and operating system. This is needed to deliver the website and keep it secure (legitimate interest, Art. 6(1)(f) GDPR). These log files are deleted after {T("14")} days.</p><p>The fonts are loaded from our own server, not from Google. We use no cookies, no analytics tools and no advertising pixels (such as the Meta Pixel).</p><p>If you reach the website through one of our ads, the link contains the name of the campaign (for example “utm_campaign=pilot”). If you then send a form, we store this campaign name with it so we know which ad worked. It does not identify you.</p>'),
 ('forms', 'Forms: contact, Quick-Check and pilot application', '<p>When you send a form, we receive the details you enter: name, business, email, phone (optional), industry, team size, the software you use and your description of the problem. We also store the date, the page and the language of the form.</p><p>We use this to reply to you, arrange a meeting and, for the pilot programme, to assess and select applications. The legal basis is taking steps at your request before a possible contract (Art. 6(1)(b) GDPR). You then receive a confirmation email from us.</p><p>If you tick the case study box, we may publish the findings of your Discovery as a case study, anonymously if you wish. This is based on your consent (Art. 6(1)(a) GDPR), which you can withdraw at any time by email, with effect for the future.</p><p>Giving us these details is voluntary, but without them we cannot answer your request. Please do not include health information about your clients or patients in the form.</p>'),
 ('facebook', 'Applying through Facebook or Instagram', f'<p>If you apply through a form inside Facebook or Instagram, Meta Platforms Ireland Ltd. collects your answers on our behalf and passes them to us. We transfer them into our application list using {TRANSFER}. We then process them exactly as described for the website forms. Meta’s own processing when you use Facebook or Instagram is described in <a href="https://www.facebook.com/privacy/policy">Meta’s privacy policy</a>.</p>'),
 ('email', 'Email', '<p>If you write to us by email, we use your message and address to answer you (Art. 6(1)(b) GDPR, or Art. 6(1)(f) GDPR for general questions).</p>'),
 ('recipients', 'Who else receives your data', f'<p>Only our team (Daniel Sheccoury, Dr. Tibor Sekera, Jean Christoph Leob) can see your details. We do not sell them or pass them on for advertising. We use these service providers, who process data on our behalf under a data processing agreement:</p><ul><li><b>Google Ireland Ltd.</b> (Google Workspace: Sheets, Gmail, Apps Script): storing applications and sending emails</li><li><b>{HOST}</b>: hosting this website</li><li><b>Meta Platforms Ireland Ltd.</b>: Facebook and Instagram lead forms</li><li><b>{TRANSFER}</b>: transferring Facebook leads to our list</li></ul><p>Some of these providers or their parent companies are based in the USA. Transfers there are covered by the EU-US Data Privacy Framework (adequacy decision under Art. 45 GDPR) or by the EU standard contractual clauses (Art. 46 GDPR).</p>'),
 ('retention', 'How long we keep your data', '<ul><li><b>Pilot applications that are not selected:</b> deleted 6 months after the selection date.</li><li><b>Enquiries that do not lead to an assignment:</b> deleted 12 months after our last contact.</li><li><b>Clients:</b> for the duration of the assignment. Invoices and accounting records are kept for 7 years, as required by Austrian tax law (§ 132 BAO).</li><li><b>Server log files:</b> ' + T('14') + ' days.</li></ul>'),
 ('decisions', 'No automated decisions', '<p>We do not make decisions about you by automated means (Art. 22 GDPR). Every application is read and assessed by a person in our team.</p>'),
 ('rights', 'Your rights', '<p>You have the right to access your data (Art. 15 GDPR), to have it corrected (Art. 16) or deleted (Art. 17), to restrict its processing (Art. 18), to receive it in a portable format (Art. 20) and to object to processing based on our legitimate interest (Art. 21). You can withdraw consent at any time (Art. 7(3)). An email to us is enough.</p><p>If you believe we process your data unlawfully, you can complain to the Austrian Data Protection Authority: Datenschutzbehörde, Barichgasse 40–42, 1030 Vienna, <a href="mailto:dsb@dsb.gv.at">dsb@dsb.gv.at</a>, <a href="https://www.dsb.gv.at">www.dsb.gv.at</a>.</p>'),
]

facts_de = '<div class="facts">' + ''.join(f'<div><b>{b}</b><span>{s}</span></div>' for b, s in [
  ('Keine Cookies, kein Tracking', 'Keine Analyse-Tools, keine Werbe-Pixel, daher kein Cookie-Banner.'),
  ('Nur, was Sie uns schicken', 'Wir speichern Ihre Formular-Angaben, um zu antworten und Ihre Bewerbung zu prüfen.'),
  ('Löschung nach Plan', 'Nicht ausgewählte Bewerbungen löschen wir 6 Monate nach der Auswahl.'),
  ('Menschen entscheiden', 'Bewerbungen werden von unserem Team gelesen und bewertet, nicht automatisiert.')]) + '</div>'
privacy_de = [
 ('verantwortlich', 'Verantwortlicher', '<p>Verantwortlicher im Sinne der Datenschutz-Grundverordnung (DSGVO) ist:</p>' + kv([('Unternehmen', CO_DE), ('Anschrift', ADDR_DE), ('E-Mail', EMAIL)]) + '<p>Bei Fragen zu Ihren Daten schreiben Sie uns an die oben genannte Adresse. Zur Bestellung eines Datenschutzbeauftragten sind wir nicht verpflichtet.</p>'),
 ('website', 'Besuch dieser Website', f'<p>Wenn Sie diese Website aufrufen, verarbeitet unser Hosting-Anbieter ({T("Hosting-Anbieter, Anschrift")}) automatisch die technischen Daten, die Ihr Browser übermittelt: IP-Adresse, Datum und Uhrzeit, aufgerufene Seite sowie Browser und Betriebssystem. Das ist nötig, um die Website auszuliefern und sicher zu betreiben (berechtigtes Interesse, Art. 6 Abs. 1 lit. f DSGVO). Diese Protokolldateien werden nach {T("14")} Tagen gelöscht.</p><p>Die Schriften werden von unserem eigenen Server geladen, nicht von Google. Wir verwenden keine Cookies, keine Analyse-Tools und keine Werbe-Pixel (wie das Meta-Pixel).</p><p>Kommen Sie über eine unserer Anzeigen auf die Website, enthält der Link den Namen der Kampagne (z. B. „utm_campaign=pilot“). Senden Sie danach ein Formular ab, speichern wir diesen Kampagnennamen mit, damit wir wissen, welche Anzeige funktioniert hat. Er lässt keinen Rückschluss auf Ihre Person zu.</p>'),
 ('formulare', 'Formulare: Kontakt, Quick-Check und Pilot-Bewerbung', '<p>Wenn Sie ein Formular absenden, erhalten wir Ihre Angaben: Name, Betrieb, E-Mail, Telefon (freiwillig), Branche, Teamgröße, die Software, die Sie nutzen, und Ihre Beschreibung des Problems. Außerdem speichern wir Datum, Seite und Sprache des Formulars.</p><p>Wir verwenden diese Daten, um Ihnen zu antworten, einen Termin zu vereinbaren und im Pilotprogramm die Bewerbungen zu prüfen und auszuwählen. Rechtsgrundlage ist die Durchführung vorvertraglicher Maßnahmen auf Ihre Anfrage (Art. 6 Abs. 1 lit. b DSGVO). Sie erhalten anschließend eine Bestätigung per E-Mail.</p><p>Wenn Sie das Kästchen zur Fallstudie ankreuzen, dürfen wir die Ergebnisse Ihrer Analyse als Fallstudie veröffentlichen, auf Wunsch anonym. Grundlage ist Ihre Einwilligung (Art. 6 Abs. 1 lit. a DSGVO), die Sie jederzeit per E-Mail mit Wirkung für die Zukunft widerrufen können.</p><p>Die Angabe der Daten ist freiwillig, ohne sie können wir Ihre Anfrage aber nicht bearbeiten. Bitte geben Sie im Formular keine Gesundheitsdaten Ihrer Kund:innen oder Patient:innen an.</p>'),
 ('facebook', 'Bewerbung über Facebook oder Instagram', f'<p>Bewerben Sie sich über ein Formular in Facebook oder Instagram, erhebt Meta Platforms Ireland Ltd. Ihre Antworten in unserem Auftrag und übermittelt sie an uns. Wir übertragen sie mit {TRANSFER_DE} in unsere Bewerbungsliste und verarbeiten sie dann genau wie bei den Website-Formularen. Wie Meta selbst Daten verarbeitet, wenn Sie Facebook oder Instagram nutzen, steht in der <a href="https://www.facebook.com/privacy/policy">Datenschutzrichtlinie von Meta</a>.</p>'),
 ('email', 'E-Mail', '<p>Wenn Sie uns per E-Mail schreiben, verwenden wir Ihre Nachricht und Adresse, um Ihnen zu antworten (Art. 6 Abs. 1 lit. b DSGVO, bei allgemeinen Fragen Art. 6 Abs. 1 lit. f DSGVO).</p>'),
 ('empfaenger', 'Wer Ihre Daten noch erhält', f'<p>Ihre Angaben sieht nur unser Team (Daniel Sheccoury, Dr. Tibor Sekera, Jean Christoph Leob). Wir verkaufen sie nicht und geben sie nicht für Werbung weiter. Wir setzen folgende Dienstleister ein, die Daten in unserem Auftrag auf Grundlage eines Auftragsverarbeitungsvertrags verarbeiten:</p><ul><li><b>Google Ireland Ltd.</b> (Google Workspace: Sheets, Gmail, Apps Script): Speicherung der Bewerbungen und Versand der E-Mails</li><li><b>{T("Hosting-Anbieter")}</b>: Hosting dieser Website</li><li><b>Meta Platforms Ireland Ltd.</b>: Lead-Formulare in Facebook und Instagram</li><li><b>{TRANSFER_DE}</b>: Übertragung der Facebook-Bewerbungen in unsere Liste</li></ul><p>Einige dieser Anbieter oder ihre Muttergesellschaften haben ihren Sitz in den USA. Übermittlungen dorthin sind durch das EU-US Data Privacy Framework (Angemessenheitsbeschluss nach Art. 45 DSGVO) oder durch EU-Standardvertragsklauseln (Art. 46 DSGVO) abgesichert.</p>'),
 ('speicherdauer', 'Wie lange wir Ihre Daten speichern', '<ul><li><b>Nicht ausgewählte Pilot-Bewerbungen:</b> Löschung 6 Monate nach dem Auswahltermin.</li><li><b>Anfragen ohne Auftrag:</b> Löschung 12 Monate nach dem letzten Kontakt.</li><li><b>Kund:innen:</b> für die Dauer des Auftrags. Rechnungen und Buchhaltungsunterlagen bewahren wir 7 Jahre auf, wie es das österreichische Steuerrecht verlangt (§ 132 BAO).</li><li><b>Server-Protokolldateien:</b> ' + T('14') + ' Tage.</li></ul>'),
 ('entscheidungen', 'Keine automatisierten Entscheidungen', '<p>Wir treffen keine automatisierten Entscheidungen über Sie (Art. 22 DSGVO). Jede Bewerbung wird von einer Person aus unserem Team gelesen und bewertet.</p>'),
 ('rechte', 'Ihre Rechte', '<p>Sie haben das Recht auf Auskunft (Art. 15 DSGVO), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) und Widerspruch gegen Verarbeitungen auf Grundlage unseres berechtigten Interesses (Art. 21). Eine Einwilligung können Sie jederzeit widerrufen (Art. 7 Abs. 3). Eine E-Mail an uns genügt.</p><p>Wenn Sie meinen, dass wir Ihre Daten unrechtmäßig verarbeiten, können Sie sich bei der österreichischen Datenschutzbehörde beschweren: Datenschutzbehörde, Barichgasse 40–42, 1030 Wien, <a href="mailto:dsb@dsb.gv.at">dsb@dsb.gv.at</a>, <a href="https://www.dsb.gv.at">www.dsb.gv.at</a>.</p>'),
]

DN_EN = '<b>Draft.</b> <mark>Yellow</mark> = still to fill in. Have it checked (WKO or a lawyer) before going online.'
DN_DE = '<b>Entwurf.</b> <mark>Gelb</mark> = noch auszufüllen. Vor Veröffentlichung prüfen lassen (WKO oder Anwalt).'
pages = {
 'imprint.html': page('en', 'Imprint', 'Legal', 'Imprint', 'Who is behind ImplementAI, as required by Austrian law.', imprint_en, 'impressum.html', 'DE', '../../index.html', DN_EN, 'On this page', 'Last updated: ' + T('date')),
 'impressum.html': page('de', 'Impressum', 'Rechtliches', 'Impressum', 'Wer hinter ImplementAI steht, wie es das österreichische Recht verlangt.', imprint_de, 'imprint.html', 'EN', '../../de/index.html', DN_DE, 'Auf dieser Seite', 'Stand: ' + T('Datum')),
 'privacy.html': page('en', 'Privacy policy', 'Legal', 'Privacy <i>policy</i>', 'What we do with your details when you visit this website, send us a form or apply for the pilot programme, in plain language.', privacy_en, 'datenschutz.html', 'DE', '../../index.html', DN_EN, 'On this page', 'Last updated: ' + T('date'), before=facts_en),
 'datenschutz.html': page('de', 'Datenschutzerklärung', 'Rechtliches', 'Daten<i>schutz</i>', 'Was wir mit Ihren Daten machen, wenn Sie diese Website besuchen, uns ein Formular schicken oder sich für das Pilotprogramm bewerben, in verständlicher Sprache.', privacy_de, 'privacy.html', 'EN', '../../de/index.html', DN_DE, 'Auf dieser Seite', 'Stand: ' + T('Datum'), before=facts_de),
}
for name, html in pages.items():
    open(os.path.join(HERE, name), 'w').write(html)
print('ok', list(pages))
