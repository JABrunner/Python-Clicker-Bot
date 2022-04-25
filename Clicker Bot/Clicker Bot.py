import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import PySimpleGUI as sg

TOGGLE_KEY = KeyCode(char="t")
sg.theme('Dark Green 5')
layout = [
    
    [sg.Text('Press T to Start and Stop Clicker')],
    [sg.Button('Close', button_color = ('black','green'))],
    
]
window = sg.Window('Clicker Bot', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == 'Close':
        window.close()

window.close()




    
clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            time.sleep(0.0001)

def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()