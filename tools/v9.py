#!/usr/bin/env python3
"""v9: resmi KVKK metni, adres düzeltmesi (No: 11), Google yorum bölümü, şirket ünvanı. Idempotent."""
import os, re, json, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLACE = 'ChIJ4_bKkfgRKxURchBS0CBWZuI'
RATING, COUNT, ASOF = '4,1', '3.247', 'Ekim 2026'
LINK_READ = f'https://search.google.com/local/reviews?placeid={PLACE}'
LINK_WRITE = f'https://search.google.com/local/writereview?placeid={PLACE}'
COMPANY = 'Panorama Mobilya İnşaat Turizm Otel Sanayi Ticaret A.Ş.'
def rd(p): return open(os.path.join(ROOT,p),encoding='utf-8').read()
def wr(p,s): open(os.path.join(ROOT,p),'w',encoding='utf-8').write(s)
FILES = [f for f in os.listdir(ROOT) if f.endswith('.html')] + ['en/'+f for f in os.listdir(os.path.join(ROOT,'en')) if f.endswith('.html')]

# ---------- resmi KVKK metni -> HTML ----------
def kvkk_html():
    raw = [l.rstrip() for l in rd('tools/kvkk_resmi.txt').split('\n')]
    raw = [l for l in raw if l.strip()][2:]          # tekrar eden başlık satırlarını at
    item = re.compile(r'^\s*(?:[a-n]|i{1,3}|iv)\s?\.\s?\S|^\s*[•–]\s')
    head = re.compile(r'^([A-K])\.\s+(.*)$')
    blocks=[]; buf=[]; mode=None; hdr_open=False
    def flush():
        nonlocal buf,mode
        if buf:
            t=' '.join(x.strip() for x in buf); blocks.append((mode,t)); buf=[]; mode=None
    for l in raw:
        s=l.strip()
        if s=='Gizlilik Politikası': flush(); blocks.append(('gz',s)); continue
        m=head.match(s)
        if m: flush(); blocks.append(('h',s)); hdr_open=True; continue
        if blocks and blocks[-1][0]=='h' and not blocks[-1][1].endswith((':','Sebep')) and hdr_open: blocks[-1]=('h',blocks[-1][1]+' '+s.rstrip(':')+(':' if s.endswith(':') else '')); hdr_open=False; continue
        if item.match(l): flush(); mode='li'; buf=[re.sub(r'^[•–]\s*','',s)]; 
        else:
            if mode is None: mode='p'
            buf.append(s)
        if len(s)<72 and re.search(r'[.:;]$',s): flush()
    flush()
    # temizlik
    fix=lambda t: t.replace('City One Hotel &Spa;','City One Hotel & Spa').replace('No:11Kayseri','No: 11 Kayseri').replace('No:11 Kayseri','No: 11 Kayseri').replace('&Spa(','& Spa (')
    out_k=[]; out_g=[]; cur=out_k; lst=False
    for typ,t in blocks:
        t=html.escape(fix(t),quote=False)
        t=t.replace('Başvuru Adresi','<br>Başvuru Adresi').replace('Başvuru E-Posta','<br>Başvuru E-Posta')
        t=re.sub(r'(info@cityonekayseri\.com)',r'<a href="mailto:\1">\1</a>',t)
        t=re.sub(r'(https://www\.cityonekayseri\.com)',r'<a href="\1">\1</a>',t)
        if typ=='gz': cur=out_g; continue
        if typ!='li' and lst: cur.append('</ul>'); lst=False
        if typ=='li' and not lst: cur.append('<ul>'); lst=True
        if typ=='h': cur.append('<h3>'+t+'</h3>')
        elif typ=='li': cur.append('<li>'+t+'</li>')
        else: cur.append('<p>'+t+'</p>')
    if lst: cur.append('</ul>')
    return ''.join(out_k), ''.join(out_g)

