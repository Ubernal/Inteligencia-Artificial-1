from enviroment import *
from aspiradora import *

habitacion = Enviroment(64,64)
habitacion.CreateDirt(500)

agente = Aspiradora(3,4,habitacion)

agente.room.Print()

agente.Limpiar()

agente.room.Print()

