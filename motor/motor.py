import time
import RPi.GPIO as GPIO
#choose BCM or BOARD
#GPIO.setmode(GPIO.BOARD) #(e.g. P1)
GPIO.setmode(GPIO.BCM) # numbers after "GPIO"
GPIO.setup(23, GPIO.OUT)

p = GPIO.PWM(23, 50) # GPIO 角位=23 頻率=50Hz
p.start(0)
listPWM=[5,7.5,10]
try:
    while 1:
        for dc in listPWM:
            p.ChangeDutyCycle(dc)
            time.sleep(1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()