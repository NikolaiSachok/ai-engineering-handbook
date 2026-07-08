import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Enterprise RAG & Agents Handbook',
  tagline: 'A practical, first-principles guide to production RAG and agentic systems',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // TODO: set before first public deploy (real domain + GitHub org/user).
  url: 'https://example.com',
  baseUrl: '/enterprise-rag-agents-handbook/',
  organizationName: 'PLACEHOLDER', // TODO: GitHub org/user name — set before first public deploy
  projectName: 'enterprise-rag-agents-handbook',

  onBrokenLinks: 'throw',

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
    // (no external service / network calls). Index docs + blog for both locales.
    [
      require.resolve('@easyops-cn/docusaurus-search-local'),
      {
        hashed: true,
        indexDocs: true,
        indexBlog: true,
        docsRouteBasePath: '/',
        // Build a search index per locale.
        language: ['en', 'ru'],
      },
    ],
  ],

  // i18n: Russian is the primary/default locale; English is secondary.
  i18n: {
    defaultLocale: 'ru',
    locales: ['ru', 'en'],
    localeConfigs: {
      ru: {label: 'Русский'},
      en: {label: 'English'},
    },
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          // Serve the docs (the handbook) at the site root.
          routeBasePath: '/',
          // TODO: set editUrl to the real repo before first public deploy.
          // editUrl: 'https://github.com/PLACEHOLDER/enterprise-rag-agents-handbook/tree/main/',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // TODO: set editUrl to the real repo before first public deploy.
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'RAG & Agents Handbook',
      logo: {
        alt: 'Enterprise RAG & Agents Handbook',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'handbookSidebar',
          position: 'left',
          label: 'Handbook',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
        {
          type: 'localeDropdown',
          position: 'right',
        },
        // TODO: set GitHub URL before first public deploy.
        // {href: 'https://github.com/PLACEHOLDER/enterprise-rag-agents-handbook', label: 'GitHub', position: 'right'},
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Handbook',
          items: [
            {label: 'Введение', to: '/'},
            {label: 'Глоссарий', to: '/glossary'},
          ],
        },
        {
          title: 'More',
          items: [
            {label: 'Blog', to: '/blog'},
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
