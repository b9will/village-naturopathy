// Serves the static site exactly as authored (.html URLs), mapping directory
// paths ("/" and "/uk/london/") to their index.html. Redirects and headers
// still come from _redirects and _headers.
export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // Directory-style URLs without a trailing slash get a 301 to the slash version
    // (e.g. /uk/london -> /uk/london/), so each page has exactly one canonical URL.
    const last = url.pathname.split('/').pop();
    if (!url.pathname.endsWith('/') && last && !last.includes('.')) {
      url.pathname += '/';
      return Response.redirect(url.toString(), 301);
    }

    if (url.pathname.endsWith('/')) url.pathname += 'index.html';
    const res = await env.ASSETS.fetch(new Request(url, request));

    // Staging (workers.dev) must never be indexed or compete with the real domain.
    if (url.hostname.endsWith('.workers.dev')) {
      const out = new Response(res.body, res);
      out.headers.set('X-Robots-Tag', 'noindex, nofollow');
      return out;
    }
    return res;
  },
};
