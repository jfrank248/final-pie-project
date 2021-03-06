import RPi.GPIO as GPIO
from time import sleep
from random import randint
import pygame

# set to True to enable debugging output
DEBUG = False

# initialize the pygame library
pygame.init()

switches = [23, 18, 24, 25]
leds = [4, 17, 22, 5]
sounds = [pygame.mixer.Sound("one.wav"),
          pygame.mixer.Sound("two.wav"),
          pygame.mixer.Sound("three.wav"),
          pygame.mixer.Sound("four.wav")]

GPIO.setmode(GPIO.BCM)

GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leds, GPIO.OUT)

def lose():
    for i in range(0, 4):
        GPIO.output(leds, True)
        sleep(0.5)
        GPIO.output(leds, False)
        sleep(0.5)

seq = []
seq.append(randint(0, 3))
seq.append(randint(0, 3))

print "Welcome to Simon!"
print "Try to play the sequence back by pressing the switches."
print "Press Ctrl+C to exit..."

try:
    while(True):
        seq.append(randint(0,3))
        if (DEBUG):
            print seq

        for s in seq:
            GPIO.output(leds[s], True)
            sounds[s].play()
            sleep(1)
            GPIO.output(leds[s], False)
            sleep(0.5)

        count = 0

        while (count < len(seq)):
            pressed = False

            while (not pressed):
                for i in rang(len(switches)):
                    while (GPIO.input(switches[i]) == True):
                        val = i
                        pressed = True
            if (DEBUG):
                print val

            GPIO.output(leds[val], True)
            sounds[val].play()
            sleep(1)
            GPIO.output(leds[val], False)
            sleep(0.25)

            if (val != seq[count]):
                lose()

                GPIO.cleanup()

                exit(0)

            count += 1

except KeyboardInterrupt:
    GPIO.cleanup()
 
