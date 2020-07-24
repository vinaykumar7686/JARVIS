# library used 'plyer'. Intallation: pip install plyer
from plyer import notification
import os,sys
def notify(title = '', message = '', icon = None, time = 3):
    notification.notify(
    title='This is Title',
    message='This is message',
    app_icon=None,
    timeout=3)
