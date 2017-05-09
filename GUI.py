from Tkinter import *


master = Tk()
Label(master, text="""Good Day Captain. Today is xx/xx/xxxx. The invasion of Earth as begun./
As Martian High Commander it is your duty to lead the Armada, but before we can
attack we must reactivate our long dormant weapons systems. The process is tedious
but without it we can not accomplish our mission. Your are our only hope. Activate
the weapons systems and destroy the puny earthlings, but be careful. If the weapons
system password is keyed incorrectly three times the ship will self-destruct.
It is a foolish concept we know, but it was implemented by the Mar's High
Council to prevent espionage and terror attacks. Good luck Captain! Note: Type
"Command Override. Password Recovery." to progress deeper into the game when
the password input is displayed. Good Luck!""").grid(row=0)




mainloop( )


master = Tk()




while MyGlobalTries > 0:    
	password = Label(master, text="Weapons Systems Password: ").grid(row=0)
	e1 = Entry(master)
	if password == RandPassGen():
        #covers the situation in which the password was correct
    	Label(master, text = 'Password {} Accpeted! Firing Weapons Systems!'.format(password))
        #End Game Sequence Code should be inserted here
        Label(master, text ='Here is a small reward for all of your hard work!')
        sleep(5)
        EndGame()
        
    elif password == "Command Override. Password Recovery.":
        beginSimSeq = Label(master, text = 'Would you like to solve the Sequence to recover the password? Yes or No?: ')
		e2 = Entry(master)
        if beginSimSeq == "Yes":
            while myGlobal < 3:
                SimonGameSeq()

            #Prints the password once the player achieves his/her simSeq
            else:
                Label(master, text = """Fantastic Job Captain! You now how the key to activate the
                weapons systems and defeat the Earthlings. All thats left now is to
                activate the guns. Good luck Captain.""")
                Label(master, text = "RandPassGen()")
                PassReq()

        elif beginSimSeq == "No":
            Label(master, text = "Very Well. The option still remains. You must wait 15s to retry, but it is your final attempt.")
            sleep(15)
            Label(master, text = 'Would you like to solve the Sequence to recover the password? Yes or No?: ')
            e3 = Entry(master)

            if beginSimSeq == "Yes":
                #runs the game until the player successfully completes it 3 times in a row
                while myGlobal < 3:
                    SimonGameSeq()

                    #Prints the password once the player achieves his/her simSeq
                else:
                    Label(master, text = """Fantastic Job Captain! You now how the key to activate the
                    weapons systems and defeat the Earthlings. All thats left now is to
                    activate the guns. Good luck Captain.""")
                    Label(master, text = "RandPassGen()"
                        
            elif beginSimSeq == "No":
                Label(master, text = "Mission Failed!")
                death()
                #print a death icon/end game function here
    else:
        #covers the situation in which the password was wrong
        Label(master, text ="Incorrect password. You have {} tries remaining!".format(myGlobalTries)
        password = Label(master, text ='Weapons Systems Password: ')
        myGlobalTries -= 1

else:
    death()


e1.grid(row=0, column=1)


mainloop( )
