for(let c = 0; c <= 20; c++){
    console.log(c)
}

//ou 


const carros = ['carro1','carro2', 'carro3', 'carro4'];
for(let i = 0; i < carros.length; i++){
    console.log(carros[i])
}

//ou


for( let carro of carros){
    console.log(carro)
}



let index = 0;
while(index < 10){
    console.log(index);
    //index = index + 1;
}