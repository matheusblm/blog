## Banco Relacionais

Banco de dados = lugar para guardar info, para persistir de forma estavel.

Dados são importantes pois os softwares são desenhados aos redor dele para gerir as informções
que ele trás.

Sistemas de gerenciamento de bancos de dados - SGBD 
Além de ser aquele que garante a manipulção dos dados do ban da co.
Ele é responsavel por outros aspectos da camada de persistencia, como:
COnsistencia dos dados
Gerenciar quando dois ou mais servidores pretendem modificiar o mesmo dado
Fornece uma linguagem para interção simplicando a manipulçao dos dados
Implementar algoritmos avançados de buscas.

Banco de dados relacionais, constroem o banco utilizando tabelas com linhas e colunas,
tipos de dados e estratégias de relacionamento entre as tabelas.

#### Tabela

Representam as informações

Colunas:
São utilizadas para definir características dos dados.

Linhas:
AS Linhas de uma tabela são os dados que guardamos, respeitando as regras definidas
para cada uma das colunas.

### Tipos de dados
Null
Integer
Real = float
Text
Blobl: binary large object
https://medium.com/@sravankonkumutti/database-database-is-an-organized-collection-of-interrelated-data-stored-in-a-computer-237bec9671bf


### PostgreSQL
Para iniciar o banco de dados sudo -u NOMEdoBANCO psql

Comandos de localização 
\conninfo
\du
\l
exite
CREATEROLE

Para crar seu usario deve usar a aspa simples na hora de encapsular a senha.
O comando tem que termianr com ;

Para criar um DB
CREATE DATABASE nome_do_seu_usuario;

Comando de localização II
\c
https://www.postgresql.org/download/linux/ubuntu/
https://www.postgresql.org/docs/8.0/sql-createuser.html
