import pyautogui


def forward():
    pyautogui.press('right')
def backward():
    pyautogui.press('left')

def speedup():
    pyautogui.press('>')
def speeddown():
    pyautogui.press('<')