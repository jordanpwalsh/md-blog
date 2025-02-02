import os
from markdown import markdown
from jinja2 import Template
from io import StringIO

from constants import TEMPLATE


def read_posts(directory):
    posts = []
    for filename in sorted(os.listdir(directory), reverse=True):
        if filename.endswith(".md"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                print(f"Reading file: {filename}")
                content = file.read()
                filename_parts = filename.split("_")
                post_date = filename_parts[0]
                post_title = filename_parts[1][:-3]
                post_content = markdown(content)
                posts.append((post_title, post_date, post_content))
    return posts

def render_posts(posts):
    template = Template(TEMPLATE)
    html = template.render(posts=posts)
    return html

if __name__ == "__main__":
    posts = read_posts("posts")
    print(render_posts(posts))
