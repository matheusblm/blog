## Demo

Iniciar um projeto nodejs

yarn init -y

install express

yarn add express
criar .gitignore

- No node nao usamos o import e sim o required

Exemplo de app basico:

const express = require("express")
const app = express()
const PORT = 3000

_REQ=request do user_
_RES=response da rota_

app.get("/api", (req, res) => {
res.send("Rota get")
})

app.lister(PORT, ()=> console.log("App is running on port ${PORT}"))

**Para deixar como o import ser padrao e so mudar no package.json, adicionar o type: module.**

Adicionar o nodemon, para que ele atualize em tempo real nosso codigo no servidor.
Para rodar e so dar um yar nodemon "arquivo"

Para rodar automatico, tem que adicionar ao package.json na parte dos scripts, dev: nodemon index.js.

**Usar underscore em parametros que nao estao sendo usado.**

## Configurar o eslint e o prettier ao projeto.

yarn add -D eslint prettier eslint-config-prettier eslint-plugin-prettier

yarn run eslint --init

code . prettierrc.json > adicionar "singleQuote": true, "tabWidth": 2

code .eslintignore > adicionar o /node_modules

## Continuando com o codigo

yarn run dev para rodar

para forcar o tipo do header retornado, para ser sempre como json, utilizar o:
app.use(express.json()) > so adicionar res.json dai.

Para pegar o body da requisicao > req.body
Utilizar a descontrucao > cosnt {parametros} = req.body
res.tatus(200).json(RESPOSTA)
res.tatus(200).header().json(RESPOSTA)
