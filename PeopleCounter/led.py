
#import time
import cv2
from gpiozero import LED
from time import sleep
from PeopleCounter import cnt_up
from PeopleCounter import cnt_down

# Define the serial port and baud rate.
# Ensure the 'COM#' corresponds to what was seen in the Windows Device Manager
led_red = LED(17)
led_green = LED(16)
sleep(2) #wait for 2 secounds for the communication to get established


while True :
    if (cnt_up - cnt_down == 4):
        led_red.on()
        led_green.off()
        print("LED_Red turned ON")
        sleep(1)
    else:
        led_green.on()
        led_red.off()
        print("LED_Green turned ON")
        sleep(1)
