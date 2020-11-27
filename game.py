#--------Modulse
import random
import pygame
import pygame.mixer 
from pygame import *
from pygame.locals import*
import time
import datetime
from configparser import ConfigParser
#import sys
import logging
import json
import webbrowser
logging.basicConfig(filename="files/game.log", level=logging.INFO)
open("files/game.log","w+")
logging.info("")
#--------about
build_game = ("1.1")
build_engine = ("1.1.0")
code_name = ("Podiezd")
date_build = ("22.11.2020")
#------debug shit
logging.info("[Build: " + build_game + "]\n[Build Engine: " + build_engine + "] \n[Name project: " + code_name + "] \n[Date compile project: " + date_build + "]")
print ("[Build: " + build_game + "]\n[Build Engine: " + build_engine + "] \n[Name project: " + code_name + "] \n[Date compile project: " + date_build + "]")
#---------icon
icon =pygame.image.load('icon.png')
#-----
W = 970  # ширина экрана 970
H = 620 # высота экрана 620
print(time.strftime("%Y-%m-%d-%H.%M.%S") +"[initialization loading...]")
logging.info(time.strftime("%Y-%m-%d-%H.%M.%S") +"[initialization loading...]")

pygame.init()
pygame.mixer.pre_init()
pygame.mixer.init()
#pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.display.set_caption("Подъезд")
screen=pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
pygame.display.set_icon(icon)
config = ConfigParser()
config.read("files\config.ini")
SaveGame = ConfigParser()
SaveGame.read("SaveGame\save1.txt")
#----------- LOGO
IMGlogo = pygame.image.load('files\engine\logo.png')
WHITE = (255, 255, 255)
adult_mode = str(config["Settings"]["adult"])

def title():
    global level_selected
    level_selected = 0
    screen.fill(WHITE)
    screen.blit(IMGlogo, (0, 0))
    pygame.display.update()
    time.sleep(3)
    level_selected = 1 
title()
#------------

logging.info(time.strftime("%Y-%m-%d-%H.%M.%S") +"[initialization complete loaded]")
print(time.strftime("%Y-%m-%d-%H.%M.%S") +"[initialization complete loaded]")
#---------fonts loader
logging.info(time.strftime("%Y-%m-%d-%H.%M.%S") +"[Fonts loading...]")
print(time.strftime("%Y-%m-%d-%H.%M.%S") +"[Fonts loading...]")

font1 = pygame.font.Font('fonts/Noto_Sans.ttf', 24)
font2 =pygame.font.Font('fonts/Comic_Sans_MS_pixel.ttf', 24)

print(time.strftime("%Y-%m-%d-%H.%M.%S") +"[Fonts complete loaded]")
logging.info(time.strftime("%Y-%m-%d-%H.%M.%S") +"[Fonts complete loaded]")
#---------sounds loader
logging.info(time.strftime("%Y-%m-%d-%H.%M.%S") +"[Audio loading...]")
print(time.strftime("%Y-%m-%d-%H.%M.%S") +"[Audio loading...]")
#------DEV
Squit = pygame.mixer.Sound('sounds/quit.wav')
Sscreenshot = pygame.mixer.Sound('sounds/picture.wav')
#------custom

from files.loader_audio import * 

print(time.strftime("%Y-%m-%d-%H.%M.%S") +"[Audios complete loaded]")
logging.info(time.strftime("%Y-%m-%d-%H.%M.%S") +"[Audios complete loaded]")

#------image loader
logging.info(time.strftime("%Y-%m-%d-%H.%M.%S") +"[Images loading...]")
print(time.strftime("%Y-%m-%d-%H.%M.%S") +"[Images loading...]")
#------DEV
player0 = pygame.image.load('files\engine\player_empty.png')
background1 = pygame.image.load('files\engine\empty.png')
PIC_loading = pygame.image.load('files\engine\loading.png')
empty = pygame.image.load('files\engine\empty.png')
dialog_pic = pygame.image.load('files\engine\dialog_pic.png')
dialog_pic_wn = pygame.image.load('files\engine\dialog_pic_wn.png')
IMGlogoT = pygame.image.load('files\engine\logoT.png')
choice_pic = pygame.image.load('files\engine\choice.png')
#cursor_pic = pygame.image.load('files\engine\Cursor.png')
player_empty = pygame.image.load('files/engine/player_empty.png')
#------custom
menu_pic = pygame.image.load('files\engine\menu.png')
menu_pic_a = pygame.image.load('files\engine\menu_a.png')
menu_pic_b = pygame.image.load('files\engine\menu_b.png')

from files.loader_img import * 


logging.info(time.strftime("%Y-%m-%d-%H.%M.%S") +"[Images complete loaded]")
print(time.strftime("%Y-%m-%d-%H.%M.%S") +"[Images complete loaded]")


