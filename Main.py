import pygame
import Player
import Ball


class Game:
    def tick(self):
        """Return time in seconds since previous call
        and limit speed of the game to 50 fps"""
        self.delta = self.clock.tick(70) / 1000.0

    def __init__(self):
        """Constructor of the Game"""
        self._running = True
        pygame.init()
        self.size = self.width, self.height = 450, 600
        # create main display - 640x400 window
        # try to use hardware acceleration
        self.screen = pygame.display.set_mode(self.size)#, pygame.HWSURFACE
        pygame.display.set_caption('Game')
        self.clock = pygame.time.Clock()
        # set default tool
        self.tool = 'run'
        self.player  = Player.Player(1, x=self.width/2, y=370,r = 30 )   # Синий нижний игрок
        self.player2 = Player.Player(0, x=self.width/2, y=50,r = 30 )    # Красный верхний игрок
        self.ball    = Ball.Ball()
        self.ethik   = 10                                                  # Толщина отступов
        self.ecolor = (255,179,0)
        self.font = pygame.font.Font('materials/9013.ttf', 100)
        self.gate = 40                                                     # Полудлина ворот

    def event_handler(self, event):
        """Handling one pygame event"""
        if event.type == pygame.QUIT:
            # close window event
            self.exit()
        elif event.type == pygame.KEYDOWN:
            # keyboard event on press ESC
            if event.key == pygame.K_ESCAPE:
                self.exit()

    def move(self):
        """Here game objects update their positions"""
        self.tick()
        self.pressed = pygame.key.get_pressed()
        self.ball.check_hit(self.player,self)
        self.ball.check_hit(self.player2,self)
        self.ball.update(self)
        self.player.update(self)
        self.player2.update(self)

    def render(self):
        """Render the scene"""
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(game.screen,self.ecolor,(0,0,self.width/2-self.gate,self.ethik))                                #Край верхней грани
        pygame.draw.rect(game.screen,self.ecolor,(self.width/2+self.gate,0,self.width,self.ethik))                       ###################
        pygame.draw.rect(game.screen,self.ecolor,(0,0,self.ethik,self.height))                                           # Край левой грани
        pygame.draw.rect(game.screen,self.ecolor,(self.width-self.ethik,0,self.ethik,self.height))                       # Край правой грани
        pygame.draw.rect(game.screen,self.ecolor,(0,self.height-self.ethik,self.width/2-self.gate,self.height))          # Край нижней грани
        pygame.draw.rect(game.screen,self.ecolor,(self.width/2+self.gate,self.height-self.ethik,self.width,self.height)) ###################
        self.player.render(self)
        self.player2.render(self)
        self.ball.render(self)
        pygame.display.flip()

    def exit(self):
        """Exit the game"""
        self._running = False

    def cleanup(self):
        """Cleanup the Game"""
        pygame.quit()

    def execute(self):
        """Execution loop of the game"""
        while(self._running):
            # get all pygame events from queue
            for event in pygame.event.get():
                self.event_handler(event)
            self.move()
            self.render()
        self.cleanup()
if __name__ == "__main__":
    game = Game()
    game.execute()