import random

class Enviroment:
    def __init__(self,size_x,size_y):
        self.sizex=size_x
        self.sizey=size_y
        self.tablero=[[0]*self.sizex for i in range(self.sizey)]
    
    def CreateDirt(self,cantDirt):
        while cantDirt>0:
            x=random.randint(0,self.sizex-1)
            y=random.randint(0,self.sizey-1)
            if self.tablero[x][y] == 0 :
                self.tablero[x][y]=1
                cantDirt-=1
    
    def ValidMove(self,posX,posY):
        if posX < self.sizex and posX >-1 and posY < self.sizey and posY > -1:
            return True
        
        return False
    
    def isDirty(self,posX,posY):
        if self.tablero[posX][posY] == 1:
            return True
        
        return False
    
    def Clean(self,posX,posY):
        self.tablero[posX][posY]=0

    def SizeX(self):
        return self.sizex

    def SizeY(self):
        return self.sizey
    
    def Print(self):
        for y in range (0,self.sizey):

            print("[",end=" ")

            for x in range (0,self.sizex):

                if self.tablero[x][y]==0:
                    print("0",end=" ")

                if self.tablero[x][y]==1:
                    print("1",end=" ")

                if self.tablero[x][y]==5:
                    print("S",end=" ")
                
                if self.tablero[x][y]==10:
                    print("E",end=" ")

            print("]")