import os
import pygame
from tkinter import Tk, Button, filedialog

# Initialize pygame mixer
pygame.mixer.init()

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    if file_path:
        pygame.mixer.music.load(file_path)
        play_music()

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

# Create a simple GUI
root = Tk()
root.title("Minimal Music Player")

load_button = Button(root, text="Load Music", command=load_file)
load_button.pack(pady=20)

play_button = Button(root, text="Play", command=play_music)
play_button.pack(pady=20)

stop_button = Button(root, text="Stop", command=stop_music)
stop_button.pack(pady=20)

root.mainloop()

