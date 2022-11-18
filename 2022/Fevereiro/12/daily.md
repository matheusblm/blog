## Porque utilizar bancos relacionados

Legibilidade, Performance, repeticao de dados, manuntencao

## Diagrama Entidade Relacionamento (DER)

Entidades sao a representacao das tabelas do banco
Atribnutos sao caracteristicas de uma entidade, represetam as colunas relevantes.
Relacionamentos descreve como as entidades se conectam.

### Relacionamento 1:1

Define que um item so pode ser relacionar com um itemde outra bela.

foreign key: É uma chave estrangeira que está dentro da tabela, que vai referenciar a primary key (chave primária) de outra tabela, no nosso caso essa chave é a usuario_id que está referenciando a primary key (chave primária) id da tabela usuarios;
references: De onde a sua chave estrangeira está sendo referenciada, nesse caso ela é do campo o id da tabela usuarios.

## Inner Join

para juntar duas ou mais tabelas por sua determinada relação, onde cada linha da tabela endereco corresponde o mesmo valor que possui na tabela pessoa
Poderíamos utilizar apenas JOIN, mas por fins didáticos deixamos explícito a query com o INNER, já que pode ser encontrado em alguns códigos ou materiais didáticos.

## Left Join

Caso algum dos dados da tabela nao tenha o item do inner joint utilizamos o left join.

## Rigth Join

Ao contrário do LEFT JOIN com o RIGHT JOIN obtemos todos os dados do lado direito (endereco) mesmo que não tenha correspondência com a outra tabela que se relaciona.

## Full outer Join

Já com o FULL OUTER JOIN podemos obter todas as informações registradas, mesmo que algumas delas não sejam correspondentes.
