from time import sleep
import keyboard
from datetime import datetime

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
    Historical alarms/retreive alarms after reboot
    Remove sleep calls (for simulation with keyboard only)
    ++
    +
'''

class Alarm():
    global alarmListHigh, alarmListLow, alarms
    alarms = []
    instanceList = []
    alarmListHigh = []
    alarmListLow = []

    def __init__(self, alarm, pri, text, *triggers):
        self.alarm = alarm
        self.pri = pri
        self.text = text
        self.state = False
        self.triggers = []
        for trigger in triggers:
            self.triggers.append(trigger)
        alarms.append(self.alarm)
        Alarm.instanceList.append(self)
    
    def activate(self, timestamp):
        self.state = True
        sleep(1)
        if self.pri == "high":
            self.addToList(alarmListHigh, timestamp)
        elif self.pri == "low":
            self.addToList(alarmListLow, timestamp)

    def reset(self):
        self.state = False
        if self.pri == "high":
            self.removeFromList(alarmListHigh)
        elif self.pri == "low":
            self.removeFromList(alarmListLow)

    def addToList(self, alarmList, timestamp):
        if len(alarmList) == 0:
            alarmList.append((self.alarm, timestamp))
            print("Alarm Activated!")
        else:
            if self.alarm in [x[0] for x in alarmList]:
                print("Alarm already in list")
            else:
                alarmList.append((self.alarm, timestamp))
                print("Alarm Activated!")

    def removeFromList(self, alarmList):
        self.state = False
        if self.pri == "high":
            if self.alarm in alarmList:
                alarmList.remove(self.alarm)
            else:
                print("Could not remove alarm!")

    def printAlarm(self):
        print("Low: ", alarmListLow)
        print("High: ", alarmListHigh)

trigger1 = False
trigger2 = False
trigger3 = False

# Define Alarm Instances
emgStop = Alarm("emgStop", "high", "Emg Stop Activated")
overSpeed = Alarm("overSpeed", "high", "Overspeed detected!")
batteryLow = Alarm("batteryLow", "low", "Battery level low")
connectionSucks = Alarm("connectionSucks", "low", "Bad connection")

# Simualte alarms
while True:
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    if keyboard.is_pressed('e'):
        emgStop.activate(timestamp)
    if keyboard.is_pressed('o'):
        overSpeed.activate(timestamp)
    if keyboard.is_pressed('b'):
        batteryLow.activate(timestamp)
    if keyboard.is_pressed('c'):
        connectionSucks.activate(timestamp)
    if keyboard.is_pressed('r'):
        emgStop.reset()
    if keyboard.is_pressed('p'):
        print(alarmListHigh, "\t", alarmListLow)