#!/usr/bin/env python3

import cv2

'''
ASCII = [   '$', '@', 'B', '%', '8', '&', 'W', 'M',
            '#', '*', 'o', 'a', 'h', 'k', 'b', 'd',
            'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q',
            'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c',
            'v', 'u', 'n', 'x', 'r', 'j', 'f', 't',
            '/', '\\','|', '(', ')', '1', '{', '}',
            '[', ']', '?', '-', '_', '+', '~', '<',
            '>', 'i', '!', 'l', 'I', ';', ':', ',',
            '"', '^', '`','\'', '.',
]

'''
ASCII = [
    '@','%','#','*','+','=','-',':','.',' '
]

def map_range(src, dst, value):
    src_start, src_end = src
    dst_start, dst_end = dst
    return dst_start + ((value - src_start) * (dst_end - dst_start)) / (src_end - src_start)

def gray_to_ascii(value):
    '''
    return ASCII[int(
            map_range(
            (0,255),
            (0,len(ASCII)-1),
            255-value)
    )]
    '''
    return ASCII[len(ASCII)-1 - min(int(value * len(ASCII) / 255), len(ASCII)-1)]


def row_to_line(row):
    res = ""
    for pixel in row:
        res += gray_to_ascii(pixel)
    return res

SIZE = 256

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
        text += row_to_line(row) + '\n'
    print(text + f'\033[{SIZE+1}A\033[K')
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.waitKey(33)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
