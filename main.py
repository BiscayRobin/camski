#!/usr/bin/env python3

import cv2

ASCII = [
    '@','%','#','*','+','=','-',':','.',' '
]

SIZE = 256

def map_range(src, dst, value):
    src_start, src_end = src
    dst_start, dst_end = dst
    return dst_start + ((value - src_start) * (dst_end - dst_start)) / (src_end - src_start)

def gray_to_ascii(value):
    return ASCII[
            len(ASCII) - 1 - min(int(value * len(ASCII) / 255),            len(ASCII)-1)
    ]


def row_to_ASCII_line(row):
    res = ""
    for pixel in row:
        res += gray_to_ascii(pixel)
    return res

def main():
    cap = cv2.VideoCapture(0)
    cap.set(3,SIZE) #width
    cap.set(4,SIZE) #height
    i=0

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while(ret):
        # Capture frame by frame
        ret, frame = cap.read()

        # Array of gray value
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        text = ""
        for row in gray:
            text += row_to_ASCII_line(row) + '\n'
        print(text + f'\033[{SIZE+1}A\033[K')
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        cv2.waitKey(33)

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __package__ == "__main__":
    main()
