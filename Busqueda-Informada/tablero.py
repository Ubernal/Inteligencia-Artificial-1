from aEstrella import *
import random

class Tablero:
    def __init__(self,size_x,size_y,startPos,endPos):
        self.sizex=size_x
        self.sizey=size_y
        self.tablero=[[0]*self.sizex for i in range(self.sizey)]
        self.tablero[startPos.X][startPos.Y]=5
        self.tablero[endPos.X][endPos.Y]=10
    
    def CreateObstacles(self,cantObs):
        while cantObs>0:
            x=random.randint(0,self.sizex-1)
            y=random.randint(0,self.sizey-1)
            if self.tablero[x][y] == 0 :
                self.tablero[x][y]=1
                cantObs-=1
    
    def Adyacentes(self,pos):
        adyacentes = [ Position(pos.X+1,pos.Y),Position(pos.X-1,pos.Y), Position(pos.X,pos.Y+1), Position(pos.X,pos.Y-1) ]
        result = []
        for adyacente in adyacentes:
            if adyacente.X > -1 and adyacente.X < self.sizex and adyacente.Y > -1 and adyacente.Y < self.sizey:
                if self.tablero[adyacente.X][adyacente.Y] == 0 or self.tablero[adyacente.X][adyacente.Y] == 10:
                    result.append(adyacente)
        
        return result

    
    def Print(self):
        for y in range (0,self.sizey):

            print("[",end=" ")

            for x in range (0,self.sizex):

                if self.tablero[x][y]==0:
                    print("⬜",end=" ")

                if self.tablero[x][y]==1:
                    print("⬛",end=" ")

                if self.tablero[x][y]==5:
                    print("🔷",end=" ")

                if self.tablero[x][y]==10:
                    print("🔶",end=" ")
                
                if self.tablero[x][y] == 20:
                    print("▞",end=" ")

            print("]")