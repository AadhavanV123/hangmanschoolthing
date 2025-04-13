import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import time
from functools import partial
import random
import asyncio
import os
from subprocess import run
from tkinter import PhotoImage
import sys
import pandas as pd
from pygame import mixer

## NEED TO DO SOUND EFFECTS (ONLY IN HOME) AND NEED TO ADD PLAYER NAMES

##Total wins, total losses
##
##Average incorrect guesses per game
##
##Average time taken per game
##
##Longest streak of correct guesses
##
##Words guessed correctly in a row


##
##import tkinter as tk
##
##from pygame import mixer
##
##mixer.init()
##sound = mixer.Sound("sound.ogg")
##
##root = tk.Tk()
##tk.Button(root, command=sound.play).pack()
##root.mainloop()
##



themes = {
    "Food": [
        "APPLE", "BANANA", "ORANGE", "CAKE", "COOKIE", "PIZZA", "BURGER", "FRIES", 
        "SPAGHETTI", "ICE CREAM", "DONUT", "MUFFIN", "CHOCOLATE", "LOLLIPOP", "WAFFLE", 
        "TACO", "SUSHI", "STEAK", "SALAD", "CHEESE", "CEREAL", "PUDDING", "POPCORN", 
        "CUPCAKE", "PIE", "LEMON", "WATERMELON", "GRAPES", "BACON", "HOT DOG", 
        "SANDWICH", "TOAST", "MILK", "JUICE", "RICE", "NOODLES", "BREAD", "CORN", "PEAS", 
        "YOGURT", "CHIPS", "PICKLES", "CARROT", "TOMATO", "CUCUMBER", "GARLIC", "ONION"
    ],
    "Toys": [
        "BALL", "DOLL", "TOY CAR", "LEGO", "DRONE", "PUZZLE", "KITE", 
        "TEDDY BEAR", "YO-YO", "HULA HOOP", "BICYCLE", "TRAMPOLINE", "SWING", "TOY TRAIN", 
        "RUBBER DUCK", "MARBLES", "PLUSHIE", "ACTION FIGURE", "FRISBEE", "BOUNCY BALL", 
        "BUILDING BLOCKS", "TOY ROBOT", "WATER GUN", "RUBBER BAND", "BOUNCY CASTLE"
    ],
    "Shapes": [
        "CIRCLE", "SQUARE", "TRIANGLE", "RECTANGLE", "STAR", "HEART", "DIAMOND", "OVAL", 
        "CUBE", "CONE", "SPHERE", "PYRAMID", "ARROW", "CROSS", "MOON", "SUN", "WAVE", 
        "SPIRAL", "HEXAGON", "OCTAGON", "ELLIPSE", "CYLINDER", "CONE", "BOX", "LADDER"
    ],
    "Weather": [
        "RAIN", "SUN", "SNOW", "WIND", "CLOUD", "STORM", "THUNDER", "FOG", "HAIL", 
        "DRIZZLE", "HEATWAVE", "TORNADO", "LIGHTNING", "BLIZZARD", "RAINBOW", "MIST", 
        "HURRICANE", "CYCLONE", "CLEAR", "CHILLY", "SLEET", "MONSOON", "FROST"
    ],
    "Technology": [
        "COMPUTER", "PHONE", "LAPTOP", "TABLET", "CAMERA", "WI-FI", "DRONE", "PRINTER", 
        "MOUSE", "KEYBOARD", "TV", "SMARTWATCH", "APP", "GAME", "WEBSITE", "E-MAIL", 
        "PASSWORD", "CLOUD", "BLUETOOTH", "VIDEO", "SPEAKER", "ROUTER", "SCANNER", "SEARCH", 
        "BATTERY", "FLASHLIGHT", "CABLE", "SMARTPHONE"
    ],
    "Nature": [
        "TREE", "FLOWER", "MOUNTAIN", "RIVER", "OCEAN", "CLOUD", "ROCK", "BIRD", "FISH", 
        "ANIMAL", "GRASS", "LAKE", "BEACH", "FOREST", "SKY", "SUNFLOWER", "CACTUS", "RAIN", 
        "DESERT", "POND", "BUSH", "LEAF", "SEA", "RAINFOREST", "SUN", "MEADOW", "LAKESIDE"
    ],
    "Places": [
        "HOUSE", "PARK", "ZOO", "MUSEUM", "LIBRARY", "SCHOOL", "BEACH", "RESTAURANT", 
        "HOSPITAL", "FARM", "CHURCH", "HOTEL", "MALL", "BANK", "STORE", "AIRPORT", "CITY", 
        "TOWN", "FARM", "SHOP", "MOUNTAIN", "CAVE", "SCHOOL", "PLAYGROUND", "GARDEN"
    ],
    "Objects": [
        "CHAIR", "TABLE", "LAMP", "PHONE", "BAG", "CLOCK", "KEY", "DOOR", "PLATE", 
        "FORK", "SPOON", "BRUSH", "SHIRT", "SHOES", "JACKET", "SOCKS", "PEN", "NOTEBOOK", 
        "BOOK", "TOOTHBRUSH", "WALLET", "PILLOW", "GLASSES", "MUG", "TOWEL", "SCISSORS", 
        "RUG", "MIRROR", "HELMET", "SCARF", "CUSHION"
    ],
    "Animals": [
        "DOG", "CAT", "BIRD", "FISH", "LION", "TIGER", "ELEPHANT", "WHALE", "SHARK", 
        "RABBIT", "HORSE", "MONKEY", "BEAR", "KANGAROO", "KOALA", "PENGUIN", "SNAKE", 
        "GIRAFFE", "ZEBRA", "CROCODILE", "PANDA", "PARROT", "GOAT", "COW", "SHEEP", "PIG", 
        "DUCK", "CHICKEN", "HORSE", "FROG", "BAT", "EAGLE", "SPIDER", "TURTLE", "OWL"
    ],
    "Entertainment": [
        "MOVIE", "MUSIC", "GAME", "TV SHOW", "PLAY", "SPORT", "DANCE", "COMEDY", "DRAMA", 
        "OPERA", "CONCERT", "JOKE", "PUZZLES", "BOOKS", "MAGAZINES", "PODCAST", "VLOG", 
        "VIDEO", "MOVIE THEATER", "VIDEO GAME", "GAME SHOW", "CARTOON", "QUIZ", "DANCE PARTY", 
        "MUSIC VIDEO", "YOUTUBE", "RADIO"
    ],
    "Fantasy": [
        "DRAGON", "VAMPIRE", "WITCH", "WIZARD", "UNICORN", "MERMAID", "FAIRY", "ELF", 
        "TROLL", "ZOMBIE", "WEREWOLF", "GHOST", "SORCERER", "POTION", "MAGIC", "SPELL", 
        "MONSTER", "GRIFFIN", "GOLEM", "PHOENIX", "BASILISK", "GOBLIN", "CHIMERA", 
        "ENCHANTED", "CASTLE", "SWORD", "CURSED", "WAND"
    ],
    "Sports": [
        "SOCCER", "BASKETBALL", "BASEBALL", "TENNIS", "FOOTBALL", "GOLF", "HOCKEY", 
        "VOLLEYBALL", "CRICKET", "RUGBY", "SWIMMING", "CYCLING", "BOXING", "RUNNING", 
        "GYMNASTICS", "WEIGHTLIFTING", "SKATING", "SNOWBOARDING", "SURFING", "ROWING", 
        "PING PONG", "BADMINTON", "WRESTLING", "TRACK", "FIELD", "BOWLING", "KARATE"
    ],
    "Vehicles": [
        "CAR", "BUS", "BICYCLE", "TRUCK", "MOTORCYCLE", "SCOOTER", "PLANE", "BOAT", 
        "TRAIN", "SUBWAY", "HELICOPTER", "TAXI", "LIMO", "VAN", "TRACTOR", "SPACESHIP", 
        "YACHT", "SHIP", "BUS STOP", "CART", "ROCKET", "ICE CREAM TRUCK", "RACING CAR"
    ],
    "Colors": [
        "RED", "BLUE", "GREEN", "YELLOW", "ORANGE", "PURPLE", "PINK", "BROWN", "BLACK", 
        "WHITE", "GRAY", "CYAN", "MAGENTA", "TEAL", "IVORY", "BEIGE", "VIOLET", "GOLD", 
        "SILVER", "INDIGO", "TURQUOISE", "LAVENDER", "MINT", "CRIMSON"
    ]
}





