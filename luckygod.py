'''
-*-coding:UTF-8-*-
环境：python3.6.2_32bit
程序功能：幸运之神5.0--抽签助手
完成日期：2020年12月27日
本程序由伟大的李一田倾力制作
'''

'''
------------------------------------------------------------------
|☺幸运之神5.0--抽签助手                                      |-|口|X|
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


#我也不知道为什么要import这么多插件……
import random as 随机模块
from tkinter  import *
import pygame as 音效播放模块
import tkinter as 视窗模块
import tkinter.messagebox
import threading as 多线程模块
from PIL import Image, ImageTk
import cv2 as 图像处理模块
import time as 时间模块
import sys

#########初始化##########
窗体= 视窗模块.Tk()
窗体.geometry("520x490")#窗口大小
窗体.title('幸运之神V5.0--抽签助手')#标题名称
窗体.resizable(False,False)#窗口大小不能改变
窗体.iconbitmap('./main.ico')#窗口图标
窗体.flag = True
未处理图片 = [None]
路径 = '.\\picture\\gallery1\\'
人数 = []
#读取文本文档内容
with open(r'文字显示内容.txt', 'r', encoding='UTF-8') as 文本文档内容:
    文本文档数据 = 文本文档内容.read().splitlines()
文字框列表 = list(文本文档数据)
#生成人数列表初始值
人数.clear()
for i in range(1,34):
    人数.append(i)
###########################################################
#########################交互界面###########################
###########################################################
音效播放模块.mixer.init()
音效选择 = r'.\music\music1.mp3'

def 音效一():
    global 音效选择
    音效选择 = r'.\music\music1.mp3'

def 音效二():
    global 音效选择
    音效选择 = r'.\music\music2.mp3'

def 音效三():
    global 音效选择
    音效选择 = r'.\music\music3.mp3'

def 音效四():
    global 音效选择
    音效选择 = r'.\music\music4.mp3'

def 音效五():
    global 音效选择
    音效选择 = r'.\music\music5.mp3'

def 音效开始播放():
    global 音效选择
    音效播放模块.mixer.music.load(音效选择)
    音效播放模块.mixer.music.play(-1,0)

def 音效停止播放():
    音效播放模块.mixer.music.stop()

def 随机选择文字():
    global 文字框列表
    文字选择 = 随机模块.choice(文字框列表)
    文字显示框['text']=文字选择

def 快速抽签():
        随机选择文字()
        status["foreground"] = 'green'
        时间模块.sleep(0.1)
        快速抽签和单班抽签人数 = int(human.get())
        人数选择 = 随机模块.randrange(1,快速抽签和单班抽签人数+1)#这个地方一定要加一
        countbar['text']=人数选择
        路径名称 = 路径 + str(人数选择) + '.jpg'
        第一次处理后的图片 = 图像处理模块.imread(路径名称)
        第二次处理后的图片 = Image.fromarray(图像处理模块.cvtColor(第一次处理后的图片,图像处理模块.COLOR_BGR2RGB))
        未处理图片[0] = ImageTk.PhotoImage(image = 第二次处理后的图片)
        photos.config(image=未处理图片[0])
        窗体.update_idletasks()
        status["foreground"] = 'red'

def 开始单班抽签 ():
    多线程模式=多线程模块.Thread(target=单班抽签)
    多线程模式.start()
    音效开始播放()
    status["foreground"] = 'green'

def 结束单班抽签 ():
     窗体.flag = False
     音效停止播放()
     status["foreground"] = 'red'

def 无重开始控制():
    if len(set(人数))== 0:
        视窗模块.messagebox.showinfo("提示", "剩余人数为零，无法抽签，请重置人数数量！")
    else:
        a=多线程模块.Thread(target=无重复抽签)
        a.start()
        音效开始播放()
        status["foreground"] = 'green'

剩余人数 = 视窗模块.Label(窗体,
                text="剩余33人")
剩余人数.place(x=440, y=260, width=51, height=16)
剩余人数.place_forget()
def 无重结束控制 ():
     窗体.flag = False
     音效停止播放()
     status["foreground"] = 'red'
     人数选择 = int(随机模块.choice(人数))
     countbar['text']=人数选择
     路径名称 = 路径 + str(人数选择) + '.jpg'
     第一次处理后的图片 = 图像处理模块.imread(路径名称)
     第二次处理后的图片 = Image.fromarray(图像处理模块.cvtColor(第一次处理后的图片,图像处理模块.COLOR_BGR2RGB))
     未处理图片[0] = ImageTk.PhotoImage(image = 第二次处理后的图片)
     photos.config(image=未处理图片[0])
     窗体.update_idletasks()
     人数.remove(人数选择)
     剩余人数['text']="剩余"+str(len(set(人数)))+"人"
     

#########标题##########
biaoti = 视窗模块.Label(窗体, 
            text='幸运之神V5.0',    # 标签的文字
            font=('Arial', 48),     # 字体和字体大小(待改动）
            foreground='lightskyblue',  #这个颜色超好看，建议不要改
            width=15, height=2  # 标签长宽（待改动）
              )
biaoti.place(x=10, y=10, width=400, height=60)


##########菜单##########
menu0=Menu(窗体)#参数是父级控件


#文件菜单
file=Menu(menu0,tearoff=False)#定义不可拖移菜单名称
file.add_command(label= str('开始      Up'),
                 command = 开始单班抽签
                 )
file.add_command(label= str('停止      Down'),
                 command = 结束单班抽签
                 )
file.add_command(label= str('退出'),
                 command = sys.exit
                 )

menu0.add_cascade(label='文件',menu=file)#在menu0中添加一个label为项目的级联菜单

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
mode.add_separator()

文字显示框 = 视窗模块.Message(窗体,
                    anchor='s',
                    font=('黑体', 35),
                    bd=10,
                    text = '',
                    )
文字显示框.place(x=525, y=10, width=250, height=455)


def 显示文字框():
    窗体.update()
    if 窗体.winfo_width() == 520:
        窗体.geometry("780x470")
    elif 窗体.winfo_width() == 780:
        窗体.geometry("520x470")

mode.add_command(label= str('文字显示开关'),
                 command = 显示文字框 
                 )
menu0.add_cascade(label='模式',menu=mode)#一级菜单名称

#图库菜单
def picture1():
      global 路径
      路径 = '.\\picture\\gallery1\\'

def picture2():
      global 路径
      路径 = '.\\picture\\gallery2\\'

def picture3():
      global 路径
      路径 = '.\\picture\\gallery3\\'

def picture4():
      global 路径
      路径 = '.\\picture\\gallery4\\'

def picture5():
      global 路径
      路径 = '.\\picture\\gallery5\\'

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
                 command = 音效一
                 )
soundeffects.add_command(label= str('音效2'),
                 command = 音效二
                 )
soundeffects.add_command(label= str('音效3'),
                 command = 音效三
                 )
soundeffects.add_command(label= str('音效4'),
                 command = 音效四
                 )
soundeffects.add_command(label= str('音效5'),
                 command = 音效五
                 )

menu0.add_cascade(label='音效',menu=soundeffects)

#关于菜单
def 关于():
    视窗模块.messagebox.showinfo('关于作者','本程序由伟大的李一田倾力制作')
about=Menu(menu0,tearoff=False)#定义不可拖移菜单名称
about.add_command(label=str('关于作者'),
                     command = 关于
                     )
menu0.add_cascade(label='关于',menu=about)
    

##########计数器##########
countbar = 视窗模块.Label(窗体,
    #                bg='white',
                    anchor='se',
                    font=('黑体', 35),
                    bd=10,
                    text = '0',
                    )
countbar.place(x=410, y=10, width=100, height=60)




##########按钮##########
#抽签
fastb = 视窗模块.Button(窗体,
                        text='抽签',
                        font=('黑体', 20),
                        command=快速抽签,
                        )
#开始
    
startb = 视窗模块.Button(窗体,
                        text='开始',
                        font=('黑体', 20),
                        command=开始单班抽签,
                        )
startb.place(x=410, y=295, width=100, height=50)

#停止     
stopb = 视窗模块.Button(窗体,
                        text='停止',
                        font=('黑体', 20),
                       command=结束单班抽签
                        )
stopb.place(x=410, y=355, width=100, height=50)

#退出
exitb = 视窗模块.Button(窗体,
                        text='退出',
                        font=('黑体', 20),
                        command=sys.exit
                        )
exitb.place(x=410, y=415, width=100, height=50)


norestart = 视窗模块.Button(窗体,
                        text='开始',
                        font=('黑体', 20),
                        command=无重开始控制,
                        )
startb.place(x=410, y=295, width=100, height=50)
    
norestop = 视窗模块.Button(窗体,
                        text='停止',
                        font=('黑体', 20),
                       command=无重结束控制
                        )
stopb.place(x=410, y=355, width=100, height=50)


norestart.place_forget()
##########状态灯##########
status = 视窗模块.Label(窗体,
                  text='◉',
                 font=('黑体', 80),
                  foreground='red',
                   )
status.place(x=410, y=80, width=100, height=100)


norestart.place_forget()



##########人数调整##########
human = StringVar()
human.set(33)
label_renshu = 视窗模块.Label(窗体,
                    text='人数',
                    font=('Arial', 12),
                    bd=10)
label_renshu.place(x=410, y=210, width=30, height=20)

def 调整人数():
    人数.clear()
    for i in range(1,int(human.get())+1):
        人数.append(i)
    剩余人数['text']="剩余"+str(len(set(人数)))+"人"

resetb = 视窗模块.Button(窗体,
                        text='重置',
                        font=('黑体', 20),
                        command=调整人数
                        )

dognumber = 视窗模块.Spinbox(窗体,
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
    音效播放模块.mixer.music.set_volume(1.0)
else:
    音效播放模块.mixer.music.set_volume(0)
    
def yinxiaokaiguan():
    if var.get() == 1:
        音效播放模块.mixer.music.set_volume(1.0)
    else:
        音效播放模块.mixer.music.set_volume(0)


soundeffectchoose = 视窗模块.Checkbutton(窗体,
                                   text='音效',
                                   variable=var,
                                   command=yinxiaokaiguan
                                   )
soundeffectchoose.place(x=440, y=240, width=51, height=16)

#############图片###########
photos = 视窗模块.Label(窗体,
                    image = '',
#                    bg='white',
                    bd=10)
photos.place(x=10, y=75, width=390, height=390)


###########################################################
#########################主程序功能#########################
###########################################################


##########单班抽签##########
def 单班抽签 ():
     窗体.flag=True
     global 路径
     while 窗体.flag:
        随机选择文字()
        快速抽签和单班抽签人数 = int(human.get())
        人数选择 = 随机模块.randrange(1,快速抽签和单班抽签人数+1)#这个地方一定要加一
        countbar['text']=人数选择
        路径名称 = 路径 + str(人数选择) + '.jpg'
        第一次处理后的图片 = 图像处理模块.imread(路径名称)
        第二次处理后的图片 = Image.fromarray(图像处理模块.cvtColor(第一次处理后的图片,图像处理模块.COLOR_BGR2RGB))
        未处理图片[0] = ImageTk.PhotoImage(image = 第二次处理后的图片)
        photos.config(image=未处理图片[0])
        窗体.update_idletasks()

##########无重复抽签############
def 无重复抽签():
    窗体.flag=True
    global 路径
    while 窗体.flag:
        随机选择文字()
        人数选择 = int(随机模块.choice(人数))
        countbar['text']=人数选择
        路径名称 = 路径 + str(人数选择) + '.jpg'
        第一次处理后的图片 = 图像处理模块.imread(路径名称)
        第二次处理后的图片 = Image.fromarray(图像处理模块.cvtColor(第一次处理后的图片,图像处理模块.COLOR_BGR2RGB))
        未处理图片[0] = ImageTk.PhotoImage(image = 第二次处理后的图片)
        photos.config(image=未处理图片[0])
        窗体.update_idletasks()

窗体['menu']=menu0#窗口窗体的menu是menu0
窗体.mainloop()



