import pygame
import sys

class Player():
    def __init__(self, width, height, team, r = 12, x = 20, y = 20, vx = 1, vy = 1, a = 200, color = (245,234,213)):
        self.width, self.height = width, height
        self.color = color
        self.r = r
        self.a =a
        self.vx, self.vy = vx, vy
        self.x, self.y = x, y
        self._team = team
        self.keys1 = (pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN,pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s)
    def render(self,game):
        """Draw Player on the Game window"""
        pygame.draw.rect(game.screen,self.color,(self.x,self.y,self.width,self.height),2)
    def update(self,game):
        """Update Player state"""
        if game.pressed[self.keys1[self._team*4]]:
            self.vx -= game.delta * self.a
        if game.pressed[self.keys1[self._team*4+1]]:
            self.vx += game.delta * self.a
        if game.pressed[self.keys1[self._team*4+2]]:
            self.vy -= game.delta * self.a
        if game.pressed[self.keys1[self._team*4+3]]:
            self.vy += game.delta * self.a

        self.vx -= game.delta * self.vx
        self.vy -= game.delta * self.vy

        self.x += self.vx * game.delta
        self.y += self.vy * game.delta

        """Do not let Player get out of the Game window"""
        if self.x < 0:
            if self.vx < 0:
                self.vx = 0
            self.x = 0
        if self.y < self._team*(game.height/2+self.r):
            if self.vy < 0:
                self.vy = 0
            self.y = self._team*(game.height/2+ self.r)
        if self.x > game.width - self.width:
            if self.vx > 0:
                self.vx = 0
            self.x = game.width - self.width
        if self.y > (self._team+1)*game.height/2 - (1-self._team)*self.r  - self.height-1:
            if self.vy > 0:
                self.vy = 0
            self.y = (self._team+1)*game.height/2 - (1-self._team)*self.r - self.height


