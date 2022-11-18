Usar a tipagem simples e -> para demonstrar o retorno do dunder method
Ex:
def __init__(self, country: str) -> None

Lib typing, utilizar o union para indicar quando o metodo tem mais de um retorno possivle.

—-
Criando Excecoes - EAFP (e mais facil pedir perdao do que permissao)
Existem duas maneiras de criar erros personalizados:
Heranca de alguma classe de erro.
	exemplo : class CustomError(exception):
			pass
Heranca porem se preocupando com a mensagem de erro.
	exemplo: class CustomError(Exception):
			def __init__(self, *args, **kwargs):
				super().__init__(*args, **kwargs)
Raise - palavra para gerar um except.

Exemplo : raise NOMEDACLASS (“Mensagem de erro”)

—---------

Padrao Json

Modelo de transmissao de informacoes em objetos de dados.
Exemplo:
{
    "name": "Tereza",
    "age": 25,
    "height": 1.63,
    "staff": True,
    "technologies": ["Flask", "Django"]
}

Bibiliotecas JSON

Python tem a lib json. Tambem existem lib externas ujson, em questao de performance a ujson e mais rapida.

dica: import ujson as json

json.dump() - Usado para armazenar dados no formato JSON em um arquivo.


Exemplo
ninja = {"nome": "Uchiha Itachi", "vila": "Konoha"}
with open("dados.json", "w") as json_file:
    # ninja      -> objeto a ser escrito
    # json_file  -> file pointer
    # indent     -> opcional para indentação
    dump(ninja, json_file, indent=4)

json.dumps() - formata um determinado objeto python para uma string em formato JSON.

ninja = { 'nome': 'Uchiha Itachi', 'vila': 'Konoha'}
result = dumps(ninja)
'{"nome": "Uchiha Itachi", "vila": "Konoha"}'

json.load() - faz ao contrário do dump.
Exemplo: 
with open("dados.json", "r") as json_file:
    dados = load(json_file)
    print(dados)
{'nome': 'Uchiha Itachi', 'vila': 'Konoha'}

json.loads() - faz ao contrário do dumps.
Exemplo:
ninja_str = '{"nome": "Uchiha Itachi", "vila": "Konoha"}'
result = loads(ninja_str)
{'nome': 'Uchiha Itachi', 'vila': 'Konoha'}
