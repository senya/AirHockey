import pygame
import Player
import math

class Ball:
    def __init__(self, Vx = 10, Vy = 10, x = 300, y = 300, a = 5, r = 12, color = (225,225,225)):
        self.Vx, self.Vy, self.x, self.y, self.a, self.r, self.color = Vx, Vy, x, y , a, r, color

    def render(self,game):
        pygame.draw.circle(game.screen,self.color,(int(self.x),int(self.y)),self.r)

    def update(self,game):
        self.x += self.Vx * game.delta
        self.y += self.Vy * game.delta

    def check_hit(self, player, game):
        color = [(230,51,51),(54,116,225)]
        """Удар с правой гранью экрана"""
        if self.x + self.r + game.ethik>game.width:
            self.x = game.width - game.ethik - self.r
            self.Vx =-self.Vx

        """Удар с левой гранью экрана"""
        if self.x - self.r - game.ethik<0:
            self.x = self.r + game.ethik
            self.Vx = -self.Vx

        """Удар с нижней гранью экрана"""
        if self.y + self.r + game.ethik>game.height:
            self.y = game.height - self.r - game.ethik
            self.Vy = -self.Vy

        """Удар с верхней гранью экрана"""
        if self.y-self.r - game.ethik<0:
            self.y = self.r + game.ethik
            self.Vy = -self.Vy

        """Удар с шаром игрока"""
        if ((self.x - player.x)**2+(self.y - player.y)**2<(self.r+player.r)**2):
            mod = math.sqrt((self.x - player.x)**2+(self.y - player.y)**2)       #Содуль вектора, соединящего центры шаров
            cosa = (self.x-player.x)/mod                                         #Косинус угла наклона вектора, соединяющего центры шаров
            sina = (self.y-player.y)/mod
            self.x = player.x + (self.r+player.r)*(self.x-player.x)/mod
            self.y = player.y + (self.r+player.r)*(self.y-player.y)/mod
            self.color = color[player._team]
            self.Vx = player.vx + self.Vx
            self.Vy = player.vy + self.Vy
