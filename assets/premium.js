(function(){'use strict';
var p=document.createElement('div');p.className='prog';document.body.appendChild(p);
function s(){var h=document.documentElement,m=h.scrollHeight-h.clientHeight;p.style.transform='scaleX('+(m>0?h.scrollTop/m:0)+')'}
s();addEventListener('scroll',s,{passive:true});
var f=document.querySelector('.feature-img');
if(f&&'IntersectionObserver' in window){new IntersectionObserver(function(e,o){if(e[0].isIntersecting){f.classList.add('in');o.disconnect()}},{threshold:.25}).observe(f)}else if(f){f.classList.add('in')}
var v=document.querySelector('.hero-video');
if(v){if(matchMedia('(prefers-reduced-motion:reduce)').matches){v.pause()}else{var t=v.play();if(t&&t.catch)t.catch(function(){})}}
})();
