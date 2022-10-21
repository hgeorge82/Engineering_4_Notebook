# type: ignore
import board ##
import digitalio ##
import time ## 
ledgreen = digitalio.DigitalInOut(board.GP18) ## 
ledgreen.direction = digitalio.Direction.OUTPUT
ledred = digitalio.DigitalInOut(board.GP13)
ledred.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP16) #
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN


while True: # 
  if button.value == True:
    for x in range (10, -1, -1): #
      if x != 0: #
        ledred.value = True
        print(x)
        time.sleep(0.5)
        ledred.value = False
        time.sleep(0.5)
      
       
      else: #
        print("Liftoff!")
        ledgreen.value = True
        print(x)
        time.sleep(0.5)
        ledgreen.value = False
        time.sleep(0.5)
