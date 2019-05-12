import cv2
import numpy as np
import pyautogui
from controller import *



class toArena(object):

    def __init__(self):

        self.static_template = {
            'home':'arena images/home.jpg',
            'arena':'arena images/step2.jpg',
            'goToArena':'arena images/step3.jpg',
            'battle':'arena images/step4.jpg',
            'wings':'arena images/step5.jpg',
            'start':'arena images/step6.jpg',
        }
        self.template = {k: cv2.imread(v,0) for (k,v) in self.static_template.items()}

        self.frame = None

    def take_screenshot(self):
        im=pyautogui.screenshot()
        im_rgb= np.array(im)
        im_gray=cv2.cvtColor(im_rgb,cv2.COLOR_BGR2GRAY)
        return im_gray

    def refresh_frame(self):
        self.frame=self.take_screenshot()

    def find_loc(self,im_gray,image):
        res= cv2.matchTemplate(im_gray,image,cv2.TM_CCOEFF_NORMED)
        min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
        w,h=image.shape
        pos=max_loc
        pos=(max_loc[0]+(h/2),max_loc[1]+(w/2))
        return pos

    def templates(self,name):
        im_gray=self.take_screenshot()
        return self.find_loc(
        im_gray,
        self.template[name]
        )
