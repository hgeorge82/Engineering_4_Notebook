# type: ignore
import busio
import adafruit_mpu6050
import board
import digitalio
import time

ledred = digitalio.DigitalInOut(board.GP16)
ledred.direction = digitalio.Direction.OUTPUT
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)

while True:
   if mpu.acceleration > 9
   ledred.value 
   time.sleep()
   ledred.value
    