import os
import cv2 as cv
import numpy as np

pixel_to_cm = 9/27550

def get_frame(sec, count):
    vidcap = cv.VideoCapture('video.mp4')
    vidcap.set(cv.CAP_PROP_POS_MSEC, sec*1000)
    has_frames, image = vidcap.read() # pega um frame do video
    if has_frames: # se o video ainda não tiver acabado
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY) # converte o frame pra grayscale
        image = cv.medianBlur(image, 5) # tira pontos brancos
        image = cv.threshold(image, 100, 255, cv.THRESH_BINARY_INV)[1] # binariza
        M = cv.moments(image)
        cX = int(M["m10"] / M["m00"]) # calculo da coordenada x do centro de massa
        cY = int(M["m01"] / M["m00"]) # calculo da coordenada x do centro de massa
        cv.circle(image, (cX, cY), 3, (0, 0, 0), -1) # desenhando o centro de massa
        # f = open('posxt.txt', 'a')
        # f.write(f'{cX} {sec}\n') # escreve posicao e tempo no arquivo txt
        # f.close()
        print(sec, cX*pixel_to_cm)
        cv.imwrite(os.path.join( './binary_images/', "image" + str(count) + ".jpg" ), image) # salva o frame na pasta ./binary_images/
    return has_frames


def expand_video():
    sec = 0
    count = 1 # variavel auxiliar pra salvar os nomes dos arquivos em ordem crescente
    frame_rate = round(1/30, 2) # 30 fps
    success = get_frame(sec, count)
    while (success and count < 40):
        count += 1
        sec += frame_rate
        sec = round(sec, 2)
        success = get_frame(sec, count)


def main():
    expand_video()
    pass


if __name__ == "__main__":
    main()