# ---------- 1) adres ----------
for f in FILES+['tools/enhance.py','tools/build.py']:
    s=rd(f); n=s.replace('No: 6002','No: 11').replace('No+6002','No+11').replace('No 6002','No 11')
    if n!=s: wr(f,n)

# ---------- 2) KVKK TR ----------
k,g = kvkk_html()
s=rd('kvkk.html')
a=s.index('<h2 id="kvkk">'); b=s.index('<h2 id="gizlilik">'); c=s.index('<h2 id="cerez">')
priv_old=s[b:c]
# mevcut siteye özgü gizlilik alt başlıklarını koru
keep=priv_old[priv_old.index('<h3>Sitede topladığımız bilgiler</h3>'):]
keep=keep.replace('Gönder” düğmesine bastığınızda bu bilgiler hazır bir mesaj olarak WhatsApp’a aktarılır ve mesajı siz göndermeden bize ulaşmaz. Gönderdikten sonra mesajınız WhatsApp’ın kendi gizlilik koşullarına tabidir.',
                  'Gönder” düğmesine bastığınızda bu bilgiler hazır bir mesaj olarak WhatsApp’a (veya “E-posta ile gönder” seçeneğinde e-posta uygulamanıza) aktarılır ve mesajı siz göndermeden bize ulaşmaz. Gönderdikten sonra mesajınız ilgili hizmetin (WhatsApp / e-posta sağlayıcınız) gizlilik koşullarına tabidir.')
if True:
    intro=(f'<!--c1:resmi--><p class="muted">Veri sorumlusu: <strong>{COMPANY}</strong> – City One Hotel &amp; Spa.</p>')
    new=('<h2 id="kvkk">Kişisel Verilerin İşlenmesine İlişkin Aydınlatma Metni</h2>'+intro+k+
         '<h2 id="gizlilik">Gizlilik Politikası</h2>'+g+keep)
    s=s[:a]+new+s[c:]
    s=s.replace('<a href="#kvkk">KVKK Aydınlatma Metni</a>','<a href="#kvkk">KVKK Aydınlatma Metni</a>')
    s=s.replace('“Anladım” seçiminizi hatırlamak için tarayıcınızın yerel depolamasında <em>c1-cookie</em> kaydı tutulur.','Çerez tercihinizi (“Anladım” veya “Reddet”) hatırlamak için tarayıcınızın yerel depolamasında <em>c1-cookie</em> kaydı tutulur.')
    wr('kvkk.html',s)

# EN: yasal metnin Türkçesi esastır
e=rd('en/legal.html')
if 'c1:resmi' not in e:
    e=e.replace('<h2 id="kvkk">KVKK Privacy Notice</h2>',
      f'<h2 id="kvkk">KVKK Privacy Notice</h2><!--c1:resmi--><p class="muted">Data controller: <strong>{COMPANY}</strong> – City One Hotel &amp; Spa. The official, legally binding text of the notice is the <a href="../kvkk.html#kvkk">Turkish version</a>; this page is an English summary for convenience.</p>',1)
    e=e.replace('<h3>1. Data controller</h3><p>City One Hotel &amp; Spa,',f'<h3>1. Data controller</h3><p>{COMPANY} – City One Hotel &amp; Spa,',1)
    wr('en/legal.html',e)

# ---------- 3) footer şirket ünvanı ----------
for f in FILES:
    s=rd(f)
    n=s.replace('© 2026 City One Hotel &amp; Spa. Tüm hakları saklıdır.',f'© 2026 City One Hotel &amp; Spa · {COMPANY} Tüm hakları saklıdır.')
    n=n.replace('© 2026 City One Hotel &amp; Spa. All rights reserved.',f'© 2026 City One Hotel &amp; Spa · {COMPANY} All rights reserved.')
    if n!=s: wr(f,n)

