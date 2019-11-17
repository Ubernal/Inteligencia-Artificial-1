import random

class Aspiradora:
    def __init__(self, startX, startY, room):
        self.room = room
        self.currentX = startX
        self.currentY = startY
        self.room.tablero[startX][startY] = 5
        self.puntos = 0
        self.life = 0

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

    def Limpiar(self):
        permit = True
        UP = True

        while self.life < 1000:
            if self.room.isDirty(self.currentX, self.currentY):
                self.room.Clean(self.currentX, self.currentY)
                self.puntos += 1
                self.life += 1
            
            direction = random.randint(0,3)
            if direction == 0:
                self.goRight()
            elif direction == 1:
                self.goLeft()
            elif direction == 2:
                self.goDown()
            elif direction == 3:
                self.goUP()

        print("Limpiado: " + str(self.puntos))
        print("Vida restante: " + str(1000 - self.life))
        self.room.tablero[self.currentX][self.currentY]=10
