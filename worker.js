// Serves the static site exactly as authored (.html URLs), mapping directory
// paths ("/" and "/conditions/") to their index.html. Redirects and headers
// still come from _redirects and _headers.
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname.endsWith('/')) url.pathname += 'index.html';
    return env.ASSETS.fetch(new Request(url, request));
  },
};
