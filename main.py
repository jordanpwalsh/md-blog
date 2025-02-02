import os
from markdown import markdown

def read_posts(directory):
    posts = []
    for filename in sorted(os.listdir(directory), reverse=True):
        if filename.endswith(".md"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                content = file.read()
                html_content = markdown(content)
                posts.append((filename[:-3], html_content))
    return posts

def render_posts(posts):
    html = "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<title>Blog</title>\n<link rel=\"stylesheet\" href=\"styles.css\">\n</head>\n<body>"
    for title, content in posts:
        html += f"<h2>{title}</h2><div>{content}</div>"
    html += "</body></html>"
    return html

if __name__ == "__main__":
    # Changed the greeting from "Hello" to "Hey"
    print("Hey! Here are your blog posts:")
    
    posts = read_posts("/posts")
    print(render_posts(posts))
