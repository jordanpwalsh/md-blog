FROM python:3.12-slim as builder

WORKDIR /app

COPY . .

RUN pip install jinja2 markdown pygments
RUN python main.py > index.html

#Web Server Container
FROM nginx

COPY --from=builder /app/index.html /usr/share/nginx/html
COPY posts/images /usr/share/nginx/html/images
COPY resume.html /usr/share/nginx/html
COPY styles.css /usr/share/nginx/html
COPY syntax.css /usr/share/nginx/html
