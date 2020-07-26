import pyautogui as pag, time
from launch import launchx
from notify import notifyx

def create_env():
    notifyx(message="Sir, you can get a glass of water, till then I will make sure that your setup is ready for use." , time = 8)

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

    notifyx(message="Your workspace environment is ready. Let's get onto the work.", time = 4)

if __name__ == "__main__":
    create_env()
