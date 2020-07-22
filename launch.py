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

    if app == 'chrome':
        # for case if no website is passed
        args.append(['google'])

        for i, site in enumerate(args[1]):
            
            pag.typewrite(site)
            pag.hotkey('enter')
            time.sleep(1)
            if i<(len(args[1])-1):
                pag.hotkey('ctrl','t')






