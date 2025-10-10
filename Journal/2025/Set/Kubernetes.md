Rodar cluster em diversas maquinas
Veio de dentro do Google
GCP Melhor cloud para kubernets
Orquestrar containers

é disponibilizado através de um conjuneto de APIs
usado atraves do CLI kubectl
Parecido com o docker na criação do arquivo .yaml

Cluster = conjunto de maquinas (Nodes)
Kubernets Master - Controla os nós
Cada maquina possui uma quantidade de vCPU e Memoria
Pods: Unidade que contem os containers provisionados, representa o processo rodando no cluster
Normalmente um pod por container
Deployment = Provisionar os pods, necessario saber quantas replicas
Replicas sets = numero de replicas que vai ser necessario, se um cair o ourto ja sobe automaticamente

B = Backend = 3 replicas
F = Front = 2 replicas