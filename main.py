import pyttsx3, pyautogui as pag
import time, datetime
import os,sys
from notify import notifyx
from launch import launchx

# Initialising Engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

pag.FAILSAFE = False

#OUTPUT
def speak(audio):
    '''
    speaks the argument passed
    '''
    engine.say(audio)
    engine.runAndWait()

def printNspeak(audio):
    '''
    Prints as well as speaks the argument passed to it
    '''
    print(audio)
    engine.say(audio)
    engine.runAndWait()

#code for completing the tasks assigned

def wishMe():
    '''
    Wishes user as per the time
    '''

    hour=int(datetime.datetime.now().hour)

    if hour>=4 and hour<12:
        printNspeak("Good Morning Sir!")

    elif hour>=12 and hour<16:
        printNspeak("Good Afternoon Sir!")

    elif hour>=16 and hour<=20:
        printNspeak("Good Evening Sir!")

    else:
        printNspeak("Good Night Sir!")
    
    notifyx(message= "Sorry sir, My ability of taking voice commands is under development, until then please type the commands.")

def search(txt):
    pag.hotkey("win")
    time.sleep(1)
    pag.typewrite(txt, interval=0.2)

if __name__ == "__main__":
    
    wishMe()
    websites={
        'youtube':'www.youtube.com',
        'google':'www.google.com',
        'facebook':'www.facebook.com',
        'hackerrank':'www.hackerrank.com',
        'leetcode':'www.leetcode.com',
        'instagram':'www.instagram.com',
        'geeksforgeeks':'www.geeksforgeeks.org',
        'wikipedia':'www.wikipedia.org',
        'github': 'www.github.com',
        'linkedin' : 'www.linkedin.com'
        }

    while True:

        query=input("How can I help sir?\n").lower()
        qry=query.split(" ")

        if qry[0]=='open' and qry[1] in websites:
            launchx('chrome', [websites[qry[1]]])

        elif 'on google' in query and 'search' in query:
            query=query.replace('on google', '')
            query=query.replace('search', '')
            launchx('chrome', [query])

            notifyx(message='Search Results are ready.', time = 4)

        elif 'launch' in query:
            query=query.replace('launch','')
            launchx(query)

        elif query in ['create workspace environment', 'workspace environment', 'setup workspace environment', ] :
            from work_space import create_env
            create_env()            
        
        #SEARCH
        elif query=='search':
            search(txt)
            txt=""

        elif 'search' in query:
            query=query.replace('search',"")
            search(query)
        
        #TIME AND SCHEDULES

        elif query in ["what's the time?",'what is the time?','current time','time']:
            notifyx(message=f'The time is {time.strftime("%I:%M")}', time = 4)
            printNspeak(f'The time is {time.strftime("%I:%M")}')

        elif query in["what's the date?",'what is the date?',"today's date",'date']:
            notifyx(message=f'Today is {time.strftime("%d")}', time = 4)
            printNspeak(f'Today is {time.strftime("%d")}')

        #ASSISSTANT CONTROL
        elif query == 'quit' or query == 'stop':
            printNspeak("Exiting Sir. Thank You!")
            break 
        else:
            printNspeak("Sorry Sir, I don't know how to help.")
            printNspeak("Say 'search' to search")
            txt=query