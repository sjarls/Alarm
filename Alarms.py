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
    global alarms, alarmList
    alarms = []
    instanceList = []
    alarmList = []

    def __init__(self, alarm, pri, text):
        self.alarm = alarm
        self.pri = pri
        self.text = text
        self.state = False
        alarms.append(self.alarm)
        Alarm.instanceList.append(self)
    
    def activate(self):
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.state = True
        alarmList.append((self.text, self.pri, timestamp))

    def removeFromList(self, alarmList):
        if self.alarm in [x[0] for x in alarmList]:
            alarmList.remove(self.alarm)
        else:
            print("Could not remove alarm!")

    def printAlarm():
        print(alarmList)
        print("length: ", len(alarmList))

    def loadHistorical():
        f = open("History.txt","r")
        alarmList = f.read()
        f.close()
        return alarmList

    def saveHistorical(alarmList):
        f = open("History.txt","w")
        f.write(str(alarmList))
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
        alarmList = Alarm.loadHistorical()
        alarmList = eval(alarmList)
        startup = False
        
    if keyboard.is_pressed('e'):
        emgStop.activate()
        sleep(1)
    if keyboard.is_pressed('o'):
        overSpeed.activate()
        sleep(1)
    if keyboard.is_pressed('b'):
        batteryLow.activate()
        sleep(1)
    if keyboard.is_pressed('c'):
        connectionSucks.activate()
        sleep(1)
    if keyboard.is_pressed('p'):
        Alarm.printAlarm()
        sleep(1)

    Alarm.saveHistorical(alarmList)