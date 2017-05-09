

####################################################################
#Names:Collin Corbett, Tyler Perryman, Tristan  Note: I forgot Tristan's last name :(
#Date: 2/10/17
#Description: Code for the Mansion Game. This version is to be fun and a collection/reader
#game. The end result is either death or you get tired of searching rooms.
####################################################################
# the blueprint for a room
class Room(object):
    # the constructor
    def __init__(self, name):
        # rooms have a name, exits (e.g., south), exit locations
        # (e.g., to the south is room n), items (e.g., table), item
        # descriptions (for each item), and grabbables (things that
        # can be taken into inventory)
        self.name = name
        self.exits = []
        self.exitLocations = []
        self.items = []
        self.itemDescriptions = []
        self.grabbables = []

        # getters and setters for the instance variables
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def exitLocations(self):
        return self._exitLocations

    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def itemDescriptions(self):
        return self._itemDescriptions

    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value

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
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made
    # of wood)
    def addItem(self, item, desc):
        # append the item and exit to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)

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
        for item in self.items:
            s += item + " "
        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self.exits:
            s += exit + " "
        return s


#####################################################

# creates the rooms
def createRooms():
    # r1 through r4 are the four rooms in the mansion
    # currentRoom is the room the player is currently in (which can
    # be one of r1 through r4)
    # since it needs to be changed in the main part of the program,
    # it must be global
    global currentRoom

    # create the rooms and give them meaningful names
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")
    r5 = Room("Room 5")
    r6 = Room("Room 6")
    r7 = Room("Room 7")
    r8 = Room("Room 8")
    r9 = Room("Room 9")
    r10 = Room("Room 10")
    r11 = Room("Room 11")
    r12 = Room("Room 12")
    r13 = Room("Room 13")
    r14 = Room("Room 14")
    r15 = Room("Room 15")
    r16 = Room("Room 16")
    r17 = Room("Room 17")
    r18 = Room("Room 18")
    r19 = Room("Room 19")
    r20 = Room("Room 20")
    r21 = Room("Room 21")
    r22 = Room("Room 22")
    r23 = Room("Room 23")
    r24 = Room("Room 24")
    r25 = Room("Room 25")
    r26 = Room("Room 26")

    
    # add exits to room 1
    r1.addExit("east", r2) # -> to the east of room 1 is room 2
    r1.addExit("south", r3)
    r1.addExit("west", r5)
    # add grabbables to room 1
    r1.addGrabbable("key")
    # add items to room 1
    r1.addItem("chair", "It is made of bones and no one is sitting on it.\
 A lonely spider sits perched on the arm.")
    r1.addItem("table", "It is made of oak. A golden key rests on it.")

    # add exits to room 2
    r2.addExit("west", r1)
    r2.addExit("south", r4)
    # add items to room 2
    r2.addItem("rug", "It is weaved from the softest of skin. It also needs to be vacuumed.")
    r2.addItem("fireplace", "It is full of burnt corpses.")

    # add exits to room 3
    r3.addExit("north", r1)
    r3.addExit("east", r4)
    r3.addExit("south", r7)
    r3.addExit("west", r6)
    # add grabbables to room 3
    r3.addGrabbable("book")
    # add items to room 3
    r3.addItem("bookshelves", "They are empty. Go figure.")
    r3.addItem("statue", "There is nothing special about it.")
    r3.addItem("desk", "The statue is resting on it. So is a book.")

    # add exits to room 4
    r4.addExit("north", r2)
    r4.addExit("west", r3)
    r4.addExit("south", None) # DEATH!
    # add grabbables to room 4
    r4.addGrabbable("6-pack")
    # add items to room 4
    r4.addItem("brew_rig", "Gourd is sensually brewing some sort of oatmeal stout\
on the brew rig. A 6-pack is resting   beside it.")
    r4.addItem("window", "After seeing Gourd shirtless now would be a perfect time to\
fling yourself into the          bottomless abyss that surrounds the mansion.... soooo whats stopping\
 you?")
