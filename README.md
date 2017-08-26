# python_b5m

El script main.py es un ejemplo de uso de la api.

El script mainUDP.py es una modificacion del ejemplo para iniciar 
un servidor UDP y permitir el control del dispositivo Arduino de
forma remota.

Para que el servidor acepte peticiones desde cualquier destino se debe setear la IP en "0.0.0.0". 

``` python mainUDP.py --ip "0.0.0.0" ```

optional arguments:
```
  -h, --help            show this help message and exit
  --port PORT, -p PORT  numero de puerto (default: 8081)
  --ip IP               ip de trabajo (default: 127.0.0.1)
```
