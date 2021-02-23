Antes de comenzar es necesario tener instaladas la imagen de la aplicación:

Middleware para calcular tiempo en colas de un servidor
Es una aplicación que une un software de generador de traza y un software de simulador de colas en un sólo todo.

Para compilar generator utiliza el siguiente comando:
docker build -f Dockerfile -t middle:tarea_1 .

Una vez construida la imagen haga:
docker run -ti middle:tarea_1 python3 middleware.py 1 1 1.5 2  ---------> para ejecuutar una prueba


Ejecutar aplicación:

python3 middleware.py <id_worker > <inter_arrival> <service_time> <distribution> > reporte1.txt

Ejemplo:
python3 middleware.py 1 1 1.5 2

Donde:
id_worker: es el número de trabajadores que se desea obtener (en este caso sólo es disponible 1)
inter_arrival: es el tiempo de interarrivo promedio de las peticiones
distribution: 1:Uniforme, 2:Poisson, y 3:Normal
service_time: es el tiempo promedio de servicio




