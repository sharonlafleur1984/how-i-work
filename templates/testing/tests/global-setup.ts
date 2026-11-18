// import { execFileSync } from 'node:child_process';

// Runs once, before any test file. If tests read a generated file (CSS built from Figma tokens, say), build it here.
// Never build it inside a test: test files run in parallel, and one reads the file while another is rewriting it,
// so tests fail at random. (Found in voyager-code, Nov 18, 2026: 53 bad reads out of 561.)
export default function setup() {
  // Example. Uncomment the import and this line, and point it at the repo's own build step:
  // execFileSync('node', ['scripts/build-tokens.mjs'], { stdio: 'pipe' });
}
