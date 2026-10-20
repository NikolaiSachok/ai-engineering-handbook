/**
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 *
 * ---------------------------------------------------------------------------
 * Swizzled (ejected) from @docusaurus/theme-classic.
 *
 * The only changes from the upstream component are in the per-locale item map:
 *
 *  1. On click of a *cross-locale* item we capture the reader's position (see
 *     src/lib/localeScrollPosition.ts) keyed by the destination pathname, so the
 *     position can be restored after the full-page navigation. The `#hash` is kept,
 *     as upstream does: heading ids are shared across locales (#813), so it names
 *     the same section on the other side.
 *
 *  2. Only the locales the current page exists in are listed
 *     (src/lib/availableLocales.ts): an English-only course or the blog does not
 *     offer a "translation" that would be the same English page.
 *
 * Everything else — labels, active-class logic, query-string merging, the
 * dropdown itself — is verbatim upstream, so normal dropdown behavior, in-page
 * anchor links, and the TOC are unaffected.
 * ---------------------------------------------------------------------------
 */

import React, {type ReactNode} from 'react';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import {useAlternatePageUtils} from '@docusaurus/theme-common/internal';
import {translate} from '@docusaurus/Translate';
import {mergeSearchStrings, useHistorySelector} from '@docusaurus/theme-common';
import DropdownNavbarItem from '@theme/NavbarItem/DropdownNavbarItem';
import IconLanguage from '@theme/Icon/Language';
import type {LinkLikeNavbarItemProps} from '@theme/NavbarItem';
import type {Props} from '@theme/NavbarItem/LocaleDropdownNavbarItem';

import {capturePosition} from '@site/src/lib/localeScrollPosition';
import {useSetPreferredLocale} from '@site/src/lib/localePreference';
import {useAvailableLocales} from '@site/src/lib/availableLocales';

import styles from './styles.module.css';

/** Extract a bare pathname from a locale-dropdown `to` value, e.g.
 *  `pathname:///base/en/foo/?q=1#hash` -> `/base/en/foo/`. This matches what
 *  `window.location.pathname` will be on the destination page. */
function pathnameFromTo(to: string): string {
  return to
    .replace(/^pathname:\/\//, '')
    .replace(/[?#].*$/, '');
}

function useLocaleDropdownUtils() {
  const {
    siteConfig,
    i18n: {localeConfigs},
  } = useDocusaurusContext();
  const alternatePageUtils = useAlternatePageUtils();
  const search = useHistorySelector((history) => history.location.search);
  const hash = useHistorySelector((history) => history.location.hash);

  const getLocaleConfig = (locale: string) => {
    const localeConfig = localeConfigs[locale];
    if (!localeConfig) {
      throw new Error(
        `Docusaurus bug, no locale config found for locale=${locale}`,
      );
    }
    return localeConfig;
  };

  const getBaseURLForLocale = (locale: string) => {
    const localeConfig = getLocaleConfig(locale);
    const isSameDomain = localeConfig.url === siteConfig.url;
    if (isSameDomain) {
      // Shorter paths if localized sites are hosted on the same domain
      // This reduces HTML size a bit
      return `pathname://${alternatePageUtils.createUrl({
        locale,
        fullyQualified: false,
      })}`;
    }
    return alternatePageUtils.createUrl({
      locale,
      fullyQualified: true,
    });
  };

  return {
    getURL: (locale: string, options: {queryString: string | undefined}) => {
      // We have 2 query strings because
      // - there's the current one
      // - there's one user can provide through navbar config
      // see https://github.com/facebook/docusaurus/pull/8915
      const finalSearch = mergeSearchStrings(
        [search, options.queryString],
        'append',
      );
      return `${getBaseURLForLocale(locale)}${finalSearch}${hash}`;
    },
    getLabel: (locale: string) => {
      return getLocaleConfig(locale).label;
    },
    getLang: (locale: string) => {
      return getLocaleConfig(locale).htmlLang;
    },
  };
}

export default function LocaleDropdownNavbarItem({
  mobile,
  dropdownItemsBefore,
  dropdownItemsAfter,
  queryString,
  ...props
}: Props): ReactNode {
  const utils = useLocaleDropdownUtils();

  const {
    i18n: {currentLocale},
  } = useDocusaurusContext();
  const locales = useAvailableLocales();
  const setPreferredLocale = useSetPreferredLocale();
  const localeItems = locales.map((locale): LinkLikeNavbarItemProps => {
    const isCurrent = locale === currentLocale;
    const to = utils.getURL(locale, {queryString});
    return {
      label: utils.getLabel(locale),
      lang: utils.getLang(locale),
      to,
      target: '_self',
      autoAddBaseUrl: false,
      // Any pick is an explicit choice: remember it, so neither the first-visit detector
      // nor the out-of-scope fallback routing acts against it — picking English while
      // shown an English-only course in place of German keeps the reader in English. On a
      // cross-locale switch, also capture the reader's position just before the
      // full-page navigation.
      onClick: () => {
        setPreferredLocale(locale);
        if (!isCurrent) {
          capturePosition(pathnameFromTo(to));
        }
      },
      className:
        // eslint-disable-next-line no-nested-ternary
        isCurrent
          ? // Similar idea as DefaultNavbarItem: select the right Infima active
            // class name. This cannot be substituted with isActive, because the
            // target URLs contain `pathname://` and therefore are not NavLinks!
            mobile
            ? 'menu__link--active'
            : 'dropdown__link--active'
          : '',
    };
  });

  const items = [...dropdownItemsBefore, ...localeItems, ...dropdownItemsAfter];

  // Mobile is handled a bit differently
  const dropdownLabel = mobile
    ? translate({
        message: 'Languages',
        id: 'theme.navbar.mobileLanguageDropdown.label',
        description: 'The label for the mobile language switcher dropdown',
      })
    : utils.getLabel(currentLocale);

  return (
    <DropdownNavbarItem
      {...props}
      mobile={mobile}
      label={
        <>
          <IconLanguage className={styles.iconLanguage} />
          {dropdownLabel}
        </>
      }
      items={items}
    />
  );
}
