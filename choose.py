# Choose.py
# by Wylder G., Tabor F., 
# Description: starter code for the Choose Your
# Own Adventure Project

# Music
'FL Studios Gunshot FX'
'John Coltrane: In a Sentimental Mood'

# Import Statements
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox
import os

root = Tk()
w = Label(root, text="Choose Your Own Adventure")
w.pack()

# Beginning Dialogue
os.startfile('coltrane.mp3')
messagebox.showinfo("...", "July 10th, 2023. A day at work.")
messagebox.showinfo("Prologue", "'Congratulations on this "
                        "new position. It's gonna be a brand n"
                        "ew start for you as one of my detecti"
                        "ves. Hopefully things don't get too bo"
                        "ring for you. For now, rest up until "
                        "tomorrow. Enjoy your night.'")
name = simpledialog.askstring("Prologue", "'By the way, what was"
                                   " your name again?")
messagebox.showinfo("Prologue", "" + name + ", I'll remember that.")
messagebox.showinfo("Prologue", "Later that night.")
messagebox.showinfo("Prologue", "'Too many papers tonight..."
                        " Hey, excuse me sir. No visitors after-")
os.startfile('gunshot.mp3')
messagebox.showinfo("Prologue", "BANG")
messagebox.showinfo("A New Case", "The next day.")
os.startfile('coltrane.mp3')
messagebox.showinfo("A New Case", "You're excited for a new"
                        " start at your workplace. In your car, "
                        "you notice sirens near the building an"
                        "d as you get closer see investigators. "
                        "As you park your car and rush to the s"
                        "cene, you can't help but think your fi"
                        "rst case might be coming sooner than y"
                        "ou thought.")
messagebox.showinfo("A New Case", "'What happened?' you ask one of the"
                        " nearby officers.")
messagebox.showinfo("A New Case", "\n'The boss, he was shot and killed', he answers."
                        "\n    " 
                        "\n'What!?' you yell out in surprise. Quickly you, cal"
                        "m down and walk a short distance away from everyone."
                        "You realize that your next move could change you ent"
                        "ire life and career.")

def intro():
    """ Introductory Function -> starts the story going """

    choice = simpledialog.askinteger("A New Case", "\n What will you do?" + \
                                 "\n (1) Take on the case yourself in secret" + \
                                 "\n (2) Ignore the situation and walk away" + \
                                 "\n (3) Quit the job at the agency" + \
                                 "\n (4) Pursue vengeance on the people that did this")
                                 
    if choice == 1:
        iwork()
    elif choice == 2:
        iignore()
    elif choice == 3:
        iquit()
    elif choice == 4:
        ivengence()
    else:
        intro()

################ Amiel's Functions #####################

# I still need to finish THESE before I can continue
"""
]iwork2_2, 3
]iwork4_1
"""
def iwork():
    messagebox.showinfo("Secrecy and Solitude", "You decide to work in"
                        " secrecy and solitude. What is your next choice?")
    choice = simpledialog.askinteger("Secrecy and Solitude",
                                     "(1) Go back to the crime scene; Reinvestigate"
                                     "\n(2) Re-interrogate your prime suspect"
                                     "\n(3) Go over your evidence once more")
    if (choice == 1):
        messagebox.showinfo("Secrecy and Solitude",
                            "You go back to the crime scene to reinvestigate, and"
                            " find a new letter. You open the letter and it says"
                            "\n\n    'TO: ROBERT M: Great job on the hit Robert, that"
                            " detective won't be snooping in private affairs anymore"
                            ", here is the $15,000, as promised' -S ")
        iwork2_1()
    elif (choice == 2):
        messagebox.showinfo("Secrecy and Solitude",
                            "You see him in the nearby alleyway, on the way to"
                            " his home, harassing an innocent woman.")
        iwork2_2()
    elif (choice == 3):
        messagebox.showinfo("Secrecy and Solitude",
                            "You find new evidence in an hour log that gives"
                            " your prime suspect the time to commit the murder")
        iwork2_3()
    else:
        iwork()

