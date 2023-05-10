class Salario:
    def __init__(self, base, bonus):
        self.base = base
        self.bonus = bonus

    def salario_anual(self):
        return (self.base*12)+self.bonus

    def change_base(self, base):
        self.base = base


class Emprego:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario_agregado = salario

    def salario_total(self):
        return self.salario_agregado.salario_anual()


salario = Salario(1000, 800)
emp = Emprego("mus", 46, salario)
# print(salario.base)
# salario.change_base(200)
# print(salario.base)


class Circulo:
    _total_circulos = 0  # todas as classes compartilham do mesmo contador

    def __init__(self, pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        type(self)._total_circulos += 1

    @classmethod
    def __gettotal_circulos(cls):
        return cls._total_circulos

    def gettotal_circulos(cls):
        return cls._total_circulos


crc = Circulo(2, 3, 6)
print(crc.gettotal_circulos())

# static methods = validar
