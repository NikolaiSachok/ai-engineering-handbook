/**
 * Locale routing on client-side navigation.
 *
 * The blocking <head> script in docusaurus.config.ts (`localeDetectionScript`) moves a reader
 * whose page does not exist in their locale to the English page, and back once it does. It
 * runs once per full page load, but navbar, sidebar and in-content links navigate inside the
 * single-page app, so a German reader clicking from the RAG course to the English+Russian
 * Azure course would otherwise land on `/de/azure-dotnet/` — German chrome over English pages.
 * This calls the same function on every route update, before the new route renders.
 */

import type {ClientModule} from '@docusaurus/types';

declare global {
  interface Window {
    __handbookLocaleRedirect?: (location: {pathname: string; search: string; hash: string}) => boolean;
  }
}

const clientModule: ClientModule = {
  onRouteUpdate({location, previousLocation}) {
    // The initial render was already handled by the head script.
    if (!previousLocation || typeof window === 'undefined') {
      return;
    }
    window.__handbookLocaleRedirect?.(location);
  },
};

export default clientModule;
