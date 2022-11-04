'''faça um programa que entre o preço de um produto e o valor em dinheiro pago.
imprima qual o valor do troco'''

produto = float(input('qual o valor do produto? '))
valor = float(input('qual o valor do dinheiro pago? '))

total = valor - produto

print(f'o valor restante é de {total}')