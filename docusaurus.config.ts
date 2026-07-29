import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

// --- i18n single source of truth -------------------------------------------
// The whole locale mechanism (config below, the browser-language detection in
// `localeDetectionScript`, the search index, the locale dropdown) is driven off
// these constants. Adding a language later = add it to the locale lists and give
// it a `localeConfigs` label — detection and switching pick it up with NO other
// code change. `DEFAULT_LOCALE` serves at the site root; every other locale
// serves under `/<locale>/`.
//
// Released vs unreleased locales (gated visibility). RELEASED_LOCALES ship on the
// public site. UNRELEASED_LOCALES are still being translated: they are built and
// broken-link/i18n-validated in CI (so their tree can't silently rot), but stay
// OUT of the deployed locale dropdown until they're launch-ready — a public
// dropdown pointing at a half-translated locale falls back to EN per missing page
// and undermines the showcase. The gate is one env var:
//   - CI (`.github/workflows/ci.yml`) sets HANDBOOK_INCLUDE_UNRELEASED=1, so the
//     build includes + validates the unreleased locales.
//   - Deploy (`.github/workflows/deploy.yml`) leaves it unset, so the public build
//     serves only RELEASED_LOCALES.
// Launching a locale = move it from UNRELEASED_LOCALES to RELEASED_LOCALES (one
// line); its `localeConfigs` label is already set below, so nothing else changes.
const DEFAULT_LOCALE = 'en';
const RELEASED_LOCALES = ['en', 'ru', 'sk']; // Slovak launched 2026-07-15; both courses now ship complete in all three
const UNRELEASED_LOCALES: string[] = ['de']; // German in progress (from 2026-07-28): built+validated in CI, gated out of the deployed dropdown
const INCLUDE_UNRELEASED = process.env.HANDBOOK_INCLUDE_UNRELEASED === '1';
const LOCALES = [...RELEASED_LOCALES, ...(INCLUDE_UNRELEASED ? UNRELEASED_LOCALES : [])];
const BASE_URL = '/ai-engineering-handbook/';

// Each locale's endonym — the name that language calls itself, which reads correctly in
// every locale and so is never translated. One table, two consumers: Docusaurus'
// `localeConfigs` labels (the locale dropdown) and the landing hub's per-course language
// line. They used to be written out twice, which is how a course card can advertise a
// language the site does not serve.
const LOCALE_LABELS: Record<string, string> = {
  en: 'English',
  ru: 'Русский',
  sk: 'Slovenčina',
  de: 'Deutsch',
};

