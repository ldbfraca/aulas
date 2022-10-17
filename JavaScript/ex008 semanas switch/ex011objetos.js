const pessoa1 = {
    nome: 'Lucas',
    sobrenome: 'França',
    idade: 24,
    hobbie: ['crossfit', 'estudar']
};

const pessoa2 = {
    nome: 'Manu',
    sobrenome: 'Prado',
    idade: 20,
    hobbie: ['mandar mensagem', 'brigar com lucas']
};

/*  const nome = pessoa2.nome;
    const sobrenome = pessoa2.sobrenome;
    const idade = pessoa2.idade;
    const hobbie = pessoa2.hobbie; */


const {nome,sobrenome,hobbie,idade} = pessoa1;

pessoa1.cachorro = 'Parça'


console.log(pessoa1.cachorro);

