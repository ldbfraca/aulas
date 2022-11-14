def tela1():
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

    janela.close()
