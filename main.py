import os
import sys
from markdown import markdown
from jinja2 import Environment, FileSystemLoader


def read_posts(directory):
    posts = []
    for filename in sorted(os.listdir(directory), reverse=True):
        if 'draft' in filename.lower():
            print(f"Skipping draft post: {filename}", file=sys.stderr)
            continue
        if filename.endswith(".md"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                print(f"Reading file: {filename}", file=sys.stderr)
                content = file.read()
                filename_parts = filename.split("_")
                post_date = filename_parts[0]
                post_title = filename_parts[1][:-3]
                post_content = markdown(content, extensions=[
                    "extra",
                    "fenced_code",   # Enables triple-backtick code blocks
                    "tables",        # Enables Markdown tables
                    "toc",           # Adds a Table of Contents
                    "sane_lists",    # Improves list handling
                    "codehilite"    # Enables syntax highlighting
                ])
                posts.append((post_title, post_date, post_content))
    return posts

def render_posts(posts):
    env = Environment(loader=FileSystemLoader("skel"))
    template = env.get_template("template.html")
    html = template.render(posts=posts)
    return html

if __name__ == "__main__":
    posts = read_posts("posts")
    print(render_posts(posts))
