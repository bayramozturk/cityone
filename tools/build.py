#!/usr/bin/env python3
"""City One Hotel & Spa - statik site üretici. Çalıştır: python3 tools/build.py"""
import os, json
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEL = '0352 207 00 00'; TEL_RAW = '+903522070000'
WA = '0506 752 02 86'; WA_RAW = '905067520286'
MAIL = 'info@cityonekayseri.com'
ADDR = 'Eski Sanayi Bölgesi 2. Cadde No: 11, Kayseri / Türkiye'
MAPQ = 'City One Hotel Eski Sanayi Bölgesi 2. Cadde No 11 Kayseri'

_sz = {}
def size(path):
    if path not in _sz:
        _sz[path] = Image.open(os.path.join(ROOT, path)).size
    return _sz[path]

def img(name, alt, cls='', thumb=False, lazy=True, sizes=''):
    p = f"assets/{'thumb' if thumb else 'img'}/{name}.webp"
    w, h = size(p)
    return (f'<img src="{p}" width="{w}" height="{h}" alt="{alt}"'
            f'{" class=%s" % chr(34)+cls+chr(34) if cls else ""}'
            f'{" loading=lazy" if lazy else ""} decoding="async">')

def lb(name, alt, group, cls='', thumb=True):
    return (f'<a href="assets/img/{name}.webp" class="lb" data-lb="{group}" data-caption="{alt}">'
            f'{img(name, alt, cls, thumb)}</a>')

ICONS = {
 'wifi':'M5 12.55a11 11 0 0 1 14 0M8.5 16.05a6 6 0 0 1 7 0M12 20h.01M1.42 9a16 16 0 0 1 21.16 0',
 'cup':'M4 8h13v5a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5V8zM17 9h2a2 2 0 0 1 0 5h-2M7 2v3M11 2v3M15 2v3',
 'drop':'M12 2.5s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z',
 'iron':'M3 18h18v2H3zM3 18c0-6 3-10 8-10h6a4 4 0 0 1 4 4v6M9 13h.01M13 13h.01',
 'fridge':'M6 2h12v20H6zM6 10h12M9 5v2M9 13v4',
 'car':'M3 13l2-6h14l2 6M3 13v5h3v-2h12v2h3v-5M3 13h18M7 16h.01M17 16h.01',
 'bell':'M3 18h18M5 18a7 7 0 0 1 14 0M12 8V6M10 6h4',
 'pool':'M2 17c2 0 2-1.5 5-1.5s3 1.5 5 1.5 3-1.5 5-1.5 3 1.5 5 1.5M2 21c2 0 2-1.5 5-1.5s3 1.5 5 1.5 3-1.5 5-1.5 3 1.5 5 1.5M8 14V5a2 2 0 0 1 4 0M14 14V5a2 2 0 0 1 4 0M8 9h6',
 'steam':'M8 21c-2-2 2-4 0-6s2-4 0-6M13 21c-2-2 2-4 0-6s2-4 0-6M18 21c-2-2 2-4 0-6s2-4 0-6',
 'therm':'M14 14.8V4a2 2 0 0 0-4 0v10.8a4 4 0 1 0 4 0z',
 'dumb':'M6 6v12M18 6v12M3 9v6M21 9v6M6 12h12',
 'jac':'M3 14h18v2a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4v-2zM8 10h.01M12 7h.01M16 10h.01M12 11h.01',
 'glass':'M6 3h12l-1.5 17a2 2 0 0 1-2 1.8h-5a2 2 0 0 1-2-1.8L6 3zM7 9h10',
 'phone':'M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z',
 'pin':'M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12zM12 12a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z',
 'clock':'M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zM12 6v6l4 2',
 'mail':'M3 5h18v14H3zM3 6l9 7 9-7',
 'check':'M20 6L9 17l-5-5',
 'arrow':'M5 12h14M13 5l7 7-7 7',
 'ruler':'M3 17L17 3l4 4L7 21zM8 12l2 2M11 9l2 2M14 6l2 2',
 'users':'M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8',
 'cal':'M3 5h18v16H3zM3 10h18M8 2v4M16 2v4',
 'play':'M6 4l14 8-14 8z',
 'ski':'M3 20l18-5M7 6a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM8 8l4 3 4 1M12 11l-2 5',
 'menu':'M3 6h18M3 12h18M3 18h18',
 'x':'M18 6L6 18M6 6l12 12',
}
def ic(n, cls='ic'):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true"><path d="{ICONS[n]}"/></svg>'

WA_PATH = 'M20.5 3.5A11 11 0 0 0 3.4 17.1L2 22l5-1.3A11 11 0 1 0 20.5 3.5zM12 20.2a9.100 9.100 0 0 1-4.700-1.300l-.3-.2-3 .8.8-2.900-.2-.3A9.100 9.100 0 1 1 12 20.200zm5-6.800c-.3-.1-1.600-.8-1.900-.9s-.5-.1-.6.1l-.9 1.100c-.2.2-.3.2-.6.1a7.400 7.400 0 0 1-3.700-3.200c-.3-.5.3-.5.8-1.500.1-.2 0-.3 0-.5l-.9-2.100c-.2-.5-.5-.5-.6-.5h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.200c0 1.300.9 2.500 1 2.700s1.800 2.800 4.400 3.900c1.600.7 2.300.7 3.100.6.500-.1 1.600-.7 1.800-1.300.2-.6.2-1.100.2-1.200-.1-.1-.3-.2-.6-.3z'
WA_SVG = f'<svg class="ic wa-ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" stroke="none" d="{WA_PATH}"/></svg>'

def wa_link(msg='Merhaba, City One Hotel & Spa hakkında bilgi almak istiyorum.'):
    from urllib.parse import quote
    return f'https://wa.me/{WA_RAW}?text={quote(msg)}'

NAV = [('odalar.html','Odalar'),('olanaklar.html','Spa & Olanaklar'),('restoran.html','Restoran'),
       ('salonlar.html','Etkinlik Salonları'),('galeri.html','Galeri'),('iletisim.html','İletişim')]

