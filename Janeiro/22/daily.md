## RestFull API

E uma api que tem todas as 6 restricoes do conceito rest

1 - Uniform Interface

Ter um padrao para as interfaces.
Um dado so pode ser acessado por uma rota especifica.

2 - Client-Server

Front e back independentes.

3 - Stateless

Cada solicitacao e independente.

4 - Cacheable

Deve ser aplicado a tecnica de cache apenas nas partes necessarias.

5 - Sistema de camadas

Sistema de camada para autentificacao sem que o usuario perceba.

6 - Code ondemanda

## Design Patterns

Tem a intencao de resolver problemas que sao bastatne comuns independete da linguagem.
Elementos padroes:
-Intencao
-Motivacao
-Estrutura
-Exemplo de codigo

O uso do padrao deve ajudar a resolver o problema e NAO ser um teamplate.

## Padrao MVC

Model View Controller

Model - A camada que manipula e representa os dados
View - representa a interface que sera apresentada, definicao de rotas por exemplo.
Controller - intrega as outras duas camadas, com as funcoes auxiliares.

- Legibilidade
- Escalabilidade
- Manuntencao

## Flask Factory Pattern

Tratase de uma funcao especifica para aplicao denominada create_app

Exemplo

from flask import Flask

def create_app(): # Instanciando o Flask
app = Flask(**name**)

    # Contexto de configuração
    app.config["JSON_SORT_KEYS"] = False

    # Camada de rotas
    @app.get("/")
    def rota_1():
        return "Seja bem vindo ao Flask Factory Pattern"

    @app.get("/message")
    def rota_2():
        return "Seja bem vindo, novamente, ao Flask Factory Pattern"

    # Por último SEMPRE retornamos a variável app
    return app

#### Desacoplagem

app/**init**.py

from flask import Flask

# Importando as rotas

from app import routes

def create_app():
app = Flask(**name**)

    app.config["JSON_SORT_KEYS"] = False

    # Camada de Views desacoplada
    routes.init_app(app)

    return app

app/routes/**init**.py

# Importando o Flask para Type Hint

from flask import Flask

# Criando a função init_app

def init_app(app: Flask):

    # Importanto a função home_route() e passando o app por parâmetro
    from app.routes.home_route import home_route
    home_route(app)

app/routes/home_route.py

# O Flask está sendo importado apenas para Type Hint

from flask import Flask

def home_route(app: Flask):

    # Rota 1
    @app.get("/")
    def rota_1():
        return "Seja bem vindo ao Flask Factory Pattern"

    # Rota 2
    @app.get("/message")
    def rota_2():
        return "Seja bem vindo, novamente, ao Flask Factory Pattern"

## Controllers

Funcoes que contem a logica das rotas.
