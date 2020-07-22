import pyautogui as pag, time

def launchx(*args):
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






