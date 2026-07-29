import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led_pin = 26

GPIO.setup(led_pin, GPIO.OUT)
flashing = True
while flashing:
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led_pin, GPIO.LOW)
    time.sleep(1)