import sympy as sy
from math import *




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



def calculadoraerro(listadevariaveis,valoresdasvariaveis,f, erro):

    derivadapronta = []
    i = 0
    separados = listadevariaveis.split()
    numerosseparados = valoresdasvariaveis.split()
    errosseparados = erro.split()
    
  
    for x in separados:
        derivadapronta.append(derivada(f,x))
        i+=1
    
    p = 0
    subs = []
    i = 0 
    cont = 0


    for y in derivadapronta:
            for x in separados:
                if (p <= 0):
                    subs.append(substitui(str(y),x,numerosseparados[p]))
                else:
                    subs[i] = substitui(subs[i],x,numerosseparados[p])
                p+=1
            i+=1   
            p=0
          
    i = 0
    
    print(subs)
    for x in subs:
        subs[i] = eval(subs[i])
        i+=1
    
    i = 0
    
    for x in errosseparados:
        errosseparados[i] = eval(errosseparados[i])
        i+=1





    i = 0
    h = []
    
    for x in subs:
        
        h.append( (((subs[i]))**2 * (errosseparados[i])**2))
        
        i+=1
    
    total = 0.0

    for x in h:
        total += x 


    
    totalconta = (total)**(1/2)

    #totalconta 

    
    
    return ("{}".format(totalconta))


        
#funcao


#(t)/(c)
# t c
#65.8740 0.0022
#0.0006 0.0004


#f = "b*r*c"
#a = "b r c"
#b = "0.089 47 (80.8*10**-6)"
#erro = "0.002 2.35 (2.5*10**-6)"


#b = "(614*10**(-9)) (-0.044) 0.05 960"

#erro = "(30*10**(-9)) (0.005) (0.002) (0)"

f = "1/(sin(x))"

a = "x"

b = "0.80"

erro = "0.02"

#variaveis q vai derivar
#print('use o padrão do python \033[31m(** potencia) (*multiplicação) (/divisão)\033[m  \033[1;33m não se esqueça número descimal usa . \033[m' )
#f = input("digite sua função: ")
#a = input("fale as variaveis envolvidas: ")
#b = input("fale os valores das variaveis: ")
#erro = input("fale os valores dos erros: ")



print (calculadoraerro(a,b,f,erro))
