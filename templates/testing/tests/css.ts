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
