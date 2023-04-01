import sympy as sy
from math import *
import re
import random


def substitui(f,icognita,numero):
    tota = ''
    
    for x in f:
        if (x == icognita):
            x = numero
        tota +=x 
    return (tota)



def derivada(f2,emrelacao):
    x = sy.diff(f2,emrelacao)

    return x


def sorteia_letra(separados):
    letra_aletorio = random.choice('abcdefghjklmnopqrstuvwxyz')
  
    if letra_aletorio in separados:
        while letra_aletorio in separados:
            letra_aletorio = random.choice('abcdefghjklmnopqrstuvwxyz')
            print("entrou")

    return (letra_aletorio)
    

def calculadoraerro(funcao_original,listadevariaveis,valoresdasvariaveis,f, erro):

    if not listadevariaveis:
        return("coloque as variaveis")

    if not valoresdasvariaveis:
        return("coloque as variaveis")

    if not f:
        return("coloque as variaveis")

    if not erro:
        return("coloque as variaveis")
    

    derivadapronta = []
    i = 0
    separados = listadevariaveis.split()
    numerosseparados = valoresdasvariaveis.split()
    errosseparados = erro.split()
    
    
    
    for x in separados:
        derivadapronta.append(derivada(f,x))
        i+=1
    
    p = 0
    subst = []
    i = 0 
    cont = 0
    i = 0
    
   
    for x in subst:
        subst[i] = eval(subst[i])
        i+=1
    
    

    for y in derivadapronta:
            for x in separados:
                if (p <= 0):
                    subst.append(y.subs(x,numerosseparados[p]))
                else:
                    subst[i] = subst[i].subs(x,numerosseparados[p])
                p+=1
            i+=1   
            p=0

    i = 0
    
    for x in errosseparados:
        errosseparados[i] = eval(errosseparados[i])
        i+=1

    i = 0
    h = []
    
    for x in subst:
        
        h.append( (((subst[i]))**2 * (errosseparados[i])**2))
        
        i+=1
    
    total = 0.0

    for x in h:
        total += x 


    
    totalconta = (total)**(1/2)

   
    #converter python para latex
    
    cont = 0
    c = ''
    ppp = ''
    
    for x in derivadapronta:
        z = "((({})**2)*(Delta_{})**2)".format(x,separados[cont])
        if cont == 0:
            c+=z
        if cont !=0:
            c += "+soma" + z 
        
        cont+=1



    c = "({})**(1/2)".format(c)
    
    cont=0
    for x in separados:
        derivada_antes = "( partial_{} / partial_{})* (Delta_{})**2".format(funcao_original,separados[cont],separados[cont])
        if cont == 0:
            ppp +=derivada_antes
        if cont !=0:
            ppp += "+" + derivada_antes
        
        cont+=1

    ppp = "({})**(1/2)".format(ppp)
    ppp = sy.latex(sy.sympify(ppp))
    ppp = re.sub(r"partial",r"\\partial", ppp)

    for x in separados:
        ppp = re.sub(r"\\Delta_",r"\\Delta ", ppp)  
        ppp = re.sub(r"partial_",r"partial ", ppp)

    encontre = re.findall(r"Delta.{8}", ppp)

    ppp = re.sub(r"\\Delta.{8}",r" ", ppp) 

        
    lista_privisoria = ppp.split("+")
    
    pppp = []
    for  i, elemento  in enumerate(encontre):
        if i == len(encontre)-1:
            pppp.append(lista_privisoria[i] +encontre[i]+")}")
        else:
            pppp.append(lista_privisoria[i] +"({})".format(encontre[i]))

    ppp =  "+".join(pppp)
    ppp = re.sub(r"Delta",r"\\Delta", ppp)
    ppp = re.sub(r"}}}\\Delta",r"}}(\\Delta", ppp)

    # for x in range(len(encontre)):
    #     ppp = re.sub(,r"\\Delta", ppp)  

  
    print(ppp)
    
    
    
    
   
    # latex = sy.latex(sy.sympify(c))
    # latex = re.sub(r"partial",r"\\partial", latex)

    # for x in separados:
    #     latex = re.sub(r"\\Delta_",r"\\Delta ", latex)  
    #     latex = re.sub(r"partial_",r"partial ", latex)

    # encontre_2 = re.findall(r"Delta.{8}", latex)

    # latex = re.sub(r"\\Delta.{8}",r" ", latex) 

        
    # lista_privisoria_2 = latex.split("+ \operatorname{soma}")

    # print(lista_privisoria_2)
    
    # latexp = []
    # for  i, elemento  in enumerate(encontre_2):
    #     if i == len(encontre)-1:
    #         latexp.append(lista_privisoria_2[i] +encontre_2[i]+")}")
    #     else:
    #         latexp.append(lista_privisoria_2[i] +"({})".format(encontre_2[i]))

    # latex =  "+".join(latexp)
    # latex = re.sub(r"Delta",r"\\Delta", latex)
    # latex = re.sub(r"}}}\\Delta",r"}}(\\Delta", latex)


    # padrao = r'\\Delta.{8}'
    # encontre = re.findall(padrao, ppp)
 
    # ppp = ppp.split("+")
    
    # i = 0
    # lista = []
    # for x in ppp:
    #    teste = re.sub(r"\\Delta.{8}","",x)
    #    lista.append(teste+'({})'.format(encontre[i]))
   
    #    i+=1
    # ppp = '+'.join(lista)

     # latex = sy.latex(sy.sympify(c))

    # for x in range(len(palavras_para_remover)):
    #     latex = re.sub(palavras_para_remover[x],"", latex)
    #     ppp = re.sub(palavras_para_remover[x],"", ppp)
    #     latex = re.sub(r"\\Delta_",r"\\Delta ", latex)
    

    # encontre = re.findall(padrao, latex)
 
    # latex= latex.split("+")
    
    # i = 0
    # lista = []
    # for x in latex:
    #    teste = re.sub(r"\\Delta.{8}","",x)
    #    lista.append(teste+'({})'.format(encontre[i]))
   
    #    i+=1
    # latex= '+'.join(lista)
    
    
    latex = 0
    return ("{} {}".format(totalconta, latex))

        
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

funcao_original = "V"
f = " R*I"
a = "R I"
b = "0.22 0.44 "
erro = "0.04 0.04 "

#(((B+b)h)/2)/T
#B b h T
#0.22 0.44 6.4 1
#0.04 0.04 0.4 0.04

print (calculadoraerro(funcao_original,a,b,f,erro))
