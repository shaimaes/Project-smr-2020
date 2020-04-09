
import time
from gpiozero import LED
from time import sleep
from people_counter import totalUp
from people_counter import totalDown

# Define the serial port and baud rate.
# Ensure the 'COM#' corresponds to what was seen in the Windows Device Manager
led_red = LED(17)
led_green = LED(16)
time.sleep(2) #wait for 2 secounds for the communication to get established


while True :
    if (totalUp - totalDown == 4):
        led_red.on()
        led_green.off()
        print("LED_Red turned ON")
        sleep(1)
    else:
        led_green.on()
        led_red.off()
        print("LED_Green turned ON")
        sleep(1)
        break
