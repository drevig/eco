# Imports 
import random
import time
import os
import time
clear = lambda: os.system('cls')


# Location Detials
Location = {}
  # Location Names
First_Location_Name = ["St.", "Mackles", "Union", "Ley", "Long","Salty", "Moist","The ", "Old ","Nort","Weaver", "Stratford", "Witney","CWC","Stratum","Orkecsh", "Grave", "Canary", "Victoria", "Bleeb", "Sunny", "East", "North"]
Second_Location_Name = [" towers", " springs", " mire", " caverns"," grove"," junction", " wood", " castle"," dam"," land"," up-on-hill", " caverns"," Park", " Close", " Works" , "dene", " End", "liegh"]
  # Location Types
Location_Types = ["Hot", "Cold", "Volatile", "Temperate"]

# Corp Detials
All_Corps = {}
  # Corp Names
First_Corp_Name = ["Nortons", "Weavers", "Indie Prince","B2G", "Wil-Worms", "OXFLIB", "Healy", "COTW", "Steveo", "Classic", "The ", "Sheel", "Gummo", "Scum"]
Second_Corp_Name = [" Corp", " Industries", " Indies"," Limited", " Public", ".Co", " Inc", " Studios", " Since 1996", " Incorporated"," Gang"," Crew"]
  # Corp Number
Corporation_Number = random.randint(5,10)
  
  # Leader Names
First_Leader_Name = ["Mrs.","Sir.","Dr.","Sir","Dan ","Steve ","Wayne ","Brock ","Gumo ", "Simon ","Jeane "]
Second_Leader_Name = ["Dimblesbury", "Cackall","Ozbourne", "Jhonston","Coyne", "Crosby", "T", "Tekashi", "Chan", "Addie","Six","Mangum", "McBryde"]
  # Leader Types
Leader_Types = ["Greedy","Safe"]

# Materials
All_Materials = {}
  # Material Names
First_Material_Name = ["Min", "Oyx","Met", "Jel", "Med", "Shish", "Spis", "Ammi", "Cay","Ami","Lem","Aro","Nem","Neg", "Meem", "Shi", "Ple", "Phe", "Sha","Ti","Sh", "Leb"]
Second_Material_Name = ["eral","ite","ish","mem","nesia","y","ie","in","al","sh","cy","al","ton","en","ish", "bel", "oy", "ams", "per", "el", "lk","eh"]
  # Material Number
Material_Number = random.randint(5,10)
# Time
Hour = 0
Day = 0
Week = 0
Month = 0
Year = 0

# Stats
Crisis_Aversions = 0

# Trading Assets
Potential_Clients = []
Potential_Materials = []

# Graphical Assets 
Leaderboard = {}
##########################################################################

# Graphics
def Night_Sequence():
    Night_Falls = ["Night Falls."]
    Night_Falls_Print = []
    Tick = 0
    for letters in range(0,12):
        Letter = Night_Falls[0][Tick]
        Night_Falls_Print.append(Letter)
        print (Night_Falls_Print)
        time.sleep(0.5)
        Tick = Tick + 1
        clear()
    else:
            print(Night_Falls_Print)
            time.sleep(5)
            clear()
def Top_Corps():
    Tick = 0
    for Corps in range(len(All_Corps)):
        Leaderboard = {All_Corps[Tick] : All_Corps[Tick]["Name"]["Funds"]["Wallet"]}

# Corporation Gen Functions
def Name_Generator():
    Name_Number_One = random.randint(0,(len(First_Corp_Name)-1))
    Name_Number_Two = random.randint(0,(len(Second_Location_Name)-1))
    Name_To_Be_Returned = First_Corp_Name[Name_Number_One] + Second_Location_Name[Name_Number_Two]
    First_Corp_Name.remove(First_Corp_Name[Name_Number_One])
    return Name_Number_One + Name_Number_Two
def Leader_Name_Generator():
    Name_Number_One = random.randint(0,(len(First_Leader_Name)-1))
    Name_Number_Two = random.randint(0,(len(Second_Leader_Name)-1))
    Name_To_Be_Returned = First_Leader_Name[Name_Number_One] + Second_Leader_Name[Name_Number_Two]
    First_Leader_Name.remove(First_Leader_Name[Name_Number_One])
    Second_Leader_Name.remove(Second_Leader_Name[Name_Number_Two])
    return Name_Number_One + Name_Number_Two
def Leader_Type_Generator():
    Type = random.randint(1, ((len(Leader_Types)-1)))
    return Leader_Types[Type]
def Location_Name_Generator():
    Name_Number_One = random.randint(0,(len(First_Location_Name)-1))
    Name_Number_Two = random.randint(0,(len(Second_Location_Name)-1))
    Name_To_Be_Returned = First_Location_Name[Name_Number_One] + Second_Location_Name[Name_Number_Two]
    First_Location_Name.remove(First_Location_Name[Name_Number_One])
    Second_Location_Name.remove(Second_Location_Name[Name_Number_Two])
    return Name_Number_One + Name_Number_Two
def Location_Type_Generator():
    Type_Chosen = random.randint(1, (len(Location_Types)-1))
    return Location_Types[Type_Chosen]
def Startup_Funds():
    Funds = random.randint(50,150)

    return Funds

# World Bank Functions 
def World_Bank_Name_Gen():
    Name_Number_One = random.randint(0,(len(First_Leader_Name)-1))
    Name_Number_Two = random.randint(0,(len(Second_Leader_Name)-1))
    Name_To_Be_Returned = First_Leader_Name[Name_Number_One] + Second_Leader_Name[Name_Number_Two]
    First_Leader_Name.remove(First_Leader_Name[Name_Number_One])
    Second_Leader_Name.remove(Second_Leader_Name[Name_Number_Two])
    return Name_Number_One + Name_Number_Two
