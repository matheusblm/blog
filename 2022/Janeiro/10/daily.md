10/01 - Sprint 3

Classes sao basicamente a mesma coisa em quase todas as linguagens apenas mudando sua sintaxe.

class NOMEDACLAS:
codigo.
Instanciando a classe:
exemplo = NOMEDACLAS()

Atributos - Podem ser chamadas de caracteristicas.
exemplo:
class nomedaclass:
def**init**(self,exemplo):
self.exemplo = exemplo

Metodos em classe:
Sao funcoes dentro de uma classe.
exemplo:

class nomedaclass:
def**init**(self,exemplo = False):
self.exemplo = exemplo
de ligar(self)
self.exemplo = True
obs: o operador “=” define um valor padrao para o parametro.

Variáveis globais ficam logo abaixo da declaração da classe.
Tomar cuidado com os dados imutaiveis e mutáveis.

Atributos estáticos = existem sem a necessidade de uma instância
Atributos de instância = existem dentro de cada instancia.

—
Métodos estáticos

Não faz parte do escope da instância nem da classe, não recebe parâmetro de referência.
Usado através do decoretor @staticmethod

@classmethod = para utilizar um método que se encontra na instância na classe. Utilitários nos parâmetros.
@staticmethod = não necessita de referência.

—

Métodos Mágicos / Métodos especiais / Dunder Methods

Para cada funcao built-in existeum metodo dunder correspondente.
Exemplo:

def **len**(self):
return len(self.exemplo)
def **str**(self):
return f’O {self.exemplo} esta lindo hoje.’

—--------------
Herança
Consistem em pasar a a interface da classe pai para as demais classes.
Exemplo:
clas Animal:
def **init**(self, peso, cor):
self.peso = peso
self.cor = cor
class Cachorro(Animal):
def **init**(self,peso,cor,pelo,genro):
super().**init**(peso,cor)
self.pelo = pelo
self.genero = genero

class Cachorro(Animal):
def **init**(self,peso,cor,patas : int = 4, cela: bool = true):
super().**init**(peso,cor)
self.pelo = pelo
self.genero = genero
