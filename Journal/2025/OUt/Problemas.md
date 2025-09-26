** Problemas Gerais **

Loading dentro da tabela

Indicar que a tabela não tem registro (pois não sei quando o loading terminou ou não)

Muito espaço em branco não usado

Adicionar tooltip nos botões com ícones (hover ao passar mostrar o nome daquele botão)

Ícones de ação com o olho não remetem a ver detalhes

Ícone de exportar em Excel não remete a exportar, acaba tendo um X no meio. (Muitas vezes o X indica algo relacionado à exclusão)

Tamanho das fontes pequeno demais, em monitores grandes fica quase ilegível

Ao aplicar filtros e ordenações nas tabelas voltar para a página inicial

Precisa ter alguma maneira de remover a ordenação de uma coluna

Adicionar a possibilidade do usuário escolher o número de itens por página e salvar no local storage essa informação para ser comum a todas as tabelas

Caso as fontes fiquem no mesmo tamanho, aumentar o número de itens para 20 como base, pois hoje tem muito espaço em branco na tela

Alterar o placeholder dos filtros abaixo do nome das colunas para não ficar algo repetitivo

O scroll deve ficar dentro do conteúdo das tabelas, não fora no bloco inteiro

Ao clicar em abrir o modal de detalhes ele aparece um modal bem pequeno primeiro e depois o modal grande, o interessante é abrir o modal e daí fazer a requisição e mostrar um loading com skeleton

Ao clicar em abrir o modal ele faz todos os requests de uma vez, seria interessante ele fazer o request da aba apenas quando entrar nela e adicionar um skeleton loading nos campos

Edição nas linhas da tabela acaba ficando muito confusa e o campo pequeno não é o ideal para escrever as observações, seria interessante fazer essa alteração no modal

Precisa ter um padrão de botões de ações nas tabelas: ou eles terem textos ou ícones

Filtros de select com opções padrões

Filtros de data deixar colocar apenas 8 digitios ou 6 digitos e deixar na formatação do tabela

** Ajustes Tela Consultar Notas **

Adicionar trava no filtro de input ao alterar a data de inicio para alguma data, alterar automatico a data final para uma da data limite (no caso d+30)

Adicionar tags com cores para a coluna de Situação (Trânsito - Amarela, Entregue - Verde, etc)

Coluna de Analista aparece para os clientes? (Caso sim, é necessário?)

Juntar as colunas de destino e UF destino (PATO BRANCO - PR, adicionar validação no filtro: quando uma busca for por duas letras buscar apenas estados, quando for mais letras buscar pela cidade)

Podemos juntar a Coluna de Situação com a de Último Tracking (adicionar um ícone: ao passar o mouse ver o último tracking ou é necessário filtrar essas informações?)

Adicionar arredondamento nas bordas da tabela

Número total ficar ao lado do título (Consultar Notas - (1520 itens))

Filtros ficarem abaixo do título, para não ficar tudo na mesma linha

Adicionar labels nos filtros que estão ao lado do título, acaba ficando confuso saber qual coluna está sendo filtrada

** Modal Tela Consultar Notas **

Aba de Nota: Alterar o título da aba para "Detalhes". Informações muito longe dos labels causam confusão. Alterar para label acima da informação ou mais próximo, colocar as informações em ordem de importância (número da NF e série). Não precisa repetir o título embaixo. Caso não tenha nenhuma informação não mostrar o label

Aba de CTE / Documentos: informações muito longe dos labels. Faria sentido juntar com a aba de Nota Fiscal, pois acaba ficando muito espaço em branco em ambas

Aba de Histórico: título repetitivo. Itens que são repetitivos e não mudam em cada linha (Remetente, Nota, Série, Destinatário) devem ficar acima da tabela para não ficarem repetitivos. Faz sentido os filtros dentro dessas tabelas?

Particularidades Entrega: o título da tabela é uma coisa e o título da aba é outra, acaba ficando confuso. Faz sentido ser uma tabela? Em alguns casos pode existir muitos registros. Talvez alterar para uma visibilidade em blocos

** Tela Notas em Trânsito **

Filtros com a cor cinza (da paleta de cores) dão a sensação de estarem desabilitados. Seria interessante usar a cor primária. Também seria interessante estarem abaixo do título de maneira mais organizada. O "todas" em primeiro já selecionado, etc

Colunas da tabela:

"Status Apoio" → Alterar para texto com tag dos Status. Motivo: os ícones não trazem tanta clareza do que se trata. Outra opção é adicionar o tooltip aqui também

"Nota Fiscal" → Juntar com Série NF

"Série NF" → Juntar com Nota Fiscal

"Tomador" → ok

"Transportador" → ok

"Data Expedição" → ok

"Previsão Entrega" → ok

"Data Agenda" → ok

"Reagendamento" → ok

"Observação Ocorrência Tracking" → Se a observação for campo livre não faz muito sentido ter o filtro

"Código Tracking" → ok

"Cliente Destino" → ok

"Destino" → Juntar com UF Destino

"UF Destino" → Juntar com Destino

"Analista" → Faz sentido mostrar essa informação?

"Analista Transp" → Faz sentido mostrar essa informação?

"Operação" → Faz sentido mostrar essa informação?

"CNPJ Destino" → ok

"Apoio" → Não faz sentido, pois traz a mesma informação de Status Apoio

"Observação Apoio" → Talvez faça sentido juntar com a coluna Apoio ou Status Apoio e mostrar a informação ao passar o mouse

"Ocorrência Agendamento" → Talvez faça sentido juntar com a coluna Observação Agendamento e mostrar a informação ao passar o mouse

"Observação Agendamento" → Talvez faça sentido juntar com a coluna Observação Agendamento e mostrar a informação ao passar o mouse

