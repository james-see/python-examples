# Python Examples Documentation Site

This is the source for the GitHub Pages documentation site for python-examples.

## 🚀 Built With

- **Astro** - Fast, content-focused static site generator
- **Academic Paper Design** - Clean, professional typography inspired by research papers
- **Interactive Filtering** - Search and filter examples by category
- **Personality** - Easter eggs and touches that show character

## 🛠️ Development

```bash
cd docs

# Install dependencies
npm install

# Start dev server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 📁 Structure

```
docs/
├── src/
│   ├── layouts/     # Page layouts
│   ├── pages/       # Astro pages
│   ├── styles/      # Global CSS
│   └── components/  # Reusable components (future)
├── public/          # Static assets
└── astro.config.mjs # Astro configuration
```

## 🎨 Design Philosophy

- **Academic aesthetic** - Serif fonts, paper-like background, numbered sections
- **Monospace code** - JetBrains Mono for all code examples
- **Accent color** - Burnt orange (#d35400) for personality
- **Clean typography** - Crimson Pro for body, Inter for UI elements
- **Interactive** - Search, filters, and easter eggs for engagement

## 🚀 Deployment

The site automatically deploys to GitHub Pages when changes are pushed to master via GitHub Actions.

## 🎯 Features

- ✅ Responsive design
- ✅ Search functionality
- ✅ Category filtering
- ✅ Print-friendly (for actual paper)
- ✅ Easter egg (Konami code)
- ✅ Fast static site generation
- ✅ Academic paper styling

## 📝 Adding New Examples

Edit `src/pages/index.astro` and add to the `examples` array:

```javascript
{
  title: 'your-example.py',
  description: 'What it does',
  category: 'Category Name',
  tags: ['tag1', 'tag2'],
  difficulty: 'beginner' // or 'intermediate', 'advanced'
}
```

The site will automatically update filters and search.
