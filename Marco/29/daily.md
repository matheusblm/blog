## TypeORM 01 - Configuração Inicial

ORM (Object–relational mapping) é uma técnica que permite consultar e manipular dados de um banco de dados usando um paradigma orientado a objetos.

Para adicionar o typeorm utilizamos o 
yarn add typeorm@0.2.45 reflect-metadata 
ao inves do yarn init -y

Adicionando os types:
yarn add -D @types/node

Para configurações inicias:
yarn typeorm init --database postgr

Com o comando inicializador do TypeORM, a biblioteca "reflect-metadata" 
é importada automaticamente no index.ts. Sua importação
deve sempre deve ficar em um local global da sua aplicação.

**Modificando estrutura padrão do projeto**

Renomearemos a pasta "entity" para "entities".
Renomearemos a pasta "migration" para "migrations.
Corrigiremos as importações que agora mudaram, pois as pastas foram renomeadas.
Renomearemos o arquivo ormconfig.json para ormconfig.ts e faremos mais algumas alterações
export default no ormconfig