root=Tk()
root.geometry("600x700")
root.resizable(False, False)
root.title("\"Hnagman\" by Aadhavan")
icon = PhotoImage(file="hangmanicon.png")
root.iconphoto(False, icon)

canvas = Canvas(root, bg="#025718",
           height=700, width=600)
scorefilepath = "score.csv"
score = 0
seconds = -1
hint_time = 0
try:
    scoredf = pd.read_csv(scorefilepath)
except FileNotFoundError:
    scoredf = pd.DataFrame(columns=['Score'])

def game():
    def exitgame():
        global scoredf
        global scorefilepath
        global score
        if 'Score' in scoredf.columns:
            new_score = pd.DataFrame({'Score': [score]})
            scoredf = pd.concat([scoredf, new_score], ignore_index=True)
        else:
            scoredf = pd.DataFrame({'Score': [score]})
        scoredf.to_csv(scorefilepath, index=False)
        root.quit()
        root.destroy()
    canvas.delete("all")
    global key
    global val
    global randtheme
    global randword
    global word
    global dashcoords
    global hangmanbodynum
    global dcordx1
    global dcordx2
    global dcordym
    global letlist
    global butdict
    global wrongletnum
    global wrongletx
    global wronglety
    global showletnum
    global ngs
    global wrongletclicked
    global correctlettersclicked
    global dash
    global score
    global word_list
    global seconds
    global minutes
    global timer_running
    global timer_text
    global keyspressed
    global haxtext
    global haxbro
    global time_str
    global hint_time
    global hint_time_sec
    global hint_time_min
    global hint_time
    global hint_num_allow
    global hint_btns
    global hint_btn_num
    global hint_word
    global hint_let
    global no_of_hints
    global score
    global scorefilepath
    global scoredf
    global score_lbl
    global progress_bar
    global progress_var
    global progress_inc_val
    global onlyletword

    haxtext = ""
    onlyletword = ""
    keyspressed = ""
        
    key, val = random.choice(list(themes.items()))
    randtheme = key
    randword = val[random.randint(0,len(val)-1)]

    word = randword
    hint_word = word
    hint_let = ""

    dashcoords = {}

    hangmanbodynum = 1

    dcordx1 = 30
    dcordx2 = 70

    dcordym = 367
    letlist = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    butdict = {}

    wrongletnum = 1
    wrongletx = 300
    wronglety = 220

    showletnum = 0
    ngs = 0
    wrongletclicked=[]
    correctlettersclicked=[]

    dash=len(word)
    hint_num_allow = 3
    hint_btns = {}
    hint_btn_num = 1
    no_of_hints = 0

    progress_inc_val = 1

    word_list = []
    for i in word.upper():
        word_list.append(i)

    def pos(event):
        print("x = " + str(event.x) + ", y = " + str(event.y))

    canvas.bind( "<Button-1>", pos )

    
    minutes = 0
    timer_running = True
    timer_text = canvas.create_text(410, 90, anchor = "center", text = "Time: 00:00", fill = "white", font=("Arial", 20, "bold"))
    themetext = "Theme: " + str(randtheme)
    canvas.create_text(417, 120, anchor="center", text=themetext, fill = "white", font=("Arial", 20, "bold"))

    score_lbl = canvas.create_text(417, 60, anchor="center", text="Score: 00", fill = "white", font=("Arial", 20, "bold"))


    exitgamebtn = Button(root, text = "Exit 😞" , command = exitgame, width=8)
    canvas.create_window(545, 60, window = exitgamebtn)

    for i in word:
        if i.upper() in letlist:
            onlyletword += i
    progress_inc_val = ((1/len(onlyletword))*100)
    print("progreihsoiuefhgo9iuyrfg90uiewy: " + str(progress_inc_val))
    progress_bar = ttk.Progressbar(root, length=390, mode = "determinate")
    canvas.create_window(300, 20, window = progress_bar)
    progress_bar["value"] = 1
    
    def update_timer():
        global seconds
        global minutes
        global timer_text
        global time_str
        global hint_time
        global hint_time_sec
        global hint_time_min
        global hint_num_allow
        global hint_btn_num
        global no_of_hints
        global score
        global score_lbl
        
        
        if timer_running:
            seconds += 1
            minutes = seconds // 60
            sec = seconds % 60
            time_str = f"{minutes:02}:{sec:02}"
            canvas.itemconfig(timer_text,text="Time: "+time_str)
            root.after(1000, update_timer)
            hint_time_min = hint_time // 60
            hint_time_sec = hint_time % 60
            if minutes == hint_time_min and sec == hint_time_sec:
                if no_of_hints <= 4:
                    print("noofhintqwes: " + str(no_of_hints))
                    showhintbtn()
                hint_btn_num +=1
                hint_time = hint_time + 30
                hint_time_min = hint_time // 60
                hint_time_sec = hint_time % 60

            canvas.itemconfig(score_lbl,text=f"Score: {score:02}")
        
    def showhintbtn():
        global hint_btns
        global hint_btn_num
        global hint_word
        global no_of_hints
        print("hint yay")
        btn = Button(root, text = "Hint x" + str(hint_btn_num), command = partial(hintbtn, hint_btn_num), width=8)
        canvas.create_window(220+60*int(hint_btn_num), 170, window = btn)
        hint_btns["hint" + str(hint_btn_num)] = btn
        print(hint_btns)
        no_of_hints = no_of_hints + 1
        print("noofhints: " + str(no_of_hints))

    def hintbtn(num):
        global hint_word
        global hint_let
        global hint_btns
        global correctlettersclicked
        print("btn" + str(num) + " clicked")
        for i in hint_word:
            print("let:",i)
            if i in correctlettersclicked:
                print(i,"yes")
                hint_word = hint_word.replace(i, "")
                print("hntword:",hint_word)
        hint_let = random.choice(hint_word)
        print(hint_let)
        print(hint_word)
        showlet(hint_let, True)
        hint_btns["hint" + str(num)].destroy()
        print("clc: " + str(correctlettersclicked))
        


    
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
        global dashcoords
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
        global score
        global score_lbl
        global progress_var
        
        if correct_or_wrong:
            if letter in correctlettersclicked:
                if letter == " " or letter == "'" or letter == "-":
                    print()
                print("Letter already clicked!")
            else:
                for index, item in enumerate(word_list):
                    if item == letter:

                        showletnum = showletnum + 1

                        text = tk.StringVar()
                        text.set(letter)

                        DCL = dashcoords[index+1]

                        if letter == " ":
                            canvas.create_line(DCL[0],DCL[2],DCL[1],DCL[2], fill = "#025718", width = 5)
