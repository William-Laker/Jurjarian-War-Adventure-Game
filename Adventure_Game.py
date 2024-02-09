import random
import time
import sys

global hp 
hp=10 
global exp
exp=0 
global level
level=1
global health_potion
health_potion=5
global treasure
treasure=0
global modifier
modifier = 2
global armour
armour = 10

weapon = "null"
inventory = ["stick", "dagger"]

class charactorStats: 
   def __init__(self, health, armourClass, modifier, level, exp):
      self.phealth = health
      self.parmourClass = armourClass
      self.pmodifier = modifier
      self.plevel = level
      self.pexp = exp

player = charactorStats(10, 10, 2, 0, 0)

class Enemies_Stats:

    def __init__(self, health, modifier, armourClass):
        self.health = health
        self.modifier = modifier
        self.armourClass = armourClass

Enemy_Rat = Enemies_Stats(1, 1, 12)
Enemy_Spider = Enemies_Stats(3, 2, 10)
Enemy_Skele = Enemies_Stats(4, 1, 8)


class Weapons_Stats:

    def __init__(self, MinDamage, MaxDamage):
        self.min = MinDamage
        self.max = MaxDamage

Weapon_Longsword = Weapons_Stats(1, 4)
Weapon_Shortsword = Weapons_Stats(1, 3)
Weapon_Battleaxe = Weapons_Stats(1, 5)
Weapon_Greatsword = Weapons_Stats(2, 6)
Weapon_Halberd = Weapons_Stats(2, 4)

class Armour_Stats:

    def __init__(self, AdditionalArmour, MaxDexIncrease):
        self.AdditionalArmour = AdditionalArmour
        self.MaxDexIncrease = MaxDexIncrease

Armour_Leather = Armour_Stats(2, 999)
Armour_Mail = Armour_Stats(4, 999)
Armour_Breastplate = Armour_Stats(5, 2)
Armour_HalfPlate = Armour_Stats(6, 2)
Armour_FullPlate = Armour_Stats(8, 0)


def Death_function(): #Function to end the game if the player is dead
   print("...You have Died...")
   time.sleep(5)
   sys.exit()

def Levelup_function(player):
   global level
   global exp
   global modifier
   print("You have ",exp,"Experience points")
   print("...You have leveled up... \n")
   time.sleep(1)
   level=level+1
   modifier=modifier+1
   print("You are now level",level,"\n")
   exp=exp-5
   time.sleep(1)

def Healthpotion_function():
   global hp
   global health_potion
   hpup=random.randint(1,4)
   print("You are healing "+str(hpup)+" hitpoints")
   hp=hp+hpup
   print("Your health is now " +str(hp))
   health_potion=health_potion-1
   print("You now have " +str(health_potion)+" Health potions left")
   
   
def Inventory_function(weapon):
    print("Do you wish to pick up the weapon?")
    print("You already have....")
    print(inventory)
    choice=str(input("choose y to pick up or n to leave alone"))
    #This allows you to leave stuff alone
    if choice == "y":
        print("Got it!")
        inventory.append(weapon)
        print(inventory)
    else:
        print("Okay, leave it!")
    return

def Combat_Function(player, enemy): 
    
    while(enemy.health > 0 and player.phealth > 0):             
        hitchance = random.randint(1,20)
        Attack_Roll = hitchance + player.pmodifier
        print(Attack_Roll)
         
        if Attack_Roll >= enemy.armourClass:
          enemy.health = enemy.health-1
          print("You have",player.phealth,"Hitpoints left \n")
          time.sleep(1)
        
        else:
          print ("It attacks you")
          attackchance = random.randint(1,20)
          Eattack_Roll = attackchance + enemy.modifier
          if Eattack_Roll >= player.parmourClass:
            player.phealth=player.phealth-1                         
            print("You have",player.phealth,"Hitpoints left \n")
            time.sleep(1)
          else:
             print("The creature missed")



name=input ("Type in your adventurers name... ") #enter name

print(Enemy_Rat)

print ("Welcome",name,"to the Jurjarian Temple")
time.sleep(1)

