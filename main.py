import pgzrun
from pgzero.actor import Actor

from src import player
#configs da tela
WIDTH = 1448
HEIGHT = 1086
FPS = 60
status_game = "Start"
musics = "sounds_menu"
music.play(musics)
player = player.Player()

def sounds():
    global musics
    if status_game == "Menu":
        musics = "sounds_menu"
sounds()

def menu():
    bg = Actor("bg_inicial_2")
    bg.draw()
def game_start():
    bg = Actor("bg_start")
    bg.draw()

def draw():
    if status_game == "Menu":
        menu()
    elif status_game == "Start":
        game_start()
        player.draw()
def update():
    player.update(WIDTH)
pgzrun.go()
