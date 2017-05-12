########################################################################################
#Name: Collin Corbett, Jonathan Frank, John Do
#Date: 5/11/17
#Description: Final Form of the Martian Invader Project (Postable). This Code
#begins with a Random Password Generator. The player is asked if they wish to
#input the password. They can attempt to guess/type the password(which could
#eventually lead to death), or they can choose to override the password. If
#the player chooses to override the password they must navigate the maze ship
#until they reach the Weapons Control room (Room 20). Once the room is reached
#the player is asked to solve the color sequence. If the sequence is solved the
#password is displayed, and the user is asked to input it once again. Once the
#password is inputed correctly the game is considered completed, and the player
#wins. To simulate a reward we have attached an EndGame() function. This function
#contains borrowed code and all credit goes to the original author. The code plays
#no actual part to the game, and is only used to solidify the fact the player is
#finished and has achieved the maximum score for the game. The game is both score based.
#The goal is to achieve the maximum of 15 points, any less would only count as a good
#attempt
########################################################################################



########
#imports
########
import random
import RPi.GPIO as GPIO
from time import sleep
from random import randint
from Tkinter import *
import time
import pygame
from pygame.locals import * #pong v1.0; demonstration purposes only
from sys import exit #pong v1.0; demonstration purposes only/ Credit to Original Author


#################################################
#Global Variables Used to track:
#   #The Simon Sequence
#   #Lives
#   #Score
#   #Password
#   #Ship Explorer
#################################################
myGlobal = 0
count = 0
myGlobalTries = 3
pw1 = 0101
score = 0
#currentRoom = r1
#################################################



