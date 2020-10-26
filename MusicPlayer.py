from tkinter import *
from tkinter.filedialog import askopenfilename
from pygame import mixer,mixer_music
from PIL import Image,ImageTk
import random
import os
from functools import partial
import pygame
from  tkinter import messagebox
from tkinter import ttk
from tkinter import font

def openfile():
    # global i
    # global music_list
    filename=askopenfilename(defaultextension=".mp3",filetypes=[("Allfiles","*.*"),("musicfiles","*.mp3")])
    print(filename)
    if i==0:
        music_list.insert(i,filename)
    else:
        music_list.insert(i+1,filename)
    if filename ==" ":
        filename =NONE
    else:
        listbox.insert(END,filename)
def MakeFalse():
    global shuffle,playall
    shuffle =False
    playall=False
    return
def play():
    pygame.mixer.init()
    # global music_list
    global playall
    # global shuffle
    global x
    listlen=len(music_list)-1
    if playall == True:
        try:
            x=0
            statusbar['text']= music_list[x]
            pygame.mixer_music.load(music_list[x])
            pygame.mixer_music.play(0)
            pygame.mixer_music.set_volume(1.0)
            playall_loop()
        except Exception as e:
            pass   

    elif shuffle ==True:
        try:
            statusbar['text']=music_list[random.randrange(0,listlen)]
            pygame.mixer_music.load(music_list[random.randrange(0,listlen)])
            pygame.mixer_music.play(0)
            pygame.mixer_music.set_volume(1.0)
            shuffle_loop()
        except Exception as e:
            pass
    else :
        try:
            fromlist=listbox.get(listbox.curselection())
            statusbar['text']= fromlist
            pygame.mixer_music.load(fromlist)
            pygame.mixer_music.play(0)
            pygame.mixer_music.set_volume(1.0)
        except Exception as e:
            messagebox.showinfo("song ","Select a Song")
    MakeFalse()
    return

#for playall     
def playall_loop():
    global x
    try:
        if int(pygame.mixer_music.get_pos()) ==-1:
            x=x+1
            statusbar['text']= music_list[x]
            pygame.mixer_music.load(music_list[x])
            pygame.mixer_music.play(0)
            pygame.mixer_music.set_volume(1.0)
        root.after(1,playall_loop)
    except Exception as e:
        # mixer_music.stop()
        statusbar['text']="Playlist Completed"         

#to play next
def next():
    try:
        pygame.mixer_music.stop()
    except Exception as e:
        pass
    return
def prev(value):
    #print(value)
    #x=x-1
    pass
#for shuffle playback
def shuffle_loop():
    global y
    try:
        listlen=len(music_list)-1
        if int(pygame.mixer_music.get_pos()) ==-1:
            statusbar['text']= music_list[random.randrange(0,listlen)]
            pygame.mixer_music.load(music_list[random.randrange(0,listlen)])
            pygame.mixer_music.play(0)
            pygame.mixer_music.set_volume(1.0)
        root.after(1,shuffle_loop)
    except Exception as e:
        statusbar['text']="Music Stopped"

#To enable shuffle
def shuffle_all():
    global shuffle
    shuffle=True
    return
#To enable playall
def play_all():
    global playall
    playall=True
    return 
    
def stop():
    try:
        pygame.mixer.quit() 
        statusbar['text']="music stoped"
    except Exception as e:
        pass
    return
def pause():
    try:
        pygame.mixer_music.pause()
        statusbar['text']="music paused"
    except Exception as e:
        pass
    return
def rewind():
    try:
        pygame.mixer_music.rewind()
    except Exception as e:
        pass
    return
def soundon(i):
    # global value
    # value=value+i
    # if value <= 1.0:
    #     sound=value/100
    try:
        mixer_music.set_volume(5.0)
    except Exception as e:
        pass
    # else:
    #     print("Playing at meximum volume")
def soundoff():
    try:
        mixer_music.set_volume(0.0)
    except Exception as e:
        pass
#to delete selected song 
def delete():
    try:
        selected_song = listbox.curselection()
        print(selected_song,selected_song[0])
        selected_song = int(selected_song[0])
        listbox.delete(selected_song)
        deleted=music_list.pop(selected_song)
        satusbar['text']="music deleted"
    except Exception as e:
        pass
