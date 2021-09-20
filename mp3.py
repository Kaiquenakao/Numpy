import PySimpleGUI as sg
import vlc

def mp3():
    sg.theme('Reddit')
    layout = [
        [sg.Input(default_text='Insira o arquivo MP3: '), sg.FileBrowse('Seleciona', key='-IN-')],
        [sg.Button('Tocar', key='tocar')], [sg.Button('Parar', key='parar')],
    ]
    return sg.Window('MP3', layout, finalize=True)

# GUI
janela = mp3()

# Eventos do sistema
while True:
    window, event, values = sg.read_all_windows()
    # Evento para fechar o sistema
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'tocar' and values['-IN-'] != "":
        vlc.MediaPlayer(values['-IN-']).play()

