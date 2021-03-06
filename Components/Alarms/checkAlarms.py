from Components.Alarms.alarms import Alarms
from Components.Alarms.CallPage.callPage import CallPage
from datetime import date, datetime

class CheckAlarms:
    
    callPage = None    
    alarmFrame = None
    menu = None
    list = None
    frame = None
    
    def __init__(self, frame, alarmFrame, menu, list):
        
        self.frame = frame
        self.alarmFrame = alarmFrame
        self.menu = menu
        self.list = list
        self.callPage = CallPage(self.frame, self.alarmFrame, self.menu, self.list)
    
    def Check(self):
        
        for a in Alarms.alarmsList:
            
            if a.on == True and datetime.now().hour == a.hour and datetime.now().minute == a.minute and (datetime.today().weekday() + 1 in a.days or len(a.days) == 0) and a.played == False:
                
                print("alarm {}:{} --------- {} ............. {}".format(a.hour, a.minute, a.days, a.color))
                self.callPage.ShowCallFrame(a)
                a.played = True
                
                if len(a.days) == 0:
                    
                    a.on = False
                    
            elif a.played == True and datetime.now().minute  == a.minute + 1:
                
                a.played = False
                
                
                
                
        