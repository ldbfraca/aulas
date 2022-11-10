import PySimpleGUI as sg
import distribuicao
layout = [[sg.T("                   "), sg.Checkbox('Recebeu Salário?', default=False, key='salario')],
          [sg.T("                   "), sg.Checkbox('Recebeu Por Fora?', default=False, key='recebeu fora')],
          [sg.T("                   "), sg.Checkbox('Quer investir??', default=False, key='investimento')],
          [sg.T("Quanto recebeu?"), sg.InputText('', key='valor')],
          [sg.Button('Calcular'), sg.Cancel()],
          [sg.Text('', key='valor recebido')],
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
