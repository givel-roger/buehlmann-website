# Statische Webseite Bühlmann Söhne AG, ausgeliefert via nginx
FROM nginx:alpine

# Nur die fertigen Webdateien ins Image (kein build.py, kein Git, kein code.html)
COPY assets/           /usr/share/nginx/html/assets/
COPY *.html            /usr/share/nginx/html/
COPY sitemap.xml robots.txt /usr/share/nginx/html/
RUN rm -f /usr/share/nginx/html/code.html

COPY deploy/nginx-site.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
