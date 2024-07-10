'''
-*-coding:UTF-8-*-
enviro: python3.12.4
Program function: This program is a lucky draw assistant, which can be used in class, party, etc.


This program is made by the greatest Eden Li, and the program is open source.
If you want to distribute this program, please contact the author.
If you want to use this program for commercial purposes, please contact the author.
If you want to use this program for illegal purposes, JUST DO IT and GOOD LUCK BRO.

'''
'''
------------------------------------------------------------------
|☺LuckyGod5.0 - Lottery Assistant                          |-|口|X|
------------------------------------------------------------------
|File|Mode|Gallery|Sound|About|                                          |
------------------------------------------------------------------
|    十     ·   一       ·       ·  |  |  | --   ---   ---------- |
|    一     一   一     ----     -  曰  | | |_   |  |   |       0| |
|    ¥      —___△___   -------  |  |   |   _| .|__|   |--------- |
|                                                                |
| __________________________________________________       _     |
||                                                  |    -   -   |
||                                                  |   -  -  -  |
||                                                  |    -   -   |
||                                                  |      -     |
||                                                  |            |
||                                                  |            |
||                                                  | —————————— |
||                                                  ||People 33| |
||                                                  | —————————— |
||                                                  |            |
||                                                  |Remain32people|
||                                                  |            |
||                                                  |  口 Sound    |
||                                                  |            |
||                                                  |            |
||                                                  |            |
||                                                  |  _____     |
||                                                  |  |START|   |
||                                                  |  -----     |
||                                                  |  _____     |
||                                                  |  |STOP|    |
||                                                  |  -----     |
||                                                  |  _____     |
||                                                  |  |EXIT|    |
||__________________________________________________|   ----     |
|________________________________________________________________|
'''
import random
from tkinter  import *
import pygame as py
import tkinter as tk
import tkinter.messagebox
import threading
from PIL import Image, ImageTk
import cv2
import webbrowser
import time
import sys
#from os import environ
#environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

#########INIT##########
root= tk.Tk()
root.geometry("520x495")#The size of the window
root.title('LuckyGod5.0 - Lottery Assistant')#The title of the window
root.resizable(False,False)#The window can't be resized
root.iconbitmap('main.ico')#The icon of the window
root.flag = True
img = [None]
path = 'picture/gallery1/'
number_of_people = []
#The number of people
number_of_people.clear()
for i in range(1,34):
    number_of_people.append(i)
###########################################################
#########################交互界面###########################
###########################################################
py.mixer.init()
musound = r'music/music1.mp3'

def sound1():
    global musound
    musound = r'music/music1.mp3'

def sound2():
    global musound
    musound = r'music/music2.mp3'

def sound3():
    global musound
    musound = r'music/music2.mp3'

def sound4():
    global musound
    musound = r'music/music2.mp3'

def sound5():
    global musound
    musound = r'music/music2.mp3'

def sound_start():
    global musound
    py.mixer.music.load(musound)
    py.mixer.music.play(-1,0)

def sound_stop():
    py.mixer.music.stop()

