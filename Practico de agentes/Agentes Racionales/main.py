from enviroment import *
from aspiradora import *

habitacion = Enviroment(30,30)
habitacion.CreateDirt(50)

agente = Aspiradora(3,4,habitacion)

agente.room.Print()

agente.Limpiar()

agente.room.Print()

