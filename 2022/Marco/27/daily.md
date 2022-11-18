## Diferença entre type e interfa

Interface - Podem ser mergiadas, 

Types - São unicos, mas podemos alterar o tipo de algo declarado anteriormente  por outro type, aceita usar o tipo direto.



Note que apenas o type pode ser utilizado para definir um tipo a partir de uma união. Interface deve ser utilizada exclusivamente para objetos.

interface Bear extends Animal {
  honey: boolean
}

type Bear = Animal & { 
  honey: boolean 
}