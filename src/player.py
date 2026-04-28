from pgzero.actor import Actor
from pgzero.keyboard import keyboard
from pygame.display import list_modes


class Player:
    def __init__(self):
        self.actor = Actor("player_idle1", (300, 650))
        self.limit = False

        self.index = 0
        self.frame_delay = 8

        self.animations_walk = [
            "player_walk1", "player_walk2", "player_walk3", "player_walk4", "player_walk5"
        ]

        self.animations_idle = [
            "player_idle1", "player_idle2", "player_idle3", "player_idle4"
        ]
        self.animations_atack = [

        ]

    # animação andando
    def animation_walk(self):
        if self.frame_delay > 0:
            self.frame_delay -= 1
        else:
            self.index = (self.index + 1) % len(self.animations_walk)
            self.actor.image = self.animations_walk[self.index]
            self.frame_delay = 8

    # animação parado
    def animation_idle(self):
        if self.frame_delay > 0:
            self.frame_delay -= 1
        else:
            self.index = (self.index + 1) % len(self.animations_idle)
            self.actor.image = self.animations_idle[self.index]
            self.frame_delay = 12

    def movimento(self):
        moving = False

        # direita
        if keyboard.d and self.limit == False:
            self.actor.x += 3
            moving = True

        # esquerda
        if keyboard.a and self.limit == False:
            self.actor.x -= 3
            moving = True

        # escolhe animação
        if moving:
            self.animation_walk()
        else:
            self.animation_idle()

    def render_limte(self,WIDTH): #Limite de borda
        if self.actor.x <= 30:
            self.limit = True
            self.actor.x += 10
        else:
            self.limit = False
        if self.actor.x >= (WIDTH - 100):
            self.limit = True
            self.actor.x -= 10


    def draw(self):
        self.actor.draw()

    def update(self,WIDTH):
        self.render_limte(WIDTH)
        self.movimento()