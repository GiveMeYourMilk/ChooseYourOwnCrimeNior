# Choose.py
# by Wylder G., Tabor F., Amiel I., Niraj M.
    ########################################
    #Starring Niraj M. as Malin383         #
    #And Tabor F. as robat81               #
    #Also Amiel I. as amiel445566          #
    #featuring Wylder G. as GiveMeYourMilk #
    ########################################
# Description: starter code for the Choose Your
# Own Adventure Project

# Music
'FL Studios Gunshot FX'
'John Coltrane: In a Sentimental Mood'
'Pokemon: Wallys Theme'
'Seinfeld Theme'

# Import Statements
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox
import os

root = Tk()
w = Label(root, text="Choose Your Own Adventure")
w.pack()

# Beginning Dialogue
def intro():
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
    intro2()

def intro2():
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

    ### MAP OF FUNCTIONS ###
"""
]1_1
    ]2_1
        ]3_1
            ]4_1
    ]2_2
        ]3_2
            ]4_2
                ]5_1
    ]2_3
        ]2_2
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
                            "Robert Malcone, 13 counts of armed robbery, 2 counts "
                            "of manslaughter, and suspect for dozens of murder "
                            "cases; street alias, 'The Gun'"
                            "\n\nRobert must be the hired hand for whoever 'S' is.")
        messagebox.showinfo("Secrecy and Solitude",
                            "You now can either freelance with this new information, or give"
                            " this information to the police"
                            "\n\nDo you follow up freelance, or go to the police with this newfound information?")
        iwork3_1()
    else:
        iwork2_1()

def iwork2_2():
    choice = simpledialog.askinteger("Secrecy and Solitude",
                                     "(1) 'Hey, Giordini, I have some questions to ask you!'"
                                     "\n(2) Oh... this dirtbag is just ASKING FOR IT! (knuckle cracking)")
    if (choice == 1):
        messagebox.showinfo("Secrecy and Solitude",
                            "He bolts off")
        iwork3_2()
    elif (choice == 2):
        messagebox.showinfo("Secrecy and Solitude",
                            "The fight is over quickly, for his only real targets of his 'collections' are "
                            "the elderly...")
        messagebox.showinfo("Secrecy and Solitude",
                            "Although it seemed right at the time, this was in fact a poor choice. "
                            "Giordini now refuses to cooperate with the police in the attempt "
                            "to find out who really killed your boss.")
        messagebox.showinfo("Secrecy and Solitude",
                            "Along with all this, you are being sued by copious amounts of "
                            "agencies, the likes of many that you had not even knew existed. "
                            "It seems your days of working detective are over.")
    else:
        iwork2_2()

def iwork2_3():
    choice = simpledialog.askinteger("Secrecy and Solitude",
                                     "(1) Reinterrogate your prime suspect. Discuss new information "
                                     "with him (get some answers)"
                                     "\n (2) Turn over new evidence to the police, a full force is "
                                     "stronger than one man")
    if (choice == 1):
        messagebox.showinfo("Secrecy and Solitude",
                            "You see him in the nearby alleyway, on the way to"
                            " his home, harassing an innocent woman.")
        iwork2_2()
    elif (choice == 2):
        messagebox.showinfo("Secrecy and Solitude",
                            "When you turn over the case, your co-workers could see that "
                            "this case was distressing you, so they relieve you when they "
                            "get access to this new evidence. You can no longer work on the "
                            "case")
    else:
        iwork2_3()

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

def iwork3_2():
    choice = simpledialog.askinteger("Secrecy and Solitude",
                                     "(1) Chase him"
                                     "\n(2) Shoot him")
    if (choice == 1):
        messagebox.showinfo("Secrecy and Solitude",
                            "You follow him to his hideout, and hear ludicrous amounts of cursing, "
                            "then you hear Giordini talking to one another")
        messagebox.showinfo("Secrecy and Solitude",
                            "'Did that cop follow you here?' 'Who do you take me for?, I'm 'The Gun', "
                            "Its not hard to outrun a pig")
        iwork4_2()
    elif (choice == 2):
        messagebox.showinfo("Secrecy and Solitude",
                            "He died, what did you expect")
        messagebox.showinfo("Secrecy and Solitude",
                            "You lost your only lead because you forgot what a gun does. Good job.")
    else:
        iwork3_2()

def iwork4_1():
    choice = simpledialog.askinteger("Secrecy and Solitude",
                                     "(1) End his life"
                                     "\n(2) Bring him in yourself")
    if (choice == 1):
        messagebox.showinfo("Secrecy and Solitude",
                            "In a storm of rage, and short-sightedness, you pull the trigger. "
                            "This for only a breif moment are you relieved as you are brought "
                            "into custody yourself for murder in the first degree.")
    elif (choice == 2):
        messagebox.showinfo("Secrecy and Solitude",
                            "You bring him in, and are greeted with promotion, relief and "
                            "celebrations of all sorts. You find that bringing him in has alleviated "
                            "your troubles and you can finally move on. Thorugh this capture you "
                            "end up taking the position as lead detective, and replace your old "
                            "boss.")
    else:
        iwork4_1()

def iwork4_2():
    choice = simpledialog.askinteger("Secrecy and Solitude",
                                     "(1) Call for backup (running for police is a probable cause "
                                     "for a search warrent)"
                                     "\n(2) Go in vigilante, you can't risk losing you handle on this "
                                     "case")
    if (choice == 1):
        messagebox.showinfo("Secrecy and Solitude",
                            "They hear you calling for backup outside of their hideout. "
                            "It seems you still haven't mastered the art of not talking loudly. "
                            "They bring you in before you can disclose the location of the "
                            "hideout to the police.")
        messagebox.showinfo("Secrecy and Solitude",
                            "After hours of torture, they assume you are just a goon of the "
                            "police, and that you know nothing. They let you go, but not "
                            "before adequate bruising")
        messagebox.showinfo("Secrecy and Solitude",
                            "You overheard their chatter as they move their hideout to a "
                            "new location, 'Hey Silvone, this guy is just a dunce, knows "
                            "nothing. Wouldn't want more heat drawn to another murder. "
                            "*chatter*, yeah we messed him up good, we wont talk.")
        messagebox.showinfo("Secrecy and Solitude",
                            "'SILVONE', you think in your head (as you learned your lesson "
                            "about talking loudly last time), he is the head of the mafia, and "
                            "now we have probable cause to search his offices. We can finally "
                            "bring him down!")
        iwork5_1()
    elif (choice == 2):
        messagebox.showinfo("Secrecy and Solitude",
                            "You get shot. C'mon it's a hideout of armed assailants.")
    else:
        iwork4_2()

def iwork5_1():
    choice = simpledialog.askinteger("Secrecy and Solitude",
                                     "(1) 'Silvone will get out if I don't take care of him; I need to "
                                     " kill him so his lawyers don't get him out again.'"
                                     "\n(2) 'This time, we have REAL evidence, we need to pursue "
                                     "the LEGAL path")
    if (choice == 1):
        messagebox.showinfo("Secrecy and Solitude",
                            "You are there, holding a gun to his face, past all his handcuffed "
                            "goons, all struggling to make sure you don't kill thier meal ticket. "
                            "You do the only thing left and pull the trigger.")
        messagebox.showinfo("Secrecy and Solitude",
                            "BANG, Silvone is dead, and now you are in jail, good going.")
    elif (choice == 2):
        messagebox.showinfo("Secrecy and Solitude",
                            "You go back over evidence, and discover that the gun the "
                            "hitman used on your superior and the guns used in crimes "
                            "assosiated with 'S' are in fact from the same weapon. The "
                            "hitman is just a hired hand and Silvone, and now you have the "
                            "real evidence to prove the injustice Silvone has caused.")
        messagebox.showinfo("Secrecy and Solitude",
                            "You bring him in, and are greeted with promotion, relief and "
                            "celebrations of all sorts. You find that bringing him in has alleviated "
                            "your troubles and you can finally move on. Thorugh this capture you "
                            "end up taking the position as lead detective, and replace your old "
                            "boss.")
    else:
        iwork5_1()
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
    messagebox.showinfo("Accepting Fate",
                        "\n'Hey, bro', you call out to your partner." + \
                        "\n"
                        "\n'Yo, what up?', he replies."
                        "\n"
                        "\n'I'm gonna take up that case. Regarding the murder"
                        " in the agency.'")
    messagebox.showinfo("Accepting Fate",
                        "At first, your partner looks at you shocked. "
                        "Then he smiles, as if not surprised by your deci"
                        "sion. 'Heh, it's about time. Here's all the data"
                        ". The crime scenes are still fresh so you should che"
                        "ck them out before they go stale. Time to show off "
                        "your skills rookie.'"
                        "\n" + \
                        "\nYou look at him and smile. Turning around you begin"
                        " the investigation.")
    victims()
def victims():
    choice = simpledialog.askinteger("Accepting Fate",
                                     "\nYou check the files and see there's not" + \
                                     " much to go off of. You're going to have to"
                                     " check out the victims yourself. But which one?"
                                     "\n"
                                     "\n(1)Check out the first victim, your boss"
                                     "\n(2)Check out the second victim")
    if choice == 1:
        victim1()
    elif choice == 2:
        victim2()
    else:
        victims()
def victim1():
    messagebox.showinfo("First Hit",
                        "Deciding to check on the first victim, you walk tow"
                        "ards the crime scene. You look at the files and see"
                        " that there's not much to go off of. Jack Robinson, th"
                        "e man  that gave you this job. Trying to shake off the"
                        " feeling of nostalgia, you reach the crime scene and"
                        " investigate.")
    messagebox.showinfo("First Hit",
                        "'What's this?' you think to yourself, seeing a small "
                        "letter, seemingly hiding in the corner. A lot of the"
                        " commotion is with the fresh second victim, so this"
                        " crime scene is seemingly empty. Picking up the letter"
                        ", you begin to read it to yourself. Or at least"
                        ", what's legible.")
    messagebox.showinfo("First Hit",
                        "\nTo: S------" + \
                        "\n"
                        "\nI'll g---ly take that deal. In fact, j--t get the"
                        " money read- by tomorrow. The job will be done before"
                        " yo-'r- even awake."
                        "\n"
                        "\nRo--er- Mal-c--e")
    vic1()

def vic1():    
    choice = simpledialog.askinteger("First Hit",
                                     "\nYou can clearly see that two people w"
                                     "ere involved and what the plot was but "
                                     "the names are not very clear. It's time "
                                     "to try and close in on the suspects."
                                     "\n"
                                     "\n(1)Give the letter to a lead analyzer"
                                     "\n(2)Investigate the crime scene further")
    if choice == 1:
        analyze()

    elif choice == 2:
        investigate()

    else:
        vic1()
def analyze():
    messagebox.showinfo("Robert Malcone and S",
                        "Nothing seems to be present, so you decide to leave"
                        " the crime scene. You decide to give the letter to "
                        "a lead analyzer, who begins work on it right away. "
                        "While making yourself a cup of joe, he comes running"
                        " too you. 'Wow, that was quick' you think.")
    messagebox.showinfo("Robert Malcone and S",
                        "\n'Sir! The killer, it's the hitman Robert Malcone!'" + \
                        " he says with panic in his voice."
                        "\n"
                        "\n'Alright, we'll get on that right away...' you begin bu"
                        "t stop as the analyzer looks very scared.")
    messagebox.showinfo("Robert Malcone and S",
                        "\n'What's wrong?' you ask him." + \
                        "\n"
                        "\n'The 'S' in the letter it's...it's...it's Silvone."
                        "\n"
                        "\nYou drop your mug and stare. A few seconds later, you"
                        "'re in your car, driving towards the mobsters hideout.")
    messagebox.showinfo("Robert Malcone and S",
                        "You have reached his hideout and are ready to go in."
                        " This is it. With your sleuthing skills, you man"
                        "age to get in and are there. And who is sitting there?"
                        " None other than the killer and the boss. Robert Malc"
                        "one and Silvone.")
    choice = simpledialog.askinteger("Robert Malcone and S",
                                     "\nThis is it, the time has come. What" + \
                                     " will you do?"
                                     "\n"
                                     "\n(1)An eye for an eye"
                                     "\n(2)Close your case")
    # Wylder, analyze() function  will lead to one of yours functions finish up
        #next class

    
def investigate():
    messagebox.showinfo("Third Hit",
                        "\nDeciding to investigate further, you look for more ev" + \
                        "idence but fail to find any. Turning to leave, you come"
                        " face to face with a pistol."
                        "\n"
                        "\n'Ha, forgot to send that letter', the shooter tells you."
                        " 'Robert Malcone by the way.'")
    messagebox.showinfo("Third Hit",
                        "Pulling the trigger, no chance of survival is possible."
                        " Within a minute, you die and the only piece of eviden"
                        "ce is gone and the hitman is now free.")
    messagebox.showinfo("Third Hit",
                        "INVESTIGATOR ENDING")
def victim2():
    messagebox.showinfo("Second Hit",
                        "You decide to check up on the second victim. Looking"
                        " at the files, you see he was a moderately new detecti"
                        "ve, and feel a pang of guilt for not taking the case "
                        "sooner. Shaking off the feeling, you approach the "
                        "crime scene and show your badge.")
    messagebox.showinfo("Second Hit",
                        "\n'Sir!', an officer says, approaching you. 'We've fou" + \
                        "nd some evidence on the killer. It's seems to be a"
                        " scrapbook.'"
                        "\n"
                        "\n'Thank you', you say, taking the notebook. 'Is ther"
                        "e any other evidence? Fingerprints, weapons, or some"
                        "thing of the sort?'"
                        "\n"
                        "\n'No sir', he answers. 'Whoever this guy was, he ma"
                        "de a slip and this is all we got.'")
    messagebox.showinfo("Second Hit",
                        "Thanking the officer you walk away. Evidence is a "
                        "good start. Looking out, you see that the commotion aroun"
                        "d the crime scene has died down. The day's almost"
                        " ended.")
    vic2()
    
def vic2():
    choice = simpledialog.askinteger("Second Hit",
                                     "\nWhat will you do?" + \
                                     "\n(1)Go home and rest for the day"
                                     "\n(2)Investigate the evidence imme"
                                     "diately")
    if choice == 1:
        lose()
    elif choice == 2:
        killer()
    else:
        vic2()
def lose():
    messagebox.showinfo("The Only Evidence",
                        "Heading home, you take this evidence with you"
                        ". Once home you head inside and crash on your"
                        " couch, instantly falling asleep from all the"
                        " stress. 'So sleepy' you think, drifting away.")
    messagebox.showinfo("The Only Evidence",
                        "All of a sudden, you hear a large crash. Instantly"
                        " getting up, you look around and see a man stormin"
                        "g your house. He points a gun at you while you ner"
                        "vously watch him.")
    messagebox.showinfo("The Only Evidence",
                        "\n'Sorry about this', the man says. 'I forgot this at"
                        " that detective agency.'" + \
                        "\n"
                        "\n'You're the shooter?' you ask in shock."
                        "\n"
                        "\n'The one and only', he replies. 'I normally would"
                        " leave you alone, but just in case...' He points hi"
                        "s gun at you and shoots you in the leg.")
    messagebox.showinfo("The Only Evidence",
                        "You crumple over and are helpless to watch the killer"
                        " take the scrapbook. The only evidence you had against"
                        " the killer is now gone. In the near future, you are"
                        " known as a failed detective and continued killings "
                        "occur. This takes a big hit on you and you vow never"
                        " to take another case ever again.")
    os.startfile('fail.mp3')
    messagebox.showinfo("The Only Evidence",
                        "FAILED DETECTIVE ENDING")
def killer():
    messagebox.showinfo("The Killer",
                        "You decide to investigate the scrapbook immediately,"
                        " figuring there's no point in resting when you've fou"
                        "nd some crucial evidence. Grabbing some of the top ev"
                        "idence analyzers in the agency. By the end of the day,"
                        " you have a pretty clear idea of who the killer is.")
    messagebox.showinfo("The Killer",
                        "Later that evening...")
    messagebox.showinfo("The Killer",
                        "\n'Detective " + name + "?'" + \
                        "\n"
                        "\n'Yes?'"
                        "\n"
                        "\nThe cocking of a pistol. 'I'm here for that scrap"
                        "book. So if you wanna leave alive, then I suggest-'"
                        "\n"
                        "\n'Freeze!'")
    messagebox.showinfo("The Killer",
                        "The killer has fallen right into your trap. Suspecting"
                        " he would come after you next, a decoy was sent in you"
                        "r place. And the killer was who you suspected it was; "
                        "Robert Malcone, a hired hitman. The scrapbook was intac"
                        "t enough that you could recognize similarities as well a"
                        "s the history. But after interrogation, he refuses to "
                        "say who hired him. A successful case closed, but a new "
                        "one has now unfolded.")
    messagebox.showinfo("The Killer",
                        "CASE CLOSED? ENDING")

def confess():
    os.startfile('seinfeld.mp3')
    messagebox.showinfo("A Stupid Liar",
                        "You lose your mind and confess to the two murders that"
                        " have happened. Absolutely no one believes you and"
                        " this results you being stripped of your badge "
                        "and sent to an asylum for mental analysis. Thus"
                        " ends your career as a detective. Oh, you also"
                        " compromised  all other existing relationships.")
    messagebox.showinfo("A Stupid Liar",
                        "INSANITY ENDING")
def nope():
    messagebox.showinfo("The Next Victim",
                        "Late at night, you're looking at other cases th"
                        "at might be available for you. Suddenly the door"
                        " opens." + \
                        "\n"
                        "\n'Detective " + name + "?'")
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
    os.startfile('falsehero.mp3')
    messagebox.showinfo("The Next Victim",
                        "FALSE HERO ENDING")
################ Robat's Row Row Row your boat gently down the stream robat Functions #####################
    ### TEST ###
def iquit():
    choice = simpledialog.askinteger("Quiter",
                                     "You decide that the life you've always wanted "
                                     "\n as a detective is not suitable to live."
                                     "\n It's too dangerous for you to take the risk of"
                                     "\n working there after someone just got killed."
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
                                     " It was a short walk to the store, but once you got"
                                     "\n to the store you couldnt find the milk. Walking"
                                     "\n around a bit you finally find the dairy aisle,"
                                     "\n however they only have one gallon of each milk type"
                                     "\n Do you take the (1) 1% milk or (2) the Whole milk")
    if (choice == 1):
        q1%()
        
    elif (choice == 2):
        qwhole()
        
    else:
        qstore()


def qhome():
    choice = simpledialog.askinteger("Going Home",
                                     "You decide to go home but you want to get home quickly. "
                                     "\n There is a path up ahead that will get you home much quicker, "
                                     "\n but you have never been down it before and it's a bit sketchy."
                                     "\n Do you want to (1) take the shortcut or (2) go the long route?")
    if (choice == 1):
        qshortcut()
        
    elif (choice == 2):
        qnormal()
        
    else:
        qhome()

def qnormal():
    messagebox.showinfo("Going Home",
                        "Theres no point in going down some sketchy road at dusk."
                        "\n Any other day you would have been all over this new road,"
                        "\n exploring this path and trying to play some detective game"
                        "\n as you waited to hear back from the agency. However, that life"
                        "\n is all behind you now. You start to wonder how your life"
                        "\n will change. After all, you quit the job you worked so hard to get."
                        "\n Little did you know this was the last thing that was on your mind."
                        "\n Even though you went the normal way home you still felt rushed."
                        "\n Quickly you decide to cross the street. As you cross the street,"
                        "\n you feel a sensation. You look up and all you see is the blinding"
                        "\n lights of a car. You can barely breath as everything goes black...")

    messagebox.showinfo("Going Home",
                        "SORROW AND REGRET ENDING")


def qshortcut():
    choice = simpledialog.askinteger("Going Home",
                                     "Approaching the corner you start to get uneasy."
                                     "\n You get this very strange vibe from the alley as"
                                     "\n you turn onto to it. However all you see is an old"
                                     "\n man that looks poor and homeless."
                                     "\n (1) Approach the hobo or"
                                     "\n (2) ignore him and head home.")
    if (choice == 1):
        qhobo()
        
    elif (choice == 2):
        qhome_end()
        
    else:
        qshortcut()

def qhobo():
    choice = simpledialog.askinteger("Hobo Interactions",
                                     " You approach the hobo with caution, it's almost like"
                                     "\n you feared the man against the wall. You ask if he is"
                                     "\n ok and he replies in a raspy voice,"
                                     "\n 'Would you kindly spare some change for me?'"
                                     "\n (1) Give the hobo money or (2) kick dirt in his face?")
    if (choice == 1):
        qhobo_end()
        
    elif (choice == 2):
        qhobo_kill()
        
    else:
        qhobo()


def qhobo_end():
    messagebox.showinfo("Hobo Interactions",
                        "You reach into your wallet and realize you have no change,"
                        "\n just a few dollar bills. You offer him what you have and"
                        "\n he accepts it graciously. You begin to walk away but before"
                        "\n you get to the end of the alley, the hobo stops you."
                        "\n He calls to you and tells you to come with him.")

    messagebox.showinfo("Hobo Interactions",
                        "He went to an old payphone down the street and called someone."
                        "\n He said he called his brother to come and treat you because"
                        "\n of your generosity. In a matter of minutes a car pulls up to"
                        "\n the curb and the driver tells you to git in. He was well dressed"
                        "\n in a nice new suit. You get well situated with him and go out"
                        "\n for some drinks. The rest of the night is a blur but it was fun.")

    messagebox.showinfo("Hobo Interactions",
                        "GOOD SAMARITAN ENDING")

def qhobo_kill():
    messagebox.showinfo("Hobo Interactions",
                        "...")

    messagebox.showinfo("Hobo Interactions",
                        "You stand shocked, there is blood starting to trickle"
                        "\n down his shoulder. There must have been a shard of metal"
                        "\n in the dirt. You start to panic as you try to check if he"
                        "\n is fine. Worried, you take him to the hospital and then"
                        "\n something hits you. The kick of dirt must have been pretty"
                        "\n powerful if it was to impale him with a shard of metal"
                        "\n To test this power you found, you try out for a soccer club."
                        "\n Amazingly enough you're the best forward there. They recruit"
                        "\n you on spot. You make enough of an impact to play in"
                        "\n the upcoming world cup event and win it for your team.")

    messagebox.showinfo("Hobo Interactions",
                        "UNFOUND TALENT ENDING")


def qhome_end():
    messagebox.showinfo("Going Home",
                        " You walk past the hobo as if he wasn't even there."
                        "\n You just want to get home so there is no need to"
                        "\n talk to this stranger. When you arrived at your"
                        "\n house it felt extremely quiet. So that night you"
                        "\n decided to get a dog and adopted it on the spot."
                        "\n You become best friends and completely forget about"
                        "\n your life outside the house.")

    messagebox.showinfo("Going Home",
                        "IGNORANCE IS BLISS ENDING")


 ################ GiveMeYourMilk Functions #####################
        #204863 204863 204863 204863 204863 204863
def ivengence():
    choice = simpledialog.askinteger("...with vengence",
                                     "You take this murder personally. It was"
                                     " your first day and someone went and killed"
                                     " your boss. You will catch the peson who"
                                     " did this, no matter what the cost!"
                                     "\n You sneak past the police tape and"
                                     " start snooping for evidence. You notice"
                                     " something under some papers on his desk."
                                     " A note! \n It reads: \n 'Meet me \n on the"
                                     " roof \n \n   -R'"
                                     "\n (1) ignore the letter (2) go to the roof")
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
                        "you're not a world class ninja-spy-assassin."
                        " As you walk away you realise that was it,"
                        " you're last chance to live out your dream"
                        " of being a classic detective like the ones"
                        " your grandfather would tell you about and show you"
                        " in classic films and now it's over now. You walk home"
                        " with your head hung low, knowing that your"
                        " dream is lost.")
def vfollow():
    choice = simpledialog.askinteger("Rooftop",
                                     "You catch the killer on rooftop"
                                     "\n Kill him(1) or Question him(2)")
    if (choice == 1):
        fkill()

    elif (choice == 2):
        fquestion()

    else:
        vfollow()

def fkill():
    choice = simpledialog.askinteger("Killer",
                                     "What will you do with his body?"
                                     "\n Hide it(1) or Display it(2)")
    if (choice == 1):
        khide()

    elif (choice == 2):
        kdisplay()

    else:
        fkill()

def khide():
    messagebox.showinfo("END",
                        "You hide the body where it"
                        " will never be found. Your guilt won't let you"
                        " show your face work anymore now")

def kdisplay():
    messagebox.showinfo("END",
                        "With the body so visble it isn't"
                        " hard for the police to discover"
                        " enough evidence to put you away"
                        " for a long time")

def fquestion():
    choice = simpledialog.askinteger("Rooftop",
                                     "You discover he was just a hitman for"
                                     " Silvone. Silvone was the biggest mob"
                                     " in the city. He was the man Robinson"
                                     " was trying to bring down when he was"
                                     " shot. Silvone had been untouchable, "
                                     "but Robinson had finally got something"
                                     " on him. You cuff the hitman to the rooftop"
                                     " and leave his note on the office door."
                                     " You finally had something on Silvone,"
                                     " but you're not sure it's enough. You"
                                     " need evidence from the source. "
                                     "\n (1) check the local crime bar (2) check the mafia hideout")
    if (choice == 1):
        qbar()

    elif (choice == 2):
        qmafia()

    else:
        fquestion()

def qmafia():
    messagebox.showinfo("END",
                        "You're just outside the old abandoned warehouse that"
                        " the mafia has been using as their head quarters."
                        " You bust through the doors and yell that you're"
                        " here to bring bring in Silvone. As you say that"
                        " you realise that they killed your boss in his office"
                        " just for having the evidence. You hear the doors behind"
                        " you slam shut and you realise you've reached the end of"
                        " the line.")

def qbar():
    choice = simpledialog.askinteger("Bar",
                                     "You decide against confronting the people who"
                                     " kill in cold blood. You head to The Stacked Deck."
                                     " This was the place where all the filth of"
                                     " Chicago spent their dirty money. You decide against"
                                     " yelling out your motives for being here and head to"
                                     " the bar to scope the place out. You sit down and"
                                     " the bartender sets a drink down infront of you."
                                     "\n (1) drink it (2) avoid it")
    if (choice == 1):
        bdink()

    elif (choice == 2):
        bsmart()
    
    else:
        qbar()

def bdrink():
    messagebox.showinfo("END",
                        "You take a sip of your drink. Fizzy"
                        " you think to yourself. You see something"
                        " interesting happening in the back of the"
                        " bar. You stand up to check it. The room"
                        " starts spinning. You collapse. As you die"
                        " you realise that taking drinks from stangers might"
                        " no be the best idea.")

def bsmart():
    choice = simpledialog.askinterger("The Ace",
                                      "You look down at the drink, but decide against it."
                                      " You turn back around to scope out the bar. There is"
                                      " massive bar fight going on. You wonder if this kind"
                                      " of thing happens often. Behind the choas of flying"
                                      " chairs you see a girl who stands. A brunette in slinky"
                                      " black dress sipping on something fruity. You rationalise"
                                      " that talking to her would be very useful to your investagation."
                                      " You walk back to her avoiding flying bodies. You ask what"
                                      " she's doing in a place like this. She tells you something"
                                      " about how her boyfriend asked her to wiat for him here."
                                      " she doesn't seem to like him much. You wonder why she is"
                                      " still with him. You're about to tell her something about"
                                      " how you'd treat her better when someone grabs you by your"
                                      " shoulder and punches you. It wasn't a hard punch, but probably"
                                      " the strongest he could throw. This guy didn't seem like"
                                      " someone who does this sort of 'work' often. He still manages to"
                                      " overpower you. You need an advantage..."
                                      "\n (1) grab the steak knife (2) grab the glass")
    if (choice == 1):
        sknife()

    elif (choice == 2):
        sglass()
    
    else:
        bsmart()

################ Winikka's Functions #####################
# Note this is an alert of the Winikka Broadcast System  #
# This is only a test                                    #
# Winikka is not really going to code a function here    #
# If he were to code, he would put it here.              #
# This is just to show you how to collaborate using Git  #
##########################################################

################ Main #####################
intro()

root.destroy()
