import serial
import threading
import time

class B5mManager(object):
    SERVO_BASE = 0
    SERVO_HOMBRO = 1
    SERVO_CODO = 2
    SERVO_MUNIECA = 3
    SERVO_PINZA = 4

    def __init__(self,conexion):
        """ Clase B5mManager. Se encarga de manejar un brazo robotico Arduino
        con el control arduino_b5m (https://github.com/yoshKnight/arduino_b5m).
        :param conexion: conexion abierta con el dispositivo Arduino a 9600bps.
        """
        self.__conexion = conexion
        self.__callbacks = []
    def mover(self,servoId,delta):
        """
        :param servoId: numero del motor que se quiere girar.
        :param delta: magnitud del delta entero entre [-8 y 8].
        """
        command = "||mover&2&"+str(servoId)+"&"+str(delta)+"&||"
        self.__conexion.write(command.encode())
        time.sleep(0.4)
    def grabar(self):
        """

        """
        self.__conexion.write(b"||grabar&||")
        time.sleep(0.4)
    def reproducir(self):
        """
        """
        self.__conexion.write(b"||reproducir&||")
        time.sleep(0.4)
    def detener(self):
        """
        """
        self.__conexion.write(b"||detener&||")
        time.sleep(0.4)
    def subscribe(self, callback):
        """
        """
        self.__callbacks.append(callback)
    def unsubscribe(self, callback):
        """
        """
        self.__callbacks.remove(callback)
    def __notifyAll(self,msg):
        """
        """
        for fn in self.__callbacks:
            fn(msg)
    def initReader(self):
        """
        Inicia un thread para la recibir los datos que se envien desde la placa
        arduino.
        """
        t = threading.Thread(target=self.__reader)
        t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
        t.start()
    def __reader(self):
        """
        Esta funcion es la encargada de procesar los datos enviados desde
        Arduino. Cada linea es enviada a las funciones de callback que esten
        suscriptas.
        """
        print("__READER INITIATED")
        while True:
            msg = self.__conexion.readline()
            self.__notifyAll(str(msg))
