#bug dans les coordonnées
import numpy
import pandas as pd
# def datamotsmeles():
#     global data
#     data=""
#     for y in range(dimensionsy):
#         #print((dimensionsy-y)-1)
#         for x in range(dimensionsx):
#             #data=data+
#             index=indexSurListe(x,(dimensionsy-y)-1)
#             data=data+letters[index]
#             #f.write(letters[index]+" ")
#         data=data+";\n"
#     #f.close()
#     data=data+";\n"
#     for mot in mots:
#         data=data+mot+";\n"
import random


alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#premier=True
# for repeat in range(fois):
#     for sens in sensPossible:
#         sensdemots.append(sens)
#         """if premier==True:
#             sensdemots.append(sens)#("hd")
#             premier=False
#         else:
#             sensdemots.append(sens)"""
        
# for sens in sensPossible:
#     sensfin.append(sens)
    
# for repeat in range(len(mots)-fois*len(sensPossible)):
#     Random=random.randint(0,len(sensfin)-1)
#     sensdemots.append(sensfin[Random])
#     del sensfin[Random]
sensdemots = random.sample(sensPossible, len(mots))

# for repeat in range(dimensionsy):
#     for repeat in range(dimensionsx):
#         letters.append("")
#     letters.append(" ")

#print(letters)
def generate(sensPossible=["h","hd","d","bd","b","bg","g","hg"],dimensionsx=20,dimensionsy=20,mots=["BEDWARS","BUILDBATTLE","BLOCKPARTY","HIDEANDSEEK","SKYWARS","PARTYGAMES","PVP","DEATHRUN"]):
    
    letters = numpy.empty((dimensionsy, dimensionsx), dtype=str)
    answers = pd.DataFrame(columns=['mot', 'sens', 'x', 'y'])
    for mot in mots:
        #print("count: "+str(count)
        sens=random.choice(sensPossible)
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
                    if letters[yh,xh]!="":
                        if letters[yh,xh]!=letter:
                            Break=True
                            break
                    xh+=addx
                    yh+=addy
                if Break==False:                
                    choixcoordonnees.append((x,y))
        assert choixcoordonnees, "Désolé, le générateur s'est planté, il suffit juste de rexcécuter le programme."
        x,y=random.choice(choixcoordonnees)
        #xh,yh=coordonnees(index)
        VraiReponses=VraiReponses+"Mot : "+mot+", Sens : "+sens+", Coordonnees : "+str(x)+", "+str(y)
        fx=x
        for letter in mot:
            letters[y,x]=letter
            #xh,yh=coordonnees(index)
            print(type(x),type(addx))
            x+=addx
            y+=addy
            #index=indexSurListe(xh+addx,yh+addy)
        VraiReponses=VraiReponses+", Jusque : "+str(x)+", "+str(y)+"\n"
    def verifsens(addx,addy):

        letters[y,x]=letter 
        mot=letter
        xh,yh=x,y
        while 0<=xh<dimensionsx and 0<=yh<dimensionsy:
            if letters[yh,xh]=="":
                return True
            if mot in mots:
                return False
            #lettrespossible.append(letter)
            mot+=letters[yh,xh]
            xh+=addx
            yh+=addy 
        return True
    #filemotsmeles("motsmeles.txt")
    #print(VraiReponses)
    #rrzu=input("enter")
    for y in range(dimensionsy):
        for x in range(dimensionsx):
            
            #pindex=indexSurListe(x,y)
            #print(index)
            #try:
            #    anciennelettre=letters[y,x]
            #except IndexError:
            #    print("len(letters) :"+str(len(letters))+"index:"+str(pindex))
            lettrespossible=[]
            if letters[y,x]=="":
                for letter in alphabet:
                    for addx,addy in [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]:
                        if not verifsens(addx,addy):
                            lettrespossible.append(letter)
                            break
                    else:
                        lettrespossible.append(letter)

                if not lettrespossible:
                    raise Exception("Désolé, le générateur s'est planté, il suffit juste de rexcécuter le programme.")
                letters[y,x]=random.choice(lettrespossible)
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

                    
                
    
