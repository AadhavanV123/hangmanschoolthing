import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import time
from functools import partial
import random
import asyncio
import os
from subprocess import run

#WORDS WITH SPACES NEED TO WORK

themes = {
    "Food": [
        "Apple", "Banana", "Orange", "Cake", "Cookie", "Pizza", "Burger", "Pasta", 
        "Ice Cream", "Spaghetti", "Donut", "Muffin", "Chocolate", "Lollipop", "Waffle", 
        "Taco", "Sushi", "Steak", "Salad", "Pineapple", "Cheese", "Cereal", "Pudding", 
        "Popcorn", "Cupcake", "Pie", "Lemon", "Watermelon", "Grapes", "Bacon"
    ],
    "Toys": [
        "Action Figure", "Doll", "Teddy Bear", "LEGO", "Puzzle", "Ball", "Rubik's Cube", 
        "Yo-Yo", "Kite", "Drone", "Toy Train", "Building Blocks", "Stuffed Animal", 
        "Bicycle", "Swing", "Marbles", "Jigsaw", "Plushie", "Rubber Duck", "Top", 
        "Hula Hoop", "Rubber Ball", "Spinning Top", "Fidget Spinner", "Toy Car", "Trampoline"
    ],
    "Shapes": [
        "Circle", "Square", "Triangle", "Rectangle", "Pentagon", "Hexagon", "Octagon", 
        "Star", "Heart", "Diamond", "Spiral", "Crescent", "Ellipse", "Cube", "Cone", 
        "Cylinder", "Pyramid", "Tetrahedron", "Prism", "Sphere", "Rhombus", "Arrow", "Wave"
    ],
    "Weather": [
        "Sun", "Rain", "Snow", "Cloud", "Wind", "Thunderstorm", "Lightning", "Fog", 
        "Hail", "Tornado", "Hurricane", "Cyclone", "Blizzard", "Drought", "Tempest", 
        "Vortex", "Eclipse", "Heatwave", "Monsoon", "Gale", "Sleet", "Drizzle", "Mist"
    ],
    "Technology": [
        "Computer", "Smartphone", "Tablet", "Laptop", "Camera", "Drone", "GPS", "Smartwatch", 
        "Robot", "Internet", "Wi-Fi", "Bluetooth", "Printer", "Scanner", "Microwave", 
        "Smart TV", "Virtual Reality", "Augmented Reality", "Blockchain", "Software", 
        "App", "Server", "Cloud", "Hologram", "Camera", "Electric Car"
    ],
    "Nature": [
        "Tree", "Mountain", "River", "Ocean", "Forest", "Desert", "Cactus", "Flower", 
        "Sunflower", "Rainforest", "Waterfall", "Lake", "Rock", "Cave", "Coral Reef", 
        "Volcano", "Island", "Glacier", "Tundra", "Swamp", "Meadow", "Pond", "Grassland", 
        "Cliff", "Wildlife", "Earth", "Soil"
    ],
    "Places": [
        "House", "Mansion", "Castle", "Beach", "Park", "Museum", "Zoo", "Library", 
        "Hospital", "City", "Town", "Village", "Island", "Airport", "Factory", "Farm", 
        "Cave", "Mountain", "School", "Restaurant", "Church", "Bank", "Theater", "Hotel", 
        "Garden", "Mall"
    ],
    "Objects": [
        "Chair", "Table", "Lamp", "Phone", "Cup", "Shoes", "Bag", "Clock", "Key", 
        "Door", "Plate", "Fork", "Spoon", "Brush", "Scissors", "Shirt", "Guitar", "Trolley", 
        "Jacket", "Scarf", "Teapot", "Biscuit", "Magnet", "Chalk", "Tractor", "Mirror", 
        "Helmet", "Rug", "Cushion", "Towel", "Toothbrush", "Wallet", "Pillow", "Ladder", 
        "Faucet", "Kettle"
    ],
    "Animals": [
        "Dog", "Cat", "Fish", "Bird", "Lion", "Tiger", "Elephant", "Whale", "Dolphin", 
        "Giraffe", "Crocodile", "Bear", "Penguin", "Rabbit", "Kangaroo", "Panda", "Koala", 
        "Zebra", "Horse", "Parrot", "Snake", "Turtle", "Monkey", "Gorilla", "Shark", 
        "Octopus", "Bat", "Leopard", "Eagle", "Raven", "Cheetah", "Buffalo", "Hippopotamus"
    ],
    "Entertainment": [
        "Movie", "Music", "Concert", "Game", "Theater", "Dance", "Play", "Sport", "Festival", 
        "Magic", "Juggling", "Clown", "Circus", "Amusement Park", "Roller Coaster", "Opera", 
        "Comedy", "Drama", "Documentary", "Podcast", "YouTube", "Vlog", "Reality Show", 
        "Quiz", "Game Show", "Book", "Magazine", "Puzzles", "TV Show", "Dance", "DJ"
    ],
    "Fantasy": [
        "Vampire", "Dragon", "Unicorn", "Fairy", "Wizard", "Witch", "Mermaid", "Troll", 
        "Griffin", "Phoenix", "Gargoyle", "Elf", "Werewolf", "Zombie", "Doppelganger", 
        "Paradox", "Sorcerer", "Potion", "Magic", "Mystic", "Wand", "Teleport", "Rune", 
        "Dungeon", "Cursed", "Necromancer", "Portal"
    ]
}


