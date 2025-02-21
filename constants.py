from enum import Enum

class FileName(Enum):
    DATE = 0
    TITLE = 1

TEMPLATE = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>My Minimal Blog</title>
        <link rel="stylesheet" href="styles.css">
        <link rel="stylesheet" type="text/css" href="syntax.css"> 
    </head>
    <body>
    <!-- Header with navigation links -->
      <header>
        <nav>
          <a href="/">Home</a>
          <a href="/resume.html" target="_blank">Resume</a>
        </nav>
      </header>

    <!-- Brief intro -->
    <section class="intro">
        <h1>Jordan Walsh</h1>
        <p>Hello! I'm Jordan - Software Engineer, husband and father. This is a personal blog where I share my thoughts, projects, and updates.</p>
    </section>

    <!-- rendered blog posts -->
    <section id="posts">
        {% for title, date, content in posts %}
        <article>
            <h4> {{ date }}</h4>
            <div>
                {{ content }}
            </div>
        </article>
        {% endfor %}
    </section>
</body>
</html>
"""
