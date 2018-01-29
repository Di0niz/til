Установка node.js 

1. Настройка сборки:

.Dockerfile

```
FROM mhart/alpine-node:8

WORKDIR /app
#COPY . .


#installing react app first
RUN npm install -g create-react-app

VOLUME [ "/app" ]

#First example was EXPOSE 3000 35729
EXPOSE 3000
EXPOSE 35729

```

| docker build ./{nodefolder} -t nodejs-app

2. Запуск и настройка приложения 

| docker run -it -p 3000:3000 -p 35729:35729 -v $(pwd)/{nodefolder}/app:/app nodejs-app

3. Выполнение команд по настройке :
```
cd /app
create-react-app .
yarn start
```
4. Конфигурирования сервера Nodejs:

docker-compose.xml

```
version: '2'
services:
  web:
    build: ./{nodefolder}
    volumes:
        - "./{nodefolder}/app:/app"
    ports:
        - "3000:3000"
        - "35729:35729"
```        
Полезная функция (зайти в контейнер):

# Enter the container
$ docker exec -it <container id> /bin/bash
  
5. Дополнительная настройка

.dockerignore
