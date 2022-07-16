




function fazPost(url, body){
    console.log("Body=",body)
    let request = new XMLHttpRequest()
    request.open("POST",url,true)
    request.setRequestHeader("Content-type","application/json")
    request.send(JSON.stringify(body))

    request.onload = function(){
        console.log(this.responseText)
        //window.alert("o erro = " + this.responseText)
        var element = document.getElementById("valorfinal");
        element.innerHTML = this.responseText
    }   
    return request.responseText
}

function mandavalor(t){
    let url = "https://polar-headland-20103.herokuapp.com/https://teste-ca.herokuapp.com//calc"
    fazPost(url,t)   
}


function calcular(){
    
    
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
