
import numpy
import pandas as pd
import random
import sys
import builtins

from psutil import sensors_battery

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# TODO remplacer sensPossible par allow_inverse, allow_diagonal
def generate(
    mots,
    dimensionsx=10,
    dimensionsy=10,
    sensPossible={"b","d","h","g","bg","bd","hd","hg"}
    # allow_diagonal=True,
    # allow_reverse=True,
    ):
    # sensPossible = {"b","d"} | (
    #     {"bg","bd","hd","hg"} if allow_diagonal else set() &\
    #     {"h","g","hd","bg"} if allow_reverse else set())
    jeu = numpy.empty((dimensionsy, dimensionsx), dtype=str)
    answers = pd.DataFrame(columns=['mot', 'sens', 'x', 'y','xh', 'yh'])
    for mot in mots:
        #Vérification du mot
        mot = mot.upper()
        for letter in mot:
            assert letter in alphabet,f"Mot invalid: {mot}"
        dim = min(dimensionsx, dimensionsy)
        assert len(mot) <= dim, f"Mot trop long: {mot}"
        
        #choix de rangey, rangex, addy, addx
        sens = random.choice(tuple(sensPossible))
        if "h" in sens:
            """if count==2: #2
                print("math: "+str((dimensionsy-len(mots))+1))"""
            rangey=range((dimensionsy-len(mot))+1)
            addy=1
        elif "b" in sens:
            rangey=range(len(mot)-1,dimensionsy)
            #print("b rangey :"+str(rangey))
            addy=-1
        else:
            rangey=range(dimensionsy)
            addy=0
        if "d" in sens:
            rangex=range((dimensionsx-len(mot))+1)
            addx=1
        elif "g" in sens:
            rangex=range(len(mot)-1,dimensionsx)
            addx=-1
        else:
            rangex=range(dimensionsx)
            addx=0
        """if count==2: #2
            print("rangey: "+str(rangey)+", rangex: "+str(rangex))"""
        for _ in range(10):
            choixcoordonnees=[]
            for y in rangey:

                for x in rangex:

                    #pindex=indexSurListe(x,y)
                    #index=pindex
                    #print(", longueur de lettres: "+str(len(letters))+", index: "+str(index))
                    xh,yh=x,y #create copy of x,y
                    Break=False
                    for letter in mot:
                        """try: #2
                            letters[index]
                        except IndexError:
                            print(", longueur de lettres: "+str(len(letters))+", index: "+str(index))"""
                        #Verify if it's a good emplacement mean: verify if it's blank OR filled with the right letter
                        if jeu[yh,xh]!="":
                            if jeu[yh,xh]!=letter:
                                break
                        xh+=addx
                        yh+=addy
                    else:               
                        choixcoordonnees.append((y,x))
        else:
            raise ValueError(f"Impossible de placer le mot {mot}")
        y,x=random.choice(choixcoordonnees)
        #xh,yh=coordonnees(index)
        xh,yh=x,y
        for letter in mot:
            jeu[yh,xh]=letter # a big debug: replace with yh, xh
            #xh,yh=coordonnees(index)
            #print(type(x),type(addx))
            xh+=addx
            yh+=addy
        answers.loc[len(answers)] = {'mot': mot, 'sens': sens, 'x': x, 'y': y,'xh': xh, 'yh': yh}
        #answers = answers.append({'mot': mot, 'sens': sens, 'x': x, 'y': y,'xh': xh, 'yh': yh}, ignore_index=True)

            #index=indexSurListe(xh+addx,yh+addy)
    def verifsens(addx,addy):

        jeu[y,x]=letter 
        mot=letter
        xh,yh=x,y
        while 0<=xh<dimensionsx and 0<=yh<dimensionsy:
            if jeu[yh,xh]=="":
                return True
            if mot in mots:
                return False
            #lettrespossible.append(letter)
            mot+=jeu[yh,xh]
            xh+=addx
            yh+=addy 
        return True
    #filemotsmeles("motsmeles.txt")
    #print(VraiReponses)
    #rrzu=input("enter")
    # FIXME a bug of blank letters
    for y in range(dimensionsy):
        for x in range(dimensionsx):
            for _ in range(1):
                xs,ys=x,y
                #pindex=indexSurListe(x,y)
                #print(index)
                #try:
                #    anciennelettre=letters[y,x]
                #except IndexError:
                #    print("len(letters) :"+str(len(letters))+"index:"+str(pindex))
                lettrespossible=[]
                if jeu[y,x]:
                    #print(repr(letters[y,x]))
                    break
                for letter in alphabet:
                    for addx,addy in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
                        if not verifsens(addx,addy):
                            lettrespossible.append(letter)
                            break
                    else:
                        lettrespossible.append(letter)

                assert lettrespossible, "Désolé, le générateur s'est planté, il suffit juste de rexcécuter le programme."
                jeu[y,x]=random.choice(lettrespossible)
            if jeu[ys,xs] not in alphabet:
                pass
            
            
    for y in range(dimensionsy):
        for x in range(dimensionsx):
            if jeu[y,x] not in alphabet:
                pass
    
    # for y in range(dimensionsy):
    #     for x in range(dimensionsx):
    #         if letters[y,x]=="":
    #             pass
                #letters[y,x]=random.choice(alphabet)
    return jeu,answers

def print(letters,file=sys.stdout):
    for y in range(len(letters)):
        for x in range(len(letters[0])):
            builtins.print(letters[y,x],end="",file=file)
        builtins.print(file=file)

def save(letters,file="motsmeles.txt"):
    with open(file,"w") as f:
        print(letters,file=f)
#datamotsmeles()
# reponses=["c","r","s"]
# reponse=""
# while reponse=="":
#     reponse=input("\nnom du fichier ?")
# f=open(reponse,"w")
# f.write(data)
# f.close()
# print("données enregistrés avec succès")
"""while True:
    reponse=None
    while reponse not in reponses:
        reponse=input("\n\nc pour voir le code\nr pour voir les réponses\ns pour enregistrer dans un fichier")
    if reponse=="c":
        print("\n\ncode :\n\n"+data.replace("\n",""))
    elif reponse=="r":
        print("\n\nRéponses :\n"+VraiReponses)
    else:
        reponse=input("\n\nnom du fichier?")
        if reponse!="":
            f=open(reponse,"w")
            f.write(data)
            f.close()
            print("données enregistrés avec succès")"""

                    
                
    
