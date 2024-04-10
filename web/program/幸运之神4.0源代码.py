#本程序由伟大的李一田倾力制作

#我也不知道为什么要import这么多插件……
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

#########初始化##########
root= tk.Tk()
root.geometry("520x510")#窗口大小
root.title('幸运之神V4.0')#标题名称
root.resizable(False,False)#窗口大小不能改变
root.iconbitmap('./main.ico')#窗口图标
root.flag = True
img = [None]
path = '.\\picture\\gallery1\\' 
  
###########################################################
#########################交互界面###########################
###########################################################
py.mixer.init()
musound = r'.\music\music1.mp3'

def sound1():
    global musound
    musound = r'.\music\music1.mp3'

def sound2():
    global musound
    musound = r'.\music\music2.mp3'

def sound3():
    global musound
    musound = r'.\music\music3.mp3'

def sound4():
    global musound
    musound = r'.\music\music4.mp3'

def sound5():
    global musound
    musound = r'.\music\music5.mp3'

def soundstart():
    global musound
    py.mixer.music.load(musound)
    py.mixer.music.play(-1,0)

def soundstop():
    py.mixer.music.stop()

def fastchoose():
        status["foreground"] = 'green'
        time.sleep(0.5)
        people = int(human.get())
        xuanze = random.randrange(1,people+1)#这个地方一定要加一
        countbar['text']=xuanze
        filename = path + str(xuanze) + '.jpg'
        img1 = cv2.imread(filename)
        im1 = Image.fromarray(cv2.cvtColor(img1,cv2.COLOR_BGR2RGB))
        img[0] = ImageTk.PhotoImage(image = im1)
        photos.config(image=img[0])
        root.update_idletasks()
        status["foreground"] = 'red'

def statuscolorgreen ():
    t=threading.Thread(target=oneclass)
    t.start()
    soundstart()
    status["foreground"] = 'green'

def statuscolorred ():
     root.flag = False
     soundstop()
     status["foreground"] = 'red'
   
#########标题##########
biaoti = tk.Label(root, 
            text='幸运之神V4.0',    # 标签的文字
            font=('Arial', 48),     # 字体和字体大小(待改动）
            foreground='lightskyblue',  #这个颜色超好看，建议不要改
            width=15, height=2  # 标签长宽（待改动）
              )
biaoti.place(x=10, y=10, width=400, height=60)


##########菜单##########
menu0=Menu(root)#参数是父级控件


#文件菜单
file=Menu(menu0,tearoff=False)#定义不可拖移菜单名称
file.add_command(label= str('开始      Up'),
                 command = statuscolorgreen
                 )
file.add_command(label= str('停止      Down'),
                 command = statuscolorred
                 )
file.add_command(label= str('退出'),
                 command = exit
                 )

menu0.add_cascade(label='文件',menu=file)#在menu0中添加一个label为项目的级联菜单

#模式菜单
def changeto1():
    fastb.place_forget()
    startb.place(x=410, y=310, width=100, height=50)
    stopb.place(x=410, y=370, width=100, height=50)
    exitb.place(x=410, y=430, width=100, height=50)

def changeto2():
    startb.place_forget()
    stopb.place_forget()
    exitb.place_forget()
    fastb.place(x=410, y=310, width=100, height=150)
    
mode=Menu(menu0,tearoff=False)#定义不可拖移菜单名称

mode.add_command(label= str('单班抽签'),
                 command = changeto1
                 )
mode.add_command(label= str('瞬间抽签'),
                 command = changeto2
                 )
menu0.add_cascade(label='模式',menu=mode)#一级菜单名称

#图库菜单
def picture1():
      global path
      path = '.\\picture\\gallery1\\'

def picture2():
      global path
      path = '.\\picture\\gallery2\\'

def picture3():
      global path
      path = '.\\picture\\gallery3\\'

def picture4():
      global path
      path = '.\\picture\\gallery4\\'

def picture5():
      global path
      path = '.\\picture\\gallery5\\'

gallery=Menu(menu0,tearoff=False)#定义不可拖移菜单名称
gallery.add_command(label= str('原版图库'),
                    command = picture1
                    )
gallery.add_command(label= str('（2019级）高一三班专版'),
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
about.add_command(label=str('！！！捐赠！！！'),
                     command = juanzeng
                     )
menu0.add_cascade(label='关于',menu=about)
    

##########计数器##########
countbar = tk.Label(root,
                    bg='white',
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
                        command=fastchoose,
                        )
fastb.place(x=410, y=310, width=100, height=150)
fastb.place_forget()
#开始
    
startb = tk.Button(root,
                        text='开始',
                        font=('黑体', 20),
                        command=statuscolorgreen,
                        )
startb.place(x=410, y=310, width=100, height=50)

#停止     
stopb = tk.Button(root,
                        text='停止',
                        font=('黑体', 20),
                       command=statuscolorred
                        )
stopb.place(x=410, y=370, width=100, height=50)

#退出
exitb = tk.Button(root,
                        text='退出',
                        font=('黑体', 20),
                        command=exit
                        )
exitb.place(x=410, y=430, width=100, height=50)

##########状态灯##########
status = tk.Label(root,
                  text='◉',
                 font=('黑体', 80),
                  foreground='red',
                   )
status.place(x=410, y=80, width=100, height=100)



##########人数调整##########
human = StringVar()
human.set(32)
label_renshu = tk.Label(root,
                    text='人数',
                    font=('Arial', 12),
                    bd=10)
label_renshu.place(x=410, y=210, width=30, height=20)



dognumber = tk.Spinbox(root,
                       from_ = 1,
                       to = 5000,
                       textvariable = human,
                       increment = 1,
                       )
dognumber.place(x=440, y=210, width=70, height=20)


##########音效##########
#此模块无bug
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
soundeffectchoose.place(x=440, y=270, width=51, height=16)



###########作者##########
#此模块无bug
lord = tk.Label(root,
                    text='-本程序由伟大的李一田倾力制作-',
                    font=('Arial', 10),
                    bd=10)
lord.place(x=110, y=470, width=230, height=20)



#############图片###########
photos = tk.Label(root,
                    image = '',
                    bg='white',
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
        

#快捷键
def kaishi(event):
    statuscolorgreen()

def tingzhi(event):
    statuscolorred()

root.bind_all("<KeyPress-Up>", kaishi)
root.bind_all("<KeyPress-Down>", tingzhi)


root['menu']=menu0#窗口root的menu是menu0
root.mainloop()