// --- Courses (docs instances) — the hub's single source of truth -------------
// This site is a HUB of independent AI-engineering courses, not one book. Each
// course is its own Docusaurus docs instance served under its own URL prefix
// (`routeBasePath`); the root `/` is a landing hub (src/pages/index.tsx) that
// presents them as equal peers. The navbar items, the local search index, and
// the landing page all DERIVE from this one list — so the courses never drift
// apart across those surfaces.
//
// Adding a THIRD course later is symmetric and mechanical:
//   1. Append an entry to COURSES below (id, basePath, sidebarId, label, flags) —
//      including `locales`, the locale codes that course claims. A course need not be
//      trilingual: an English-only course declares `['en']` and the i18n gates scope
//      themselves to it (see the field's comment).
//   2. Wire its docs instance. The FIRST course is the preset `docs` (the
//      "default" instance, id 'default') — its i18n lives under the UN-suffixed
//      `i18n/<loc>/docusaurus-plugin-content-docs/`. EVERY OTHER course is a
//      `@docusaurus/plugin-content-docs` entry in `plugins` (generated from
//      COURSES.slice(1) below) with a matching `id`; its i18n lives under
//      `i18n/<loc>/docusaurus-plugin-content-docs-<id>/`.
//   3. Create its content dir `docs-<id>/` and a `sidebars-<id>.ts`.
//   4. Add its EN + per-locale intro so parity holds.
// Navbar + search + landing then pick it up with NO further code changes.
type Course = {
  id: string;          // docs-plugin instance id ('default' = the preset instance)
  basePath: string;    // routeBasePath, e.g. '/rag-agents'
  sidebarId: string;   // the sidebar key exported by its sidebars file
  navbarLabel: string; // label shown in the navbar and on the landing card
  blurb: string;       // one-line description for the landing hub card
  // The locales this course CLAIMS — the ones it is translated into, or is being
  // translated into. Locale CODES, not display names: two gates read this list
  // (scripts/courses.py → locale_parity.py + i18n-link-check.sh), and the landing card's
  // language line is derived from it (released members only, via LOCALE_LABELS).
  //
  // Why a course declares this at all. The parity gate used to assume the site-wide truth
  // "every course is translated in every released locale", and hard-failed a released
  // locale with no i18n tree for a course. That held while every course was trilingual and
  // stops holding the moment one course deliberately is not — an English-only course would
  // fail CI for ru and sk on the day it is registered, and for de on the day de launches.
  // Scope belongs to the course, because the course is what decides it.
  //
  // Deliberately NOT defaulted: a course that declares no locales aborts the gates rather
  // than inheriting every released locale, since the permissive default is the fail-open
  // this field exists to close. `en` must always be present — the English tree is the
  // source every other locale is compared against.
  locales: string[];
  live: boolean;       // true = content shipped; false = placeholder / in progress
  inNavbar: boolean;   // add a docSidebar item to the navbar yet?
  // The course's slice of the footer sitemap, in order. `path` is appended to
  // `basePath` ('' = the course intro). This is per-course DATA rather than
  // something the footer derives, because which routes a course even HAS is
  // decided in its content tree — a Part gets its own page only if that Part's
  // EN `_category_.json` carries a `link` (the EN one decides for every locale) —
  // and the footer cannot guess that.
  // Only list routes that actually exist: released builds run
  // `onBrokenLinks: 'throw'`, so an invented footer link is a build failure. And
  // keep this in step when a course gains pages — the footer is the only
  // always-visible navigation on phones, so a gap here is a gap for most readers.
  footerLinks: {label: string; path: string}[];
};
const COURSES: Course[] = [
  // RAG & Agents — the launched, trilingual course. It stays the DEFAULT docs
  // instance (id 'default') so its frozen EN `docs/` + RU/SK i18n trees never
  // move; only its URL prefix changed from '/' to '/rag-agents'.
  {
    id: 'default',
    basePath: '/rag-agents',
    sidebarId: 'handbookSidebar',
    navbarLabel: 'RAG & Agents',
    blurb:
      'Production RAG and agentic systems from first principles — ingestion, retrieval, ' +
      'generation, agents, and the eval, guardrails and LLMOps that keep them honest.',
    locales: ['en', 'ru', 'sk', 'de'],
    live: true,
    inNavbar: true,
    footerLinks: [
      {label: 'Introduction', path: ''},
      {label: 'Part I — RAG', path: 'part-1-rag/overview'},
      {label: 'Part II — Agents', path: 'part-2-agents/overview'},
      {label: 'Part III — Production & LLMOps', path: 'part-3-production/overview'},
      {label: 'Glossary', path: 'glossary'},
    ],
  },
  // AI SDLC — shipped complete and trilingual (July 2026): all five Parts, 22
  // lessons plus 4 optional deep-dives, in EN/RU/SK (28 pages per locale incl.
  // intro + glossary). `live: true` badges it "Live" on the hub, like RAG.
  // Part labels below are the `_category_.json` labels verbatim, so the footer and
  // the sidebar name the same thing the same way.
  {
    id: 'ai-sdlc',
    basePath: '/ai-sdlc',
    sidebarId: 'aiSdlcSidebar',
    navbarLabel: 'AI SDLC',
    blurb:
      'The AI-assisted software development lifecycle: planning, building, reviewing and ' +
      'shipping when AI agents are part of the team.',
    locales: ['en', 'ru', 'sk', 'de'],
    live: true,
    inNavbar: true,
    footerLinks: [
      {label: 'Introduction', path: ''},
      {label: 'Part I — The Foundation', path: 'part-1-foundation/overview'},
      {label: 'Part II — The Loop', path: 'part-2-loop/overview'},
      {label: 'Part III — Verification', path: 'part-3-verification/overview'},
      {label: 'Part IV — The Platform', path: 'part-4-platform/overview'},
      {label: 'Part V — Scale & Governance', path: 'part-5-scale-governance/overview'},
      {label: 'Glossary', path: 'glossary'},
    ],
  },
];
// Validate the declared scope at config load, so a malformed declaration fails the build
// rather than quietly reaching the gates — which read the same field and would then be
// scoping themselves off a typo. Three ways to get it wrong, all fatal:
for (const c of COURSES) {
  if (!c.locales.length) {
    throw new Error(
      `Course '${c.id}' declares no locales. A course must state which locales it claims; ` +
        'there is no default, because "all of them" is exactly the assumption per-course ' +
        'locale scope exists to remove.',
    );
  }
  if (!c.locales.includes(DEFAULT_LOCALE)) {
    throw new Error(
      `Course '${c.id}' does not claim the default locale '${DEFAULT_LOCALE}'. The English ` +
        'tree is the source every other locale is compared against, so every course has one.',
    );
  }
  const unknown = c.locales.filter((loc) => !(loc in LOCALE_LABELS));
  if (unknown.length) {
    throw new Error(
      `Course '${c.id}' claims unknown locale(s): ${unknown.join(', ')}. Add the locale to ` +
        'LOCALE_LABELS (and to the released/unreleased lists) in the same change.',
    );
  }
}

