import PySimpleGUI as sg
import bibliotecas
import tela2
layout = [
        [sg.T("Qual a fonte do recebimento?")],
        [sg.T(" ")],
        [sg.T("                   "), sg.Checkbox('Salário', default=False, key='salario')],
        [sg.T("                   "), sg.Checkbox('Amipress', default=False, key='amipress')],
        [sg.T("                   "), sg.Checkbox('Glaucia', default=False, key='glaucia')],
        [sg.T("                   "), sg.Checkbox('Legado', default=False, key='legado')],
        [sg.T(" ")],
        [sg.T(" ")],
        [sg.Button('Calcular'), sg.Cancel()],
        ]


janela = sg.Window('LOTAR DINHEIRINHO sem ter reserva', layout, size=(400, 300))

while True:
    eventos, valores, janela = sg.read_all_windows()

    if eventos == sg.WIN_CLOSED or eventos == 'Cancel':
        break

    if eventos == 'Calcular':

        if valores['salario'] == True:
            telaa = tela1()
            tela1.hide()



