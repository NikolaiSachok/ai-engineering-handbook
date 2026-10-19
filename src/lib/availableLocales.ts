import {useLocation} from '@docusaurus/router';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

type LocaleScope = {path: string; locales: string[]};

/**
 * The locales the current page actually exists in, for the language pickers.
 *
 * Docusaurus builds every route in every locale, so a page a locale does not translate
 * (an English-only course, the blog) is still served there — in English — and a reader who
 * picked that locale would be moved straight back to English by the locale routing in the
 * head script. Offering it in the picker promises a translation that is not there. The scopes come from
 * `customFields.localeScopes` (docusaurus.config.ts), derived from each course's declared
 * `locales`; a route outside every scope (landing page, search) is in every locale.
 */
export function useAvailableLocales(): string[] {
  const {
    siteConfig: {baseUrl, customFields},
    i18n: {locales},
  } = useDocusaurusContext();
  const {pathname} = useLocation();
  const scopes = (customFields?.localeScopes ?? []) as LocaleScope[];

  // `baseUrl` is the current locale's base (e.g. `/ai-engineering-handbook/ru/`), so
  // stripping it leaves the locale-independent route (`azure-dotnet/part-1-.../`).
  const route = `/${pathname.startsWith(baseUrl) ? pathname.slice(baseUrl.length) : pathname}`;
  const scope = scopes.find((s) => route === s.path || route.startsWith(`${s.path}/`));
  if (!scope) {
    return locales;
  }
  return locales.filter((locale) => scope.locales.includes(locale));
}