const DEFAULT_COURSE = COURSES[0];
// Every course's route base path — the set of docs instances the local search
// index must cover (see the search theme below).
const DOCS_ROUTE_BASE_PATHS = COURSES.map((c) => c.basePath);

// Search-index languages. The local search plugin loads a lunr stemmer per language
// via `require.resolve('lunr-languages/lunr.<code>')`; lunr-languages ships stemmers
// for many languages but NOT Slovak (nor Czech), so passing 'sk' straight through
// hard-crashes the build (MODULE_NOT_FOUND on lunr.sk). We therefore feed the plugin
// LOCALES filtered to the codes lunr actually supports: a locale lunr can't stem (sk)
// is still built and served, its content still indexed, just tokenized with the
// default analyzer instead of a Slovak-specific stemmer — acceptable until/unless a
// Slovak stemmer exists. This stays LOCALES-driven: add a lunr-supported locale and it
// joins the search set automatically. (`en` needs no stemmer module.) Keep the set in
// sync with lunr-languages' shipped `lunr.*.js`.
const LUNR_SUPPORTED_LANGUAGES = new Set([
  'en', 'ar', 'da', 'de', 'nl', 'el', 'es', 'fi', 'fr', 'he', 'hi', 'hu', 'hy',
  'it', 'ja', 'jp', 'kn', 'ko', 'no', 'pl', 'pt', 'ro', 'ru', 'sa', 'sv', 'ta',
  'te', 'th', 'tr', 'vi', 'zh',
]);
const SEARCH_LANGUAGES = LOCALES.filter((l) => LUNR_SUPPORTED_LANGUAGES.has(l));

