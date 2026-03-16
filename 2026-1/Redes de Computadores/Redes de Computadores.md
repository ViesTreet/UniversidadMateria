# Ch1: Computer networks & internet
### tabla de contenido

1. [[### Internet vista con tuercas y tornillos |Internet visto con tuercas y tornillos]]
2. 
## Introducción
### Internet vista con tuercas y tornillos
![[Pasted image 20260302115726.png]]
**Millones de dispositivos computacionales conectados donde **
+ Host: final del sistema
+ Corriendo aplicaciones en los bordes del internet
![[Pasted image 20260302115901.png]]
**Switch de paquetes : paquetes (trozos de paquetes)**
* Routers y switcher
![[Pasted image 20260302115910.png]]
**Canales de comunicación **
+ Fibra, cobre , radio, satélite, etc.
+ Tasa de transmisión: ancho de banda
![[Pasted image 20260302120034.png]]
**Redes**
* Colección de dispositivos, routes y conexiones, administrada por una organización.
![[Pasted image 20260302115516.png]]
**El Internet es la red de redes**
* Son ISPs interconectados
**Protocolos esta en todos lados**
* Control de envió y recepción de mensajes
* HTTP, Streaming, Skype, etc..
**Estándares del Internet**
* RFC: solicitud de comentarios
* IETF: Ingenieros de fuerza de tarea del internet
### Internet con vista a los servicios
**Infraestructura que provee servicios para aplicaciones**
* web, Streaming, Multimedia, Correo, etc..
**Provee de una interfaz de programación para aplicaciones distribuidas**
* "Hooks", nos permite enviar y recibir aplicaciones para conectarnos y usar los medios de transporte del Internet
* Provee opciones de servicios, análogos a servicio postal
### ¿ Que es un protocolo?
Usado por computadores donde los protocolos manejan todo el Internet

*Los protocolos definen el formato, orden de los mensajes enviados y recibidos entre entidades de redes, y acciones tomadas en transmisión de mensajes, recibirlo.*
![[Pasted image 20260302123105.png]]
## Network edge
Podemos referirnos a ellos como **host** y estos se dividirían en dos categorías **Cliente** y **Servidores** 
+ Cliente: suelen ser maquinas comunes, computadores, celulares, etc.
+ Servidores: Suelen ser maquinas potentes o data centers.
#### Acceso a la red
Para conectarnos a la red y usamos usualmente un router el cual se conecta con los ISPs locales, estos "routers de bordes" nos permiten conectarnos con el exterior y saltar entre islas de redes
![[Pasted image 20260306102214.png]]
###### Acceso desde casa
Hay dos maneras de conectarse al Internet desde casa que predominan, que son DSL(Linea digital de suscripción) y cable.
**DSL**
Los DSL usan los cables de teléfonos preexistentes, estos se conectan mediante un modem, y llegan a la compañía de telecomunicaciones y mediante un multiplexor(DSLAM) que transforma los tonos de alta frecuencia en formato digital, entonces la compañía actúa también como un ISP
![[Pasted image 20260306103116.png]]Este sistema tiene una desventajas:
+ Conexión asimétrica (diferencia entre subida y bajada)
+ Peor rendimiento mientras mas lejos este físicamente el módem de la oficina central
**Cable**
Este sistema usa los cables de televisión preexistentes, cada cable soporta entre 500 y 5000 casas conectadas, usando un sistema de cable coaxial para alcanzar cada hogar esto a veces se llama HFC (fibra híbrida coaxial) .
En la casa para conectarse se usa un módem de cable que va conectado por  el puerto ethernet del computador el cual lleva finalmente a un CMTS similar al DSLAM en función, este tipo de conexión tiene una característica,  los datos se envían por un cable compartido por lo cual la red se puede saturar, también se necesita coordinar la transmisión para evitar colisiones.
+ Es asimétrico 
+ se puede sobrecargar el cable coaxial 
+ Puede haber colisión debido a que múltiples casas usan la misma red para conectarse
![[Pasted image 20260306104210.png]]
**Fibra a casa (FTTH)**
El concepto es tener un cable de fibra óptica que  sale de la oficina central y va hacia las casas. En el sistema PON, cada casa tiene un terminador óptico de red que se conecta a un splitter del vecindario,habitualmente menos de 100 casas, luego va a un OLT que realiza la transformación de señales.
![[Pasted image 20260306110307.png]]
**Acceso a la network mediante wireless**
conectamos el end system al router al cual llamaremos punto de acceso, los separamos  en dos 
1. **Wireless local area networks(WLANs):** Tipicamente alrededor de edificios, 802.11b/g/(WiFi): 11, 54, 450 mbps de transmisión
	![[Pasted image 20260315164302.png]]
2. **Wide-area cellular access networks:** Lo provee los operadores mobiles , 10Mbps, 4G y 5G
	![[Pasted image 20260315164340.png]]
**Red de empresas**
+ Compañías, universidades, etc.
+ Mix de cables, wireless, switches y  routers
+ Ethernet y wifi
	![[Pasted image 20260315164943.png]]
**Data center red**
Ancho de banda alto (10s to 100s gbps) conectando cientos o miles de servidores a si mismos y al Internet
### Host: envíos de paquetes de data
host tiene la función de enviar:
+ toman mensajes de la aplicación
+ rompe en pequeños en pequeños chunks, conoce como paquetes de un largo de L bits
+ transmite paquetes con un ratio de transmisión R
	+ transmisión de conexión, capacidad o ancho de banda
$$PacketTransmisionDelay = tiempoNecesarioParaTransmitirLBitsEnElEnlace = \frac{L(bits)}{R(bits/sec)}$$
### Enlace físicos
+ bit: propagado entre transmisor y receptor par
+ Enlace físico: lo que hay entre el transmisor y receptor
+ Medio guiado: señal propagada en un medio solido por ejemplo un cable
+ Medio no guiado: señal propagada libremente, ej Radio
+ Twisted pair(TP): dos cables de cobre entrelazados 
	+ categoría 5: 100 Mbps, 1 Gbps ethernet
	+ categoría 6: 10 Gbps ethernet
+ Coaxial cable: dos conductores de cables concentricos, bidireccional, tiene múltiple frecuencia de los canales del cable y con unos 100 Mbps por canal
+ Cables de fibra óptica: cable de cristal que llevan pulsos de luz, cada pulso es un bit, alta velocidad, bajo error ya que hay repetidores y es inmune a electromagnetismo 
+ Ondas de radio inalambrico: varias bandas del espectro electromagnético, no hay un cable físico, emisor "half-duplex", es afectado por el entorno
	+ Wireless LAN(WiFi)
	+ Wide-area(4G)
	+ Bluetooth
	+ Ondas de microondas 
	+ satélite
## Network core
+ malla de routers intercomunicados
+ packet-swithing: el servidor rompe los mensajes de las aplicaciones en paquetes
	+ la red envía paquetes de un router al otro a través de enlaces hasta su destino
**forwarding**
+ aka switching
+ acción local: mover los paquetes entrantes al enlace correcto para seguir su camino
**Routing**
+ Acción global: determinar la ruta que tomara el  paquete para llegar a su destino.
+ algoritmo de ruta.
### store and forward
+ tiene delay
+ paquetes enteros llegan al router y luego son transmitidos al siguiente enlace.
	![[Pasted image 20260315183102.png]]
### cola
La cola llega cuando el trabajo llega mas rápido de lo que puede ser trasladado.
![[Pasted image 20260315183239.png]]
Los paquetes se almacenaran el la cola pero si se sobrepasa la capacidad de buffer este generara  perdida de paquetes
### circuit switching
Es otra forma de transmitir datos, en donde se reserva un camino entre el origen y el destino para transmitir todo los datos, garantiza el rendimiento
#### Circuit switching: FDM and TPM
##### Frecuency Division Multiplexing
Dividimos la frecuencia depende la cantidad de usuarios, si tenemos 4 usuarios, a cada uno les corresponde el 25% del ancho de banda
##### Time division Multiplexing
Usamos el tiempo para dividir a los usuarios, los usuarios cuenta con el 100% de la red por un tiempo limitado, si fueran 10 segundos y 4 usuarios, serian 2,5 segundos por usuario
### Packet switching vs circuit switching
+ circuit switching: 10 usuarios  activos
+ Packet switching: podemos tener 35 usuarios activos, donde tenemos una probabilidad de 10 activos, este es mas eficiente.
	+ Se consume en base a si el usuario esta activo, consume solo cuando  esta en uso
	+ hay una posible congestión, lo que provocaría perdida de datos y retraso en los paquetes
### Estructura de la red de redes
![[Pasted image 20260309113117.png]]
tenemos que dividir la red para no colapsarla, usar proveedores locales que se conectan a proveedores mas grandes   
![[Pasted image 20260309113634.png]]
# Performance
### Perdida de paquetes 
los routers tienen bufers, cuando este buffer se llena esto genera perdida de los paquetes
![[Pasted image 20260309113836.png]]
esta es la formula paca calcular el delay del nodo, el delay de transmisión es distinto al de propagación
### Delay de paquetes en cola
![[Pasted image 20260309114429.png]]
es una manera de calcular el delay de la cola, si es cercano a 0, el delay es pequeño, si se acerca a 1 el delay es alto y si es mayor a 1 es infinito
### Comando traceroute 
nos permite ver el delay, envía 3 paquetes al destino
![[Pasted image 20260309115012.png]]
### Throughput 
es el ratio entre el que envía y el que recibe
![[Pasted image 20260309115714.png]]
aqui se genera un cuello de botella debido a que el mas pequeño pone el limite
## Seguridad
### Sniffing de paquetes
la tarjeta en modo promiscuo puede leer todos los paquetes, escucha todo
![[Pasted image 20260309121011.png]]
### Falsa identidad
IP spoofing: inyecta un paquete con un origen de direccion falso
![[Pasted image 20260309121031.png]]
### Denegación de servicios
sobrecargan el objetivo, mediante peticiones mal formadas
![[Pasted image 20260309121134.png]]
#### lineas de defensas
+ autenticacion
+ confidencialidad
+ chequeo de integridad
+ restriccion de acceso
+ firewall
### Capas de protocolos y servicios
Cada capa presenta un servicio
![[Pasted image 20260309122610.png]]
Usar el modelo de capas mejora la mantención. 
### stack de las capas de los protocolos
![[Pasted image 20260315184513.png]]
![[Pasted image 20260315184546.png]]
![[Pasted image 20260315184559.png]]
En resumen los protocolos tienen una estructura al enviarse "se arma de una manera", y al llegar al destino se "desarma" para extraer la información
# ch2: capa de aplicación
### Principios
#### paradigma cliente-servidor
+ **Host:** Ip estática, siempre hosteando y aveces en datacenters.
+ **Cliente:** Ip dinámica, se contacta con el servidor, no se comunica con otros clientes.
![[Pasted image 20260313125617.png]]
#### P2P Arquitectura
+ No siempre en servidor
+ Sistema arbitrario de fin del sistema
+ los pares hace peticiones de un servicio al otro y otro par lo retorna
+ cambia de ip 
![[Pasted image 20260313125633.png]]
![[Pasted image 20260313130725.png]]
#### Socket
El socket es un análogo a una puerta, es una comunicación donde se reciben y se envían mensajes, es como una comunicación entre dos extremos donde no se interactua con el exterior, tienen que estar en el mismo socket para comunicarse.
#### Proceso de direcciones
Para enviar algo necesitamos la ip y el puerto, esa son las direcciones en internet.
##### Protocolos
Existen protocolos abiertos y cerrados, donde los cerrados solo los propietarios saben como funciona 
![[Pasted image 20260313131731.png]]
#### Que necesitan los servicios?
+ Necesitan integridad de datos(algunos aceptan perdida)
+ Timing, necesitamos un delay bajo
+ throughput, muchas apps necesitan poco, bits/s
+ Seguridad, encriptacion de datos
![[Pasted image 20260313132232.png]]
#### Protocolos de servicio
1. TCP
	+ Garantiza la integridad de los datos
	+ El enviador no puede saturar al receptor
	+ tiene control de congestion
	+ se requiere un proceso entre el cliente y el receptor
	+ no provee: timing, throughput ni seguridad
2. UDP
	+ No garantiza la integridad de datos
	+ no provee. integridad, control de flujo, control de congestión, timing, throughput, seguridad o conexión.
![[Pasted image 20260313132602.png]]
![[Pasted image 20260313132959.png]]
#### Seguridad TCP
1. Vanilla TCP y UDP
	+ Esta todo en texto plano
	+ No es seguro
2. Transport Layer Security(TLS)
	+ Esta encriptado
	+ Integridad de datos
	+ Autenticacion por endpoint
### Web y HTTP
Para acceder a una web primero ponemos el nombre del host y luego el path
![[Pasted image 20260316114808.png]]
#### Vista de HTTP
http(hypertext transfer protocol) es un protocolo, que el cliente recibe y permite al navegador desplegar la pagina y el servidor envía este protocolo.
http usa TCP, o sea el cliente manda una petición por el puerto 80, es recibido y se cierra la conexión, este protocolo no guarda la información del cliente anterior.
#### Conexiones HTTP: dos tipos:
1. **No persistente HTTP**
	+ Se abre la conexión
	+ se envía el objeto
	+ se cierra la conexión
	+ ![[Pasted image 20260316115521.png]] ![[Pasted image 20260316115542.png]]
2. **HTTP persistente**
	+ se abre la conexión TCP
	+ Muchos objetos se envían por este socket
	+ se cierra la conexión

#### HTTP no persistente 

| Palabra | Definicion                                                                 |
| ------- | -------------------------------------------------------------------------- |
| RTT     | Tiempo en que un paquete pequeño viaja del cliente al servidor y de vuelta |
**HTTP response time(per object):**
+ Un RTT inicia la conexión TCP
+ Se crea una respuesta
+ Object/File transmisión
$$NonPersistentHTTPResponseTime = 2RTT+FileTransmisionTime$$
La conexiones no persistentes tienen unos problemas, requiere dos RTTs por objeto, el sistema crea overhead por cada conexión TCP y los navegadores ofrecen múltiples conexiones TCP de manera paralela, para referenciar objetos
#### HTTP persistente (HTTP1.1)
Se mantiene la conexión abierta por lo que no requerimos de muchas llamadas RTT para cargar los objetos, si no que se abre la conexión y se mantiene abierta para el envío de objetos, logrando reducir el tiempo de carga
#### Request mensajes
se hace en ASCII.
Formato general
![[Pasted image 20260316120925.png]]
Estas son peticiones request:
![[Pasted image 20260316121013.png]]
y existen varios códigos de respuestas:
![[Pasted image 20260316121052.png]]
#### Cookies
Muchos navegadores usan cookies para mantener el estado de una transacción, las cookies se mantienen el el host de usuario administrado por el navegador y también una parte se guarda en la base de datos el sitio web.
![[Pasted image 20260316122553.png]]
![[Pasted image 20260316123015.png]]
#### Web Caches
La web cache es una copia del html que se guarda de manera local en el navegador, este hace una consulta en el servidor para ver si la versión guardada sigue estando actualizada, se devuelve una cache al cliente(una versión guardada de manera local de la pagina).
También se conocen como proxy servers, actúa en ambos lados(cliente/servidor), el header dice como almacenar la cache
![[Pasted image 20260316124120.png]]
Reduce el tiempo de petición, la cache esta mas cerca del cliente, reduce el trafico en los enlaces de instituciones y el Internet esta lleno  de cache
![[Pasted image 20260316124335.png]]
