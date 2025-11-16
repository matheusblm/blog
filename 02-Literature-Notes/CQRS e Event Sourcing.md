

É um crud, porem o read fica separado.
### Command

### Query

### Responsibility

### Segregation


Get() - Jamais faz uma alteração = Comando
Set() - Retorna nada e faz uma alteração = Query


Cliente -> command / querry -> handler -> model -> db = normal

Evente sourcing - Nao perder os eventos = Auditabilidade
Write heade logs - nao faz persistencias dos logs, ele grava apenas um "txt" para fazer isso

Exemplo saldo do banco - tem todo o historico das transações
Conjuntos dos eventos tomados para chegar em X

Eventos imutaveis

## Referência
https://www.youtube.com/watch?v=0B20k31Gyq0&list=WL&index=10&t=1239s




[[Arquitetura]]
