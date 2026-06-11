#!/usr/bin/env python3
"""Inject a layout/contrast probe into the rendered report. Usage: probe_inject.py <render.html> <out.html>"""
import sys

PROBE = r"""
<script>
(function(){
  function $(s){return document.querySelector(s);}
  function $$(s){return Array.prototype.slice.call(document.querySelectorAll(s));}
  var cv=document.createElement('canvas'); cv.width=2; cv.height=2;
  var cx=cv.getContext('2d',{willReadFrequently:true});
  function norm(c){cx.fillStyle='#000';cx.fillStyle=c;return cx.fillStyle;}
  function parseC(c){ // pixel-accurate: handles oklab/color-mix serializations
    cx.clearRect(0,0,2,2);
    cx.fillStyle='#fff'; cx.fillRect(0,0,2,2);
    try{cx.fillStyle=c;}catch(e){}
    cx.fillRect(0,0,2,2);
    var px=cx.getImageData(0,0,1,1).data;
    var aProbe=px[3]/255;
    // alpha: redo over black to detect translucency
    cx.fillStyle='#000'; cx.fillRect(0,0,2,2);
    try{cx.fillStyle=c;}catch(e){}
    cx.fillRect(0,0,2,2);
    var pb=cx.getImageData(0,0,1,1).data;
    // if color is opaque, white-composite == black-composite
    var alpha=(px[0]===pb[0]&&px[1]===pb[1]&&px[2]===pb[2])?1:1; // composited values returned
    return [px[0],px[1],px[2],1];}
  function lum(rgb){function f(v){v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4);}
    return 0.2126*f(rgb[0])+0.7152*f(rgb[1])+0.0722*f(rgb[2]);}
  function blend(fg,bg){var a=fg[3];return [fg[0]*a+bg[0]*(1-a),fg[1]*a+bg[1]*(1-a),fg[2]*a+bg[2]*(1-a),1];}
  function ratio(fg,bg){fg=blend(fg,bg);var l1=lum(fg),l2=lum(bg);var hi=Math.max(l1,l2),lo=Math.min(l1,l2);
    return Math.round(((hi+0.05)/(lo+0.05))*100)/100;}
  function bgOf(el){ // walk up for first non-transparent background
    var n=el;
    while(n && n.nodeType===1){
      var b=getComputedStyle(n).backgroundColor;
      var p=parseC(b);
      if(p[3]>0 && !(p[3]===0)) { if(getComputedStyle(n).backgroundColor!=='rgba(0, 0, 0, 0)') return p; }
      n=n.parentElement;
    }
    return parseC(getComputedStyle(document.body).backgroundColor);
  }
  function pair(label,el,bgEl){
    if(!el) return {label:label,missing:true};
    var fg=parseC(getComputedStyle(el).color);
    var bg=bgOf(bgEl||el);
    return {label:label,fg:norm(getComputedStyle(el).color),bg:'rgb('+Math.round(bg[0])+','+Math.round(bg[1])+','+Math.round(bg[2])+')',ratio:ratio(fg,bg)};
  }
  function left(sel){var e=$(sel);return e?Math.round(e.getBoundingClientRect().left*100)/100:null;}
  function rect(el){var r=el.getBoundingClientRect();return {l:Math.round(r.left*10)/10,r:Math.round(r.right*10)/10,w:Math.round(r.width*10)/10,t:Math.round(r.top)};}

  function ensureSynthetic(){
    if(!document.querySelector('.chip-honors')){
      var c=document.createElement('span'); c.className='chip chip-honors'; c.textContent='Honors';
      c.id='__synth-chip__'; document.querySelector('.scorecard').appendChild(c);
    }
    if(!document.querySelector('.vi-honors')){
      var v=document.createElement('span'); v.className='verdict-image vi-honors'; v.textContent='synthetic';
      document.querySelector('.scorecard').appendChild(v);
      var w=document.createElement('span'); w.className='verdict-image vi-tension'; w.textContent='synthetic';
      document.querySelector('.scorecard').appendChild(w);
    }
  }
  function collectColors(){
    ensureSynthetic();
    var o={};
    o.viHonors=pair('vi-honors',$('.vi-honors'));
    o.viTension=pair('vi-tension',$('.vi-tension'));
    o.theme=document.documentElement.getAttribute('data-theme');
    o.body=pair('body-text',$('.f-explain p')||document.body);
    o.tx2=pair('tx2-muted',$('.dek'));
    o.scNum=pair('sc-num',$('.sc-num'));
    o.relViol=pair('scf-rel-violates',$('.scf-rel.rel-violates'));
    o.relTens=pair('scf-rel-tension',$('.scf-rel.rel-tension'));
    o.feViol=pair('fe-rel-violates',$('.fe-rel.rel-violates'));
    o.feTens=pair('fe-rel-tension',$('.fe-rel.rel-tension'));
    o.figcap=pair('figcaption',$('figure.code figcaption .loc'),$('figure.code'));
    o.codePlain=pair('code-plain',$('figure.code code'),$('figure.code'));
    ['t-cm','t-st','t-nu','t-kw','t-ty','t-fn','t-bi'].forEach(function(c){
      o[c]=pair(c,$('figure.code .'+c),$('figure.code'));
    });
    o.linkMast=pair('mast-link',$('.mast-meta .mm-value a'));
    o.linkFoot=pair('footer-link',$('footer.report .content-col p:not(.foot-nav) a'));
    o.footNav=pair('foot-nav-link',$('.foot-nav a'));
    o.chipH=pair('chip-honors',$('.chip-honors'),$('.chip-honors'));
    o.chipT=pair('chip-tension',$('.chip-tension'),$('.chip-tension'));
    o.chipV=pair('chip-violates',$('.chip-violates'),$('.chip-violates'));
    o.rkH=pair('rk-honors',$('.rk-honors'));
    o.rkT=pair('rk-tension',$('.rk-tension'));
    o.rkV=pair('rk-violates',$('.rk-violates'));
    o.verdictPill=pair('verdict-image',$('.verdict-image'));
    o.fTitle=pair('f-title',$('.f-title'));
    o.toggle=pair('theme-toggle',$('#theme-toggle'));
    // ::selection
    try{
      var ss=getComputedStyle(document.body,'::selection');
      var sb=parseC(ss.backgroundColor), sc=parseC(ss.color);
      var bodyBg=parseC(getComputedStyle(document.body).backgroundColor);
      o.selection={bg:norm(ss.backgroundColor), fg:norm(ss.color),
        ratio:ratio(sc, blend(sb,bodyBg))};
    }catch(e){o.selection={err:String(e)};}
    return o;
  }

  function run(){
    // freeze-proof sampling: kill transitions so theme switches resolve instantly
    var st=document.createElement('style');
    st.textContent='*,*::before,*::after{transition:none!important;animation:none!important}';
    document.head.appendChild(st);
    var out={};
    out.url=location.href; out.vw=window.innerWidth;
    // ---------- structure ----------
    out.counts={
      findings:$$('.finding').length,
      asterisms:$$('.f-aster').length,
      scGroups:$$('.sc-group').length,
      scFindLinks:$$('.sc-findings a').length,
      feItems:$$('.fe-item').length,
      engagesLabels:$$('.fe-label').length,
      codeFigs:$$('figure.code').length,
      copyBtns:$$('.code-copy').length,
      cites:$$('.cite').length,
      remedies:$$('ul.remedy').length,
      hrs:$$('hr').length
    };
    out.scCounts=$$('.sc-count').map(function(e){return e.textContent.trim();});
    out.scChips=$$('.sc-row .chip').map(function(e){return e.textContent.trim();});
    out.scNames=$$('.sc-name').map(function(e){return e.textContent.trim();});
    out.findingIds=$$('.finding').map(function(e){return e.id;});
    out.verdictPillText=$('.verdict-image')?$('.verdict-image').textContent.trim():null;
    out.title=document.title;
    out.metaDesc=($('meta[name="description"]')||{}).content||null;
    out.ogTitle=($('meta[property="og:title"]')||{}).content||null;
    out.ogDesc=($('meta[property="og:description"]')||{}).content||null;
    out.twCard=($('meta[name="twitter:card"]')||{}).content||null;
    var fav=$('link[rel="icon"]'); out.favicon=fav?fav.href.slice(0,30):null;
    out.faviconIsData=fav?/^data:image\/svg\+xml/.test(fav.href):false;
    out.noscript=$$('noscript').length;
    var tg=$('#theme-toggle');
    out.toggleTitle=tg?tg.title:null;
    out.toggleKeys=tg?tg.getAttribute('aria-keyshortcuts'):null;
    out.toggleLabel=tg?tg.textContent:null;
    out.toggleAria=tg?tg.getAttribute('aria-label'):null;
    out.externalResources=performance.getEntriesByType('resource').map(function(r){return r.name;})
      .filter(function(n){return !/^http:\/\/localhost:8742\//.test(n);});

    // ---------- geometry ----------
    var edge=left('header.report .content-col');
    out.contentEdge=edge;
    var g={};
    g.h1=left('h1.system'); g.dek=left('.dek'); g.mastMeta=left('.mast-meta');
    g.sumCap=left('.sum-cap'); g.verdict=left('.sum-verdict'); g.summaryP=left('.summary p');
    g.scCap=left('.sc-cap'); g.ratingsKey=left('.ratings-key');
    g.fTitle=left('.f-title'); g.fExplain=left('.f-explain p');
    g.citeBody=left('.cite-body'); g.citeQuote=left('.cite-quote');
    g.remedyLi=left('ul.remedy li'); g.structuralP=left('.structural p');
    g.footNav=left('.foot-nav'); g.footerP=left('footer.report .content-col p:not(.foot-nav)');
    g.mCaps=$$('.m-cap').map(function(e){return rect(e).l;});
    g.scNamesL=$$('.sc-name').map(function(e){return rect(e).l;});
    g.plainLiText=$$('ul.plain li').slice(0,3).map(function(e){
      // text starts after the 1.6rem padding; measure the li box left
      return rect(e).l;});
    out.geom=g;
    out.hrs=$$('hr').map(function(e){var r=rect(e);return {cls:e.className,l:r.l,r:r.r,w:r.w};});
    // rails must sit left of edge
    out.rail={};
    var fr=$('.f-rail'); out.rail.fRail=fr?rect(fr):null;
    var refs=$$('.cite-ref').filter(function(e){return e.textContent.trim();});
    out.rail.citeRef=refs.length?rect(refs[0]):null;
    var mk=$('.sc-marker'); out.rail.scMarker=mk?rect(mk):null;
    var layout=$('.layout'); out.layout=layout?rect(layout):null;
    out.toggleRect=tg?rect(tg):null;
    out.togglePos=tg?getComputedStyle(tg).position:null;
    // code overflow / fade
    var pres=$$('figure.code pre');
    out.code={n:pres.length, overflowing:0, hasMore:0, tabindexed:0};
    pres.forEach(function(p){
      if(p.scrollWidth>p.clientWidth+1){out.code.overflowing++;}
      if(p.parentElement.classList.contains('has-more')) out.code.hasMore++;
      if(p.hasAttribute('tabindex')) out.code.tabindexed++;
    });
    // finding permalink stars
    out.permalinks=$$('.f-rail a.f-star').map(function(a){return a.getAttribute('href');});

    // ---------- colors: dark (default) ----------
    out.dark=collectColors();
    // toggle click -> light, then wait out the 0.2s body transition
    if(tg){ tg.click(); }
    out.afterClickTheme=document.documentElement.getAttribute('data-theme');
    out.afterClickLabel=tg?tg.textContent:null;
    setTimeout(function(){
      out.light=collectColors();
      // D key -> back to dark
      document.body.dispatchEvent(new KeyboardEvent('keydown',{key:'d',bubbles:true}));
      out.afterDKeyTheme=document.documentElement.getAttribute('data-theme');
      try{localStorage.setItem('mh-theme','dark');}catch(e){}

      out.scrollY=window.scrollY;
      var tgt=location.hash?document.getElementById(decodeURIComponent(location.hash.slice(1))):null;
      if(tgt){
        out.target={id:tgt.id, top:Math.round(tgt.getBoundingClientRect().top),
          titleColor:getComputedStyle(tgt.querySelector('.f-title')).color};
      }
      var pre=document.createElement('script');
      pre.type='text/plain'; pre.id='__probe__';
      pre.textContent='PROBE_START'+JSON.stringify(out)+'PROBE_END';
      document.body.appendChild(pre);
    },700);
  }
  function attempt(){
    try{run();}catch(e){
      var pre=document.createElement('script');pre.type='text/plain';pre.id='__probe__';
      pre.textContent='PROBE_START'+JSON.stringify({error:String(e),stack:e&&e.stack})+'PROBE_END';
      document.body.appendChild(pre);}
  }
  var tries=0;
  var iv=setInterval(function(){
    tries++;
    var done=document.querySelector('footer.report .content-col');
    if(done||tries>40){ clearInterval(iv); setTimeout(attempt,600); }
  },250);
})();
</script>
"""

src, out = sys.argv[1], sys.argv[2]
html = open(src, encoding="utf-8").read()
assert "</body>" in html
html = html.replace("</body>", PROBE + "\n</body>")
open(out, "w", encoding="utf-8").write(html)
print("probe written:", out)
