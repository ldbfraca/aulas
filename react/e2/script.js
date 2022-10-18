var area = document.getElementById('area')
function entrar(){
    alert("clicou")
    var nome = prompt('diga o nome')

    if(nome == '' || nome == null){
        alert("ops, deu errado")
        area.innerHTML = "TEM QUE ESCREVER ALGO IMBECIL"
    }else{
        area.innerHTML = "isso ai " + nome
        let botao = document.createElement("button");
        botao.innerText = "sair";
        botao.onclick = sair;
        area.appendChild(botao);
    }
}

function sair(){
    alert("até mais")
    area.innerHTML = "vc saiu"
}

function mediaAluno(n1,n2){
    var media = (n1 + n2) / 2

    if (media >= 6 ){
        console.log("aluno aprovado com media " + media)
    }else if(media < 6){
        console.log("aluno reprovado com media "+ media)
    }
}


function nomeAluno(nome){
    var nome
    console.log(nome)
}