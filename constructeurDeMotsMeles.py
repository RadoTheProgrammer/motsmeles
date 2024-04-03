def impression3D(nomdefichier,originex,originey,originez):
    f=open(nomdefichier,"r")
    lignes=f.readlines()
    f.close()
    coords=lignes[0].split(",")
    dimensionsx=int(coords[0])
    dimensionsy=int(coords[1])
    dimensionsz=int(coords[2])
    for repeat in range(1):
        idxligne=1
        mc.setBlocks(originex,originey,originez,originex+(dimensionsx-1),originey+(dimensionsy-1),originez+(dimensionsz-1),1)
        for y in range(dimensionsy):
            #mc.setBlocks(originex,originey+y,originez,originex+(dimensionsx-1),originey+y,originez+(dimensionsz-1),1)
            idxligne=idxligne+1
            for x in range(dimensionsx):
                ligne=lignes[idxligne]
                idxligne=idxligne+1
                donnee=ligne.split(",")
                for z in range(dimensionsz):
                    blockid=donnee[z].split("/")
                    if len(blockid)==1:
                        mc.setBlock(originex+x,originey+y,originez+z,int(blockid[0]))
                    else:
                        mc.setBlock(originex+x,originey+y,originez+z,int(blockid[0]),int(blockid[1]))
from mcpi.minecraft import Minecraft,Vec3
from os import path
mc=Minecraft.create()
question=True
while question:
    reponse=input("Le fichier qui contient du code?")
    if path.exists(reponse):
        question=False
    else:
        print("Fichier non trouvé")
print("Chargement du mots mélés...")
f=open(reponse,"r")
lignes=f.readlines()
f.close()
DIMX=6
DIMY=8
longueurDeLigne=len(lignes[0])

x,y,z=mc.player.getTilePos()
x+=1
z+=1

"""while letter<len(data):
    xcons=x
    while data[letter]!="\n":
        file=data[letter]+".csv"
        if path.exists(file):
            impression3D(data[letter]+".csv",xcons,y,z)
        else:
            impression3D("inconnu.csv",xcons,y,z)
        xcons+=DIMX
        letter+=2
    letter+=1
    y+=DIMY"""
for count in range(len(lignes)): 
    xcons=x
    ligne=lignes[len(lignes)-(count+1)][:-1].replace(" ","")
    for letter in ligne: 
        file=letter+".csv"
        if path.exists(file):
            impression3D(file,xcons,y,z)
        else:
            impression3D("datainconnu.csv",xcons,y,z)
        xcons+=DIMX
    y+=DIMY
print("Terminé")
    
