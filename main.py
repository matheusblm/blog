import os
from os import makedirs

def criar_dias_mes(mes):
    makedirs(f"./{mes} ", exist_ok=True)
    file = "daily.md"
<<<<<<< HEAD
    for x in range(4,31):
=======
    for x in range(10,31):
>>>>>>> 5cdf0ced1ec4b7f993303b74710b52d5cc49aa4d
        path = f'{mes}/{x}'
        makedirs(path, exist_ok=True)
        with open(os.path.join(path, file), 'w') as fp:
            pass
<<<<<<< HEAD
criar_dias_mes("Marco")
=======
criar_dias_mes("Março")
>>>>>>> 5cdf0ced1ec4b7f993303b74710b52d5cc49aa4d
