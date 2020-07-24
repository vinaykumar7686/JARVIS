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
    pag.hotkey('win', 'down')
    pag.hotkey('win', 'down')

    launchx('notes.txt')

    # Moveback to Desktop 1
    time.sleep(2)
    for _ in range(4):
        pag.hotkey('win', 'ctrl', 'left')

if __name__ == "__main__":
    create_env()
