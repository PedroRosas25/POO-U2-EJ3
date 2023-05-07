from manejadorregistro import ManejadorRegistro
from registro import Registro
class MenuOpciones:
    def __init__(self):
        self.__opcion = None

    def opciones(self, lista):
        while self.__opcion != 4:
            print("Menu de opciones: ")
            print("1)- Mostrar para una variable el dia y hora de mayor y menor valor.")
            print("2)- Indicar temperatura promedio mensual por cada hora.")
            print("3)- Listar los valores de las tres variables para cada hora de un día dado.")
            print("4)- SALIR")
            self.__opcion = int(input("Seleccione una opcion: "))
            
            if self.__opcion == 1:
                variable = str(input("Ingrese una variable (Temperatura, Humedad o Presion): "))
                
                if variable == "Temperatura":
                    lista.menortemperatura()
                    lista.mayortemperatura()
                elif variable == "Humedad":
                    lista.menorhumedad()
                    lista.mayorhumedad()
                elif variable == "Presion":
                    lista.menorpresion()
                    lista.mayorpresion()
            
            elif self.__opcion == 2:
                print(lista.promediotemperatura())
            
            elif self.__opcion == 3:
                diadado = int(input("Ingrese un dia del mes (1,2 o 3): "))
                print(lista.listarvalores(diadado))   
            
            elif self.__opcion !=1 and self.__opcion !=2 and self.__opcion !=3 and self.__opcion !=4:
                print("Opcion no valida, ingrese otra opcion")

        print ('Usted salio del programa ')        