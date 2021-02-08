#Schaltet Ventilator AN
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

# init pin numbers

pinList = [18]

# through pins and set mode and state to 'high'

for i in pinList: 
    GPIO.setup(18, GPIO.OUT) 
    GPIO.output(18, GPIO.HIGH)

# main

try:
  GPIO.output(18, GPIO.LOW)
  print "Ventilator AN"

# End program cleanly with keyboard
except KeyboardInterrupt:

  # Reset GPIO settings
  GPIO.cleanup()
