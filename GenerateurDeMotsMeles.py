#bug dans les coordonnées
def indexSurListe(x,y):
    return (y*(dimensionsx+1))+x
def coordonnees(index):
    y=int(index/(dimensionsx+1))
    return index-(y*(dimensionsx+1)),y
def datamotsmeles():
    global data
    data=""
    for y in range(dimensionsy):
        #print((dimensionsy-y)-1)
        for x in range(dimensionsx):
            #data=data+
            index=indexSurListe(x,(dimensionsy-y)-1)
            data=data+letters[index]
            #f.write(letters[index]+" ")
        data=data+";\n"
    #f.close()
    data=data+";\n"
    for mot in mots:
        data=data+mot+";\n"
import random
print("génération d'un nouveau mots mélés...")
sensdemots=[]
sensdemotsH=[]
sensfin=[]
letters=[]
VraiReponses=""
dimensionsx=20
dimensionsy=20
sensPossible=["h","hd","d","bd","b","bg","g","hg"]
lettresDeLalphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
mots=["BEDWARS","BUILDBATTLE","BLOCKPARTY","HIDEANDSEEK","SKYWARS","PARTYGAMES","PVP","DEATHRUN"]
fois=int(len(mots)/len(sensPossible))
#premier=True
for repeat in range(fois):
    for sens in sensPossible:
        sensdemots.append(sens)
        """if premier==True:
            sensdemots.append(sens)#("hd")
            premier=False
        else:
            sensdemots.append(sens)"""
        
for sens in sensPossible:
    sensfin.append(sens)
    
for repeat in range(len(mots)-fois*len(sensPossible)):
    Random=random.randint(0,len(sensfin)-1)
    sensdemots.append(sensfin[Random])
    del sensfin[Random]
    
for repeat in range(len(sensdemots)):
    Random=random.randint(0,len(sensdemots)-1)
    sensdemotsH.append(sensdemots[Random])
    del sensdemots[Random]
#sensdemotsH[0]="bd"
#print(sensdemotsH)

for repeat in range(dimensionsy):
    for repeat in range(dimensionsx):
        letters.append("")
    letters.append(" ")

#print(letters)
for count,mot in enumerate(mots):
    #print("count: "+str(count)
    sens=sensdemotsH[count]
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
            pindex=indexSurListe(x,y)
            index=pindex
            #print(", longueur de lettres: "+str(len(letters))+", index: "+str(index))
            Break=False
            for letter in mot:
                """try: #2
                    letters[index]
                except IndexError:
                    print(", longueur de lettres: "+str(len(letters))+", index: "+str(index))"""
                if letters[index]!="":
                    if letters[index]!=letter:
                        Break=True
                        break
                xh,yh=coordonnees(index)
                index=indexSurListe(xh+addx,yh+addy)
            if Break==False:                
                choixcoordonnees.append(pindex)
    if len(choixcoordonnees)>0:
        index=random.choice(choixcoordonnees)
    else:
        raise Exception("Désolé, le générateur s'est planté, il suffit juste de rexcécuter le programme.")
    xh,yh=coordonnees(index)
    VraiReponses=VraiReponses+"Mot : "+mot+", Sens : "+sens+", Coordonnees : "+str(xh)+", "+str(yh)
    for letter in mot:
        letters[index]=letter
        xh,yh=coordonnees(index)
        index=indexSurListe(xh+addx,yh+addy)
    xh,yh=coordonnees(index)
    VraiReponses=VraiReponses+", Jusque : "+str(xh)+", "+str(yh)+"\n"
def verifsens(addx,addy):
    global Break,index
    index=pindex
    letters[index]=letter 
    mot=letter
    Break=False
    while index<len(letters) and index>-1:
        if letters[index]=="":
            break
        if mot in mots:
            Break=True
            break
        #lettrespossible.append(letter)
        xh,yh=coordonnees(index)
        mot+=letters[index]
        index=indexSurListe(xh+addx,yh+addy)
#filemotsmeles("motsmeles.txt")
#print(VraiReponses)
#rrzu=input("enter")
for y in range(dimensionsy):
    for x in range(dimensionsx):
        
        pindex=indexSurListe(x,y)
        #print(index)
        try:
            anciennelettre=letters[pindex]
        except IndexError:
            print("len(letters) :"+str(len(letters))+"index:"+str(pindex))
        lettrespossible=[]
        if letters[pindex]=="":
            for letter in lettresDeLalphabet:
                verifsens(0,1)
                if Break==False:
                    verifsens(1,1)
                    if Break==False:
                        verifsens(1,0)
                        if Break==False:
                            verifsens(1,-1)
                            if Break==False:
                                verifsens(0,-1)
                                if Break==False:
                                    verifsens(-1,-1)
                                    if Break==False:
                                        verifsens(-1,0)
                                        if Break==False:
                                            verifsens(-1,1)
            lettrespossible.append(letter)

            index=pindex
            if len(lettrespossible)>0:
                letters[index]=random.choice(lettrespossible)
            else:
                raise Exception("Désolé, le générateur s'est planté, il suffit juste de rexcécuter le programme.")

datamotsmeles()
print("Terminé")
reponses=["c","r","s"]
reponse=""
while reponse=="":
    reponse=input("\nnom du fichier ?")
f=open(reponse,"w")
f.write(data)
f.close()
print("données enregistrés avec succès")
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

                    
                
    
