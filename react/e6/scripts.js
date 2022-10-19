function acao(){
    document.write('executando ... <br>')
}
//setInterval(acao,100)


//ou
//setInterval(() => {
//   document.write('executando... <br>');
//},100)

setTimeout(acao,1000) //executa uma vez o role

//ou 
//setTimeout(() => {
//    console.log('execute')
//},1000);