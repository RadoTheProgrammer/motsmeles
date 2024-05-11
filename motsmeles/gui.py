import pygame
pygame.init()
class GUI:
    size = (1280, 720)
    screen_color = "black"
    def __init__(self,game):
        self.game=game
        
    def start(self):
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill("blue")
        clock = pygame.time.Clock()
        running = True

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                print(event)

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill(self.screen_color)
            #grid_height,grid_width = self.game.grid.shape
            #for ygrid in range(grid_height):
            #    for xgrid in range(grid_width):
                    

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            pygame.display.flip()

            clock.tick(60)  # limits FPS to 60

        pygame.quit()
        
def start_gui(game):
    gui = GUI(game)
    gui.start()
    return gui