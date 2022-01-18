##Typescript

E um superset do JS, basicamente uma tipagem estatica.
---
+Evita resultados inesperados
+Avisa se estiver fazendo algo errado
+Deixa a IDE mais interativa.
- Necessita ser compilado 
- Aprendizado inicial dos tipos 
- Erros nem semore muito claros.


tsconfig init - para dar inicio no typescript.

----
Tipos aceitado
Boolean, string, number, array, Tuple, Any, void, never, object.

----

Type Inference
DRY

Type Aliance 
Cria tipos mais complexos, com mais informarcoes.
O ponto de interrocacao deixa a tipage opicional.

----
Type Aliance x Interface


Generics

ReadOnly
Pick 
Omit

Decorators

Para funcionar tem que editar o ts config. 
Inicia com o arroba, e um timpo espcial de declaracao que pode ser anexada a uma classe, metodo ou parametro.E uma funcao que recebe alguns parametros especificos.

exemplo

function log(prefix sting){
    return(target) console.log(target)
} 

log("awesome")