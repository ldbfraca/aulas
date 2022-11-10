import PySimpleGUI as sg
import bibliotecas
layout = [
        [sg.T("sua reserva chegou em 6k?")],
        [sg.T(" ")],
        [sg.T("                   "), sg.Checkbox('mais que 6k', default=False, key='simreserva')],
        [sg.T("                   "), sg.Checkbox('menos que 6k', default=False, key='naoreserva')],
        [sg.T(" ")],
        [sg.T(" ")],
        [sg.Button('Calcular'), sg.Cancel()],
          ]


janela = sg.Window('LOTAR DINHEIRINHO sem ter reserva', layout, size=(400, 300))
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED or eventos == 'Cancel':
        break

    if eventos == 'Calcular':
        reais = int(valores['valor'])


        if valores['salario'] == True and valores['recebeu fora'] == True and valores['investimento'] == True \
                or valores['salario'] == True and valores['recebeu fora'] == True \
                or valores['salario'] == True and valores['investimento'] == True \
                or valores['recebeu fora'] == True and valores['investimento'] == True:
            janela['valor recebido'].update('APERTOU DOIS OU MAIS')


        elif valores['salario'] == True and valores['recebeu fora'] == False and valores['investimento'] == False:#só salario é verdadeiro
            janela['valor recebido'].update(distribuicao.recebeusalario(reais))


        elif valores['recebeu fora'] == True and valores['salario'] == False and valores['investimento'] == False: #só recebeu fora verdadeiro
            janela['valor recebido'].update(distribuicao.recebeuporfora(reais))


        elif valores['recebeu fora'] == False and valores['salario'] == False and valores['investimento'] == True:
            janela['valor recebido'].update(distribuicao.investimentos(reais))

        else:
            janela['valor recebido'].update('APERTE AO MENOS UM PARA CALCULAR')
janela.close()
