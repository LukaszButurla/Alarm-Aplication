class Alarms:
    
    alarmsList = []
    
    def __init__(self, on, hour, minute, days, repeat, description, color, played, snoozeTime):        
        
        self.on = on
        self.hour = hour
        self.minute = minute
        self.days = days
        self.repeat = repeat
        self.description = description
        self.color = color
        self.played = played
        self.snoozeTime = snoozeTime
        self.alarmsList.append(self)        

