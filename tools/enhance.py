#!/usr/bin/env python3
"""City One v8 – tüm TR/EN sayfalara SEO, güven, erişilebilirlik ve içerik katmanını uygular.
Idempotent: tekrar çalıştırmak güvenlidir.  Kullanım: python3 tools/enhance.py
SITE değişkenini gerçek alan adıyla değiştirip yeniden çalıştırın."""
import os, re, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://www.cityonekayseri.com'          # <- GERÇEK ALAN ADINI YAZIN
WA = '905067520286'

PAGES = [('index.html','en/index.html','Ana Sayfa','Home'),
         ('odalar.html','en/rooms.html','Odalar','Rooms'),
         ('olanaklar.html','en/spa.html','Spa & Olanaklar','Spa & Facilities'),
         ('restoran.html','en/restaurant.html','Restoran','Restaurant'),
         ('salonlar.html','en/halls.html','Etkinlik Salonları','Event Halls'),
         ('galeri.html','en/gallery.html','Galeri','Gallery'),
         ('iletisim.html','en/contact.html','İletişim','Contact'),
         ('kvkk.html','en/legal.html','KVKK','Legal')]

P = {  # ikonlar
 'pin':'M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12zM12 12a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z',
 'pool':'M2 17c2 0 2-1.5 5-1.5s3 1.5 5 1.5 3-1.5 5-1.5 3 1.5 5 1.5M2 21c2 0 2-1.5 5-1.5s3 1.5 5 1.5 3-1.5 5-1.5 3 1.5 5 1.5M8 14V5a2 2 0 0 1 4 0M14 14V5a2 2 0 0 1 4 0M8 9h6',
 'users':'M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8',
 'bell':'M3 18h18M5 18a7 7 0 0 1 14 0M12 8V6M10 6h4',
 'ski':'M3 20l18-5M7 6a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM8 8l4 3 4 1M12 11l-2 5',
 'cup':'M4 8h13v5a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5V8zM17 9h2a2 2 0 0 1 0 5h-2M7 2v3M11 2v3M15 2v3',
 'castle':'M3 21V9l3 2V6l3 2V4h6v4l3-2v5l3-2v12zM10 21v-5h4v5',
 'mount':'M2 20l7-13 4 7 3-4 6 10z',
 'phone':'M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z',
 'cal':'M3 5h18v16H3zM3 10h18M8 2v4M16 2v4',
 'arrow':'M5 12h14M13 5l7 7-7 7',
 'mail':'M3 5h18v14H3zM3 6l9 7 9-7',
}
def ic(n): return f'<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="{P[n]}"/></svg>'
WA_PATH = re.search(r'wa-ic[^>]*><path fill="currentColor" stroke="none" d="([^"]+)"',
                    open(os.path.join(ROOT,'index.html'),encoding='utf-8').read()).group(1)
WA_IC = f'<svg class="ic wa-ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" stroke="none" d="{WA_PATH}"/></svg>'

