// CSS rules from the product-engineer skill: styles stay easy to change because nothing forces its way past the
// cascade. No !important, no ID selectors, and spacing written with logical properties (margin-inline,
// padding-block) so the layout follows the reading direction.
import { describe, expect, it } from 'vitest';
import { cssFiles, cssRules, readCss, withoutAccessibilitySettings } from './css';

const files = cssFiles();

describe('CSS rules', () => {
  it("uses no !important, except to honor a person's accessibility setting", () => {
    expect(withoutAccessibilitySettings('a { b: c; } @media (prefers-reduced-motion: reduce) { * { animation: none !important; } } d { e: f; }')).not.toMatch(/!important/);
    for (const f of files) expect(withoutAccessibilitySettings(readCss(f)).match(/!important[^;]*/g) ?? [], f).toEqual([]);
  });
  it('uses no ID selectors', () => {
    for (const f of files) {
      const ids = cssRules(readCss(f)).map((r) => r.sel).filter((sel) => !sel.startsWith('@') && /(^|[\s,>+~(])#[a-zA-Z_-]/.test(sel));
      expect(ids, f).toEqual([]);
    }
  });
  it('writes spacing with logical properties', () => {
    for (const f of files) expect(readCss(f).match(/\b(margin|padding)-(left|right|top|bottom)\s*:/g) ?? [], f).toEqual([]);
  });
});
