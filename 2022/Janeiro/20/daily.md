## MongoDB

CRUD = create read update delete

O mongoDb fornece os metodos para inserir doc em uma colecao:
###Create
db.collection.insertOne()
db.collection.insertMany()

Caso a colection nao exista ele vai crira uma e e gerado um ID

###Read

db.collection.find()
cursor.pretty()
cursor.limit(number)
cursor.sort()

###UPDATE

db.collection.updateOne()
db.collection.updateMany()

db.users.updateMany({idade: 25}, {$set: {nome: "João da Silva"}})

###delete

db.collection.deleteOne()
db.collection.deleteMany()

###query no mongo

db.nome_collection.find({chave: valor})

Para pegar todos os dados menos um :
db.nome_collection.find({chave: {$ne: valor}})

Para pegar um dado maior:
db.nome_collection.find({chave: {$gt: valor}})
para pegar um dado maior ou igual tem que adiiconar um e ao gt.
para pegar um dado menor:
db.nome_collection.find({chave: {$lt: valor}}),

dados que NAO sejam algo
db.nome_collection.find({chave: {$not: {$gt: valor}}})

busca de dados que possuam uma chave especifica:

db.nome_collection.find({chave: {$exists: boolean}})

verificar os dados que possuam algum dos dados passados:
db.nome_collection.find({chave: {$in: [valor1, valor2, ...]}})

###AND e OR

and basta voce passar uma virgula apos o primeiro parametro
or voce adiciona o $or antes e adiciona os parametros dentro de um array: 
db.usuarios.find({$or:[{idade: 23}, {idade: 15}]})
