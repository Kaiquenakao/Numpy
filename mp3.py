import PySimpleGUI as sg
# Biblioteca para rodar o mp3
import vlc

def mp3():
    sg.theme('Reddit')
    # Definir o layout
    layout = [
    ]
    return sg.Window('MP3', layout, finalize=True)

# GUI
janela = mp3()

# Eventos do sistema
while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WINDOW_CLOSED:
        break

