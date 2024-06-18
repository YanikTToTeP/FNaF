from pygame import *

font.init()
mw = display.set_mode((1280,720))
display.set_caption('FNaF')
bg = transform.scale(image.load('Ofis\Centr.jpg'), (1280, 720))
bg_number = 1


while True:
    for e in event.get():
        if e.type == QUIT:
            exit()
    mw.blit(bg, (0,0))

    keys = key.get_pressed()
    if keys[K_LEFT]:
        if bg_number == 1:
            bg = transform.scale(image.load('Ofis\Left.jpg'), (1280, 720))
            bg_number = 0
        elif bg_number == 2:
            bg = transform.scale(image.load('Ofis\Centr.jpg'), (1280, 720))
            bg_number = 1
    if keys[K_RIGHT]:
        if bg_number == 1:
            bg = transform.scale(image.load('Ofis\Right.jpg'), (1280, 720))
            bg_number = 2
        elif bg_number == 0:
            bg = transform.scale(image.load('Ofis\Centr.jpg'), (1280, 720))
            bg_number = 1

    
    display.update()
    time.delay(20)