##################################################################################################################
#Rooms 5-26 and all of their items/grabbables are original additions to the game.
#There is no ending to this game other than death. Your goal is to collect the items from the unnamed number of
#rooms in the mansion. Once you are satisfied with your results, or feel you have mastered the mansion and have
#found no new dialogue, you have reached the "end". The main purpose of this mansion game is to entertain rather
#than give a specific goal. You will die, and you will die a lot, but where is the fun in simply living?
#The game only supports the basic commands so don't waste time trying to eat/use anything you collect. Any
#collection is to simply bring satisfaction and humor to gameplay. Enjoy.
##################################################################################################################
    # add exits to room 5
    r5.addExit("east", r1) # -> to the east of room 5 is room 1 
    # add grabbables to room 5
    r5.addGrabbable("baby")
    # add items to room 5
    r5.addItem("crib", "Inside the Crib you see a Chubby Spider Baby throwing\
some mad gangster signs.")
    r5.addItem("super_toilet", "We don't talk about Super Toilet.")

    # add exits to room 6
    r6.addExit("east", r3) # -> to the east of room 6 is room 3 
    # add grabbables to room 6
    r6.addGrabbable("taco")
    # add items to room 6
    r6.addItem("taco_truck", "Why is there a taco truck? Well... Why not! Get a taco!")
    r6.addItem("derp_horse", "Its blank stare threatens to steal your soul, but part of\
 you doesn't want to look away.     Luckily it falls dead before it managed to steal your soul.")

    # add exits to room 7
    r7.addExit("north", r3) # -> to the north of room 7 is room 3
    r7.addExit("south", r8) 
    # add grabbables to room 7
    r7.addGrabbable("poop")
    # add items to room 7
    r7.addItem("normal_toilet", "Now this toilet we can talk about! Its full of poop.\
 Grabbing some may prove useful later.")
    r7.addItem("note", "If you took the poop.... that was a joke. You are now covered\
 and smell like my feces.")
    r7.addItem("front_door", "You may be wondering why there is a toilet near the front\
 entrance... Well the explaination for that is quite simple.... I have the Hershey Squirts.")

    # add exits to room 8
    r8.addExit("north", r7) # -> to the  of room  is room 
    r8.addExit("south", r9)
    r8.addExit("east", None)
    r8.addExit ("west", None)
    # add grabbables to room 
    r8.addGrabbable("crusty_old_barnacle")
    # add items to room 
    r8.addItem("awkward_sponge", "You see a strange sponge propped against the wall.\
 It appears to be wearing pants, and you swear that you can hear it scream.")
    r8.addItem("whale_blubber", "It's in a jar. The sticker on it simply says\
 'Pearl'. A crusty_old_barnacle rests beside it.")
    r8.addItem("blood_splatter", "There is writing on the wall written in\
 starfish blood. It reads, 'Are you feeling it now Mr. Krabs.")
    
    # add exits to room 9 
    r9.addExit("north", r8) # -> to the  of room  is room 
    r9.addExit("south", r10)
    r9.addExit("east", None)
    r9.addExit("west", None)
    # add grabbables to room 
    r9.addGrabbable("pinky_finger")
    # add items to room 
    r9.addItem("script", "Upon closer inspection you realize that\
 this is the sacred script of the greatest love story of\
all time, The Bee Movie. Your life has never felt so complete.")
    r9.addItem("chuck_norris", "You find yourself incapable of\
 looking at the greatness that is Chuck Norris. The mighty\
Chuck Norris allows you to have the honor of pulling his pinky_finger.\
You see Morgan Freeman singing a high octave. It is still low.")

    # add exits to room 10
    r10.addExit("north", r9) # -> to the  of room  is room 
    r10.addExit("south", r14)
    r10.addExit("east", None)
    r10.addExit("west", None)
    # add grabbables to room 
    r10.addGrabbable("vomit")
    # add items to room 
    r10.addItem("stack_of_books", "You look deeply into the covers.\
 You realize they are all of the failed manuscripts for 50\
 Shades of Grey. You vomit. Part of you wants to reclaim your vomit.")
    r10.addItem("spicy_memes", "Cash me ousside how bout dah.")

    # add exits to room 11
    r11.addExit("north", None) # -> to the  of room  is room 
    r11.addExit("south", None)
    r11.addExit("west", None)
    r11.addExit("east", r12)
    # add grabbables to room 
    r11.addGrabbable("small_ship")
    # add items to room 
    r11.addItem("iceberg", "You see a tiny iceberg complete with miniature\
 rioting polar bears on strike againt Global Warming.\
 Nearby you find a small_ship.")
    r11.addItem("small_ship", "It looks like a replica of a famous ship.\
 You feel the urge to pick it up and never let it go.")

    # add exits to room 12
    r12.addExit("north", None) # -> to the  of room  is room 
    r12.addExit("south", r18)
    r12.addExit("east", r13)
    r12.addExit("west", r11)
    # add grabbables to room 
    r12.addGrabbable("lucious_hair")
    # add items to room 
    r12.addItem("small_anky's", "You look around you to see hundreds of\
 miniature Anky's fighting each other with toothpicks and potato skins.\
You question your existence, and how you are still passing his class.")
    r12.addItem("gourd", "No, not the Doctor. Just a normal Gourd. But\
 with lucious_hair.")

    # add exits to room 13
    r13.addExit("north", None) # -> to the  of room  is room 
    r13.addExit("south", r19)
    r13.addExit("east", r14)
    r13.addExit("west", r12)
    # add grabbables to room 
    r13.addGrabbable("spicy_deets")
    # add items to room 
    r13.addItem("uncle_steve", "He offers you an apple for $500, but it catches on fire.")
    r13.addItem("uncle_bill", "He offers you a window for $500, but it shatters.")
    r13.addItem("uncle_snowden", "He offers you spicy_deets for FRREEEEEEEE!!!!!")

    # add exits to room 14
    r14.addExit("north", r10) # -> to the  of room  is room 
    r14.addExit("south", r20)
    r14.addExit("east", r15)
    r14.addExit("west", r13)
    # add grabbables to room 
    r14.addGrabbable("dragon_tears")
    # add items to room 
    r14.addItem("swamp_poster", "As you look into the poster you begin to feel a warm glow. It's Shrek. He caresses your shoulder and whispers, 'Shrek is love, Shrek is life'.\
 You faint and wake up feeling different than normal. But you think of it in a good way.")
    r14.addItem("tiny_donkey", "It's being eaten by a small dragon. It seems that\
 not all relationships are meant to last. You see some dragon_tears fall as she rips off\
 his head.")

    # add exits to room 15
    r15.addExit("north", None) # -> to the  of room  is room 
    r15.addExit("south", r21)
    r15.addExit("east", r16)
    r15.addExit("west", r14)
    # add grabbables to room 
    r15.addGrabbable("the_feels")
    # add items to room 
    r15.addItem("your_hopes", "You see the person you FAILED to admit your\
 feelings to. the_feels get to you.")
    r15.addItem("your_dreams", "You fall asleep and wake up nude. What?")

    # add exits to room 16
    r16.addExit("north", None) # -> to the  of room  is room 
    r16.addExit("south", r22)
    r16.addExit("east", r17)
    r16.addExit("west", r15)
    # add grabbables to room 
    r16.addGrabbable("yo_girl")
    # add items to room 
    r16.addItem("ponies", "You have strange flashbacks of your childhood.\
 You realize Friendship is not Magic. You cry.")
    r16.addItem("samurai", "He says his name is Jack. He's gotta get back,\
 back to the past. But on the way he tries to steal yo_girl. You gonna take that fam?")

    # add exits to room 17
    r17.addExit("north", None) # -> to the  of room  is room 
    r17.addExit("south", None)
    r17.addExit("east", None)
    r17.addExit("west", r16)
    # add grabbables to room 
    r17.addGrabbable("nickle")
    # add items to room 
    r17.addItem("nickleback", "It is a nickle with the tails side facing up,\
  what did you expect?.")
    r17.addItem("roach", "He looks at you and claims to be your papa.")

    # add exits to room 18
    r18.addExit("north", r12) # -> to the  of room  is room 
    r18.addExit("south", None)
    r18.addExit("east", r19)
    r18.addExit("west", None)
    # add grabbables to room 
    r18.addGrabbable("body_oil")
    # add items to room 
    r18.addItem("action_figure", "You know it's there. You know it's shredded....\
 but.... YOU JUST CAN'T SEE IT!!!!!")
    r18.addItem("fridge", "You open it and look around. Your weak human eyes\
 fail to see the hunk of man in front of you. You see some body_oil on one of the shelves.")

    # add exits to room 19
    r19.addExit("north", r13) # -> to the  of room  is room 
    r19.addExit("south", r23)
    r19.addExit("east", r20)
    r19.addExit("west", r18)
    # add grabbables to room 
    r19.addGrabbable("million_dollars")
    # add items to room 
    r19.addItem("nigerian_prince", "He smiles as you receive an email from him\
  thanking you for sending him money, he offers you the million_dollars he had\
  mentioned on ymail back in 2003.")
    r19.addItem("tom_anderson", "He drops to his knees and begs you to get back on MySpace.")

    # add exits to room 20
    r20.addExit("north", r14) # -> to the  of room  is room 
    r20.addExit("south", r24)
    r20.addExit("east", r21)
    r20.addExit("west", r19)
    # add grabbables to room 
    r20.addGrabbable("small_pence")
    # add items to room 
    r20.addItem("strange_sight", "You look to the ceiling to see a giant birds nest.\
  Inside Donald is feeding his Trumplings a small loan of a million dollars.")
    r20.addItem("juicy_pile", "It's beneath the nest. You are scared to touch\
  it but it seems to be covered in gold. The smell is awful. A small_pence rests on top.")

    # add exits to room 21
    r21.addExit("north", r15) 
    r21.addExit("south", r25)
    r21.addExit("east", r22)
    r21.addExit("west", r20)
    # add grabbables to room 
    r21.addGrabbable("pink_mustache")
    # add items to room 
    r21.addItem("pewdiepie", "He starts screaming for no reason at all and tries\
  #to either punch you or give you a fistbump. You choose to high-five his face.")
    r21.addItem("markiplier", "He stands gloriously with his crown of acorns made\
  by the finest squirrel blacksmiths around. He offers you his sacred pink_mustache.")

    # add exits to room 22
    r22.addExit("north", r16)  
    r22.addExit("south", None)
    r22.addExit("east", None)
    r22.addExit("west", r21)
    # add grabbables to room 
    r22.addGrabbable("small_pug")
     #add items to room 
    r22.addItem("tug_boat", "It seems to be pulling a small_pug around in a chocolate lake. It's Edgar. He is dead. He drowned in the chocolate.")
    r22.addItem("frail_bird", "Jk it's just Bernie Sanders. If you listen closely\
 he might offer you some free college.")

    # add exits to room 23
    r23.addExit("north", r19) # -> to the  of room  is room 
    r23.addExit("south", None)
    r23.addExit("east", r24)
    r23.addExit("west", None)
    # add grabbables to room 
    r23.addGrabbable("tissue")
    # add items to room 
    r23.addItem("darth_vader", "He looks at you disappointedly and questions\
  why you are still playing this game. He also tells you that you are adopted\
  and that he is not your father.")
    r23.addItem("maury", "He tell you to talk to Darth Vader and assures you\
  that what he says is true. He offers you a tissue.")

    # add exits to room 24
    r24.addExit("north", r20) # -> to the  of room  is room 
    r24.addExit("south", r26)
    r24.addExit("east", r25)
    r24.addExit("west", r23)
    # add grabbables to room 
    r24.addGrabbable("bird")
    # add items to room 
    r24.addItem("nothing", "It's nothing. Like.... what did you expect?")
    r24.addItem("bird", "It's a chubby little bird. I think it wants you to\
  take it with you.")

    # add exits to room 25
    r25.addExit("north", 21) # -> to the  of room  is room 
    r25.addExit("south", None)
    r25.addExit("east", None)
    r25.addExit("west", r24)
    # add grabbables to room 
    r25.addGrabbable("plate_of_tacos")
    # add items to room 
    r25.addItem("small_wall", "You look behind the wall and see a plate_of_tacos.")
    r25.addItem("clock", "The clock tells the time and the day of the week.\
  The hands are moving at an extremely fast rate but stop briefly\
  every Tuesday to open the gates of the small_wall.")

    # add exits to room 26
    r26.addExit("north", 24) # -> to the  of room  is room 
    r26.addExit("south", None)
    r26.addExit("east", None)
    r26.addExit("west", None)
    # add grabbables to room 
    r26.addGrabbable("small_book")
    # add items to room 
    r26.addItem("desk", "The desk is made of waxed oak. On it sits a small_book.\
  It was written by Mark Twain.")
    r26.addItem("table", "There is a cup of Joe steaming on top. This looks\
  like a great place for you to relax and read a good book. The room has a nice view too.")

    # set room 1 as the current room at the beginning of the game
    currentRoom = r1
