import pyautogui
import cv2
import numpy as np
import time

class skills(object):

    def __init__(self):
        self.static_template={
            'tailwind':'arena images/tailwind.jpg',
            'bernard':'arena images/bernard.jpg',
            'atkbuff':'arena images/megan.jpg',
            'megan':'arena images/meganbody.jpg',
            'amp':'arena images/amp.jpg',
            'arrow':'arena images/yellowarrow.jpg',
            'auto':'arena images/auto.jpg',
            'reward':'arena images/reward.jpg',
        }

        self.template={k:cv2.imread(v,0) for (k,v) in self.static_template.items()}
        self.state='no skills used'
        self.frame=None

    def take_screenshot(self):
        im=pyautogui.screenshot()
        im_rgb= np.array(im)
        im_gray=cv2.cvtColor(im_rgb,cv2.COLOR_BGR2GRAY)
        return im_gray

    def refresh_frame(self):
        self.frame=self.take_screenshot()

    def find_skill(self,im_gray,image,precision):
        res= cv2.matchTemplate(im_gray,image,cv2.TM_CCOEFF_NORMED)
        min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
        w,h=image.shape
        if max_val >= precision:
            pos=max_loc
            pos=(max_loc[0]+(h/2),max_loc[1]+(w/2))
            return pos
        else:
            "Could not find."

    def templates(self,name,precision):
        im_gray=self.take_screenshot()
        return self.find_skill(
        im_gray,
        self.template[name],
        precision,
        )
