import { readFileSync, readdirSync, statSync } from 'node:fs';
import { join } from 'node:path';

// Shared by the tests that read CSS, so each test file doesn't keep its own copy.
export const stripComments = (css: string) => css.replace(/\/\*[\s\S]*?\*\//g, '');
export const cssRules = (css: string) =>
  [...stripComments(css).matchAll(/([^{}]+)\{([^{}]*)\}/g)].map((m) => ({ sel: m[1].trim(), body: m[2] }));
/** Every .css file under a folder, generated folders skipped. */
export const cssFiles = (dir = 'src'): string[] => readdirSync(dir).flatMap((f) => {
  const p = join(dir, f);
  if (statSync(p).isDirectory()) return ['node_modules', 'build', 'dist'].includes(f) ? [] : cssFiles(p);
  return p.endsWith('.css') ? [p] : [];
});
export const readCss = (file: string) => stripComments(readFileSync(file, 'utf8'));
/** The CSS with every block for a person's accessibility setting taken out: reduce motion, forced colors and more
 *  contrast. Their choice has to win over every other style, so these blocks may use !important. */
export const withoutAccessibilitySettings = (css: string) => {
  const open = /@media[^{]*\((?:prefers-reduced-motion|forced-colors|prefers-contrast)\b[^{]*\{/g;
  let out = css;
  for (let m = open.exec(out); m; m = open.exec(out)) {
    let depth = 1, i = m.index + m[0].length;
    while (i < out.length && depth) depth += out[i] === '{' ? 1 : out[i] === '}' ? -1 : 0, i++;
    out = out.slice(0, m.index) + out.slice(i);
    open.lastIndex = m.index;
  }
  return out;
};