#################################################################################################################
#################################################################################################################


# displays an appropriate "message" when the player dies
# yes, this is intentionally obfuscated!
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


####################################################################################


######################################################################
# START THE GAME!!!
inventory = [] # nothing in inventory...yet
createRooms() # add the rooms to the game

# play forever (well, at least until the player dies or asks to quit)
while (True):
    # set the status so the player has situational awareness
    # the status has room and inventory information
    status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)

    # if the current room is None, then the player is dead
    # this only happens if the player goes south when in room 4
    if (currentRoom == None):
        status = "You are dead."

    # display the status
    print "========================================================="
    print status

    # if the current room is None (and the player is dead), exit the
    # game
    if (currentRoom == None):
        death()
        break

    # prompt for player input
    # the game supports a simple language of <verb> <noun>
    # valid verbs are go, look, and take
    # valid nouns depend on the verb
    # we use raw_input here to treat the input as a string instead of
    # a numeric value
    action = raw_input("What to do? ")

    # set the user's input to lowercase to make it easier to compare
    # the verb and noun to known values
    action = action.lower()

    # exit the game if the player wants to leave (supports quit,
    # exit, and bye)
    if (action == "quit" or action == "exit" or action == "bye"):
        break


    # set a default response
    response = "I don't understand. Try verb noun. Valid verbs are \
go, look, and take"
    # split the user input into words (words are separated by spaces)
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
            for i in range(len(currentRoom.exits)):
                # a valid exit is found
                if (noun == currentRoom.exits[i]):
                    # change the current room to the one that is
                    # associated with the specified exit
                    currentRoom = currentRoom.exitLocations[i]

                    # set the response (success)
                    response = "Room changed."

                    # no need to check any more exits
                    break

        # the verb is: look
        elif (verb == "look"):
            # set a default response
            response = "I don't see that item."

            # check for valid items in the current room
            for i in range(len(currentRoom.items)):
                # a valid item is found
                if (noun == currentRoom.items[i]):
                    # set the response to the item's description
                    response = currentRoom.itemDescriptions[i]

                    # no need to check any more items
                    break 
            
        
        # the verb is: take
        elif (verb == "take"):
            # set a default response
            response = "I don't see that item."

            # check for valid grabbable items in the current room
            for grabbable in currentRoom.grabbables:
                # a valid grabbable item is found
                if (noun == grabbable):
                    # add the grabbable item to the player's
                    # inventory
                    inventory.append(grabbable)

                    # remove the grabbable item from the room
                    currentRoom.delGrabbable(grabbable)

                    # set the response (success)
                    response = "Item grabbed."

                    # no need to check any more grabbable items
                    break

        # display the response
        print "\n{}".format(response)







           
















