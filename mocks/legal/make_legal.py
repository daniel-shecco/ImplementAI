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
{('<div class="draft"><div class="wrap">' + draft_note + '</div></div>') if draft_note else ""}
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
CO, ADDR, EMAIL, PHONE = 'Daniel Sheccoury', 'Gumpendorfer Straße 83–85/2/57, 1060 Vienna, Austria', '<a href="mailto:implementsai@gmail.com">implementsai@gmail.com</a>', T('+43 … (optional)')
CO_DE, ADDR_DE = 'Daniel Sheccoury', 'Gumpendorfer Straße 83–85/2/57, 1060 Wien, Österreich'
HOST = 'Cloudflare, Inc., 101 Townsend Street, San Francisco, CA 94107, USA'

# ================= IMPRINT EN =================
imprint_en = [
 ('provider', 'Responsible for this website', '<p>Information under § 5 E-Commerce Act (ECG) and disclosure under § 25 Media Act (MedienG).</p>' + kv([
   ('Name', CO), ('Project', 'ImplementAI, a consultancy in preparation (launch planned for 2027)'), ('Address', ADDR),
   ('Email', EMAIL)])),
 ('status', 'Status', '<p>ImplementAI is being prepared and is not yet a registered business. We do not offer or provide any services yet: this website collects registrations of interest for our planned launch. Before we start working with clients, we will register the business and its trade licence and update this page with the details.</p>'),
 ('media', 'Disclosure under § 25 MedienG', kv([
   ('Media owner', CO + ', ' + ADDR),
   ('Purpose', 'Preparing an AI implementation consultancy for small and medium-sized businesses in gastronomy, hospitality and wellness &amp; beauty'),
   ('Editorial line', 'Information about the planned services of ImplementAI')])),
 ('liability', 'Liability and copyright', '<p>We write the content of this website with care, but we cannot guarantee that it is complete, correct and up to date at all times. The services and prices described are planned and not yet binding offers.</p><p>We are not responsible for the content of external websites we link to. If we learn that a linked page breaks the law, we remove the link.</p><p>Texts, images and the logo on this website are protected by copyright. Please ask us before using them.</p>'),
]
imprint_de = [
 ('verantwortlich', 'Verantwortlich für diese Website', '<p>Informationen gemäß § 5 E-Commerce-Gesetz (ECG) und Offenlegung gemäß § 25 Mediengesetz (MedienG).</p>' + kv([
   ('Name', CO_DE), ('Projekt', 'ImplementAI, Beratungsunternehmen in Vorbereitung (Start für 2027 geplant)'), ('Anschrift', ADDR_DE),
   ('E-Mail', EMAIL)])),
 ('status', 'Status', '<p>ImplementAI befindet sich in Vorbereitung und ist noch kein angemeldetes Unternehmen. Wir bieten noch keine Leistungen an und erbringen keine: Diese Website sammelt Interessensbekundungen für unseren geplanten Start. Bevor wir mit Kund:innen arbeiten, melden wir das Unternehmen und die Gewerbeberechtigung an und ergänzen diese Seite um die Angaben.</p>'),
 ('medien', 'Offenlegung gemäß § 25 MedienG', kv([
   ('Medieninhaber', CO_DE + ', ' + ADDR_DE),
   ('Zweck', 'Vorbereitung eines Beratungsunternehmens für KI-Einführung in kleinen und mittleren Betrieben in Gastronomie, Hotellerie sowie Wellness &amp; Beauty'),
   ('Grundlegende Richtung', 'Information über die geplanten Leistungen von ImplementAI')])),
 ('haftung', 'Haftung und Urheberrecht', '<p>Wir erstellen die Inhalte dieser Website mit Sorgfalt, können aber nicht garantieren, dass sie jederzeit vollständig, richtig und aktuell sind. Die beschriebenen Leistungen und Preise sind geplant und noch keine verbindlichen Angebote.</p><p>Für die Inhalte externer Websites, auf die wir verlinken, sind wir nicht verantwortlich. Erfahren wir von rechtswidrigen Inhalten auf einer verlinkten Seite, entfernen wir den Link.</p><p>Texte, Bilder und das Logo dieser Website sind urheberrechtlich geschützt. Bitte fragen Sie uns, bevor Sie sie verwenden.</p>'),
]

