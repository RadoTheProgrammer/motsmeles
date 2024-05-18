import pygame
pygame.init()


class GUI:
    screen_size = (1280, 720)
    screen_color = "black"
    letter_color = "white"
    grid_proportion = 3/4
    font_name = pygame.font.get_default_font()  # Get the default system font

    # font = pygame.font.SysFont("mishafi.ttf", 36)
    font = pygame.font.SysFont(font_name, 36)
    font.set_bold(True)

    def __init__(self, game):
        self.game = game

        # self.get_letter_size()
    def get_case_size(self):
        self.grid_pwidth, self.grid_pheight = (
            self.screen_size[0]*self.grid_proportion, self.screen_size[1])
        self.case_size = min((
            self.grid_pwidth/self.game.grid.shape[1],
            self.grid_pheight / self.game.grid.shape[0]))
        # print(pygame.font.get_fonts())
        # widths,heights=[],[]
        # for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        #     text = self.font.render("A", True, self.letter_color)
        #     s=text.get_size()
        #     print(letter,s)
        #     widths.append(s[0])
        #     heights.append(s[1])
        # self.l_size)etter_size=(max(widths),max(heights))
        # print(self.letter
        return

    def get_font(self):
        font_size = 1
        while True:
            font = pygame.font.Font(size=font_size)
            text = font.render("A", True, self.letter_color)
            if max(text.get_size()) > self.case_size:
                return
            font_size += 1
            self.font = font

    def start(self):
        self.get_case_size()
        self.get_font()
        self.screen = pygame.display.set_mode(self.screen_size)
        self.screen.fill(self.screen_color)
        self.grid_lheight, self.grid_lwidth = self.game.grid.shape
        clock = pygame.time.Clock()
        running = True

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                print(event)

            # fill the screen with a color to
            # wipe away anything from last frame

            self.screen.fill(self.screen_color)

            # Blit the text onto the screen
            # self.screen.blit(text, text_rect)
            # grid_height,grid_width = self.game.grid.shape
            y = self.case_size//2
            for row in self.game.grid:
                x = self.case_size//2
                for letter in row:
                    letter_surface = self.font.render(
                        letter, True, self.letter_color)

                    letter_rect = letter_surface.get_rect(center=(x, y))
                    self.screen.blit(letter_surface, letter_rect)
                    x += self.case_size
                y += self.case_size

            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            pygame.display.flip()

            clock.tick(60)  # limits FPS to 60

        pygame.quit()


def start_gui(game):
    GUI(game).start()
