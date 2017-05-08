##############################################
#Name: Collin Corbett, Jonathan Frank, John Do
#Date: 5/2/17
#Description: Working Sample for Friday Class
##############################################

################
#Pre-GUI Sample
#Pre-Game Sample
################

############################################################################
#Notes:
#This segment of the code is for in class testing purposes only.
#The full file will implement a puzzle for Cyber Storm participants
#as well as a GUI to make the reading of statements and inputing responses
#easier and smoother. Currently the puzzle for the code is being reformatted
#and the GUI is still under construciton.
############################################################################

############################################################################
#Test Code Structure:
#1)Print Statement to give the user background knowledge to the activity,
#and build a mock situation to aid in immersion.
#2)Delay before the User input is displayed. (User input will only take
#the password that is generated in the Random Password Generator Class.)
#3)A User input that will redirect to the Simon Sequence. (In the final
#version of the code this User input will redirect to the puzzle, upon
#completion of the puzzle the user will be redirected to the Simon Sequence).
#4)Upon completion of the Simon Sequence the password will be displayed.
#5)User input for password will reappear.
#6)After password is correctly inputted a print statement closing the game
#will appear. Points will be displayed, and a game or file will be opened
#to act as a "reward".
#7)End.
############################################################################


############################################################################
#Begin Code
############################################################################

########
#imports
########
import random
import RPi.GPIO as GPIO
from time import sleep
from random import randint
import pygame
from pygame.locals import * #pong v1.0; demonstration purposes only
from sys import exit #pong v1.0; demonstration purposes only


#################################################
#Global Variable Used to track the Simon Sequence
#Note: We will have to implement a way to start
#back at the beginning of the Simon Sequence as
#many times as necessary so that the password
#can be obtained should the user input the simon
#sequence incorrectly on their first try.
#################################################
myGlobal = 0
myGlobalTries = 3
#################################################



