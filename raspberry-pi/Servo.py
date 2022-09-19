# type: ignore
import board
import digitalio
import time
import pwmio
from adafruit_motor import servo


ledgreen = digitalio.DigitalInOut(board.GP18)
ledgreen.direction = digitalio.Direction.OUTPUT
ledred = digitalio.DigitalInOut(board.GP13)
ledred.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP16)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

servo1.angle = 0
servoname.angle = desired_angle


pwm_servo = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)


while True: 
  if button.value == True:
    for x in range (10, 0, -1):
      if x != 0:
        ledred.value = True
        print(x)
        time.sleep(0.5)
        ledred.value = False
        time.sleep(0.5)
      
      
      else: 
        print("Liftoff!")
        ledgreen.value = False 
        print(x)
        time.sleep(0.5)
        ledgreen.value = True
        time.sleep(0.5)
