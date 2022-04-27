### Docker compose

Docker compose é um binario que possibilita a instalação de mutiplos container ao mesmo tempo === um orquestrador de containeres.

Exemplo de arquivo docker-compose.yml

 docker-compose.yml # version "3"
 
 services 
 my-first-build: 
 container_name: my-first-build 
 image: my-first-build 
 build: . 
  volumes: - ./src:/src 
  ports: - 8080:8080 
expose: - "8080"
 node: image: node volumes: - ./src:/src ports: - 3000:80
 
 ##### instalando o coker compose
 
 sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
 
 sudo chmod +x /usr/local/bin/docker-compose
 docker-compose --version
 
 
 ### Utilizando o docker-compose
 
 