print("""
The floor of the cave is now mostly submerged beneath inky black water
Your shoes give up the battle to keep the water out and you walk with a
steady squelch
""") #Info
time.sleep(1)

print ("You spot a fierce rat in the centre of the tunnel")

time.sleep(1)

event1 = input("Press s to sneak by. Press t to throw a stone at it. ")
if event1 == ("s"):
   print ("You carefully edge past \n")
   exp=exp+2
   time.sleep(1)
if event1 == ("t"):
    print ("You throw a stone at the rat\n")
    Combat_Function(player, Enemy_Rat)
    time.sleep(1)
    print("The rat is dead \n")
    exp=exp+1

if exp >= 5:
   Levelup_function()

print ("You have",hp,"hitpoints left") #Prints out hp and exp
print ("You have",exp,"experience points \n")
time.sleep(1)

#Random encounter 1
encounter1=random.randint(1,3)

if encounter1 == 1:
   print("A stone broke off the ceiling and hit you in the head \n")
   hp=hp-1
   time.sleep(1)
   
if encounter1 == 2:
   print("An angry looking spider crawls out of a hole in the wall \n")
                                    
   time.sleep(1)
   Combat_Function(player, Enemy_Spider)
   exp=exp+2
   time.sleep(1)
   
if encounter1 == 3:
   print("You find a small shiny looking emerald on the ground")
   time.sleep(1)
   treasure=treasure+1
   print("...You have added an item to you treasure pile!... \n")
   exp=exp+1
   time.sleep(1)

if encounter1 == 2:
   print("The spider is dead")
   time.sleep(1)

if exp >= 5:
   Levelup_function()
   
#End of random encounter 1

heal=input("Would you like to heal some health? say yes or no")
time.sleep(1)
if heal == "yes" or "Yes":
    Healthpotion_function()
if heal == "no" or "No":
    print("Ok then \n")
   

time.sleep(1)

print ("You have",hp,"hitpoints left") #Prints out hp and exp
print ("You have",exp,"experience points\n")
time.sleep(1)

print("""
The cavern opens up to a room of sorts. At the other end you see a large
door, it looks old and worn.

The floor looks a little weak, the floor could collapse in on itself!
""")
time.sleep(1)
event2=input("To edge you way along the wall press c to run across press r \n ")

if event2 == "c":
   print("You carefully edge along the wall. \n")
   time.sleep(1)
   exp=exp+2
   print("You reach the end of the cave easily \n")
   time.sleep(1)

if event2 == "r":
   print("You bolt across the room however the floor collapses beneath you ")
   print("You fall down an endless cavern\n")
   time.sleep(1)
   Death_function()
   

if exp >= 5:
   Levelup_function()

print ("You have",hp,"hitpoints left") #Prints out hp and exp
print ("You have",exp,"experience points")
time.sleep(1)

print("""
You reach the end of the room to the decrepit door, you try to open the door 
but the door falls over flat instantly, the hinges had obviously rooted away 
ages ago 
""")
time.sleep(1)

print("...You enter the structure... \n")
time.sleep(1)

print("You can see a reanimated skeleton in the centre of the hallway \n")

time.sleep(1)

event3=input("Would you like to try to sneak past the skeleton press s or to attack it head on press a")

if event3 == "s":
    sneakchance=random.randint(1,10)
    print("You rolled a ",sneakchance,)
    time.sleep(1)
    if sneakchance <= 5:
        print("You failed to sneak by the skeleton")
        time.sleep(1)
        Combat_Function(player, Enemy_Skele)
        exp=exp+1
    else:
        print("You successfully creeped past the skeleton")
        time.sleep(1)
        exp=exp+2

if event3 == "a":
    print("You charge at the Skeleton")
    time.sleep(1)
    Combat_Function(player, Enemy_Spider)
    exp=exp+2

print("You made it past the skeleton")

print("You find a sword on the ground")
weapon="sword"
Inventory_function(weapon)
time.sleep(1)

print ("You have",hp,"hitpoints left") #Prints out hp and exp
print ("You have",exp,"experience points")
time.sleep(1)