def update_timer():
    global seconds
    global minutes
    
    if timer_running:
        seconds += 1
        minutes = seconds // 60
        sec = seconds % 60
        time_str = f"{minutes:02}:{sec:02}"
        canvas.itemconfig(timer_text,text="Time: "+time_str)
        root.after(1000, update_timer)  # Update every 1 second

root=Tk()
root.geometry("600x700")
root.resizable(False, False)
root.title("\"Hnagman\" by Aadhavan")

canvas = Canvas(root, bg="#025718",
           height=700, width=600)

key, val = random.choice(list(themes.items()))
randtheme = key
randword = val[random.randint(0,len(val)-1)]

word = randword

dashcoords = {}

hangmanbodynum = 1

dcordx1 = 30
dcordx2 = 70

dcordym = 367
letlist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
butdict = {}

wrongletnum = 1
wrongletx = 300
wronglety = 135

showletnum = 0
ngs = 0
wrongletclicked=[]
correctlettersclicked=[]

dash=len(word)
score = 0

word_list = []
for i in word.upper():
    word_list.append(i)

def pos(event):
    print("x = " + str(event.x) + ", y = " + str(event.y))

canvas.bind( "<Button-1>", pos )

themetext = "Theme: " + str(randtheme)
canvas.create_text(410, 70, anchor="center", text=themetext, fill = "white", font=("Arial", 20, "bold"))

seconds = -1
minutes = 0
timer_running = True
timer_text = canvas.create_text(410, 35, anchor = "center", text = "Time: 00:00", fill = "white", font=("Arial", 20, "bold"))
update_timer()

def stand():
    canvas.create_line(199, 80, 199, 40, fill = "white", width = 8)
    canvas.create_line(250, 40, 10, 40, fill = "white", width = 10)
    canvas.create_line(30, 21, 30, 300, fill = "white", width = 10)
    canvas.create_line(28, 97, 94, 39, fill = "white", width = 7)

def face():
    canvas.create_oval(225, 80, 175, 130, outline = "white", fill = "#025718", width = 5)
    canvas.create_rectangle(185, 93, 191, 97, outline = "white" , fill = "white", width = 2)
    canvas.create_rectangle(215, 93, 209, 97, outline = "white" , fill = "white", width = 2)
    canvas.create_arc(185, 100, 215, 130, start=0, extent=180, outline="white", width=3)

def body():
    canvas.create_line(199,130,199,231, fill = "white", width = 5)

def leg1():
    canvas.create_line(199,231,163,267, fill = "white", width = 5)

def leg2():
    canvas.create_line(199,231,235,267, fill = "white", width = 5)

def arm1():
    canvas.create_line(199,162,145,183, fill = "white", width = 5)

def arm2():
    canvas.create_line(199,162,253,183, fill = "white", width = 5)

