import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://james-see.github.io',
  base: '/python-examples',
  outDir: '../dist',
  build: {
    assets: '_assets'
  }
});
