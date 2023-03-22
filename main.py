import os
from os import makedirs

def criar_dias_mes(mes, startDate, endDate):
    for x in range(startDate,endDate):
        file = f'{x}.md'
        path = f'./Journal/{mes}'
        makedirs(path, exist_ok=True)
        with open(os.path.join(path, file), 'w') as fp:
            pass

criar_dias_mes("Março", 1, 31)
