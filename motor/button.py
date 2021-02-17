import RPi.GPIO as GPIO   
import time   

GPIO.setmode(GPIO.BOARD)   
GPIO.setup(13, GPIO.IN)

while True:
    inputValue = GPIO.input(13)
    if inputValue == False:
        print("Button pressed ")
        time.sleep(0.5)
  
