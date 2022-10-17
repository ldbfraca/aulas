const pessoa1 = {
    nome: 'lucas',
    sobrenome: 'frança',
    idade: 24,
    hobbie: ['crossfit', 'estudar']
};

const pessoa2 = {
    nome: 'manu',
    sobrenome: 'prado',
    idade: 20,
    hobbie: ['mandar mensagem', 'brigar com lucas']
};

/*  const nome = pessoa2.nome;
    const sobrenome = pessoa2.sobrenome;
    const idade = pessoa2.idade;
    const hobbie = pessoa2.hobbie; */


const {nome,sobrenome,hobbie,idade} = pessoa1;

console.log(nome, sobrenome, hobbie);