##                        elif letter == "'":
##                            canvas.create_line(DCL[0],DCL[2],DCL[1],DCL[2], fill = "#025718", width = 5)
##                            letterlbl = canvas.create_text((DCL[0]), DCL[2] - 18, anchor="center", text="’",
##                                                                   fill="white", font=("Arial", 50, "bold"))
                        elif letter == "-":
                            canvas.create_line(DCL[0],DCL[2],DCL[1],DCL[2], fill = "#025718", width = 5)
                            canvas.create_line(DCL[0]+5,DCL[2]-18,DCL[1]-5,DCL[2]-18, fill = "white", width = 5)
##                            letterlbl = canvas.create_text((DCL[0] + 18), DCL[2] - 18, anchor="center", text="-",
##                                                                   fill="white", font=("Arial", 16, "bold"))

                        else:
                            progress_bar["value"] += progress_inc_val
                            score += 1
                            canvas.itemconfig(score_lbl,text=f"Score: {score:02}")
                            letterlbl= canvas.create_text((DCL[0]+18), DCL[2]-18, anchor="center", text=letter, fill="white", font=("Arial", 16, "bold"))
                        # letterlbl = tk.Label(root, pady=-100, bg ="#025718", fg = "white", bd = 5, font=("Arial", 16, "bold"), textvariable=text)
                        # letterlbl.place(x=(DCL[0]+7),y=DCL[2]-36)
                        print("\n\n\n" + str(DCL))
                        correctlettersclicked.append(letter)
                        
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
        global score
        global seconds
        global hint_time
        root.quit()
        root.destroy()
        run("python hangman.py CONTINUE " + str(score) + " " + str(seconds) + " " + str(hint_time), check=True)
        

    



    #    global letlist
    #    global bcordx
    #    global bcordy
    def buttons():
        global ngs
        global dashcoords
        bcordx = 30
        fnldsh = dashcoords[int(dash)]
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
        global score
        global score_lbl
        
        print(btnname)
        showlet(" ",True)
        if btnname in word_list:
            showlet(btnname, True)
            correctlettersclicked.append(btnname)




        else:
            if btnname in wrongletclicked:
                print("Letter already clicked!")
            else:
                score = score - 1
                canvas.itemconfig(score_lbl,text=f"Score: {score:02}")
                text = tk.StringVar()
                text.set(btnname)
                canvas.create_text(wrongletx,wronglety,text=btnname,fill="white",font=("Arial", 28, "bold"))
                line_length = 20
                canvas.create_line(wrongletx - line_length, wronglety - line_length, wrongletx + line_length, wronglety + line_length, width=5, fill="red")
                wrongletx = wrongletx+50
                nexth()
                wrongletclicked.append(btnname)
                


    def changehaxtext():
        global haxbro
        
        root.after(3000, canvas.itemconfig(haxbro,text=""))
        #

    def haxdoing():
        global haxtext
        global haxbro
        var = IntVar()
        root.after(1000, var.set, 1)
        haxtext = "hax: " + randword.upper()
        haxbro = canvas.create_text(80, 15, anchor="center", text=haxtext, fill = "white", font=("Arial", 5, "bold"))
    ##  
        root.wait_variable(var)   

    def key_handler(event):
        global keyspressed
        global haxtext
        global haxbro
        keyspressed += str(event.char)
        #print("Keys: " + keyspressed)
        if "hangmanhax" in keyspressed:
            print("Ok bro")
            keyspressed = ""
            haxtext = "hax: " + randword.upper()
