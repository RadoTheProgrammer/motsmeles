import pygame
pygame.init()


class GUI:
    screen_size = (1280, 720)
    screen_color = "black"
    letter_color = "white"
    word_color = "white"
    grid_proportion = 3/4
    font_name = pygame.font.get_default_font()  # Get the default system font

    # font = pygame.font.SysFont("mishafi.ttf", 36)
    letter_font = pygame.font.SysFont(font_name, 36)
    letter_font.set_bold(True)

    def __init__(self, game):
        self.game = game

        # self.get_letter_size()
    def get_case_size(self):
        self.grid_pwidth, self.grid_pheight = (
            self.screen_size[0]*self.grid_proportion, self.screen_size[1])
        self.case_size = min((
            self.grid_pwidth/self.game.grid.shape[1],
            self.grid_pheight / self.game.grid.shape[0]))
        self.word_pwidth, self.word_pheight = (
            self.screen_size[0]*(1/self.grid_proportion),
            self.screen_size[1]/len(self.game.words)
        )
        #self.word_pheight = self.words_pheight / len(self.game.words)
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

    def get_letter_font(self):
        letter_font_size = 1
        while True:
            font = pygame.font.Font(size=letter_font_size)
            text = font.render("A", True, self.letter_color)
            if max(text.get_size()) > self.case_size:
                return
            letter_font_size += 1
            self.letter_font = font

    def get_words_font(self):
        word=self.get_biggest_word()
        word_font_size=1
        while True:
            font = pygame.font.Font(size=word_font_size)
            text = font.render(word, True, self.word_color)
            width,height = text.get_width(), text.get_height()
            if width>self.word_pwidth or height>self.word_pheight:
                print(word_font_size)
                return
            word_font_size += 1
            self.word_font = font
            
    def get_biggest_word(self):
        biggest_width=0
        for word in self.game.words:
            font = pygame.font.Font(size=12)
            text = font.render(word,True,self.word_color)
            width=text.get_width()
            if width>biggest_width:
                biggest_width=width
                biggest_word=word
        return biggest_word
        
        
            
    def start(self):
        self.get_case_size()
        self.get_letter_font()
        self.get_words_font()
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
                    letter_surface = self.letter_font.render(
                        letter, True, self.letter_color)

                    letter_rect = letter_surface.get_rect(center=(x, y))
                    self.screen.blit(letter_surface, letter_rect)
                    x += self.case_size
                y += self.case_size
            y = 0
            for word in self.game.words:
                #print(word)
                x = self.grid_pwidth
                word_surface = self.word_font.render(word,True,self.word_color)
                self.screen.blit(word_surface, word_surface.get_rect(topleft=(int(x),int(y))))
                #pygame.display.flip()
                y += self.word_pheight
            
            # RENDER YOUR GAME HERE

            # flip() the display to put your work on screen
            pygame.display.flip()

            clock.tick(60)  # limits FPS to 60

        pygame.quit()


def start_gui(game):
    GUI(game).start()
