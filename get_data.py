import cv2 as cv


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


def get_frame(sec):
    vidcap = cv.VideoCapture('video.mp4')
    vidcap.set(cv.CAP_PROP_POS_MSEC, sec*1000)
    has_frames, image = vidcap.read() # pega um frame do video
    if has_frames: # se o video ainda não tiver acabado
        image = binarize(image)
        cX = center_of_mass(image)
        write_time(sec)
        write_pos(cX)
    return has_frames


def write_time(sec):
    dados_tempo = open('./output/tempos.txt', 'a')
    dados_tempo.write(f'{sec}\n')
    dados_tempo.close()


def write_pos(pos):
    dados_espaciais = open('./output/espacos.txt', 'a')
    dados_espaciais.write(f'{pos*pixel_to_cm}\n') # conversao da unidade de medida da posicao de pixel para cm (baseada nos dados experimentais)
    dados_espaciais.close()


def expand_video():
    sec = 0
    frame_rate = round(1/30, 2) # 30 fps
    success = get_frame(sec)
    while success:
        sec += frame_rate
        sec = round(sec, 2)
        success = get_frame(sec)


def main():
    expand_video()
    pass


if __name__ == "__main__":
    main()
