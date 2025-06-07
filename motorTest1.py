import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

in1 = 17
in2 = 18

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

print("Test 1")
for x in range(100):
    GPIO.output(in1,1)
    GPIO.output(in2,0)
    time.sleep(0.02)
    GPIO.output(in1,0)
    GPIO.output(in2,0)
    time.sleep(0.02)
print("Test 2")
for x in range(100):
    GPIO.output(in1,0)
    GPIO.output(in2,1)
    time.sleep(0.02)
    GPIO.output(in1,0)
    GPIO.output(in2,0)
    time.sleep(0.02)

GPIO.cleanup()