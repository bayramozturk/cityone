(function(){
'use strict';
var $=function(s,c){return (c||document).querySelector(s)},$$=function(s,c){return Array.prototype.slice.call((c||document).querySelectorAll(s))};
var store={get:function(k){try{return localStorage.getItem(k)}catch(e){return null}},set:function(k,v){try{localStorage.setItem(k,v)}catch(e){}}};

/* header */
var hdr=$('#hdr');var isHome=document.body.dataset.page==='index.html';function onScroll(){hdr.classList.toggle('solid',window.scrollY>40);if(isHome)document.body.classList.toggle('at-hero',window.scrollY<window.innerHeight*.5)}onScroll();window.addEventListener('scroll',onScroll,{passive:true});
var burger=$('#burger'),nav=$('#nav');
burger.addEventListener('click',function(){var o=nav.classList.toggle('open');burger.setAttribute('aria-expanded',o);burger.setAttribute('aria-label',o?'Menüyü kapat':'Menüyü aç')});
$$('a',nav).forEach(function(a){a.addEventListener('click',function(){nav.classList.remove('open');burger.setAttribute('aria-expanded','false')})});

/* reveal */
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12});$$('.reveal').forEach(function(el){io.observe(el)})}else{$$('.reveal').forEach(function(el){el.classList.add('in')})}

/* hero slider */
var slides=$$('.slide'),dots=$$('.dot'),cur=0,timer;
function go(i){slides[cur].classList.remove('on');dots[cur]&&dots[cur].classList.remove('on');cur=(i+slides.length)%slides.length;slides[cur].classList.add('on');dots[cur]&&dots[cur].classList.add('on')}
if(slides.length>1){timer=setInterval(function(){if(window.__c1pause||window.__c1hover)return;go(cur+1)},6000);dots.forEach(function(d,i){d.addEventListener('click',function(){go(i);clearInterval(timer)})})}

/* dates + whatsapp booking */
var WA='905067520286',EN=document.documentElement.lang==='en',AP=EN?'../assets/':'assets/';
function iso(d){return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0')}
function tr(s){if(!s)return '';var p=s.split('-');return EN?p[2]+'/'+p[1]+'/'+p[0]:p[2]+'.'+p[1]+'.'+p[0]}
function wa(t){window.open('https://wa.me/'+WA+'?text='+encodeURIComponent(t),'_blank','noopener')}
var today=new Date(),tom=new Date(Date.now()+864e5);
$$('input[type=date]').forEach(function(i){i.min=iso(today)});
var book=$('#book');
if(book){var g=book.elements.g,c=book.elements.c;g.value=iso(today);c.value=iso(tom);
 g.addEventListener('change',function(){if(c.value<=g.value){var d=new Date(g.value);d.setDate(d.getDate()+1);c.value=iso(d)}c.min=g.value});
 book.addEventListener('submit',function(e){e.preventDefault();
  wa(EN?'Hello, I would like to check room availability and prices at City One Hotel & Spa.\nCheck-in: '+tr(g.value)+'\nCheck-out: '+tr(c.value)+'\nAdults: '+book.elements.y.value+'\nChildren: '+book.elements.co.value:'Merhaba, City One Hotel & Spa için oda müsaitliği ve fiyat bilgisi almak istiyorum.\nGiriş: '+tr(g.value)+'\nÇıkış: '+tr(c.value)+'\nYetişkin: '+book.elements.y.value+'\nÇocuk: '+book.elements.co.value)})}
var form=$('#rezervasyon');
if(form){form.addEventListener('submit',function(e){e.preventDefault();var f=form.elements,err=$('#ferr');
  if(!f.ad.value.trim()||!f.kvkk.checked){err.hidden=false;err.textContent=EN?'Please enter your name and tick the privacy consent box.':'Lütfen adınızı yazın ve KVKK onayını işaretleyin.';return}
  err.hidden=true;var L=EN?['Hello, I am ','Request: ','Check-in: ','Check-out: ','Guests: ','Phone: ','Message: ']:['Merhaba, ben ','Talep: ','Giriş: ','Çıkış: ','Kişi sayısı: ','Telefon: ','Mesaj: '];var t=L[0]+f.ad.value.trim()+'.';
  if(f.oda.value)t+='\n'+L[1]+f.oda.value;if(f.g.value)t+='\n'+L[2]+tr(f.g.value);if(f.c.value)t+='\n'+L[3]+tr(f.c.value);
  t+='\n'+L[4]+f.k.value;if(f.tel.value)t+='\n'+L[5]+f.tel.value;if(f.m.value.trim())t+='\n'+L[6]+f.m.value.trim();wa(t)})}

/* room thumbs */
$$('.room').forEach(function(r){var main=$('.room-main img',r),a=$('.room-main',r);
 $$('.rt',r).forEach(function(b,i){b.addEventListener('click',function(){
  $$('.rt',r).forEach(function(x){x.classList.remove('on')});b.classList.add('on');
  main.src=AP+'img/'+b.dataset.src+'.webp';a.href=main.src;a.dataset.caption=$('img',b).alt;main.alt=$('img',b).alt})})});

/* gallery filter */
var fb=$$('.fbtn');
if(fb.length){fb.forEach(function(b){b.addEventListener('click',function(){
 fb.forEach(function(x){x.classList.toggle('on',x===b)});var f=b.dataset.f,vg=$('#vgrid'),ms=$('#masonry');
 if(f==='video'){ms.hidden=true;vg.hidden=false}else{vg.hidden=true;ms.hidden=false;$$('.gi').forEach(function(g){g.hidden=!(f==='hepsi'||g.dataset.c===f)});$$('video',vg).forEach(function(v){v.pause()})}})})}

/* lightbox */
var lbx=$('#lightbox'),lim=$('img',lbx),lcap=$('figcaption',lbx),list=[],idx=0;
function show(i){idx=(i+list.length)%list.length;lim.src=list[idx].href;lim.alt=list[idx].dataset.caption||'';lcap.textContent=list[idx].dataset.caption||''}
function open(a){var grp=a.dataset.lb;list=$$('a.lb[data-lb="'+grp+'"]').filter(function(x){return x.closest('[hidden]')===null});idx=list.indexOf(a);if(idx<0){list=[a];idx=0}show(idx);lbx.hidden=false;document.body.style.overflow='hidden';$('.lb-x',lbx).focus()}
function close(){lbx.hidden=true;document.body.style.overflow='';lim.src=''}
document.addEventListener('click',function(e){var a=e.target.closest('a.lb');if(a){e.preventDefault();open(a)}});
$('.lb-x',lbx).addEventListener('click',close);$('.lb-n',lbx).addEventListener('click',function(){show(idx+1)});$('.lb-p',lbx).addEventListener('click',function(){show(idx-1)});
lbx.addEventListener('click',function(e){if(e.target===lbx)close()});
document.addEventListener('keydown',function(e){if(lbx.hidden)return;if(e.key==='Escape')close();if(e.key==='ArrowRight')show(idx+1);if(e.key==='ArrowLeft')show(idx-1)});
var sx=0;lbx.addEventListener('touchstart',function(e){sx=e.touches[0].clientX},{passive:true});lbx.addEventListener('touchend',function(e){var d=e.changedTouches[0].clientX-sx;if(Math.abs(d)>50)show(idx+(d<0?1:-1))});

/* cookie */
var ck=$('#cookie');if(ck&&!store.get('c1-cookie')){ck.hidden=false;$('#cookieOk').addEventListener('click',function(){store.set('c1-cookie','1');ck.hidden=true})}
})();