# ----------------------------------------------------------------- METİNLER
T = {'tr': dict(
 why_e='Neden City One', why_h='Konaklamanızı farklı kılan dört şey',
 why_p='Kayseri\'de iş de olsa tatil de olsa, ihtiyacınız olan her şey tek çatı altında.',
 why=[('pin','Şehrin merkezinde','Kayseri\'de iş ve gezi programınıza yakın, ulaşımı kolay bir konum.'),
      ('pool','Spa\'ya ücretsiz erişim','Yarı olimpik havuz, hamam, sauna ve fitness tüm konuklarımıza ücretsiz.'),
      ('users','750 kişiye kadar organizasyon','Altı etkinlik salonu ve Sini Restoran ile düğünden toplantıya her ölçek.'),
      ('bell','7/24 hizmet','Gece gündüz oda servisi ve girişte vale karşılama.')],
 disc_e='Kayseri\'yi keşfedin', disc_h='Şehir, tarih ve doğa bir arada',
 disc_p='Konaklamanızı Kayseri\'nin öne çıkan rotalarıyla birleştirin; önerilerimiz için resepsiyonumuza danışın.',
 disc=[('ski','Erciyes Kayak Merkezi','Kış aylarında Türkiye\'nin önemli kayak merkezlerinden biri.'),
       ('castle','Tarihi Kayseri','Kayseri Kalesi, Selçuklu eserleri ve tarihi çarşılar.'),
       ('mount','Kapadokya\'ya kapı','Kapadokya rotasına yaptığınız gezilerde konforlu bir üs.'),
       ('cup','Kayseri lezzetleri','Mantı, pastırma ve sucuk gibi yöre lezzetleri.')],
 info=[('Giriş (check-in)','14:00'),('Çıkış (check-out)','12:00'),('Kahvaltı','07:00 – 10:00'),('Oda servisi','7/24')],
 faq_e='Sık sorulan sorular', faq_h='Aklınızdaki sorular',
 faq=[('Nasıl rezervasyon yapabilirim?','Telefonla (0352 207 00 00), WhatsApp\'tan (0506 752 02 86), bu sayfadaki form veya e-posta (info@cityonekayseri.com) ile bize ulaşabilirsiniz. Tarih ve kişi sayınızı iletmeniz yeterli; müsaitlik ve fiyat bilgisini hemen paylaşırız.'),
      ('Kahvaltı saatleri nedir?','Zengin açık büfe kahvaltımız her sabah 07:00 – 10:00 arasında servis edilir.'),
      ('Spa ve havuz konuklar için ücretsiz mi?','Evet. Konuklarımız yarı olimpik havuz, jakuzi, Türk hamamı, Fin hamamı, sauna ve fitness alanlarından ücretsiz yararlanır. Spa hafta içi 09:00 – 23:00, hafta sonu 09:00 – 21:00 açıktır.'),
      ('Wi-Fi ücretsiz mi?','Evet, otelin tamamında ücretsiz Wi-Fi sunuyoruz.'),
      ('Oda servisi var mı?','Evet, oda servisimiz 7 gün 24 saat hizmet verir.'),
      ('Otopark veya vale hizmeti var mı?','Girişte vale hizmetimiz bulunmaktadır.'),
      ('Düğün veya toplantı için salon ayırtabilir miyim?','Elbette. Altı etkinlik salonumuz ve 750 kişiye kadar kapasiteli Sini Restoran ile düğün, nişan, kına, toplantı ve kurumsal organizasyonlara ev sahipliği yapıyoruz. Tarih ve kişi sayınızı iletin, size özel teklif hazırlayalım.')],
 mbar=('Ara','WhatsApp','Rezervasyon'), top='Yukarı çık', no='Reddet', ok='Kabul et',
 mail_alt='Mesajınızı e-posta ile göndermek için', mail_btn='E-posta ile gönder',
 ),
 'en': dict(
 why_e='Why City One', why_h='Four things that set your stay apart',
 why_p='Whether you are in Kayseri for business or leisure, everything you need is under one roof.',
 why=[('pin','In the city centre','A location close to your business and sightseeing plans in Kayseri, easy to reach.'),
      ('pool','Complimentary spa access','Semi-Olympic pool, hammam, sauna and fitness are free for all guests.'),
      ('users','Events up to 750 guests','Six event halls and Sini Restaurant host everything from weddings to meetings.'),
      ('bell','24/7 service','Round-the-clock room service and valet welcome at the entrance.')],
 disc_e='Discover Kayseri', disc_h='City, history and nature in one trip',
 disc_p='Combine your stay with Kayseri\'s highlights; ask our reception for recommendations.',
 disc=[('ski','Erciyes Ski Resort','One of Türkiye\'s notable ski resorts in the winter months.'),
       ('castle','Historic Kayseri','Kayseri Castle, Seljuk monuments and historic bazaars.'),
       ('mount','Gateway to Cappadocia','A comfortable base for your trips along the Cappadocia route.'),
       ('cup','Kayseri flavours','Local specialities such as mantı, pastırma and sucuk.')],
 info=[('Check-in','14:00'),('Check-out','12:00'),('Breakfast','07:00 – 10:00'),('Room service','24/7')],
 faq_e='FAQ', faq_h='Frequently asked questions',
 faq=[('How can I make a reservation?','Call us (+90 352 207 00 00), message us on WhatsApp (+90 506 752 02 86), use the form on this page or email info@cityonekayseri.com. Just send your dates and number of guests and we will share availability and rates right away.'),
      ('What are the breakfast hours?','Our rich open buffet breakfast is served every morning from 07:00 to 10:00.'),
      ('Are the spa and pool free for guests?','Yes. Guests enjoy the semi-Olympic pool, jacuzzi, Turkish hammam, Finnish hammam, sauna and fitness areas free of charge. The spa is open 09:00 – 23:00 on weekdays and 09:00 – 21:00 on weekends.'),
      ('Is Wi-Fi free?','Yes, we offer free Wi-Fi throughout the hotel.'),
      ('Is room service available?','Yes, room service is available 24 hours a day, 7 days a week.'),
      ('Is there parking or valet service?','Valet service is available at the entrance.'),
      ('Can I book a hall for a wedding or a meeting?','Of course. With six event halls and Sini Restaurant (up to 750 guests) we host weddings, engagements, henna nights, meetings and corporate events. Send your date and guest count and we will prepare a tailored offer.')],
 mbar=('Call','WhatsApp','Book'), top='Back to top', no='Decline', ok='Accept',
 mail_alt='', mail_btn='Send by email',
 )}

