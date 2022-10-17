class Pessoa{
    constructor(nome){
        this.nome = nome;
  
    }
    digaMeuNome(){
        return `meu nome é ${this.nome}`;
    }


}

modulo.exports = {
    Pessoa,
};