import cv2 as cv

vidcap = cv.VideoCapture('video.mp4')

def getFrame(sec):
    vidcap.set(cv.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv.imwrite("image"+str(count)+".jpg", image)     # salva o frame como jpg
    return hasFrames

sec = 0
frameRate = 0.04 # salva uma imagem a cada 0.04 segundos == 25 fps
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
