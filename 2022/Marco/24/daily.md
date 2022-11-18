## Node 12 Routers

Metodo do express - Para isolar as rotas em outro arquivo.

**Utilizando o Router**

EXEMPLO 1 

Ele e bom de utilizar para separa os arquivos, fazer um micro gerenciamento.
Exemplo:

EXEMPLO 2
EXEMPLO 3

**Utilizando Router com controllers**
Exemplo 4
---

## Estrtura de um projeto com Express

Principio MVC.

1. Separar o servirdor do restante da aplicacao:
Alterar no json, o dev nodemon e adicionar a seguinte opcao:
 --experimental-specifier-resolution=node
 2. Todas as rotas separadas.
 3. Shapes pasta separada
 4. Middlewares pasta separadas.
 5. Controllers pasta separadas.
 6. Toda ves que tiver alguma logica, adicioanr ela ao service e ao controoler deixxar apenas o try catch, caso necessario.
 7. Ter as pasta de models

**Sempre importar os arquivos para o index da pasta e depois exportar ele**

Exemplo 5