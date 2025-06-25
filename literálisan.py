import pygame
import tkinter as tk
from tkinter import simpledialog

pygame.mixer.init()

def play_sound(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

root = tk.Tk()
root.withdraw()  # Hide the tkinter root window

be = True
while be:
    valasz = simpledialog.askinteger("Kinyilatkoztatás", "Írd be a számot (0–31):")
    if valasz is None:
        break
    if valasz == 0:
        play_sound("kilepo.mp3")
        print("A program leáll")
        be = False
    elif valasz == 1:
        play_sound("testveremsz.mp3")
    elif valasz == 2:
        play_sound(r'csao papikam.mp3')
    elif valasz == 3:
        play_sound(r'1.5 honap.mp3')
    elif valasz == 4:
        play_sound(r'7_24.mp3')
    elif valasz == 5:
        play_sound(r'amugy... ja.mp3')
    elif valasz == 6:
        play_sound(r'annyit drogoztunk.mp3')
    elif valasz == 7:
        play_sound(r'baszni is szeretek.mp3')
    elif valasz == 8:
        play_sound(r'bazdmeeg.mp3')
    elif valasz == 9:
        play_sound(r'bulizok baszok.mp3')
    elif valasz == 10:
        play_sound(r'C1.mp3')
    elif valasz == 11:
        play_sound(r'catchy.mp3')
    elif valasz == 12:
        play_sound(r'csibesz ver.mp3')
    if valasz == 13:
        play_sound(r"drog driller.mp3")
    elif valasz == 14:
        play_sound(r'fajdalom.mp3')
    elif valasz == 15:
        play_sound(r'fenegyerek.mp3')
    elif valasz == 16:
        play_sound(r'frontin....mp3')
    elif valasz == 17:
        play_sound(r'hu cigany.mp3')
    elif valasz == 18:
        play_sound(r'hugy szar.mp3')
    elif valasz == 19:
        play_sound(r'hulyek vagyunk.mp3')
    elif valasz == 20:
        play_sound(r'KDT.mp3')
    elif valasz == 21:
        play_sound(r'literalisan csokynak pl a csaki.mp3')
    elif valasz == 22:
        play_sound(r'mindenki kis pancser.mp3')
    elif valasz == 23:
        play_sound(r'nem... igen.mp3')
    elif valasz == 24:
        play_sound(r'paprikaspre.mp3')
    elif valasz == 25:
        play_sound(r'roxtar.mp3')
    elif valasz == 26:
        play_sound(r'roxtar2.mp3')
    elif valasz == 27:
        play_sound(r'szinpad baszas.mp3')
    elif valasz == 28:
        play_sound(r'szuleiddel elsz.mp3')
    elif valasz == 29:
        play_sound(r'tovig.mp3')
    elif valasz == 30:
        play_sound(r'uuuuuu.mp3')
    elif valasz == 31:
        play_sound(r'roxtar.mp3')
        play_sound(r'szuleiddel elsz.mp3')
    elif valasz == 0:
        be = False
        play_sound(r'kilepo.mp3')
        print('A program leáll')
    else:
        print('kurva anyád')