def head(title, desc, page, og='otel-hava-gunduz'):
    return f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#2a1d17">
<meta property="og:type" content="website"><meta property="og:locale" content="tr_TR">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/{og}.webp">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body data-page="{page}">
<a class="skip" href="#icerik">İçeriğe geç</a>
'''

def header(page):
    links = ''.join(f'<a href="{h}"{" class=active" if h==page else ""}>{t}</a>' for h,t in NAV)
    return f'''<div class="topbar"><div class="wrap">
  <span>{ic('pin')} Kayseri / Türkiye</span>
  <span class="tb-r"><a href="tel:{TEL_RAW}">{ic('phone')} {TEL}</a><a href="{wa_link()}" target="_blank" rel="noopener">{WA_SVG} WhatsApp: {WA}</a></span>
</div></div>
<header class="hdr" id="hdr"><div class="wrap hdr-in">
  <a class="brand" href="index.html" aria-label="City One Hotel & Spa - Ana Sayfa"><img src="assets/logo.png" width="600" height="395" alt="City One Hotel & Spa logosu"></a>
  <nav class="nav" id="nav" aria-label="Ana menü">{links}</nav>
  <a class="btn btn-or hdr-cta" href="iletisim.html#rezervasyon">Rezervasyon</a>
  <button class="burger" id="burger" aria-label="Menüyü aç" aria-expanded="false" aria-controls="nav">{ic('menu')}</button>
</div></header>
<main id="icerik">
'''

def footer():
    return f'''</main>
<section class="cta-band"><div class="wrap">
  <div><h2>Konaklamanızı Planlayalım</h2><p>Rezervasyon, grup ve etkinlik talepleriniz için bize hemen ulaşın.</p></div>
  <div class="cta-btns"><a class="btn btn-or" href="tel:{TEL_RAW}">{ic('phone')} {TEL}</a>
  <a class="btn btn-wa" href="{wa_link()}" target="_blank" rel="noopener">{WA_SVG} WhatsApp ile Yazın</a></div>
</div></section>
<footer class="ftr"><div class="wrap ftr-grid">
  <div><img class="ftr-logo" src="assets/logo.png" width="600" height="395" alt="City One Hotel & Spa" loading="lazy">
   <p>Kayseri'de 4 yıldızlı konfor: ferah odalar, spa & wellness, zengin açık büfe kahvaltı ve etkinlik salonları.</p></div>
  <div><h3>Keşfedin</h3><ul>{''.join(f'<li><a href="{h}">{t}</a></li>' for h,t in NAV)}</ul></div>
  <div><h3>İletişim</h3><ul class="ci">
   <li>{ic('pin')}<span>{ADDR}</span></li>
   <li>{ic('phone')}<a href="tel:{TEL_RAW}">{TEL}</a></li>
   <li>{WA_SVG}<a href="{wa_link()}" target="_blank" rel="noopener">{WA}</a></li>
   <li>{ic('mail')}<a href="mailto:{MAIL}">{MAIL}</a></li></ul></div>
  <div><h3>Saatler</h3><ul class="ci">
   <li>{ic('cup')}<span>Kahvaltı 07:00 – 10:00</span></li>
   <li>{ic('bell')}<span>Oda servisi 7/24</span></li>
   <li>{ic('pool')}<span>Spa 09:00 – 23:00 (hafta sonu 21:00)</span></li></ul></div>
</div>
<div class="wrap ftr-bot"><span>© 2026 City One Hotel &amp; Spa. Tüm hakları saklıdır.</span>
 <span><a href="kvkk.html">KVKK Aydınlatma Metni</a> · <a href="kvkk.html#gizlilik">Gizlilik Politikası</a> · <a href="kvkk.html#cerez">Çerez Politikası</a></span></div>
</footer>
<a class="wa-fab" href="{wa_link()}" target="_blank" rel="noopener" aria-label="WhatsApp ile iletişime geçin">{WA_SVG}<span>WhatsApp</span></a>
<div class="cookie" id="cookie" hidden><p>Sitemizde deneyiminizi iyileştirmek için çerezler kullanılabilir. Ayrıntılar için <a href="kvkk.html#cerez">Çerez Politikası</a>'nı inceleyin.</p><button class="btn btn-or" id="cookieOk">Anladım</button></div>
<div class="lightbox" id="lightbox" hidden role="dialog" aria-modal="true" aria-label="Fotoğraf görüntüleyici">
 <button class="lb-x" aria-label="Kapat">{ic('x')}</button><button class="lb-p" aria-label="Önceki">{ic('arrow')}</button><button class="lb-n" aria-label="Sonraki">{ic('arrow')}</button>
 <figure><img alt=""><figcaption></figcaption></figure></div>
<script src="assets/main.js" defer></script>
</body></html>'''

def page_hero(h1, sub, bg, crumb):
    return f'''<section class="phero"><div class="phero-bg">{img(bg, '', lazy=False)}</div>
