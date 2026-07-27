import MDXComponents from '@theme-original/MDXComponents';
import Infographic from '@site/src/components/Infographic';
import InfoCard, {Branch, Flow, Grid, Lane, Merge, Node} from '@site/src/components/InfoCard';
import YouTube from '@site/src/components/YouTube';

// Register components globally so any .md/.mdx page can use them without an import.
// `InfoCard` + Lane/Node/Flow/Branch/Merge/Grid compose a card from HTML, so its labels are real
// text and localise. `Infographic` renders a whole generated card image and stays registered for
// the cards that are still rasters (the cost comparison) and for the RU/SK pages, whose labels are
// not translated yet.
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
  YouTube,
};
