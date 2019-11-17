

class Aspiradora:
    def __init__(self,startX,startY,room):
        self.room=room
        self.currentX=startX
        self.currentY=startY
        self.room.tablero[startX][startY]=5
        self.puntos=0
        self.life = 0
    
    def perspective(self):
        for x in range (0,self.room.SizeX()):
            for y in range (0,self.room.SizeY()):
                if self.room.isDirty(x,y):
                    return False
        
        return True

    def goLeft(self):
        if self.room.isDirty(self.currentX, self.currentY):
            self.room.Clean(self.currentX, self.currentY)
            self.puntos += 1
            self.life += 1

        if self.room.ValidMove(self.currentX-1, self.currentY):
            if self.room.isDirty(self.currentX-1, self.currentY):
                self.room.Clean(self.currentX-1, self.currentY)
                self.puntos += 1
                self.life += 1

            self.currentX -= 1
            self.life += 1
            return True
        
        return False

    def goRight(self):
        if self.room.isDirty(self.currentX, self.currentY):
            self.room.Clean(self.currentX, self.currentY)
            self.puntos += 1
            self.life += 1

        if self.room.ValidMove(self.currentX+1, self.currentY):
            if self.room.isDirty(self.currentX+1, self.currentY):
                self.room.Clean(self.currentX+1, self.currentY)
                self.puntos += 1
                self.life += 1

            self.currentX += 1
            self.life += 1
            return True
        
        return False

    def goDown(self):

        if self.room.isDirty(self.currentX, self.currentY):
            self.room.Clean(self.currentX, self.currentY)
            self.puntos += 1
            self.life += 1

        if self.room.ValidMove(self.currentX, self.currentY+1):
            if self.room.isDirty(self.currentX, self.currentY+1):
                self.room.Clean(self.currentX, self.currentY+1)
                self.puntos += 1
                self.life += 1

            self.currentY += 1
            self.life += 1

            return True
        
        return False

    def goUP(self):
        if self.room.isDirty(self.currentX, self.currentY):
            self.room.Clean(self.currentX, self.currentY)
            self.puntos += 1
            self.life += 1

        if self.room.ValidMove(self.currentX, self.currentY-1):
            if self.room.isDirty(self.currentX, self.currentY-1):
                self.room.Clean(self.currentX, self.currentY-1)
                self.puntos += 1
                self.life += 1

            self.currentY -= 1
            self.life += 1
            return True
        
        return False

    
    def Limpiar(self):
        permit = True
        UP = True

        while self.life < 1000:
            if self.room.isDirty(self.currentX,self.currentY):
                self.room.Clean(self.currentX,self.currentY)
                self.puntos+=1
                self.life+=1
            
            if self.currentX == 0:
                if self.goUP() == False:
                    self.goRight()
            
            if (self.currentY % 2 == 0):
                if self.goRight() == False:
                    self.goDown()
                continue

            if (self.currentY % 2 == 1 and self.currentX != 1):
                self.goLeft()
                continue

            self.goDown()
                

                
        print("Limpiado: " + str(self.puntos))
        print("Vida restante: " + str(1000 - self.life))
        self.room.tablero[self.currentX][self.currentY]=10
            




