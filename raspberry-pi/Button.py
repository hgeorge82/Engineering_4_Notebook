# type: ignore
import board
import digitalio
import time
ledgreen = digitalio.DigitalInOut(board.GP18)
ledgreen.direction = digitalio.Direction.OUTPUT
ledred = digitalio.DigitalInOut(board.GP13)
ledred.direction = digitalio.Direction.OUTPUT
button.pull = digital.Pull.UP


if button == True:
   for x in range (10, 0, -1):
     if x != 0:
      ledred.value = True
      print(x)
      time.sleep(1)
      ledred.value = False
      time.sleep(1)