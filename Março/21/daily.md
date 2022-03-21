## Node 07 Biblioteca Yup para validações

Yup é um construtor de esquema para validação de dados.

Yup deixa mais fácil fazer as validações, sem a necessidade de ficarmos nos preocupando tanto.

Para instalar usa:

yarn add yup

import \* as yup from "yup";

### Exemplo de esquema com o Yup

const addressSchema = yup.object().shape({
email: yup.string().email().required(),
fullName: yup.string().required(),
houseNumber: yup.number().required().positive().integer(),
address: yup.string().required(),
postCode: yup.string().required(),
state: yup.string().matches(/^[A-Z]{2}$/).required(),
city: yup.string().required()
});

**Também existe a possibilidade de fazer um esquema condicional: **

yup.string().required(),
address_2: yup.string()
.when("city", {
is: "Curitiba",
then: yup.string().required(),
}),
});

.when fará essa condição.

**Podemos usar o default**

yup.date().default(() => { new Date() }),

## Fazendo validações no Node

app.post("/address", async (req,res)=>{
const data = req.body
addressSchema.validate(data)
}).then((value)=> res.json((value)).catch((err)=> res.json(err)))})

### Node 08 Validações no Express

As validações com yup também servem para que possamos verificar os dados que o usuário esta forncendo.

**Exemplo:**

const item = {
name: "Coxinha",
description: "Salgado de frango empanado e frito",
price: 5.99,
}

name: string().required()
description: string()
price: number()

app.post("/create/:id", (req, res) => {
return res.json({
body: req.body
id: req.params.id
})
})

**Criando o esquema**

import \* as yup from 'yup'

const itemSchema = yup.obkect().shape({
name: yup.string().required(),
description: yup.string(),
price: yup.number().positive().required()
})

_Para fazer a validação do tipo devemos utilizar o .strict() junto do .string() ou .number(), caso contrário ele irá apenas transformar o tipo da variável_

**Criação do middleware**

const validate = (schema) => async (req,res,next) => {
const resource = req.body
try{
await
schema.validate(resource)
next()
}catch(e){
res.status(400).json({error: e.errors.join(", ")})
}
}

**Adiconando o esquema e o middleware a rota**

app.post("/create", validate(itemSchema), (req, res) => {
const {body: item} = req
return res.json(item)
})

### Node 09 - Autenticação e Autorização

- Autenticação é o processo de validação dos dados que o usuário forneceu estão corretos.

- Autorização processo que permite o usuário autenticado a ter acesso a um certo tipo de contéudo.

**Biblioteca jsonwebtoken**

Biblioteca mais popular para trabalharmos com JWT é a jsonwebtoken

yarn add jsonwebtoken > Criar um objeto com as configurações para os tokens JWT. Adicionar ao app.js > const config = {
secret: "my_random_secret_key", expiersIn: 600
}

\*ExpiresIn é um valor numérico, caso seja fornecido uma string, deve ser adicionado com a unidade de tempo. Ex: 2 days, 10h, 7d.

O Campo secrete deve vir preferencialmente da váriaves de ambiente.\*

Maneira mais usual de fazer a verificação se o usuário está logado é com o middleware

### Node 10 - Hash de senhas com Bcrypt

- Hash é um processo de criptográfia, que usualmente é utilizado para validar autenticidade.

- O processo de hash é seguro, pois ele é um processo unidirecional.

**BCrypt**

- Guarda as senhas em formato de textp, porém de uma maneira segura.

- Sua maior vantagem é a utilização de salt(sais criptográficos)

- O salt acrescenta aleatoriamente sequências de caracteres a senha.

_Instalação:
yarn add bcrypt jsonwebtoken _

Para utilizar no arquivo:

import bcrypt from 'bcrypt';
import jsonwebtoken from 'jsonwebtoken';

Exemplo no arquivo: autenticação.js

### Utilizando Variáveis de ambiente

Para adicionar utiliza yarn add dotenv

exemplo de arquivo env, esta no arquivo . env

**Configuração e uso**

import dotenv from 'dotenv'

dotenv.config()

const host = process.env.DB_HOST;
const username = process.env.DB_USER;
const password = process.env.DB_PASS;
const jwtSecret = process.env.JWT_SECRET;
