
import numpy
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
def generate(
    words,
    width=DEFAULT_WIDTH,
    height=DEFAULT_HEIGHT,
    #sensPossible={"b","d","h","g","bg","bd","hd","hg"}
    no_diagonal=False,
    no_reverse=False,
    ):

    sensPossible={"b","d","h","g","bg","bd","hd","hg"}
    if no_diagonal:
        sensPossible -= {"bg","bd","hd","hg"}
    if no_reverse:
        sensPossible -= {"h","g","hd","bg"}
        
    grid = numpy.empty((height, width), dtype=str)
    answers = pd.DataFrame(columns=['word', 'direction', 'x1', 'y1','x2', 'y2'])
    
    def _generate():
        # 1. Placer les mots
        for word in words:
            #Vérification du mot
            word = word.upper()
            for letter in word:
                assert letter in ALPHABET,f"Mot invalid: {word}"
            dim = min(width, height)
            assert len(word) <= dim, f"Mot trop long: {word}"
            
            #choix de rangey, rangex, addy, addx
            direction = random.choice(tuple(sensPossible))
            if "h" in direction:

                rangey=range((height-len(word))+1)
                addy=1
            elif "b" in direction:
                rangey=range(len(word)-1,height)
                addy=-1
            else:
                rangey=range(height)
                addy=0
            if "d" in direction:
                rangex=range((width-len(word))+1)
                addx=1
            elif "g" in direction:
                rangex=range(len(word)-1,width)
                addx=-1
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
            answers.loc[len(answers)] = {'word': word, 'direction': direction, 'x1': x1, 'y1': y1,'x2': x2, 'y2': y2}

        def verifsens(addx,addy):

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
                                lettrespossible.append(letter)
                                break
                        else:
                            lettrespossible.append(letter)
                    if not lettrespossible:
                        raise GenerateError(f"Unable to place {x1},{y1}")
                    grid[y1,x1]=random.choice(lettrespossible)
                if grid[ys,xs] not in ALPHABET:
                    pass
            
        return grid,answers
    errs=[]
    for _ in range(10):
        try:
            return _generate()
        except GenerateError as err:
            if debug_mode:
                print(err)
    else:
        raise GenerateError("Unable to generate a grid")

def print(grille,file=sys.stdout):
    for y in range(len(grille)):
        for x in range(len(grille[0])):
            builtins.print(grille[y,x],end="",file=file)
        builtins.print(file=file)

def save(grille,file="motsmeles.txt"):
    with open(file,"w") as f:
        print(grille,file=f)
def save_answers(answers,file="motsmeles-answers.csv"):
    answers.to_csv(file,index=False)
        
def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="générateur de mots mêlés")
    parser.add_argument("words", nargs="+", help="les mots à placer")
    parser.add_argument("-W", "--width", type=int, default=DEFAULT_WIDTH, help="the width of the grid")
    parser.add_argument("-H", "--height", type=int, default=DEFAULT_HEIGHT, help="the height of the grid")
    #parser.add_argument("-o", "--output-file", help="fichier de sortie")
    parser.add_argument("-d","--no-diagonal", action="store_true", help="no diagonal words")
    parser.add_argument("-r","--no-reverse", action="store_true", help="no reverse words")
    args=parser.parse_args()
    grid,answers=generate(
        args.words,
        args.width,
        args.height,
        no_diagonal=args.no_diagonal,
        no_reverse=args.no_reverse,
        )
    print(grid)
    builtins.print(answers)
if __name__=="__main__":
    main()


                    
                
    
