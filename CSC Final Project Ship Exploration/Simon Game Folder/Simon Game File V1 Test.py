import RPi.GPIO as GPIO
from time import sleep
import pygame

pygame.init()

leds = [4, 17, 22, 5]
sounds = [pygame.mixer.Sound("one.wav"),
          pygame.mixer.Sound("two.wav"),
          pygame.mixer.Sound("three.wav"),
          pygame.mixer.Sound("four.wav")]

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)

print "Watch the LEDs light with sound!"
for i in range(len(leds)):
    GPIO.output(leds[i], True)
    sounds[i].play()
    sleep(1)
    GPIO.output(leds[i], False)
    sleep(0.5)
print "Sionara!"
GPIO.cleanup()
