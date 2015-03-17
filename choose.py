# Choose.py
# by Wylder G., Tabor F., 
# Description: starter code for the Choose Your
# Own Adventure Project

# Import Statements
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox

root = Tk()
w = Label(root, text="Choose Your Own Adventure")
w.pack()

# Beginning Dialogue
messagebox.showinfo("...", "July 10th, 1999. A day at work.")
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
#os.startfile('Gunshot.mp3')
messagebox.showinfo("A New Case", "The next day.")
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
################ Student B Functions #####################
def iignore():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            "You chose right.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok.  THE END")
    else:
        choice2()

################ Robat's Functions #####################
def iquit():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            "You chose right.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok.  THE END")
    else:
        choice2()

################ Student D Functions #####################
def ivengence():
    choice = simpledialog.askinteger("Choose wisely",
                                     "This is the next part of the story.  Now you must choose 1 or 2 again.")
    if (choice == 1):
        messagebox.showinfo("The End",
                            "You chose right.  THE END")

    elif (choice == 2):
        messagebox.showinfo("The End",
                            "You chose ok.  THE END")
    else:
        choice1()

################ Winikka's Functions #####################
# Note this is an alert of the Winikka Broadcast System
# This is only a test
# Winikka is not really going to code a function here
# If he were to code, he would put it here.
# This is just to show you how to collaborate using Git

################ Main #####################
intro()

root.destroy()
