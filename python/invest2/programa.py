import PySimpleGUI as sg
import bibliotecas
layout = [ ]
janela = sg.Window('LOTAR DINHEIRINHO sem ter reserva', layout, size=(400, 300))
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED or eventos == 'Cancel':
        break

    if eventos == 'Calcular':
        reais = int(valores['valor'])


janela.close()
