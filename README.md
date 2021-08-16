# Alarm

Class for making alarms for robotic systems.
Instanciate alarms with alarm name, alarm text and priority (high/low).

Alarms are activated with <instance>.activate()

The alarm list is stored in History.txt and are saved every desired interval and returned upon startup.
Alarm info is stored in a tuple:
  (Alarm Text, Priority, Date and Time of event)