logging.info(time.strftime("%Y-%m-%d-%H.%M.%S") +"[Game loading...]")
print(time.strftime("%Y-%m-%d-%H.%M.%S") +"[Game loading...]")

#---------Выборы выборы
choice_1 = [0, 0]
choice_2 = [0, 0]
choice_3 = [0, 0]
choice_4 = [0, 0]
choice_5 = [0, 0]
choice_6 = [0, 0]
choice_7 = [0, 0]
choice_8 = [0, 0]
choice_9 = [0, 0]
choice_10 = [0, 0]
def reset_choice():
    choice_1 = [0, 0]
    choice_2 = [0, 0]
    choice_3 = [0, 0]
    choice_4 = [0, 0]
    choice_5 = [0, 0]
    choice_6 = [0, 0]
    choice_7 = [0, 0]
    choice_8 = [0, 0]
    choice_9 = [0, 0]
    choice_10 = [0, 0]
#------------------------------------------------------------
RED = (225, 0, 50)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
BLUE = (0, 21, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
transparent = (0, 0, 0, 0)
#-------------------------------------------------------------
debug_mode = str(config["Settings"]["debug"])
Hide_text = False
music_playing = ''
adult_mode = str(config["Settings"]["adult"])
FPS = int(config["Settings"]["fps"])
pygame.mixer.music.set_volume(float(config["Settings"]["volume"]))
mousex, mousey = pygame.mouse.get_pos()
run_once = True
run_once1 = True
timer = 0
#------------level number
level_selected = 1 #1 = menu
#-------------------------------------------------------------
def print_info(text_sys):
    print(time.strftime("%Y-%m-%d-%H.%M.%S") +'['+text_sys+']')
    logging.info(time.strftime("%Y-%m-%d-%H.%M.%S") +'['+text_sys+']')
#print_info("[test]")
def show_fps(screen, clock):
    if debug_mode==('yes'):
        pygame.draw.rect(screen, (100, 100, 100, 50), (0, 0, 308, 82))
        fps_overlay = font1.render('FPS: '+str(clock.get_fps()), True, GREEN)
        level_overlay = font1.render('Level: '+str(level_selected), True, GREEN)
        version_overlay = font1.render('Version: '+str(build_game), True, GREEN)
        screen.blit(fps_overlay, (5, 0))
        screen.blit(version_overlay, (5, 25))
        screen.blit(level_overlay, (5, 50))
class dialog:
    def __init__(self,level_num, name, text_1, text_2, text_3, background, player, player_x, player1, player1_x):
         self.level_num = level_num
         if level_selected==(self.level_num):
            self.name = name
            self.text_1 = text_1
            self.text_2 = text_2
            self.text_3 = text_3
            self.background = background
            self.player = player
            self.player_x = player_x
            self.player1 = player1
            self.player1_x = player1_x
            self.show()
    def show(self):
        global level_selected, run_once
        if level_selected==(self.level_num):
            if run_once:
                screen.blit(self.background,(0, 0))
                screen.blit(self.player, (self.player_x, 0))
                screen.blit(self.player1, (self.player1_x, 0))
                if self.text_1 == (""):
                    pass
                else:
                    if Hide_text ==(False):
                        if self.name == (""):
                            screen.blit(dialog_pic_wn,(0, 0))
                        else:
                            screen.blit(dialog_pic,(0, 0))
                run_once = False
            if self.text_1 == (""):
                pass
            else:
                if Hide_text ==(False):
                    text_text_1 = font1.render(self.text_1, 1, WHITE)
                    text_text_2 = font1.render(self.text_2, 1, WHITE)
                    text_text_3 = font1.render(self.text_3, 1, WHITE)
                    text_name = font2.render(self.name, 1, WHITE)
                    screen.blit(text_text_1,(40, 427))
                    screen.blit(text_text_2,(40, 471))
                    screen.blit(text_text_3,(40, 515))
                    screen.blit(text_name,(40, 370))

class choice:
    def __init__(self,level_num, text1, text2, choice_var, background, player, player_x, player1, player1_x):
         self.level_num = level_num
         if level_selected==(self.level_num):
            self.text1 = text1
            self.text2 = text2
            self.choice_var = choice_var
            self.background = background
            self.player = player
            self.player_x = player_x
            self.player1 = player1
            self.player1_x = player1_x
            self.show()
    def show(self):
        global level_selected, run_once
        if level_selected==(self.level_num):
            if run_once:
                screen.blit(self.background,(0, 0))
                screen.blit(self.player, (self.player_x, 0))
                screen.blit(self.player1, (self.player1_x, 0))
                screen.blit(choice_pic,(0, 0))
                run_once = False
        if level_selected==(self.level_num):
            if mousey<=(295):
                text_choice_1 = font1.render(self.text1, 1, YELLOW)
                text_choice_2 = font1.render(self.text2, 1, WHITE)
                self.choice_var[:] = [1, 0]
            elif mousey>=(295):
                text_choice_2 = font1.render(self.text2, 1, YELLOW)
                text_choice_1 = font1.render(self.text1, 1, WHITE)
                self.choice_var[:] = [0, 1]
            text_rect1 = text_choice_1.get_rect(center=(W/2, 243))
            text_rect2 = text_choice_2.get_rect(center=(W/2, 330))
            screen.blit(text_choice_1, text_rect1)
            screen.blit(text_choice_2, text_rect2)
        pass

class dialog_after_choice:
    def __init__(self,level_num, name, text_1, text_2, text_3, choice_var,  name1, text1_1, text1_2, text1_3, background, player, player_x, player1, player1_x):
         self.level_num = level_num
         if level_selected==(self.level_num):
            self.name = name
            self.text_1 = text_1
            self.text_2 = text_2
            self.text_3 = text_3
            self.name1 = name1
            self.text1_1 = text1_1
            self.text1_2 = text1_2
            self.text1_3 = text1_3
            self.background = background
            self.player = player
            self.player_x = player_x
            self.player1 = player1
            self.player1_x = player1_x
            self.choice_var = choice_var
            self.show()
    def show(self):
        global level_selected, run_once
        if level_selected==(self.level_num):
            if run_once:
                screen.blit(self.background,(0, 0))
                screen.blit(self.player, (self.player_x, 0))
                screen.blit(self.player1, (self.player1_x, 0))
                if self.text_1 == (""):
                    pass
                else:
                    if Hide_text ==(False):
                        if self.name == (""):
                            screen.blit(dialog_pic_wn,(0, 0))
                        else:
                            screen.blit(dialog_pic,(0, 0))
                run_once = False
            if self.name == (""):
                pass
            else:
                if Hide_text ==(False):
                    self.choice_var = str(self.choice_var)
                    if self.choice_var==str([1, 0]):
                        text_text_1 = font1.render(self.text_1, 1, WHITE)
                        text_text_2 = font1.render(self.text_2, 1, WHITE)
                        text_text_3 = font1.render(self.text_3, 1, WHITE)
                        text_name = font2.render(self.name, 1, WHITE)
                        screen.blit(text_text_1,(40, 427))
                        screen.blit(text_text_2,(40, 471))
                        screen.blit(text_text_3,(40, 515))
                        screen.blit(text_name,(40, 370))
                    elif self.choice_var ==str([0, 1]):
                        text_text_1 = font1.render(self.text1_1, 1, WHITE)
                        text_text_2 = font1.render(self.text1_2, 1, WHITE)
                        text_text_3 = font1.render(self.text1_3, 1, WHITE)
                        text_name = font2.render(self.name, 1, WHITE)
                        screen.blit(text_text_1,(40, 427))
                        screen.blit(text_text_2,(40, 471))
                        screen.blit(text_text_3,(40, 515))
                        screen.blit(text_name,(40, 370))

class dialog_set:
    def __init__(self,level_num, set_level):
         self.level_num = level_num
         self.set_level = set_level
         self.show()
    def show(self):
        global level_selected
        if level_selected==(self.level_num):
            level_selected = self.set_level

class dialog_set_after_choice:
    def __init__(self,level_num, set_level1, choice_var, set_level2):
         self.level_num = level_num
         if level_selected==(self.level_num):
            self.set_level1 = set_level1
            self.set_level2 = set_level2
            self.choice_var = choice_var
            self.show()
    def show(self):
        global level_selected
        if level_selected==(self.level_num):
            if self.choice_var==[1, 0]:
                level_selected = self.set_level1
            if self.choice_var==[0, 1]:
                level_selected = self.set_level2

class play_sound:
    def __init__(self,level_num, sound_name):
         self.level_num = level_num
         self.sound_name = sound_name
         self.play_sounds()
    def play_sounds(self):
        if level_selected==(self.level_num):
            print_info("Sound playing:"+str(self.sound_name))
            self.sound_name.play()

class play_music:
    def __init__(self,level_num, music_name):
         self.level_num = level_num
         self.music_name = music_name
         self.play_musics()
    def play_musics(self):
        global music_playing
        if level_selected==(self.level_num):
            pygame.mixer.music.load(self.music_name)
            pygame.mixer.music.play(loops=-1)
            music_playing = self.music_name
            print_info("Music playing:"+str(self.music_name))
class stop_music:
    def __init__(self,level_num):
         self.level_num = level_num
         self.stop_musics()
    def stop_musics(self):
        global music_playing
        if level_selected==(self.level_num-1):
            pygame.mixer.music.stop()
            music_playing = ''
            print_info("Music stopped")
def Save_loaded():
    global music_playing
    if music_playing ==(''):
        pygame.mixer.music.stop()
    else:
        pygame.mixer.music.load(music_playing)
        pygame.mixer.music.play(loops=-1)
class start_script:
    def __init__(self,level_num, code):
         self.level_num = level_num
         self.code = code
         self.start_scripts()
    def start_scripts(self):
        global run_once1
        if level_selected==(self.level_num):
            if run_once1==(True):
                exec(self.code)
                run_once1 = False
#-------------------------------------------------------------
print(time.strftime("%Y-%m-%d-%H.%M.%S") +"[Game complete loaded]")
logging.info(time.strftime("%Y-%m-%d-%H.%M.%S") +"[Game complete loaded]")
print_info("--------------------------------------------------------------------")
running = True

def dialogs_while():
    dialog1 = dialog(2, "Имя", "Первая строка", '2 строка', '3 строка', background1, player0, 0, player0, 0,)
    dialog1.show()

def audio_click():
    play_music1 = play_music(1000, None)
    play_sound1 = play_sound(1000, None)
    stop_music1 = stop_music(1000)
    play_sound1.play_sounds
    play_music1.play_musics
    stop_music1.stop_musics

while running:
    timer += 1
    mousex, mousey = pygame.mouse.get_pos()
	#game over
    show_fps(screen, clock)
		#-------------------------------------------------------------End dialogs
    dialogs_while()
    if level_selected==(1):
        reset_choice()
        pygame.mixer.music.stop()
        music_playing = ''
        if (mousey<=331) and (mousex<100):
            screen.blit(menu_pic_a, (0, 0))
            pass
        elif (mousey>=331) and (mousex<100):
            screen.blit(menu_pic_b, (0, 0))
            pass
        else:
            screen.blit(menu_pic, (0, 0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            Squit.play()
            time.sleep(1)
            running = False
        elif i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                run_once = True
                if level_selected==(1):
                    if (mousey>=331) and (mousex<100):
                        Squit.play()
                        time.sleep(1)
                        running = False
                        pass
                    elif (mousey<=331) and (mousex<100):
                        level_selected +=1
                        pass
                else:
                    #print("[Level:" + str(level_selected) + "]")
                    level_selected +=1
                    pass
                print("[Level:" + str(level_selected) + "]")
                run_once1 = True
                audio_click()
            elif i.button == 3:
                Hide_text = not Hide_text
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_F2:
                Sscreenshot.play()
                pygame.image.save(screen,"screenshots/"+ time.strftime("%Y-%m-%d-%H.%M.%S") +".png")
            if i.key == pygame.K_F5:
                SaveGame['Level'] = {'Level_selected': int(level_selected), 'Music_playing': str(music_playing),
					'choice_1': choice_1, 'choice_2': choice_2, 'choice_3': choice_3, 'choice_4': choice_4, 'choice_5': choice_5, 
					'choice_6': choice_6, 'choice_7': choice_7, 'choice_8': choice_8, 'choice_9': choice_9, 'choice_10': choice_10}
                with open('SaveGame\save1.txt', 'w') as configfile:
                    SaveGame.write(configfile)
                print_info("Game saved")
            if i.key == pygame.K_F6:
                screen.blit(PIC_loading,(0, 0))
                level_selected = int(SaveGame["Level"]["Level_selected"])
                music_playing = SaveGame["Level"]["music_playing"]
                choice_1 = SaveGame["Level"]['choice_1']
                choice_2 = SaveGame["Level"]["choice_2"]
                choice_3 = SaveGame["Level"]["choice_3"]
                choice_4 = SaveGame["Level"]["choice_4"]
                choice_5 = SaveGame["Level"]["choice_5"]
                choice_6 = SaveGame["Level"]["choice_6"]
                choice_7 = SaveGame["Level"]["choice_7"]
                choice_8 = SaveGame["Level"]["choice_8"]
                choice_9 = SaveGame["Level"]["choice_9"]
                choice_10 = SaveGame["Level"]["choice_10"]
                choice_1 = json.loads(choice_1)
                choice_2 = json.loads(choice_2)
                choice_3 = json.loads(choice_3)
                choice_4 = json.loads(choice_4)
                choice_5 = json.loads(choice_5)
                choice_6 = json.loads(choice_6)
                choice_7 = json.loads(choice_7)
                choice_8 = json.loads(choice_8)
                choice_9 = json.loads(choice_9)
                choice_10 = json.loads(choice_10)
                Save_loaded()
                print_info("Game loaded")
            if i.key == pygame.K_ESCAPE:
                if level_selected==(1):
                    Squit.play()
                    time.sleep(1)
                    running = False
                else:
                    Squit.play()
                    time.sleep(1)
                    level_selected = 1
    if timer==2:
        run_once = True
        timer = 0
    clock.tick(FPS)
    pygame.display.update()
pygame.quit()