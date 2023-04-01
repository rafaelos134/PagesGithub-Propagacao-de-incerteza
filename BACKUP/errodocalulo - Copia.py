import sympy as sy
from math import *
import re


class trata_dados:
    def __init__(self,variavel_para_tratar,separacao=' '):
       self.valor_separado = variavel_para_tratar.split(separacao)

    def remove_espacos(self):   
       self.espacos_removidos = [x.replace(" ", "") for x in self.valor_separado]

    def biblioteca_de_erros(self):
        biblioteca = {}
        for x in self.valor_separado:
          x= x.split('+-')
          biblioteca[x[0]] = x[1]
        
        return(biblioteca)
    
    def derivada(f2,emrelacao):
        x = sy.diff(f2,emrelacao)

        return x
       





def calculadoraerro(f,variaveis_envolvidas,dados_dos_erros):
    derivadapronta = []
    funcao_separada = trata_dados(f,'=')
    variaveis_serparadas = trata_dados(variaveis_envolvidas)
    dados_erros = trata_dados(dados_dos_erros)
    
    for x in variaveis_serparadas:
            derivadapronta.append(derivada(funcao_separada,x))
            i+=1

    print(derivadapronta)

 

        
#funcao


#f = ""
#a = ''
#b = ""
#erro = ""


f = "t/c"
a = 't c'
b = " 2 3"
erro = "1 4"


#f = "b*r*c"
#a = "b r c"
#b = "0.089 47 (80.8*10**-6)"
#erro = "0.002 2.35 (2.5*10**-6)"


#b = "(614*10**(-9)) (-0.044) 0.05 960"

#erro = "(30*10**(-9)) (0.005) (0.002) (0)"

#f = "(-2*l)/(R * C * log(a))"

#a = "l R C a"

#b = "(1.26*10**(-3)) (47) (80*10**(-6)) (0.87)"

#erro = "(0.01*10**(-3)) (5) (1*10**(-6)) (0.01)"

#variaveis q vai derivar
# print('use o padrão do python \033[31m(** potencia) (*multiplicação) (/divisão)\033[m  \033[1;33m não se esqueça número descimal usa . \033[m' )
# funcao_original = input("função original: ")
# f = input("digite sua função: ")
# a = input("fale as variaveis envolvidas: ")
# b = input("fale os valores das variaveis: ")
# erro = input("fale os valores dos erros: ")


f = "v = (((B+b)*h)/2)/T"
variaveis = "B b h T"
valores = "0.22+-0.04 0.44+-0.04 6.4+-0.4 1+-0.04"


#(((B+b)h)/2)/T
#B b h T
#0.22 0.44 6.4 1
#0.04 0.04 0.4 0.04

print (calculadoraerro(f,variaveis,valores))