# ================= PRIVACY EN =================
facts_en = '<div class="facts">' + ''.join(f'<div><b>{b}</b><span>{s}</span></div>' for b, s in [
  ('No cookies, no tracking', 'No analytics, no advertising pixels, no cookie banner needed.'),
  ('Only what you send us', 'We store what you enter in a form, to reply and to choose the first 10.'),
  ('Deleted on schedule', 'If we don’t launch, we delete every registration. Otherwise, those not selected 6 months after selection.'),
  ('People decide', 'Registrations are read and scored by our team, not by an automated system.')]) + '</div>'
privacy_en = [
 ('controller', 'Who is responsible', '<p>The controller under the General Data Protection Regulation (GDPR) is:</p>' + kv([('Name', CO), ('Address', ADDR), ('Email', EMAIL)]) + '<p>ImplementAI is a consultancy in preparation and not yet a registered business, so the person responsible is Daniel Sheccoury. For any question about your data, write to the address above.</p>'),
 ('website', 'Visiting this website', f'<p>When you open this website, our hosting provider ({HOST}) automatically processes the technical data your browser sends: IP address, date and time, the page requested, and browser and operating system. This is needed to deliver the website and keep it secure (legitimate interest, Art. 6(1)(f) GDPR). We do not keep these log files ourselves; Cloudflare keeps them only as long as needed for delivery and security.</p><p>The fonts are loaded from our own server, not from Google. We use no cookies, no analytics tools and no advertising pixels (such as the Meta Pixel).</p><p>If you reach the website through one of our ads, the link contains the name of the campaign (for example “utm_campaign=pilot”). If you then send a form, we store this campaign name with it so we know which ad worked. It does not identify you.</p>'),
 ('forms', 'Forms: registering your interest and contacting us', '<p>When you send a form, we receive the details you enter: name, business, email, phone (optional), industry, team size, the software you use, your description of the problem, how soon you would like it solved and whether you want the founding-client benefits. We also store the date, the page and the language of the form.</p><p>We use this to reply to you, to contact you about our launch and to choose the 10 businesses for the free Discovery Pack. The legal basis is taking steps at your request before a possible contract (Art. 6(1)(b) GDPR). You then receive a confirmation email from us.</p><p>If you tick the case study box, we may publish the findings of your Discovery as a case study, anonymously if you wish. This is based on your consent (Art. 6(1)(a) GDPR), which you can withdraw at any time by email, with effect for the future.</p><p>Giving us these details is voluntary, but without them we cannot answer your request. Please do not include health information about your clients or patients in the form.</p>'),
 ('facebook', 'Registering through Facebook or Instagram', f'<p>If you register through a form inside Facebook or Instagram, Meta Platforms Ireland Ltd. collects your answers on our behalf and passes them to us. We download them from Meta and add them to our registration list. We then process them exactly as described for the website forms. Meta’s own processing when you use Facebook or Instagram is described in <a href="https://www.facebook.com/privacy/policy">Meta’s privacy policy</a>.</p>'),
 ('email', 'Email', '<p>If you write to us by email, we use your message and address to answer you (Art. 6(1)(b) GDPR, or Art. 6(1)(f) GDPR for general questions).</p>'),
 ('recipients', 'Who else receives your data', f'<p>Only the three members of the ImplementAI team can see your details. We do not sell them or pass them on for advertising. We use these service providers, who process data on our behalf under a data processing agreement:</p><ul><li><b>Google Ireland Ltd.</b> (Google Workspace: Sheets, Gmail, Apps Script): storing registrations and sending emails</li><li><b>Cloudflare, Inc.</b>: hosting and protecting this website</li><li><b>Meta Platforms Ireland Ltd.</b>: Facebook and Instagram lead forms</li></ul><p>Some of these providers or their parent companies are based in the USA. Transfers there are covered by the EU-US Data Privacy Framework (adequacy decision under Art. 45 GDPR) or by the EU standard contractual clauses (Art. 46 GDPR).</p>'),
 ('retention', 'How long we keep your data', '<ul><li><b>If we decide not to launch:</b> all registrations and enquiries are deleted within 3 months of that decision.</li><li><b>Registrations that are not selected:</b> deleted 6 months after the selection date.</li><li><b>Enquiries that do not lead to an assignment:</b> deleted 12 months after our last contact.</li><li><b>Clients:</b> for the duration of the assignment. Invoices and accounting records are kept for 7 years, as required by Austrian tax law (§ 132 BAO).</li><li><b>Server log files:</b> not kept by us (see “Visiting this website”).</li></ul>'),
 ('decisions', 'No automated decisions', '<p>We do not make decisions about you by automated means (Art. 22 GDPR). Every registration is read and assessed by a person in our team.</p>'),
 ('rights', 'Your rights', '<p>You have the right to access your data (Art. 15 GDPR), to have it corrected (Art. 16) or deleted (Art. 17), to restrict its processing (Art. 18), to receive it in a portable format (Art. 20) and to object to processing based on our legitimate interest (Art. 21). You can withdraw consent at any time (Art. 7(3)). An email to us is enough.</p><p>If you believe we process your data unlawfully, you can complain to the Austrian Data Protection Authority: Datenschutzbehörde, Barichgasse 40–42, 1030 Vienna, <a href="mailto:dsb@dsb.gv.at">dsb@dsb.gv.at</a>, <a href="https://www.dsb.gv.at">www.dsb.gv.at</a>.</p>'),
]

