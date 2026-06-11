#!/usr/bin/env python3
"""Inject the v5 verification probe into the rendered report. Usage: probe_v5.py <render.html> <out.html>"""
import sys

PROBE = r"""
<script>
(function(){
  function $(s){return document.querySelector(s);}
  function $$(s){return Array.prototype.slice.call(document.querySelectorAll(s));}
  var cv=document.createElement('canvas'); cv.width=2; cv.height=2;
  var cx=cv.getContext('2d',{willReadFrequently:true});
  function norm(c){cx.fillStyle='#000';cx.fillStyle=c;return cx.fillStyle;}
  function parseC(c){
    cx.fillStyle='#fff'; cx.fillRect(0,0,2,2);
    try{cx.fillStyle=c;}catch(e){}
    cx.fillRect(0,0,2,2);
    var px=cx.getImageData(0,0,1,1).data;
    return [px[0],px[1],px[2],1];}
  function lum(rgb){function f(v){v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4);}
    return 0.2126*f(rgb[0])+0.7152*f(rgb[1])+0.0722*f(rgb[2]);}
  function ratio(fg,bg){var l1=lum(fg),l2=lum(bg);var hi=Math.max(l1,l2),lo=Math.min(l1,l2);
    return Math.round(((hi+0.05)/(lo+0.05))*100)/100;}
  function bgOf(el){
    var n=el;
    while(n && n.nodeType===1){
      var b=getComputedStyle(n).backgroundColor;
      if(b!=='rgba(0, 0, 0, 0)' && b!=='transparent') return parseC(b);
      n=n.parentElement;
    }
    return parseC(getComputedStyle(document.body).backgroundColor);
  }
  function pair(label,el,bgEl){
    if(!el) return {label:label,missing:true};
    var fg=parseC(getComputedStyle(el).color);
    var bg=bgOf(bgEl||el);
    return {label:label,fg:norm(getComputedStyle(el).color),ratio:ratio(fg,bg)};
  }
  function npair(label,colorStr,bgEl){ /* non-text: a color value vs an element's bg */
    var fg=parseC(colorStr); var bg=bgOf(bgEl||document.body);
    return {label:label,fg:norm(colorStr),ratio:ratio(fg,bg)};
  }
  function rect(el){if(!el)return null;var r=el.getBoundingClientRect();
    return {l:Math.round(r.left*100)/100,r:Math.round(r.right*100)/100,w:Math.round(r.width*100)/100,t:Math.round(r.top),h:Math.round(r.height*100)/100};}
  function visText(el){ /* text excluding .visually-hidden descendants */
    var out='';
    function walk(n){
      if(n.nodeType===3){out+=n.nodeValue;return;}
      if(n.nodeType!==1)return;
      if(n.classList&&n.classList.contains('visually-hidden'))return;
      var cs=getComputedStyle(n);
      if(cs.display==='none')return;
      for(var i=0;i<n.childNodes.length;i++)walk(n.childNodes[i]);
    }
    walk(el); return out;
  }

  function collectColors(theme){
    var o={theme:theme};
    o.fSev=$$('.f-sev').slice(0,2).map(function(e){return pair('f-sev '+e.className,e);});
    var fv=$('.f-sev.rel-violates'), ft=$('.f-sev.rel-tension');
    o.fSevViol=pair('f-sev-violates',fv); o.fSevTens=pair('f-sev-tension',ft);
    var dv=$('.fe-dot.rel-violates'), dt=$('.fe-dot.rel-tension');
    o.dotViol=dv?npair('fe-dot-violates',getComputedStyle(dv).backgroundColor,dv):null;
    o.dotTens=dt?npair('fe-dot-tension',getComputedStyle(dt).backgroundColor,dt):null;
    o.feName=pair('fe-item-name',$('.fe-item'));
    o.fId=pair('f-id',$('.f-id'));
    o.scfOrd=pair('scf-ord',$('.scf-ord'));
    var na=$('.pagenav a'); o.navRest=pair('pagenav-resting',na);
    var cur=$('.pagenav a[aria-current="true"]');
    o.navActive=pair('pagenav-active',cur);
    o.navAccentTick=cur?npair('accent-tick',getComputedStyle(cur,'::after').backgroundColor,cur):null;
    o.navHoverInk=npair('pagenav-hover-ink',getComputedStyle(document.body).color,na); /* --tx vs bg */
    o.body=pair('body-text',$('.f-explain p'));
    o.relViol=pair('scf-rel-violates',$('.scf-rel.rel-violates'));
    o.relTens=pair('scf-rel-tension',$('.scf-rel.rel-tension'));
    o.conf=pair('f-conf',$('.f-conf'));
    try{
      var ss=getComputedStyle(document.body,'::selection');
      o.selection={bg:norm(ss.backgroundColor), fg:norm(ss.color)};
    }catch(e){}
    return o;
  }

  function run(){
    var st=document.createElement('style');
    st.textContent='*,*::before,*::after{transition:none!important;animation:none!important} html{scroll-behavior:auto!important}';
    document.head.appendChild(st);
    var out={};
    out.url=location.href; out.vw=window.innerWidth; out.vh=window.innerHeight;
    out.scrollWidth=document.documentElement.scrollWidth;
    out.hasHScroll=document.documentElement.scrollWidth>window.innerWidth;

    /* ---------- MEASURE ---------- */
    var edgeEl=$('header.report .content-col');
    var edge=rect(edgeEl).l;
    out.contentEdge=edge;
    var lefts={};
    [['h1','h1.system'],['dek','.dek'],['mastMeta','.mast-meta'],['sumCap','.sum-cap'],
     ['summaryP','.summary .content-col p'],['scCap','.sc-cap'],['ratingsKey','.ratings-key'],
     ['scName','.sc-name'],['scfLink','.sc-findings a'],['fTitle','.f-title'],['fExplain','.f-explain p'],
     ['figCode','figure.code'],['citeBody','.cite-body'],['remedyLi','ul.remedy li'],
     ['structuralP','.structural p'],['mCap','.m-cap'],['lead','.movement p.lead'],
     ['plainLi','ul.plain li'],['footNav','.foot-nav'],['footP','footer.report .content-col p:not(.foot-nav)']
    ].forEach(function(d){ var e=$(d[1]); lefts[d[0]]=e?rect(e).l:null; });
    out.lefts=lefts;
    var rights={};
    [['fExplain','.f-explain p'],['figCode','figure.code'],['lead','.movement p.lead'],
     ['summaryP','.summary .content-col p'],['dek','.dek'],['mastMeta','.mast-meta'],
     ['structural','.structural'],['remedy','ul.remedy'],['plainUl','ul.plain'],
     ['contentCol','header.report .content-col'],['footTop','footer.report .content-col']
    ].forEach(function(d){ var e=$(d[1]); rights[d[0]]=e?rect(e).r:null; });
    out.rights=rights;
    out.proseTarget=edge+564.8;
    out.hrs=$$('hr').map(function(e){var r=rect(e);return {cls:e.className,l:r.l,r:r.r};});
    out.scNoteExists=!!$('.sc-note');

    /* ---------- RAIL ---------- */
    var firstFinding=$('.finding');
    var fr=firstFinding.querySelector('.f-rail');
    out.railRect=rect(fr);
    out.railGapToEdge=edge-out.railRect.r;
    var railReport=[];
    $$('.finding').forEach(function(f){
      var r=f.querySelector('.f-rail');
      var items=Array.prototype.slice.call(r.querySelectorAll('.fe-item')).map(function(it){
        var rr=rect(it);
        var lines=it.getClientRects().length;
        return {vis:visText(it).trim(), title:it.title,
          hasDot:!!it.querySelector('.fe-dot'), dotCls:(it.querySelector('.fe-dot')||{}).className||null,
          hasHidden:!!it.querySelector('.visually-hidden'),
          hiddenTxt:(it.querySelector('.visually-hidden')||{}).textContent||null,
          w:rr.w, h:rr.h, lines:lines, overflowsRail:rr.r>r.getBoundingClientRect().right+0.5};
      });
      var sev=r.querySelector('.f-sev');
      railReport.push({
        id:f.id,
        ordinal:(r.querySelector('.f-id')||{}).textContent,
        starHref:(r.querySelector('a.f-star')||{getAttribute:function(){return null}}).getAttribute('href'),
        starLabel:(r.querySelector('a.f-star')||{getAttribute:function(){return null}}).getAttribute('aria-label'),
        sevText:sev?sev.textContent:null, sevCls:sev?sev.className:null,
        conf:(r.querySelector('.f-conf')||{}).textContent||null,
        engagesLabel:(r.querySelector('.fe-label')||{}).textContent||null,
        items:items,
        visRailText:visText(r).replace(/\s+/g,' ').trim()
      });
    });
    out.rails=railReport;

    /* ---------- ORDINALS ---------- */
    out.domOrdinals=$$('.finding .f-id').map(function(e){return e.textContent;});
    out.findingIds=$$('.finding').map(function(e){return e.id;});
    out.scorecard=$$('.sc-findings a').map(function(a){
      return {href:a.getAttribute('href'), ord:(a.querySelector('.scf-ord')||{}).textContent||null,
        rel:(a.querySelector('.scf-rel')||{}).textContent||null,
        aria:a.getAttribute('aria-label'),
        title:((a.querySelector('.scf-title')||{}).textContent||'').slice(0,40)};
    });
    out.droppedLis=$$('ul.plain.dropped li').map(function(li){return visText(li).replace(/\s+/g,' ').trim();});
    out.mergedLink=(function(){var a=$('ul.plain.dropped a'); return a?{txt:a.textContent,href:a.getAttribute('href')}:null;})();
    /* raw F-token scan over visible body text (excluding code evidence + this probe) */
    var rawTokens=[];
    (function walk(n){
      if(n.nodeType===3){
        var m=n.nodeValue.match(/\bF\d+\b/g);
        if(m){
          var p=n.parentElement;
          var inCode=p&&(p.closest('figure.code')||p.closest('script')||p.closest('style'));
          var hidden=p&&p.closest('.visually-hidden');
          var cs=p?getComputedStyle(p):null;
          if(!inCode&&!hidden&&(!cs||cs.display!=='none'))
            rawTokens.push({tok:m.join(','), ctx:n.nodeValue.slice(0,80), where:p?(p.className||p.tagName):'?'});
        }
        return;
      }
      if(n.nodeType!==1||n.tagName==='SCRIPT'||n.tagName==='STYLE')return;
      for(var i=0;i<n.childNodes.length;i++)walk(n.childNodes[i]);
    })(document.body);
    out.rawFTokens=rawTokens;

    /* ---------- NAV ---------- */
    var nav=$('.pagenav');
    out.nav={exists:!!nav};
    if(nav){
      var ns=getComputedStyle(nav);
      out.nav.display=ns.display; out.nav.position=ns.position; out.nav.zIndex=ns.zIndex;
      out.nav.pointerEvents=ns.pointerEvents;
      out.nav.rect=rect(nav);
      out.nav.items=$$('.pagenav a').map(function(a){
        var r=rect(a);
        return {txt:a.textContent, href:a.getAttribute('href'), aria:a.getAttribute('aria-label'),
          title:a.title||null, w:r?r.w:null, h:r?r.h:null,
          pe:getComputedStyle(a).pointerEvents,
          cur:a.getAttribute('aria-current')};
      });
      out.nav.clearsRail=out.nav.rect.r < out.railRect.l;
      var tgr=rect($('#theme-toggle'));
      out.nav.toggleZ=getComputedStyle($('#theme-toggle')).zIndex;
    }
    out.codaId=(function(){var c=document.getElementById('coda');return c?{tag:c.tagName,parent:c.parentElement.id}:null;})();

    /* ---------- regression sweep ---------- */
    out.reg={
      favicon:($('link[rel="icon"]')||{href:''}).href.slice(0,30),
      metaDesc:!!($('meta[name="description"]')||{}).content,
      ogTitle:($('meta[property="og:title"]')||{}).content||null,
      ogDesc:!!($('meta[property="og:description"]')||{}).content,
      twCard:($('meta[name="twitter:card"]')||{}).content||null,
      copyBtns:$$('.code-copy').length,
      codeFigs:$$('figure.code').length,
      findings:$$('.finding').length,
      asterisms:$$('.f-aster').length,
      scGroups:$$('.sc-group').length,
      scChips:$$('.sc-row .chip').map(function(e){return e.textContent.trim();}),
      scCounts:$$('.sc-count').map(function(e){return visText(e).trim();}),
      footNav:!!$('.foot-nav'),
      footNavTxt:$('.foot-nav')?$('.foot-nav').textContent.trim():null,
      skipLink:!!$('.skip-link'),
      toggleTitle:($('#theme-toggle')||{}).title,
      toggleKeys:$('#theme-toggle')?$('#theme-toggle').getAttribute('aria-keyshortcuts'):null,
      verdictPill:$('.verdict-image')?$('.verdict-image').textContent.trim():null,
      external:performance.getEntriesByType('resource').map(function(r){return r.name;})
        .filter(function(n){return !/^http:\/\/localhost:8742\//.test(n);})
    };
    var pres=$$('figure.code pre');
    out.reg.code={n:pres.length,overflowing:0,hasMore:0,tabindexed:0,roleRegion:0};
    pres.forEach(function(p){
      if(p.scrollWidth>p.clientWidth+1)out.reg.code.overflowing++;
      if(p.parentElement.classList.contains('has-more'))out.reg.code.hasMore++;
      if(p.hasAttribute('tabindex'))out.reg.code.tabindexed++;
      if(p.getAttribute('role')==='region')out.reg.code.roleRegion++;
    });

    /* ---------- colors: theme 1 (as loaded) ---------- */
    var theme0=document.documentElement.getAttribute('data-theme');
    out.colors1=collectColors(theme0);

    /* ---------- :target + aria-current sequence (async) ---------- */
    var seq=[];
    out.navCurrentInitial=$$('.pagenav a[aria-current="true"]').map(function(a){return a.textContent;});
    location.hash='#f-F8'; /* ordinal 04 */
    setTimeout(function(){
      var f8=document.getElementById('f-F8');
      var tcol=getComputedStyle(f8.querySelector('.f-title')).color;
      out.target={id:'f-F8', titleColor:norm(tcol), top:Math.round(f8.getBoundingClientRect().top),
        matchesTargetSel:!!document.querySelector('.finding:target')&&document.querySelector('.finding:target').id==='f-F8'};
      setTimeout(function(){
        out.navCurrentAfterScroll=$$('.pagenav a[aria-current="true"]').map(function(a){return a.textContent;});
        out.navCurrentCount=$$('.pagenav a[aria-current="true"]').length;
        /* theme flip via D key */
        document.body.dispatchEvent(new KeyboardEvent('keydown',{key:'d',bubbles:true}));
        out.themeAfterD=document.documentElement.getAttribute('data-theme');
        setTimeout(function(){
          out.colors2=collectColors(out.themeAfterD);
          try{localStorage.removeItem('mh-theme');}catch(e){}
          var pre=document.createElement('script');
          pre.type='text/plain'; pre.id='__probe__';
          pre.textContent='PROBE_START'+JSON.stringify(out)+'PROBE_END';
          document.body.appendChild(pre);
        },350);
      },900);
    },300);
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
    var done=document.querySelector('.pagenav');
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
