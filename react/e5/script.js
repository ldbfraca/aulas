var peso;
var altura;
var imc;
var resultado;

function calcular(event){
    event.preventDefault(); //deixa o texto no formulário
    peso = document.getElementById('peso').value;
    altura = document.getElementById('altura').value;
    
    imc = peso / (altura * altura);

    if(imc < 17){
        resultado = document.getElementById('resultado').value;
        //resultado.innerHTML = `<br> Seu resultado foi: ${imc} está muito abaixo do peso`
        console.log(resultado)
    } 




}