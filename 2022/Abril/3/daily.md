## Docker 01 - Introdução ao Docker

Docker é uma plataforma de conteinerização de código aberto.

Uma VM (Máquina Virtual) é um "outro computador" (guest) inteiro rodando em cima da máquina (host). Já o Docker é uma parte isolada do computador host que compartilha o ‘kernel’ (sistema operacional) e possivelmente, os binários e bibliotecas.

De forma geral: a estrutura de container (Docker) é muito mais rápida para fazer deploy, permite mais facilidade no gerenciamento de migrações de sistema e também "pesa menos", ou seja, tem menos overhead que uma VM. Por causa disso, também podemos ter mais aplicações rodando em simultâneo, no mesmo hardware.

Quando queremos fazer o controle de versão do sistema operacional em que a aplicação está rodando;
Quando queremos distribuir/disponibilizar para colaboração do time o sistema operacional em que a aplicação está rodando;
Quando queremos fazer com que o ambiente de desenvolvimento seja também o ambiente de produção, ajudando a eliminar inconsistências entre desenvolvimento e deploy;
Quando nossa aplicação precisa passar por vários estágios no pipeline de desenvolvimento (desenvolvimento → teste → produção);

As imagens são pacotes com sistemas de arquivos que contêm as dependências necessárias para a execução de nossas aplicações em nossos contêineres.
