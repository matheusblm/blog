## Organização das pastas nodejs

Temos o src onde fica tudo.
>
config:
database.js > fica as configurações do database
jest.config.js > fica as configurações dos testes
>
controllers:
Pode exister mais pastas dentro com , para separa melhores os controllers de cada rota
>
middlewares:
Ficam os middlewares.
>
models:
Models de cada route.
>
routes:
NOME.routes.js
index.js > importando cada rota para ca.
>
service:
a logica de cada controller.
>
shapes:
Aqui fica o schema do yup de cada item.
>
test:
>
utils:
>

app.js > import da routes e usar o routes(app)
server.js > aqui inicia o server com a importtação do app.

----
## NodeJS teste com JEST

fazemos a instalação normal do jest:
yarn add jest -D
yarn jest --init > fazer as configurações inicias padrões.
Para fazer o jest passar mesmo que não tenha nenhum teste, tem que adcionar a flag:
yarn test --passWithNoTests

**Configurando o package.json**

  "scripts": {
    "test": "NODE_OPTIONS=--experimental-vm-modules jest"
  }
  
  para rodarmos os teste, usamos o yarn test.
  
  ### Testando Requests
  
  Temos que adicionar o supertest:
  yarn add supertest -D
  
  




