# -*- coding: utf-8 -*-

import cv2
import math
import os
import numpy as np
import pygame
import events
from tkinter.filedialog import askdirectory
from tkinter import *
#import PIL.Image

root=Tk()
frame = Frame(root, bg='orange')
frame.pack()

songlist = []
index=0
v = StringVar()
songname=""
flag=0

label=Label(frame,text="Music Player")
label.pack()

songlist.reverse()

listbox=Listbox(frame)

songlabel= Label(frame,textvariable=v)
 
def nextsong(event):
    global index
    if(index==(len(songlist))-1):
        index=0
    else:
        index+=1
    pygame.mixer.music.load(songlist[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    if(index==0):
        index=len(songlist)-1
    else:
        index-=1
    pygame.mixer.music.load(songlist[index])
    pygame.mixer.music.play()
    updatelabel()

def playsong2(event):
    global flag
    if(flag==1):
        flag=0
        pygame.mixer.music.unpause()
    else:    
        pygame.mixer.music.load(songlist[index])
        pygame.mixer.music.play()
        updatelabel()
        
def stopsong2(event):
    pygame.mixer.music.stop()

def pausesong2(event):
    global flag
    if(flag==0):
        pygame.mixer.music.pause()
        flag=1

def volumeup(event):
    x=pygame.mixer.music.get_volume()
    if(x>=1.0):
        print("Full Volume")
    else:
        x+=0.1;
        pygame.mixer.music.set_volume(x)

def volumedown(event):
    x=pygame.mixer.music.get_volume()
    if(x<=0.1):
        print("Current volume is minimum")
    else:
        x-=0.1;
        pygame.mixer.music.set_volume(x)
    
def playsong():
    global flag
    if(flag==1):
        flag=0
        pygame.mixer.music.unpause()
    else:    
        pygame.mixer.music.load(songlist[index])
        pygame.mixer.music.play()
        updatelabel()

def updatelabel():
    global index
    global songname
    v.set(songlist[index])
    return songname
    
def dir_chooser():
    dir=askdirectory()
    os.chdir(dir)
    for files in os.listdir(dir):
        if files.endswith(".mp3"):
            songlist.append(files)

    pygame.mixer.init()
    pygame.mixer.music.load(songlist[0])
    for items in songlist:
        listbox.insert(0,items)


listbox.pack()

songlabel.pack()

nextbutton=Button(frame,text="Next Song", activebackground='grey')
nextbutton.pack(side=LEFT)

prevbutton=Button(frame,text="Previous Song", activebackground='grey')
prevbutton.pack(side=LEFT)

playbutton=Button(frame,text="Play Song", activebackground='grey')
playbutton.pack(side=LEFT)

pausebutton=Button(frame,text="Pause Song", activebackground='grey')
pausebutton.pack(side=LEFT)

stopbutton=Button(frame,text="Stop Song", activebackground='grey')
stopbutton.pack(side=LEFT)

volumeupbutton=Button(frame,text="Volume up", activebackground='grey')
volumeupbutton.pack(side=LEFT)

volumedownbutton=Button(frame,text="Volume down", activebackground='grey')
volumedownbutton.pack(side=LEFT)

nextbutton.bind("<Button-1>",nextsong)
prevbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong2)
playbutton.bind("<Button-1>",playsong2)
pausebutton.bind("<Button-1>",pausesong2)    
volumeupbutton.bind("<Button-1>",volumeup)
volumedownbutton.bind("<Button-1>",volumedown)

try:
    dir_chooser()
    playsong()
    root.mainloop()
except KeyboardInterrupt:	# to stop playing, press "ctrl-c"
    pygame.quit()
    root.destroy()
    print("\nTerminated")