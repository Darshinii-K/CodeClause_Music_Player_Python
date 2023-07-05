from tkinter import *
from PIL import Image,ImageTk
import os
from pygame import mixer

col1="#ffffff" #white
col2="#9897A9" #purple
col3="#333333" #black
col4= "#CFC7F8" #light purple

#tkinter window
window= Tk()
window.title("")
window.geometry('325x280')
window.configure(background=col1)
window.resizable(width=FALSE,height=FALSE)


#functions for buttons
def play_music():
    running = listbox.get(ACTIVE)
    running_song['text']= running
    mixer.music.load(running)
    mixer.music.play()
def pause_music():
    mixer.music.pause()

def continue_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

def next_music():
    playing = running_song['text']
    index=songs.index(playing)
    new_index=index+1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)

    show()

    listbox.select_set(new_index)
    running_song['text'] = playing

def prev_music():
    playing = running_song['text']
    index=songs.index(playing)
    new_index=index-1
    playing=songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0,END)

    show()


#frames
left_frame = Frame(window,width=150,height=150,bg=col1)
left_frame.grid(row=0,column=1,padx=1,pady=1)

right_frame=Frame(window,width=250,height=150,bg=col3)
right_frame.grid(row=0,column=0,padx=0)

down_frame=Frame(window,width=400,height=100,bg=col2)
down_frame.grid(row=1,column=0,columnspan=3,padx=0,pady=1)

#images
#defining logo
img_1=Image.open("C:\\Users\\darsh\\OneDrive\\Desktop\\Music_system\\logo.png")
img_1=img_1.resize((75,75))
img_1=ImageTk.PhotoImage(img_1)
app_image=Label(left_frame,height=130,image=img_1,padx=10,bg=col1)
app_image.place(x=10,y=15)


#buttons
#all the buttons are defined
#previous button definition
img_2=Image.open("C:\\Users\\darsh\\OneDrive\\Desktop\\Music_system\\rewind.jpeg")
img_2=img_2.resize((30,30))
img_2=ImageTk.PhotoImage(img_2)
rewind_button=Button(down_frame,height=40,width=40,image=img_2,padx=10,bg=col1,font=("Ivy 10"),command=prev_music)
rewind_button.place(x=30,y=30)

#play_button definition
img_3=Image.open("C:\\Users\\darsh\\OneDrive\\Desktop\\Music_system\\play.jpg")
img_3=img_3.resize((30,30))
img_3=ImageTk.PhotoImage(img_3)
play_button=Button(down_frame,height=40,width=40,image=img_3,padx=10,bg=col1,font=("Ivy 10"),command=play_music)
play_button.place(x=72,y=30)

#next_button definition
img_4=Image.open(r"C:\Users\darsh\OneDrive\Desktop\Music_system\forward.jpeg")
img_4=img_4.resize((30,30))
img_4=ImageTk.PhotoImage(img_4)
forward_button=Button(down_frame,height=40,width=40,image=img_4,padx=10,bg=col1,font=("Ivy 10"),command=next_music)
forward_button.place(x=114,y=30)

#pause_button definition
img_5=Image.open(r"C:\Users\darsh\OneDrive\Desktop\Music_system\pause.jpeg")
img_5=img_5.resize((30,30))
img_5=ImageTk.PhotoImage(img_5)
pause_button=Button(down_frame,height=40,width=40,image=img_5,padx=10,bg=col1,font=("Ivy 10"),command=pause_music)
pause_button.place(x=156,y=30)

#stop_button definition
img_6=Image.open(r"C:\Users\darsh\OneDrive\Desktop\Music_system\stop button.png")
img_6=img_6.resize((30,30))
img_6=ImageTk.PhotoImage(img_6)
stop_button=Button(down_frame,height=40,width=40,image=img_6,padx=10,bg=col1,font=("Ivy 10"),command=stop_music)
stop_button.place(x=198,y=30)

#continue_button definition
img_7=Image.open(r"C:\Users\darsh\OneDrive\Desktop\Music_system\continue.png")
img_7=img_7.resize((30,30))
img_7=ImageTk.PhotoImage(img_7)
cont_button=Button(down_frame,height=40,width=40,image=img_7,padx=10,bg=col1,font=("Ivy 10"),command=continue_music)
cont_button.place(x=240,y=30)

#list box
listbox=Listbox(right_frame,selectmode=SINGLE,font=("Arial 9 bold"),width=22,bg=col3,fg=col1)
listbox.grid(row=0,column=0)

w=Scrollbar(right_frame)
w.grid(row=0,column=1)


listbox.config(yscrollcommand=w.set)
w.config(command=listbox.yview)

running_song=Label(down_frame,text="Choose a Song",font=("Algerian"),width=44,height=1,padx=10,bg=col1,fg=col3,anchor=NW)
running_song.place(x=0,y=1)
os.chdir("C:\\Users\\darsh\\OneDrive\\Desktop\\Music_system\\songs")
songs=os.listdir()

#events
#showing the songs list in the listbox
def show():
    for i in songs:
        listbox.insert(END,i)
show()

mixer.init()
music_state= StringVar()
music_state.set("Choose one!")

window.mainloop()
