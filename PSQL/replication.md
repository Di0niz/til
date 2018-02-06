## Настройка физической репликации

Элемент конфигурационного файла docker-compose.xml

```
  mpg1:
    image: postgres:alpine
    restart: always
    environment:
      POSTGRES_PASSWORD: example
    volumes:
      - ./mpg1:/var/lib/postgresql/data


  spg1:
    image: postgres:alpine
    restart: always
    environment:
      POSTGRES_PASSWORD: example
    volumes:
      - ./spg1:/var/lib/postgresql/data

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
psql -c "select pg_start_backup('initial_backup');"
rsync -cva --inplace --exclude=*pg_xlog* /var/lib/pgsql/data/userdata spg1:/var/lib/pgsql/data/userdata
psql -c "select pg_stop_backup();"
```
