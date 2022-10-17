const numero = [1,2,3,4,5,6,7,8,9,10]

const numerovezes2 = numero.map(function(number){
    return number *2;})

console.log(numerovezes2)

const pares = numero.filter(function(numero){ //para numeros pares
    return numero % 2 ==0;})

console.log(pares)


//somar valores da lista

const soma = numero.reduce(function(numero, accumulator){
    return accumulator + numero
},0);

console.log(soma)