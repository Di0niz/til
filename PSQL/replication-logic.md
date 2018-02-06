## Настройка логической репликации

Элемент конфигурационного файла docker-compose.xml

```
  db1:
    image: postgres:alpine
    restart: always
    environment:
      POSTGRES_PASSWORD: example
    volumes:
      - ./pg2:/var/lib/postgresql/data
```

Подключаемся к созданному контейнеру
```
docker exec -t -i 1d0d68b61af4 /bin/bash
```
1d0d68b61af4 - ID контейнера определяемый по команде docker ps

Установка пароля для доступа к базе данных:
```
ALTER USER "postgres" WITH PASSWORD 'example';
```

Команды настройки репликации данных для постгресса:

```
pg_recvlogical -d cybergame1 --slot test --create-slot
pg_recvlogical -d cybergame1 --slot test --start -f -
```
