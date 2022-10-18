function pedir(){
    var valor = prompt("digite um valor de 1 a 4")
    console.log(valor)

    switch(Number(valor)){
        case 1:
            alert("escolheu 1")
            break
        case 2:
            alert("escolheu 2")
            break
        case 3:
            alert("esolheu 3")
            break
        case 4:
            alert("fazer pedido")
            break
        default:
            alert("escolha entre 1 e 4 mané")
            break
    }
}