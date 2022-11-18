## NodeJS Introdução ao Typescript

Typescript adicionado tipagem ao código.

Beneficios dele :

Tornar explícitos os tipos de atributos, objetos ou parâmetros de uma função, o que aumenta a legibilidade e manutenibilidade do código.
Auxiliar na identificação de bugs com mensagens de erro mais compreensíveis. Também é capaz de apontar trechos passíveis a apresentar problemas.
Diminuir a ocorrência de erros em tempo de execução e em ambientes de produção.

instalação atraves do 
yarn add -D typescript
yarn add -D ts-node

**Configuração**

 npx tsc --init

 ## NodeJS 17

 Definindo tipos:
 Usando a interferencia
 Quando apenas utlizamos:
 let myStr = "STR"

ele interfere e ve que o tipo é uma string.

**Forma explicita**

Para declararmos de forma explicita utilizamos:

let myStr: string = "str"
let myArray: Array ou string[]

## NodeJS 18 - Funções e o tipo Any

Declaramos o tipo de parametro e de retorno da função.

Exemplo:

const myFunction = (name: string, age: number): string => {
  return `Nome: ${name} - Idade: ${age}`;
}; 

**Definir parametros opcionais**

Utilizamos o  ?

## Node 19 - Union Types

Serve para tipagens mais complexas.

A onion utiliza o |

Exemplo number | string

Como não temos um tipo exato, temos que fazer a verificação do tipo antes de usar algo.

**Usando Union para Restringir Valores**

ex: status: "Processing" | "Shipped" | "In Transit" | "Delivered"