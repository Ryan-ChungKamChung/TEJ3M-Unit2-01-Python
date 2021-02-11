#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in January 2021
# Program blinks an LED


import board
import digitalio
import time


def main():
    # Blinks a light on and off every second

    led = digitalio.DigitalInOut(board.D13)
    led.direction = digitalio.Direction.OUTPUT

    while True:
        led.value = True
        time.sleep(1)
        led.value = False
        time.sleep(1)


# Makes this file run as the main file of the program, and runs menu_scene()
if __name__ == "__main__":
    main()
