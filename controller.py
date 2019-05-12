import pyautogui
import time
import random

class controller(object):

    def __init__(self):
        self.mouse = pyautogui

    def move(self,pos,duration=1):
        self.mouse.moveTo(pos[0],pos[1],duration=1)

    def left_click(self):
        self.mouse.click()

    def double_click(self):
        self.mouse.doubleClick(interval=1.0)

    def left_drag(self):
        self.mouse.moveTo(982,570)
        self.mouse.dragTo(982,430,5)
