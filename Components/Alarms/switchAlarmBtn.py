class SwitchBtn:
    
    def __init__(self):
        
        pass
    
    def Switch(self, alarm):
        
        print("switch")        
        print(alarm)
        
        if alarm.on == True:
            
            alarm.on = False
            print("false")
        
        elif alarm.on == False:
            
            alarm.on = True
            print("true")