<div class="wrap"><nav class="crumb" aria-label="Sayfa yolu"><a href="index.html">Ana Sayfa</a> / <span>{crumb}</span></nav>
<h1>{h1}</h1><p>{sub}</p></div></section>'''

def write(name, html):
    open(os.path.join(ROOT, name), 'w', encoding='utf-8').write(html)

COMMON = [('wifi','Ücretsiz Wi-Fi'),('cup','Ücretsiz çay & kahve seti'),('drop','Ücretsiz su'),
          ('fridge','Mini bar'),('iron','Ütü & ütü masası'),('bell','7/24 oda servisi')]

# ------------------------------------------------------------------ ODALAR
ROOMS = [
 dict(id='standart', ad='Standart Oda', m2=27, imgs=['oda-standart','oda-standart-2','banyo-1'],
      txt='Sade ve fonksiyonel tasarımı, sıcak ahşap zemini ve konforlu yatağıyla iş ya da kısa süreli konaklamalar için ideal bir başlangıç.'),
 dict(id='double', ad='Double Oda', m2=None, imgs=['oda-double','oda-double-2','banyo-2'],
      txt='Çift kişilik konaklamalar için tasarlanmış; sıcak tonları ve ferah düzeniyle huzurlu bir dinlenme alanı.'),
 dict(id='twin', ad='Twin Oda', m2=41, imgs=['oda-twin','oda-detay-cay','banyo-3'],
      txt='Ayrı yatak düzeniyle arkadaş grupları ve iş seyahatleri için geniş ve ferah bir seçenek.'),
 dict(id='superior', ad='Superior Oda', m2=43, imgs=['oda-superior','oda-detay-ikram','banyo-4'],
      txt='Daha geniş yaşam alanı, oturma grubu ve özel duvar sanatıyla yükseltilmiş bir konfor deneyimi.'),
 dict(id='family', ad='Family Oda', m2=47, imgs=['oda-family','oda-detay-ikram-2','banyo-1'],
      txt='Aileler için geniş alan: birlikte rahatça konaklayabileceğiniz, ferah ve düzenli bir oda.'),
 dict(id='jakuzili', ad='Jakuzili Oda', m2=53, imgs=['oda-jakuzili','oda-jakuzili-2','banyo-2'],
      txt='Odanın içinde özel jakuzisiyle balayı, yıl dönümü ve özel günler için en ayrıcalıklı seçenek.'),
]

def room_alt(r, i): return f"{r['ad']} - görsel {i+1}"

def rooms_page():
    rows = ''
    for k, r in enumerate(ROOMS):
        thumbs = ''.join(f'<button type="button" class="rt{" on" if i==0 else ""}" data-src="{n}" aria-label="{r["ad"]} fotoğraf {i+1}">{img(n, room_alt(r,i), thumb=True)}</button>' for i,n in enumerate(r['imgs']))
        chip = f'<span class="chip">{ic("ruler")} {r["m2"]} m²</span>' if r['m2'] else ''
        feats = ''.join(f'<li>{ic(i)} {t}</li>' for i,t in COMMON)
        msg = f"Merhaba, {r['ad']} için müsaitlik ve fiyat bilgisi almak istiyorum."
        rows += f'''<article class="room{" rev" if k%2 else ""} reveal" id="{r['id']}">
 <div class="room-media"><a href="assets/img/{r['imgs'][0]}.webp" class="lb room-main" data-lb="{r['id']}" data-caption="{r['ad']}">{img(r['imgs'][0], r['ad'], thumb=False)}</a>
  <div class="rthumbs">{thumbs}</div>
  {''.join(f'<a class="lb hid" href="assets/img/{n}.webp" data-lb="{r["id"]}" data-caption="{room_alt(r,i)}"></a>' for i,n in enumerate(r['imgs'][1:],1))}</div>
 <div class="room-body"><div class="chips">{chip}<span class="chip">{ic('wifi')} Ücretsiz internet</span></div>
  <h2>{r['ad']}</h2><p>{r['txt']}</p>
  <ul class="feat">{feats}</ul>
  <div class="room-act"><a class="btn btn-or" href="{wa_link(msg)}" target="_blank" rel="noopener">{WA_SVG} Fiyat & Müsaitlik</a>
  <a class="btn btn-line" href="tel:{TEL_RAW}">{ic('phone')} Ara</a></div></div></article>'''
    nav = ''.join(f'<a href="#{r["id"]}">{r["ad"]}</a>' for r in ROOMS)
    return (head('Odalarımız | City One Hotel & Spa Kayseri', 'City One Hotel & Spa Kayseri odaları: Standart, Double, Twin, Superior, Family ve Jakuzili odalar. 27 m²\'den 53 m²\'ye geniş seçenekler.', 'odalar.html', 'oda-superior')
      + header('odalar.html')
      + page_hero('Odalarımız', 'Her konuk profiline uygun, özenle tasarlanmış altı farklı oda tipi.', 'oda-jakuzili', 'Odalar')
      + f'<section class="sec"><div class="wrap"><div class="subnav">{nav}</div>{rows}'
      + f'''<div class="incl reveal"><h3>Tüm Odalarımızda</h3><ul class="feat feat-row">{''.join(f'<li>{ic(i)} {t}</li>' for i,t in COMMON + [('car','Vale hizmeti')])}</ul>
      <p class="muted">Tüm konuklarımız ayrıca spa, Türk hamamı, sauna ve yarı olimpik yüzme havuzundan ücretsiz yararlanır.</p></div></div></section>'''
      + footer())

# ------------------------------------------------------------------ OLANAKLAR
def amen_page():
    spa = [('pool','Yarı Olimpik Yüzme Havuzu'),('jac','Jakuzi'),('steam','Türk Hamamı'),('therm','Fin Hamamı'),
           ('therm','Sauna'),('dumb','Spor Salonu & Fitness'),('dumb','Ağırlık Salonu'),('glass','Vitamin Bar')]
    cards = ''.join(f'<div class="amen reveal">{ic(i)}<h3>{t}</h3></div>' for i,t in spa)
    gal = ''.join(lb(n, a, 'spa') for n,a in [
        ('havuz','Yarı olimpik kapalı yüzme havuzu'),('havuz-2','Havuz ve dinlenme alanı'),('jakuzi','Jakuzi ve dinlenme alanı'),
        ('turk-hamami','Türk hamamı'),('turk-hamami-2','Türk hamamı kurnaları'),('vitamin-bar','Spa vitamin bar'),
        ('spa-dinlenme','Spa dinlenme alanı'),('spor-salonu','Spor salonu ve fitness')])
    svc = [('wifi','Ücretsiz Wi-Fi','Otelin tamamında kesintisiz internet.'),('cup','Çay & Kahve Seti','Odalarda ücretsiz çay ve kahve hazırlama seti.'),
           ('drop','Ücretsiz Su','Her odada ücretsiz içme suyu.'),('fridge','Mini Bar','Odalarda mini bar.'),
           ('iron','Ütü & Ütü Masası','Konforunuz için odada hazır.'),('car','Vale Hizmeti','Girişte karşılama ve araç teslimi.'),
           ('bell','7/24 Oda Servisi','Gece gündüz damak zevkinize hizmet.'),('glass','Spa Vitamin Bar','Taze içecekler ve atıştırmalıklar.')]
    scards = ''.join(f'<div class="svc reveal">{ic(i)}<div><h3>{t}</h3><p>{d}</p></div></div>' for i,t,d in svc)
    return (head('Spa & Olanaklar | City One Hotel & Spa Kayseri', 'Yarı olimpik havuz, Türk hamamı, sauna, jakuzi, fitness ve vitamin bar. City One Hotel & Spa Kayseri spa ve otel olanakları.', 'olanaklar.html', 'havuz')
      + header('olanaklar.html')
      + page_hero('Spa & Olanaklar', 'Güne enerjiyle başlayın, günün yorgunluğunu hamam, sauna ve havuzda bırakın.', 'havuz', 'Spa & Olanaklar')
      + f'''<section class="sec"><div class="wrap"><div class="sec-h"><span class="eyebrow">Spa & Wellness</span><h2>Bedeniniz ve zihniniz için</h2>
      <p>Konuklarımız spa alanındaki tüm olanaklardan ücretsiz yararlanır.</p></div>
      <div class="amen-grid">{cards}</div>
      <div class="hours reveal"><div>{ic('clock')}<h3>Spa Çalışma Saatleri</h3></div>
       <div class="hrow"><span>Hafta içi</span><strong>09:00 – 23:00</strong></div>
       <div class="hrow"><span>Hafta sonu</span><strong>09:00 – 21:00</strong></div></div>
      <div class="mosaic">{gal}</div></div></section>
      <section class="sec sec-sand"><div class="wrap"><div class="sec-h"><span class="eyebrow">Otel Hizmetleri</span><h2>Her ayrıntı düşünüldü</h2></div>
      <div class="svc-grid">{scards}</div></div></section>'''
      + footer())

# ------------------------------------------------------------------ RESTORAN
def dining_page():
    kg = ''.join(lb(n, a, 'kahvalti') for n,a in [('kahvalti-1','Açık büfe kahvaltı - şarküteri tabakları'),('kahvalti-2','Açık büfe kahvaltı alanı'),
        ('kahvalti-3','Kahvaltı büfesi - peynir ve şarküteri'),('kahvalti-4','Kahvaltı büfesi - peynir çeşitleri'),
        ('kahvalti-5','Taze salata ve zeytin çeşitleri'),('kahvalti-6','Kahvaltı büfesi - kanepeler'),('kahvalti-7','Kahvaltı büfesi - çeşitler')])
    return (head('Restoran & Kahvaltı | City One Hotel & Spa Kayseri', 'Her sabah 07:00-10:00 açık büfe kahvaltı, akşam yemeği ve 7/24 oda servisi. City One Hotel & Spa Kayseri restoran.', 'restoran.html', 'kahvalti-1')
      + header('restoran.html')
      + page_hero('Restoran & Kahvaltı', 'Zengin açık büfe kahvaltıdan akşam yemeğine, 7/24 oda servisine.', 'kahvalti-6', 'Restoran')
      + f'''<section class="sec"><div class="wrap">
      <div class="dcards">
       <div class="dcard reveal">{ic('cup')}<h3>Açık Büfe Kahvaltı</h3><p class="big">07:00 – 10:00</p><p>Taze ve zengin çeşitlerle her sabah.</p></div>
       <div class="dcard reveal">{ic('glass')}<h3>Akşam Yemeği</h3><p class="big">00:00'a kadar</p><p>Ala carte ve zengin menü seçenekleri.</p></div>
       <div class="dcard reveal">{ic('bell')}<h3>Oda Servisi</h3><p class="big">7/24</p><p>Dilediğiniz an odanıza servis.</p></div></div>
      <div class="split reveal"><div class="split-img">{img('restoran-salon','City One restoran salonu')}</div>
       <div><span class="eyebrow">Restoran</span><h2>Şehir manzaralı restoran salonu</h2>
       <p>Geniş ve aydınlık salonumuzda gün boyu konuklarımızı ağırlıyoruz. Kayseri mutfağının lezzetlerini ve zengin menümüzü keyifle deneyimleyin.</p>
       <ul class="ticks"><li>{ic('check')} Açık büfe kahvaltı</li><li>{ic('check')} Akşam yemeği</li><li>{ic('check')} 7/24 oda servisi</li></ul></div></div>
      <div class="sec-h"><span class="eyebrow">Kahvaltı</span><h2>Sabahın en güzel hali</h2></div>
      <div class="mosaic">{kg}</div>
      <div class="split rev reveal"><div class="split-img">{img('restoran-sini-teras','Sini Restoran teras ve akşam atmosferi')}</div>
       <div><span class="eyebrow">Sini Restoran</span><h2>Büyük davetlere de ev sahipliği</h2>
       <p>Sini Restoran, 750 kişiye kadar kapasitesiyle hem günlük yemekler hem de büyük organizasyonlar için geniş bir alan sunar.</p>
       <a class="btn btn-line" href="salonlar.html">Etkinlik Salonlarını Gör {ic('arrow')}</a></div></div>
      </div></section>'''
      + footer())

# ------------------------------------------------------------------ SALONLAR
HALLS = [
 ('kayseri','Kayseri Salonu','Işıltılı avizeleri, geniş mermer pisti ve sahnesiyle düğün ve büyük organizasyonlar için.',['salon-kayseri','salon-kayseri-2','salon-kayseri-3']),
 ('yelken','Yelken Salonu','Cam çatısı ve açık gökyüzü manzarasıyla unutulmaz nişan ve düğünler için.',['salon-yelken','salon-yelken-2']),
 ('kapadokya','Kapadokya Salonu','Zarif dekorasyon ve özel gün konseptleriyle nişan, kına ve davetler için.',['salon-kapadokya','salon-kapadokya-2','salon-kapadokya-3']),
 ('efes','Efes Salonu','Esnek oturma düzeni ve ferah yapısıyla kokteyl, toplantı ve davetler için.',['salon-efes','salon-efes-2']),
 ('erciyes','Erciyes Salonu','Özel anların ve ilk dansın yaşandığı, atmosferi yüksek davet salonu.',['salon-erciyes']),
 ('sini','Sini Restoran Salonu','750 kişiye kadar kapasitesiyle büyük davet ve organizasyonlar için.',['restoran-sini-teras']),
]
def halls_page():
    rows = ''
    for k,(i,ad,txt,imgs) in enumerate(HALLS):
        extra = ''.join(f'<a class="lb hid" href="assets/img/{n}.webp" data-lb="h-{i}" data-caption="{ad}"></a>' for n in imgs[1:])
        more = f'<span class="more">+{len(imgs)-1} fotoğraf</span>' if len(imgs) > 1 else ''
        rows += f'''<article class="hall reveal"><a class="lb hall-img" href="assets/img/{imgs[0]}.webp" data-lb="h-{i}" data-caption="{ad}">{img(imgs[0], ad, thumb=True)}{more}</a>{extra}
        <div class="hall-b"><h3>{ad}</h3><p>{txt}</p><a class="link" href="{wa_link(f'Merhaba, {ad} için etkinlik teklifi almak istiyorum.')}" target="_blank" rel="noopener">Teklif Al {ic('arrow')}</a></div></article>'''
    types = ['Düğün','Nişan','Kına Gecesi','Sünnet','Toplantı & Seminer','Mezuniyet','Kurumsal Yemek','Doğum Günü']
    return (head('Etkinlik Salonları | City One Hotel & Spa Kayseri', 'Düğün, nişan, kına, toplantı ve davetler için City One Hotel & Spa Kayseri etkinlik salonları: Kayseri, Yelken, Kapadokya, Efes, Erciyes ve Sini.', 'salonlar.html', 'salon-kayseri')
      + header('salonlar.html')
      + page_hero('Etkinlik Salonları', 'Özel günleriniz ve kurumsal organizasyonlarınız için altı farklı salon.', 'salon-yelken', 'Etkinlik Salonları')
      + f'''<section class="sec"><div class="wrap"><div class="sec-h"><span class="eyebrow">Organizasyon</span><h2>Hayalinizdeki davet, bizimle</h2>
      <p>Salonlarımızda profesyonel ekibimizle düğün, nişan, kına, toplantı ve davetlerinizi eksiksiz planlıyoruz.</p></div>
      <div class="tags">{''.join(f'<span>{t}</span>' for t in types)}</div>
      <div class="halls">{rows}</div>
      <div class="split reveal"><div class="split-img vid"><video src="assets/video/sini-restoran.mp4" controls preload="none" playsinline poster="assets/thumb/restoran-sini-teras.webp"></video></div>
       <div><span class="eyebrow">Kapasite & Teklif</span><h2>Size özel teklif hazırlayalım</h2><p>Tarih, kişi sayısı ve konseptinizi bize iletin; salon seçimi ve menü seçenekleriyle size özel bir teklif hazırlayalım.</p>
       <a class="btn btn-or" href="{wa_link('Merhaba, etkinlik salonları için teklif almak istiyorum.')}" target="_blank" rel="noopener">{WA_SVG} WhatsApp'tan Teklif İsteyin</a></div></div>
      </div></section>'''
      + footer())

# ------------------------------------------------------------------ GALERI
GAL = [
 ('otel-hava-gunduz','otel','Otelin havadan gündüz görüntüsü'),('otel-giris-gece','otel','Otel girişi gece'),('lobi-hali','otel','Otel lobisi'),
 ('oda-jakuzili','odalar','Jakuzili oda'),('havuz','spa','Yarı olimpik yüzme havuzu'),('kahvalti-1','restoran','Açık büfe kahvaltı'),
 ('salon-kayseri','salonlar','Kayseri Salonu'),('oda-superior','odalar','Superior oda'),('turk-hamami','spa','Türk hamamı'),
 ('otel-giris-gece-2','otel','Otel girişi geceleri'),('oda-standart','odalar','Standart oda'),('restoran-salon','restoran','Restoran salonu'),
 ('salon-yelken','salonlar','Yelken Salonu'),('banyo-2','odalar','Oda banyosu'),('jakuzi','spa','Jakuzi'),
 ('lobi-resepsiyon','otel','Resepsiyon'),('oda-family','odalar','Family oda'),('kahvalti-3','restoran','Kahvaltı büfesi'),
 ('havuz-2','spa','Havuz ve dinlenme alanı'),('salon-kapadokya','salonlar','Kapadokya Salonu'),('oda-twin','odalar','Twin oda'),
 ('otel-panorama-gunduz','otel','Otel ve Kayseri panoraması'),('spor-salonu','spa','Spor salonu'),('restoran-sini-teras','restoran','Sini Restoran teras'),
 ('oda-double','odalar','Double oda'),('banyo-1','odalar','Oda banyosu'),('vitamin-bar','spa','Spa vitamin bar'),('kahvalti-5','restoran','Taze salata ve zeytin çeşitleri'),
 ('salon-efes','salonlar','Efes Salonu'),('lobi-oturma','otel','Lobi oturma alanı'),('oda-detay-ikram','odalar','Oda ikramı'),('gelin-hamami','spa','Gelin hamamı'),
 ('salon-erciyes','salonlar','Erciyes Salonu'),('otel-cephe-gunduz','otel','Otel cephesi'),('kahvalti-6','restoran','Kahvaltı kanepeleri'),('turk-hamami-2','spa','Türk hamamı'),
 ('salon-kayseri-2','salonlar','Kayseri Salonu geniş görünüm'),('lobi-genis','otel','Lobi'),('oda-standart-2','odalar','Standart oda'),('banyo-amenities','odalar','Banyo ürünleri'),
]
def gallery_page():
    cats = [('hepsi','Tümü'),('otel','Otel'),('odalar','Odalar'),('spa','Spa'),('restoran','Restoran'),('salonlar','Salonlar'),('video','Videolar')]
    btns = ''.join(f'<button type="button" class="fbtn{" on" if k=="hepsi" else ""}" data-f="{k}">{v}</button>' for k,v in cats)
    items = ''.join(f'<div class="gi" data-c="{c}">{lb(n, a, "galeri")}</div>' for n,c,a in GAL)
    vids = [('lobi-tanitim','Otel lobisi','portrait'),('gelin-hamami','Gelin hamamı',''),('sini-restoran','Sini Restoran',''),('erciyes-kayak','Erciyes Kayak Merkezi','portrait')]
    vh = ''.join(f'<figure class="gv {p}"><video src="assets/video/{n}.mp4" controls preload="metadata" playsinline></video><figcaption>{t}</figcaption></figure>' for n,t,p in vids)
    return (head('Galeri | City One Hotel & Spa Kayseri', 'City One Hotel & Spa Kayseri fotoğraf ve video galerisi: odalar, spa, restoran, lobi ve etkinlik salonları.', 'galeri.html', 'otel-giris-gece')
      + header('galeri.html')
      + page_hero('Galeri', 'Otelimizden kareler: odalar, spa, restoran ve etkinlik salonları.', 'otel-giris-gece-2', 'Galeri')
      + f'''<section class="sec"><div class="wrap"><div class="filters" role="group" aria-label="Galeri filtresi">{btns}</div>
      <div class="masonry" id="masonry">{items}</div>
      <div class="vgrid" id="vgrid" hidden>{vh}</div></div></section>'''
      + footer())

# ------------------------------------------------------------------ ILETISIM
def contact_page():
    return (head('İletişim & Rezervasyon | City One Hotel & Spa Kayseri', 'City One Hotel & Spa Kayseri iletişim: Eski Sanayi Bölgesi 2. Cadde No: 11. Telefon 0352 207 00 00, WhatsApp 0506 752 02 86.', 'iletisim.html', 'otel-hava-gunduz')
      + header('iletisim.html')
      + page_hero('İletişim & Rezervasyon', 'Sorularınız, rezervasyon ve etkinlik talepleriniz için buradayız.', 'otel-panorama-gunduz', 'İletişim')
      + f'''<section class="sec"><div class="wrap cgrid">
      <div class="cinfo reveal"><h2>Bize Ulaşın</h2>
       <ul class="ci big">
        <li>{ic('pin')}<div><strong>Adres</strong><span>{ADDR}</span></div></li>
        <li>{ic('phone')}<div><strong>Telefon (Santral)</strong><a href="tel:{TEL_RAW}">{TEL}</a></div></li>
        <li>{WA_SVG}<div><strong>WhatsApp</strong><a href="{wa_link()}" target="_blank" rel="noopener">{WA}</a></div></li>
        <li>{ic('mail')}<div><strong>E-posta</strong><a href="mailto:{MAIL}">{MAIL}</a></div></li>
        <li>{ic('bell')}<div><strong>Oda Servisi</strong><span>7/24</span></div></li>
        <li>{ic('pool')}<div><strong>Spa</strong><span>Hafta içi 09:00–23:00 · Hafta sonu 09:00–21:00</span></div></li></ul>
       <a class="btn btn-line" href="https://www.google.com/maps/dir/?api=1&destination={MAPQ.replace(' ','+')}" target="_blank" rel="noopener">{ic('pin')} Yol Tarifi Al</a></div>
      <form class="form reveal" id="rezervasyon" novalidate><h2>Rezervasyon / Mesaj</h2>
       <p class="muted">Formu doldurun; mesajınız WhatsApp üzerinden bize iletilsin.</p>
       <div class="fr"><label>Ad Soyad<input name="ad" required autocomplete="name"></label><label>Telefon<input name="tel" type="tel" autocomplete="tel"></label></div>
       <div class="fr"><label>Giriş Tarihi<input name="g" type="date"></label><label>Çıkış Tarihi<input name="c" type="date"></label></div>
       <div class="fr"><label>Oda Tipi<select name="oda"><option value="">Seçiniz</option>{''.join(f'<option>{r["ad"]}</option>' for r in ROOMS)}<option>Etkinlik / Salon</option></select></label>
       <label>Kişi Sayısı<input name="k" type="number" min="1" max="20" value="2"></label></div>
       <label>Mesajınız<textarea name="m" rows="4"></textarea></label>
       <label class="chk"><input type="checkbox" name="kvkk" required> <span><a href="kvkk.html" target="_blank">KVKK Aydınlatma Metni</a>'ni okudum, kişisel verilerimin işlenmesini kabul ediyorum.</span></label>
       <button class="btn btn-or" type="submit">{WA_SVG} WhatsApp ile Gönder</button><p class="err" id="ferr" hidden></p></form></div>
      <div class="wrap"><div class="map reveal"><iframe title="City One Hotel & Spa harita konumu" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
       src="https://www.google.com/maps?q={MAPQ.replace(' ','+')}&output=embed&hl=tr"></iframe></div></div></section>'''
      + footer())

# ------------------------------------------------------------------ KVKK
def kvkk_page():
    ph = lambda t: f'<div class="ph"><strong>[{t} buraya eklenecek]</strong><p>Bu bölüm, otel tarafından sağlanacak resmi metinle doldurulacaktır.</p></div>'
    return (head('KVKK Aydınlatma Metni | City One Hotel & Spa Kayseri', 'City One Hotel & Spa kişisel verilerin korunması, gizlilik ve çerez politikaları.', 'kvkk.html')
      + header('kvkk.html')
      + page_hero('Yasal Bilgilendirme', 'Kişisel verilerin korunması, gizlilik ve çerez politikalarımız.', 'lobi-hali', 'KVKK')
      + f'''<section class="sec"><div class="wrap narrow legal">
      <h2 id="kvkk">KVKK Aydınlatma Metni</h2>{ph('KVKK Aydınlatma Metni')}
      <h2 id="gizlilik">Gizlilik Politikası</h2>{ph('Gizlilik Politikası')}
      <h2 id="cerez">Çerez Politikası</h2>{ph('Çerez Politikası')}
      <p class="muted">Veri sorumlusu: City One Hotel &amp; Spa · {ADDR} · <a href="mailto:{MAIL}">{MAIL}</a></p></div></section>'''
      + footer())

# ------------------------------------------------------------------ ANASAYFA
def home_page():
    slides = [('otel-hava-gunduz','Otelin havadan görünümü'),('otel-giris-gece','Gece aydınlatmalı otel girişi'),('havuz','Yarı olimpik kapalı havuz'),('oda-jakuzili','Jakuzili oda')]
    sl = ''.join(f'<div class="slide{" on" if i==0 else ""}">{img(n,a,lazy=(i>0))}</div>' for i,(n,a) in enumerate(slides))
    dots = ''.join(f'<button type="button" class="dot{" on" if i==0 else ""}" aria-label="Slayt {i+1}"></button>' for i in range(len(slides)))
    rcards = ''.join(f'''<a class="rcard reveal" href="odalar.html#{r['id']}">{img(r['imgs'][0], r['ad'], thumb=True)}
      <div class="rcard-b"><h3>{r['ad']}</h3>{f'<span class="chip">{ic("ruler")} {r["m2"]} m²</span>' if r['m2'] else ''}<span class="link">İncele {ic('arrow')}</span></div></a>''' for r in ROOMS if r['id'] in ('standart','superior','jakuzili'))
    am = [('wifi','Ücretsiz Wi-Fi'),('cup','Çay & Kahve Seti'),('drop','Ücretsiz Su'),('fridge','Mini Bar'),('iron','Ütü & Masası'),('car','Vale Hizmeti'),('bell','7/24 Oda Servisi'),('glass','Vitamin Bar')]
    amg = ''.join(f'<div class="am">{ic(i)}<span>{t}</span></div>' for i,t in am)
    spa = ['Yarı olimpik yüzme havuzu','Jakuzi','Türk hamamı & Fin hamamı','Sauna','Spor salonu, ağırlık salonu & fitness','Vitamin bar']
    gal = ['otel-giris-gece-2','oda-superior','kahvalti-3','salon-kayseri','turk-hamami','lobi-hali']
    gh = ''.join(lb(n, dict((a,b) for a,_,b in GAL).get(n, n), 'ana') for n in gal)
    schema = json.dumps({"@context":"https://schema.org","@type":"Hotel","name":"City One Hotel & Spa","starRating":{"@type":"Rating","ratingValue":"4"},
        "address":{"@type":"PostalAddress","streetAddress":"Eski Sanayi Bölgesi 2. Cadde No: 11","addressLocality":"Kayseri","addressCountry":"TR"},
        "telephone":"+903522070000","email":MAIL,"image":"assets/img/otel-hava-gunduz.webp","amenityFeature":[{"@type":"LocationFeatureSpecification","name":n,"value":True} for n in ["Ücretsiz Wi-Fi","Yüzme havuzu","Spa","Türk hamamı","Sauna","Fitness","Oda servisi","Vale"]]}, ensure_ascii=False)
    return (head('City One Hotel & Spa Kayseri | 4 Yıldızlı Otel, Spa & Etkinlik Salonları', 'Kayseri\'de 4 yıldızlı City One Hotel & Spa: yarı olimpik havuz, Türk hamamı, sauna, açık büfe kahvaltı, 7/24 oda servisi ve etkinlik salonları. Hemen rezervasyon yapın.', 'index.html').replace('</head>', f'<script type="application/ld+json">{schema}</script>\n</head>')
      + header('index.html')
      + f'''<section class="hero" id="hero"><div class="slides">{sl}</div><div class="hero-shade"></div>
      <div class="wrap hero-c"><span class="stars" aria-label="4 yıldızlı otel">★★★★</span><h1>Kayseri'de Konfor,<br><em>Konukseverlikle</em> Buluşuyor</h1>
       <p>Ferah odalar, spa &amp; wellness, zengin açık büfe kahvaltı ve etkinlik salonlarıyla City One Hotel &amp; Spa.</p>
       <div class="hero-btns"><a class="btn btn-or" href="odalar.html">Odaları Keşfet</a><a class="btn btn-ghost" href="tel:{TEL_RAW}">{ic('phone')} {TEL}</a></div></div>
      <div class="dots">{dots}</div>
      <form class="book" id="book"><div class="wrap book-in">
       <label>{ic('cal')}<span>Giriş</span><input type="date" name="g" required></label>
       <label>{ic('cal')}<span>Çıkış</span><input type="date" name="c" required></label>
       <label>{ic('users')}<span>Yetişkin</span><select name="y"><option>1</option><option selected>2</option><option>3</option><option>4</option><option>5</option></select></label>
       <label>{ic('users')}<span>Çocuk</span><select name="co"><option>0</option><option>1</option><option>2</option><option>3</option></select></label>
       <button class="btn btn-or" type="submit">{WA_SVG} Müsaitlik Sor</button></div></form></section>

      <section class="sec intro"><div class="wrap split">
       <div class="split-txt reveal"><span class="eyebrow">Hoş Geldiniz</span><h2>İş de olsa, tatil de olsa; doğru adres</h2>
        <p>City One Hotel &amp; Spa, Kayseri'de iş ve tatil seyahatleri için konfor, hizmet kalitesi ve zengin olanakları bir araya getirir. Sıcak karşılama, özenle tasarlanmış odalar, spa ve yemek seçenekleriyle konaklamanızı unutulmaz kılmak için buradayız.</p>
        <div class="stats"><div><strong>4★</strong><span>Otel</span></div><div><strong>6</strong><span>Oda Tipi</span></div><div><strong>7/24</strong><span>Oda Servisi</span></div><div><strong>6</strong><span>Etkinlik Salonu</span></div></div></div>
       <div class="duo reveal">{img('lobi-hali','City One lobi girişi', thumb=False)}{img('otel-giris-gece-3','City One otel girişi gece', thumb=True)}</div></div></section>

      <section class="sec sec-sand"><div class="wrap"><div class="sec-h"><span class="eyebrow">Odalarımız</span><h2>Size uygun odayı seçin</h2><p>27 m²'den 53 m²'ye, altı farklı oda tipi.</p></div>
       <div class="rgrid">{rcards}</div><div class="center"><a class="btn btn-line" href="odalar.html">Tüm Odaları Gör {ic('arrow')}</a></div></div></section>

      <section class="sec"><div class="wrap"><div class="sec-h"><span class="eyebrow">Olanaklar</span><h2>Konforunuz için her şey hazır</h2></div><div class="amg">{amg}</div></div></section>

      <section class="feature"><div class="feature-img">{img('havuz','Yarı olimpik kapalı yüzme havuzu')}</div>
       <div class="feature-b reveal"><span class="eyebrow lt">Spa & Wellness</span><h2>Yorgunluğu havuzda, hamamda bırakın</h2>
       <ul class="ticks">{''.join(f'<li>{ic("check")} {s}</li>' for s in spa)}</ul>
       <p class="hrs">{ic('clock')} Hafta içi 09:00 – 23:00 · Hafta sonu 09:00 – 21:00</p><a class="btn btn-or" href="olanaklar.html">Spa & Olanaklar</a></div></section>

      <section class="sec"><div class="wrap"><div class="sec-h"><span class="eyebrow">Restoran</span><h2>Sofranızda zengin bir sabah, gece boyu servis</h2></div>
       <div class="dgrid"><a class="dtile reveal" href="restoran.html">{img('kahvalti-3','Açık büfe kahvaltı',thumb=True)}<div><h3>Açık Büfe Kahvaltı</h3><p>07:00 – 10:00</p></div></a>
       <a class="dtile reveal" href="restoran.html">{img('restoran-salon','Restoran salonu',thumb=True)}<div><h3>Akşam Yemeği</h3><p>00:00'a kadar</p></div></a>
       <a class="dtile reveal" href="restoran.html">{img('restoran-kebap','Oda servisi ve ana yemekler',thumb=True)}<div><h3>Oda Servisi</h3><p>7/24</p></div></a></div></div></section>

      <section class="sec sec-brown erc"><div class="wrap split">
       <div class="reveal"><span class="eyebrow lt">Erciyes</span><h2>Kayak merkezi Erciyes'e kısa bir yolculuk</h2>
       <p>Kış aylarında Erciyes Kayak Merkezi'nin pistlerine, yaz aylarında ise Kayseri'nin tarihi ve doğal güzelliklerine açılan kapınız City One.</p>
       <a class="btn btn-or" href="iletisim.html">Plan Yapalım</a></div>
       <div class="vwrap reveal"><video src="assets/video/erciyes-kayak.mp4" poster="assets/video/erciyes-poster.jpg" autoplay muted loop playsinline preload="none" aria-label="Erciyes Kayak Merkezi videosu"></video></div></div></section>

      <section class="sec"><div class="wrap"><div class="sec-h"><span class="eyebrow">Etkinlik Salonları</span><h2>Özel anlarınız için doğru salon</h2><p>Düğün, nişan, kına, toplantı ve davetler.</p></div>
       <div class="dgrid">{''.join(f'<a class="dtile reveal" href="salonlar.html">{img(h[3][0],h[1],thumb=True)}<div><h3>{h[1]}</h3></div></a>' for h in [HALLS[0],HALLS[1],HALLS[2]])}</div>
       <div class="center"><a class="btn btn-line" href="salonlar.html">Tüm Salonlar {ic('arrow')}</a></div></div></section>

      <section class="sec sec-sand"><div class="wrap"><div class="sec-h"><span class="eyebrow">Galeri</span><h2>Otelimizden kareler</h2></div>
       <div class="gstrip">{gh}</div><div class="center"><a class="btn btn-line" href="galeri.html">Tüm Galeri {ic('arrow')}</a></div></div></section>

      <section class="sec"><div class="wrap cols2"><div class="reveal"><span class="eyebrow">Konum</span><h2>Bizi kolayca bulun</h2>
       <ul class="ci big"><li>{ic('pin')}<div><strong>Adres</strong><span>{ADDR}</span></div></li><li>{ic('phone')}<div><strong>Telefon</strong><a href="tel:{TEL_RAW}">{TEL}</a></div></li><li>{WA_SVG}<div><strong>WhatsApp</strong><a href="{wa_link()}" target="_blank" rel="noopener">{WA}</a></div></li></ul>
       <a class="btn btn-line" href="iletisim.html">İletişim Sayfası {ic('arrow')}</a></div>
       <div class="map reveal"><iframe title="City One Hotel & Spa harita konumu" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q={MAPQ.replace(' ','+')}&output=embed&hl=tr"></iframe></div></div></section>'''
      + footer())

if __name__ == '__main__':
    write('index.html', home_page()); write('odalar.html', rooms_page()); write('olanaklar.html', amen_page())
    write('restoran.html', dining_page()); write('salonlar.html', halls_page()); write('galeri.html', gallery_page())
    write('iletisim.html', contact_page()); write('kvkk.html', kvkk_page())
    write('robots.txt', 'User-agent: *\nAllow: /\n')
    print('ok')
