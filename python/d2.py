''' faça um programa que leia 3 valores inteiros e imprima o maior e o menor deles'''

a = int(input('diga qual o valor 1: '))
b = int(input('diga qual o valor 2: '))
c = int(input('diga qual o valor 3: '))

if a == b == c:
    print(f'os valores sao iguais: {a}')

elif a > b & a > c:
    print(f'o valor a: {a} é maior')

elif b > a & b > c:
    print(f' o valor {b} é maior')

elif c > b & c > a:
    print(f'c é maior, com {c}')
