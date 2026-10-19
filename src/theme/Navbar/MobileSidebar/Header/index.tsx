import React, {type ReactNode} from 'react';
import Header from '@theme-original/Navbar/MobileSidebar/Header';
import type HeaderType from '@theme/Navbar/MobileSidebar/Header';
import type {WrapperProps} from '@docusaurus/types';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import {useAlternatePageUtils} from '@docusaurus/theme-common/internal';
import IconLanguage from '@theme/Icon/Language';
import {useAvailableLocales} from '@site/src/lib/availableLocales';
import {setPreferredLocale} from '@site/src/lib/localePreference';

type Props = WrapperProps<typeof HeaderType>;

/**
 * P1 — mobile language discoverability.
 *
 * On a docs/lesson page the mobile drawer auto-opens the course sidebar
 * (secondary panel); the navbar's `localeDropdown` collapses into the PRIMARY
 * panel, one non-obvious "← Back to main menu" tap away — so a monolingual
 * reader concludes there is no language switch. This renders a compact language
 * control in the ALWAYS-VISIBLE drawer header (rendered by the Layout directly
 * inside `.navbar-sidebar`, ABOVE both the primary and secondary panels), so
 * language is one tap from any page, including a lesson.
 *
 * It reuses Docusaurus's own locale-switch mechanism (the exact URL construction
 * from `LocaleDropdownNavbarItem`: `useAlternatePageUtils().createUrl`), so
 * switching preserves the CURRENT page's translation (same page, target locale)
 * rather than jumping to a locale root. It is locale-list-driven off
 * `useAvailableLocales()`, so a new locale appears automatically where its pages exist.
 *
 * Desktop (>=997px) never renders the mobile drawer, so desktop is untouched.
 */
function MobileLanguageSwitch(): ReactNode {
  const {
    siteConfig: {url: siteUrl, baseUrl},
    i18n: {currentLocale, localeConfigs},
  } = useDocusaurusContext();
  const alternatePageUtils = useAlternatePageUtils();
  // Only the locales this page exists in (same rule as the desktop dropdown).
  const locales = useAvailableLocales();

  // Nothing to switch between: a single-locale build, or a page in one locale only.
  if (locales.length <= 1) {
    return null;
  }

  return (
    <div
      className="mobileLangSwitch"
      role="group"
      aria-label="Select language">
      <IconLanguage className="mobileLangSwitch__icon" />
      {locales.map((locale) => {
        const localeConfig = localeConfigs[locale];
        // Same construction as the theme's LocaleDropdownNavbarItem: for a
        // same-domain locale use a shorter `pathname://` path; otherwise a
        // fully-qualified URL. `pathname://` forces a real navigation (a locale
        // switch is not a client-side route). `createUrl` maps to the SAME page
        // in the target locale, keeping the reader's place.
        const isSameDomain = localeConfig?.url === siteUrl;
        const to = isSameDomain
          ? `pathname://${alternatePageUtils.createUrl({
              locale,
              fullyQualified: false,
            })}`
          : alternatePageUtils.createUrl({locale, fullyQualified: true});
        const isActive = locale === currentLocale;
        return (
          <Link
            key={locale}
            to={to}
            target="_self"
            autoAddBaseUrl={false}
            onClick={() => setPreferredLocale(locale, baseUrl)}
            className={
              isActive
                ? 'mobileLangSwitch__link mobileLangSwitch__link--active'
                : 'mobileLangSwitch__link'
            }
            aria-current={isActive ? 'true' : undefined}
            aria-label={localeConfig?.label ?? locale}
            lang={localeConfig?.htmlLang}>
            {locale.toUpperCase()}
          </Link>
        );
      })}
    </div>
  );
}

export default function HeaderWrapper(props: Props): ReactNode {
  return (
    <>
      <Header {...props} />
      <MobileLanguageSwitch />
    </>
  );
}