"Agendamento Acatado" → Faz sentido mostrar essa informação? Talvez mostrar apenas dentro dos detalhes

"Agendamento Acatado Data" → Faz sentido mostrar essa informação? Talvez mostrar apenas dentro dos detalhes

"Agendamento Acatado Email" → Faz sentido mostrar essa informação? Talvez mostrar apenas dentro dos detalhes

"Placa Carreta" → ok

"Ocorrência Incidente" → Talvez faça mais sentido juntar com Observação Incidente

"Observação Incidente" → Talvez faça mais sentido juntar com Ocorrência Incidente

"Container" → ok

"Origem Atualiz" → Faz sentido mostrar essa informação?

"Sistema Origem" → Não faz sentido mostrar se atualmente todas as informações vêm apenas de um lugar

Alterar a ordem e deixar as informações mais relevantes em primeiro, e as observações por último

Botões de "em lote" e agendamento ficarem desabilitados ao não ter nada selecionado e, ao passar o mouse em cima, ter um tooltip falando para selecionar

Não faz sentido Status Apoio ficar grudado à esquerda da tela

** Modal Detalhes **

Fazer os mesmos ajustes do Modal Tela Consultar Notas

Deixar o background da trilha inteira da mesma cor da imagem da timeline de entrega

Alterar o lançamento de tracking

Aba de Histórico - faz sentido ser uma tabela? Vão existir muitos registros?

** Modal Lançamento de Agendamento **

Não é necessário um modal tão grande

As informações do primeiro passo não precisam ficar em uma tabela quando for apenas um registro. Quando for mais de um, não precisa ter tantas informações

Alterar a ordem dos inputs para: Tracking > Data de Agendamento > Hora de Agendamento

Colocar o input de observação maior e abaixo dos outros

Colocar o botão de próximo no lado direito do modal no footer

Ter um botão de voltar

Salvar as informações apenas após a finalização

** Notas Retidas **

Total de NF → Ficar abaixo do título ao invés de na mesma linha e dar um destaque maior

Cubagem, Peso Bruto e Peso Calculado repete a informação, porém com dados diferentes. Colocar a unidade de medida

** Abrir Incidente **

Adicionar botão para voltar

Ações só serem concluídas no final do processo

Muito espaço em branco entre as informações

Informações que não podem ser editadas devem ser mostradas de outra maneira, atualmente dá a sensação de ser um input editável

Alterar a ordem dos campos de submotivo, motivo, etc

Alterar a lista de e-mail para ser uma tabela (ou outro tipo de listagem), listar todos os e-mails daquele remetente filtrado e, na tabela, adicionar duas colunas checkbox: uma para adicionar no envio e uma para adicionar como cópia

** Perguntas Clientes **

O que eles acham do tamanho das fontes?

Edição na linha da tabela não confunde vocês?

Quais colunas vocês não usam?

Sentem falta de alguma informação?

Vocês sentem dificuldade em identificar rapidamente as informações mais importantes nas tabelas?

Os filtros atuais ajudam vocês a encontrar o que precisam ou falta alguma forma de busca/filtro?

O uso de ícones sem texto é claro ou seria melhor ter ícones acompanhados de rótulos?

Vocês costumam usar a edição diretamente na tabela ou preferem abrir em modal/detalhes?

Há campos ou colunas que vocês nunca usam e poderiam ser removidos para simplificar a tela?

Existe alguma informação que hoje não aparece no sistema, mas seria importante ter?

Gostariam de configurar a ordem ou visibilidade das colunas de acordo com a preferência de cada usuário?

A quantidade de registros exibidos por página atende ou seria útil ter mais/menos opções?

É fácil entender quando um dado ainda está carregando (loading) ou ficou confuso em algum momento?

Os modais atuais são claros ou preferem que determinadas informações abram em uma tela própria?

Quando consultam os detalhes, o que é mais importante aparecer primeiro?

Vocês preferem uma interface mais compacta (com muitas informações na mesma tela) ou mais espaçosa e organizada em blocos?

Se pudessem priorizar uma melhoria, qual seria a mais urgente?









"Ações"
1
: 
"Status Apoio"
2
: 
"Nota Fiscal"
3
: 
"Serie NF"
4
: 
"Valor NF"
5
: 
"Tomador"
6
: 
"Vip"
7
: 



"Transportador"
8
: 
"Cliente Destino"
20
: 
"Destino"
21
: 
"UF Destino"
22
"CNPJ Destino"
26
: 


"Observação Ocorrência Tracking"
13
: 
"Código Tracking"
14
: 

"Data Expedição"
9
: 
"Previsão Entrega"
10
: 
"Data Agenda"
11
: 
"Reagendamento"
12
: 
: 
"Analista"
23
: 
"Analista Transp"
24
: 
"Operação"
25
: 



"Idade Overdue"
15
: 
"Risco Atraso Etapas"
16
: 

"Data Última Atualiz."
17
: 
"Último Status API"
18
: 

"Ocorrência Agendamento"
29
: 
"Observação Agendamento"
30
: 
"Agendamento Acatado Email"
35
: 

"Agenda Cross"
33
: 
"Horas Para Agenda"
34
: 

"Placa Carreta"
36


: 
"Ocorrência Incidente"
37
: 
"Observação Incidente"
38
: 
"Container"
39
: 
"Origem Atualiz"
40
: 
"Sistema Origem"




"Lançar Status" - na verdade é uma ação
"Apoio"- Removido
"Observação Apoio" - Removido, colocado junto com o status
"Agendamento Acatado" - Repetitivo, pois se existir esse tipo a Coluna Agendamento Acatado Data vai estar preenchida
"Agendamento Acatado Data" - Alterado nome para Agendamento Acatado apenas
"Horas Para Agenda" - O que seria esse campo?
Apenas um botão para o agendamento,