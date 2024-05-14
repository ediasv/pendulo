import os
import cv2 as cv

def get_frame (sec, count):
    vidcap = cv.VideoCapture('video.mp4')
    vidcap.set(cv.CAP_PROP_POS_MSEC, sec*1000)
    has_frames, image = vidcap.read()
    if has_frames:
        cv.imwrite("image" + str(count) + ".jpg", image)
    return has_frames


def save_images():
    sec = 0
    count = 1
    frame_rate = round(1/30, 2) # 30 fps
    success = get_frame(sec, count)
    while (success and count<10):
        count += 1
        sec += frame_rate
        sec = round(sec, 2)
        success = get_frame(sec, count)


def binarize():
    pass


def main():
    save_images()
    binarize()
    pass


if __name__ == "__main__":
    main()