####################################
#Function for the Password Generator
####################################
def RandPassGen():
    characters = "abcdefghijklmnopqrstuvwxyz"
    upperchar = characters.upper()
    pass_len = 2 #sets the password to be (x) characters long
    passlist = []

    for i in range(pass_len//3):
        passlist.append(characters[random.randrange(len(characters))])
        passlist.append(upperchar[random.randrange(len(upperchar))])
        #passlist.append(str(random.randrange(10))) #adds numbers to the password. Causes errors. #1's look like L's
    for i in range(pass_len-len(passlist)):
        passlist.append(characters[random.randrange(len(characters))])

    random.shuffle(passlist)
    pwstring = "".join(passlist)

    #returns the password. Password is then saved to the Global Variable PW1 in the PassReq() funciton
    return(pwstring)



######################################
#Function for the Ship Explorer Puzzle
######################################
def ShipExplorer():
    # the room class
    # note that this class is fully implemented with dictionaries as illustrated in the lesson "More on Data Structures"
    class Room(object):
        # the constructor
        def __init__(self, name, image):
            # rooms have a name, an image (the name of a file), exits (e.g., south), exit locations
            # (e.g., to the south is room n), items (e.g., table), item descriptions (for each item),
            # and grabbables (things that can be taken into inventory)
            self.name = name
            self.image = image
            self.exits ={}
            self.items = {}
            self.grabbables = []

        # getters and setters for the instance variables
        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, value):
            self._name = value

        @property
        def image(self):
            return self._image

        @image.setter
        def image(self, value):
            self._image = value

        @property
        def exits(self):
            return self._exits

        @exits.setter
        def exits(self, value):
            self._exits = value

        @property
        def items(self):
            return self._items

        @items.setter
        def items(self, value):
            self._items = value

        @property
        def grabbables(self):
            return self._grabbables

        @grabbables.setter
        def grabbables(self, value):
            self._grabbables = value

        # adds an exit to the room
        # the exit is a string (e.g., north)
        # the room is an instance of a room
        def addExit(self, exit, room):
            # append the exit and room to the appropriate dictionary
            self._exits[exit] = room

        # adds an item to the room
        # the item is a string (e.g., table)
        # the desc is a string that describes the item (e.g., it is made of wood)
        def addItem(self, item, desc):
            # append the item and description to the appropriate dictionary
            self._items[item] = desc

        # adds a grabbable item to the room
        # the item is a string (e.g., key)
        def addGrabbable(self, item):
            # append the item to the list
            self._grabbables.append(item)

        # removes a grabbable item from the room
        # the item is a string (e.g., key)
        def delGrabbable(self, item):
            # remove the item from the list
            self._grabbables.remove(item)

        # returns a string description of the room
        def __str__(self):
            # first, the room name
            s = "You are in {}.\n".format(self.name)

            # next, the items in the room
            s += "You see: "
            for item in self.items.keys():
                s += item + " "
            s += "\n"

            # next, the exits from the room
            s += "Exits: "
            for exit in self.exits.keys():
                s += exit + " "

            return s

    # the game class
    # inherits from the Frame class of Tkinter
    class Game(Frame):
            # the constructor
        def __init__(self, parent):
            # call the constructor in the superclass
            Frame.__init__(self, parent)

        # creates the rooms
        def createRooms(self):
                    # r1 through r4 are the four rooms in the mansion
                    # currentRoom is the room the player is currently in (which
                    # can be one of r1 through r4)

                    # create the rooms and give them meaningful names and an
                    # image in the current directory


    #This creates the 27 rooms that make up the mansion game. Each room has a unique image to help add to the
    #diversity of the game.
                    r1 = Room("Bridge", "bridge.gif") #this room provides access to the GUI to input passwords
                    r2 = Room("Crew Quarters", "crew_quarters.gif")
                    r3 = Room("Officer Stations", "officer_stations.gif")
                    r4 = Room("Officer Quarters", "officer_quarters.gif")
                    r5 = Room("Mess Hall Epsilon", "mess_hall.gif")
                    r6 = Room("Lounge", "lounge.gif")
                    r7 = Room("Mess Hall Gamma", "mess_hall.gif")
                    r8 = Room("Weapon Bay One", "weapon_bay.gif")
                    r9 = Room("Briefing Room", "briefing_room.gif")
                    r10 = Room("Weapon Bay Four", "weapon_bay.gif")
                    r11 = Room("Weapon Bay Two", "weapon_bay.gif")
                    r12 = Room("Hangar", "hangar.gif")
                    r13 = Room("Weapon Bay Five", "weapon_bay.gif")
                    r14 = Room("Weapon Bay Three", "weapon_bay.gif")
                    r15 = Room("Reactor Room", "reactor_room.gif")
                    r16 = Room("Weapon Bay Six", "weapon_bay.gif")
                    r17 = Room("Ordinance Bay One", "ordinance_bay.gif")
                    r18 = Room("Laboratory", "laboratory.gif")
                    r19 = Room("Ordinance Bay Two", "ordinance_bay.gif")
                    r20 = Room("Weapons Control Room", "weapons_control.gif") #Room will provide access to the simon Sequence
                    r21 = Room("Engine Bay Sigma", "engine_bay.gif")
                    r22 = Room("Shield Generator Room", "shield_generator.gif")
                    r23 = Room("Engine Bay Lima", "engine_bay.gif")
                    r24 = Room("Engine Bay Xray", "engine_bay.gif")
                    r25 = Room("Engine Bay Tango", "engine_bay.gif")
                    r26 = Room("Engine Bay November", "engine_bay.gif")
                    r27 = Room("Engine Bay Kilo", "engine_bay.gif")
                    r28 = Room("Engine Bay Juliett", "engine_bay.gif")
                    
    #The following code adds exits, grabbables, and collectible items to the rooms
                    r1.addExit("north", r3)
                    r1.addGrabbable("")
                    r1.addItem("bridge", "This room is where all control of the ship is usually handled, but everyone seems frantic.")
                    r1.addItem("", "")

                    r2.addExit("north", r5)
                    r2.addExit("east", r3)
                    r2.addGrabbable("")
                    r2.addItem("quarters", "This is where the bulk of the crew rests when they get a chance.")
                    r2.addItem("", "")

                    r3.addExit("north", r6)
                    r3.addExit("south", r1)
                    r3.addExit("east", r4)
                    r3.addExit("west", r2)
                    r3.addGrabbable("")
                    r3.addItem("officer_stations", "Here officers work tirelessly to keep the ship in the air.")
                    r3.addItem("", "")

                    r4.addExit("north", r7)
                    r4.addExit("west", r3)
                    r4.addGrabbable("")
                    r4.addItem("quarters", "This is where the ships officers, including the Captain, rest.")
                    r4.addItem("", "")

                    r5.addExit("north", r8)
                    r5.addExit("south", r2)
                    r5.addExit("east", r6)
                    r5.addGrabbable("")
                    r5.addItem("hall", "One of the two mess halls on the ship. The smell of food fills the air.")
                    r5.addItem("", "")

                    r6.addExit("north", r9)
                    r6.addExit("south", r3)
                    r6.addExit("east", r7)
                    r6.addExit("west", r5)
                    r6.addGrabbable("")
                    r6.addItem("lounge", "Here the crew takes their breaks after long stressful shifts.")
                    r6.addItem("", "")
                    
                    r7.addExit("north", r10)
                    r7.addExit("south", r4)
                    r7.addExit("west", r6)
                    r7.addGrabbable("")
                    r7.addItem("hall", "One of the two mess halls on the ship. The smell of food fills the air.")
                    r7.addItem("", "")

                    r8.addExit("north", r11)
                    r8.addExit("south", r5)
                    r8.addExit("east", r9)
                    r8.addGrabbable("")
                    r8.addItem("bay", "One of the six weapon bays on the ship. The smell of oil and machinery fills the air.")
                    r8.addItem("", "")

                    r9.addExit("north", r12)
                    r9.addExit("south", r6)
                    r9.addExit("east", r10)
                    r9.addExit("west", r8)
                    r9.addGrabbable("")
                    r9.addItem("room", "This is the briefing room for the highest ranking officers. The room seems tense.")
                    r9.addItem("", "")

                    r10.addExit("north", r13)
                    r10.addExit("south", r7)
                    r10.addExit("west", r9)
                    r10.addGrabbable("")
                    r10.addItem("bay", "One of the six weapon bays on the ship. The smell of oil and machinery fills the air.")
                    r10.addItem("", "")

                    r11.addExit("north", r14)
                    r11.addExit("south", r8)
                    r11.addExit("east", r12)
                    r11.addGrabbable("")
                    r11.addItem("bay", "One of the six weapon bays on the ship. The smell of oil and machinery fills the air.")
                    r11.addItem("", "")

                    r12.addExit("north", r15)
                    r12.addExit("south", r9)
                    r12.addExit("east", r13)
                    r12.addExit("west", r11)
                    r12.addGrabbable("")
                    r12.addItem("hangar", "Here the ships defense fighters and transports sit waiting for use.")
                    r12.addItem("", "")

                    r13.addExit("north", r16)
                    r13.addExit("south", r10)
                    r13.addExit("west", r12)
                    r13.addGrabbable("")
                    r13.addItem("bay", "One of the six weapon bays on the ship. The smell of oil and machinery fills the air.")
                    r13.addItem("", "")

                    r14.addExit("north", r17)
                    r14.addExit("south", r11)
                    r14.addExit("east", r15)
                    r14.addGrabbable("")
                    r14.addItem("bay", "One of the six weapon bays on the ship. The smell of oil and machinery fills the air.")
                    r14.addItem("", "")

                    r15.addExit("north", r18)
                    r15.addExit("south", r12)
                    r15.addExit("east", r16)
                    r15.addExit("west", r14)
                    r15.addGrabbable("")
                    r15.addItem("reactor", "This room contains the ships reactor. Without this we would be dead in space.")
                    r15.addItem("", "")

                    r16.addExit("north", r19)
                    r16.addExit("south", r13)
                    r16.addExit("west", r15)
                    r16.addGrabbable("")
                    r16.addItem("bay", "One of the six weapon bays on the ship. The smell of oil and machinery fills the air.")
                    r16.addItem("", "")

                    r17.addExit("north", None)
                    r17.addExit("south", r14)
                    r17.addExit("east", r18)
                    r17.addExit("west", r23)
                    r17.addGrabbable("")
                    r17.addItem("bay", "One of the two ordinance bays on the ship. All munitions are stored here.")
                    r17.addItem("", "")

                    r18.addExit("north", r21)
                    r18.addExit("south", r15)
                    r18.addExit("east", r19)
                    r18.addExit("west", r17)
                    r18.addGrabbable("")
                    r18.addItem("lab", "The ships laboratory. All research is done in this room, and it is here human\
    specimens will be dissected and studied.")
                    r18.addItem("", "")

                    r19.addExit("north", r22)
                    r19.addExit("south", r16)
                    r19.addExit("east", r26)
                    r19.addExit("west", r18)
                    r19.addGrabbable("")
                    r19.addItem("bay", "One of the two ordinance bays on the ship. All munitions are stored here.")
                    r19.addItem("", "")

                    r20.addExit("south", r17)
                    r20.addExit("east", r21)
                    r20.addExit("west", r24)
                    r20.addGrabbable("")
                    r20.addItem("station", "This is the weapons control room. From here we will rain down fire upon\
    the puny earthlings.")
                    r20.addItem("", "")

                    r21.addExit("south", r18)
                    r21.addExit("east", r22)
                    r21.addExit("west", None)
                    r21.addGrabbable("")
                    r21.addItem("bay", "This is the main engine bay of the ship.")
                    r21.addItem("", "")

                    r22.addExit("south", r19)
                    r22.addExit("east", r27)
                    r22.addExit("west", r21)
                    r22.addGrabbable("")
                    r22.addItem("room", "This room houses the ships shield generator. With this even the humans strongest weapons will mean nothing.")
                    r22.addItem("", "")

                    r23.addExit("north", r24)
                    r23.addExit("east", r17)
                    r23.addGrabbable("")
                    r23.addItem("bay", "One of the six smaller engine bays on the ship.")
                    r23.addItem("", "")

                    r24.addExit("north", r25)
                    r24.addExit("south", r23)
                    r24.addExit("east", None)
                    r24.addGrabbable("")
                    r24.addItem("bay", "One of the six smaller engine bays on the ship.")
                    r24.addItem("", "")

                    r25.addExit("south", r24)
                    r25.addGrabbable("")
                    r25.addItem("bay", "One of the six smaller engine bays on the ship.")
                    r25.addItem("", "")

                    r26.addExit("north", r27)
                    r26.addExit("west", r19)
                    r26.addGrabbable("")
                    r26.addItem("bay", "One of the six smaller engine bays on the ship.")
                    r26.addItem("", "")

                    r27.addExit("north", r28)
                    r27.addExit("south", r26)
                    r27.addExit("west", r22)
                    r27.addGrabbable("")
                    r27.addItem("bay", "One of the six smaller engine bays on the ship.")
                    r27.addItem("", "")

                    r28.addExit("south", r27)
                    r28.addGrabbable("")
                    r28.addItem("bay", "One of the six smaller engine bays on the ship.")
                    r28.addItem("", "")


       

       
       
       

                    
    #############################################################################################################################################################################################
                    
                    # set room 1 as the current room at the beginning of the game
                    Game.currentRoom = r1

                    # initialize the player's inventory
                    Game.inventory = []


        # sets up the GUI
        def setupGUI(self):
                    # organize the GUI
                    self.pack(fill=BOTH, expand=1)

                    # setup the player input at the bottom of the GUI
                    # the widget is a Tkinter Entry
                    # set its background to white and bind the return key to the
                    # function process in the class
                    # push it to the bottom of the GUI and let it fill
                    # horizontally
                    # give it focus so the player doesn't have to click on it
                    Game.player_input = Entry(self, bg="white")
                    Game.player_input.bind("<Return>", self.process)
                    Game.player_input.pack(side=BOTTOM, fill=X)
                    Game.player_input.focus()

                    # setup the image to the left of the GUI
                    # the widget is a Tkinter Label
                    # don't let the image control the widget's size
                    img = None
                    Game.image = Label(self, width=WIDTH / 2, image=img)
                    Game.image.image = img
                    Game.image.pack(side=LEFT, fill=Y)
                    Game.image.pack_propagate(False)

                    # setup the text to the right of the GUI
                    # first, the frame in which the text will be placed
                    text_frame = Frame(self, width=WIDTH / 2)
                    # the widget is a Tkinter Text
                    # disable it by default
                    # don't let the widget control the frame's size
                    Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
                    Game.text.pack(fill=Y, expand=1)
                    text_frame.pack(side=RIGHT, fill=Y)
                    text_frame.pack_propagate(False)

                    
        # sets the current room image
        def setRoomImage(self):
                    if (Game.currentRoom == None):
                            # if dead, set the skull image
                            Game.img = PhotoImage(file="weapons_control.gif")
                    else:
                            # otherwise grab the image for the current room
                            Game.img = PhotoImage(file=Game.currentRoom.image)

                    # display the image on the left of the GUI
                    Game.image.config(image=Game.img)
                    Game.image.image = Game.img
      

        # sets the status displayed on the right of the GUI
        def setStatus(self, status):
                    # enable the text widget, clear it, set it, and disabled it
                    Game.text.config(state=NORMAL)
                    Game.text.delete("1.0", END)
                    if (Game.currentRoom == None):
                        #allows the global score to be increased
                        global score
                        score += 5
                        #replaces the old death function and forces the rest of the code to run
                        #request for Simon Seq
                        beginSimSeq = input('Would you like to solve the Color Sequence to recover the password? Yes or No?: ')
                        if beginSimSeq == "Yes":
                            sleep(5)
                            while count < 2:
                                #runs funciton for simon seq
                                SimonGameSeq()
                            
                            else:
                                #increases score for getting sequence correct
                                #global score#
                                score += 5
                                print """Fantastic Job Captain! You now how the key to activate the weapons systems and
defeat the Earthlings. All thats left now is to activate the guns.
Good luck Captain."""
                                global pw1
                                print (pw1)
                                sleep(5)

                                #asks for the password again
                                password = input('Weapons Systems Password: ')
                                #keeps track of lives and checks player isn' "dead"
                                global myGlobalTries
                                while myGlobalTries > 0:
                                    if password == (pw1):
                                        #global score#
                                        score += 5
                                        print('Password {} Accepeted! Firing Weapons Systems!'.format(pw1))
                                        print('You achieved a score of {}!'.format(score))
                                        sleep(5)
                                        #End Game function. Only for entertainment purposes. Game ends on print statement
                                        EndGame()
                                    else:
                                        myGlobalTries -= 1
                                        print "Incorrect password. You have {} tries remaining!".format(myGlobalTries)
                                        sleep(5)
                                        #allows code to loop
                                        Looper2()
                                        
                        #allows code to loop a final time           
                        elif beginRecoverSeq == "No":
                            print "Very Well. The option still remains. You must wait 15s to retry, but it is your final attempt."
                            sleep(15)
                            beginSimSeq = input('Would you like to solve the Color Sequence to recover the password? Yes or No?: ')

                            if beginSimSeq == "Yes":
                                #runs the game until the player successfully completes it 1 time
                                while count < 2:
                                    SimonGameSeq()

                            #Prints the password once the player achieves his/her simSeq
                                else:
                                    print """Fantastic Job Captain! You now have the key to activate the weapons systems and
defeat the Earthlings. All thats left now is to activate the guns.
Good luck Captain."""
                                print (pw1)
                                looper2()

                            elif beginSimSeq == "No":
                                print "Mission Failed"
                                death()
                                print('You achieved a score of {}!'.format(score))

                    else:
                            # otherwise, display the appropriate status
                            Game.text.insert(END, str(Game.currentRoom) +\
                                             "\nYou are carrying: " + str(Game.inventory) +\
                                             "\n\n" + status)
                    Game.text.config(state=DISABLED)                

        # plays the game
        def play(self):
            # add the rooms to the game
            self.createRooms()
            # configure the GUI
            self.setupGUI()
            # set the current room
            self.setRoomImage()
            # set the current status
            self.setStatus("")

        # processes the player's input
        def process(self, event):
                    # grab the player's input from the input at the bottom of
                    # the GUI
                    action = Game.player_input.get()
                    # set the user's input to lowercase to make it easier to
                    # compare the verb and noun to known values
                    action = action.lower()
                    # set a default response
                    response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"

                    # exit the game if the player wants to leave (supports quit,
                    # exit, and bye)
                    if (action == "quit" or action == "exit" or action == "bye" or action == "sionara!"):
                            exit(0)

                    # if the player is dead if goes/went south from room 4
                    if (Game.currentRoom == None):
                            # clear the player's input
                            Game.player_input.delete(0, END)
                            return

                    # split the user input into words (words are separated by
                    # spaces) and store the words in a list
                    words = action.split()

                    # the game only understands two word inputs
                    if (len(words) == 2):
                            # isolate the verb and noun
                            verb = words[0]
                            noun = words[1]

                            # the verb is: go
                            if (verb == "go"):
                                    # set a default response
                                    response = "Invalid exit."

                                    # check for valid exits in the current room
                                    if (noun in Game.currentRoom.exits):
                                            # if one is found, change the current room to
                                            # the one that is associated with the
                                            # specified exit
                                            Game.currentRoom = Game.currentRoom.exits[noun]
                                    # set the response (success)
                                    response = "Room changed."
                            # the verb is: look
                            elif (verb == "look"):
                                    # set a default response
                                    response = "I don't see that item."

                                    # check for valid items in the current room
                                    if (noun in Game.currentRoom.items):
                                            # if one is found, set the response to the
                                            # item's description
                                            response = Game.currentRoom.items[noun]
                            # the verb is: take
                            elif (verb == "take"):
                                    # set a default response
                                    response = "I don't see that item."

                                    # check for valid grabbable items in the current
                                    # room
                                    for grabbable in Game.currentRoom.grabbables:
                                            # a valid grabbable item is found
                                            if (noun == grabbable):
                                                    # add the grabbable item to the player's
                                                    # inventory
                                                    Game.inventory.append(grabbable)
                                                    # remove the grabbable item from the
                                                    # room
                                                    Game.currentRoom.delGrabbable(grabbable)
                                                    # set the response (success)
                                                    response = "Item grabbed."
                                                    # no need to check any more grabbable
                                                    # items
                                                    break

                    # display the response on the right of the GUI
                    # display the room's image on the left of the GUI
                    # clear the player's input
                    self.setStatus(response)
                    self.setRoomImage()
                    Game.player_input.delete(0, END)
    ##########################################################
    # the default size of the GUI is 800x600
    WIDTH = 800
    HEIGHT = 600

    # create the window
    window = Tk()
    window.title("Room Adventure")

    # create the GUI as a Tkinter canvas inside the window
    g = Game(window)
    # play the game
    g.play()

    # wait for the window to close
    window.mainloop()





