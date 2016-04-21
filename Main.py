import pygame
import Player
import Ball


class Game:
    def tick(self):
        """Return time in seconds since previous call
        and limit speed of the game to 50 fps"""
        self.delta = self.clock.tick(50) / 1000.0

    def __init__(self):
        """Constructor of the Game"""
        self._running = True
        self.size = self.width, self.height = 640, 600
        # create main display - 640x400 window
        # try to use hardware acceleration
        self.screen = pygame.display.set_mode(self.size)#, pygame.HWSURFACE
        #self.image = pygame.Surface((640,400))
        # set window caption
        pygame.display.set_caption('Game')
        # get object to help track time
        self.clock = pygame.time.Clock()
        # set default tool
        self.tool = 'run'
        self.player  = Player.Player(1, x=220, y=370,r = 30 )
        self.player2 = Player.Player(0, x=220, y=10,r = 30 )
        self.ball    = Ball.Ball(player1=self.player, player2=self.player2)

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

        self.ball.update(self)
        self.player.update(self)
        self.player2.update(self)


    def render(self):
        """Render the scene"""
        self.screen.fill((0, 0, 0))
        #self.screen = pygame.image.load("images/back.png")
        #self.image = pygame.image.load("images/back.png")
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