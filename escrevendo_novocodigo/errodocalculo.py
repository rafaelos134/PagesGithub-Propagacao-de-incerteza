import sympy as sy
from math import *
import re


class trata_dados:
    def __init__(self,variavel_para_tratar = "lixo",separacao=' '):
       self.valor_separado = variavel_para_tratar.split(separacao)
       
    def remove_espacos(self):   
       espacos_removidos = [x.replace(" ", "") for x in self.valor_separado]
       return espacos_removidos

    def biblioteca_de_erros(self):
        biblioteca = {}
        for x in self.valor_separado:
          x= x.split('+-')
          biblioteca[x[0]] = x[1]
        
        return(biblioteca)
    
    def derivada(self, f,emrelacao):
        x = sy.diff(f,emrelacao)
        return x
       





def calculadoraerro(f,variaveis_envolvidas,dados_dos_erros):
   
    
    funcao_separada = trata_dados(f,'=')
    variaveis_serparadas = trata_dados(variaveis_envolvidas)
    dados_erros = trata_dados(dados_dos_erros)
    derivada_pronta = trata_dados()


    
    
    derivada_pronta = [derivada_pronta.derivada(funcao_separada.remove_espacos()[1],variaveis_serparadas.remove_espacos()[x]) for x in range(len(variaveis_serparadas.remove_espacos()))]

    

    print(derivada_pronta)
   


    
    #fazer codigo para obter somete latex 1 
    #obter somente erro
    #obter somente latex 2
    # print(derivadapronta)
 

        


f = "v = (((B+b)*h)/2)/T"
variaveis = "B b h T"
valores = "0.22+-0.04 0.44+-0.04 6.4+-0.4 1+-0.04"


#(((B+b)h)/2)/T
#B b h T
#0.22 0.44 6.4 1
#0.04 0.04 0.4 0.04

print (calculadoraerro(f,variaveis,valores))
