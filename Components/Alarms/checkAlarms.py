from Components.Alarms.alarms import Alarms
from datetime import date, datetime

class CheckAlarms:
    
    def Check():
        
        for a in Alarms.alarmsList:
            
            if a.on == True and datetime.now().hour == a.hour and datetime.now().minute == a.minute:
                
                print("alarm {}:{}".format(a.hour, a.minute))
        