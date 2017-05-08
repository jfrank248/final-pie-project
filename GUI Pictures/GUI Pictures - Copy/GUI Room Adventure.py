###########################################################################################
# Name: 
# Date: 
# Description: 
###########################################################################################

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
#First Floor Rooms
                r1 = Room("Main Hall", "room1.gif")
                r2 = Room("Reading Room", "room2.gif")
                r3 = Room("Grand Library", "room3.gif")
                r4 = Room("Enchanting Room", "room4.gif")
                r5 = Room("Study", "")
                r6 = Room("Kitchen", "")
                r7 = Room("Lab", "")
                r8 = Room("Bathroom", "")
                r9 = Room("Bedroom", "")
                r10 = Room("Living Room", "")
                r11 = Room("Master Bedroom", "")
                r12 = Room("Library", "")
                r13 = Room("Grand Study", "")
                r14 = Room("Sactuary", "")
                r15 = Room("Boiler Room", "")
                r16 = Room("Dining Room", "")
                r17 = Room("Wine Room", "")
                r18 = Room("Spider Haven", "")
                r19 = Room("Torture Room", "")
                r20 = Room("Bedroom", "")
                r21 = Room("Meat Locker", "")
                r22 = Room("Bathroom", "")
                r23 = Room("Guest Room", "")
                r24 = Room("Guest Study", "")
                r25 = Room("Grand Stair Case Room", "")
                r26 = Room("Cellar Room", "")
                r27 = Room("Trash Room", "")                          
                

                # add exits to room 1
                r1.addExit("south", r5)
                # add grabbables to room 1
                r1.addGrabbable("picture")
                # add items to room 1
                r1.addItem("paintings", "Elaborate paintings decorate the hall, and they seem to go on forever.")
                r1.addItem("small_table", "It is made of oak. It is the only piece of furniture in hall. On it rests a picture that reads 'Turn Back'.")
   

                # add exits to room 2
                r2.addExit("east", r3)
                r2.addExit("south", r9)
                r2.addGrabbable("dagger")
                # add items to room 2
                r2.addItem("rug", "It is made of a bear, a dagger rests in his mouth.")
                r2.addItem("fireplace", "A small fire burns inside, and a pile of books rests nearby. Someone has been here, and recently.")
                r2.addItem("bookshelves", "Hundreds of books line the walls surrounding a single chair in the middle of the room.")

                # add exits to room 3
                r3.addExit("south", r10)
                r3.addExit("east", r4)
                r3.addExit("west", r2)
                # add grabbables to room 3
                r3.addGrabbable("book")
                # add items to room 3
                r3.addItem("bookshelves", "There seems to be thousands of shelves lining a massive chamber. The sight takes your breath away.")
                r3.addItem("statue", "A large statue rests in the middle of the room, it looks like a mythical monster but you can't place what it is.")
                r3.addItem("desk", "The desk is in front of the statue, and it is made of aged oak. A strange looking book sits on top of the desk.")

                # add exits to room 4
                r4.addExit("east", r5)
                r4.addExit("west", r3)
                r4.addExit("south", r11)
                # add grabbables to room 4
                r4.addGrabbable("potion")
                # add items to room 4
                r4.addItem("walls", "The walls are covered in demonic symbols which appear to be drawn in blood. Upon closer inspection you think it may be paint, but it sends a shiver down your spine.")
                r4.addItem("alchemy_table", "The strange looking table is covered in beakers full of glowing a liquid. A single finished potion sits on the tabel, but you don't know what it does.")


                r5.addExit("north", r1)
                r5.addExit("south", r12)
                r5.addExit("east", r6)
                r5.addExit("west", r4)
                r5.addGrabbable("sword")
                r5.addItem("room", "The room is fairly simple. A few bookshelves line the walls along with some filing cabinets. A desk sits in the middle of the room with a large leather chair behind it.")
                r5.addItem("desk", "It is made of a gorgeous stained cedar, on top rests an old sword made of damascus steel.")

                r6.addExit("south", r13)
                r6.addExit("east", r7)
                r6.addExit("west", r5)
                r6.addGrabbable("soda")
                r6.addItem("fridge", "The kitchen is elaborate and enourmous. You open the massive fridge only to find a single soda.")

                r7.addExit("south", r14)
                r7.addExit("east", r8)
                r7.addExit("west", r6)
                r7.addGrabbable("rat")
                r7.addItem("cage", "This lab is used to run cruel experiments on animals. You see a cage with a cute lab rat inside and it breaks your heart.")

                r8.addExit("south", r15)
                r8.addExit("west", r7)
                r8.addGrabbable("amulet")
                r8.addItem("sink", "The bathroom is quite large. You walk up to the sink, which is made of gold, and find an amulet resting inside it.")

                r9.addExit("north", r2)
                r9.addExit("south", r16)
                r9.addExit("east", r10)
                r9.addGrabbable("rose")
                r9.addItem("bed", "A large bed rest in the middle of a highly decorated room. It looks comfty, but you wish to explore more of the house. A single rose rests on top of the bed.")

                r10.addExit("north", r3)
                r10.addExit("south", r17)
                r10.addExit("east", r11)
                r10.addExit("west", r9)
                r10.addItem("couch", "The couch is massive and made out of leather, you've never felt something more amazing in your life.")
                r10.addItem("elaborate_chair", "The chair is massive and a cat is sitting in it, but he won't let you touch him.")

                r11.addExit("north", r4)
                r11.addExit("south", r18)
                r11.addExit("east", r12)
                r11.addExit("west", r10)
                r11.addGrabbable("gun")
                r11.addItem("bed", "This room is without a doubt the master bedroom. The bed is 5x larger than any king size bed, and it is covered in sheets and blankets made of the finest silk.")
                r11.addItem("dresser", "You see a gun inside, there aren't any bullets, but it looks ancient.")

                r12.addExit("north", r5)
                r12.addExit("south", r19)
                r12.addExit("east", r13)
                r12.addExit("west", r11)
                r12.addItem("books", "They cover the walls. This library is much smaller than one would expect, but it is much more eerie as well.")
                #r12.addItem("ladder", "Your stereotypical rolling library ladder. It is leaning against one of the shelves and has obviously lost its war against the termites.")

                r13.addExit("north", r6)
                r13.addExit("south", r20)
                r13.addExit("east", r14)
                r13.addExit("west", r12)
                r13.addGrabbable("bullets")
                r13.addGrabbable("twinkie")
                r13.addItem("grand_desk", "The desk is massive, and trimmed with gold. On top of it sits a collection of assorted books that look like something out of a fairytale.")
                r13.addItem("desk_drawer", "The drawer is extremely heavy, inside you find a twinkie and some bullets for a gun. Hopefully you never need them.")
                
                r14.addExit("north", r7)
                r14.addExit("south", r21)
                r14.addExit("east", r15)
                r14.addExit("west", r13)
                r14.addItem("altar", "You don't recognize the markings etched into the stone structure, but they look sinister, and the stones are stained an offset red.")
                #r14.addItem("knife", "It seems different from your normal, everyday kitchen knife. This one is sharper and more angular with a strange star on the side.")

                r15.addExit("north", r8)
                r15.addExit("south", r22)
                r15.addExit("west", r14)
                r15.addItem("boiler", "The boiler looks ancient and steam is leaking from the pipes. Its probably not a good idea to stand too close to it.")
                #r15.addItem("wrench", "An old monkey wrench. It was once a bright red but the rust has given it a new shade.")

                r16.addExit("north", r9)
                r16.addExit("east", r17)
                r16.addGrabbable("turkey")
                r16.addItem("table", "A giant turkey rests on the table. It looks delicious. I'm sure no one would mind if you borrowed it for later.")
                #r16.addItem("chair", "A rickety old chair. Its covered in a thick layer of dust.")

                r17.addExit("north", r10)
                r17.addExit("south", r23)
                r17.addExit("east", r18)
                r17.addExit("west", r16)
                r17.addGrabbable("wine")
                r17.addItem("wine_rack", "Wine racks line the walls for hundreds of feet. The racks are filled to the brim with bottles of hundred year old wine. I'm sure no one would mind you taking a bottle.")
                #r17.addItem("broken_bottle", "A broken wine bottle. The contents have long since evaporated but a sticky spot still remains. Nearby you see a shelf that had been eaten by termites to the point that it gave way."

                r18.addExit("north", r11)
                r18.addExit("south", r24)
                r18.addExit("east", r19)
                r18.addExit("west", r17)
                r18.addItem("spider_nest", "It's crawling with giant spiders, I would stay away, they look pretty deadly.")
                #r18.additem("egg_sac", "Well, now you know where all of the spiders came from. Rest in peace Big Momma Crawlah"

                r19.addExit("north", r12)
                r19.addExit("south", r25)
                r19.addExit("east", r20)
                r19.addExit("west", r18)
                r19.addGrabbable("locket")
                r19.addItem("torture_table", "The sight of this device leaves you sick. Dried blood cakes the floor and the tools are all jagged and rusty.")
                r19.addItem("locket", "An old locket sits on the table, its rusty, but you can still make out a family in the aged photo.")
                
                r20.addExit("north", r13)
                r20.addExit("south", r26)
                r20.addExit("east", r21)
                r20.addExit("west", r19)
                r20.addItem("room", "The room is very bland. There are paintings on the wall and the eyes seem to be following you")
                #r20.addItem("strange_painting", "After a few minutes you covnince yourself that the paintings are not watching you and it is all just an optical illusion. That is, until one of the paintings changes its expression.")

                r21.addExit("north", r14)
                r21.addExit("south", r27)
                r21.addExit("east", r22)
                r21.addExit("west", r20)
                r21.addGrabbable("flesh")
                r21.addItem("meat_racks", "flesh hangs from the ceiling on sharp hooks dripping with blood. Something about this meat seems off, and its still fresh. The thought that you are not alone once again crosses your mind.")
                #r21.addItem("meat_hook", "A normal-looking meat hook. You shiver at the thought of being impaled and suspended by it and question why you still here.")

                r22.addExit("north", r15)
                r22.addExit("west", r21)
                r22.addGrabbable("soap")
                r22.addItem("sink", "The sink seems pretty bland. Except for the glowing bar of soap on the counter. Thats pretty neat.")
                #r22.addItem("glowing_soap", "It has a strange iridescent glow about it. It has a brilliant and comforting blue as you walk towards it and a dangerous, threatening red when you walk away")

                r23.addExit("north", r17)
                r23.addExit("east", r24)
                r23.addGrabbable("log_book")
                r23.addItem("log_book", "The book contains the names of every guest that has ever stayed in this room. Strangely there is a faded red line running through all of the names. Except the last line... where you read your name crossed out in fresh blood.")
                #r23.addItem("quill", "There is a quill nearby that was somehow crafted from a bone.....hopefully not human.") 

                r24.addExit("north", r18)
                r24.addExit("east", r25)
                r24.addExit("west", r23)
                #r24.addGrabbable("handkerchief")
                #r24.addItem("room", "The room is fairly simple, a few bookshelves on the wall and a desk and chair in the middle of the room. However, the freshly spilled blood that coats the room turns your stomach. Something is definitely wrong with this place. Maybe it's the armor in the corner.")
                #r24.addItem("armor", "There is a suit of armor off in a corner that is holding a halberd and a handkerchief, you wish you could crawl in and hide until you realized that it is emitting a stench, a closer inspection reveals a human body is inside.")
                
                r25.addExit("north", r19)
                r25.addExit("east", r26)
                r25.addExit("west", r24)
                r25.addExit("south", None)
                r25.addItem("stairs", "They are coated in blood and seem to lead into darkness. You hear strange noises, and you aren't sure what to do. A sign says to turn back.")
                #r25.addItem("lever", "A strange lever is in the wall by the stairs. A pull on this lever made the stairs form a kind of ramp. A body slowly slides down to greet you.\
#The stairs go back to normal after this.")

                r26.addExit("north", r20)
                r26.addExit("east", r27)
                r26.addExit("west", r25)
                r26.addExit("south", None)
                r26.addItem("cellar_door", "You hear strange noises down below. Now would be a good time to turn back the way you come or leave with the path of the sun.")
                #r26.addItem("lock", "An old, rusty lock that may have once kept the cellar's secrets safe.")

                r27.addExit("north", r21)
                r27.addExit("west", r26)
                r27.addGrabbable("stone")
                r27.addItem("garbage_pile", "A small stone sits on top of the vile pile of goop before you. It reminds you of the stones you used to play with as a child.")
                #r27.addItem("head", "A noseless head that seems to be watching you. Somebody never got their nose back as a child.")

                
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