facts_de = '<div class="facts">' + ''.join(f'<div><b>{b}</b><span>{s}</span></div>' for b, s in [
  ('Keine Cookies, kein Tracking', 'Keine Analyse-Tools, keine Werbe-Pixel, daher kein Cookie-Banner.'),
  ('Nur, was Sie uns schicken', 'Wir speichern Ihre Formular-Angaben, um zu antworten und die ersten 10 auszuwählen.'),
  ('Löschung nach Plan', 'Starten wir nicht, löschen wir alle Anmeldungen. Sonst nicht ausgewählte 6 Monate nach der Auswahl.'),
  ('Menschen entscheiden', 'Anmeldungen werden von unserem Team gelesen und bewertet, nicht automatisiert.')]) + '</div>'
privacy_de = [
 ('verantwortlich', 'Verantwortlicher', '<p>Verantwortlicher im Sinne der Datenschutz-Grundverordnung (DSGVO) ist:</p>' + kv([('Name', CO_DE), ('Anschrift', ADDR_DE), ('E-Mail', EMAIL)]) + '<p>ImplementAI befindet sich in Vorbereitung und ist noch kein angemeldetes Unternehmen. Verantwortlich ist daher Daniel Sheccoury. Bei Fragen zu Ihren Daten schreiben Sie an die oben genannte Adresse.</p>'),
 ('website', 'Besuch dieser Website', f'<p>Wenn Sie diese Website aufrufen, verarbeitet unser Hosting-Anbieter (Cloudflare, Inc., 101 Townsend Street, San Francisco, CA 94107, USA) automatisch die technischen Daten, die Ihr Browser übermittelt: IP-Adresse, Datum und Uhrzeit, aufgerufene Seite sowie Browser und Betriebssystem. Das ist nötig, um die Website auszuliefern und sicher zu betreiben (berechtigtes Interesse, Art. 6 Abs. 1 lit. f DSGVO). Wir speichern diese Protokolldateien nicht selbst; Cloudflare bewahrt sie nur so lange auf, wie es für Auslieferung und Sicherheit nötig ist.</p><p>Die Schriften werden von unserem eigenen Server geladen, nicht von Google. Wir verwenden keine Cookies, keine Analyse-Tools und keine Werbe-Pixel (wie das Meta-Pixel).</p><p>Kommen Sie über eine unserer Anzeigen auf die Website, enthält der Link den Namen der Kampagne (z. B. „utm_campaign=pilot“). Senden Sie danach ein Formular ab, speichern wir diesen Kampagnennamen mit, damit wir wissen, welche Anzeige funktioniert hat. Er lässt keinen Rückschluss auf Ihre Person zu.</p>'),
 ('formulare', 'Formulare: Interesse anmelden und Kontakt', '<p>Wenn Sie ein Formular absenden, erhalten wir Ihre Angaben: Name, Betrieb, E-Mail, Telefon (freiwillig), Branche, Teamgröße, die Software, die Sie nutzen, Ihre Beschreibung des Problems, bis wann Sie es gelöst haben möchten und ob Sie die Vorteile als Gründungskund:in wünschen. Außerdem speichern wir Datum, Seite und Sprache des Formulars.</p><p>Wir verwenden diese Daten, um Ihnen zu antworten, Sie über unseren Start zu informieren und die 10 Betriebe für das kostenlose Analyse-Paket auszuwählen. Rechtsgrundlage ist die Durchführung vorvertraglicher Maßnahmen auf Ihre Anfrage (Art. 6 Abs. 1 lit. b DSGVO). Sie erhalten anschließend eine Bestätigung per E-Mail.</p><p>Wenn Sie das Kästchen zur Fallstudie ankreuzen, dürfen wir die Ergebnisse Ihrer Analyse als Fallstudie veröffentlichen, auf Wunsch anonym. Grundlage ist Ihre Einwilligung (Art. 6 Abs. 1 lit. a DSGVO), die Sie jederzeit per E-Mail mit Wirkung für die Zukunft widerrufen können.</p><p>Die Angabe der Daten ist freiwillig, ohne sie können wir Ihre Anfrage aber nicht bearbeiten. Bitte geben Sie im Formular keine Gesundheitsdaten Ihrer Kund:innen oder Patient:innen an.</p>'),
 ('facebook', 'Anmeldung über Facebook oder Instagram', f'<p>Melden Sie sich über ein Formular in Facebook oder Instagram an, erhebt Meta Platforms Ireland Ltd. Ihre Antworten in unserem Auftrag und übermittelt sie an uns. Wir laden sie bei Meta herunter und übernehmen sie in unsere Anmeldeliste und verarbeiten sie dann genau wie bei den Website-Formularen. Wie Meta selbst Daten verarbeitet, wenn Sie Facebook oder Instagram nutzen, steht in der <a href="https://www.facebook.com/privacy/policy">Datenschutzrichtlinie von Meta</a>.</p>'),
 ('email', 'E-Mail', '<p>Wenn Sie uns per E-Mail schreiben, verwenden wir Ihre Nachricht und Adresse, um Ihnen zu antworten (Art. 6 Abs. 1 lit. b DSGVO, bei allgemeinen Fragen Art. 6 Abs. 1 lit. f DSGVO).</p>'),
 ('empfaenger', 'Wer Ihre Daten noch erhält', f'<p>Ihre Angaben sehen nur die drei Mitglieder des ImplementAI-Teams. Wir verkaufen sie nicht und geben sie nicht für Werbung weiter. Wir setzen folgende Dienstleister ein, die Daten in unserem Auftrag auf Grundlage eines Auftragsverarbeitungsvertrags verarbeiten:</p><ul><li><b>Google Ireland Ltd.</b> (Google Workspace: Sheets, Gmail, Apps Script): Speicherung der Anmeldungen und Versand der E-Mails</li><li><b>Cloudflare, Inc.</b>: Hosting und Schutz dieser Website</li><li><b>Meta Platforms Ireland Ltd.</b>: Lead-Formulare in Facebook und Instagram</li></ul><p>Einige dieser Anbieter oder ihre Muttergesellschaften haben ihren Sitz in den USA. Übermittlungen dorthin sind durch das EU-US Data Privacy Framework (Angemessenheitsbeschluss nach Art. 45 DSGVO) oder durch EU-Standardvertragsklauseln (Art. 46 DSGVO) abgesichert.</p>'),
 ('speicherdauer', 'Wie lange wir Ihre Daten speichern', '<ul><li><b>Wenn wir nicht starten:</b> Löschung aller Anmeldungen und Anfragen innerhalb von 3 Monaten nach dieser Entscheidung.</li><li><b>Nicht ausgewählte Anmeldungen:</b> Löschung 6 Monate nach dem Auswahltermin.</li><li><b>Anfragen ohne Auftrag:</b> Löschung 12 Monate nach dem letzten Kontakt.</li><li><b>Kund:innen:</b> für die Dauer des Auftrags. Rechnungen und Buchhaltungsunterlagen bewahren wir 7 Jahre auf, wie es das österreichische Steuerrecht verlangt (§ 132 BAO).</li><li><b>Server-Protokolldateien:</b> speichern wir nicht selbst (siehe „Besuch dieser Website“).</li></ul>'),
 ('entscheidungen', 'Keine automatisierten Entscheidungen', '<p>Wir treffen keine automatisierten Entscheidungen über Sie (Art. 22 DSGVO). Jede Anmeldung wird von einer Person aus unserem Team gelesen und bewertet.</p>'),
 ('rechte', 'Ihre Rechte', '<p>Sie haben das Recht auf Auskunft (Art. 15 DSGVO), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung der Verarbeitung (Art. 18), Datenübertragbarkeit (Art. 20) und Widerspruch gegen Verarbeitungen auf Grundlage unseres berechtigten Interesses (Art. 21). Eine Einwilligung können Sie jederzeit widerrufen (Art. 7 Abs. 3). Eine E-Mail an uns genügt.</p><p>Wenn Sie meinen, dass wir Ihre Daten unrechtmäßig verarbeiten, können Sie sich bei der österreichischen Datenschutzbehörde beschweren: Datenschutzbehörde, Barichgasse 40–42, 1030 Wien, <a href="mailto:dsb@dsb.gv.at">dsb@dsb.gv.at</a>, <a href="https://www.dsb.gv.at">www.dsb.gv.at</a>.</p>'),
]

