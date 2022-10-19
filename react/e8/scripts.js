function sorteador(...numeros){
    console.log(numeros);

    const numeroGerado = Math.floor(Math.random() * numeros.length);

    console.log(numeros[numeroGerado])
}

sorteador(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)