# Material Gen Functions 
def Material_Name_Gen():
    Name_Number_One = random.randint(0,(len(First_Material_Name)-1))
    Name_Number_Two = random.randint(0,(len(Second_Material_Name)-1))
    Name_To_Be_Returned = First_Material_Name[Name_Number_One] + Second_Material_Name[Name_Number_Two]
    First_Material_Name.remove(First_Material_Name[Name_Number_One])
    Second_Material_Name.remove(Second_Material_Name[Name_Number_Two])
    return Name_Number_One + Name_Number_Two
def Rarity_Generator():

    return random.randint(0,100)
def Cost_Generator():
    Tick = -1
    for Mats in range(0,len(All_Materials)):
        Tick = Tick + 1
        if All_Materials[Tick]["Rarity"] > 90:
            All_Materials[Tick]["Cost"] = 100
        elif All_Materials[Tick]["Rarity"] > 80:
            All_Materials[Tick]["Cost"] = 90
        elif All_Materials[Tick]["Rarity"] > 80:
            All_Materials[Tick]["Cost"] = 70
        elif All_Materials[Tick]["Rarity"] > 70:
            All_Materials[Tick]["Cost"] = 60
        elif All_Materials[Tick]["Rarity"] > 60:
            All_Materials[Tick]["Cost"] = 50
        elif All_Materials[Tick]["Rarity"] > 50:
            All_Materials[Tick]["Cost"] = 50
        elif All_Materials[Tick]["Rarity"] > 40:
            All_Materials[Tick]["Cost"] = 30
        elif All_Materials[Tick]["Rarity"] > 30:
            All_Materials[Tick]["Cost"] = 20
        elif All_Materials[Tick]["Rarity"] > 20:
            All_Materials[Tick]["Cost"] = 10
        elif All_Materials[Tick]["Rarity"] < 9:
            All_Materials[Tick]["Cost"] = 5
def Location_Sorter():
    Loc_Number = random.raident(0,500)
    return Loc_Number
        

# World Gen
def Spawn_Materials():
    Tick = 0
    for Mats in range(1, (len(All_Materials))):
        Spawn_Chance = random.randint(0,100)
        if All_Materials[Tick]["Rarity"] < Spawn_Chance:
            All_Materials[Tick]["Quantity"] = All_Materials[Tick]["Quantity"] + 1
            Tick = Tick + 1
        else:
            All_Materials[Tick]["Quantity"]
            Tick = Tick + 1
def Coproration_Generator():
    Tick = 0
    for Coprs in range(Corporation_Number):
        All_Corps[Tick] = {"Name"    : Name_Generator(), 
                          "Location" : {"Location Name" : Location_Name_Generator(), "Location Type" : Location_Type_Generator(), "Location Code": Location_Sorter()},
                          "Leader"   : {"Leader Name" : Leader_Name_Generator(), "Leader Type" : Leader_Type_Generator()},
                          "Funds"    : {"Wallet": Startup_Funds()},
                          "Materials": {}
                          
                          }
        Tick = Tick + 1                         
def Material_Generator():
    Tick = 0 
    for mats in range (Material_Number):
        All_Materials[Tick] = {"Name" : Material_Name_Gen(), "Rarity" : Rarity_Generator(), "Quantity" : 0, "Cost" : 0, "Location Code" : Location_Sorter()}
        Tick = Tick + 1
def World_Bank_Gen():
    World_Bank = {"Name": World_Bank_Name_Gen(), "Funds": 0}
    World_Bank["Funds"] + 1000

# Trading Mechanics 
def Client_Check():
    Tick = 0
    for Corps in range(0,len(All_Corps)-1):
        if All_Corps[Tick]["Funds"]["Wallet"] >= 1:
            Potential_Clients.append(All_Corps[Tick])
            Tick = Tick + 1
            Potential_Clients.sort
        else:
            Tick = Tick + 1
def Material_Check():
    Tick = 0 
    for mats in range(0,len(All_Materials)):
        if All_Materials[Tick]["Quantity"] > 1:
            Potential_Materials.append(All_Materials[Tick])
def Distance_Calculator(Potential_Mat,Potential_Client):
    Distance = Potential_Mat - Potential_Client
    if Distance < 0:
        Distance = -Distance
        return Distance
    else:
       return Distance
def Transport_Cost():
    Corp_Tick = 0
    Mat_Tick = 0
    Cost = 0
    for Mats in range(0,len(Potential_Materials)):
        Distance = Distance_Calculator(Potential_Materials[Mat_Tick],Potential_Clients[Corp_Tick])
        if Distance > 400:
            Cost = 50
def Trade():
    Client_Tick = 0
    Material_Tick = 0
    for mats in Potential_Materials:
        Distance = Distance_Calculator(Potential_Clients[Client_Tick]["Name"]["Location"]["Location_Code"],Potential_Materials[Material_Tick]["Location Code"])
        if Distance >= 50:
            Purchase(Potential_Clients[Client_Tick],Potential_Materials[Material_Tick])
            Potential_Materials[Material_Tick]["Quantity"] - 1
            Potential_Clients[Client_Tick]["Name"]["Funds"]["Wallet"] - Potential_Materials[Material_Tick]["Cost"]
            if Potential_Materials[Material_Tick]["Quantity"] =< 0:
                Potential_Materials.remove()





# Transport Mechanics
def Trade_Display():

    print("please finish")

# Start Up Seq
Startup = 1
print("Welcome!")
Coproration_Generator()
Material_Generator()
World_Bank_Gen()
Cost_Generator()
time.sleep(2)
clear()
Startup = 0

# World Start
while Startup == 0:
    if Hour == 0:


