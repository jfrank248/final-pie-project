from Tkinter import *

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
                r1.addItem("", "")
                r1.addItem("", "")

                r2.addExit("north", r5)
                r2.addExit("east", r3)
                r2.addGrabbable("")
                r2.addItem("", "")
                r2.addItem("", "")

                r3.addExit("north", r6)
                r3.addExit("south", r1)
                r3.addExit("east", r4)
                r3.addExit("west", r2)
                r3.addGrabbable("")
                r3.addItem("", "")
                r3.addItem("", "")

                r4.addExit("north", r7)
                r4.addExit("west", r3)
                r4.addGrabbable("")
                r4.addItem("", "")
                r4.addItem("", "")

                r5.addExit("north", r8)
                r5.addExit("south", r2)
                r5.addExit("east", r6)
                r5.addGrabbable("")
                r5.addItem("", "")
                r5.addItem("", "")

                r6.addExit("north", r9)
                r6.addExit("south", r3)
                r6.addExit("east", r7)
                r6.addExit("west", r5)
                r6.addGrabbable("")
                r6.addItem("", "")
                r6.addItem("", "")
                
                r7.addExit("north", r10)
                r7.addExit("south", r4)
                r7.addExit("west", r6)
                r7.addGrabbable("")
                r7.addItem("", "")
                r7.addItem("", "")

                r8.addExit("north", r11)
                r8.addExit("south", r5)
                r8.addExit("east", r9)
                r8.addGrabbable("")
                r8.addItem("", "")
                r8.addItem("", "")

                r9.addExit("north", r12)
                r9.addExit("south", r6)
                r9.addExit("east", r10)
                r9.addExit("west", r8)
                r9.addGrabbable("")
                r9.addItem("", "")
                r9.addItem("", "")

                r10.addExit("north", r13)
                r10.addExit("south", r7)
                r10.addExit("west", r9)
                r10.addGrabbable("")
                r10.addItem("", "")
                r10.addItem("", "")

                r11.addExit("north", r14)
                r11.addExit("south", r8)
                r11.addExit("east", r12)
                r11.addGrabbable("")
                r11.addItem("", "")
                r11.addItem("", "")

                r12.addExit("north", r15)
                r12.addExit("south", r9)
                r12.addExit("east", r13)
                r12.addExit("west", r11)
                r12.addGrabbable("")
                r12.addItem("", "")
                r12.addItem("", "")

                r13.addExit("north", r16)
                r13.addExit("south", r10)
                r13.addExit("west", r12)
                r13.addGrabbable("")
                r13.addItem("", "")
                r13.addItem("", "")

                r14.addExit("north", r17)
                r14.addExit("south", r11)
                r14.addExit("east", r15)
                r14.addGrabbable("")
                r14.addItem("", "")
                r14.addItem("", "")

                r15.addExit("north", r18)
                r15.addExit("south", r12)
                r15.addExit("east", r16)
                r15.addExit("west", r14)
                r15.addGrabbable("")
                r15.addItem("", "")
                r15.addItem("", "")

                r16.addExit("north", r19)
                r16.addExit("south", r13)
                r16.addExit("west", r15)
                r16.addGrabbable("")
                r16.addItem("", "")
                r16.addItem("", "")

                r17.addExit("north", r20)
                r17.addExit("south", r14)
                r17.addExit("east", r18)
                r17.addExit("west", r23)
                r17.addGrabbable("")
                r17.addItem("", "")
                r17.addItem("", "")

                r18.addExit("north", r21)
                r18.addExit("south", r15)
                r18.addExit("east", r19)
                r18.addExit("west", r17)
                r18.addGrabbable("")
                r18.addItem("", "")
                r18.addItem("", "")

                r19.addExit("north", r22)
                r19.addExit("south", r16)
                r19.addExit("east", r26)
                r19.addExit("west", r18)
                r19.addGrabbable("")
                r19.addItem("", "")
                r19.addItem("", "")

                r20.addExit("south", r17)
                r20.addExit("east", r21)
                r20.addExit("west", r24)
                r20.addGrabbable("")
                r20.addItem("", "")
                r20.addItem("", "")

                r21.addExit("south", r18)
                r21.addExit("east", r22)
                r21.addExit("west", r20)
                r21.addGrabbable("")
                r21.addItem("", "")
                r21.addItem("", "")

                r22.addExit("south", r19)
                r22.addExit("east", r27)
                r22.addExit("west", r21)
                r22.addGrabbable("")
                r22.addItem("", "")
                r22.addItem("", "")

                r23.addExit("north", r24)
                r23.addExit("east", r17)
                r23.addGrabbable("")
                r23.addItem("", "")
                r23.addItem("", "")

                r24.addExit("north", r25)
                r24.addExit("south", r23)
                r24.addExit("east", r20)
                r24.addGrabbable("")
                r24.addItem("", "")
                r24.addItem("", "")

                r25.addExit("south", r24)
                r25.addGrabbable("")
                r25.addItem("", "")
                r25.addItem("", "")

                r26.addExit("north", r27)
                r26.addExit("west", r19)
                r26.addGrabbable("")
                r26.addItem("", "")
                r26.addItem("", "")

                r27.addExit("north", r28)
                r27.addExit("south", r26)
                r27.addExit("west", r22)
                r27.addGrabbable("")
                r27.addItem("", "")
                r27.addItem("", "")

                r28.addExit("south", r27)
                r28.addGrabbable("")
                r28.addItem("", "")
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
                        Game.img = PhotoImage(file="skull.gif")
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
                        # if dead, let the player know
                        Game.text.insert(END, "You are dead. The only thing you can do now is   quit.\n")
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

