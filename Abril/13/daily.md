Como começar um projeto

yarn init -y
yarn add typeorm@0.2.45 reflect-metadata express
yarn add @types/express @types/node ts-node-dev -D
yarn typeorm init --database postgres

criar uma pasta db, colocar o ormconfig dentro dele.

Orm config transformar em um const devConfig, e o colocar como as ConnectionOptions
no tsconfig adicionar esModuleInterop como true.

Adicionar no scripts

"start": "ts-node-dev --files src/index.ts"
"typeorm": "node --requeire ts-node/register ./node_modules/typeorm/cli.js -f src/db/ormconfig.ts"

.touch .env
adicionar as chaves que você ira usar

yarn add dotenv
import dotenv
dotenv.config()

criar app.ts
cirar server.ts

depois de confiurar app e server iniciarlizar o docker
docker run --name configInicial --env-file ./env -p 5432:5432 -d postgres
docker start configInicial

yarn typeorm migration:create -n initialCommit
yarn typeorm migration:generate

para criação do primeiro usuario admin tem que ser feito na mão
exemplo:
adicionar ao primeiro migrations.
`INSERT INTO "users" ("name", "email", "password", "isAdmin") VALUES (name,email,passowrd hashSync(password,10), true)
yarn add bcrypt && @types/brcypt -D

Criação de entitdade

yarn typeorm entity:create -n Product
