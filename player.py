import os
import pygame
import tkinter
from tkinter.ttk import Progressbar
from tkinter import ttk 
from tkinter.filedialog import askdirectory
from tkinter import *
from datetime import datetime
from datetime import timedelta
from mutagen.mp3 import MP3
root = Tk()
list_songs = []
count = 0
global next_b6
global progressbar,prog_bar_end,prog_bar_start
#tot_len = 0  
def directory():
    d = askdirectory()
    os.chdir(d)
    for files in os.listdir(d):
        if(files.endswith(".mp3")):
           list_songs.append(files)
    
    pygame.mixer.init()
    pygame.mixer.music.load(list_songs[count])
    #pygame.mixer.music.play()
    list_songs.reverse()
    for i in list_songs:
        lbox.insert(0,i)

def next_b():
    global count
    count = count + 1
    pygame.mixer.music.load(list_songs[count])
    a = pygame.mixer.music.play()
    song_str.set(list_songs[count])
    audio = MP3(list_songs[count])
    tot_len = int(audio.info.length)
    
    progressbar['maximum'] = tot_len
    prog_bar_end.configure(text='{}'.format(str(timedelta(seconds=tot_len))))
    prog_bar_1()
    progressbar['value'] = 0.00
    

def prog_bar_1():
    #curr_len = 0.00
    curr_len = pygame.mixer.music.get_pos()//1000
    progressbar['value'] = curr_len
    prog_bar_start.configure(text='{}'.format(str(timedelta(seconds=curr_len))))
    progressbar.after(2,prog_bar_1)
    
        
def prev_b():
    global count
    count = count - 1
    pygame.mixer.music.load(list_songs[count])
    pygame.mixer.music.play()
    song_str.set(list_songs[count])
    audio = MP3(list_songs[count])
    tot_len = int(audio.info.length)
    prog_bar_end.configure(text='{}'.format(str(timedelta(seconds=tot_len))))
    prog_bar_1()
def play_b():
    pygame.mixer.music.unpause()
def playstop_b():
    pygame.mixer.music.pause()
    
    
    
l1 = Label(root,text="Fimoloop",bg='black',fg='white',font='Terminal 40')
l1.grid(row=0,column=1,pady=20,padx=170)


lbox = Listbox(root,width=30,height=25,bg='slate gray',fg='white',font='helvetica 10')
lbox.grid(row=1,column=0,pady=10,padx=10)

b1 = Button(text="Select Audio Track",width=19,bg='slate gray',fg='white',font='helvetica 15',command=directory)
b1.grid(row=2,column=0,pady=10)


next_b = Button(root,text="Play",command=next_b,width=25,height=1,fg='white',bg='orange')
next_b.grid(row=3,column=0)

prev_b = Button(root,text="Previous",command=prev_b,width=25,fg='white',bg='orange')
prev_b.grid(row=4,column=0)

playstop_b = Button(root,text="Stop",command=playstop_b,width=25,fg='white',bg='orange')
playstop_b.grid(row=5,column=0)

play_b = Button(root,text="Resume",command=play_b,width=25,height=1,fg='white',bg='orange')
play_b.grid(row=6,column=0)


song_str = StringVar()
song_name = Label(root,textvariable=song_str,bg='black',fg='white',font='helvetica 15',width=40)
song_name.grid(row=7,column=1)

made_with_love = Label(root,text="Developed By: Nishant Tiwari",width=25,fg='white',bg='black',font='helvetica 11')
made_with_love.grid(row=8,column=0)

prog_bar = Label(root,text='',bg='grey')
prog_bar.grid(row=8,column=1)

prog_bar_start = Label(prog_bar,text='0:00:00',bg='grey',fg='white')
prog_bar_start.grid(row=8,column=1)

s = ttk.Style()
s.theme_use('clam')
s.configure("Horizontal.TProgressbar", foreground='blue', background='blue')

progressbar = Progressbar(prog_bar,style="Horizontal.TProgressbar",orient=HORIZONTAL,mode='determinate',value=0)
progressbar.grid(row=8,column=2,ipadx=200)

prog_bar_end = Label(prog_bar,text='0:00:00',bg='grey',fg='white')
prog_bar_end.grid(row=8,column=3)


#root.config(bg="green")
root.title("Music Player")
root.geometry('900x780+200+50')
root.resizable(0,0)
root.configure(bg='black')
root.mainloop()
