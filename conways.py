import os
from PIL import Image

clear = lambda: os.system('cls')

def createWorld(dimlin, dimcol):
    arr = [] #RESET WORLD
    print("World Created")
    for i in range(dimlin):
        arr.append([])
        for b in range(dimcol):
            arr[i].append(0)
    return arr

def createCell(poslin,poscol, world):
    world[poslin][poscol] = 1

def showWorld(arr):
    for i in range(len(arr)):
        for b in range(len(arr[i])):
            print(arr[i][b], end = " ")
        print("")

def showWorldIm(world):
    img = Image.new('1',(len(world)-1, len(world[0])-1))
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i, j] = world[j][i]
    img.show()

def showWorldImInvert(world):
    worldToInvert = world.copy()
    for i in range(len(worldToInvert)):
        for b in range(len(worldToInvert[i])):
            if worldToInvert[i][b] == 0:
                worldToInvert[i][b] = 1
            else:
                worldToInvert[i][b] = 0
    img = Image.new('1',(len(worldToInvert)-1, len(worldToInvert[0])-1))
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i, j] = worldToInvert[j][i]
    img.show()

def checkCellAC(world,poslin,poscol): #Anti-Clockwise
    neighbors = []
    nSum = 0
    if poslin == 0 and poscol == 0: #Left Upper Corner-------------------------------
        neighbors.append(world[poslin+1][poscol]) #Down cell
        neighbors.append(world[poslin+1][poscol+1]) #Right Diagonal Down Cell
        neighbors.append(world[poslin][poscol+1]) #Right Cell

    elif poslin == 0 and poscol == len(world[poslin])-1: #Right Upper Corner-------------------------------
        neighbors.append(world[poslin][poscol-1]) #Left cell
        neighbors.append(world[poslin-1][poscol-1]) #Lef Diagonal Down Cell
        neighbors.append(world[poslin-1][poscol]) #Down Cell

    elif poslin == len(world)-1 and poscol == len(world[poslin])-1: #Right Down corner-------------------------------
        neighbors.append(world[poslin-1][poscol]) #Upper Cell
        neighbors.append(world[poslin-1][poscol-1]) #Left Upper Diagonal Cell
        neighbors.append(world[poslin][poscol-1]) #Left Cell

    elif poslin == len(world)-1 and poscol == 0: #Left Down corner-----
        neighbors.append(world[poslin-1][poscol]) #Upper Cell
        neighbors.append(world[poslin-1][poscol]) #Right Cell
        neighbors.append(world[poslin][poscol-1]) #Upper Right Diagonal Cell

    elif poslin == 0 and poscol != 0: #Upper Line (No corner)-------------------------------
        neighbors.append(world[poslin][poscol-1]) #Left Cell
        neighbors.append(world[poslin+1][poscol-1]) #Left Diagonal Down Cell
        neighbors.append(world[poslin+1][poscol]) #Down Cell
        neighbors.append(world[poslin+1][poscol+1]) #Right Diagonal Down Cell
        neighbors.append(world[poslin][poscol+1]) #Right Cell

    elif poslin == len(world)-1 and poscol != 0: #Down Line (No corner)------------------------------
        neighbors.append(world[poslin][poscol+1]) #Right Cell
        neighbors.append(world[poslin-1][poscol+1]) #Right Diagonal Down Cell
        neighbors.append(world[poslin-1][poscol]) #Upper Cell
        neighbors.append(world[poslin-1][poscol-1]) #Left Diagonal Down Cell
        neighbors.append(world[poslin][poscol-1]) #Left Cell

    elif poslin != 0 and poslin != len(world)-1 and poscol == 0: #Left Wall-------------------------------------------
        neighbors.append(world[poslin-1][poscol]) #Upper Cell
        neighbors.append(world[poslin+1][poscol]) #Down Cell
        neighbors.append(world[poslin+1][poscol+1]) #Down Right Diagonal Cell
        neighbors.append(world[poslin][poscol+1]) #Right Cell
        neighbors.append(world[poslin-1][poscol+1]) #Upper Right Diagonal Cell

    elif poslin != 0 and poscol == len(world[poslin])-1: #Right Wall-----------------------
        neighbors.append(world[poslin-1][poscol]) #Upper Cell
        neighbors.append(world[poslin-1][poscol-1]) #Upper Left Diagonal Cell
        neighbors.append(world[poslin][poscol-1]) #Left Cell
        neighbors.append(world[poslin+1][poscol-1]) #Down Left Diagonal Cell
        neighbors.append(world[poslin+1][poscol]) #Down Cell

    elif (poslin != 0 and poslin != len(world)-1) and (poscol != 0 and poscol != len(world[poslin])-1):
        neighbors.append(world[poslin-1][poscol]) #Upper Cell
        neighbors.append(world[poslin-1][poscol-1]) #Upper Left Diagonal Cell
        neighbors.append(world[poslin][poscol-1]) #Left Cell
        neighbors.append(world[poslin+1][poscol-1]) #Down Left Diagonal Cell
        neighbors.append(world[poslin+1][poscol]) #Down Cell
        neighbors.append(world[poslin+1][poscol+1]) #Down Right Diagonal Cell
        neighbors.append(world[poslin][poscol+1]) #Right Cell
        neighbors.append(world[poslin-1][poscol+1]) #Upper Right Diagonal Cell

    for i in range(len(neighbors)):
        nSum = nSum + neighbors[i]
    return nSum

def runWorld_UDLR(world,times): #UP TO DOWN AND LEFT TO RIGHT (Update World Every Cell After Checking)  
    for i in range(times):
        for b in range(len(world)):
            for c in range(len(world[b])):
                cellVal = world[b][c]
                neighbors = checkCellAC(world,b,c)
                if cellVal == 1:
                    if neighbors == 1 or neighbors == 0 or neighbors >= 4:
                        world[b][c] = 0
                elif cellVal == 0:
                    if neighbors == 3:
                        world[b][c] = 1
        #clear()
        print("RUN: ", str(i+1))
        showWorld(world)
        print("")
    showWorldImInvert(world)
    
def runWorld_UDLR_AU(world,times): #UP TO DOWN AND LEFT TO RIGHT (Update After World Scanning Every Cell)
    worldB = world.copy()
    for i in range(times):
        for b in range(len(world)):
            for c in range(len(world[b])):
                cellVal = world[b][c]
                neighbors = checkCellAC(world,b,c)
                if cellVal == 1:
                    if neighbors == 1 or neighbors == 0 or neighbors >= 4:
                        worldB[b][c] = 0
                    else:
                        worldB[b][c] = 1
                elif cellVal == 0:
                    if neighbors == 3:
                        worldB[b][c] = 1
                    else:
                        worldB[b][c] = 0
        world = worldB.copy()
        #clear()
        print("RUN: ", str(i+1))
        showWorld(world)
        print("")
    showWorldImInvert(world)




#DEBUGGING




ary = createWorld(20,20)

createCell(3,5,ary)
createCell(3,6,ary)
createCell(4,5,ary)
createCell(4,7,ary)
createCell(4,8,ary)
showWorld(ary)
print("")
runWorld_UDLR_AU(ary,4)
