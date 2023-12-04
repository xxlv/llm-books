import os
import toml 

def get_book_title(folder):
    toml_file = os.path.join(folder, 'book.toml')

    # 检查是否存在book.toml文件
    if os.path.exists(toml_file):
        with open(toml_file, 'r', encoding='utf-8') as f:
            toml_data = toml.load(f)

            # 从book.toml文件中获取标题
            return toml_data.get('book', {}).get('title', '')
    
    return ''


def generate_book_links():
    book_links = []
    books_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.')

    # 遍历当前文件夹下的所有第一层文件夹
    for folder in os.listdir(books_dir):
        folder_path = os.path.join(books_dir, folder)

        # 检查是否为文件夹且不以点开头
        if os.path.isdir(folder_path) and not folder.startswith('.'):
            # 获取书籍标题
            book_title = get_book_title(folder_path)
            
            # 生成书籍链接
            if book_title:
                book_link = f'<li><a href="{folder}/index.html" title="{book_title}">{book_title}</a></li>'
                book_links.append(book_link)

    return '\n'.join(book_links)


def generate_html():
    # 生成书籍链接
    book_links = generate_book_links()

    # 添加样式
    styles = """
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        h1 {
            color: #333;
        }

        ol {
            padding: 0;
            list-style-type: decimal;
        }

        li {
            margin-bottom: 10px;
        }

        a {
            text-decoration: none;
            color: #0066cc;
            font-weight: bold;
        }

        a:hover {
            color: #004080;
        }
    </style>
    """

    # 构建HTML内容
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Book List</title>
        {styles}
    </head>
    <body>
        <h1>My Book List</h1>
        <ol>
            {book_links}
        </ol>
    </body>
    </html>
    """

    # 将HTML内容写入文件
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == '__main__':
    # 生成HTML文件
    generate_html()
    print('HTML file "index.html" has been generated.')
