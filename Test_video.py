import PySimpleGUI as sg
import cv2 as cv




def main():
    imageTypes={'Type1':[1080,1920],
            'Type2': [1080,1080],
            'Type3': [1080,566],
            'Type4': [1080,1350],
            'Type5': [1200,630],
            'Type6': [851,315],
            'Type7': [640,480]}

    filename = sg.popup_get_file('Search File')
    if filename is None:
        return
    vidFile = cv.VideoCapture(filename)
    num_frames = vidFile.get(cv.CAP_PROP_FRAME_COUNT)
    fps = vidFile.get(cv.CAP_PROP_FPS)

    sg.theme('Black')

    layout = [[sg.Text('On Air', size=(15, 1), font='Helvetica 20')],
              [sg.Image(filename='',size=(100,20), key='-image1-'), sg.Image(filename='',size=(100,20), key='-image2-')],
              [sg.Slider(range=(0, num_frames),
                        size=(60, 10), orientation='h', key='-slider-')],
              [sg.Button('Exit', size=(7, 1), pad=((600, 0), 3), font='Helvetica 14'),sg.Text(' RealVideo', size=(15, 1), font='Helvetica 10')]]

    window = sg.Window('Frame', layout, no_titlebar=False, location=(0, 0))

    image_elem1 = window['-image1-']
    image_elem2 = window['-image2-']
    slider_elem = window['-slider-']

    cur_frame = 0
    while vidFile.isOpened():
        event, values = window.read(timeout=0)
        if event in ('Exit', None):
            break
        ret, frame = vidFile.read()
        if not ret:  
            break
        if int(values['-slider-']) != cur_frame-1:
            cur_frame = int(values['-slider-'])
            vidFile.set(cv.CAP_PROP_POS_FRAMES, cur_frame)
        slider_elem.update(cur_frame)
        cur_frame += 1
        frameResize = cv.resize(frame,(imageTypes['Type6'][0],imageTypes['Type6'][1]))
        imgTransform = cv.cvtColor(frameResize, cv.COLOR_RGB2GRAY)
        imgbytes = cv.imencode('.png', frameResize)[1].tobytes()  
        imgbytes2 = cv.imencode('.png', imgTransform)[1].tobytes() 
        image_elem1.update(data=imgbytes)
        image_elem2.update(data=imgbytes2)


main()