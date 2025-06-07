import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) #Means using pin number as GPIO pin designation

#Choose GPIO pins to use
TRIG1 = 11 #Pins for first sensor
ECHO1 = 12

TRIG2 = 13 #Pins for second sensor
ECHO2 = 15

#Settup GPIO pins
GPIO.setup(TRIG1, GPIO.OUT) #Trig is the signal being sent to activate the sensor, so it is an OUT signal.
GPIO.setup(ECHO1, GPIO.IN)  #Echo is the returning data being recieved from the sensor, so it is an IN signal.

GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)

#Ensures the sensors are off (in 2 different ways)
GPIO.output(TRIG1, False)
GPIO.output(TRIG2, 0)
time.sleep(0.2) #Why do we do this??

#Measures data by sending signal to sensor 1, gathering data, and turning off sensor.
GPIO.output(TRIG1, True)
time.sleep(0.00001)
GPIO.output(TRIG1, False)

#Marks???
while GPIO.input(ECHO1)==0:
    startTime1 = time.time()
    
while GPIO.input(ECHO1)==1:
    stopTime1 = time.time()

#Measures data by sending signal to sensor 2, gathering data, and turning off sensor.
GPIO.output(TRIG2, 1)
time.sleep(0.00001)
GPIO.output(TRIG2, 0)

#Marks???
while GPIO.input(ECHO2)==0:
    startTime2 = time.time()
    
while GPIO.input(ECHO2)==1:
    stopTime2 = time.time()

#Calculates the distance for both sensors using the distance formula and the times found above
print("First sensors distance: ", (stopTime1 - startTime1) * 17000)
print("Second sensors distance: ", (stopTime2 - startTime2) * 17000)

GPIO.cleanup()