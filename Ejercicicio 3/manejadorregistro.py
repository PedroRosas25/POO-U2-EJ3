import csv
import random
from registro import Registro
dias = 3
horas = 24      
     
class ManejadorRegistro:

    def __init__(self):
          self.__registros = [[Registro(None, None, None) for _ in range(horas)] for _ in range(dias)]
    def escribirarchivo(self):
            with open ('datosmetereologicos.csv', 'w') as archivo:
                for dia in range (1,dias+1):
                    for hora in range (0,horas):
                        temperatura = round(random.uniform(10, 30),2)
                        humedad = round (random.uniform(0,100),2)
                        presion = round (random.uniform(900,1000),2)
                        archivo.write(f"{dia}\t, {hora}\t, {temperatura}\t, {humedad}\t, {presion} \n")
                archivo.close()

    def cargar (self):
        archivo = open('datosmetereologicos.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            dia = int (fila[0])
            hora = int (fila [1])    
            temperatura = float(fila[2])
            humedad = float (fila[3])
            presion = float (fila[4])
            registro = Registro(temperatura, humedad, presion)
            self.__registros[dia-1][hora]= registro
    def menortemperatura (self):
        minimo = 10000
        minimodia= 0
        minimohora= 0
        for i in range (dias):
            for j in range (horas):
                if self.__registros[i-1][j].retornaTemperatura()< minimo:
                    minimo = self.__registros [i][j].retornaTemperatura()
                    minimodia = i+1
                    minimohora = j
        print (" El minimo es {} en el dia {} a la hora {} ".format(minimo, minimodia, minimohora))

    def mayortemperatura (self):
        maximo = -100
        maximodia= 0
        maximohora= 0
        for i in range (dias):
            for j in range (horas):
                if self.__registros[i][j].retornaTemperatura()> maximo:
                    maximo = self.__registros [i][j].retornaTemperatura()
                    maximodia = i+1
                    maximohora = j
        print (" El maximo es {} en el dia {} a la hora {} ".format(maximo, maximodia, maximohora))


    def menorhumedad(self):
        minimo = 10000
        minimodia= 0
        minimohora= 0
        for i in range (dias):
            for j in range (horas):
                if self.__registros[i][j].retornaHumedad()< minimo:
                    minimo = self.__registros [i][j].retornaHumedad()
                    minimodia = i+1
                    minimohora = j
        print (" El minimo es {} en el dia {} a la hora {} ".format(minimo, minimodia, minimohora))
    def mayorhumedad(self):
        maximo = -100
        maximodia= 0
        maximohora= 0
        for i in range (dias):
            for j in range (horas):
                if self.__registros[i][j].retornaHumedad()> maximo:
                    maximo = self.__registros [i][j].retornaHumedad()
                    maximodia = i+1
                    maximohora = j
        print (" El maximo es {} en el dia {} a la hora {} ".format(maximo, maximodia, maximohora))

    def menorpresion(self):
        minimo = 10000
        minimodia= 0
        minimohora= 0
        for i in range (dias):
            for j in range (horas):
                if self.__registros[i][j].retornaPresion()< minimo:
                    minimo = self.__registros [i][j].retornaPresion()
                    minimodia = i+1
                    minimohora = j
        print (" El minimo es {} en el dia {} a la hora {} ".format(minimo, minimodia, minimohora))

    def mayorpresion(self):
        maximo = -100
        maximodia= 0
        maximohora= 0
        for i in range (dias):
            for j in range (horas):
                if self.__registros[i][j].retornaPresion()> maximo:
                    maximo = self.__registros [i][j].retornaPresion()
                    maximodia = i+1
                    maximohora = j
        print (" El maximo es {} en el dia {} a la hora {} ".format(maximo, maximodia, maximohora))

    def promediotemperatura(self):
        for j in range (horas):
            acum=0
            for i in range (dias):
                acum+= self.__registros[i][j].retornaTemperatura()
            print ("La temperatura promedio de la hora {} en el mes es de: {:.2f}".format(j,acum/dias))    

    def listarvalores(self, diadado):
        print ("Valores registrados del dia: {}".format(diadado))
        print("DIA:---{}---".format(diadado))
        print ("Hora\tTemperatura\tHumedad\t\tPresion")
        for j in range(horas):
            print("{}\t{}\t\t{}\t\t{}".format(j,self.__registros[diadado-1][j].retornaTemperatura(),self.__registros[diadado-1][j].retornaHumedad(),self.__registros[diadado-1][j].retornaPresion()))
            


