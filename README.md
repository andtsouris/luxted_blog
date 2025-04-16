# Luxted Blog

A simple blog website built with HTML, Tailwind CSS, and Markdown.

## Features

- Modern, responsive design using Tailwind CSS
- Markdown support for writing articles
- Syntax highlighting for code blocks
- Clean and minimal UI

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Convert markdown articles to HTML:
```bash
python convert.py
```

3. Open `index.html` in your browser to view the blog.

## Adding New Articles

1. Create a new markdown file in the `articles` directory
2. Write your article using markdown syntax
3. Run `python convert.py` to convert the markdown to HTML
4. The new article will be available on the blog

## Project Structure

```
luxted_blog/
├── index.html          # Main blog page
├── articles/           # Directory for markdown articles
│   ├── tailwind-intro.md
│   └── markdown-guide.md
├── convert.py          # Script to convert markdown to HTML
└── requirements.txt    # Python dependencies
```

## Technologies Used

- HTML5
- Tailwind CSS
- Markdown
- Python
- markdown2 (for markdown to HTML conversion)
- highlight.js (for code syntax highlighting)

## License

MIT License 