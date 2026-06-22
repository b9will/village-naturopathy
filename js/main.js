(function () {
  "use strict";

  var prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Mobile menu toggle
  var nav = document.getElementById("nav");
  var toggle = nav && nav.querySelector(".nav-toggle");
  var hamburgerIcon = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>';
  var closeIcon = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><path d="M18 6L6 18M6 6l12 12"/></svg>';

  function closeMenu() {
    nav.setAttribute("data-open", "false");
    toggle.setAttribute("aria-expanded", "false");
    toggle.innerHTML = hamburgerIcon;
    document.body.style.overflow = "";
  }

  if (nav && toggle) {
    // Inject CTA + social links into nav-links for mobile
    var navLinksEl = nav.querySelector(".nav-links");
    if (navLinksEl) {
      var mobileCta = document.createElement("li");
      mobileCta.className = "mobile-cta";
      mobileCta.innerHTML = '<a class="btn btn--warm" href="book.html">Book now</a>';
      navLinksEl.appendChild(mobileCta);

      var mobileSocial = document.createElement("li");
      mobileSocial.className = "mobile-social";
      mobileSocial.innerHTML =
        '<a href="https://www.facebook.com/villagenaturopathy" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg></a>' +
        '<a href="https://www.instagram.com/villagenaturopathy" target="_blank" rel="noopener noreferrer" aria-label="Instagram"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg></a>';
      navLinksEl.appendChild(mobileSocial);
    }

    toggle.addEventListener("click", function () {
      var open = nav.getAttribute("data-open") === "true";
      nav.setAttribute("data-open", String(!open));
      toggle.setAttribute("aria-expanded", String(!open));
      toggle.innerHTML = !open ? closeIcon : hamburgerIcon;
      document.body.style.overflow = !open ? "hidden" : "";
    });
    nav.querySelectorAll(".nav-links a, .nav-cta").forEach(function (link) {
      link.addEventListener("click", function () {
        closeMenu();
      });
    });
  }

  // 1. Text clip-reveal — wrap section headings in mask spans (before observer)
  if (!prefersReducedMotion) {
    document.querySelectorAll(".section-head h2, .split-copy h2, .cta-banner-content h2").forEach(function (el) {
      if (el.closest(".hero-copy")) return;
      var wrapper = document.createElement("span");
      wrapper.className = "text-reveal";
      var inner = document.createElement("span");
      inner.innerHTML = el.innerHTML;
      wrapper.appendChild(inner);
      el.innerHTML = "";
      el.appendChild(wrapper);
    });
  }

  // 5. Eyebrow slide-in (before observer)
  if (!prefersReducedMotion) {
    document.querySelectorAll(".section-head .eyebrow, .split-copy .eyebrow, .cta-banner-content .eyebrow").forEach(function (el) {
      if (el.closest(".hero-copy, .article-hero, .booking-panel, .page-hero")) return;
      el.classList.add("eyebrow-anim");
    });
  }

  // Scroll-triggered reveal animations
  var observer;
  if ("IntersectionObserver" in window) {
    observer = new IntersectionObserver(
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

  // 3. Staggered reveals — add to grids that don't have it
  document.querySelectorAll(".focus-grid, .credentials").forEach(function (el) {
    if (!el.classList.contains("reveal-stagger") && !el.classList.contains("reveal")) {
      el.classList.add("reveal-stagger");
      if (observer) observer.observe(el);
    }
  });

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

    document.querySelectorAll('a[href$="book.html"]').forEach(function (link) {
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

  // ---- Form validation + Formspree submission ----
  function setupFormValidation(formEl, successId, eventName) {
    if (!formEl) return;

    formEl.querySelectorAll("[required]").forEach(function (input) {
      input.addEventListener("blur", function () { validateField(input); });
      input.addEventListener("input", function () {
        if (input.closest(".form-group").classList.contains("has-error")) validateField(input);
      });
    });

    formEl.addEventListener("submit", function (e) {
      e.preventDefault();
      var valid = true;
      formEl.querySelectorAll("[required]").forEach(function (input) {
        if (!validateField(input)) valid = false;
      });
      if (!valid) return;

      var btn = formEl.querySelector('[type="submit"]');
      var origText = btn.textContent;
      btn.disabled = true;
      btn.textContent = "Sending…";

      var errorEl = formEl.querySelector(".form-submit-error");

      fetch(formEl.action, {
        method: "POST",
        body: new FormData(formEl),
        headers: { "Accept": "application/json" }
      }).then(function (res) {
        if (res.ok) {
          formEl.setAttribute("hidden", "");
          var successEl = document.getElementById(successId);
          if (successEl) successEl.removeAttribute("hidden");
          if (window.plausible) plausible(eventName);
        } else {
          throw new Error("Server error");
        }
      }).catch(function () {
        if (errorEl) {
          errorEl.textContent = "Something went wrong — please email us directly at drheather@villagenaturopathy.com";
          errorEl.removeAttribute("hidden");
        }
        btn.disabled = false;
        btn.textContent = origText;
      });
    });
  }

  function validateField(input) {
    var group = input.closest(".form-group");
    var errorSpan = group ? group.querySelector(".form-error") : null;
    if (!group) return true;

    if (!input.checkValidity()) {
      group.classList.add("has-error");
      if (errorSpan) {
        if (input.validity.valueMissing) errorSpan.textContent = "This field is required";
        else if (input.validity.typeMismatch) errorSpan.textContent = "Please enter a valid " + input.type;
        else errorSpan.textContent = input.validationMessage;
      }
      return false;
    }
    group.classList.remove("has-error");
    if (errorSpan) errorSpan.textContent = "";
    return true;
  }

  setupFormValidation(document.getElementById("contact-form"), "contact-success", "Form_ContactSubmit");

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

  // Clone brand for mobile (sits outside the overlay)
  var navBrandLi = navLinks && navLinks.querySelector(".nav-brand .brand");
  if (navBrandLi && nav) {
    var mobileBrand = navBrandLi.cloneNode(true);
    mobileBrand.classList.add("mobile-brand");
    nav.insertBefore(mobileBrand, navLinks);
  }

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

      // Nav pill hide/show on scroll direction
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

  // ---- Premium animations ----

  // 7. Magnetic buttons — subtle cursor-follow on hover
  if (!prefersReducedMotion) {
    document.querySelectorAll(".btn").forEach(function (btn) {
      btn.addEventListener("mousemove", function (e) {
        var rect = btn.getBoundingClientRect();
        var x = e.clientX - rect.left - rect.width / 2;
        var y = e.clientY - rect.top - rect.height / 2;
        btn.style.setProperty("--mx", (x * 0.075) + "px");
        btn.style.setProperty("--my", (y * 0.075) + "px");
      });
      btn.addEventListener("mouseleave", function () {
        btn.style.setProperty("--mx", "0px");
        btn.style.setProperty("--my", "0px");
      });
    });
  }

  // 8. Page transition fade — smooth crossfade between pages
  if (!prefersReducedMotion) {
    document.addEventListener("click", function (e) {
      var link = e.target.closest("a");
      if (!link || e.defaultPrevented) return;
      var href = link.getAttribute("href");
      if (!href || href.charAt(0) === "#" || href.startsWith("mailto") || href.startsWith("javascript") || href.startsWith("tel")) return;
      if (link.target === "_blank") return;
      if (link.hostname && link.hostname !== "" && link.hostname !== window.location.hostname) return;
      e.preventDefault();
      document.body.classList.add("page-leaving");
      setTimeout(function () { window.location.href = href; }, 200);
    });
    window.addEventListener("pageshow", function (e) {
      if (e.persisted) document.body.classList.remove("page-leaving");
    });
  }

  // 9. Footer parallax reveal — staggered column entrance
  var footerTop = document.querySelector(".footer-top");
  if (footerTop && "IntersectionObserver" in window && !prefersReducedMotion) {
    var footerItems = footerTop.querySelectorAll(".footer-brand, .footer-col");
    footerItems.forEach(function (item, i) {
      item.classList.add("footer-col-reveal");
      item.style.transitionDelay = (i * 100) + "ms";
    });
    var footerObs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.querySelectorAll(".footer-col-reveal").forEach(function (item) {
            item.classList.add("is-visible");
          });
          footerObs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });
    footerObs.observe(footerTop);
  }

  // Footer clocks — Toronto + London
  var clockEls = document.querySelectorAll(".clock-time[data-tz]");
  if (clockEls.length) {
    function updateClocks() {
      clockEls.forEach(function (el) {
        el.textContent = new Intl.DateTimeFormat("en-US", {
          hour: "numeric", minute: "2-digit", timeZoneName: "short",
          timeZone: el.getAttribute("data-tz")
        }).format(new Date());
      });
    }
    updateClocks();
    setInterval(updateClocks, 60000);
  }

  // Footer email — click to copy with toast
  var footerEmail = document.querySelector('.footer-contact-item a[href^="mailto:"]');
  if (footerEmail) {
    footerEmail.addEventListener("click", function (e) {
      e.preventDefault();
      var email = footerEmail.textContent.trim();
      navigator.clipboard.writeText(email).then(function () {
        var toast = document.getElementById("copy-toast");
        if (!toast) {
          toast = document.createElement("div");
          toast.id = "copy-toast";
          toast.className = "toast";
          toast.textContent = "Email copied to clipboard";
          document.body.appendChild(toast);
        }
        toast.classList.add("show");
        setTimeout(function () { toast.classList.remove("show"); }, 2200);
      });
    });
  }

  // ---- GDPR Cookie Consent ----
  var CONSENT_KEY = "vn_cookie_consent";

  function getConsent() {
    try { return JSON.parse(localStorage.getItem(CONSENT_KEY)); } catch (e) { return null; }
  }

  function setConsent(prefs) {
    prefs.timestamp = new Date().toISOString();
    localStorage.setItem(CONSENT_KEY, JSON.stringify(prefs));
    applyConsent(prefs);
    hideBanner();
    hidePrefsModal();
  }

  function applyConsent(prefs) {
    if (prefs.analytics) loadAnalytics();
    if (prefs.marketing) loadMarketing();
  }

  function loadAnalytics() {
    if (document.getElementById("plausible-script")) return;
    var domainMeta = document.querySelector('meta[name="plausible-domain"]');
    var domain = domainMeta ? domainMeta.getAttribute("content") : "villagenaturopathy.com";
    var s = document.createElement("script");
    s.id = "plausible-script";
    s.defer = true;
    s.setAttribute("data-domain", domain);
    s.src = "https://plausible.io/js/script.js";
    document.head.appendChild(s);

    window.plausible = window.plausible || function () {
      (window.plausible.q = window.plausible.q || []).push(arguments);
    };

    attachConversionEvents();
    loadCoreWebVitals();
  }

  function attachConversionEvents() {
    document.querySelectorAll('a[href*="book.html"]').forEach(function (link) {
      link.addEventListener("click", function () {
        if (window.plausible) plausible("CTA_Book");
      });
    });

    var modalObs = new MutationObserver(function (mutations) {
      mutations.forEach(function (m) {
        if (m.target.classList && m.target.classList.contains("open")) {
          if (window.plausible) plausible("Modal_BookingOpen");
        }
      });
    });
    var bookModal = document.getElementById("book-modal");
    if (bookModal) modalObs.observe(bookModal, { attributes: true, attributeFilter: ["class"] });
  }

  function loadCoreWebVitals() {
    var s = document.createElement("script");
    s.src = "https://unpkg.com/web-vitals@4/dist/web-vitals.iife.js";
    s.onload = function () {
      if (!window.webVitals) return;
      function sendCWV(metric) {
        if (window.plausible) {
          plausible("CWV_" + metric.name, { props: { value: Math.round(metric.value), rating: metric.rating } });
        }
      }
      webVitals.onCLS(sendCWV);
      webVitals.onINP(sendCWV);
      webVitals.onLCP(sendCWV);
      webVitals.onFCP(sendCWV);
      webVitals.onTTFB(sendCWV);
    };
    document.head.appendChild(s);
  }

  function loadMarketing() {
    if (document.getElementById("meta-pixel-script")) return;
    var pixelId = document.querySelector('meta[name="fb-pixel-id"]');
    if (!pixelId) return;
    var id = pixelId.getAttribute("content");
    if (!id) return;
    var s = document.createElement("script");
    s.id = "meta-pixel-script";
    s.textContent = "!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','" + id + "');fbq('track','PageView');";
    document.head.appendChild(s);
  }

  function buildBanner() {
    var banner = document.createElement("div");
    banner.className = "cookie-banner";
    banner.id = "cookie-banner";
    banner.setAttribute("role", "region");
    banner.setAttribute("aria-label", "Cookie consent");
    banner.innerHTML =
      '<div class="cookie-banner-inner">' +
        '<p class=”cookie-banner-text”>We use privacy-respecting analytics to understand how visitors use this site. No personal data is collected. By clicking “Accept all,” you consent to anonymous usage tracking. <a href=”privacy.html”>Privacy policy</a></p>' +
        '<div class="cookie-banner-actions">' +
          '<button class="btn--cookie-outline" id="cookie-reject">Essential only</button>' +
          '<button class="btn--cookie-outline" id="cookie-prefs-btn">Manage preferences</button>' +
          '<button class="btn btn--warm btn--sm" id="cookie-accept">Accept all</button>' +
        '</div>' +
      '</div>';
    document.body.appendChild(banner);
    requestAnimationFrame(function () {
      requestAnimationFrame(function () { banner.classList.add("is-visible"); });
    });

    document.getElementById("cookie-accept").addEventListener("click", function () {
      setConsent({ essential: true, analytics: true, marketing: true });
    });
    document.getElementById("cookie-reject").addEventListener("click", function () {
      setConsent({ essential: true, analytics: false, marketing: false });
    });
    document.getElementById("cookie-prefs-btn").addEventListener("click", function () {
      showPrefsModal();
    });
  }

  function buildPrefsModal() {
    var current = getConsent() || { analytics: false, marketing: false };
    var overlay = document.createElement("div");
    overlay.className = "cookie-modal-overlay";
    overlay.id = "cookie-modal";
    overlay.innerHTML =
      '<div class="cookie-modal">' +
        '<h2>Cookie preferences</h2>' +
        '<p>We use different types of cookies to optimise your experience. Choose which cookies you’d like to allow. You can change these settings at any time via the link in our footer.</p>' +
        '<div class="cookie-category">' +
          '<div class="cookie-cat-info"><strong>Essential</strong><p>Required for the site to function. Cannot be disabled.</p></div>' +
          '<label class="cookie-toggle"><input type="checkbox" checked disabled><span class="cookie-toggle-track"></span></label>' +
        '</div>' +
        '<div class="cookie-category">' +
          '<div class="cookie-cat-info"><strong>Analytics</strong><p>Help us understand how visitors use the site so we can improve it.</p></div>' +
          '<label class="cookie-toggle"><input type="checkbox" id="cookie-analytics" ' + (current.analytics ? 'checked' : '') + '><span class="cookie-toggle-track"></span></label>' +
        '</div>' +
        '<div class="cookie-category">' +
          '<div class="cookie-cat-info"><strong>Marketing</strong><p>Used to deliver relevant ads and measure campaign performance.</p></div>' +
          '<label class="cookie-toggle"><input type="checkbox" id="cookie-marketing" ' + (current.marketing ? 'checked' : '') + '><span class="cookie-toggle-track"></span></label>' +
        '</div>' +
        '<div class="cookie-modal-actions">' +
          '<button class="btn btn--sage btn--sm" id="cookie-save">Save preferences</button>' +
          '<button class="btn--cookie-outline" id="cookie-modal-accept" style="color:var(--text-body);border-color:var(--greige)">Accept all</button>' +
        '</div>' +
      '</div>';
    document.body.appendChild(overlay);

    overlay.addEventListener("click", function (e) {
      if (e.target === overlay) hidePrefsModal();
    });
    document.getElementById("cookie-save").addEventListener("click", function () {
      setConsent({
        essential: true,
        analytics: document.getElementById("cookie-analytics").checked,
        marketing: document.getElementById("cookie-marketing").checked
      });
    });
    document.getElementById("cookie-modal-accept").addEventListener("click", function () {
      setConsent({ essential: true, analytics: true, marketing: true });
    });
  }

  function showPrefsModal() {
    var modal = document.getElementById("cookie-modal");
    if (!modal) buildPrefsModal();
    modal = document.getElementById("cookie-modal");
    modal.classList.add("open");
    document.body.style.overflow = "hidden";
  }

  function hidePrefsModal() {
    var modal = document.getElementById("cookie-modal");
    if (modal) {
      modal.classList.remove("open");
      document.body.style.overflow = "";
    }
  }

  function hideBanner() {
    var banner = document.getElementById("cookie-banner");
    if (banner) {
      banner.classList.remove("is-visible");
      setTimeout(function () { if (banner.parentNode) banner.parentNode.removeChild(banner); }, 500);
    }
  }

  // Wire up "Cookie settings" links in footers
  document.querySelectorAll('[data-cookie-settings]').forEach(function (link) {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      showPrefsModal();
    });
  });

  // Init: check consent on load
  var existingConsent = getConsent();
  if (existingConsent) {
    applyConsent(existingConsent);
  } else {
    buildBanner();
  }

  // 10. Lenis smooth scroll — butter-smooth momentum scrolling
  if (!prefersReducedMotion) {
    var s = document.createElement("script");
    s.src = "https://cdn.jsdelivr.net/npm/lenis@1.1.14/dist/lenis.min.js";
    s.onload = function () {
      try {
        var lenis = new Lenis({
          duration: 1.2,
          easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); },
          smoothWheel: true
        });
        function raf(time) { lenis.raf(time); requestAnimationFrame(raf); }
        requestAnimationFrame(raf);
        document.documentElement.style.scrollBehavior = "auto";
      } catch (e) {}
    };
    document.head.appendChild(s);
  }
  // ---- A/B Testing (config-driven) ----
  fetch("data/ab-tests.json")
    .then(function (r) { return r.json(); })
    .then(function (tests) {
      Object.keys(tests).forEach(function (testName) {
        var test = tests[testName];
        if (!test.active) return;
        var el = document.querySelector('[data-ab="' + testName + '"]');
        if (!el || !test.variants.length) return;

        var totalWeight = test.weights.reduce(function (a, b) { return a + b; }, 0);
        var rand = Math.random() * totalWeight;
        var cumulative = 0;
        var chosen = 0;
        for (var i = 0; i < test.weights.length; i++) {
          cumulative += test.weights[i];
          if (rand < cumulative) { chosen = i; break; }
        }

        el.textContent = test.variants[chosen];
        if (window.plausible) {
          plausible("AB_Variant", { props: { test: testName, variant: String(chosen) } });
        }
      });
    })
    .catch(function () {});

  // ---- Testimonials (loaded from JSON) ----
  var testimonialGrid = document.getElementById("testimonial-grid");
  if (testimonialGrid) {
    fetch("data/testimonials.json")
      .then(function (r) { return r.json(); })
      .then(function (data) {
        if (!data || !data.length) {
          testimonialGrid.closest("section").style.display = "none";
          return;
        }
        testimonialGrid.innerHTML = data.map(function (t) {
          var stars = "";
          for (var i = 0; i < (t.rating || 5); i++) stars += "★";
          return '<div class="testimonial-card">' +
            '<span class="testimonial-stars">' + stars + '</span>' +
            '<p class="testimonial-quote">' + t.quote + '</p>' +
            '<div class="testimonial-meta">' +
            '<span class="testimonial-name">' + t.name + '</span>' +
            '<span class="testimonial-detail">' + t.location + ' &middot; ' + t.condition + '</span>' +
            '</div></div>';
        }).join("");
        if (observer) {
          testimonialGrid.classList.add("reveal-stagger");
          observer.observe(testimonialGrid);
        }
      })
      .catch(function () {
        testimonialGrid.closest("section").style.display = "none";
      });
  }
})();
