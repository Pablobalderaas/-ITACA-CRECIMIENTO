/* Menú superior: se oculta al bajar y reaparece al subir un poco.
   data-autohide="stick": el menú va dentro de la portada y se fija arriba al hacer scroll.
   data-autohide="sticky": la cabecera ya está fija (sticky) y solo se oculta o se muestra. */
(function () {
  var el = document.querySelector('[data-autohide]');
  if (!el) return;
  var stick = el.getAttribute('data-autohide') === 'stick';
  var last = window.pageYOffset;
  var ticking = false;

  function update() {
    var y = Math.max(window.pageYOffset, 0);
    var h = el.offsetHeight;
    var open = el.classList.contains('open');

    if (stick) {
      var shouldStick = y > h * 2;
      if (shouldStick && !el.classList.contains('stuck')) {
        // Se fija ya oculto y sin animación, para que no parpadee
        el.classList.add('no-anim', 'stuck', 'nav-hidden');
        requestAnimationFrame(function () { el.classList.remove('no-anim'); });
      } else if (!shouldStick && el.classList.contains('stuck')) {
        el.classList.remove('stuck', 'nav-hidden');
      }
    }

    if (y > last + 2 && y > h && !open) {
      el.classList.add('nav-hidden');          // bajando
    } else if (y < last - 2 || y <= h) {
      el.classList.remove('nav-hidden');       // subiendo o arriba del todo
    }
    last = y;
    ticking = false;
  }

  window.addEventListener('scroll', function () {
    if (!ticking) { requestAnimationFrame(update); ticking = true; }
  }, { passive: true });
})();
