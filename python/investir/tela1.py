import PySimpleGUI as sg


layout = [[sg.T("Completou a reserva?"), sg.Checkbox('??', default=False, key='salario')],


          #[sg.T("                   "), sg.Checkbox('Recebeu Por Fora?', default=False, key='recebeu fora')],
          #[sg.T("                   "), sg.Checkbox('Quer investir??', default=False, key='investimento')],
          #[sg.T("Quanto recebeu?"), sg.InputText('', key='valor')],
          #[sg.Button('Próximo'), sg.Cancel()]
          #[sg.Text('', key='valor recebido')],
          ]
janela = sg.Window('LOTAR DINHEIRINHO sem ter reserva', layout, size=(400, 300))
while True:
    window, eventos, valores = sg.read_all_windows()
    if eventos == sg.WIN_CLOSED or eventos == 'Cancel':
        break
    
    
janela.close()
