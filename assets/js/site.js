(function () {
  // Mobile navigation
  var toggle = document.querySelector('.nav-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var open = document.body.classList.toggle('nav-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && document.body.classList.contains('nav-open')) toggle.click();
    });
  }

  // Photo frames: show the real photo when it loads, keep the designed panel otherwise
  document.querySelectorAll('.photo img').forEach(function (img) {
    var frame = img.closest('.photo');
    function ok () { frame.classList.add('has-img'); }
    function fail () { frame.classList.remove('has-img'); img.remove(); }
    if (img.complete) { img.naturalWidth ? ok() : fail(); }
    else { img.addEventListener('load', ok); img.addEventListener('error', fail); }
  });

  // Bail cost estimator (How Bail Works page)
  var est = document.querySelector('[data-estimator]');
  if (est) {
    var input = est.querySelector('input');
    var out = est.querySelector('[data-out]');
    var fmt = function (n) { return '$' + Math.round(n).toLocaleString('en-US'); };
    var update = function () {
      var bond = parseFloat(String(input.value).replace(/[^0-9.]/g, '')) || 0;
      var premium = Math.max(bond * 0.12, bond > 0 ? 120 : 0);
      out.textContent = fmt(premium);
    };
    input.addEventListener('input', update);
    update();
  }
})();
