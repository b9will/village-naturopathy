(function () {
  "use strict";

  // Mobile menu toggle
  var nav = document.getElementById("nav");
  var toggle = nav && nav.querySelector(".nav-toggle");
  if (nav && toggle) {
    toggle.addEventListener("click", function () {
      var open = nav.getAttribute("data-open") === "true";
      nav.setAttribute("data-open", String(!open));
      toggle.setAttribute("aria-expanded", String(!open));
    });
    nav.querySelectorAll(".nav-links a, .nav-cta").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.setAttribute("data-open", "false");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  // Scroll-triggered reveal animations
  if ("IntersectionObserver" in window) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15, rootMargin: "0px 0px -40px 0px" }
    );
    document.querySelectorAll(".reveal, .reveal-stagger").forEach(function (el) {
      observer.observe(el);
    });
  } else {
    document.querySelectorAll(".reveal, .reveal-stagger").forEach(function (el) {
      el.classList.add("is-visible");
    });
  }

  // Booking region modal
  var modalHTML = '<div class="modal-overlay" id="book-modal" role="dialog" aria-modal="true" aria-labelledby="modal-title">' +
    '<div class="modal" style="position:relative">' +
    '<button class="modal-close" aria-label="Close" type="button">' +
    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M18 6L6 18M6 6l12 12"/></svg></button>' +
    '<h2 id="modal-title">Where are you located?</h2>' +
    '<p>Choose your region to book with the correct clinic.</p>' +
    '<div class="modal-options">' +
    '<a class="modal-option" href="https://villagenaturopathy.janeapp.com/locations/village-naturopathy/book#staff_member/1" target="_blank" rel="noopener noreferrer">' +
    '<span class="modal-option-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z"/><path d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z"/></svg></span>' +
    '<span class="modal-option-text"><strong>I’m in Ontario</strong><span>Virtual naturopathic consultations</span></span></a>' +
    '<a class="modal-option" href="https://villagenaturopathy.janeapp.com/locations/village-naturopathy-uk/book#staff_member/1" target="_blank" rel="noopener noreferrer">' +
    '<span class="modal-option-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21a9.004 9.004 0 008.716-6.747M12 21a9.004 9.004 0 01-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 017.843 4.582M12 3a8.997 8.997 0 00-7.843 4.582m15.686 0A11.953 11.953 0 0112 10.5c-2.998 0-5.74-1.1-7.843-2.918m15.686 0A8.959 8.959 0 0121 12c0 .778-.099 1.533-.284 2.253m0 0A17.919 17.919 0 0112 16.5a17.92 17.92 0 01-8.716-2.247m0 0A9.015 9.015 0 013 12c0-1.605.42-3.113 1.157-4.418"/></svg></span>' +
    '<span class="modal-option-text"><strong>I’m in the UK</strong><span>Virtual naturopathic consultations</span></span></a>' +
    '</div></div></div>';

  if (!document.querySelector('.booking-split')) {
    document.body.insertAdjacentHTML('beforeend', modalHTML);
    var overlay = document.getElementById('book-modal');
    var closeBtn = overlay.querySelector('.modal-close');

    function openModal(e) {
      e.preventDefault();
      overlay.classList.add('open');
      document.body.style.overflow = 'hidden';
      closeBtn.focus();
    }
    function closeModal() {
      overlay.classList.remove('open');
      document.body.style.overflow = '';
    }

    document.querySelectorAll('a[href="book.html"]').forEach(function (link) {
      if (!link.closest('.footer-col') && !link.closest('.footer-bottom-links') && !link.classList.contains('nav-cta')) {
        link.addEventListener('click', openModal);
      }
    });

    closeBtn.addEventListener('click', closeModal);
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) closeModal();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && overlay.classList.contains('open')) closeModal();
    });
  }

  // Booking form — show confirmation on submit
  var form = document.getElementById("booking-form");
  var confirm = document.getElementById("booking-confirm");
  if (form && confirm) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      form.closest(".booking-split").setAttribute("hidden", "");
      confirm.removeAttribute("hidden");
      window.scrollTo(0, 0);
    });
  }

  var prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Animated stat counters
  if ("IntersectionObserver" in window) {
    var statObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        var raw = el.textContent.trim();
        var suffix = raw.replace(/[0-9]/g, "");
        var target = parseInt(raw, 10);
        if (isNaN(target)) return;
        statObserver.unobserve(el);
        if (prefersReducedMotion) return;
        var start = performance.now();
        var duration = 1400;
        function tick(now) {
          var t = Math.min((now - start) / duration, 1);
          var ease = 1 - Math.pow(1 - t, 3);
          el.textContent = Math.round(target * ease) + suffix;
          if (t < 1) requestAnimationFrame(tick);
        }
        el.textContent = "0" + suffix;
        requestAnimationFrame(tick);
      });
    }, { threshold: 0.5 });
    document.querySelectorAll(".stat-number").forEach(function (el) {
      statObserver.observe(el);
    });
  }

  // Scroll progress bar
  var progressBar = document.createElement("div");
  progressBar.className = "scroll-progress";
  document.body.appendChild(progressBar);

  // Floating pill navbar — hide/show nav links on scroll direction
  var navLinks = document.querySelector(".nav-links");
  var lastScrollY = 0;

  // Parallax hero image
  var heroBg = document.querySelector(".hero-bg img");
  var heroSection = document.querySelector(".hero");

  // Back-to-top button
  var topBtn = document.createElement("button");
  topBtn.className = "back-to-top";
  topBtn.setAttribute("aria-label", "Back to top");
  topBtn.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 15l-6-6-6 6"/></svg>';
  document.body.appendChild(topBtn);
  topBtn.addEventListener("click", function () {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });

  // Unified scroll handler (rAF-throttled)
  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      var scrollY = window.scrollY;
      var docHeight = document.documentElement.scrollHeight - window.innerHeight;

      // Progress bar
      if (docHeight > 0) {
        progressBar.style.transform = "scaleX(" + (scrollY / docHeight) + ")";
      }

      // Nav pill hide/show (brand + CTA stay visible)
      if (navLinks) {
        if (scrollY > 200 && scrollY > lastScrollY) {
          navLinks.classList.add("nav-hidden");
        } else {
          navLinks.classList.remove("nav-hidden");
        }
        lastScrollY = scrollY;
      }

      // Parallax hero
      if (heroBg && heroSection && !prefersReducedMotion) {
        var heroH = heroSection.offsetHeight;
        if (scrollY < heroH) {
          heroBg.style.transform = "translateY(" + (scrollY * 0.3) + "px)";
        }
      }

      // Back-to-top visibility
      if (scrollY > 600) {
        topBtn.classList.add("visible");
      } else {
        topBtn.classList.remove("visible");
      }

      ticking = false;
    });
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Reveal nav pill when mouse approaches top edge
  document.addEventListener("mousemove", function (e) {
    if (e.clientY < 80 && navLinks) {
      navLinks.classList.remove("nav-hidden");
    }
  });
})();
