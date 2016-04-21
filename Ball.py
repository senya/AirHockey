import pygame
import Player
import math

class Ball:
    def __init__(self, player1, player2, Vx = 10, Vy = 10, x = 300, y = 300, a = 5, r = 12, color = (225,225,225)):
        self.Vx, self.Vy, self.x, self.y, self.a, self.r, self.color = Vx, Vy, x, y , a, r, color
        self.player1, self.player2 = player1, player2

    def render(self,game):
        pygame.draw.circle(game.screen,self.color,(int(self.x),int(self.y)),self.r)

    def update(self,game):
        self.check_hit(self.player1, game)
        self.check_hit(self.player2, game)
        self.x += self.Vx * game.delta
        self.y += self.Vy * game.delta

    def check_hit(self, player, game):
        color = [(230,51,51),(54,116,225)]
        if self.x+self.r>game.width:
            self.x = game.width - self.r
            self.Vx =-self.Vx
        if self.x-self.r<0:
            self.x = self.r
            self.Vx = -self.Vx
        if self.y+self.r>game.height:
            self.y = game.height - self.r
            self.Vy = -self.Vy
        if self.y-self.r<0:
            self.y = self.r
            self.Vy = -self.Vy
        if (self.x<=player.x+player.r) and (self.x>=player.x):
            range = player.y-self.y # расстояние он верхней левой грани платформы до центра шарика
            if (range<0):
                #шарик снизу платвормы
                if abs(range+player.r) <= self.r:
                    if (abs(player.vy)>0):
                        self.Vy = player.vy + abs(self.Vy)*abs(player.vy)/player.vy    #Считаем, что после удара скорость шарика = скорости платформы
                    else:
                        self.Vy = -self.Vy
                    if (abs(player.vx)>0):
                        self.Vx = player.vx/2 + self.Vx
                    else:
                        self.Vx = self.Vx
                    self.y = player.y + player.r + self.r
                    self.color = color[player._team]
            else:
                if (abs(range) <= self.r):
                    if (abs(player.vy)>0):
                        self.Vy = player.vy + abs(self.Vy)*abs(player.vy)/player.vy
                    else:
                        self.Vy = -self.Vy
                    if (abs(player.vx)>0):
                        self.Vx = player.vx/2  + self.Vx
                    else:
                        self.Vx = self.Vx
                    self.y = player.y - self.r
                    self.color = color[player._team]