def dashes():
    global dash
    global dcordx1
    global dcordx2
    for i in range(1,dash+1):
        
        if i == 1:
            dashcoords.setdefault(i,[]).extend([dcordx1,dcordx2,dcordym])
            canvas.create_line(dcordx1,dcordym,dcordx2,dcordym, fill = "white", width = 5)
            dcordx1=70*i+30
            print("x = " + str(dcordx1))
            dcordx2=70*(i+1)
            print("y = " + str(dcordx2))


        if i!= 1 and i<=8:
            dashcoords.setdefault(i,[]).extend([dcordx1,dcordx2,dcordym])
            canvas.create_line(dcordx1,dcordym,dcordx2,dcordym, fill = "white", width = 5)
            dcordx1=70*i+30
            print("x = " + str(dcordx1))
            dcordx2=70*(i+1)
            print("y = " + str(dcordx2))


        if i==9:
            dcordx1 = 30
            dcordx2 = 70
            dashcoords.setdefault(i,[]).extend([dcordx1,dcordx2,dcordym+83])
            canvas.create_line(dcordx1,dcordym+83,dcordx2,dcordym+83, fill = "white", width = 5)
            dcordx1=70*(i-8)+30
            print("x = " + str(dcordx1))
            dcordx2=70*(i-8+1)
            print("y = " + str(dcordx2))


        if i>9 and i<=16:
            dashcoords.setdefault(i,[]).extend([dcordx1,dcordx2,dcordym+83])
            canvas.create_line(dcordx1,dcordym+83,dcordx2,dcordym+83, fill = "white", width = 5)
            dcordx1=70*(i-8)+30
            print("x = " + str(dcordx1))
            dcordx2=70*(i-8+1)
            print("y = " + str(dcordx2))

        if i==17:
            dcordx1 = 30
            dcordx2 = 70
            dashcoords.setdefault(i,[]).extend([dcordx1,dcordx2,dcordym+166])
            canvas.create_line(dcordx1,dcordym+166,dcordx2,dcordym+166, fill = "white", width = 5)
            dcordx1=70*(i-16)+30
            print("x = " + str(dcordx1))
            dcordx2=70*(i-16+1)
            print("y = " + str(dcordx2))


        if i>17 and i<=24:
            dashcoords.setdefault(i,[]).extend([dcordx1,dcordx2,dcordym+166])
            canvas.create_line(dcordx1,dcordym+166,dcordx2,dcordym+166, fill = "white", width = 5)
            dcordx1=70*(i-16)+30
            print("x = " + str(dcordx1))
            dcordx2=70*(i-16+1)
            print("y = " + str(dcordx2))


        print(dashcoords)

def showlet(letter, correct_or_wrong):
    global showletnum
    global ngs
    global correctlettersclicked
    global dashcoords
    global timer_running

    if correct_or_wrong:
        if letter in correctlettersclicked:
            if letter == " ":
                print()
            print("Letter already clicked!")
        else:
            for index, item in enumerate(word_list):
                if item == letter:

                    showletnum = showletnum + 1

                    text = tk.StringVar()
                    text.set(letter)

                    DCL = dashcoords[index+1]
                    letterlbl= canvas.create_text((DCL[0]+18), DCL[2]-18, anchor="center", text=letter, fill="white", font=("Arial", 16, "bold"))
                    # letterlbl = tk.Label(root, pady=-100, bg ="#025718", fg = "white", bd = 5, font=("Arial", 16, "bold"), textvariable=text)
                    # letterlbl.place(x=(DCL[0]+7),y=DCL[2]-36)
                    print("\n\n\n" + str(DCL))
                    correctlettersclicked.append(letter)
                    if letter == " ":
                        canvas.create_line(DCL[0],DCL[2],DCL[1],DCL[2], fill = "#025718", width = 5)

                    if showletnum == dash:

                        for index, item in enumerate(word_list):
                            showletnum = showletnum + 1

                            text = tk.StringVar()
                            text.set(item)

                            DCL = dashcoords[index + 1]
                            letterlbl = canvas.create_text((DCL[0] + 18), DCL[2] - 18, anchor="center", text=item,
                                                               fill="white", font=("Arial", 16, "bold"))
                            # letterlbl = tk.Label(root, pady=-100, bg ="#025718", fg = "white", bd = 5, font=("Arial", 16, "bold"), textvariable=text)
                            # letterlbl.place(x=(DCL[0]+7),y=DCL[2]-36)
                            print("\n\n\n" + str(DCL))



                        the_text = canvas.create_text(300, 300, anchor="center", text="You Won! 😄", fill = "white", font=("Arial", 64, "bold"))

                        timer_running = False
                        root.after(3000, restartgame)

    else:
        for index, item in enumerate(word_list):
            if item == letter:

                showletnum = showletnum + 1

                text = tk.StringVar()
                text.set(letter)
                DCL = dashcoords[index + 1]
                letterlbl = canvas.create_text((DCL[0] + 18), DCL[2] - 18, anchor="center", text=letter, fill="red",
                                               font=("Arial", 16, "bold"))
                # letterlbl = tk.Label(root, pady=-100, bg ="#025718", fg = "white", bd = 5, font=("Arial", 16, "bold"), textvariable=text)
                # letterlbl.place(x=(DCL[0]+7),y=DCL[2]-36)
                print("\n\n\n" + str(DCL))



