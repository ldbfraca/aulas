let pessoa={
    nome: "lucas",
    idade: 34,
    cargo: 'programador'
}

let novaPessoa = {
    ...pessoa,
    status: 'rico',
    cidade:'campinas'
}

console.log(novaPessoa)