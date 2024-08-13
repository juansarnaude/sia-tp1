import sys
import pandas as pd

class Coordinates:
    def __init__(self,posX,posY):
        self.posX = posX
        self.posY = posY

    def setNewPos(self,posX,posY):
        self.posX = posX
        self.posY = posY

states=[]

with open(f"{sys.argv[1]}.txt", "r") as file:
    map = []

    boxes=[]
    flags=[]
    player=None

    for i,line in enumerate(file):
        new_row = []
        for j,char in enumerate(line[:-1]):
            new_row.append(char)
            if char=='.':
                flag_coordinates=Coordinates(j,i)
                flags.append(flag_coordinates)
            elif char=='$':
                box_coordinates=Coordinates(j,i)
                boxes.append(box_coordinates)
            elif char=='@':
                player=Coordinates(j,i)

        map.append(new_row)

    states.append(map)
    print(pd.DataFrame(map))

    print("------------------------------")

    #Jugada 1

    map[player.posY][player.posX]=' '
    map[player.posY][player.posX+1]='@'
    player.setNewPos(player.posX + 1,player.posY)
    print(pd.DataFrame(map))
    states.append(map)


