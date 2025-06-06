import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)


en1 = 18
in1 = 15
in2 = 14

GPIO.setup(en1, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.output(en1, 1)

while True:
        for x in range(100):
            GPIO.output(in1, 1)
            GPIO.output(in2, 0)
            time.sleep(0.04)
            GPIO.output(in1, 0)
            GPIO.output(in2, 0)
            time.sleep(0.02)
        time.sleep(3)

        for x in range(100):
            GPIO.output(in2, 1)
            GPIO.output(in1, 0)
            time.sleep(0.04)
            GPIO.output(in2, 0)
            GPIO.output(in1, 0)
            time.sleep(0.02)
        time.sleep(3)
        
GPIO.cleanup()