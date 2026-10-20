(function(){
'use strict';
var $=function(s,c){return (c||document).querySelector(s)},$$=function(s,c){return Array.prototype.slice.call((c||document).querySelectorAll(s))};
var EN=document.documentElement.lang==='en';
var store={get:function(k){try{return localStorage.getItem(k)}catch(e){return null}},set:function(k,v){try{localStorage.setItem(k,v)}catch(e){}}};

/* Çerez: reddet seçeneği */
var ck=$('#cookie'),no=$('#cookieNo');
if(no){no.addEventListener('click',function(){store.set('c1-cookie','0');ck.hidden=true})}

/* Mobil çubuk: hero üzerindeyken gizli (main.js body.at-hero yönetir; ana sayfa dışında hep görünür) */

/* Yukarı çık */
var tt=$('#totop');
if(tt){var f=function(){tt.classList.toggle('on',window.scrollY>900)};f();addEventListener('scroll',f,{passive:true});
 tt.addEventListener('click',function(){window.scrollTo({top:0,behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'auto':'smooth'})})}

/* Hero slider: duraklat/oynat + hover/odak duraklatma (WCAG 2.2.2). Zamanlayıcı main.js'te, bayrakları okur. */
var hero=$('#hero');
if(hero&&$$('.slide',hero).length>1){
 var paused=matchMedia('(prefers-reduced-motion:reduce)').matches;window.__c1pause=paused;
 var btn=document.createElement('button');btn.type='button';btn.className='slide-ctl';
 var PA='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 4h4v16H6zM14 4h4v16h-4z"/></svg>',PL='<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 4l14 8-14 8z"/></svg>';
 var lab=function(){btn.innerHTML=paused?PL:PA;btn.setAttribute('aria-label',paused?(EN?'Play slideshow':'Slaytı oynat'):(EN?'Pause slideshow':'Slaytı duraklat'))};
 lab();hero.appendChild(btn);
 btn.addEventListener('click',function(){paused=!paused;window.__c1pause=paused;lab()});
 hero.addEventListener('mouseenter',function(){window.__c1hover=true});hero.addEventListener('mouseleave',function(){window.__c1hover=false});
}

/* Lightbox: odak yönetimi (açılınca odak içeri, kapanınca geri; Tab dışarı kaçmaz) */
var lbx=$('#lightbox');
if(lbx){
 var last=null;
 document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a.lb');if(a)last=a},true);
 new MutationObserver(function(){if(lbx.hidden&&last&&last.focus){try{last.focus({preventScroll:true})}catch(e){}}}).observe(lbx,{attributes:true,attributeFilter:['hidden']});
 lbx.addEventListener('keydown',function(e){
  if(e.key!=='Tab')return;var f=$$('button',lbx);if(!f.length)return;
  var first=f[0],lastB=f[f.length-1];
  if(e.shiftKey&&document.activeElement===first){e.preventDefault();lastB.focus()}
  else if(!e.shiftKey&&document.activeElement===lastB){e.preventDefault();first.focus()}
 });
}

/* Formlar: telefon doğrulama + e-posta alternatifi */
var form=$('#rezervasyon');
if(form){
 var MAIL='info@cityonekayseri.com';
 var mailBtn=$('#mailSend');
 var build=function(){
  var f=form.elements,L=EN?['Hello, I am ','Request: ','Check-in: ','Check-out: ','Guests: ','Phone: ','Message: ']:['Merhaba, ben ','Talep: ','Giriş: ','Çıkış: ','Kişi sayısı: ','Telefon: ','Mesaj: '];
  var t=L[0]+f.ad.value.trim()+'.';
  if(f.oda.value)t+='\n'+L[1]+f.oda.value;if(f.g.value)t+='\n'+L[2]+f.g.value;if(f.c.value)t+='\n'+L[3]+f.c.value;
  t+='\n'+L[4]+f.k.value;if(f.tel.value)t+='\n'+L[5]+f.tel.value;if(f.m.value.trim())t+='\n'+L[6]+f.m.value.trim();return t};
 if(mailBtn){mailBtn.addEventListener('click',function(){
  var f=form.elements,err=$('#ferr');
  if(!f.ad.value.trim()||!f.kvkk.checked){err.hidden=false;err.textContent=EN?'Please enter your name and tick the privacy consent box.':'Lütfen adınızı yazın ve KVKK onayını işaretleyin.';return}
  err.hidden=true;
  location.href='mailto:'+MAIL+'?subject='+encodeURIComponent(EN?'Reservation request – City One Hotel & Spa':'Rezervasyon talebi – City One Hotel & Spa')+'&body='+encodeURIComponent(build())})}
 var tel=form.elements.tel;
 if(tel){tel.addEventListener('input',function(){tel.value=tel.value.replace(/[^\d+\s()-]/g,'')})}
 var g=form.elements.g,c=form.elements.c;
 if(g&&c){g.addEventListener('change',function(){if(c.value&&c.value<=g.value){var d=new Date(g.value);d.setDate(d.getDate()+1);c.value=d.toISOString().slice(0,10)}c.min=g.value})}
}
})();
