import serial,serial.tools.list_ports

from B5mManager import B5mManager


class ArduinoManager(object):
    def __init__(self):
        """Clase ArduinoManager. Gestiona los dispositivos Arduino Conectados.
        """
        self.__puertos=[]
    def buscarArduinosConectados(self):
        """
        Escanea los distintos puertos USB buscando los que tengan un dispositivo
        Arduino conectado y los registra en un arreglo de puertos.
        :return: arreglo de puertos con un arduino conectado.
        """
        self.__puertos=[]
        ports = list(serial.tools.list_ports.comports())
        print("Buscando Arduinos Conectados:")
        i=0;
        for p in ports:
            #Se verifica si es una placa arduino
            if "VID:PID=2341:0042" in p[0] \
            or "VID:PID=2341:0042" in p[1] \
            or "VID:PID=2341:0042" in p[2] :
                print(i, " - ", p , " [ES UN ARDUINO!]")
                self.__puertos.append(p)
                i += 1
        return self.__puertos
    def abrirConeccionB5M(self,puertoSeleccionado):
        """
        Abre una conexion con el arduino que esta conectado en el puerto
        seleccionado y, luego, crea un manejador del brazo robotico (B5mManager)
        para operar sobre dicha conexion.
        :param puertoSeleccionado: Posicion del puerto al que se desea conectar.
        :return: Instancia de B5mManager conectado al puerto seleccionado.
        """
        coneccion = serial.Serial(self.__puertos[puertoSeleccionado][0],9600)
        return B5mManager(coneccion)
