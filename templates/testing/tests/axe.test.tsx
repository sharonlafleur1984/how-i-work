// The same engine as the A11y Agent audit, run on every test run, so an accessibility issue fails the tests instead
// of waiting for someone to run an audit. Color contrast is off: the test browser can't measure colors. The live
// audit covers contrast. axe catches only part of WCAG, so still Tab through new screens.
import { render, screen } from '@testing-library/react';
import { expect, it } from 'vitest';
import { App } from '../src/app'; // Replace with the repo's main page.

it('the main page has no axe issues at WCAG 2.2 A and AA', async () => {
  const { container } = render(<App />);
  await screen.findByRole('heading', { level: 1 });
  const axe = (await import('axe-core')).default;
  const results = await axe.run(container, {
    runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'] },
    rules: { 'color-contrast': { enabled: false } },
  });
  expect(results.violations.map((v) => `${v.id} (${v.nodes.length}): ${v.help}`)).toEqual([]);
}, 30000);