def iwork2_1():
    choice = simpledialog.askinteger("Secrecy and Solitude",
                                     "(1) Hah, what nonsense"
                                     "\n (2) It seems careless for a criminal mastermind like 'S' to"
                                     " slip up like this, I should investigate. Who is this 'Robert M'?")
    if (choice == 1):
        messagebox.showinfo("Secrecy and Solitude",
                            "It seems you just gave up your only lead by sheer lack of interest."
                            " Your story ends here")
    elif (choice == 2):
        messagebox.showinfo("Secrecy and Solitude",
                            "Robert Malcone, 13 counts of armed robbery, 2 counts"
                            "of manslaughter, and suspect for dozens of murder"
                            "cases; street alias, 'The Gun'"
                            "\n\nRobert must be the hired hand for whoever 'S' is.")
        messagebox.showinfo("Secrecy and Solitude",
                            "You now can either freelance with this new information, or give"
                            " this information to the police"
                            "\n\nDo you follow up freelance, or go to the police with this newfound information?")
        iwork3_1()
    else:
        iwork2_1()
    
def iwork3_1():
    choice = simpledialog.askinteger("Secrecy and Solitude",
                                     "(1) Follow up on Roberts possible ties to the hit"
                                     "\n(2) Give this newfound information to the police")
    if (choice == 1):
        messagebox.showinfo("Secrecy and Solitude",
                            "You discover that Robert had also been working as a 'collection"
                            " agent' for the Mafia. His boss is none other than the elusive 'Silvone'."
                            " Silvone must be 'S'")
        messagebox.showinfo("Secrecy and Solitude",
                            "This man... Silvone, epiphany of a scumbag, murderer of innocent"
                            " men, women, and children all alike. This dirtbag deserves to die..."
                            " Should I murder this man? Chances are he might get out again if"
                            " I bring him to the station... Rich men walk. But if I kill him, I stoop to"
                            " his level")
        iwork4_1()
    elif (choice == 2):
        messagebox.showinfo("Secrecy and Solitude",
                            "The other detectives see you have become too invested in the case,"
                            " and with this newfound information, they are able to take the case"
                            " away from you. You lose control of the case")
    else:
        iwork3_1()
################ Niraj's Functions #####################
def iignore():
    messagebox.showinfo("The Detective Allergic to Murders",
                        "You decide to ignore the case despite some people"
                        " looking at you for answers. 'Well, it's just gonna"
                        " have to be someone else' you think. Lost in your t"
                        "houghts, you fail to notice a shady figure overlooking"
                        " the whole scene.")
    messagebox.showinfo("The Detective Allergic to Murder",
                        "The next day...")
    messagebox.showinfo("The Detective Allergic to Murder",
                        "Going through your usual morning routine,"
                        " you drive to work. There, you see the same"
                        " situation as yesterday and the situation seems "
                        "strangely familiar.")
    messagebox.showinfo("The Detective Allergic to Murder",
                        "You see the partner that was assigned to you"
                        "\n the other day and ask, 'What happened here?'" + \
                        "\n"
                        "\n 'Another murder happened, and it ain't pretty'"
                        ", he promptly answers."
                        "\n"
                        "\n You stand there shocked. Another murder? What to "
                        "do now...")
    ignore()
def ignore():
    choice = simpledialog.askinteger("The Detective Allergic to Murder",
                                     "\n(1) Work. This case could"
                                     " be your last if you're not careful" + \
                                     "\n(2) Give the lie you did it and confess for your sins."
                                     "\n(3) Ignore the murder. Not your problem")
    if (choice == 1):
        work()

    elif (choice == 2):
        confess()
    elif choice == 3:
        nope()
    else:
        ignore()
