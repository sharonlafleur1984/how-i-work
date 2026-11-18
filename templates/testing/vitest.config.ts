// Goes in the repo root. Runs every file named *.test.ts or *.test.tsx in tests/.
import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    // Runs once before any test file. Build generated files here, never inside a test (see global-setup.ts).
    globalSetup: ['./tests/global-setup.ts'],
    // Runs before each test file: shared clean-up and browser stand-ins.
    setupFiles: ['./tests/setup.ts'],
    include: ['tests/**/*.test.{ts,tsx}'],
  },
});
