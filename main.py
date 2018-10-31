import cv2
import numpy as np
from matplotlib import pyplot as plt
import pyautogui
import time
import pyscreenshot as ImageGrab

time.sleep(1)
coords = []
print '-> Locating coordinates of reCAPTCHA...'

pic = pyautogui.screenshot()    #taking screenshot
pic.save('main.jpg')            #saving screenshot

img_rgb = cv2.imread('main.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)               ###beginning template matching###
template = cv2.imread('sub.jpg',0)                                  #
w, h = template.shape[::-1]                                         #

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    coords.append(pt[0])        #storing upper left coordinates of reCAPTCHA box
    coords.append(pt[1])


if len(coords)!= 0 :
   
    print '-> Location found reCAPTCHA at :',coords

    reCAPTCHA_box_x_bias = 10
    reCAPTCHA_box_y_bias = 20

    coords[0] = coords[0] + reCAPTCHA_box_x_bias
    coords[1] = coords[1] + reCAPTCHA_box_y_bias

    print '-> Moving cursor to (1, 1)'
    pyautogui.moveTo(1, 1, duration = 0)

    print '-> Moving cursor towards reCAPTCHA'
    pyautogui.moveTo(coords[0], coords[1], duration = 0.12)

    print '-> Performing click action on reCAPTCHA'
    pyautogui.click()

    time.sleep(4)

    Submit_button_x_bias = 0
    Submit_button_y_bias = 75

    coords[0] = coords[0] + Submit_button_x_bias
    coords[1] = coords[1] + Submit_button_y_bias

    pyautogui.moveTo(coords[0], coords[1], duration = 0.14)

    print '-> Performing click action on Submit'
    pyautogui.click()

 else :
    print '-> reCAPTCHA box not found!'
    
