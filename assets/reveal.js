/* Hace aparecer los textos de forma suave a medida que entran en pantalla.
   Sin JavaScript, o con «reducir movimiento» activado, todo se ve directamente. */
(function () {
  if (!('IntersectionObserver' in window)) return;
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var selectors = document.body.getAttribute('data-reveal') ||
    '.legal-side, .legal-body > *:not(.breadcrumb)';
  var items = Array.prototype.slice.call(document.querySelectorAll(selectors));
  if (!items.length) return;

  document.documentElement.classList.add('reveal-on');
  items.forEach(function (el) {
    el.classList.add('rv');
    // Pequeño escalonado entre elementos hermanos (máx. 0,3 s)
    var i = 0, prev = el.previousElementSibling;
    while (prev && i < 4) { if (prev.classList.contains('rv')) i++; prev = prev.previousElementSibling; }
    el.style.transitionDelay = (i * 0.08) + 's';
  });

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
  items.forEach(function (el) { io.observe(el); });
})();
