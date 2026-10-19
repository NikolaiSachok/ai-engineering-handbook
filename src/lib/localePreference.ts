/**
 * Persist the reader's explicit locale choice.
 *
 * The blocking <head> detection script (in docusaurus.config.ts,
 * `localeDetectionScript`) auto-redirects a *first* visitor to the locale that
 * best matches their browser languages. Once a `preferred_locale` cookie exists,
 * that script does nothing — so writing the cookie here, the moment the reader
 * picks a language in the navbar dropdown, is what makes the choice stick: on the
 * next visit to a bare default-locale URL they are never auto-redirected against
 * their pick.
 *
 * An explicit pick also ends any automatic English fallback: the head script remembers, per
 * tab, the locale a reader was moved out of so it can return them to it, and a choice made
 * in the dropdown replaces that.
 *
 * The cookie NAME and the session KEY are mirrored as string literals in the head script (it
 * can't import this module — it's inlined into static HTML). Keep them in sync.
 */

export const PREFERRED_LOCALE_COOKIE = 'preferred_locale';
const FALLBACK_FROM_KEY = 'locale_fallback_from';

/** Remember `locale` as the reader's chosen language. Scoped to the site's
 *  baseUrl so it doesn't leak to other apps on the same host. No-op during SSR. */
export function setPreferredLocale(locale: string, baseUrl: string): void {
  if (typeof document === 'undefined') return;
  const oneYear = 60 * 60 * 24 * 365;
  const path = baseUrl || '/';
  document.cookie =
    `${PREFERRED_LOCALE_COOKIE}=${encodeURIComponent(locale)}` +
    `; path=${path}; max-age=${oneYear}; samesite=lax`;
  try {
    window.sessionStorage.removeItem(FALLBACK_FROM_KEY);
  } catch {
    // Storage blocked: there is no fallback state to clear either.
  }
}