// Blocking <head> script: on a first visit with no preference cookie, match the
// visitor's `navigator.languages` against LOCALES (English fallback) and redirect
// to the best locale, preserving path + hash. An existing cookie OR an explicit
// non-default locale already in the URL always wins, so we never fight a user's
// choice and never loop. It runs before paint (no flash) and is a no-op for
// non-JS crawlers, which get the requested URL as-is (hreflang still exposes every
// locale). Locale-list-driven: LOCALES/DEFAULT_LOCALE/BASE_URL are injected below.
// The cookie name is mirrored in src/lib/localePreference.ts — keep them in sync.
const localeDetectionScript = `
(function () {
  try {
    var LOCALES = ${JSON.stringify(LOCALES)};
    var DEFAULT = ${JSON.stringify(DEFAULT_LOCALE)};
    var BASE = ${JSON.stringify(BASE_URL)};
    var COOKIE = 'preferred_locale';

    function readCookie(name) {
      var m = document.cookie.match('(?:^|; )' + name + '=([^;]*)');
      return m ? decodeURIComponent(m[1]) : null;
    }
    function writeCookie(name, val) {
      document.cookie =
        name + '=' + encodeURIComponent(val) +
        '; path=' + BASE + '; max-age=' + (60 * 60 * 24 * 365) + '; samesite=lax';
    }

    var path = window.location.pathname;
    if (path.indexOf(BASE) !== 0) return;            // only act within our baseUrl
    var rest = path.slice(BASE.length);              // '' | 'ru/...' | 'llmops/...'
    var firstSeg = rest.split('/')[0];

    var nonDefault = LOCALES.filter(function (l) { return l !== DEFAULT; });
    var urlLocale = nonDefault.indexOf(firstSeg) !== -1 ? firstSeg : DEFAULT;

    // Any established preference (cookie) suppresses detection entirely — we never
    // auto-redirect against a choice the user has already made.
    var cookie = readCookie(COOKIE);
    if (cookie && LOCALES.indexOf(cookie) !== -1) return;

    // No cookie = genuine first visit.
    if (urlLocale !== DEFAULT) {
      // Arrived directly at a locale-prefixed URL → honor it, remember it.
      writeCookie(COOKIE, urlLocale);
      return;
    }

    // Bare default-locale path, no cookie → detect from the browser languages.
    var langs = (navigator.languages && navigator.languages.length)
      ? navigator.languages
      : (navigator.language ? [navigator.language] : []);
    var match = DEFAULT;                             // English fallback
    for (var i = 0; i < langs.length && match === DEFAULT; i++) {
      var tag = String(langs[i]).toLowerCase();
      var primary = tag.split('-')[0];
      for (var j = 0; j < LOCALES.length; j++) {
        var loc = LOCALES[j].toLowerCase();
        if (tag === loc || primary === loc) { match = LOCALES[j]; break; }
      }
    }

    writeCookie(COOKIE, match);
    if (match !== DEFAULT) {
      window.location.replace(
        BASE + match + '/' + rest + window.location.search + window.location.hash,
      );
    }
  } catch (e) {
    // Fail open: detection must never block or break the page.
  }
})();
`;

