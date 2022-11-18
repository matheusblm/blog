## MicroServiços

Seria uma quebra de tarefas, quebrando o sistema em vários pedaços

### Escalabilidade horizontal

quanto mais requisições, maior tem que ser a capacidade computacional da aplicação

### Api Gateway

Gatewat seria uma camda final na frente de todos os serviços que redicionam as requisiçõse para orespectivo serviço
exemplo - 
api.exemplo.com/users -> aplicação em flask rodando na AWS.
api.exemplo.com/products -> aplicação em node rodando em servidor local.
api.exemplo.com/orders -> serviço rodando no Heroku sob demanda.

### Load Balancer

Serve como um orquetrador que envia as requisições para vários serviços iguais de forma a não sobrecarregar nenhum deles.

*Cada microsserviço é uma aplição separada, e deve poder rodar em qualquer lugar sem depender dos demais serviços.

* O banco de dados é individual para cada microsserviço4

### Vantagens de microsserviços

Separação de serviços bem definada, assim existe menos conflito.

### Desvantagem de microsserviço

Maior complexidade, dificil de gerenciar e trafego de rede muito grande
