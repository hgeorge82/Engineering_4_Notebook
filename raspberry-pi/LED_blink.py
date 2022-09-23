#type: ignore
import board
import digitalio
import time
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True 
led.value = False
time.sleep(1)
print("kfkjsfkj")