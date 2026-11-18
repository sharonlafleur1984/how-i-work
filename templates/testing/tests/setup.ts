import { afterEach, vi } from 'vitest';
import { cleanup } from '@testing-library/react';

// Each test starts clean: nothing left on the page or in saved preferences from the test before it.
afterEach(() => { cleanup(); localStorage.clear(); sessionStorage.clear(); });

// The test browser (jsdom) doesn't have these. Stand-ins keep components that use them from crashing.
vi.stubGlobal('ResizeObserver', class { observe() {} unobserve() {} disconnect() {} });
vi.stubGlobal('matchMedia', () => ({ matches: false, addListener() {}, removeListener() {}, addEventListener() {}, removeEventListener() {} }));
Element.prototype.scrollIntoView = vi.fn();
