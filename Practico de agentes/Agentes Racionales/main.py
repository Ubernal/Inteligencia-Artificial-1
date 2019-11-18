from enviroment import *
from aspiradora import *

habitacion = Enviroment(5,5)
habitacion.CreateDirt(1)

agente = Aspiradora(3,4,habitacion)

agente.room.Print()

agente.Limpiar()

agente.room.Print()

