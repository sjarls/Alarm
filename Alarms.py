from time import sleep
import keyboard
from datetime import datetime

'''
TO DO:
    Make only one list: alarmList, ditch the high/low stuff
    Add high/low info to the alarm list tuple entry
    Sort alarm by time or priority
    Acknowledge alarm
    Max numbers of events
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
    
    def activate(self):
        timestamp = getTime()
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
        alarmList.append((self.text, self.pri, timestamp))

    def removeFromList(self, alarmList):
        if self.alarm in [x[0] for x in alarmList]:
            alarmList.remove(self.alarm)
        else:
            print("Could not remove alarm!")

    def printAlarm():
        print("Low: ", alarmListLow)
        print("High: ", alarmListHigh)
        sleep(1)

def getTime():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def loadHistorical():
    f = open("History.txt","r")
    alarmListHigh = f.read()
    f.close()
    return alarmListHigh

def saveHistorical(alarmListHigh):
    f = open("History.txt","w")
    f.write(str(alarmListHigh))
    f.close()

# Define Alarm Instances
emgStop = Alarm("emgStop", "high", "Emergency Stop Activated")
overSpeed = Alarm("overSpeed", "high", "Overspeed detected!")
batteryLow = Alarm("batteryLow", "low", "Battery level low")
connectionSucks = Alarm("connectionSucks", "low", "Bad connection")

startup = True

# Simualte alarms
while True:
    if startup:
        alarmListHigh = loadHistorical()
        alarmListHigh = eval(alarmListHigh)
        startup = False
        
    if keyboard.is_pressed('e'):
        emgStop.activate()
    if keyboard.is_pressed('o'):
        overSpeed.activate()
    if keyboard.is_pressed('b'):
        batteryLow.activate()
    if keyboard.is_pressed('c'):
        connectionSucks.activate()
    if keyboard.is_pressed('p'):
        Alarm.printAlarm()

    saveHistorical(alarmListHigh)