##            haxbro = canvas.create_text(80, 15, anchor="center", text=haxtext, fill = "white", font=("Arial", 10, "bold"))
####            for i in word_list:
####                if i not in correctlettersclicked:
####                    showlet(i, False)
##            #changehaxtext()
##            time.sleep(1)
##            canvas.itemconfig(haxbro,text="        ")
            haxdoing()
            canvas.itemconfig(haxbro,text="               ")

    root.bind("<Key>", key_handler)
    
    update_timer()
    dashes()
    stand()
    buttons()
    showlet(" ", True)
##    showlet("'", True)
    showlet("-", True)

    def changehaxtext():
        global haxbro
        
        root.after(3000, canvas.itemconfig(haxbro,text=""))
        #

    def haxdoing():
        global haxtext
        global haxbro
        var = IntVar()
        root.after(250, var.set, 1)
        haxtext = "hax: " + randword.upper()
        haxbro = canvas.create_text(80, 15, anchor="center", text=haxtext, fill = "white", font=("Arial", 5, "bold"))
    ##  
        root.wait_variable(var)   

    def key_handler(event):
        global keyspressed
        global haxtext
        global haxbro
        keyspressed += str(event.char)
        #print("Keys: " + keyspressed)
        if "hangmanhax" in keyspressed:
            print("Ok bro")
            keyspressed = ""
            haxtext = "hax: " + randword.upper()
