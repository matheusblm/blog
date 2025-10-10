Modificaçãoes do codebase de forma contínua e automatizaada evitando erros humano.
Evitar novos codigos darem erros

Principais processos
Testes, Linter, Qualidade do código, Verificação de segurança, Geração de artefatos prontos para o deploy, Identificação da proxima versão a ser gerado no software, Geração de tags e releases

Status check - Não pode ser Mergeado sem ter passado nos checks ou processo de review

Ferramentes Populares - Jenkis, Github Actions, Circle CI, AWS code build, Azure Devops, Google Cloud Build, Git lab Pipelinis / CI

Dentro de um workflow pode ter diversos jobs, e defino qual vai ser o evento que ele vai rodar

Evento -> Filtros -> Ambiente -> Ações
Push -> branches:master -> runs-on Ubuntu -> steps uses ou run npm run build

