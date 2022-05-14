from Components.Alarms.alarms import Alarms
from Components.Alarms.CallPage.callPage import CallPage
from datetime import date, datetime

class CheckAlarms:
    
    callPage = None    
    frame = None
    
    def __init__(self, frame):
        
        self.frame = frame
        self.callPage = CallPage(self.frame)
    
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
                
                
                
                
        