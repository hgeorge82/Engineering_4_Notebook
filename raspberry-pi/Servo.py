# type: ignore
import board 
import digitalio
import time
import pwmio
from adafruit_motor import servo #imports code from adafruit_motor library. 


ledgreen = digitalio.DigitalInOut(board.GP18) #defining of the led lights
ledgreen.direction = digitalio.Direction.OUTPUT
ledred = digitalio.DigitalInOut(board.GP13)
ledred.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP16) #defining of the button
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN


pwm_servo = pwmio.PWMOut(board.GP17, duty_cycle=2 ** 15, frequency=50) #powersource for the servo
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500) #tells what direction for the servo to go


servo1.angle = 0 # servo starts out as zero before loop is called


while True: 
  if button.value == True: #when button is pressed 
    for x in range (10, -1, -1): #calls values for countdown(index)
      if x != 0: 
        ledred.value = True
        print(x)
        time.sleep(0.5)
        ledred.value = False
        time.sleep(0.5)
      
      
      else: # x doesn't equal zero so the else statemnet runs
        print("Liftoff!")
        ledgreen.value = False 
        print(x)
        time.sleep(0.5)
        ledgreen.value = True
        time.sleep(0.5)
        servo1.angle = 180
