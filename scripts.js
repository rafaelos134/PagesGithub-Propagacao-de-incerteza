
function fazPost(url, body){
    var element = document.getElementById("valorfinal");
    element.innerHTML = '<li>Carregando...</li>';
    let request = new XMLHttpRequest()
    request.open("POST",url,true)
    request.setRequestHeader("Content-type","application/json")
    request.send(JSON.stringify(body))
     
    request.onload = function(){
        console.log(this.responseText)
        //window.alert("o erro = " + this.responseText)
        var element = document.getElementById("valorfinal");
        element.innerHTML = "Valor do erro = "+this.responseText
    }   
    return request.responseText
}

function mandavalor(t){
    let url = "https://polar-headland-20103.herokuapp.com/https://calculo-erroexerimental.herokuapp.com//calculos"
    fazPost(url,t)   
}

//<link href="https://rafaelos134.github.io/calc-erro/style.css" rel="stylesheet" />
//<script src="https://rafaelos134.github.io/calc-erro/scripts.js"></script>
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
