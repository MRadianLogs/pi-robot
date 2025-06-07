import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

TRIG = 13
ECHO = 15

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)

time.sleep(0.2)

print("Starting Measurement")
    
GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
    start = time.time()

while GPIO.input(ECHO)==1:
    stop = time.time()
    
print((stop - start) * 17000)


GPIO.cleanup()