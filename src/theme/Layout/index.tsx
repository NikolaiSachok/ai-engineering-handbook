/**
 * Layout wrapper (swizzled @theme/Layout) — the English-fallback notice.
 *
 * WHY THIS EXISTS
 *
 * Not every course is translated into every locale, and the blog is English-only by
 * declaration in all of them. Docusaurus handles that by falling back to the English file
 * while keeping the reader's locale, which is the right behaviour — the locale lives in the
 * URL prefix, so it is stable, shareable and unaffected by where the reader navigates. What
 * it does NOT do is say so. Until this component, `ru` and `sk` had advertised a translated
 * "Field notes" label over English posts since launch with nothing telling the reader.
 *
 * THE RULE THIS ENCODES: the site language never changes as a side effect of navigation.
 *
 * A reader on `/de/rag-agents/…` who opens Field notes goes to `/de/blog/…` — German chrome,
 * English post, and this notice. Going back to the course returns them to German, because
 * nothing was mutated; there is no state to restore. Switching the locale for them would be
 * a silent global change, and worse, it would not be undone by going back: they would return
 * to the course in English. Locale is a property of the reader, not of the page.
 *
 * WHY A LAYOUT WRAPPER RATHER THAN A DOC/BLOG ONE
 *
 * One component covers docs, blog and standalone pages, and it renders inside Layout — below
 * the navbar, above the content — instead of above the whole app the way a Root wrapper
 * would. `@theme/Root` is already swizzled for locale-switch scroll restoration and is the
 * wrong seam for anything visual.
 *
 * The path list comes from `customFields.englishOnlyPaths`, computed per locale build from
 * the same course declarations the navbar filter reads, so the two cannot drift.
 */

import React, {type ReactNode} from 'react';
import Layout from '@theme-original/Layout';
import type LayoutType from '@theme/Layout';
import type {WrapperProps} from '@docusaurus/types';
import {useLocation} from '@docusaurus/router';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import {translate} from '@docusaurus/Translate';
import styles from './styles.module.css';

type Props = WrapperProps<typeof LayoutType>;

/**
 * Does `pathname` sit under one of the English-only route prefixes?
 *
 * `pathname` carries the baseUrl and the locale (`/ai-engineering-handbook/de/ai-sdlc/…`),
 * while the prefixes are bare (`/ai-sdlc`). So this matches on a path SEGMENT rather than a
 * string prefix: a bare `includes()` would also fire on a hypothetical `/notes-ai-sdlc-x/`,
 * and an exact prefix check would never fire at all once baseUrl is in front.
 */
function isEnglishOnly(pathname: string, prefixes: string[]): boolean {
  return prefixes.some((p) => {
    const seg = p.replace(/^\/+|\/+$/g, '');
    return seg.length > 0 && new RegExp(`(^|/)${seg}(/|$)`).test(pathname);
  });
}

export default function LayoutWrapper(props: Props): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  const {pathname} = useLocation();
  const prefixes = (siteConfig.customFields?.englishOnlyPaths ?? []) as string[];

  // Empty for `en`, so this is a no-op there and the regex work never runs.
  const showNotice = prefixes.length > 0 && isEnglishOnly(pathname, prefixes);

  return (
    <Layout {...props}>
      {showNotice && (
        <div className={styles.notice} role="note">
          {translate({
            id: 'fallback.englishOnly',
            message: 'This page is only available in English.',
            description:
              'Shown above the content when a page is served in English because the reader’s locale has no translation of it. The surrounding interface stays in the reader’s language.',
          })}
        </div>
      )}
      {props.children}
    </Layout>
  );
}
