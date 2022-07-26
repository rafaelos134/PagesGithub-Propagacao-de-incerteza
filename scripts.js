
function fazPost(url, body){
    var element = document.getElementById("valorfinal");
    element.innerHTML = '<li>Carregando...</li>';
    let request = new XMLHttpRequest()
    request.open("POST",url,true)
    request.setRequestHeader("Content-type","application/json")
    request.send(JSON.stringify(body))
     
    request.onload = function(){
   
        var respostanumero = document.getElementById("valorfinal");
        var resostaeq = document.getElementById("MyEquation");

        const teste3 = this.responseText
        const teste = this.responseText.split(" "); //o erro ta nessa divisao, talvez usar outro metodo sem ser string
        
        respostanumero.innerHTML = `Valor do erro = ${teste[0]}`

        console.log(teste3)
        let cont = 0
        let c = ""

        for (let x of teste){ 
            
            if (cont != 0){
                c += x
            }  
            cont+=1
        }
        
        
        resostaeq.innerHTML  = String.raw`$ \delta (f) = ${c}$`

        
        MathJax.Hub.Queue(["Typeset",MathJax.Hub,'outputDiv']);
        
        document.getElementById("lateS").innerHTML  = `LATEX = \\delta (f) = ${c}`


        if (teste3 == "coloque as variaveis"){
            respostanumero.innerHTML = `COLOQUE AS VARAIAVEIS`
            resostaeq.innerHTML = ''
            document.getElementById("lateS").innerHTML  = ''
        }
        
        
    }

    return request.responseText
}

function mandavalor(t){
    let url = "https://polar-headland-20103.herokuapp.com/https://calculo-erroexerimental.herokuapp.com//calculos"
    fazPost(url,t)   
}

function calcular(){
    console.log("aq")
    
   let funcao = document.getElementById("funcao").value;
   let variaveis = document.getElementById("variaveis").value;
   let valordavariavel = document.getElementById("valor_variaveis").value;
   let erros = document.getElementById("erros").value;
    
    //let funcao = "(t)/(c)"
    //let variaveis = "t c"
    //let valordavariavel = "65.8740 0.0022"
    //let erros = "0.0006 0.0004"


    body = {
        "variaveis" : variaveis,
        "valordavariavel" : valordavariavel,
        "f" : funcao,
        "erro" : erros
         
    }

    console.log(body)
    mandavalor(body)
}
