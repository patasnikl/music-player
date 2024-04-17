""" Build a working MP3 Music Player """

import pygame
from pygame import mixer
import tkinter as tk
from tkinter import filedialog

back = input("Enter a background color: ")
back2 = input("Enter a second background color: ")
text = input("Enter a color for the text: ")

player = tk.Tk()
player.title("Lauren's Music Player")
player.geometry("500x400")
player.config(bg = back)

#initilize Pygame Mixer which allows us to play audio
pygame.mixer.init()

def add_songs():
    """ Set working directory and add songs to song list box
    """
    new_song = filedialog.askopenfilenames(initialdir="music_files", title="Choose a song",
     filetypes=(("mp3 Files", "*.mp3"),))
    for i in new_song:
        i=i.replace("/Users/laurenpatasnik/Documents/INST326/Final_Project/music_files/", "")
        i=i.replace(".mp3", "")
        song_list.insert(tk.END, i)

def play_song():
    """ Play current song
    """
    new_song = song_list.get(tk.ACTIVE)
    new_song = f'/Users/laurenpatasnik/Documents/INST326/Final_Project/music_files/{new_song}.mp3'
    mixer.music.load(new_song)
    mixer.music.play()

def pause_song():
    """ Pause current song
    """
    mixer.music.pause()

def stop_song():
    """ Pause current song
    """
    mixer.music.stop()
    song_list.selection_clear(tk.ACTIVE)

def prev_song():
    """ Go to previous song in song list
    """
    prev_one = song_list.curselection()
    prev_one = prev_one[0]-1

    x = song_list.size()
    if prev_one == -1:
        prev_one = prev_one + x

    current_song1 = song_list.get(prev_one)
    current_song1 = f'/Users/laurenpatasnik/Documents/INST326/Final_Project/music_files/{current_song1}.mp3'
    mixer.music.load(current_song1)
    mixer.music.play()

    #move highlighted bar
    song_list.selection_clear(0,tk.END)
    song_list.activate(prev_one)
    song_list.selection_set(prev_one)

def next_song():
    """ Go to next song in song list
    """
    next_one = song_list.curselection()
    next_one = next_one[0]+1

    y = song_list.size()
    if next_one == y:
        next_one = next_one - y

    current_song2 = song_list.get(next_one)
    current_song2 = f'/Users/laurenpatasnik/Documents/INST326/Final_Project/music_files/{current_song2}.mp3'
    mixer.music.load(current_song2)
    mixer.music.play()

    song_list.selection_clear(0,tk.END)
    song_list.activate(next_one)
    song_list.selection_set(next_one)

#create menu
menu_bar = tk.Menu(player)
player.config(menu=menu_bar)

#add song selection created in top menu bar
song_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Song Selection", menu=song_menu)
song_menu.add_command(label="Add Songs to Playlist", command=add_songs)

#create list box that will contain songs
song_list = tk.Listbox(player, bg=back2, fg=text, width=60, height=18)
song_list.pack()

#define control buttons
previous_btn_img = tk.PhotoImage(file ='previous_btn.png')
forward_btn_img = tk.PhotoImage(file ='forward_btn.png')
pause_btn_img = tk.PhotoImage(file ='pause_btn.png')
play_btn_img = tk.PhotoImage(file ='play_btn.png')
stop_btn_img = tk.PhotoImage(file ='stop_btn.png')

#organizes the layout of the control buttons
control_frame = tk.Frame(player)
control_frame.pack()

#create control buttons
previous_btn = tk.Button(control_frame, image=previous_btn_img, borderwidth=0, command=prev_song)
forward_btn = tk.Button(control_frame, image=forward_btn_img, borderwidth=0, command=next_song)
pause_btn = tk.Button(control_frame, image=pause_btn_img, borderwidth=0, command=pause_song)
play_btn = tk.Button(control_frame, image=play_btn_img, borderwidth=0, command=play_song)
stop_btn = tk.Button(control_frame, image=stop_btn_img, borderwidth=0, command=stop_song)

previous_btn.grid(row=0, column=0)
forward_btn.grid(row=0, column=1)
pause_btn.grid(row=0, column=2)
play_btn.grid(row=0, column=3)
stop_btn.grid(row=0, column=4)

player.mainloop()

