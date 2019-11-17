from tablero import * 
from aEstrella import * 

start = Position(1,1)
end = Position(11,11)

tablero = Tablero(15,15,start, end)
tablero.CreateObstacles(50)
tablero.Print()

aestrella = Path(end,start,tablero)
aestrella.SearchExit() 

print()

aestrella.tablero.Print()