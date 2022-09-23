# type: ignore
import board
import time

ledPin = 13 

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)
def loop():
    while True:
        print 'LED on'
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(1)
        print 'LED off'
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(1)

