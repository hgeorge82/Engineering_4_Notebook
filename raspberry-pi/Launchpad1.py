import time
import board
import digitalio #imports

led = digitalio.DigitalInOut(board.LED) # sets up led
led.direction = digitalio.Direction.OUTPUT  

while True: #loop
    led.value = True  #turns on
    time.sleep(0.5)  
    led.value = False #turns off
    time.sleep(0.5)  
