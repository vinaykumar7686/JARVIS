import pyautogui as pag, time

def switch_desktop(desktop):
    '''
    Assumption: Maximum desktops currently active  =  4
    '''
    for _ in range(4):
        pag.hotkey('win', 'ctrl', 'left')
    
    for _ in range(desktop-1):
        pag.hotkey('win', 'ctrl', 'right')

def launchx(*args, desktop = 0):
    '''
    Method to launch application or local files by searching fo them in windows search.
    Arguments:
    application and commands/websites if any
    Desktop: Desktop Count in which application is to be launched.(Assumption: Max Active desktop = 4)
    '''
    if not desktop == 0:
        switch_desktop(desktop)
    
    args = list(args)
    app = args[0]

    pag.hotkey('win')
    time.sleep(2)

    pag.typewrite(app)
    time.sleep(3)

    pag.hotkey('enter')
    pag.sleep(5)

    # Maximise window
    pag.hotkey('win', 'up')
    pag.hotkey('win', 'up')

    if app == 'chrome':
        # for case if no website is passed
        args.append(['google'])

        for i, site in enumerate(args[1]):
            
            pag.typewrite(site)
            pag.hotkey('enter')
            time.sleep(1)
            if i<(len(args[1])-1):
                pag.hotkey('ctrl','t')
    
    if app in ['cmd', 'dos']:
        # for case when no command is passed
        args.append('')

        for command in args[1]:
            pag.typewrite(command)
            pag.hotkey('enter')
            time.sleep(1)
        
if __name__ == "__main__":
    launchx('chrome',['geeksforgeeks', 'github'], desktop=2)