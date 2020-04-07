
import serial
import time

# Define the serial port and baud rate.
# Ensure the 'COM#' corresponds to what was seen in the Windows Device Manager
ser = serial.Serial('COM4', 9600)
time.sleep(2) #wait for 2 secounds for the communication to get established

while True :
    if (totalUp - totalDown == 4):
        ser.write('0')
        print("LED_Red turned ON")
        time.sleep(1)
    else:
        ser.write('1')
        print("LED_Green turned ON")
        time.sleep(1)
        break