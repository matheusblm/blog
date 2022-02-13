import os
from os import makedirs

def criar_dias_mes(mes):
    makedirs(f"./{mes} ", exist_ok=True)
    file = "daily.md"
    for x in range(9,28):
        path = f'{mes}/{x}'
        makedirs(path, exist_ok=True)
        with open(os.path.join(path, file), 'w') as fp:
            pass
criar_dias_mes("Fevereiro")