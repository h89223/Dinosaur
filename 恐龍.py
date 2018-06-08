############### made by 林逸倫 ####################
from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    playBtn = (470,390)
    dinasaur = (237,391) #圖位置

#開始
def restartGame():
    pyautogui.click(Cordinates.playBtn)
    pyautogui.keyDown('down')
    print('開始!')

#跳
def pressSapce():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    print('跳')
    time.sleep(0.15)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

#出現座標 300 290 tree ,420 bird
def imageGrab():
    box = (Cordinates.dinasaur[0]+65, Cordinates.dinasaur[1],
           Cordinates.dinasaur[0]+165, Cordinates.dinasaur[1]+5)
    image = ImageGrab.grab(box) #抓取範圍中的圖
    grayImage = ImageOps.grayscale(image)     
    a = array(grayImage.getcolors())
    print(a.sum())  #圖中顏色點數
    return a.sum()

#while True:
#    imageGrab()

#點數和 1647

def main():
    restartGame()
    while True:
         if(imageGrab()!=747):
             pressSapce()
           

main()




restartGame()
time.sleep(1)
pressSapce()