DN_EN = ''  # set a note here to show the green draft banner again
DN_DE = ''
pages = {
 'imprint.html': page('en', 'Imprint', 'Legal', 'Imprint', 'Who is responsible for this website, as required by Austrian law.', imprint_en, 'impressum.html', 'DE', '../../index.html', DN_EN, 'On this page', 'Last updated: 20 November 2026'),
 'impressum.html': page('de', 'Impressum', 'Rechtliches', 'Impressum', 'Wer für diese Website verantwortlich ist, wie es das österreichische Recht verlangt.', imprint_de, 'imprint.html', 'EN', '../../de/index.html', DN_DE, 'Auf dieser Seite', 'Stand: 20. November 2026'),
 'privacy.html': page('en', 'Privacy policy', 'Legal', 'Privacy <i>policy</i>', 'What we do with your details when you visit this website or register your interest, in plain language.', privacy_en, 'datenschutz.html', 'DE', '../../index.html', DN_EN, 'On this page', 'Last updated: 20 November 2026', before=facts_en),
 'datenschutz.html': page('de', 'Datenschutzerklärung', 'Rechtliches', 'Daten<i>schutz</i>', 'Was wir mit Ihren Daten machen, wenn Sie diese Website besuchen oder Ihr Interesse anmelden, in verständlicher Sprache.', privacy_de, 'privacy.html', 'EN', '../../de/index.html', DN_DE, 'Auf dieser Seite', 'Stand: 20. November 2026', before=facts_de),
}
import re as _re
ROOT = os.path.join(HERE, '..', '..')
FAV = _re.search(r'<link rel="icon"[^>]*>', open(os.path.join(ROOT, 'index.html')).read()).group(0)
for name, html in pages.items():
    open(os.path.join(HERE, name), 'w').write(html)
    # Production copy: English pages at the root, German pages in de/, fonts self-hosted.
    de = name in ('impressum.html', 'datenschutz.html')
    out = html.replace('<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Newsreader:ital,opsz,wght@0,6..72,400;1,6..72,400&display=swap" rel="stylesheet">\n', FAV + '\n')
    out = out.replace('../../assets', '../assets' if de else 'assets').replace('../../de/index.html', 'index.html').replace('../../index.html', 'index.html')
    pairs = {'imprint.html': 'impressum.html', 'privacy.html': 'datenschutz.html'}
    for en, dd in pairs.items():
        if de: out = out.replace(f'href="{en}"', f'href="../{en}"')
        else: out = out.replace(f'href="{dd}"', f'href="de/{dd}"')
    out = out.replace('© 2026 ImplementAI', '© 2026 ImplementAI · <a href="index.html">' + ('Zur Website' if de else 'Main website') + '</a>')
    open(os.path.join(ROOT, 'de' if de else '', name), 'w').write(out)
print('ok', list(pages))
