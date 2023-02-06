#Python 3.6.5

hp=10 #hp = hitpoint
exp=0 #exp = experience variable
level=1 
import random
name=input("Type in your Adventurers name")
print("welcome",name,"to the...")



print("""
      floor of the cave is now submerged
      beneath inky black water. Your shoes give up the battle to keep the water out
      and you walk with a steady squelch
      """)
print("You have " + str(hp) + " hitpoints")
print("You have " + str(exp) + " experience points")


tutorial = input("Would you like a simple tutorial? press y or n, then press enter")
                 
if tutorial == ("y"):

      print("""
--------------------------------------------------------------------------------------------------------------------
            Read the story information a choice will be given to you about what you would like to do 

            Decide what you would like to do, press the indicated letter and press enter 

            Always use lowercase letters in any answers!
-------------------------------------------------------------------------------------------------------------------
            """)

print("""
      Inky water subsides to reveal a mossy cobblestone
      leading somewhere...
      You spot a fierce mole at the end of the tuunel
      """)


event1 = input("Press s to sneak by. Press t to throw stone at it")
if event1 == ("s"):
    
    print("Carefully you edge past")
    exp=exp+2
else:
   print("You throw a stone at the mole")
   print("It attacks you")
   print("After a struggle it runs off")
   exp=exp+1
   hp=hp-1
print("You have",exp,"experience points")
print("You have",hp,"hitpoints left")

print("""
      You see a door at the end of the tunnel
      likely opening to an ancient jurjairian temple
      what might be inside?
      """)

event2 = input("Press l to lockpick. Press k to knock")
if event2 ==("l"):
    print("You pick the lock successfully")
    exp=exp+4
else:
    print("You knock on the door")
    print("one hour later")
    print("An elderly man opens the door and lets you in")
    exp=exp+3
    print("Your patience is awarded")
    hp=hp+3
# Re add old man
print("You have",exp,"experience points")
print("You have",hp,"hitpoints left")

print("You enter the Jurjairian temple")

print("""
      You are faced with two dark, dank corridors, one forward, the other right
      you cannot see down either
      """)

event3 = input("Press w to go forward. Press d to go to the right.")
if event3 == ("w"):
    print("you come across a tatty old Mace")
    print("you take it for the road But you drop it on your foot")
    exp=exp+2
    hp=hp-1
    
else:
    print("You find a Silver sword with jewels in the hilt")
    print("You take it for the road")
    exp=exp+3
    
print("You have",exp,"experience points")
print("You have",hp,"hit points left")      

print("""
      A loud crash echos from behind... 
      rumbling throughout the halls
      """)

if event3 == ("w"):
    print("The only way to go from from here is right")

    print("You reach the end of the corridor and turn left")

else:
    print("The only way to go from here is left")

    print("You walk down an extended corridor")

print("""
      You approach the end of the corridor 
      there are two buttons, one red, one yellow 
      which one will you press?
      """)

event4 = input("Do you press the red or yellow button. press r or press y")

if event4 == ("r"):
    print("A large crash echos from the entrance of the cave")
    print("Sounds like the entrance just collapsed")
    exp=exp+2

else:
    print("A large block slams behind you")
    print("Some rumble hits you in the arm!")
    exp=exp+4
    hp=hp-2

print("You have",exp,"experience points")
print("You have",hp,"hit points left") 

print("""
      After the rumble subsides a thin piller of anicent stone opens
      you step through...
      to discover a dark large seemingly empty room...
      """)

event5 = input("Would you iike to attempt to light up the area? y or n")

if event5 == ("y"):
      print("""
      You scramble in the dark, searching for a torch 
      you find one and set it alight 
      you turn away for a second 
      the fire go's out
      you reach the end of the room 
      where you see an extended corridor with a dim light at the end 
      """)
      exp=exp+2
else:
      print("""
      You stumble in the dark looking for any loot or an exit 
      feeling with you hands
      you see an extended corridor with a dim light at the end
      """)
      exp=exp+2

print("You have",exp,"experience points")
print("You have",hp,"hit points left")

print("""
      As you make your way down this corridor 
      loud rumbling echos as...
      thick stone walls begin to close in sections
      """)

event6 = input("Would you like to run for the light, let it happen or panic? Press r,l,p")

