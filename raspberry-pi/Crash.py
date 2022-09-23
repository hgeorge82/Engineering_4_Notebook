#type: ignore
import adafruit_mpu6050
import busio

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(GP.15, GP.14)


mpu = adafruit_mpu6050.MPU6050(i2c)
mpu.acceleration
mpu.acceleration[0]
mpu.gyro