def work():
    messagebox.showinfo("Accepting Fate",
                        "You finally realize that something's up and it's"
                        " about time you took action. You head to the "
                        "headquarters to finalize your decision.")
def confess():
    messagebox.showinfo("A Stupid Liar",
                        "You lose your mind and confess to the two murders that"
                        " have happened. Absolutely no one believes you and"
                        " this results you being stripped of your badge "
                        "and sent to an asylum for mental analysis. Thus"
                        " ends your career as a detective.")
    messagebox.showinfo("A Stupid Liar",
                        "INSANITY ENDING")
def ignore2():
    messagebox.showinfo("The Next Victim",
                        "Late at night, you're looking at other cases th"
                        "at might be available for you. Suddenly the door"
                        "\n opens." + \
                        "\n 'Detective " + name + "?'")
    messagebox.showinfo("The Next Victim",
                        "Turning around you answer the person who"
                        " called. 'Yes that's me. How may I-")
    os.startfile('gunshot.mp3')
    messagebox.showinfo("The Next Victim", "BANG")
    messagebox.showinfo("The Next Victim",
                        "Bleeding out, you see the killer walking away "
                        "with confidence. 'Idiot', you think to yourself."
                        " Pulling out your gun you shoot the killer who"
                        " instantly goes down. You smile."
                        " At least you go down as a hero.")
    messagebox.showinfo("The Next Victim",
                        "FALSE HERO ENDING")
################ Robat's Row Row Row your boat gently down the stream robat Functions #####################
def iquit():
    choice = simpledialog.askinteger("Quiter",
                                     "You decide that the life you've always wanted "
                                     "as a detective is not suitable to live. It's too dangerous "
                                     "for you to take the risk of working there after someone just got killed."
                                     "\n You realize you don't have milk at home. "
                                     "\n Do you want to (1) go straight home or (2) stop by the store?")
    if (choice == 1):
        qhome()
        
    elif (choice == 2):
        qstore()
        
    else:
        iquit()

def qstore():
    choice = simpledialog.askinteger("Getting Milk",
                                     )

def qhome():
    choice = simpledialog.askinteger("Going Home",
                                     "You decide to go home but you want to get home quickly. "
                                     "There is a path up ahead that will get you home much quicker, "
                                     "but you have never been down it before and it's a bit sketchy."
                                     "\n Do you want to (1) take the shortcut or (2) go the long route?")
    if (choice == 1):
        ()
        
    elif (choice == 2):
        ()
        
    else:
        qhome()



 ################ GiveMeYourMilk Functions #####################
        #204863 204863 204863 204863 204863 204863
def ivengence():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        vignore()

    elif (choice == 2):
        vfollow()

    else:
        ivengence()

def vignore():
    messagebox.showinfo("END",
                        "You look at the letter, put it down and"
                        " walk away. That letter isn't what you "
                        "need right now. You're barely a detective "
                        "you're not a world class ninja spy assassin."
                        " As you walk away you realise that was it,"
                        " you're last chance to live out your dream"
                        " of being a classic detective like the ones"
                        " your grandfather would tell you about watching"
                        " in classic films and now it's over now. You walk home"
                        " with your head hung low, knowing that your"
                        " dream is lost.")
def vfollow():
    choice = simpledialog.askinteger("Rooftop",
                                     "story goes here(capture hitman on rooftop)"
                                     "\n Kill him(1) or Question him(2)")
    if (choice == 1):
        fkill()

    elif (choice == 2):
        fquestion()

def fkill():
    choice = simpledialog.askinteger("Killer",
                                     "What will you do with his body?"
                                     "\n Hide it(1) or Display it(2)")
    if (choice == 1):
        khide()

    elif (choice == 2):
        kdisplay()

################ Winikka's Functions #####################
# Note this is an alert of the Winikka Broadcast System
# This is only a test
# Winikka is not really going to code a function here
# If he were to code, he would put it here.
# This is just to show you how to collaborate using Git

################ Main #####################
intro()

root.destroy()
