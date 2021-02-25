# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 23:52:44 2021

@author: Mueed
"""

import pyautogui, time
time.sleep(10)
f = open("file.txt" , 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    
    