def exits():
    root.destroy()
if __name__ == "__main__":
    value=0
    playall=False
    shuffle=False
    x,y,i=0,0,0
    music_list=[]
    root=Tk()
    root.title("MusiPlayer")
    root.geometry("800x600")
    #root.iconbitmap("H:/icon.png")
    filename=NONE
    # putting a background image
    # img=Image.open("H:/background.jpg")
    # img=img.resize((1000,1150))
    # background=ImageTk.PhotoImage(img)
    # canvas = Canvas(root,width = 500,height = 595)
    # canvas.place(x=295,y=0)
    # canvas.create_image(20, 20,image=background)
    
    #adding status bar
    statusbar =Label(root, text="Welcome",font='Times 10 italic',width=70,justify=LEFT)
    statusbar.pack(side=BOTTOM)
    statusbar.place(x=300,y=0)
    #adding menu bar
    menubar = Menu(root) 
    file=Menu(menubar,tearoff=False)
    menubar.add_cascade(label="File",menu=file)
    file.add_command(label="Open",command=openfile)
    file.add_command(label="Exit",command=exits)
    root.config(menu=menubar)
     #listbox right
    listbox=Listbox(root,width=50,height=100,bg="orange",highlightcolor="white")
    listbox.place(x=20,y=0)
    #scrollbar right
    scrollbar=Scrollbar(root)
    scrollbar.pack(side=LEFT,fill=Y)
    #scrollbar.configure(listbox.yview)
    # listbox.configure(scrollbar.set)
     # #adding playicon ,stopicon
    play_icon=ImageTk.PhotoImage(Image.open(r"source_images\play.png"))
    stop_icon=ImageTk.PhotoImage(Image.open(r"source_images\stop.png"))
    pause_icon=ImageTk.PhotoImage(Image.open(r"source_images\pause.png"))
    img=Image.open(r'source_images\rewind.png')
    img=img.resize((64,64))
    rewind_icon=ImageTk.PhotoImage(img)
    img=Image.open(r"source_images\next.png")
    img=img.resize((150,150))
    next_icon_left=ImageTk.PhotoImage(img)
    img=Image.open(r"source_images\next_right.png")
    img=img.resize((150,150))
    next_icon_right=ImageTk.PhotoImage(img)
    img=Image.open(r"source_images\volumeon.png")
    img=img.resize((30,30))
    volumeon=ImageTk.PhotoImage(img)
    img=Image.open(r"source_images\volumeoff.png")
    img=img.resize((30,30))
    volumeoff=ImageTk.PhotoImage(img)
    #adding playbutton stop button
    play_button=Button(root,image=play_icon,command=play)
    play_button.place(x=400,y=100)
    stop_button=Button(root,image=stop_icon,command=stop)
    stop_button.place(x=500,y=100)
    pause_button=Button(root,image=pause_icon,command=pause)
    pause_button.place(x=600,y=100)
    rewind_button=Button(root,image=rewind_icon,command=rewind)
    rewind_button.place(x=700,y=100)
    shuffle_button=Button(root,text="shuffle",command=shuffle_all)
    shuffle_button.place(x=450,y=400)
    playall_button=Button(root,text="playall",command=play_all)
    playall_button.place(x=550,y=400)
    delete_button=Button(root,text="delete",command=delete)
    delete_button.place(x=650,y=400)
    next_button_left=Button(root,image=next_icon_left,command=partial(prev))
    next_button_left.place(x=400,y=200)
    next_button_right=Button(root,image=next_icon_right,command=partial(next))
    next_button_right.place(x=600,y=200)
    on_button=Button(root,image=volumeon,command=partial(soundon,10))
    on_button.place(x=450,y=450)
    off_button=Button(root,image=volumeoff,command=soundoff)
    off_button.place(x=550,y=450)
    #adding playlabel stoplabel
    play_label=Label(root,text="play",font=4)
    play_label.place(x=400,y=40)
    stop_label=Label(root,text="stop",font=4)
    stop_label.place(x=500,y=40)
    pause_label=Label(root,text="pause",font=4)
    pause_label.place(x=600,y=40)
    rewind_label=Label(root,text="rewind",font=4)
    rewind_label.place(x=700,y=40)
    root.mainloop()
    