################################################
#Function for the Simon Sequence
#(Recycled Simon Game)
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

    seq = []
    seq.append(randint(0, 3))
    seq.append(randint(0, 3))

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
            global count
            count = 0
            while count <= 2:

                while (count < len(seq)):
                    pressed = False

                    while (not pressed):
                        for i in range(len(switches)):
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
                else:
                    return count

    except KeyboardInterrupt:
        GPIO.cleanup()


############################
#function for Password Input
############################
def PassReq():
    global currentRoom
    global myGlobalTries
    while myGlobalTries > 0:
        global pw1
        global score
    
        pw1 = RandPassGen()
        password = input('Weapons Systems Password: ')
        if password == (pw1):
            print('Password {} Accepeted! Firing Weapons Systems!'.format(pw1))
            print('You achieved a score of {}!'.format(score))
            sleep(5)
            EndGame()
            
        elif password == "Command Override. Password Recovery.":
            beginRecoverySeq = input('Would you like to solve the Sequence to recover the password? Yes or No?: ')

            if beginRecoverySeq == "Yes":
                #Begin Mansion Game here:
                ShipExplorer()

        else:
            myGlobalTries -= 1
            print "Incorrect password. You have {} tries remaining!".format(myGlobalTries)
            #calls main looper function
            Looper()
    else:
        death()
            
                        
                
