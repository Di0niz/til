# Обновление сертификата

1. Скачиванием дистрибутив

  wget https://dl.eff.org/certbot-auto

2. Установка прав на файл

  chmod a+x certbot-auto

3. Запуск для получения сертификата в ручном режиме

  ./certbot-auto certonly --authenticator manual

4. Запускаем сервер для проверки сертификата:
```
mkdir -p /tmp/letsencrypt/public_html/.well-known/acme-challenge
cd /tmp/letsencrypt/public_html
printf "%s" 4vzlMYR6A13xxx > .well-known/acme-challenge/4vzlMYR6A13Ao57kbxxx
python2.7 -c "import BaseHTTPServer, SimpleHTTPServer; SimpleHTTPServer.SimpleHTTPRequestHandler.extensions_map = {'': 'text/plain'}; s = BaseHTTPServer.HTTPServer(('', 80), SimpleHTTPServer.SimpleHTTPRequestHandler); s.serve_forever()"
```
