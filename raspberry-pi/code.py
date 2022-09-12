# type: ignore
import board
import digitalio
import time
led = digitalio.DigitalInOut(GP13.LED)
led.direction = digitalio.Direction.OUTPUT
led = digitalio.DigitalInOut(GP18.LED)
led.direction = digitalio.Direction.OUTPUT


led.value = True
led.value = False

while True:
  for x in range (10, 0, -1):
   print(x)
   led.value = True
   time.sleep(1)
   led.value = False
   time.sleep(1)
  print("Lift off")