def fast_mode():
        status["foreground"] = 'green'
        time.sleep(0.1)
        people = int(human.get())
        xuanze = random.randrange(1,people+1)#This place must be added one
        count_bar['text']=xuanze
        filename = path + str(xuanze) + '.jpg'
        img1 = cv2.imread(filename)
        im1 = Image.fromarray(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
        img[0] = ImageTk.PhotoImage(image = im1)
        photos.config(image=img[0])
        root.update_idletasks()
        status["foreground"] = 'red'

def status_colour_green():
    t=threading.Thread(target=default_mode)
    t.start()
    sound_start()
    status["foreground"] = 'green'

def status_colour_red():
     root.flag = False
     sound_stop()
     status["foreground"] = 'red'

def no_duplication_mode_start():
    if len(set(number_of_people))== 0:
        tk.messagebox.showinfo("Information", "The number of people is 0, please reset the number of people.")
    else:
        a=threading.Thread(target=no_duplication_mode)
        a.start()
        sound_start()
        status["foreground"] = 'green'

remainingPeople = tk.Label(root,
                text="Remain 33 people")
remainingPeople.place(x=440, y=260, width=51, height=16)
remainingPeople.place_forget()
def no_duplication_mode_stop ():
     root.flag = False
     sound_stop()
     status["foreground"] = 'red'
     xuanze = int(random.choice(number_of_people))
     count_bar['text']=xuanze
     filename = path + str(xuanze) + '.jpg'
     img1 = cv2.imread(filename)
     im1 = Image.fromarray(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
     img[0] = ImageTk.PhotoImage(image = im1)
     photos.config(image=img[0])
     root.update_idletasks()
     number_of_people.remove(xuanze)
     remainingPeople['text']="Remain "+str(len(set(number_of_people)))+" people"


#########标题##########
biaoti = tk.Label(root,
            text='LuckyGod V5.0',    # The title of the window
            font=('Arial', 48),     # The font of the title
            foreground='lightskyblue',  #The color of the title
            width=15, height=2  # The size of the title
              )
biaoti.place(x=10, y=10, width=400, height=60)


##########菜单##########
menu0=Menu(root)#The menu of the window


#文件菜单
file=Menu(menu0,tearoff=False)#Define the menu name that can't be dragged
file.add_command(label= str('START      Up'),
                 command = status_colour_green
                 )
file.add_command(label= str('STOP      Down'),
                 command = status_colour_red
                 )
file.add_command(label= str('EXIT'),
                 command = sys.exit
                 )

menu0.add_cascade(label='File',menu=file)

#模式菜单
def changeto1():
    fastb.place_forget()
    resetb.place_forget()
    norestart.place_forget()
    norestop.place_forget()
    remainingPeople.place_forget()
    startb.place(x=410, y=295, width=100, height=50)
    stopb.place(x=410, y=355, width=100, height=50)
    exitb.place(x=410, y=415, width=100, height=50)

def changeto2():
    startb.place_forget()
    stopb.place_forget()
    exitb.place_forget()
    resetb.place_forget()
    norestart.place_forget()
    norestop.place_forget()
    remainingPeople.place_forget()
    fastb.place(x=410, y=295, width=100, height=170)

def changeto3():
    fastb.place_forget()
    exitb.place_forget()
    startb.place_forget()
    stopb.place_forget()
    norestart.place(x=410, y=295, width=100, height=50)
    norestop.place(x=410, y=355, width=100, height=50)
    resetb.place(x=410, y=415, width=100, height=50)
    remainingPeople.place(x=440, y=260, width=51, height=16)

mode=Menu(menu0,tearoff=False)

mode.add_command(label= str('Default Mode'),
                 command = changeto1
                 )
mode.add_command(label= str('Instant Mode'),
                 command = changeto2
                 )
mode.add_command(label= str('No Duplication Mode'),
                 command = changeto3
                 )
menu0.add_cascade(label='Mode',menu=mode)

#图库菜单
def picture1():
      global path
      path = 'picture/gallery1/'

def picture2():
      global path
      path = 'picture/gallery2/'

def picture3():
      global path
      path = 'picture/gallery3/'

def picture4():
      global path
      path = 'picture/gallery4/'

def picture5():
      global path
      path = 'picture/gallery5/'

gallery=Menu(menu0,tearoff=False)
gallery.add_command(label= str('Gallery1'),
                    command = picture1
                    )
gallery.add_command(label= str('Gallery2'),
                    command = picture2
                    )
gallery.add_command(label= str('Gallery3'),
                    command = picture3
                    )
gallery.add_command(label= str('Gallery4'),
                    command = picture4
                    )
gallery.add_command(label= str('Gallery5'),
                    command = picture5
                    )

menu0.add_cascade(label='Gallery',menu=gallery)

#音效菜单
soundeffects=Menu(menu0,tearoff=False)#定义不可拖移菜单名称
soundeffects.add_command(label= str('Sound1'),
                 command = sound1
                 )
soundeffects.add_command(label= str('Sound2'),
                 command = sound2
                 )
soundeffects.add_command(label= str('Sound3'),
                 command = sound3
                 )
soundeffects.add_command(label= str('Sound4'),
                 command = sound4
                 )
soundeffects.add_command(label= str('Sound5'),
                 command = sound5
                 )

menu0.add_cascade(label='Sound',menu=soundeffects)


'''
def leadtoweb():
    webbrowser.open("http://www.baidu.com", new=0)
'''
def show_donate_message():
    tk.messagebox.showinfo('Donate','If you like this program, you can donate to the author.')
about=Menu(menu0,tearoff=False)#定义不可拖移菜单名称
'''
about.add_command(label=str('官方网站'),
                     command = leadtoweb
                     )
'''
about.add_command(label=str('Donate'),
                     command = show_donate_message
                     )
menu0.add_cascade(label='About',menu=about)


##########COUNT_BAR##########
count_bar = tk.Label(root,
    #                bg='white',
                    anchor='se',
                    font=('黑体', 35),
                    bd=10,
                    text = '0',
                    )
count_bar.place(x=410, y=10, width=100, height=60)




##########按钮##########
#抽签
fastb = tk.Button(root,
                        text='LOTTERY',
                        font=('黑体', 20),
                        command=fast_mode,
                        )
#开始

startb = tk.Button(root,
                        text='START',
                        font=('黑体', 20),
                        command=status_colour_green,
                        )
startb.place(x=410, y=295, width=100, height=50)

#停止
stopb = tk.Button(root,
                        text='STOP',
                        font=('黑体', 20),
                       command=status_colour_red
                        )
stopb.place(x=410, y=355, width=100, height=50)

#退出
exitb = tk.Button(root,
                        text='EXIT',
                        font=('黑体', 20),
                        command=sys.exit
                        )
exitb.place(x=410, y=415, width=100, height=50)


norestart = tk.Button(root,
                        text='START',
                        font=('黑体', 20),
                        command=no_duplication_mode_start,
                        )
startb.place(x=410, y=295, width=100, height=50)

norestop = tk.Button(root,
                        text='STOP',
                        font=('黑体', 20),
                       command=no_duplication_mode_stop
                        )
stopb.place(x=410, y=355, width=100, height=50)


norestart.place_forget()
##########状态灯##########
status = tk.Label(root,
                  text='◉',
                 font=('黑体', 80),
                  foreground='red',
                   )
status.place(x=410, y=80, width=100, height=100)


norestart.place_forget()



##########ADJUST_PEOPLE##########
human = StringVar()
human.set(33)
label_renshu = tk.Label(root,
                    text='People',
                    font=('Arial', 12),
                    bd=10)
label_renshu.place(x=410, y=210, width=30, height=20)

def updateNumberOfPeople():
    number_of_people.clear()
    for i in range(1,int(human.get())+1):
        number_of_people.append(i)
    remainingPeople['text']="Remain "+str(len(set(number_of_people)))+" people"

resetb = tk.Button(root,
                        text='Reset',
                        font=('黑体', 20),
                        command=updateNumberOfPeople
                        )

dognumber = tk.Spinbox(root,
                       from_ = 1,
                       to = 5000,
                       textvariable = human,
                       command = updateNumberOfPeople,
                       increment = 1,
                       )
dognumber.place(x=440, y=210, width=70, height=20)


##########SOUND##########
var = IntVar()
if var.get() == 1:
    py.mixer.music.set_volume(1.0)
else:
    py.mixer.music.set_volume(0)

def switch_audio():
    if var.get() == 1:
        py.mixer.music.set_volume(1.0)
    else:
        py.mixer.music.set_volume(0)


soundeffectchoose = tk.Checkbutton(root,
                                   text='Sound',
                                   variable=var,
                                   command=switch_audio
                                   )
soundeffectchoose.place(x=440, y=240, width=51, height=16)

#############IMAGE###########
photos = tk.Label(root,
                    image = '',
#                    bg='white',
                    bd=10)
photos.place(x=10, y=75, width=390, height=390)


###########################################################
#########################MAIN_PROGRAM######################
###########################################################


##########DEFAULT_MODE##########
def default_mode ():
     root.flag=True
     global path
     while root.flag:
        people = int(human.get())
        xuanze = random.randrange(1,people+1)#This place must be added one
        count_bar['text']=xuanze
        filename = path + str(xuanze) + '.jpg'
        img1 = cv2.imread(filename)
        im1 = Image.fromarray(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
        img[0] = ImageTk.PhotoImage(image = im1)
        photos.config(image=img[0])
        root.update_idletasks()

##########NO_DUPLICATION_MODE############
def no_duplication_mode():
    root.flag=True
    global path
    while root.flag:
        xuanze = int(random.choice(number_of_people))
        count_bar['text']=xuanze
        filename = path + str(xuanze) + '.jpg'
        img1 = cv2.imread(filename)
        im1 = Image.fromarray(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
        img[0] = ImageTk.PhotoImage(image = im1)
        photos.config(image=img[0])
        root.update_idletasks()

#hotkey
def start(event):
    status_colour_green()

def stop(event):
    status_colour_red()
root.bind_all("<KeyPress-Up>", start)
root.bind_all("<KeyPress-Down>", stop)


root['menu']=menu0#The menu of the window
root.mainloop()