const config: Config = {
  title: 'AI Engineering Handbook',
  tagline: 'First-principles courses on production AI engineering — RAG, agents, and the AI-assisted SDLC',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  url: 'https://nikolaisachok.com',
  baseUrl: BASE_URL,
  organizationName: 'NikolaiSachok', // GitHub user/org
  projectName: 'ai-engineering-handbook',

  // Expose the course list to the client so the landing hub (src/pages/index.tsx)
  // renders its cards from the SAME source of truth as the navbar and search —
  // add a course to COURSES and it shows up on the landing page automatically.
  customFields: {
    courses: COURSES.map((c) => ({
      basePath: c.basePath,
      label: c.navbarLabel,
      blurb: c.blurb,
      // Only the locales this course claims AND the site actually ships. A card that
      // advertises a language the reader cannot switch to is worse than one that
      // undersells: German is claimed by both courses while it is still being
      // translated, and must not appear here until it launches.
      languages: c.locales
        .filter((loc) => RELEASED_LOCALES.includes(loc))
        .map((loc) => LOCALE_LABELS[loc]),
      live: c.live,
    })),
  },

  // Released (deployed) builds throw on any dead internal link — the hard gate for
  // shipped EN/RU content. The unreleased-inclusive validation build (CI, sets
  // HANDBOOK_INCLUDE_UNRELEASED=1) instead warns, because gated partial translation
  // produces one class of unavoidable, non-shipping "broken" link: an untranslated
  // fallback lesson (served from `docs/`) links to the glossary via a relative `.md`
  // path, and once the glossary alone is translated (Phase 1) Docusaurus can't
  // path-match that link across the `docs/` (fallback) and `i18n/<locale>/`
  // (translated) trees — nor would the EN slug even match the localized one — until
  // the lesson itself is translated. Those links resolve correctly in every deployed
  // (released) build. CI still hard-fails on real breakage: scripts/i18n-link-check.sh
  // greps this build's output and fails on any broken link whose source is NOT an
  // untranslated fallback page (i.e. EN, RU, or a genuinely-translated locale page).
  onBrokenLinks: INCLUDE_UNRELEASED ? 'warn' : 'throw',

  // Same treatment, same reasoning, for the `#fragment` half of a link (#300). Left
  // unset, Docusaurus defaults it to 'warn', which is how 124 dead "jump to the
  // glossary entry" links survived on `main`: a lesson's terms footer pointed at
  // `glossary.md#ingestion-chunking` while the heading `## Ingestion — chunking`
  // slugified to `ingestion--chunking`, so the reader landed at the top of a very
  // long page instead of at the entry. The fix is explicit `{#anchor}` ids on every
  // glossary heading in every locale (a translated heading slugifies to something
  // else entirely, so only an explicit id can satisfy a shared inbound link); this
  // setting is what stops it coming back silently. It mirrors `onBrokenLinks` rather
  // than throwing unconditionally because a partially-translated locale hits the same
  // fallback/translated path-matching gap — and scripts/i18n-link-check.sh applies the
  // same "real break vs tolerable fallback" test to broken anchors, so released
  // locales stay hard-gated in CI too.
  onBrokenAnchors: INCLUDE_UNRELEASED ? 'warn' : 'throw',

  // Browser-language auto-detect + cookie, injected as a blocking <head> script so
  // it runs before paint (no flash-of-wrong-language). See `localeDetectionScript`.
  headTags: [
    {
      tagName: 'script',
      attributes: {type: 'text/javascript'},
      innerHTML: localeDetectionScript,
    },
  ],

  // Enable Mermaid diagrams in Markdown code blocks (```mermaid).
  markdown: {
    mermaid: true,
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },
  themes: [
    '@docusaurus/theme-mermaid',
    // Local, zero-config offline search. Builds a client-side index at build time
    // (no external service / network calls). Indexes the docs in every locale.
    [
      require.resolve('@easyops-cn/docusaurus-search-local'),
      {
        hashed: true,
        indexDocs: true,
        indexBlog: true, // the EN-only "Field notes" making-of blog (preset `blog` above)
        // Index EVERY course instance. The plugin accepts an array of route base
        // paths; derived from COURSES so a new course is indexed automatically.
        docsRouteBasePath: DOCS_ROUTE_BASE_PATHS,
        // Build a search index per locale. `language` is the set of lunr STEMMERS to
        // load — LOCALES minus codes lunr can't stem (see SEARCH_LANGUAGES above); an
        // unstemmed locale is still indexed with the default analyzer.
        language: SEARCH_LANGUAGES,
      },
    ],
  ],

  // i18n: English is the default/canonical locale (served at the site root);
  // Russian serves under /ru/. RU stays audience-primary in authoring (written
  // natively, never machine-translated) — this only sets URL/serving structure.
  // `localeConfigs` labels every locale we might build (released or not) — it is
  // harmless for a locale that isn't in `LOCALES`, so a label is set here permanently
  // the moment a locale is scaffolded (Slovak, now German); only `LOCALES` decides what
  // actually builds/serves. A label is NOT auto-derived from the locale code: a locale
  // in `LOCALES` with no `localeConfigs` entry fails the build outright, so add the
  // label in the SAME change that adds the locale.
  i18n: {
    defaultLocale: DEFAULT_LOCALE,
    locales: LOCALES,
    localeConfigs: Object.fromEntries(
      Object.entries(LOCALE_LABELS).map(([loc, label]) => [loc, {label}]),
    ),
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          // The RAG & Agents course is the DEFAULT docs instance. Its content
          // (`docs/`) and RU/SK i18n trees are frozen and UNCHANGED — only its
          // URL prefix moved from '/' to '/rag-agents' (the root is now the
          // landing hub). Everything under it (including the intro's `slug: /`)
          // is prefixed automatically; no content file changes.
          routeBasePath: DEFAULT_COURSE.basePath,
          // No "Edit this page" link: the site is read-only for visitors (no auth),
          // and the source is a click away on GitHub for the one person who edits it.
        },
        // "Field notes" — the making-of blog. This is the canonical long-form home
        // of how the handbook was built *using* the AI-assisted SDLC it teaches:
        // dated, first-person, teaching-framed field notes, each cross-linked to the
        // lesson it demonstrates. It is deliberately ENGLISH-ONLY (no i18n tree),
        // even though the curriculum ships EN/RU/SK — automated translation of
        // informal prose isn't at a bar worth publishing under the author's name yet,
        // and that limitation is itself one of the things the blog is about (there is
        // a standing note to that effect on the blog index, in the BlogListPage
        // swizzle). The curriculum's tri-lingual docs pipeline is untouched: because
        // no `i18n/<locale>/docusaurus-plugin-content-blog/` tree exists, the RU/SK
        // site builds simply fall back to the English posts — content stays English
        // everywhere by design.
        blog: {
          path: 'blog',
          routeBasePath: 'blog',
          blogTitle: 'Field notes — building this handbook with the SDLC it teaches',
          blogDescription:
            'The making-of this handbook: honest, dated field notes on building an ' +
            'AI-engineering curriculum using the AI-assisted SDLC it teaches. English-only.',
          blogSidebarTitle: 'Recent field notes',
          blogSidebarCount: 'ALL',
          showReadingTime: true,
          postsPerPage: 10,
          feedOptions: {
            type: ['rss', 'atom'],
            title: 'AI Engineering Handbook — Field notes',
            description:
              'The making-of this handbook: building an AI-engineering curriculum ' +
              'with the AI-assisted SDLC it teaches.',
            copyright: `Copyright © ${new Date().getFullYear()} Nikolai Sachok.`,
          },
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  // Every course AFTER the default one is its own docs instance, generated from
  // COURSES so adding a course needs no bespoke wiring here. Each gets its own
  // content dir (`docs-<id>/`), URL prefix, and sidebar; its i18n lives under
  // `i18n/<loc>/docusaurus-plugin-content-docs-<id>/`.
  plugins: [
    ...COURSES.slice(1).map((c): [string, Record<string, unknown>] => [
      '@docusaurus/plugin-content-docs',
      {
        id: c.id,
        path: `docs-${c.id}/`,
        routeBasePath: c.basePath,
        sidebarPath: `./sidebars-${c.id}.ts`,
      },
    ]),
  ],

  themeConfig: {
    image: 'img/og-card.jpg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      // The site is a HUB — the global brand is the hub, not any one course.
      // Each course is identified by its URL prefix + sidebar, not the navbar title.
      title: 'AI Engineering Handbook',
      logo: {
        alt: 'AI Engineering Handbook',
        src: 'img/logo.svg',
        srcDark: 'img/logo-dark.svg',
      },
      items: [
        // One docSidebar item per course that's ready to show. Derived from
        // COURSES: a course appears here only once its `inNavbar` flag is true, so
        // a course can be authored in-tree before it is advertised. The default
        // instance needs no `docsPluginId`; named instances reference their own id.
        ...COURSES.filter((c) => c.inNavbar).map((c) => ({
          type: 'docSidebar' as const,
          sidebarId: c.sidebarId,
          ...(c.id === 'default' ? {} : {docsPluginId: c.id}),
          position: 'left' as const,
          label: c.navbarLabel,
        })),
        // "Field notes" — the making-of blog (English-only; see the preset `blog`).
        {to: '/blog', label: 'Field notes', position: 'left'},
        {
          type: 'localeDropdown',
          position: 'right',
        },
        {href: 'https://github.com/NikolaiSachok/ai-engineering-handbook', label: 'GitHub', position: 'right'},
      ],
    },
    footer: {
      // A compact sitemap of the WHOLE site — most useful on phones, where the
      // sidebar is hidden behind the burger, so the footer is the only
      // always-visible navigation.
      //
      // One column PER COURSE, derived from COURSES (same source of truth as the
      // navbar, the search index and the landing hub) plus a trailing "Project"
      // column for the site-wide things that belong to no course. Columns are
      // titled with the course name, so a link's owning course is never ambiguous
      // — the old shape ("Contents" / "Reference") silently meant "the RAG course"
      // and left AI SDLC and the blog unreachable from the footer entirely.
      // Adding a course = adding it to COURSES with its `footerLinks`; no edit here.
      style: 'dark',
      links: [
        ...COURSES.filter((c) => c.inNavbar).map((c) => ({
          title: c.navbarLabel,
          items: c.footerLinks.map((l) => ({
            label: l.label,
            to: l.path ? `${c.basePath}/${l.path}` : `${c.basePath}/`,
          })),
        })),
        {
          // Site-wide, course-independent. "Field notes" is the making-of blog
          // (English-only by design — see the preset `blog` above).
          title: 'Project',
          items: [
            {label: 'Field notes', to: '/blog'},
            {label: 'GitHub', href: 'https://github.com/NikolaiSachok/ai-engineering-handbook'},
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Nikolai Sachok. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
