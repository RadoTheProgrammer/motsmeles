

import numpy as np
import pandas as pd
import random
import sys
import builtins


ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
debug_mode = hasattr(sys, 'gettrace') and sys.gettrace()
# 1TODO remplacer sensPossible par allow_inverse, allow_diagonal
class GenerateError(Exception):
    pass
DEFAULT_WIDTH=10
DEFAULT_HEIGHT=10
DIRECTIONS=((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))
class Game:
    def __init__(self,grid,words=None):
        if isinstance(grid,str):
            grid=grid.strip().split("\n")
            if not words:
                grid,words=grid[:-1],grid[-1]
            grid=np.array([list(line) for line in grid],dtype="<U1")
        assert isinstance(grid,np.ndarray)
        self.grid=grid
        
        if isinstance(words,str):
            words=words.split(" ")
        words=[word.upper() for word in words]
        self.words=words
        
    @classmethod
    def generate(
        cls,
        words,
        width=DEFAULT_WIDTH,
        height=DEFAULT_HEIGHT,
        #sensPossible={"b","d","h","g","bg","bd","hd","hg"}
        no_diagonal=False,
        no_reverse=False,
        ):


        """
        d - down
        r - right
        u - up
        l - left
        dl - down-left
        dr - down-right
        ur - up-right
        ul - up-left
        """
        possible_directions = DIRECTIONS
        if no_diagonal:
            possible_directions = [d for d in possible_directions if 0 in d]
        if no_reverse:
            possible_directions = [d for d in possible_directions if -1 not in d]
            

        
        def _generate():
            grid = np.empty((height, width), dtype=str)
            answers = pd.DataFrame(index=words, columns=['direction', 'x1', 'y1','x2', 'y2'])
            # 1. Placer les mots
            for word in words:
                #Vérification du mot
                word = word.upper()
                for letter in word:
                    assert letter in ALPHABET,f"Mot invalid: {word}"
                dim = min(width, height)
                assert len(word) <= dim, f"Mot trop long: {word}"
                
                #choix de rangey, rangex, addy, addx
                addx,addy = random.choice(tuple(possible_directions))
                if addy==1:
                    rangey=range((height-len(word))+1)
                    
                elif addy==-1:
                    rangey=range(len(word)-1,height)

                else:
                    rangey=range(height)

                if addx==1:
                    rangex=range((width-len(word))+1)

                elif addx==-1:
                    rangex=range(len(word)-1,width)

                else:
                    rangex=range(width)
                    addx=0

                choixcoordonnees=[]
                for y1 in rangey:

                    for x1 in rangex:

                        x2,y2=x1,y1 #create copy of x,y
                        Break=False
                        for letter in word:

                            #Verify if it's a good emplacement mean: verify if it's blank OR filled with the right letter
                            if grid[y2,x2]!="":
                                if grid[y2,x2]!=letter:
                                    break
                            x2+=addx
                            y2+=addy
                        else:               
                            choixcoordonnees.append((y1,x1))
                if not choixcoordonnees: 
                    
                    raise GenerateError(f"Unable to place the word {word}")
                y1,x1=random.choice(choixcoordonnees)
                #xh,yh=coordonnees(index)
                x2,y2=x1,y1
                for letter in word:
                    grid[y2,x2]=letter # a big debug: replace with yh, xh

                    x2+=addx
                    y2+=addy
                answers.loc[word] = {'direction': (addx,addy), 'x1': x1, 'y1': y1,'x2': x2-addx, 'y2': y2-addy}

            def verifsens(addx,addy):
                """Verify if the letter can be placed without placing a word in the same direction"""
                grid[y1,x1]=letter 
                word=letter
                xh,yh=x1,y1
                while 0<=xh<width and 0<=yh<height:
                    if grid[yh,xh]=="":
                        return True
                    if word in words:
                        return False
                    #lettrespossible.append(letter)
                    word+=grid[yh,xh]
                    xh+=addx
                    yh+=addy 
                return True

            for y1 in range(height):
                for x1 in range(width):
                    for _ in range(1):
                        xs,ys=x1,y1
                        lettrespossible=[]
                        if grid[y1,x1]:
                            #print(repr(letters[y,x]))
                            break
                        for letter in ALPHABET:
                            for addx,addy in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
                                if not verifsens(addx,addy):
                                    #lettrespossible.append(letter)
                                    break
                            else:
                                lettrespossible.append(letter)
                        if not lettrespossible:
                            raise GenerateError(f"Unable to place {x1},{y1}")
                        grid[y1,x1]=random.choice(lettrespossible)
                    if grid[ys,xs] not in ALPHABET:
                        pass
                
            return cls(grid,words),answers
        
        errs=[]
        for _ in range(10):
            try:
                return _generate()
            except GenerateError as err:
                if debug_mode:
                    print(err)
        else:
            raise GenerateError("Unable to generate a grid")

        
    def solve(self):
        answers = pd.DataFrame(index=self.words, columns=['direction', 'x1', 'y1', 'x2', 'y2']).reindex(self.words)
        for y1 in range(self.grid.shape[0]):
            for x1 in range(self.grid.shape[1]):
                for direction in DIRECTIONS:
                    x2,y2=x1,y1
                    word=""
                    while 0<=x2<self.grid.shape[1] and 0<=y2<self.grid.shape[0]:
                        word+=self.grid[y2,x2]
                        if word in self.words:
                            answers.loc[word] = {'direction': direction, 'x1': x1, 'y1': y1,'x2': x2, 'y2': y2}
                            break
                        x2+=direction[0]
                        y2+=direction[1]
        return answers

    def __repr__(self):
        s=""
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                s+=self.grid[y,x]
            s+="\n"
        s+=" ".join(self.words)
        return s

    @classmethod
    def load(cls,file="game1.txt"):
        with open(file) as f:
            return cls(f.read())
    def save(self,file="mygame.txt"):
        with open(file,"w") as f:
            f.write(repr(self))
    def start_gui(self):
        from .gui import GUI
        GUI(self).start()
        
generate=Game.generate
load=Game.load
        


                    
                
    
