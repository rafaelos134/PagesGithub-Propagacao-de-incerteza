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
    for x in derivadapronta:
        z = "((({})**2)*(delta_{})**2)".format(x,separados[cont])
        if cont == 0:
            c+=z
        if cont !=0:
            c += "+" + z 
        
        cont+=1

   

    c = "({})**(1/2)".format(c)
    
    latex = sy.latex(sy.sympify(c))
    
    return ("{} {}".format(totalconta, latex))

        
#funcao


f = ""
a = ''
b = ""
erro = ""


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
#print('use o padrão do python \033[31m(** potencia) (*multiplicação) (/divisão)\033[m  \033[1;33m não se esqueça número descimal usa . \033[m' )
#f = input("digite sua função: ")
#a = input("fale as variaveis envolvidas: ")
#b = input("fale os valores das variaveis: ")
#erro = input("fale os valores dos erros: ")



print (calculadoraerro(a,b,f,erro))
