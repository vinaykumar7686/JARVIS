import pyautogui as pag, time
from launch import launchx

def create_env():
    for _ in range(4):
        pag.hotkey('win', 'ctrl', 'left')
    
    # Desktop 1
    launchx('chrome', ['leetcode.com', 'geeksforgeeks.org', 'github.com'])
    
    # Desktop 2
    pag.hotkey('win', 'ctrl', 'right')
    launchx('vscode')

    # Desktop 3
    pag.hotkey('win', 'ctrl', 'right')
    launchx('cmd', ['python'])

    # Desktop 4
    pag.hotkey('win', 'ctrl', 'right')
    launchx('groove')
    pag.hotkey('space')
