import RPi.GPIO as GPIO
from time import sleep
import pygame

pygame.init()

switches = [23, 18, 24, 25]
leds = [4, 17, 22, 5]
sounds = [ pygame.mixer.Sound("one.wav"),
           pygame.mixer.Sound("two.wav"),
           pygame.mixer.Sound("three.wav"),
           pygame.mixer.Sound("four.wav") ]

GPIO.setmode(GPIO.BCM)

GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leds, GPIO.OUT)

print "Press the switches or Ctrl+C to exit..."

try:
    while (True):
        pressed = False

        while (not pressed):
            for i in range(len(switches)):
                while (GPIO.input(switches[i]) == True):
                    val = i
                    pressed = True

        GPIO.output(leds[val], True)
        sounds[val].play()
        sleep(1)
        GPIO.output(leds[val], False)
        sleep(0.25)

except KeyboardInterrupt:
    GPIO.cleanup()
    print "\nSionara!"
