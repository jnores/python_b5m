#!/usr/bin/python3
import socket
import argparse
from ArduinoManager import ArduinoManager

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 8108

#Funcion de callback opcional. Permite imprimir lo que se envia desde arduino.
def readerCallback(msg):
    print("readerCallback: " + str(msg) )

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--port','-p', type=int, default=DEFAULT_PORT,
                   help='numero de puerto (default: '+str(DEFAULT_PORT)+')')
parser.add_argument('--ip', default=DEFAULT_HOST,
                   help='ip de trabajo (default: '+str(DEFAULT_HOST)+')')

args = parser.parse_args()
print(args)


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
	puertoSeleccionado = 0;
else:
	# FIXME Seleccionar el puerto desde una lista!
	puertoSeleccionado = 0;

#Se abre el manager del brazo robotico en el puerto seleccionado.
b5mManager = arduinoManager.abrirConeccionB5M(puertoSeleccionado)

# La suscripcion de una funcion de callback y el inicio del Reader para recibir
# la informacion enviada desde arduino es opcional.
b5mManager.subscribe(readerCallback)
b5mManager.initReader()

# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print ('Socket creado')
except socket.error as msg :
    print ('Fallo creando socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    exit()


# Bind socket to local host and port
try:
    s.bind((args.ip, args.port))
except socket.error as msg:
    print ('Fallo asociando puerto. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    exit()

print ('Socket bind complete')

# Se envian comandos al Brazo.
while 1:
    data, addr = s.recvfrom(1024)
    print ('comando recibido: ',data)
    data = data.decode('utf8')
    accion, parametros = data.split('(')
    if accion == 'ROTAR':
        servo_id,delta = parametros.strip(')').split(',')
        b5mManager.mover(int(servo_id),int(delta))
