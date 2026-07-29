import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin = 26

GPIO.setup(18, GPIO.OUT)
flashing = True
while flashing:
    GPIO.output(18, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(18, GPIO.LOW)