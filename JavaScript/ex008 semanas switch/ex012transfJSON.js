const todos = [
    {
        id:0,
        descrição: 'estudar',
        completou: false
    },
    {
        id:1,
        descrição: 'treinar',
        completou: true
    },
    {
        id:2,
        descrição: 'construir site',
        completou: false
    },
];

const todosJSON = JSON.stringify(todos); //transformou pra JSON
const todoslista = JSON.parse(todosJSON); //transoforrmou em lista
console.log(todosJSON)
console.log(todoslista)

console.log(todoslista[1])