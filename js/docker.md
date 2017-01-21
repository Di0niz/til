Установка node.js 


.Dockerfile

from node:latest
# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
# Install app dependencies
COPY package.json /usr/src/app/
RUN npm install
# Bundle app source
COPY . /usr/src/app
EXPOSE 8080
CMD [ "npm", "start" ]


docker-compose.xml

version: '2'
services:
  web:
    build: .
    volumes:
        - "./app:/usr/src/app"
    ports:
        - "8080:8080"
        
Полезная функция (зайти в контейнер):

# Enter the container
$ docker exec -it <container id> /bin/bash