##            haxbro = canvas.create_text(80, 15, anchor="center", text=haxtext, fill = "white", font=("Arial", 10, "bold"))
####            for i in word_list:
####                if i not in correctlettersclicked:
####                    showlet(i, False)
##            #changehaxtext()
##            time.sleep(1)
##            canvas.itemconfig(haxbro,text="        ")
            haxdoing()
            canvas.itemconfig(haxbro,text="        ")

    root.bind("<Key>", key_handler)
    


    #for i in letlist:
    #    if ((letlist.index(i)+1) > dash):
    #        break
    #    showlet(i,(letlist.index(i)+1))
    #print("YOOOOOOO: " + str(dashcoords[dash]))




highscore_text = scoredf['Score'].max()
#game()
def exitgamenormal():
    root.quit()
    root.destroy()

if len(sys.argv) > 1:
    score = int(sys.argv[2])
    seconds = int(sys.argv[3])+3
    hint_time = int(sys.argv[4])
    if sys.argv[1] == "CONTINUE":
        game()
    
else:
        
    play = Button(root, text = "Play 😄" , command = game, width=10)
    canvas.create_window(300, 270, window = play)
    exitgame = Button(root, text = "Exit 😞" , command = exitgamenormal, width=10)
    canvas.create_window(300, 420, window = exitgame)
    the_text = canvas.create_text(300, 100, anchor="center", text="\"Hnagman\" by Aadhavan", fill = "white", font=("Arial", 32, "bold"))
    highscorelbl  = canvas.create_text(300, 185, anchor="center", text="HIGHSCORE: " + str(highscore_text), fill = "white", font=("Arial", 32, "bold"))

canvas.pack()
mainloop()