#loops the PassReq() function
def Looper():
    PassReq()
    
#modified PassReq() fuction to remove some player options
def PassReq2():
    global myGlobalTries
    while myGlobalTries > 0:
        global pw1
        password = input('Weapons Systems Password: ')
        if password == (pw1):
            print('Password {} Accepeted! Firing Weapons Systems!'.format(pw1))
            print('You achieved a score of {}!'.format(score))

            sleep(5)
            EndGame()

        else:
            myGlobalTries -= 1
            print "Incorrect password. You have {} tries remaining!".format(myGlobalTries)
            looper2()
    else:
        death()

#loops the PassReq2() function
def Looper2():
    PassReq2()
    

#############################################################################
#Death Function. Prints a skull.
#############################################################################
        
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




###############################################################################################
#End Game Function
#Pong V1.0 will be used
#for in class demonstration purposes. All credit goes to its
#original author, as this is simply a place holder to demonstrate
#working code. This code segment is for entertainment purposes only.)
#The actual "EndGame()" are the print statements

#The following comments are from the original author:
    ##!/usr/bin/env python
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#		It's my first actual game-making attempt. I know code could be much better 
#		with classes or defs but I tried to make it short and understandable with very 
#		little knowledge of python and pygame(I'm one of them). Enjoy.
###############################################################################################

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
#Main Part of the Code
######################
print """ Good Day Captain. Today is 05/17/2017. The invasion of Earth as begun.
As Martian High Commander it is your duty to lead the Armada, but before we can
attack we must reactivate our long dormant weapons systems. The process is
tedious but without it we can not accomplish our mission. Your are our only
hope. Activate the weapons systems and destroy the puny earthlings, but be
careful. If the weapons system password is keyed incorrectly three times the
ship will self-destruct. It is a foolish concept we know, but it was implemented
by the Mar's High Council to prevent espionage and terror attacks. Good luck
Captain! Note: Type "Command Override. Password Recovery." to progress deeper
into the game when the password input is displayed. Good Luck!"""

PassReq()


    

