from time import sleep
import keyboard

'''
This class can be used to construct alarms with the following properties:
    Str: Variable name
    Str: Alarm priority [high/low] (Could consider using integers)
    Str: Alarm text

The following methods are available outside the class
    Alarms are stored in alarmListHigh and alarmListLow
    
    activate() -> modifies the alarmstate to True and adds alarm to alarm list
    reset() -> modifies the alarmstate to False and removes alarm from alarm list
    printAlarm() -> prints the list of alarms (timestamps and more to be added)

Intended usage:
    For DART: construct alarms and display alarm text, priority and timestamp to Qt UI

TO DO:
    Alarm timestamps
    Historical alarms/retreive alarms after reboot
    Remove sleep calls (for simulation with keyboard only)
    ++
    +
'''

alarmListHigh = []
alarmListLow = []

class Alarm():
    def __init__(self, alarm, pri, text):
        self.alarm = alarm
        self.pri = pri
        self.text = text
        self.state = False
    
    def activate(self):
        self.state = True
        if self.pri == "high":
            self.__addToList(alarmListHigh)
        elif self.pri == "low":
            self.__addToList(alarmListLow)
        
        sleep(1)
        self.printAlarm()

    def reset(self):
        self.state = False
        if self.pri == "high":
            self.__removeFromList(alarmListHigh)
        elif self.pri == "low":
            self.__removeFromList(alarmListLow)

        sleep(1)
        self.printAlarm()

    def __addToList(self, alarmList):
        tmpExists = False
        if len(alarmList) == 0:
            alarmList.append(self.alarm)
        else:
            for i in range(len(alarmList)):
                if self.alarm == alarmList[i]:
                    tmpExists = True
                    print("Alarm already in list")
                    break
            if tmpExists != True:
                alarmList.append(self.alarm)
                tmpExists = False

    def __removeFromList(self, alarmList):
        tmpExists = False
        for i in range(len(alarmList)):
            if self.alarm == alarmList[i]:
                tmpExists = True
                alarmList.remove(self.alarm)
                break
        if tmpExists != True:
            print("Could not remove alarm!")

    def printAlarm(self):
        print("Low: ", alarmListLow)
        print("High: ", alarmListHigh)

emgStop = Alarm("emgStop", "high", "Emg Stop Activated")
overSpeed = Alarm("overSpeed", "high", "Overspeed detected!")
batteryLow = Alarm("batteryLow", "low", "Battery level low")
connectionSucks = Alarm("connectionSucks", "low", "Bad connection")

# Simualte alarms
while True:
    if keyboard.is_pressed('e'):  
        emgStop.activate()
    if keyboard.is_pressed('o'):
        overSpeed.activate()
    if keyboard.is_pressed('b'):
        batteryLow.activate()
    if keyboard.is_pressed('c'):
        connectionSucks.activate()
    if keyboard.is_pressed('r'):
        emgStop.reset()