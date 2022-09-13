# type: ignore
import board
import digitalio
import time
ledred = digitalio.DigitalInOut(board.GP13)
ledred.direction = digitalio.Direction.OUTPUT
ledgreen = digitalio.DigitalInOut(board.GP18)
ledgreen.direction = digitalio.Direction.OUTPUT


for x in range (10, 0, -1):
   if x != 0:
    ledgreen.value = True
    time.sleep(1)
    ledgreen.value = False
    time.sleep(1)
 
   else: 
    print(x)
    ledred.value = False 
    time.sleep(1)
    ledred.value = True
    time.sleep(1)

