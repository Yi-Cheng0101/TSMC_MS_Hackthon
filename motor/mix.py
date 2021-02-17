import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)  
GPIO.setup(16, GPIO.OUT)
GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.IN)

p = GPIO.PWM(16, 50)
p.start(0)

dc = 5
p.ChangeDutyCycle(dc)
try:
    while 1:
        inputValue1 = GPIO.input(11)
        inputValue2 = GPIO.input(13)
        if inputValue1 == False and dc < 8:
            dc += 1
            p.ChangeDutyCycle(dc)
            print("Button pressed 1", dc)
        elif inputValue2 == False and dc > 3:
            dc -= 1
            p.ChangeDutyCycle(dc)
            print("Button pressed 2", dc)
        time.sleep(0.5)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()