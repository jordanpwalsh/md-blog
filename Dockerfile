FROM nginx

COPY index.html /usr/share/nginx/html
COPY resume.html /usr/share/nginx/html
COPY styles.css /usr/share/nginx/html
