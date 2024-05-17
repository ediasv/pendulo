import os
import cv2 as cv
import numpy as np

pixel_to_cm = 9/27550 # relação de cm/pixel (considerando que o penulo foi solto de um ângulo inicial de aprox 10 graus)
# a massa utilizada tinha aproximadamente 102g e o comprimento do pendulo era de aproximadamente 52cm


def binarize(image):
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY) # converte o frame pra grayscale
    image = cv.medianBlur(image, 5) # tira pontos brancos
    image = cv.threshold(image, 100, 255, cv.THRESH_BINARY_INV)[1] # binariza
    return image


def center_of_mass(image):
    M = cv.moments(image)
    cX = int(M["m10"] / M["m00"]) # calculo da coordenada x do centro de massa
    return cX


def save_data(sec, cX):
    if sec:
        f = open('./output/posxt.txt', 'a')
    else:
        f = open('./output/posxt.txt', 'w')
    f.write(f'{sec}    {cX*pixel_to_cm}\n')
    f.close()


def get_frame(sec, count):
    vidcap = cv.VideoCapture('video.mp4')
    vidcap.set(cv.CAP_PROP_POS_MSEC, sec*1000)
    has_frames, image = vidcap.read() # pega um frame do video
    if has_frames: # se o video ainda não tiver acabado
        image = binarize(image)
        cX = center_of_mass(image)
        salva_tempo(sec)
        salva_espaco(cX)
        # x_data[count-1] = sec
        # y_data[count-1] = cX*pixel_to_cm
        # save_data(sec, cX)
        # cv.imwrite(os.path.join( './binarized_images/', "image" + str(count) + ".jpg" ), image) # salva o frame na pasta ./binary_images/
    return has_frames


def salva_tempo(sec):
    dados_tempo = open('./output/tempos.txt', 'a')
    dados_tempo.write(f'{sec}\n')
    dados_tempo.close()


def salva_espaco(pos):
    dados_espaciais = open('./output/espacos.txt', 'a')
    dados_espaciais.write(f'{pos}\n')
    dados_espaciais.close()


def expand_video():
    sec = 0
    count = 1 # variavel auxiliar pra salvar os nomes dos arquivos em ordem crescente
    frame_rate = round(1/30, 2) # 30 fps
    success = get_frame(sec, count)
    while success:
        count += 1
        sec += frame_rate
        sec = round(sec, 2)
        success = get_frame(sec, count)


def plot_graph():
    return


def main():
    # expand_video()
    for i in x_data:
        print(i)
    # plot_graph()
    pass


if __name__ == "__main__":
    main()
