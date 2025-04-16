import markdown
import os
import re
from bs4 import BeautifulSoup

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
        <link rel="stylesheet" href="../styles.css">
    </head>
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
            <article class="prose prose-lg max-w-none">
                {html_content}
            </article>
        </main>

        <!-- Footer -->
        <footer class="bg-gray-800 text-white">
            <div class="max-w-4xl mx-auto px-4 py-8">
                <div class="text-center">
                    <p>&copy; 2024 Luxted Blog. All rights reserved.</p>
                </div>
            </div>
        </footer>

        <script>
            document.addEventListener('DOMContentLoaded', (event) => {{
                document.querySelectorAll('pre code').forEach((block) => {{
                    hljs.highlightBlock(block);
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

def main():
    # Convert all markdown files in the current directory
    for file in os.listdir('./articles'):
        if file.endswith('.md'):
            convert_markdown_to_html(os.path.join('./articles', file))

if __name__ == "__main__":
    main() 