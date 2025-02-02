TEMPLATE = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <title>Blog</title>
    <link rel="stylesheet" href="styles.css">
    </head>
    <body>
    {% for title, date, content in posts %}
    <h2>{{ title }}</h2>
    <h4> {{ date }}</h4>
        <div>
            {{ content }}
        </div>
    {% endfor %}
    </body>
    </html>
"""
