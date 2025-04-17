import markdown
import os
import re
from bs4 import BeautifulSoup
import yaml

def convert_markdown_to_html(markdown_file):
    # Read markdown content
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Convert markdown to HTML
    html_content = markdown.markdown(content, extensions=['fenced_code', 'codehilite'])
    
    # Create HTML structure
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Luxted 5</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github.min.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
        <link rel="stylesheet" href="../styles.css">
    </head>
    <style>
        .title-circle {{
            display: inline-block;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            margin-right: 0px;
            background-color: #ef4444;
        }}
        /* Header styles */
        h1 {{ font-size: 2.5rem !important; font-weight: 800 !important; margin-top: 2rem !important; margin-bottom: 1.5rem !important; }}
        h2 {{ font-size: 2rem !important; font-weight: 700 !important; margin-top: 1.75rem !important; margin-bottom: 1.25rem !important; }}
        h3 {{ font-size: 1.75rem !important; font-weight: 600 !important; margin-top: 1.5rem !important; margin-bottom: 1rem !important; }}
        h4 {{ font-size: 1.5rem !important; font-weight: 600 !important; margin-top: 1.25rem !important; margin-bottom: 0.75rem !important; }}
        h5 {{ font-size: 1.25rem !important; font-weight: 600 !important; margin-top: 1rem !important; margin-bottom: 0.5rem !important; }}
        h6 {{ font-size: 1.1rem !important; font-weight: 600 !important; margin-top: 0.75rem !important; margin-bottom: 0.5rem !important; }}
        /* Bold text */
        strong, b {{ font-weight: 900 !important; }}
        /* Code block styles */
        .code-container {{
            position: relative;
            margin: 1rem 0;
        }}
        .copy-button {{
            position: absolute;
            top: 0.5rem;
            right: 0.5rem;
            padding: 0.25rem 0.5rem;
            background-color: #f8f9fa;
            border: 1px solid #e5e7eb;
            border-radius: 0.25rem;
            cursor: pointer;
            color: #6b7280;
            transition: all 0.2s;
        }}
        .copy-button:hover {{
            border: 1px solid #5f5f5f !important;
            background-color: #e5e7eb;
            color: #5f5f5f;
        }}
        pre {{
            background-color: #f8f9fa !important;
            border: 1px solid #e5e7eb !important;
            border-radius: 0.5rem !important;
            padding: 0.5rem !important;
            padding-left: 0rem !important;
            padding-bottom: 1rem !important;
            margin: 0 !important;
            overflow-x: auto !important;
            position: relative;
        }}
        pre code {{
            font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace !important;
            font-size: 0.875rem !important;
            background-color: #f8f9fa !important;
            line-height: 0.8 !important;
            counter-reset: line;
        }}
        pre code .line {{
            display: block;
            padding-left: 3.5rem;
            position: relative;
            margin: 0 !important;
        }}
        pre code .line::before {{
            counter-increment: line;
            content: counter(line);
            position: absolute;
            left: 0;
            width: 2.5rem;
            text-align: right;
            padding-right: 0.5rem;
            color: #5f5f5f;
            user-select: none;
        }}
        /* Inline code */
        p code, li code {{
            background-color: #f3f4f6 !important;
            border: 1px solid #e5e7eb !important;
            border-radius: 0.25rem !important;
            padding: 0.125rem 0.25rem !important;
            font-size: 0.875rem !important;
        }}
    </style>
    <body>
        <!-- Navigation -->
        <nav class="bg-white shadow-lg">
            <div class="max-w-4xl mx-auto px-4">
                <div class="flex justify-between items-center py-4">
                    <a href="../index.html" class="text-2xl font-bold text-gray-800 blog-title flex items-center hover:text-gray-600">
                        Luxted
                        <span class="title-circle ml-1 mr-1 mt-3"></span>
                        5
                    </a>
                </div>
            </div>
        </nav>

        <!-- Main Content -->
        <main class="max-w-4xl mx-auto px-4 py-8">
            <article class="prose prose-lg max-w-none mb-32">
                {html_content}
            </article>
        </main>

        <!-- Footer -->
        <footer class="bg-gray-800 text-white">
            <div class="max-w-4xl mx-auto px-4 py-8">
                <div class="text-center">
                    <p>&copy; 2025 Luxted.5 Blog. All rights reserved.</p>
                </div>
            </div>
        </footer>

        <script>
            document.addEventListener('DOMContentLoaded', (event) => {{
                // Initialize highlight.js
                document.querySelectorAll('pre code').forEach((block) => {{
                    hljs.highlightBlock(block);
                    
                    // Add line numbers
                    const lines = block.innerHTML.split('\\n');
                    block.innerHTML = lines.map((line, i) => {{
                        return `<span class="line">${{line}}</span>`;
                    }}).join('\\n');
                    
                    // Add copy button
                    const container = document.createElement('div');
                    container.className = 'code-container';
                    block.parentNode.parentNode.insertBefore(container, block.parentNode);
                    container.appendChild(block.parentNode);
                    
                    const copyButton = document.createElement('button');
                    copyButton.className = 'copy-button';
                    copyButton.innerHTML = '<i class="fas fa-copy"></i>';
                    copyButton.title = 'Copy to clipboard';
                    container.appendChild(copyButton);
                    
                    copyButton.addEventListener('click', async () => {{
                        const text = block.innerText;
                        try {{
                            await navigator.clipboard.writeText(text);
                            copyButton.innerHTML = '<i class="fas fa-check"></i>';
                            setTimeout(() => {{
                                copyButton.innerHTML = '<i class="fas fa-copy"></i>';
                            }}, 2000);
                        }} catch (err) {{
                            console.error('Failed to copy text: ', err);
                        }}
                    }});
                }});
            }});
        </script>
    </body>
    </html>
    """
    
    # Create output directory if it doesn't exist
    os.makedirs('articles', exist_ok=True)
    
    # Write HTML file
    output_file = os.path.join('articles', os.path.splitext(os.path.basename(markdown_file))[0] + '.html')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_template)
    
    print(f"Converted {markdown_file} to {output_file}")

def update_index_html(yaml_file):
    # Read YAML file
    with open(yaml_file, 'r', encoding='utf-8') as f:
        articles = yaml.safe_load(f)
    
    # Read index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
    
    # Find the articles container
    articles_container = soup.find('div', {'id': 'articles-container'})
    if not articles_container:
        print("Error: Could not find articles container in index.html")
        return
    
    # Clear existing articles
    articles_container.clear()
    
    # Add new articles
    for article in articles:
        article_div = soup.new_tag('article')
        article_div['class'] = 'article'
        article_div['data-category'] = article['category']
        
        article_html = f"""
        <div class="p-0">
            <div class="flex justify-between items-center mb-4">
                <div class="flex items-center">
                    <span class="category-circle {article['category']}"></span>
                    <h3 class="text-2xl font-semibold text-gray-900">{article['title']}</h3>
                </div>
                <div class="text-sm text-gray-500 flex items-center">
                    <span>{article['date']}</span>
                    <span class="mx-2">•</span>
                    <span>{article['readTime']}</span>
                </div>
            </div>
            <p class="text-gray-600 mb-4">{article['description']}</p>
            <a href="articles/{article['slug']}.html" class="inline-block text-blue-600 hover:text-blue-800">Read more →</a>
        </div>
        """
        article_div.append(BeautifulSoup(article_html, 'html.parser'))
        articles_container.append(article_div)
    
    # Write updated index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

def main():
    # Convert all markdown files in the current directory
    for file in os.listdir('./articles'):
        if file.endswith('.md'):
            convert_markdown_to_html(os.path.join('./articles', file))
    
    # Update index.html with article metadata
    update_index_html('articles/list.yaml')

if __name__ == "__main__":
    main() 