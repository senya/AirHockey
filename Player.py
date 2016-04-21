import pygame
import sys

class Player():
    def __init__(self, team, r = 12, x = 20, y = 20, vx = 1, vy = 1, a = 200, color = (245,234,213)):
        self.color = color
        self.r = r
        self.a =a
        self.vx, self.vy = vx, vy
        self.x, self.y = x, y
        self._team = team
        self.keys1 = (pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN,pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s)
    def render(self,game):
        """Draw Player on the Game window"""
        pygame.draw.circle(game.screen,self.color,(int(self.x),int(self.y)),self.r)
    def update(self,game):
        """Update Player state"""
        if game.pressed[self.keys1[self._team*4]]:
            self.vx -= game.delta * self.a
            self.x-=game.delta * self.a
        if game.pressed[self.keys1[self._team*4+1]]:
            self.vx += game.delta * self.a
            self.x+=game.delta * self.a
        if game.pressed[self.keys1[self._team*4+2]]:
            self.vy -= game.delta * self.a
            self.y-=game.delta * self.a
        if game.pressed[self.keys1[self._team*4+3]]:
            self.vy += game.delta * self.a
            self.y+=game.delta * self.a

        self.vx -= game.delta * self.vx
        self.vy -= game.delta * self.vy

        #self.x += self.vx * game.delta
        #self.y += self.vy * game.delta

        """Do not let Player get out of the Game window"""
        """Касание левой грани"""
        if self.x-self.r < 0:
            if self.vx < 0:
                self.vx = 0
            self.x = self.r

        """Касание верхней грани"""
        if self.y < self._team*(game.height/2) + (self.r):
            if self.vy < 0:
                self.vy = 0
            self.y = self._team*(game.height/2) + (self.r)

        """Касание правой грани"""
        if self.x > game.width - self.r:
            if self.vx > 0:
                self.vx = 0
            self.x = game.width - self.r

        """Касание нижней грани"""
        if self.y > (self._team+1)*game.height/2 - self.r:
            if self.vy > 0:
                self.vy = 0
            self.y = (self._team+1)*game.height/2 - self.r;


