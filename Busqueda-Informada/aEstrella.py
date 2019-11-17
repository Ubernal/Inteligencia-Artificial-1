from Prioridad import Priority

class Position:
    def __init__(self,X,Y):
        self.X=X
        self.Y=Y

class Nodo:
    def __init__(self,pos,Padre):
        self.Position=pos
        self.Padre=Padre
        self.F=0


class Path:
    def __init__(self,end,start,tablero):
        self.end=end
        self.start=start
        self.tablero=tablero
        self.path=Priority()
        self.visited={}
    
    def FillPath(self, node):
        currentnode = node
        while currentnode != None:
            self.tablero.tablero[currentnode.Position.X][currentnode.Position.Y]=20
            currentnode = currentnode.Padre

        self.tablero.tablero[self.start.X][self.start.Y]=5
        self.tablero.tablero[self.end.X][self.end.Y]=10
            

    def g(self,position):
        disX = abs(self.start.X - position.X)
        disY = abs(self.start.Y - position.Y)
        return disX + disY
    
    def h(self,position):
        disX = abs(self.end.X - position.X)
        disY = abs(self.end.Y - position.Y)
        return disX + disY
    
    def f(self,position):
        return self.g(position)+self.h(position)

    def SearchExit(self):
        current = self.start
        currentNode = Nodo(current, None)

        while currentNode.Position.X != self.end.X or currentNode.Position.Y != self.end.Y:
            self.visited[str(currentNode.Position.X)+"+"+str(currentNode.Position.Y)]=True
            
            vecinos = self.tablero.Adyacentes(currentNode.Position)
            for vecino in vecinos:

                vecinoNode = Nodo(vecino,currentNode)
                vecinoNode.F = self.f(vecinoNode.Position)
                
                if str(vecinoNode.Position.X)+"+"+str(vecinoNode.Position.Y) in self.visited:
                    continue

                self.path.Enqueue(vecinoNode.F,vecinoNode)
            
            currentNode = self.path.Dequeue()
        
        self.FillPath(currentNode)
        
    