def esc(s): return s.replace('&','&amp;').replace('"','&quot;')

def home_sections(L):
    t = T[L]
    why = ''.join(f'<div class="why-i reveal">{ic(i)}<h3>{h}</h3><p>{p}</p></div>' for i,h,p in t['why'])
    disc = ''.join(f'<div class="disc reveal">{ic(i)}<h3>{h}</h3><p>{p}</p></div>' for i,h,p in t['disc'])
    return (f'<section class="why"><div class="wrap"><div class="sec-h reveal"><span class="eyebrow lt">{t["why_e"]}</span><h2>{t["why_h"]}</h2><p>{t["why_p"]}</p></div>'
            f'<div class="why-g">{why}</div></div></section>\n\n',
            f'<section class="sec sec-sand"><div class="wrap"><div class="sec-h"><span class="eyebrow">{t["disc_e"]}</span><h2>{t["disc_h"]}</h2><p>{t["disc_p"]}</p></div>'
            f'<div class="disc-g">{disc}</div></div></section>\n\n')

def faq_section(L):
    t = T[L]
    info = ''.join(f'<div class="info-t reveal"><span>{a}</span><strong>{b}</strong></div>' for a,b in t['info'])
    items = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in t['faq'])
    return (f'<section class="sec sec-sand faq" id="sss"><div class="wrap"><div class="info-g">{info}</div>'
            f'<div class="sec-h"><span class="eyebrow">{t["faq_e"]}</span><h2>{t["faq_h"]}</h2></div><div class="faq-list">{items}</div></div></section>')

def faq_ld(L):
    return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in T[L]['faq']]}

def wa_href(L):
    from urllib.parse import quote
    msg = 'Merhaba, City One Hotel & Spa hakkında bilgi almak istiyorum.' if L=='tr' else 'Hello, I would like information about City One Hotel & Spa.'
    return f'https://wa.me/{WA}?text={quote(msg)}'

def ld_tag(obj): return '<script type="application/ld+json">'+json.dumps(obj,ensure_ascii=False)+'</script>'

