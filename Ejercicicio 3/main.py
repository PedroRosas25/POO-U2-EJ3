from manejadorregistro import ManejadorRegistro as MR
from menu import MenuOpciones

def test():
    controlador = MR()
    controlador.escribirarchivo()
    print ('ARCHIVO CARGADO ')
    controlador.cargar()
    print ('LISTA CARGADA')
    menu = MenuOpciones()
    menu.opciones(controlador)

if __name__ == '__main__':
    test()
