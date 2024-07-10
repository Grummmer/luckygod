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
|文件|模式|图库|音效|关于|                                          |
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
||                                                  ||人数   33 | |
||                                                  | —————————— |
||                                                  |            |
||                                                  | 还剩  32 人 |
||                                                  |            |
||                                                  |  口 音效    |
||                                                  |            |
||                                                  |            |
||                                                  |            |
||                                                  |  _____     |
||                                                  |  |开始|     |
||                                                  |  -----     |
||                                                  |  _____     |
||                                                  |  |开始|     |
||                                                  |  -----     |
||                                                  |  _____     |
||                                                  |  |退出|     |
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
        countbar['text']=xuanze
        filename = path + str(xuanze) + '.jpg'
        img1 = cv2.imread(filename)
        im1 = Image.fromarray(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
        img[0] = ImageTk.PhotoImage(image = im1)
        photos.config(image=img[0])
        root.update_idletasks()
        status["foreground"] = 'red'

def status_colour_green():
    t=threading.Thread(target=oneclass)
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

剩余人数 = tk.Label(root,
                text="剩余33人")
剩余人数.place(x=440, y=260, width=51, height=16)
剩余人数.place_forget()
def 无重结束控制 ():
     root.flag = False
     sound_stop()
     status["foreground"] = 'red'
     xuanze = int(random.choice(number_of_people))
     countbar['text']=xuanze
     filename = path + str(xuanze) + '.jpg'
     img1 = cv2.imread(filename)
     im1 = Image.fromarray(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
     img[0] = ImageTk.PhotoImage(image = im1)
     photos.config(image=img[0])
     root.update_idletasks()
     number_of_people.remove(xuanze)
     剩余人数['text']="剩余"+str(len(set(number_of_people)))+"人"


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
file.add_command(label= str('开始      Up'),
                 command = status_colour_green
                 )
file.add_command(label= str('停止      Down'),
                 command = status_colour_red
                 )
file.add_command(label= str('退出'),
                 command = sys.exit
                 )

menu0.add_cascade(label='文件',menu=file)

#模式菜单
def changeto1():
    fastb.place_forget()
    resetb.place_forget()
    norestart.place_forget()
    norestop.place_forget()
    剩余人数.place_forget()
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
    剩余人数.place_forget()
    fastb.place(x=410, y=295, width=100, height=170)

def changeto3():
    fastb.place_forget()
    exitb.place_forget()
    startb.place_forget()
    stopb.place_forget()
    norestart.place(x=410, y=295, width=100, height=50)
    norestop.place(x=410, y=355, width=100, height=50)
    resetb.place(x=410, y=415, width=100, height=50)
    剩余人数.place(x=440, y=260, width=51, height=16)

mode=Menu(menu0,tearoff=False)#定义不可拖移菜单名称

mode.add_command(label= str('单班抽签'),
                 command = changeto1
                 )
mode.add_command(label= str('瞬间抽签'),
                 command = changeto2
                 )
mode.add_command(label= str('无重复抽签'),
                 command = changeto3
                 )
menu0.add_cascade(label='模式',menu=mode)#一级菜单名称

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

gallery=Menu(menu0,tearoff=False)#定义不可拖移菜单名称
gallery.add_command(label= str('图库1'),
                    command = picture1
                    )
gallery.add_command(label= str('图库2'),
                    command = picture2
                    )
gallery.add_command(label= str('图库3'),
                    command = picture3
                    )
gallery.add_command(label= str('图库4'),
                    command = picture4
                    )
gallery.add_command(label= str('图库5'),
                    command = picture5
                    )

menu0.add_cascade(label='图库',menu=gallery)

#音效菜单
soundeffects=Menu(menu0,tearoff=False)#定义不可拖移菜单名称
soundeffects.add_command(label= str('音效1'),
                 command = sound1
                 )
soundeffects.add_command(label= str('音效2'),
                 command = sound2
                 )
soundeffects.add_command(label= str('音效3'),
                 command = sound3
                 )
soundeffects.add_command(label= str('音效4'),
                 command = sound4
                 )
soundeffects.add_command(label= str('音效5'),
                 command = sound5
                 )

menu0.add_cascade(label='音效',menu=soundeffects)

#关于菜单
#此模块无bug
'''
def leadtoweb():
    webbrowser.open("http://www.baidu.com", new=0)
'''
def juanzeng():
    tk.messagebox.showinfo('捐赠','支付宝账户：13601218240（这不是作者的手机号！！！）')
about=Menu(menu0,tearoff=False)#定义不可拖移菜单名称
'''
about.add_command(label=str('官方网站'),
                     command = leadtoweb
                     )
'''
about.add_command(label=str('捐赠'),
                     command = juanzeng
                     )
menu0.add_cascade(label='关于',menu=about)


##########计数器##########
countbar = tk.Label(root,
    #                bg='white',
                    anchor='se',
                    font=('黑体', 35),
                    bd=10,
                    text = '0',
                    )
countbar.place(x=410, y=10, width=100, height=60)




##########按钮##########
#抽签
fastb = tk.Button(root,
                        text='抽签',
                        font=('黑体', 20),
                        command=fast_mode,
                        )
#开始

startb = tk.Button(root,
                        text='开始',
                        font=('黑体', 20),
                        command=status_colour_green,
                        )
startb.place(x=410, y=295, width=100, height=50)

#停止
stopb = tk.Button(root,
                        text='停止',
                        font=('黑体', 20),
                       command=status_colour_red
                        )
stopb.place(x=410, y=355, width=100, height=50)

#退出
exitb = tk.Button(root,
                        text='退出',
                        font=('黑体', 20),
                        command=sys.exit
                        )
exitb.place(x=410, y=415, width=100, height=50)


norestart = tk.Button(root,
                        text='开始',
                        font=('黑体', 20),
                        command=no_duplication_mode_start,
                        )
startb.place(x=410, y=295, width=100, height=50)

norestop = tk.Button(root,
                        text='停止',
                        font=('黑体', 20),
                       command=无重结束控制
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



##########人数调整##########
human = StringVar()
human.set(33)
label_renshu = tk.Label(root,
                    text='人数',
                    font=('Arial', 12),
                    bd=10)
label_renshu.place(x=410, y=210, width=30, height=20)

def 调整人数():
    number_of_people.clear()
    for i in range(1,int(human.get())+1):
        number_of_people.append(i)
    剩余人数['text']="剩余"+str(len(set(number_of_people)))+"人"

#重置
#TODO 重置command
resetb = tk.Button(root,
                        text='重置',
                        font=('黑体', 20),
                        command=调整人数
                        )

dognumber = tk.Spinbox(root,
                       from_ = 1,
                       to = 5000,
                       textvariable = human,
                       command = 调整人数,
                       increment = 1,
                       )
dognumber.place(x=440, y=210, width=70, height=20)


##########音效##########
var = IntVar()
if var.get() == 1:
    py.mixer.music.set_volume(1.0)
else:
    py.mixer.music.set_volume(0)

def yinxiaokaiguan():
    if var.get() == 1:
        py.mixer.music.set_volume(1.0)
    else:
        py.mixer.music.set_volume(0)


soundeffectchoose = tk.Checkbutton(root,
                                   text='音效',
                                   variable=var,
                                   command=yinxiaokaiguan
                                   )
soundeffectchoose.place(x=440, y=240, width=51, height=16)

#############图片###########
photos = tk.Label(root,
                    image = '',
#                    bg='white',
                    bd=10)
photos.place(x=10, y=75, width=390, height=390)


###########################################################
#########################主程序功能#########################
###########################################################


##########单班抽签##########
def oneclass ():
     root.flag=True
     global path
     while root.flag:
        people = int(human.get())
        xuanze = random.randrange(1,people+1)#这个地方一定要加一
        countbar['text']=xuanze
        filename = path + str(xuanze) + '.jpg'
        img1 = cv2.imread(filename)
        im1 = Image.fromarray(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
        img[0] = ImageTk.PhotoImage(image = im1)
        photos.config(image=img[0])
        root.update_idletasks()

##########无重复抽签############
def no_duplication_mode():
    root.flag=True
    global path
    while root.flag:
        xuanze = int(random.choice(number_of_people))
        countbar['text']=xuanze
        filename = path + str(xuanze) + '.jpg'
        img1 = cv2.imread(filename)
        im1 = Image.fromarray(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
        img[0] = ImageTk.PhotoImage(image = im1)
        photos.config(image=img[0])
        root.update_idletasks()

#快捷键
def kaishi(event):
    status_colour_green()

def tingzhi(event):
    status_colour_red()
#TODO改快捷键，防止调用快捷键的时候触发人数调整
root.bind_all("<KeyPress-Up>", kaishi)
root.bind_all("<KeyPress-Down>", tingzhi)


root['menu']=menu0#窗口root的menu是menu0
root.mainloop()