def process(tr_file, en_file, tr_name, en_name, L):
    f = tr_file if L=='tr' else en_file
    path = os.path.join(ROOT, f)
    h = open(path, encoding='utf-8').read()
    pre = '' if L=='tr' else '../'          # asset öneki
    me, other = (tr_file, en_file) if L=='tr' else (en_file, tr_file)
    url_me, url_tr, url_en = f'{SITE}/{me}', f'{SITE}/{tr_file}', f'{SITE}/{en_file}'
    t = T[L]

    # ---- 0) temizle (idempotent) ----
    h = re.sub(r'<link rel="alternate"[^>]*>', '', h)
    h = re.sub(r'<!--c1:head-->.*?<!--/c1:head-->', '', h, flags=re.S)
    h = re.sub(r'<!--c1:body-->.*?<!--/c1:body-->', '', h, flags=re.S)
    h = re.sub(r'<section class="why">.*?</section>\n\n', '', h, flags=re.S)
    h = re.sub(r'<section class="sec sec-sand"><div class="wrap"><div class="sec-h"><span class="eyebrow">(?:Kayseri\'yi keşfedin|Discover Kayseri)</span>.*?</section>\n\n', '', h, flags=re.S)
    h = re.sub(r'<section class="sec sec-sand faq".*?</section>', '', h, flags=re.S)
    h = h.replace('<meta property="og:image" content="assets/img/','<meta property="og:image" content="'+SITE+'/assets/img/')
    h = re.sub(r'<meta property="og:image" content="(?!http)(?:\.\./)?assets/img/', '<meta property="og:image" content="'+SITE+'/assets/img/', h)

    title = re.search(r'<title>(.*?)</title>', h, re.S).group(1)
    desc = re.search(r'<meta name="description" content="([^"]*)"', h).group(1)
    ogimg = re.search(r'<meta property="og:image" content="([^"]*)"', h).group(1)

    # ---- 1) HEAD ----
    ld = []
    if tr_file != 'index.html':
        ld.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
            {"@type":"ListItem","position":1,"name":'Ana Sayfa' if L=='tr' else 'Home',"item":f'{SITE}/{"index.html" if L=="tr" else "en/index.html"}'},
            {"@type":"ListItem","position":2,"name":tr_name if L=='tr' else en_name,"item":url_me}]})
    if tr_file == 'iletisim.html': ld.append(faq_ld(L))
    head = ('<!--c1:head-->'
      f'<link rel="canonical" href="{url_me}">'
      f'<link rel="alternate" hreflang="tr" href="{url_tr}"><link rel="alternate" hreflang="en" href="{url_en}"><link rel="alternate" hreflang="x-default" href="{url_tr}">'
      f'<meta property="og:url" content="{url_me}"><meta property="og:site_name" content="City One Hotel &amp; Spa">'
      f'<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{ogimg}">'
      f'<link rel="apple-touch-icon" href="{pre}assets/logo.png"><link rel="manifest" href="{pre}site.webmanifest">'
      f'<link rel="stylesheet" href="{pre}assets/extra.css">'
      + ''.join(ld_tag(o) for o in ld) + '<!--/c1:head-->')
    h = h.replace('</head>', head + '</head>', 1)

    # Hotel JSON-LD (ana sayfa): mutlak URL + ek alanlar
    def fix_hotel(m):
        d = json.loads(m.group(1))
        d.update({"url": f'{SITE}/{me}', "image": [f'{SITE}/assets/img/otel-hava-gunduz.webp', f'{SITE}/assets/img/otel-giris-gece.webp', f'{SITE}/assets/img/havuz.webp'],
                  "logo": f'{SITE}/assets/logo.png', "priceRange": None, "hasMap": "https://www.google.com/maps?q=City+One+Hotel+Eski+Sanayi+Bölgesi+2.+Cadde+No+11+Kayseri",
                  "inLanguage": L, "petsAllowed": None})
        d = {k:v for k,v in d.items() if v is not None}
        d["address"]["addressRegion"] = "Kayseri"
        return ld_tag(d)
    h = re.sub(r'<script type="application/ld\+json">(\{"@context": "https://schema.org", "@type": "Hotel".*?)</script>', fix_hotel, h, count=1, flags=re.S)
    h = re.sub(r'<script type="application/ld\+json">(\{"@context":"https://schema.org","@type":"Hotel".*?)</script>', fix_hotel, h, count=1, flags=re.S)

    # ---- 2) ana sayfa bölümleri ----
    if tr_file == 'index.html':
        a, b = home_sections(L)
        h = h.replace('<section class="sec tour">', a + '<section class="sec tour">', 1)
        h = h.replace('<section class="sec"><div class="wrap cols2">', b + '<section class="sec"><div class="wrap cols2">', 1)

    # ---- 3) iletişim: bilgi + SSS, e-posta butonu ----
    if tr_file == 'iletisim.html':
        h = h.replace('</section></main>', '</section>' + faq_section(L) + '</main>', 1)
        if 'id="mailSend"' not in h:
            h = re.sub(r'(<button class="btn btn-or" type="submit">.*?</button>)(<p class="err")',
                       r'\1<button class="btn btn-line btn-mail" type="button" id="mailSend">'+ic('mail')+' '+t['mail_btn']+r'</button>\2', h, count=1, flags=re.S)
        h = h.replace('<p class="err" id="ferr" hidden>', '<p class="err" id="ferr" role="alert" hidden>')

    # ---- 4) erişilebilirlik: aria-current ----
    cur = os.path.basename(f)
    h = re.sub(r'<a href="%s" class=active>' % re.escape(cur), '<a href="%s" class="active" aria-current="page">' % cur, h)
    h = re.sub(r'<a class="active" href="%s">' % re.escape(cur), '<a class="active" aria-current="page" href="%s">' % cur, h)

    # ---- 5) çerez: reddet ----
    h = re.sub(r'<button class="btn btn-or" id="cookieOk">([^<]*)</button>',
               lambda m: f'<span class="ck-b"><button class="btn btn-line" id="cookieNo" type="button">{t["no"]}</button><button class="btn btn-or" id="cookieOk" type="button">{m.group(1)}</button></span>', h)

    # ---- 6) BODY: mobil çubuk + yukarı ----
    hrefs = {'call':'tel:+903522070000', 'wa':wa_href(L), 'book': ('iletisim.html#rezervasyon' if L=='tr' else 'contact.html#rezervasyon')}
    body = ('<!--c1:body-->'
      f'<nav class="mbar" aria-label="{"Hızlı iletişim" if L=="tr" else "Quick contact"}"><a href="{hrefs["call"]}">{ic("phone")} {t["mbar"][0]}</a>'
      f'<a href="{hrefs["wa"]}" target="_blank" rel="noopener">{WA_IC} {t["mbar"][1]}</a><a class="mb-or" href="{hrefs["book"]}">{ic("cal")} {t["mbar"][2]}</a></nav>'
      f'<button type="button" class="totop" id="totop" aria-label="{t["top"]}"><svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="{P["arrow"]}"/></svg></button>'
      '<!--/c1:body-->')
    h = h.replace('<script src="%sassets/main.js" defer></script>' % pre, body + '<script src="%sassets/main.js" defer></script>' % pre, 1)
    h = re.sub(r'<script src="[^"]*assets/extra\.js" defer></script>', '', h)
    h = h.replace('</body>', f'<script src="{pre}assets/extra.js" defer></script></body>', 1)

    open(path, 'w', encoding='utf-8').write(h)

