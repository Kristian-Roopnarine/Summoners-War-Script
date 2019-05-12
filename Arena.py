import pyautogui
import PIL
import time
from skills import skills
from controller import controller
from toArena import toArena

class Arena:

    def __init__(self,arena,controller,skills):
        self.skills=skills
        self.arena=arena
        self.controller=controller
        self.state='not-arena'

    def click_home(self):
        pos = self.arena.templates('home')
        self.controller.mouse.moveTo(pos)
        self.controller.left_click()
        time.sleep(1)

    def click_arena(self):
        pos= self.arena.templates('arena')
        self.controller.mouse.moveTo(pos)
        self.controller.left_click()
        time.sleep(1)

    def click_goToArena(self):
        pos=self.arena.templates('goToArena')
        self.controller.mouse.moveTo(pos)
        self.controller.left_click()
        time.sleep(1)

    def click_battle(self):
        pos=self.arena.templates('battle')
        self.controller.mouse.moveTo(pos)
        self.controller.left_click()
        time.sleep(1)

    def click_wings(self):
        pos=self.arena.templates('wings')
        self.controller.mouse.moveTo(pos)
        self.controller.left_click()
        time.sleep(1)

    def click_start(self):
        pos= self.arena.templates('start')
        self.controller.mouse.moveTo(pos)
        self.controller.left_click()
        time.sleep(1)

    def have_tailwind(self):
        match=self.skills.templates('tailwind',precision=.85)
        return match

    def click_tailwind(self):
        pos= self.skills.templates('tailwind',precision=.85)
        self.controller.move(pos)
        self.controller.left_click()

    def click_bernard(self):
        pos=self.skills.templates('bernard',precision=.85)
        self.controller.move(pos)
        self.controller.left_click()
        time.sleep(5)

    def have_atk_buff(self):
        match=self.skills.templates('atkbuff',precision=.85)
        return match

    def click_atk_buff(self):
        pos= self.skills.templates('atkbuff',precision=.85)
        self.controller.move(pos)
        self.controller.left_click()

    def click_megan(self):
        pos=self.skills.templates('arrow',precision=.6)
        pos=(pos[0],pos[1]+150)
        self.controller.move(pos)
        self.controller.left_click()
        time.sleep(5)

    def have_amp(self):
        match=self.skills.templates('amp',precision=.85)
        return match

    def click_amp(self):
        pos=self.skills.templates('amp',precision=.85)
        self.controller.move(pos)
        self.controller.left_click()
        time.sleep(1)

    def have_enemy(self):
        match=self.skills.templates('arrow',precision=.6)
        return match

    def click_enemy(self):
        pos=self.skills.templates('arrow',precision=.6)
        self.controller.move(pos)
        self.controller.left_click()

    def have_auto(self):
        match=self.skills.templates('auto',precision=.85)
        return match

    def click_auto(self):
        pos=self.skills.templates('auto',precision=.85)
        self.controller.move(pos)
        self.controller.left_click()

    def match_end(self):
        match=True
        while match:
            try:
                end = pyautogui.locateCenterOnScreen("arena images/reward.jpg",confidence=.5)
                if type(end) is not None:
                    pyautogui.doubleClick(pyautogui.locateCenterOnScreen("arena images/reward.jpg",confidence=.5),interval=1.0)
                    match=False
                    self.skills.state='no skills used'
            except TypeError:
                print("Match still ongoing")
                time.sleep(2)
                continue


    def double_lushen(self):
        battle=True
        while battle:
            print("Looking for skills")
            if self.have_tailwind() and self.skills.state=='no skills used':
                print("Have tailwind")
                self.click_tailwind()
                print("Using tailwind")
                self.click_bernard()
                self.skills.state='tailwind used'
            elif self.have_atk_buff():
                print("Have attack buff")
                self.click_atk_buff()
                print("Buffing")
                self.click_megan()
                self.skills.state='buffed'
            elif self.have_amp():
                for i in range(2):
                    try:
                        self.click_amp()
                        print("Using amputation magic")
                        self.click_enemy()
                        time.sleep(7)
                        self.skills.state='done'
                    except TypeError:
                        print("No Amputation Magic")
                        time.sleep(7)
            elif self.have_auto():
                    self.click_auto()
                    self.skills.state='auto'
            elif self.skills.state == 'done' or self.skills.state=='auto':
                self.match_end()
                battle=False
                self.skills.state='no skills used'



    def navigate(self):
        if self.state == 'not-arena':
            self.click_home()
            print("going to arena")
            self.click_arena()
            print("going to lobby")
            self.click_goToArena()
            print("going to click battle")
            self.click_battle()
            print("going to click on wings")

        else:
            print("Idk where you at homie.")


    def use_wings(self):
        wings=eval(pyautogui.prompt("How many wings?"))
        used_wings=0
        while used_wings < wings:
            self.click_wings()
            print("going to start battle")
            self.click_start()
            print("good luck")
            used_wings+=1
            time.sleep(10)
            self.double_lushen()
            time.sleep(2)
            if used_wings>3:
                self.controller.left_drag()
            print(used_wings)


arena=toArena()
controller=controller()
skills=skills()
lazy=Arena(arena,controller,skills)

lazy.navigate()
lazy.use_wings()
