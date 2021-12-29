import PySimpleGUI as sg
import datetime
import pytz
import psutil
import time

sg.theme('DarkGrey')

menu_def = [[ '&File', ['&Exit',]],
            [ '&Help',['&Help','&About Us']]]

column1  = [[ sg.Text('Data:', size=(5, 1)),sg.Text( key='-data-', size=(10, 1)),
              sg.Text('Hora:', size=(5, 1)),sg.Text( key='-hora-', size=(10, 1)),
              sg.Text('Bateria:',size=(7, 1)),sg.Text( key='-bateria-', size=(5, 1)),],
            [ sg.Frame(layout=[
            [ sg.Text('Total:', size=(5, 1)), sg.Text('Usada:', size=(5, 1)),sg.Text( key='-ram-', size=(10, 1))],
            [ sg.Text('?:', size=(5, 1)), sg.Text('?:', size=(5, 1))]
                              ],title='Ram Total Gbytes',title_color='red', tooltip="Center")]]

layout   = [[ sg.Menu(menu_def, tearoff=True)],
            [ sg.Column(column1, background_color='lightblue'),sg.Button('Exit', size=(7, 1))]]

window = sg.Window('System Information', layout, no_titlebar=False, location=(100,200))

while True:
    event, values = window.read(timeout=0)
    dt_now = datetime.datetime.now(tz= pytz.UTC)
    date=r'%s-%s-%s' %(dt_now.day,dt_now.month,dt_now.year)
    hour=r'%s:%s:%s' %(dt_now.hour,dt_now.minute,dt_now.second) 
    battery = psutil.sensors_battery()
    window['-data-'].update(date)
    window['-hora-'].update(hour)
    window['-ram-'].update(psutil.virtual_memory().used/1000000)
    window['-bateria-'].update(battery.percent)
    time.sleep(1)
    if event in ('Exit', None):
        break


    