for tr_f, en_f, trn, enn in PAGES:
    process(tr_f, en_f, trn, enn, 'tr')
    process(tr_f, en_f, trn, enn, 'en')

# ---- sitemap, robots, manifest ----
urls = []
for tr_f, en_f, _, _ in PAGES:
    urls.append(f'  <url><loc>{SITE}/{tr_f}</loc><xhtml:link rel="alternate" hreflang="tr" href="{SITE}/{tr_f}"/><xhtml:link rel="alternate" hreflang="en" href="{SITE}/{en_f}"/></url>')
    urls.append(f'  <url><loc>{SITE}/{en_f}</loc><xhtml:link rel="alternate" hreflang="tr" href="{SITE}/{tr_f}"/><xhtml:link rel="alternate" hreflang="en" href="{SITE}/{en_f}"/></url>')
open(os.path.join(ROOT,'sitemap.xml'),'w',encoding='utf-8').write(
  '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'+'\n'.join(urls)+'\n</urlset>\n')
open(os.path.join(ROOT,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
open(os.path.join(ROOT,'site.webmanifest'),'w',encoding='utf-8').write(json.dumps({
  "name":"City One Hotel & Spa","short_name":"City One","start_url":"index.html","display":"browser",
  "background_color":"#17100c","theme_color":"#2a1d17","icons":[{"src":"assets/favicon.png","sizes":"any","type":"image/png"}]},ensure_ascii=False,indent=1))
print('tamam')
