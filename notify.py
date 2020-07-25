# library used 'plyer'. Intallation: pip install plyer
from plyer import notification
import os,sys
def notifyx(title = 'JARVIS', message = '', icon = "src\chatbot.ico", time = 5):
    notification.notify(
    title= title,
    message= message,
    app_icon=icon,
    timeout= time)