if event6 == ("r"):
      print("""
            you dash for the dim light with speed 
            stone walls continue to slowly shut 
            you just reach the light as the final wall crashes and locks into place
            """)
      exp=exp+3
    
if event6 == ("l"):
      print("""
            You decide to just let it happen, What can go wrong, Right?
            thick stone walls close in around you 
            you wait for nearly an hour...
            A kind elderly man lets you out 
            """)
      exp=exp+4
      hp=hp+3

if event6 == ("p"):
      print("""
            You freeze in a vicious panic
            you fucking nobhead!
            something eventually lets you out!
            """)
      exp=exp+1

print("You have",exp,"experience points")
print("You have",hp,"hit points left")

print("""
      Your tired self enters a small room with a pedestal in the centre
      a bright glowing orb sits on the pedestal
      it asks to be touched 
      """)

event7 = input("Would you like to touch the orb, examine it or ignore it, press t,e,i")

if event7 == ("t"):
      print("""
            You go to touch the orb
            your hands grasp the orb tightly 
            A blinding flash controls your whole body hurting you deeply 
            """)
      hp=hp-2
      exp=exp+1
      event71 = input("Now, would you like to examine the orb, or ignore it? Press e or i")

      if event71 == ("e"):
            print("""
                  You take a close look ar the orb while avoid touching it's infinate surface 
                  It appears to be made from an alloy of silver and pure ocean pearls 
                  you also notice what appears to be a red cross on one surface
                  you cannot find anything to do with the orb

                  You press on...
                  at the end of the room appears a to be an ornate looking crossbow
                  likely of jurjairian design
                  """)

      if event71 == ("i"):
             print("""
                   You chose to ignore the orb and press on
                   at the end of the room appears a to be an ornate looking crossbow
                   likely of jurjairian design

                   You also notice that the orb has a red cross on its surface
                   """)

 
if event7 == ("e"):
      print("""
            You take a close look ar the orb  
            It appears to be made from an alloy of silver and pure ocean pearls 
            you also notice what appears to be a red cross on one surface
            you cannot find anything to do with the orb

            You press on...
            at the end of the room appears a to be an ornate looking crossbow
            likely of jurjairian design
            """)

if event7 == ("i"):
      print("""
            You chose to ignore the orb and press on
            at the end of the room appears a to be an ornate looking crossbow
            likely of jurjairian design

            You also notice that the orb has a red cross on its surface
            """)

eventopenthedoor2 = input("Would you like the shot the cross y or n ")

if eventopenthedoor2 == ("y"):
             print("""
                   You take aim to fire the crossbow at the red cross mark
                   the bolt releases at lightning speed
                   the bolt finds its mark
                   The crossbow dissolves in you hand as the Orb shatters and a secret door opens
                   you walk through...
                   """)
             hp=hp+1
             exp=exp+1

if eventopenthedoor2 == ("n"):
             print("""
                   you decide to avoid shooting anything utill you have properly searched the room
                   you search for an hour
                   nothing comes up the crossbow seems to be the only way

                   You take aim to fire the crossbow at the red cross mark
                   the bolt releases at lightning speed
                   the bolt finds its mark
                   The crossbow dissolves in you hand as the Orb shatters and a secret door opens
                   you walk through...
                   """)
             hp=hp+1
             exp=exp+1



print("""
      You enter a neverending room of a perfect white stone. The door behind you crashes closed The room has
      been left in perfect condition, there are no signs of life however everything is in a godly condition,
      shineing light pierces your skin, it almost fills your soul with a pure light. The walls are caped in
      in perfect pattern of mixed white bricks and plaid hang up cloths. The two walls rise up high above you
      and meet to form a pyrimid shape; Two king-sized tables extend to the ends of the hall, at the end of
      the sites a beauiful throne, head sized Jewels glitter the massive chair.
      
      Some unnatural force wills you to sit apon the great throne. The ancient power if the jurjairian people
      flows through you like the blood that inhabites your feeble bones.

      As you place yourself on the ancient power you feel the earth itself shakes, as the ancient temple
      emerges from below ground to stand again as the seat of power for a great empire.
      """)

print("""
--------------------------------------------------------------------------------------------------------------------
          End of Chapter One 
--------------------------------------------------------------------------------------------------------------------
      """)       