# ---------- 4) Google yorum bölümü (ana sayfa) ----------
T={'tr':dict(e='Google Yorumları',h='Misafirlerimiz ne diyor?',r=RATING,c=f'{COUNT} Google değerlendirmesi',
        p='Konuk deneyimlerini Google Haritalar’da olduğu gibi okuyabilir, konaklamanız sonrasında siz de yorumunuzu paylaşabilirsiniz. Geri bildirimleriniz hizmetimizi geliştirmemize yardımcı olur.',
        b1='Yorumları Google’da oku',b2='Yorum yaz',n=f'Puan ve yorum sayısı Google Haritalar verisidir ({ASOF} itibarıyla).',al='5 üzerinden 4,1 puan'),
   'en':dict(e='Google Reviews',h='What our guests say',r='4.1',c=f'{COUNT.replace(".",",")} Google reviews',
        p='Read guest experiences exactly as they appear on Google Maps, and share your own review after your stay. Your feedback helps us improve our service.',
        b1='Read reviews on Google',b2='Write a review',n=f'Rating and review count are taken from Google Maps (as of October 2026).',al='4.1 out of 5')}
def rev(L):
    t=T[L]
    return (f'<!--c1:rev--><section class="sec revs"><div class="wrap revs-in"><div class="revs-score reveal"><span class="rs-n">{t["r"]}</span>'
      f'<div><span class="stars-g" style="--p:82%" role="img" aria-label="{t["al"]}">★★★★★</span><strong>{t["c"]}</strong></div></div>'
      f'<div class="revs-txt reveal"><span class="eyebrow">{t["e"]}</span><h2>{t["h"]}</h2><p>{t["p"]}</p>'
      f'<div class="revs-btns"><a class="btn btn-or" href="{LINK_READ}" target="_blank" rel="noopener">{t["b1"]}</a><a class="btn btn-line" href="{LINK_WRITE}" target="_blank" rel="noopener">{t["b2"]}</a></div>'
      f'<p class="revs-note">{t["n"]}</p></div></div></section><!--/c1:rev-->\n\n')
for f,L in (('index.html','tr'),('en/index.html','en')):
    s=rd(f); s=re.sub(r'<!--c1:rev-->.*?<!--/c1:rev-->\n\n','',s,flags=re.S)
    key='<section class="sec sec-sand"><div class="wrap"><div class="sec-h"><span class="eyebrow">'+("Kayseri'yi keşfedin" if L=='tr' else 'Discover Kayseri')
    assert key in s, f
    s=s.replace(key,rev(L)+key,1)
    # JSON-LD: geo + harita
    def fix(m):
        d=json.loads(m.group(1)); d['geo']={"@type":"GeoCoordinates","latitude":38.724028,"longitude":35.4774671}
        d['hasMap']=f'https://www.google.com/maps/place/?q=place_id:{PLACE}'; return '<script type="application/ld+json">'+json.dumps(d,ensure_ascii=False)+'</script>'
    s=re.sub(r'<script type="application/ld\+json">(\{"@context": "https://schema.org", "@type": "Hotel".*?)</script>',fix,s,count=1,flags=re.S)
    wr(f,s)
# iletişim sayfaları: Google yorum bağlantısı (yol tarifi düğmesinin yanında)
for f,L in (('iletisim.html','tr'),('en/contact.html','en')):
    s=rd(f)
    if 'c1:grev' not in s:
        lab='Google yorumları' if L=='tr' else 'Google reviews'
        s=s.replace('</svg> Yol Tarifi Al</a>', f'</svg> Yol Tarifi Al</a> <!--c1:grev--><a class="btn btn-line" href="{LINK_READ}" target="_blank" rel="noopener">★ {lab}</a>',1) if L=='tr' else s.replace('</svg> Get directions</a>', f'</svg> Get directions</a> <!--c1:grev--><a class="btn btn-line" href="{LINK_READ}" target="_blank" rel="noopener">★ {lab}</a>',1)
        wr(f,s)
print('v9 tamam')