####################################
#Function for the Password Generator
####################################
def RandPassGen():
    characters = "abcdefghijklmnopqrstuvwxyz"
    upperchar = characters.upper()
    pass_len = 20 #sets the password to be (x) characters long
    passlist = []

    for i in range(pass_len//3):
        passlist.append(characters[random.randrange(len(characters))])
        passlist.append(upperchar[random.randrange(len(upperchar))])
        passlist.append(str(random.randrange(10)))
    for i in range(pass_len-len(passlist)):
        passlist.append(characters[random.randrange(len(characters))])

    random.shuffle(passlist)
    pwstring = "".join(passlist)

    return(pwstring)

################################################
#Function for the Simon Sequence
#(Recycled Simon Game, Requires further editing)
################################################
def SimonGameSeq():
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
        print "You survived for {} rounds!".format(myGlobal) #this should display how many rounds you have survived
        #add code here that will cause all sounds to play
        sounds[one].play()#this should cause the sounds to play, needs to be tested
        sleep(1)#
        sounds[two].play()#
        sleep(.75)#
        sounds[3].play()#
        sleep(.50)#
        sounds[4].play()#
        sleep(.25)#

        
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
                
                if count < 1:
                    
                    GPIO.output(leds[val], True)
                    sounds[val].play()
                    sleep(1)
                    GPIO.output(leds[val], False)
                    sleep(0.25)

                else:
                    GPIO.output(leds[val], True)
                    sounds[val].play()
                    sleep(0.5)
                    GPIO.output(leds[val], False)
                    sleep(0.13)

                if (val != seq[count]):
                    lose()

                    GPIO.cleanup()

                    exit(0)

                count += 1
                myGlobal += 1 #Print this value at loss of game
                

    except KeyboardInterrupt:
        GPIO.cleanup()




#function for Password input
def PassReq():
    password = input('Weapons Systems Password: ')
    if password == RandPassGen():
        print('Password {} Accpeted! Firing Weapons Systems!'.format(password))
        EndGame()
    else:
        print "Incorrect password. You have {} tries remaining!".format(myGlobalTries)
        password = input('Weapons Systems Password: ')
        myGlobalTries -= 1

def death():
    print " " * 17 + "u" * 7
    print " " * 13 + "u" * 2 + "$" * 11 + "u" * 2
    print " " * 10 + "u" * 2 + "$" * 17 + "u" * 2
    print " " * 9 + "u" + "$" * 21 + "u"
    print " " * 8 + "u" + "$" * 23 + "u"
    print " " * 7 + "u" + "$" * 25 + "u"
    print " " * 7 + "u" + "$" * 25 + "u"
    print " " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$" * 3 +\
"\"" + " " * 3 + "\"" + "$" * 6 + "u"
    print " " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7\
+ "$" * 4 + "\""
    print " " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 + "u" +\
"$" * 3
    print " " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 + "u" + "\
" * 6 + "u" + "$" * 3
    print " " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3 +\
"$" * 3 + "u" * 2 + "$" * 4 + "\""
    print " " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" + "$" * 7\
+ "\""
    print " " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u"
    print " " * 13 + "u$\"$\"$\"$\"$\"$\"$u"
    print " " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u" + "$"\
* 2 + " " * 7 + "u" * 3
    print " u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3 + "\
" * 7 + "u" + "$" * 4
    print " " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9 +\
"\"" + " " * 5 + "u" * 2 + "$" * 6
    print "u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " * 4 +\
"u" * 4 + "$" * 10
    print "$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 + "u" * 2\
+ "$" * 9 + "\"" * 3 + "$" * 3 + "\""
    print " " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" * 2 +\
" " + "\"" * 2 + "$" + "\"" * 3
    print " " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3
    print " " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2 +\
" \"\"" + "$" * 11 + "u" * 3 + "$" * 3
    print " " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" + "$" *\
11 + "\""
    print " " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" + "$" *\
4 + "\"\""
    print " " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\""


###############################################################
#End Game Function
#(Will either be a game or a function, Pong V1.0 will be used
#for in class demonstration purposes. All credit goes to its
#original author, as this is simply a place holder to demonstrate
#working code. The final version of the code will be original.)
###############################################################

def EndGame():
    pygame.init()

    screen=pygame.display.set_mode((640,480),0,32)
    pygame.display.set_caption("Pong Pong!")

    #Creating 2 bars, a ball and background.
    back = pygame.Surface((640,480))
    background = back.convert()
    background.fill((0,0,0))
    bar = pygame.Surface((10,50))
    bar1 = bar.convert()
    bar1.fill((0,0,255))
    bar2 = bar.convert()
    bar2.fill((255,0,0))
    circ_sur = pygame.Surface((15,15))
    circ = pygame.draw.circle(circ_sur,(0,255,0),(15/2,15/2),15/2)
    circle = circ_sur.convert()
    circle.set_colorkey((0,0,0))

    # some definitions
    bar1_x, bar2_x = 10. , 620.
    bar1_y, bar2_y = 215. , 215.
    circle_x, circle_y = 307.5, 232.5
    bar1_move, bar2_move = 0. , 0.
    speed_x, speed_y, speed_circ = 250., 250., 250.
    bar1_score, bar2_score = 0,0
    #clock and font objects
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("calibri",40)

    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    bar1_move = -ai_speed
                elif event.key == K_DOWN:
                    bar1_move = ai_speed
            elif event.type == KEYUP:
                if event.key == K_UP:
                    bar1_move = 0.
                elif event.key == K_DOWN:
                    bar1_move = 0.
        
        score1 = font.render(str(bar1_score), True,(255,255,255))
        score2 = font.render(str(bar2_score), True,(255,255,255))

        screen.blit(background,(0,0))
        frame = pygame.draw.rect(screen,(255,255,255),Rect((5,5),(630,470)),2)
        middle_line = pygame.draw.aaline(screen,(255,255,255),(330,5),(330,475))
        screen.blit(bar1,(bar1_x,bar1_y))
        screen.blit(bar2,(bar2_x,bar2_y))
        screen.blit(circle,(circle_x,circle_y))
        screen.blit(score1,(250.,210.))
        screen.blit(score2,(380.,210.))

        bar1_y += bar1_move
        
    # movement of circle
        time_passed = clock.tick(30)
        time_sec = time_passed / 1000.0
        
        circle_x += speed_x * time_sec
        circle_y += speed_y * time_sec
        ai_speed = speed_circ * time_sec
    #AI of the computer.
        if circle_x >= 305.:
            if not bar2_y == circle_y + 7.5:
                if bar2_y < circle_y + 7.5:
                    bar2_y += ai_speed
                if  bar2_y > circle_y - 42.5:
                    bar2_y -= ai_speed
            else:
                bar2_y == circle_y + 7.5
        
        if bar1_y >= 420.: bar1_y = 420.
        elif bar1_y <= 10. : bar1_y = 10.
        if bar2_y >= 420.: bar2_y = 420.
        elif bar2_y <= 10.: bar2_y = 10.
    #since i don't know anything about collision, ball hitting bars goes like this.
        if circle_x <= bar1_x + 10.:
            if circle_y >= bar1_y - 7.5 and circle_y <= bar1_y + 42.5:
                circle_x = 20.
                speed_x = -speed_x
        if circle_x >= bar2_x - 15.:
            if circle_y >= bar2_y - 7.5 and circle_y <= bar2_y + 42.5:
                circle_x = 605.
                speed_x = -speed_x
        if circle_x < 5.:
            bar2_score += 1
            circle_x, circle_y = 320., 232.5
            bar1_y,bar_2_y = 215., 215.
        elif circle_x > 620.:
            bar1_score += 1
            circle_x, circle_y = 307.5, 232.5
            bar1_y, bar2_y = 215., 215.
        if circle_y <= 10.:
            speed_y = -speed_y
            circle_y = 10.
        elif circle_y >= 457.5:
            speed_y = -speed_y
            circle_y = 457.5

        pygame.display.update()

######################
#Main Part of the code
######################

print """ Good Day Captain. Today is xx/xx/xxxx. The invasion of Earth as begun.
As Martian High Commander it is your duty to lead the Armada, but before we can
attack we must reactivate our long dormant weapons systems. The process is tedious
but without it we can not accomplish our mission. Your are our only hope. Activate
the weapons systems and destroy the puny earthlings, but be careful. If the weapons
system password is keyed incorrectly three times the ship will self-destruct.
It is a foolish concept we know, but it was implemented by the Mar's High
Council to prevent espionage and terror attacks. Good luck Captain! Note: Type
"Command Override. Password Recovery." to progress deeper into the game when
the password input is displayed. Good Luck!"""

########################################################################
########################################################################

while MyGlobalTries > 0:
    password = input('Weapons Systems Password: ')
    if password == RandPassGen():
        #covers the situation in which the password was correct
        print('Password {} Accpeted! Firing Weapons Systems!'.format(password))
        #End Game Sequence Code should be inserted here
        print('Here is a small reward for all of your hard work!')
        sleep(5)
        EndGame()
        
    elif password == "Command Override. Password Recovery.":
        beginSimSeq = input('Would you like to solve the Sequence to recover the password? Yes or No?: ')

        if beginSimSeq == "Yes":
            while myGlobal < 3:
                SimonGameSeq()

            #Prints the password once the player achieves his/her simSeq
            else:
                print """Fantastic Job Captain! You now how the key to activate the
                weapons systems and defeat the Earthlings. All thats left now is to
                activate the guns. Good luck Captain."""
                print "RandPassGen()"
                PassReq()

        elif beginSimSeq == "No":
            print "Very Well. The option still remains. You must wait 15s to retry, but it is your final attempt."
            sleep(15)
            beginSimSeq = input('Would you like to solve the Sequence to recover the password? Yes or No?: ')

            if beginSimSeq == "Yes":
                #runs the game until the player successfully completes it 3 times in a row
                while myGlobal < 3:
                    SimonGameSeq()

                    #Prints the password once the player achieves his/her simSeq
                else:
                    print """Fantastic Job Captain! You now how the key to activate the
                    weapons systems and defeat the Earthlings. All thats left now is to
                    activate the guns. Good luck Captain."""
                    print "RandPassGen()"
                        
            elif beginSimSeq == "No":
                print "Mission Failed!"
                death()
                #print a death icon/end game function here
    else:
        #covers the situation in which the password was wrong
        print "Incorrect password. You have {} tries remaining!".format(myGlobalTries)
        password = input('Weapons Systems Password: ')
        myGlobalTries -= 1

else:
    death()
#########################################################################################
#Note: (On 5/3/17) It is crucial that we finish the input command lines, the GUI, and
#finish piecing together the main part of this code on 5/3/17 and 5/4/17 so that we can
#present it in class. The code must be run on a pie and we must set up a breadboard with
#the final version of the Simon Pi project assembled on it. Once this is finished we will
#be ready for Friday, and the only remaining parts of the code will be the puzzle and the
#GUI. After that the project will be completely finished unless we decide to add or change
#any code within the project in the remaining time before the deadline.
##########################################################################################
