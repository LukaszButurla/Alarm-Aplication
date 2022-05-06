class Alarms:
    
    alarmsList = []
    
    def __init__(self, on, hour, minute, day, repeat, description):        
        
        self.on = on
        self.hour = hour
        self.minute = minute
        self.day = day
        self.repeat = repeat
        self.description = description
        self.alarmsList.append(self)
        
        
alarm = Alarms(True, 10, 20, 1, False, "Test")
alarmm = Alarms(False, 12, 20, 2, False, "test dasdasdaasdasdad")
