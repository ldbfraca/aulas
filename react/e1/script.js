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