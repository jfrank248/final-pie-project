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

Label(master, text="Weapons Systems Password: ").grid(row=0)
e1 = Entry(master)
if password == RandPassGen():
    #covers the situation in which the password was correct
    print('Password {} Accpeted! Firing Weapons Systems!'.format(password))
    #End Game Sequence Code should be inserted here
    print('Here is a small reward for all of your hard work!')
    sleep(5)
    EndGame()


e1.grid(row=0, column=1)


mainloop( )
