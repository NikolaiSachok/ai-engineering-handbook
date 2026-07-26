import MDXComponents from '@theme-original/MDXComponents';
import Infographic from '@site/src/components/Infographic';
import InfoCard, {Brace, Flow, Lane, Node} from '@site/src/components/InfoCard';
import YouTube from '@site/src/components/YouTube';

// Register components globally so any .md/.mdx page can use them without an import.
// `Infographic` renders a whole generated card image; `InfoCard` + Lane/Node/Flow/Brace compose
// the same kind of card from HTML, so its labels localise. Both are live while the composed
// approach is under review.
export default {
  ...MDXComponents,
  Brace,
  InfoCard,
  Infographic,
  Flow,
  Lane,
  Node,
  YouTube,
};
