Ententendo o relacionamento 1:1 em SQLAlchemy
Considere a seguinte linha de código, referente a criação da coluna de chave estrangeira:

estado_id = db.Column(db.Integer, db.ForeignKey("estados.id"), nullable=False, unique=True)

"estados.id": Faz referência a um atributo específico (id) da nossa EstadoModel, a partir do __tablename__ dela (estados). Dessa forma, estamos dizendo que o atributo estado_id da tabela capitais referencia o atributo id da tabela estados, da mesma forma com que fazíamos com SQL puro.
unique=True: Esse é o diferencial entre um relacionamento 1:1 e 1:N. Indicando que estado_id deve ser unicamente associada a um estado.id, conseguimos dizer com certeza que uma capital somente terá um estado associado a ela, e vice-versa.


Entendendo o relacionamento 1:N em SQLAlchemy
Como esta é uma relação 1:N, a chave estrangeira ficará do lado N da relação (estados). Considere a seguinte linha de código, referente a criação da coluna de chave estrangeira:

regiao_id = db.Column(db.Integer, db.ForeignKey('regioes.id'))

"regioes.id": Faz referência a um atributo específico (id) da nossa RegiaoModel, a partir do __tablename__ dela (regioes). Dessa forma, estamos dizendo que o atributo regiao_id da tabela estados, referencia o atributo id da tabela regioes, da mesma forma com que faziamos com SQL puro.


Relacionamento N:N é necessario uma tabela pivo para controlar o relacionamento entre elas

secondary: Em relacionamentos N:N, existe um argumento adicional que temos que passar para o relationship do SQLAlchemy fazer as relações corretamente. Esse argumento recebe a tabela intermediária da relação.


BackPopulates e Backref - 

Backpopulates - via de mao dupla
Backref - voce declara em apenas uma, e ele é mais maleavel aceita uma função backref() que te da mais liberdade

Decorator Validates
Utlizado para validar os campos.

set_trace() do interpretador de códigos ipdb para debugar, set trace seria um brekpoint.
