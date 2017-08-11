#!/usr/bin/python3
from ArduinoManager import ArduinoManager
#Funcion de callback opcional. Permite imprimir lo que se envia desde arduino.
def readerCallback(msg):
    print("readerCallback: " + str(msg) )

# Se incia el gestionador de las conexiones de arduino.
arduinoManager = ArduinoManager()

# Se consulta la lista de Arduinos conectados.
puertos = arduinoManager.buscarArduinosConectados();

# Se selecciona una puerto para entablar la comunicación
puertoSeleccionado = -1;
if len(puertos) == 0 :
	print("No se detectaron placas conectadas!");
	exit("No Arduino found - Exit")
elif len(puertos) == 1 :
	puertoSeleccionado=0;
else:
	# FIXME Seleccionar el puerto desde una lista!
	puertoSeleccionado=0;

#Se abre el manager del brazo robotico en el puerto seleccionado.
b5mManager = arduinoManager.abrirConeccionB5M(puertoSeleccionado)

# La suscripcion de una funcion de callback y el inicio del Reader para recibir
# la informacion enviada desde arduino es opcional.
b5mManager.subscribe(readerCallback)
b5mManager.initReader()

# Se envian comandos al Brazo.
while True:
    input("Press Enter to continue...")
    b5mManager.detener()
    b5mManager.grabar()
    b5mManager.mover(b5mManager.SERVO_CODO,2)
    b5mManager.mover(b5mManager.SERVO_HOMBRO,4)
    b5mManager.mover(b5mManager.SERVO_PINZA,8)
    b5mManager.detener()
    b5mManager.reproducir()
