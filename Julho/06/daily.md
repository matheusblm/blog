### HOC REACT

high order components sever para abstrir logicas repetidas.
Por exemplo, dois componentes que fazem uma mesma requisição, pode existir
um HOC que faça essa requisição para os dois.

Exemplo:

export funciotn withRepoData(WrappedComponent, username){
data = requisição
return (
<WrappedComponent repoData={ESTADO COM INFO} {...props}/>
)
}

### Error boundaries

If a component trohw a error this is gonna security the error doesnt break your application
