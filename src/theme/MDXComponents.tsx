import MDXComponents from '@theme-original/MDXComponents';
import Infographic from '@site/src/components/Infographic';
import InfoCard, {Branch, Flow, Grid, Lane, Merge, Node} from '@site/src/components/InfoCard';
import Reveal from '@site/src/components/Reveal';
import Verdict from '@site/src/components/Verdict';
import YouTube from '@site/src/components/YouTube';

// Register components globally so any .md/.mdx page can use them without an import.
// `InfoCard` + Lane/Node/Flow/Branch/Merge/Grid compose a card from HTML, so its labels are real
// text and localise. `Infographic` renders a whole generated card image and stays registered for
// the cards that are still rasters (the cost comparison) and for the RU/SK pages, whose labels are
// not translated yet. `Verdict` sets a Design Scenario's assessment apart from the answer it
// judges — a component rather than an admonition because the attempts live inside a `<details>`
// reveal, where Docusaurus does not process `:::` directives. `Reveal` is that reveal: a plain
// <details> would pick up the themed alert plate, which is right for a short collapsible and
// wrong for one holding a whole page.
export default {
  ...MDXComponents,
  Branch,
  Grid,
  InfoCard,
  Infographic,
  Flow,
  Lane,
  Merge,
  Node,
  Reveal,
  Verdict,
  YouTube,
};