def restartgame():
    root.quit()
    root.destroy()
    run("python hangman.py", check=True)






#    global letlist
#    global bcordx
#    global bcordy
def buttons():
    global ngs
    global dashcoords
    bcordx = 30
    fnldsh = dashcoords[dash]
    bcordy = fnldsh[2]+37

    for i in range(1, len(letlist)+1):
        if (i == 11):
            bcordy = bcordy+34
            bcordx = 30
        if i == 21:
            bcordx = 150
            bcordy = bcordy+34
        letidk = letlist[i-1]
        btn = Button(root, text = letlist[i-1], command = partial(butclick, letlist[i-1]), width=5)
        butdict.setdefault(letlist[i-1],btn)
        print(letlist[i-1] + ": x=" + str(bcordx) + " y=" + str(bcordy))

        canvas.create_window(bcordx, bcordy, window = btn)
        bcordx = bcordx+60

    ng = bcordy+28
    ngs = str(ng)
    ngwhole = '600x' + ngs
    root.geometry(newGeometry=ngwhole)



def nexth():
    global hangmanbodynum
    global wrongletclicked
    global timer_running
    if hangmanbodynum==1:
        face()
    elif hangmanbodynum==2:
        body()
    elif hangmanbodynum==3:
        arm1()
    elif hangmanbodynum==4:
        arm2()
    elif hangmanbodynum==5:
        leg1()
    elif hangmanbodynum==6:
        leg2()

        for i in word_list:
            if i not in correctlettersclicked:
                showlet(i, False)

        the_text = canvas.create_text(300, 300, anchor="center", text="You Lost! 😞", fill = "white", font=("Arial", 64, "bold"))

        root.attributes('-disabled', 1)
        print("You Lost!")
        timer_running = False
        root.after(3000, restartgame)
        


    hangmanbodynum = hangmanbodynum+1










def butclick(btnname):
    global wrongletnum
    global wrongletx
    global wronglety
    global word_list
    global hangmanbodynum
    global wrongletclicked
    global correctlettersclicked
    print(btnname)
    showlet(" ",True)
    if btnname in word_list:
        showlet(btnname, True)
        correctlettersclicked.append(btnname)




    else:
        if btnname in wrongletclicked:
            print("Letter already clicked!")
        else:
            text = tk.StringVar()
            text.set(btnname)
            canvas.create_text(wrongletx,wronglety,text=btnname,fill="white",font=("Arial", 28, "bold"))
            line_length = 20
            canvas.create_line(wrongletx - line_length, wronglety - line_length, wrongletx + line_length, wronglety + line_length, width=5, fill="red")
            wrongletx = wrongletx+50
            nexth()
            wrongletclicked.append(btnname)



dashes()
stand()
buttons()
showlet(" ", True)





#for i in letlist:
#    if ((letlist.index(i)+1) > dash):
#        break
#    showlet(i,(letlist.index(i)+1))
#print("YOOOOOOO: " + str(dashcoords[dash]))












canvas.pack()
mainloop()

