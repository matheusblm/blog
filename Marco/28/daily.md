## Introdução à contêineres Docker

Os containeres são ambientes isolados dispotos em um computador

ps
rm
run
stop
start

ps - Lista todos os containers ativos, com a flag -a lista todos.
rm - Deletar um container passando com argumento ID ou NAME.
run - cria um container a partir de uma imgaem local.
flags: 
--name : Define um nome para o contêiner a ser criado.
-p: Define o mapeamento de uma única porta do contêiner <host>:<container>
-e: Define uma variável de ambiente para o contêiner a ser criado.
-d: Após a criação do contêiner, ele é iniciado no background.
stop - para a execução de um ou mais containers, passados como argumento seu ID ou NAME.
start - inicia containeres parados, argumentos id ou name.

## Docker 05 - Iniciando banco de dados postgres com o Docker

Primeiramente baixar a imagem necessária para construit o conteiner:
sudo docker pull postgres:14.2-alpine
**A flag alpine deve ser utilizada somente em ambientes de desenvolvimento/testes, nunca em produção!**
--name: Define o nome do seu contêiner
-p: Mapeia a porta para acesso ao seu banco de dados postgres <host>:<container>.
-e: Define uma variável de ambiente.
-d: Após a criação, o contêiner é executado em segundo plano, deixando o terminal livre.


Exemplo:
sudo docker run --name conteiner-postgres -p 5432:5432 -e POSTGRES_PASSWORD=password -d postgres:14.2-alpine

Para a criação, é necessário o uso do comando exec com duas flags:
-i: Mantém o terminal "linkado" com o processo ativo.
-t: Inicia o processo com o TTY (terminal padrão do linux).

exemplo: 
sudo docker exec -it <ID-ou-NAME> bash

Entrar no postgres com o comnado:
psql -U postgres

## Docker 06 - Construindo imagens com o Dockerfile

# FROM define nossa imagem base para a construção da nova imagem.
FROM node:16

# O RUN executa comandos do terminal
# Aqui vamos atualizar os pacotes do ubuntu
RUN apt-get update

# O ENV define variáveis de ambiente
# Aqui estamos definindo a variável PORT que esta sendo usada para escolher a porta na aplicação express
ENV PORT=3000

# EXPOSE determina qual porta do contêiner será visível para o host.
EXPOSE 3000

# WORKDIR define a pasta raiz da sua aplicação
WORKDIR /app

# COPY copia os arquivos package.json e yarnlock para a pasta raiz do contêiner.
COPY [ "package.json", "yarn.lock" ] .

# Nesse casso vamos executar o yarn para restaurar as dependências.
RUN yarn

# Aqui estamos copiando todos os arquivos da pasta onde atual
# e mandando para a pasta raiz no contêiner.
COPY . .

# User define o usuario do ubuntu.
USER node

# CMD é o comando usado para iniciar a aplicação.
CMD [ "yarn", "start" ]


Esses comando vão no DockerFile
Usamos o sudo docker build -t hello_world_express_node  ., para criarr a imagem.
Toda vez que alterarmos o projeto temos que dar o build denovo

Para finalizar usamos o docker run, com as flags, --name, -p, -d
