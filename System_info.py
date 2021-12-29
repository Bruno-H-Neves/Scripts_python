import PySimpleGUI as sg
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import datetime
import pytz
import psutil

sg.theme('DarkGrey7')

menu_def = [[ '&File', ['&Exit',]],
            [ '&Help',['&Help','&About Us']]]

column1  = [[ sg.Text('Data:', size=(15, 1)),
              sg.Text('Hora:', size=(15, 1)),
              sg.Text('Bateria:', size=(15, 1))],
            [ sg.Frame(layout=[
            [ sg.Text('Hora:', size=(15, 1)), sg.Text('Hora:', size=(15, 1))],
            [ sg.Text('Hora:', size=(15, 1)), sg.Text('Hora:', size=(15, 1))]
                              ],title='Ram',title_color='red', tooltip="Center")]]

layout   = [[ sg.Menu(menu_def, tearoff=True)],
            [ sg.Column(column1, background_color='lightblue'),sg.Button('Exit', size=(7, 1))]]


window = sg.Window('Frame', layout, no_titlebar=True, location=(100,200))#,size=(size_row,size_col))
while True:
    event, values = window.read(timeout=0)
    dt_now = datetime.datetime.now(tz= pytz.UTC)
    date=r'%s-%s-%s' %(dt_now.day,dt_now.month,dt_now.year)
    hour=r'%s:%s:%s' %(dt_now.hour,dt_now.minute,dt_now.second) 
    used_ram='Ram: %s'%(str(psutil.virtual_memory().used))
    battery = psutil.sensors_battery()
    bat_percent ='Bat: %s '%(str(battery.percent))

    if event in ('Exit', None):
        break


    
