## MiddleWare

Sistema que intermedia a comunicacao entre dois sistemas
Tambem pode ser funcoes que interdemdiam a execucao de outras funcoes dentro de uma mesma aplicacao.

## Padrão Chain of Responsability ou Padrão Middleware

O express e baseasdo nesse padrao.

Desaclopar funcoes para que elas possam ser reutilizadas melhor.

## Middleware na prática com JS

cosnt logRequestInConsole = (req, res, next) => {
console.log(req.method)
return next()
}

Ele fara o console logg do metodo do request, e o parametro next seria a proxima funcao a ser executada.

## Inserindo o Middleware para todas as rotas

app.use(logRequestInConsole);

executado o middleware para todas as rotas que forem declaradas depois dele.

## Inserindo um ou mais Middlewares em uma rota específica

exemplo:

app.get("/data", logRequestInConsole, (req, res) => {
res.json({message: "Hello World!"})
})

o middleware e declarado apos a stringg da rota.

# Identificadores únicos com UUID

UUID significa identificador unico universal. Basicamente e um numero de 16bytes gerado aleatorio de uma maneira padronizada. E representado como 32 digitos hexadecimais.

ex: uuid: "7bedf6a0-e6cd-11e8-8fee-3160de9dc99f"

Instalando:
yarn add uuid
Imports:
import {
v1 as uuidv1,
v4 as uuidv4,
v5 as uuidv5
} from "uuid";

A versão 1 é gerada a partir de um timestamp
e um node ID, que geralmente é o endereço MAC
do computador

uuidv1(); ⇨ "2c5ea4c0-4067-11e9-8bad-9b1deb4d3b7d"

A versão 4 é gerada a partir de números aleatórios
uuidv4(); ⇨ "1b9d6bcd-bbfd-4b2d-9b5d-ab8dfbbd4bed"

A versão 5 é gerada a partir de um hash SHA1
de um namespace dado

const MY_NAMESPACE ="630eb68f-e0fa-5ecc-887a-7c7a62614681"
