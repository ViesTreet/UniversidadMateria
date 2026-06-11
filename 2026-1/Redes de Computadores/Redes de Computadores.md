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
## Principios
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
## Web y HTTP
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
En la actualidad las web caches no son del todo necesarias debido   a que la mayoría de paginas son dinámicas(con backend) y que tenemos altas velocidades de red
## Email, SMTP, IMAP
#### Email
![[Pasted image 20260323112105.png]]
**Tiene 3 componentes mayores**
+ User agents
+ Mail servers:
	+ MailBox:Contiene los mensajes entrantes para el usuario
	+ Message queue: cola de mensajes salientes que van a ser enviados
+ Simple mail transfer protocol(SMTP):
	+ Entre servidores de emails para enviar mensajes
		+ Cliente: envía al servidor de mails
		+ "Servidor": Recibiendo servidores de mails
#### SMTP RFC(5321)
usa TCP para garantizar la correcta transacción de información entre datos, se usa el puerto 25
+ Transferencia directa: Envía al servidor(actuando como cliente) para recibir al servidor
Hay 3 fases de la transferencia:
1. SMTP Handshaking 
2. SMTP transferencia de mensajes
3. SMTP cierre
Los comandos son en ASCII y las respuestas son con códigos y frases como en HTTP
![[Pasted image 20260323113030.png]]

![[Pasted image 20260323114134.png]]
![[Pasted image 20260323114422.png]]
#### Recuperando mails
El SMTP almacena y envía mensajes, es un servidor. Luego tenemos IMAP(Internet Mail Access Protocol) que nos permite acceder vía web a nuestros correos almacenados, podemos eliminar, almacenar,etc. 
Gmail, Outlook, Hotmail, etc nos dan una interfaz web para acceder a nuestros correos.
![[Pasted image 20260323115036.png]]
## DNS: Domain Name System
Nos permite acceder mas fácil a las paginas, ya que crea un enlace entre un nombre y una ip, de esta manera accedemos a usm.cl y no a 213.133.12.1.
Es una base de datos distribuida que esta implementada en las librerias de muchos servidores.
Esta en la capa de aplicación: host, DNS resuelve nombres.
+ Es el núcleo del Internet
+ es complejo en los limites de la  red
### DNS: Servicios y estructura
+ Hostnames a direcciones ip.
+ Alias de host.
+ Alias de servidores de mail.
+ Distribución de carga.
**No podemos tener un DNS centralizado debido a que si falla se cae internet, tiene un volumen de trafico alto, una base de datos distante y el mantenimiento**
Si pensamos en los DNS: 
+ Es una base  de datos distribuidas y homogenia
+ Maneja trillones de consultas
+ Organizado pero físicamente descentralizado
+ Aprueba de balas
### DNS: distribuido y jerárquico
![[Pasted image 20260323121752.png]]
### DNS: root name servers
Lo ideal es que a nivel top y autoritativo pueda resolver todas mis consultas, la ultima opción es consultar al root.
+ El internet no funciona sin el
+ DNSSEC provee seguridad(autenticación e integridad de mensajes)
ICANN(Internet Corporation for assigned Names and Numbers) Administra los root DNS
![[Pasted image 20260323122514.png]]
![[Pasted image 20260323124244.png]]
Los DNS locales suelen tener cache para acelerar la operación
![[Pasted image 20260323124331.png]]
![[Pasted image 20260323124346.png]]
![[Pasted image 20260323124413.png]]
![[Pasted image 20260323124443.png]]
## P2P aplicaciones
### Arquitectura
+ No siempre hay servidores activos.
+ Sistemas arbitrarios de comunicación.
+ Un sistema solícito y el otro retorna.
+ Hay un intercambio de direcciones de IP.
+ Tiene auto escalabilidad.
![[Pasted image 20260326145626.png]]
El tiempo que demoran los archivos en descargarse es el tiempo mayor entre el "servidor" subiendo y el "cliente" descargando.
![[Pasted image 20260326145735.png]]
Mientras más clientes hay más óptimo es el modelo de P2P sobre cliente-servidor.
### BitTorrent
![[Pasted image 20260326145922.png]]
la tecnología Torrent divide los archivos en chunks de 256kb, los peers reciben y envían chunks
+ tracker: trackea los peers que participan en torrent.
+ Torrent: grupo de peer que intercambian chunks del archivo.
Cuando uno entra a la red P2P no tiene chunks, pero se irán acumulando con el tiempo y con el tiempo uno también compartirá
+ churn: peers que vienen y se van 
### Peticiones y envío de chunks de archivos 
- Si hay carencia de ciertos chunks la red P2P automáticamente empezará a distribuir más estos chunks.
- Se usa un hash para todo el Torrent para verificar que no se está modificando él .torrent original, y además por cada chunk hay hash para verificar que no fue modificado.
+ Cada 30 segundos, aleatoriamente se selecciona otro peer, este compuesto se llama tit-for-tat
## Video streaming y distribución de contenido
+ CDN(content distribution network)
+ El streaming de video es lo que consume el mayor ancho de banda 
### Video
+ Los videos son secuencias de imágenes
+ Cada imagen son un array de píxeles
	+ cada pixel es representado por bits
+ Coding: usa redundancia sin y entre imágenes para disminuir la cantidad de bits
	+ Codificación espacial: Ve qué bits entre fotogramas no cambian y envían una instrucción para mantenerlos y de esa manera reducimos los bits que se envían
	+ Codificación temporal: Solo envían los cambios que se realizan entre dos frames, para no recargar toda la imagen.
	![[Pasted image 20260326152724.png]]
#### Codecs
+ CBR(constant Bit Rate): siempre se gastan los mismos bits
+ VBR(variable Bit Rate): con base en el movimiento de la imagen se gastan bits
![[Pasted image 20260326153144.png]]
Pero este es el mundo ideal, puesto que el internet no es constante
En la vida real existe el buffer que guarda bits de esa manera se compensa el delay
![[Pasted image 20260326153336.png]]
### Dash(Dynamic, Adaptive Streaming over HTTP)
1. Servidor
	+ Divide el video en chunks
	+ Cada chunks codifica en diferentes ratios
	+ diferentes rate de encoding se almacenan en distintos archivos
	+ los archivos se replican en varios nodos de CDN
	+ **Manifest file:** provee las direcciones de los diferentes chunks
2. Cliente
	+ Estima constantemente el ancho de banda entre cliente-servidor
	+ Consulta el manifiesto
	+ Elige un coding rate óptimo para su conexión
	![[Pasted image 20260326153851.png]]
### CDN
+ Realiza copias del contenido en los nodos CDN
+ El suscriptor solicita contenido y el servicio provee el manifiesto y la dirección cambiara en base al ancho de banda
# CH3: capa de transporte
## Servicio de la capa de transporte
Provee comunicación lógica entre aplicaciones, funciona de la siguiente manera
+ El emisor: rompe el mensaje en segmentos que pasan por la capa de red
+ El receptor: reensambla los segmentos para obtener el mensaje
existen 2 protocolos **TCP** y **UDP**
La acción sería más o menos a si:
![[Pasted image 20260330112553.png]]
![[Pasted image 20260330112607.png]]
### Los dos principales protocolos de internet
+ **TCP(Transmission Control Protocol):** 
	+ Entrega en orden y es confiable
	+ Control de congestion
	+ Control de flujo
	+ Setup de conexion
+ **UDP(User Datagram Protocol):**
	+ no es confiable, entrega desordenado
	+ Una extención basica del protocolo IP, e base al mejor esfuerzo
+ **Servicio no disponible:*
	+ Garantiza delay
	+ Garantiza ancho de banda
## Multiplexación y desmultiplexación
![[Pasted image 20260330113324.png]]
La multiplexación es una manera de juntar datos para su envío, imagínate  que en un celular tenemos muchas apps ejecutándose, cada una enviando información, pero solo disponemos de un cable para enviar información, entonces el computador realiza una multiplexación en la cual realiza lo siguiente:
+ Recoge  datos de múltiples sockets
+ Les agrega header
+ Y mete segmentos
Los datos se envian y listo, pero por ejemplo un servidor que recibe peticiones hace el proceso inverso la desmultiplexación:
+ Lee los header
+ Identifica que segmento le pertenece a que socket
+ Entrega la app correcta
### Como funciona la desmultiplexación
+ Cada host recibe el datagrama del IP
	+ Cada datagrama tiene como origen una IP y un destino que también es una IP
	+ Cada datagrama lleva un segmento de la capa de transporte
	+ Cada segmento tiene un origen y un puerto de destino
+ Los hosts usan direcciones IP y puertos para que el segmento llegue al socket correcto
![[Pasted image 20260330114156.png]]
### Desmultiplexación sin conexión
+ Cuando creamos un socket debemos especificar el puerto del host local
+ Cuando creamos un datagrama que  envia en UDP socket, debemos especificar
	+ IP de destino
	+ Puerto de destino
+ Cuando el host recibe la conexión UDP
	+ Checa el puerto del destino del segmento
	+ Dirige el segmento UDP al socket que tiene el puerto
+ IP/UDP datagramas con el mismo puerto de destino pero distintas IP y/o puerto, van a a ser dirigidos al mismo socket
![[Pasted image 20260330114614.png]]
### Conexión orientada a desmultiplexación
Los **TCP Socket** se identifican por 4 tuplas
+ IP de origen
+ Puerto de origen
+ IP de destino
+ Puerto de destino
El demux recibe los 4 valores y los dirige al socket correcto.
Los servidores pueden soportar simultáneos sockets TCP, cada socket identificado por esas 4 tuplas y cada socket asociado a distintos clientes
![[Pasted image 20260330114927.png]]
La multiplexación y desmultiplexación ocurre en todas las capas
Porque en cada capa:

- hay **múltiples “fuentes” de datos**
- se **combinan en una sola transmisión**
- y luego se **separan usando algún identificador**

Lo único que cambia es **qué campo se usa para separar**:

- Aplicación → procesos
- Transporte → puertos
- Red → protocolo (TCP/UDP)
- Enlace → tipo (EtherType)
## Transporte no orientado a conexión: UDP
## UDP
+ Un protocolo sin nada
+ El mejor esfuerzo
	+ Se pierde.
	+ Se puede  entregar en distinto orden.
+ Sin conexión
	+ NO hay handshake entre el emisor y el receptor
+ Pero tiene una utilidad, es más rápido, tiene un header pequeño, no hay RTT delay, es simple, no hay control de congestión por lo que usara todo el ancho de banda y puede funcionar con congestión
Cosas que usan UDP:
+ Streaming multimedia
+ DNS
+ SNMP
+ HTTP/3
Para poder mejorar UDP tenemos que hacerlo desde  la aplicación(HTTP/3):
+ añadir confiabilidad
+ añadir control de congestion
![[Pasted image 20260330120517.png]]![[Pasted image 20260330120530.png]]
### Header del segmento UDP
![[Pasted image 20260330120744.png]]
### UDP Checksum
![[Pasted image 20260330120922.png]]
el objetivo de esto es detectar errores
+ Emisor
	+ Trata el contenido en segmentos UDP como secuencia de integrales de 16 bits
	+ Checksum: se añade al segmento del contenido
	+ El checksum se pone en el campo del checksum
+ Receptor
	+ El computador recibe el segmento con el checksum
	+ checa que el cheksum recibido es el mismo que el calculado
		+ Si no es igual, hay error
		+ Si es igual, no hay errores, de momento
![[Pasted image 20260330121238.png]]
![[Pasted image 20260330121427.png]]
## Principio de la confiabilidad de la transferencia de datos
La complejidad de la confiablilidad de la data depende de un canal no confiable, estopuede probocar muchos problemas y para mas complejidad, el emisor y el receptor no conocen el estado del otro, por eso nace:
### Reliable data transfer protocol (rtd): interfaces
![[Pasted image 20260330122329.png]]
En la vida real esta comunicación funciona en ambos sentidos
### rdt1.0: transferencia confiable sobre un canal no confiable
Vamos a usar una maquina de estado finito entre el  emisor  y el receptor
![[Pasted image 20260330122652.png]]
En este formato imaginamos que no hay perdida de paquetes y no hay errores de bits, por lo que se envía la data de un emisor a un receptor
### rtd2.0: canal con errores de bits
imaginemos que un bit se da vuelta ya sea por interferencia en el cable, etc. Para recuperarlo usamos 
+ acknowledgements(ACKs): el emisor explícitamente envía un OK
+ negative acknowlegements(NAKs): el emisor envía un mensaje de que se envió mal
Entonces el emisor reenvía el mensaje 
**Sin errores**
![[Pasted image 20260406112710.png]]
**Con errores**
![[Pasted image 20260406112725.png]]
#### Debilidad de este modelo
Se puede corromper el ACK/NAK y como sabemos el emisor no sabe lo que pasa con el receptor por lo que se puede enviar data duplicada, cada emisor envía un pkt por cada respuesta a la cual le agrega un número lo cual puede duplicar pkt(ACK/NAK)
#### rtd2.1
![[Pasted image 20260406113502.png]]
![[Pasted image 20260406113518.png]]
El emisor envía un pkt en secuencias de 0 y 1, entonces el emisor verifica este número para ver si está repetido.
#### rtd2.2 un protocolo libre de NAK
+ Es lo mismo que rtd2.1 pero libre de NAK
+ El receptor envía un ACK, debe incluir explícitamente la secuencia de pkt
+ Los ACK duplicados son lo mismo que un NAK
![[Pasted image 20260406114211.png]]
### rtd3.0 canal con error y perdida
El emisor espera un tiempo razonable para esperar el ACK, si no responde un ACK, el emisor reenvía el paquete, pero la secuencia ya maneja duplicados, el receptor debe especificar el número de secuencia
![[Pasted image 20260406114508.png]]
![[Pasted image 20260406114537.png]]
Como vemos si el ACK se pierde el emisor lo vuelve a enviar
![[Pasted image 20260406114718.png]]
![[Pasted image 20260406114858.png]]
El protocolo es muy lento, por lo que se usa pipelining, en donde el emisor envía muchos paquetes los cuales están en espera de confirmación, el rango de secuencia se va a incrementar, hay un buffer entre el emisor y receptor
![[Pasted image 20260406115145.png]]
![[Pasted image 20260406115202.png]]
#### Go-Back-N: emisor
+ Una ventana es la cantidad de paquetes que están buenos
	+ k-bit secuencia en el header del paquete
![[Pasted image 20260406115649.png]]
+ **ACK acomulativos:** son todos los paquetes incluidos en la secuencia, cuando se recibe un ACK la ventan se mueve
+ el timer es para el paquete en vuelo más viejo
+ al haber timeout se envia el paquete n y todos los siguientes.
#### Go-Back-N: receptor
El receptor solo recibe paquetes en orden, si no lo están se ignoran o lo guarda en el buffer, el receptor solo debe recordar el último paquete correcto que se envió
![[Pasted image 20260406120404.png]]
![[Pasted image 20260409153046.png]]
### Selective repeat
Este es un tanto diferente al Go-Back-N, puesto que en este solo se reenvia el paquete faltante o dañado, por ejemplo si el emisor envía los paquetes {p1, p2 y p3} y el receptor recibe {p1 y p3}, confirma estos con un ACK y si el emisor no recibe un ACK en un tiempo dado por un paquete lo reenvía, como al emisor le falta un paquete intermedio guarda el p3 en el buffer esperando que llegue el p2, hay un número máximo de paquetes que pueden ser enviados antes de confirmar su recepción.
![[Pasted image 20260409153635.png]]
#### Parte 1: EMISOR (sender)

**Cuando llegan datos de arriba:*
- Si el número de secuencia está dentro de la ventana → **envía el paquete**
- No espera ACK inmediato → puede mandar varios seguidos

---

 Si hay timeout:
- Si el paquete **n no fue confirmado**:
    - Lo vuelve a enviar
    - Reinicia su temporizador

clave: **solo reenvía ese paquete**, no todos

---

 Cuando recibe un ACK:
- Marca el paquete como **recibido**
- Si ese paquete era el más antiguo sin confirmar:
    - **mueve la ventana hacia adelante**

Ejemplo:

- Enviados: 1,2,3,4
- Llega ACK de 1 → la ventana avanza
- Llega ACK de 2 → sigue avanzando

---

#### Parte 2: RECEPTOR (receiver)

 Cuando llega un paquete dentro de la ventana:
- Envía **ACK(n)**
- Si está fuera de orden:
    - lo guarda (buffer)
- Si está en orden:
    - lo entrega a la capa superior
    - entrega también los que tenía guardados en orden

---

 Si llega un paquete “viejo”:
- Ya lo había recibido antes
- Igual manda ACK(n) otra vez

esto ayuda si el ACK original se perdió

---

Si está fuera de todo rango:
- Lo ignora completamente

---

**La clave de todo esto**

Selective Repeat funciona porque:

- El receptor **acepta paquetes desordenados**
- El emisor **maneja cada paquete individualmente**
- Ambos usan **ventanas** para limitar el flujo
![[Pasted image 20260409154433.png]]
#### Intuición (lo importante de verdad)
Si la ventana es muy grande:
- Se “superpone” con números antiguos
- El receptor **no puede distinguir pasado vs presente**
Si la ventana es pequeña:
- Nunca confunde paquetes viejos con nuevos
---
#### Resumen corto
- Selective Repeat reutiliza números → peligro
- El receptor puede aceptar paquetes viejos por error
- Para evitarlo:
**Ventana ≤ mitad del espacio de secuencia**
![[Pasted image 20260409154805.png]]
### Causes/costs of congestion: insights
+ El throughput no puede exceder la capacidad
+ El delay aumenta
+ Las perdidas y retransmisiones disminuyen la efectividad del throughput
+ Los duplicados reducen la efectividad
+ La capacidad de subida puede limitar la velocidad de bajada
### Enfoque en el control de congestion
+ End-End congestion control
	+ No hay un feedback que enviar desde la red
+ La congestión se infiere a travez de la perdida de paquetes y el delay
+ Observar las perdidas y el delay, en eso se enfoca TCP
+ La red asiste al control de congestion
	+ Los routers envian un feedback al host para reducir un poco la carga
	+ Puede indicar el nivel de congestion
	+ TCP EN
## TCP control de congestion
### TCP congestion control: AIMD
**Enfoque:** el emisor puede reducir la tasa de envío si una congestión ocurre, empieza a aumentar en 1 los paquetes hasta que haya perdida, si hay perdida corta a la mitad el ratio de envío
![[Pasted image 20260413113223.png]]
### TCP AIMD: more
**Multiplicative decrease** detail: el ratio de envio se
+ Corta a la mitad si recibe un triple ACK
+ corta a 1 MMS (tamaño maximo de segmento) cuando detecta una perdida
Porque AIMD?
+ AIMD es distribucion, asincrona de algoritmo
+ optimiza la congestion
+ Estabiliza
### Detalles
* El TCP limita la transmision: $LastByteSent-LastByteAcked \leq cwnd$
* CWND se ajusta dinamica a la respuesta observada
### TCP empieza lento
El sistema envia 1MSS pero empieza a aumentar rápidamente
![[Pasted image 20260413113918.png]]
![[Pasted image 20260413113940.png]]
![[Pasted image 20260413114013.png]]
### TCP Cubic
![[Pasted image 20260413114158.png]]
Hay una mejor manera, mas eficiente que el TCP clásico, se recupera de manera mas rapido si hay una perdida, como vemos se descarga mucho mas con la manera cúbica, llega mas rapido al W maximo
![[Pasted image 20260413114513.png]]
Si llegamos a la ventana maxima, podemos incrementar la ventana, se es precavido cuando llegamos a la ventana $k$
![[Pasted image 20260413114652.png]]
se genera un cuello de botella en los routers
![[Pasted image 20260413114737.png]]
El objetivo es mantenerlo lo más lleno si desbordar 
### Delay basado en el control de congestion TCP
Entonces el delay se enfoca en:
+ $RTT_{min}$  de un canal no congestionado
![[Pasted image 20260413115104.png]]
Se trata de aumentar el throughput sin generar perdida y mantener un delay bajo
### Explicit congestion notification (ECN)
Se dedsplego un asistente de red que:
+ Hay dos bits en en header marcado por el router de la red que indica la congestion
+ El nivel de congestion llega al destino
+ El destinatario setea ECE bit en el ack para notificar que hay congestion
+ involves both IP (IP header ECN bit marking) and TCP (TCP header C,E bit marking)
![[Pasted image 20260413115452.png]]
![[Pasted image 20260413115525.png]]
Ambas conexiones deberian llegar a un acuerdo para ambos tener el mismo ancho de banda
![[Pasted image 20260413115632.png]]
### Sin justicia: la mayoría de apps en la red no son justas
**Fairness and UDP:**
+ La multimedia no usa comúnmente TCP
+ UDP envía a un ratio constante para tolerar solo pequeñas perdidas de paquetes
**Equidad de las conexiones paralelas TCP:**
+ Las aplicaciones pueden abrir conexiones paralelas entre dos host
+ ![[Pasted image 20260413120120.png]]
# Unidad 4: Data plane
Los segmentos son transportados a través de routers, mueven el datagrama de un puerto de origen a uno de destino
## Introducción
### las dos funciones principales de la capa de red
**forwarding:** Mueve el paquete de un router a otro router apropiado
**Routing:** determina la ruta que tomara el paquete al destino
### Plano de datos
+ **local,** funcion entre routers
+ determina como el datagrama llega al router por el puerto de entrada y es llevado al puerto de salida del router
+ **Networl-wide** logic
+ determina como el datagrama es enviado a travez de lo router, el camino que toma
+ Hay dos plano de datos:
### Plano de control por router(tradicional)
Cada componente de algoritmo en cada router interactúa con el plano de control
### Software-defined networking(SDN) control plane
Controladores remotos instalan tablas forwarding en los routers
### Modelo de servicio de red
+ Entrega garantizada para datagramas individuales
	+ garantiza el envio
	+ garantiza el envio en menos de 40 msec de delay
+ Pero para un flujo de datagramas:
	+ datagramas en orden
	+ garantiza un minimo de ancho de banda 
	+ restricciones en el cambio de inter-paquetes
### Modelo del mejor esfuerzo
![[Pasted image 20260427113420.png]]
+ Es un mecanismo simple y garantizo que la red haya sido desplegada de manera masiva
+ suficiente ancho de banda provee rendimiento en tiempo real
+ Replicación en la capa de aplicación distribuido por servicios
+ control de congestion elastico
## Que hay dentro de un router
![[Pasted image 20260427113501.png]]
### Introducción
hay puertos, un switcher de alta velocidad y un procesador de routing, por lo que el forwarding esta a nivel de hardware 
### Input port function
se recibe el bit, se entra a la capa de enlace y llega a un switching desentralizado:
+ mira el header y toma decisiones
+ El objetivo es procesar a la velocidad que llega
+ se puede formar una cola si los bits llegan mas rapido de lo que se procesan
+ hay dos maneras de hacer forwarding
	+ Basado en IP
	+ General basado en cualquier dato en el header
![[Pasted image 20260427113614.png]]
### Destino basado en forwarding
#### Match por el prefijo mas largo
Usa el prefijo más largo para hacer match con la dirección de 32 bits
Para hacer match se tiene que hacer rapido para eso usa TCAMs
![[Pasted image 20260427113853.png]]
vamos relevando bits hasta que uno encaje, no busca una precisión perfecta si no eficiencia, el que mas se parezca con menos bits relevados se elegirá, en el ejemplo 2 elegirá la interfaz 2, ya que mas bits coinciden, el prefijo mas largo.
##### 1. ¿Por qué usamos el "Longest Prefix Match" (LPM)?

El texto menciona que se verá más adelante, pero en términos de redes, se usa porque **las tablas de enrutamiento tienen entradas superpuestas**.

- A veces, un router tiene una ruta general (ej. una red grande) y una ruta más específica (ej. una subred dentro de esa red).

- El LPM permite que el router tenga flexibilidad: enviar la mayoría del tráfico a un destino general, pero poder "desviar" o tratar de forma distinta subconjuntos específicos de direcciones IP.


---

##### 2. TCAM (Ternary Content Addressable Memory)

Esta es la tecnología clave que permite que Internet funcione a la velocidad actual.

- **¿Qué es una memoria normal (RAM)?** Le das una **dirección** (índice) y te devuelve el **dato** almacenado ahí.
- **¿Qué es una TCAM?** Es una memoria de **"búsqueda por contenido"**. Tú no le das una dirección; tú le das el **dato** (la dirección IP de destino) y la TCAM busca en toda la tabla en paralelo para ver si coincide.
- **La característica "Ternaria":** Se llama "ternaria" porque, además de poder buscar `0` y `1`, admite un tercer estado: el **"Don't Care"** (representado por los asteriscos `*` en tu imagen anterior). Esto permite que el hardware compare bloques de bits ignorando las partes que no importan para la coincidencia.
---

##### 3. Rendimiento en un solo ciclo de reloj

Este es el beneficio más importante:

- **Escalabilidad:** En una búsqueda de software normal (como un algoritmo de búsqueda binaria o una tabla hash), a medida que tu tabla de enrutamiento crece, el tiempo de búsqueda aumenta (es $O(\log n)$ o $O(n)$).
- **Velocidad constante:** Con una TCAM, **no importa si tienes 10 entradas o 1 millón**; el hardware compara todas las entradas al mismo tiempo (en paralelo). Por lo tanto, el router encuentra la interfaz de salida en **un solo ciclo de reloj**.

##### 4. Caso de uso: Cisco Catalyst

El ejemplo de Cisco que mencionas ilustra que los switches/routers de grado empresarial utilizan este hardware especializado para manejar tablas de enrutamiento gigantescas (cerca de 1 millón de rutas) sin que la velocidad de procesamiento de paquetes disminuya, manteniendo la capacidad de línea (_wire speed_).
### Fabricaciónde switching
+ Transfiere paquete de un input a un output
+ **Switching rate:** es el ratio en que un paquete puede ser transferido del input al output
![[Pasted image 20260427114734.png]]
![[Pasted image 20260427114757.png]]
### Switching via memoria
**Primera generación de routers**
+ El  switching estaba a cargo de la CPU
+ los paquetes se copian en la memoria del sistema
+ la velocidad estaba limitada por el ancho de memoria
![[Pasted image 20260427114939.png]]
### Switching via bus
+ Los datagramas entrantes se redirigian a la salida mediante un bus
+ tenia limite en ancho de banda
![[Pasted image 20260427115119.png]]
### Switching via red interconectada
+ Clossbar, Clos network, entre otros inicalmente fueron desarrolladas para conectar procesadores en multiprocesadores
+ **Multistage switch:** $n*n$ switch de multiple fases en switch pequeños
+ **Explotando el paralelismo:** 
	+ Se fragmente el datagrama en entrada fijas de celdas
	+ Luego se reensambla el datagrama al salir
![[Pasted image 20260427115610.png]]
+ Se escala usando multiples planes de switching en paralelo
	+ Aumento de velocidad en base a paralelismo
![[Pasted image 20260427115745.png]]
### Cola de inputs en el puerto
+ Si el switch es lento de fabrica se puede formar una cola
	+ Genera delay, perdida de paquetes y overflow
+ **Head-of-the-line(HOL) blocking:** es un fenómeno crítico en redes que ocurre cuando el primer paquete en una cola impide que los paquetes que están detrás de él avancen, aunque las interfaces de salida de esos otros paquetes estén libres.
	Imagina que es una fila en el supermercado:
	- **Situación normal:** Todos los clientes en la fila van a la misma caja (interfaz de salida).
	
	- **HOL Blocking:** Imagina que el primer cliente de la fila tiene un problema con su pago (un paquete corrupto, una dirección de destino desconocida o simplemente un problema de procesamiento). Ese cliente se queda bloqueado en la caja. Aunque los 10 clientes detrás de él tengan sus productos listos y sus tarjetas pagadas, **no pueden avanzar** porque el primero está obstruyendo el paso.
### Cola de outputs en el puerto
+ **Buffering** es requerido cuando los datagramas llegan más rápido de lo que pueden ser despachados, esto puede provocar perdidas si es que se genera un overflow
+ **Disciplina del itinerario** Elige en la cola para la transmisión.
![[Pasted image 20260503134958.png]]
![[Pasted image 20260503135125.png]]
#### **1. Regla Tradicional (Basada en un solo flujo)**

Para maximizar la utilización del enlace, el buffer debe ser capaz de absorber las ráfagas de TCP durante su fase de _Additive Increase_:

- **Criterio:** $RTT \times C$
- **Lógica:** Evita que el enlace quede inactivo mientras la ventana de congestión de TCP se recupera tras una pérdida.

#### **2. Regla Moderna (Basada en $N$ flujos)**

En _backbones_ o routers con múltiples conexiones independientes, los flujos no están sincronizados. Esto permite reducir el tamaño del buffer sin perder eficiencia:

- **Criterio:** $\frac{RTT \times C}{\sqrt{N}}$
- **Impacto:** Permite construir routers con memorias más pequeñas y rápidas (SRAM en lugar de DRAM).

#### **3. Riesgos del "Over-buffering" (Bufferbloat)**

- **Delay Excesivo:** Buffers gigantescos aumentan el tiempo de encolado.
- **Apps en Tiempo Real:** Degradación crítica en voz sobre IP (VoIP) y streaming debido a la alta latencia.
- **Congestión:** Un buffer lleno oculta la congestión real, impidiendo que TCP ajuste su tasa de envío a tiempo.

#### **4. Principio de Diseño Moderno**
(Mantener el enlace saturado de tráfico útil, pero con la mínima cola posible).
### Gestión del buffer
+ **Drop:** cuál paquete va a ser agregado y cuál será dropeado cuando el buffer está lleno
	+ **tail drop:** dropear los paquetes entrantes
	+ **priority:** dropear en bases a una base de prioridad
+ **Marking:** cuales paquetes van a ser macados como señal de congestión
![[Pasted image 20260503140117.png]]
### Itinerario de paquetes: FCFS
+ **Itinerario de paquets:** decide cual paquete va a ser enviado al siguiente link
	+ El primero en llegar el primero en enviar
	+ Por prioridad
	+ round robin
	+ colas equitativas ponderadas
	+ ![[Pasted image 20260503140503.png]]
+ **FCFS:** Paquete transmitidos en orden de llegada a la salida del puerto
	+ Es como un FIFO(first in first out)
### políticas de itinerario: priority
+ el tráfico entrante es clasificado, en cola por clases 
	+ cualquier valor del header puede ser usado para clasificar
	+ ![[Pasted image 20260503140927.png]]
+ Envio de paquetes desde la prioridad mas alta en la cola en los paquetes del buffer
	+ FCFS sin prioridad de clases
	+ ![[Pasted image 20260503141035.png]]
### políticas de itinerario: round robin
+ el tráfico entrante es clasificado, en cola por clases 
	+ cualquier valor del header puede ser usado para clasificar
+ El servidor revisa cíclica y repetidamente las colas de clases, enviando un paquete completo de cada clase (si está disponible) por turnos
### políticas de itinerario: weighted fair queueing(WFQ)
+ Es un round robin generalizado
+ cada clase $i$, tiene un peso $w_i$ esto nos da una cantidad de peso en el servicio por cada ciclo: $\frac{w_i}{\sum_{j}w_j}$
+ Ancho de banda minimo garantizado(por clase de trafico)
+ ![[Pasted image 20260503141829.png]]
### Neutralidad de Red: Conceptos Clave

Se define como el principio de que los proveedores de servicios de internet (ISP) deben tratar todo el tráfico de datos por igual, sin discriminación.
#### **1. Las Tres Dimensiones**
- **Técnica:** Se implementa mediante el **packet scheduling** (planificación de paquetes) y el **buffer management** (gestión de colas). Define cómo el ISP reparte sus recursos.
- **Social/Económica:** Busca proteger la libre expresión y garantizar que las pequeñas _startups_ compitan en igualdad de condiciones con las grandes empresas.
- **Legal:** Se traduce en leyes y políticas que varían según cada país.
#### **2. Las 3 Reglas de Oro (Basadas en la FCC 2015)**
Para que un internet se considere "abierto", los ISP no pueden realizar estas tres acciones:
1. **No Blocking (Sin Bloqueo):** No pueden prohibir el acceso a contenido, aplicaciones o dispositivos legales.
2. **No Throttling (Sin Estrangulamiento):** No pueden ralentizar o degradar el tráfico de forma selectiva (por ejemplo, bajar la velocidad solo a los videos para favorecer otros servicios).
3. **No Paid Prioritization (Sin Priorización de Pago):** No pueden crear "carriles rápidos". Un ISP no puede cobrar a una empresa (como Netflix o Disney+) para que sus paquetes lleguen antes que los de los demás.
## IP: El protocolo del internet
### Capa de transporte: internet
![[Pasted image 20260503142335.png]]
### IP formato del datagrama
![[Pasted image 20260503142501.png]]
### Direcciones IP: introduccion
+ **Direccion IP:** identificado por 32 bits asociados con cada host o router
+ **Interface:** conexion entre host y router con un medio fisico
	+ Los routers tipicamente tienen muchas interfaces
	+ Los host suelen tener 2 interfaces (internet cableado, wireless 802.11(WiFi))
![[Pasted image 20260503142814.png]]
### Subnets
**Que es una subnet?**
interfaces de dispositivos que fisicamente pueden alcanzar otros dispositivos sin pasar por un router (Una oficina conectada por LAN)
**Las direcciones IP tienen estructuras:**
+ Parte de la subnet: los dispositivos en la misma subnet tiene un alto orden de bits
+ Parte del host: Los bits inferiores restantes
**Fórmula para definir subredes:** separar cada interfaz de su host o enrutador, creando «islas» de redes aisladas cada red aislada se denomina subred
![[Pasted image 20260503143457.png]]
### Direccionse IP: CIDR(Classless InterDomain Routing)
+ las particiones subnet de direcciones de un largo arbitrario
+ el formato de direcciones **a.b.c.d/x** el cual la **x** es la porcion de subnet.
![[Pasted image 20260503143717.png]]
### DHCP: Dynamic Host Configuration Protocol
el objetivo es obtener de manera dinamica una dirección IP para conectarse a la red
+ puede renovar su dirección de enlace mientras la esté utilizando
+ permite la reutilización de direcciones (solo mantiene la dirección mientras está conectado/activo)
+ compatibilidad con usuarios móviles que se unen a la red o la abandonan
#### El Proceso DORA
1. **Discover (Descubrimiento):**
    - El dispositivo (host) llega a la red y no tiene IP. Envía un mensaje de _broadcast_ (a todos) diciendo: _"¿Hay algún servidor DHCP por aquí? Necesito una dirección"_.
2. **Offer (Oferta):**
    - El servidor DHCP recibe el mensaje y le responde: _"Hola, tengo esta dirección IP libre para ti"_. Este paso y el anterior son opcionales en ciertos casos de renovación, pero estándar en conexiones nuevas.
3. **Request (Solicitud):**
    - El dispositivo acepta la oferta y dice formalmente: _"Ok, me gusta esa IP. Por favor, resérvamela"_.
4. **ACK (Agradecimiento/Confirmación):**
    - El servidor finaliza el proceso diciendo: _"Entendido. Aquí tienes tu IP, la máscara de red, el gateway y los DNS. Úsalos por un tiempo determinado"_.
### DHCP client-server scenario
Tipicamente el DHCP esta en el router sirivendo en la subnet
![[Pasted image 20260504223318.png]]
![[Pasted image 20260504223347.png]]
#### Los 4 Datos Fundamentales que entrega DHCP

1. **Dirección IP Asignada:** Tu identidad única dentro de la red local.
2. **Máscara de Red (Network Mask):** Indica qué parte de la dirección IP corresponde a la **red** y qué parte al **host** (dispositivo). Es vital para que el equipo sepa si un destino está en su misma red o debe buscarlo fuera.
3. **Primer Salto o Gateway (First-hop router):** La dirección IP del router. Es la "puerta de salida"; si quieres enviar datos a Google, tu PC se los entrega a esta dirección primero.
4. **Servidor DNS:** La dirección del servidor que traduce nombres (como google.com) a direcciones IP. Sin esto, tendrías que navegar escribiendo números en lugar de nombres.
![[Pasted image 20260504223708.png]]
![[Pasted image 20260504223732.png]]
![[Pasted image 20260504224334.png]]
Nosotros o una empresa compra una ip y con ella un rango por ejemplo la organización 0 tiene 200.23.16.0/23 direcciones lo cual es 
$$32-23 = 9$$
$$2⁹= 512$$
La empresa tiene 512 direcciones que puede asignar, eso equivale a este intervalo 200.23.16.1 - 200.23.17.254
![[Pasted image 20260504224828.png]]
![[Pasted image 20260504224916.png]]
### En resumen de esta seccion
+ tenemos al ICANN que esta alojado en 5 registros regionales que es el que asigna las ips
+ Las direcciones IPv4 se acabaron en 2011
+ hay una jerarquia de dominios
### NAT: network address translation
#### Qué es y cómo funciona NAT
- **IP Única hacia el Exterior:** Para el mundo exterior (Internet), todos los dispositivos de la red local comparten una única dirección IP pública (en tu ejemplo: `138.76.29.7`).
- **IPs Privadas Internas:** Dentro de la red local (LAN), cada dispositivo tiene su propia IP privada (rango `10.0.0/24`). Estas direcciones no son visibles ni alcanzables directamente desde Internet.
- **El Rol del Router NAT:** El router actúa como un traductor. Cuando un paquete sale de la red local, el router cambia la IP de origen privada por su IP pública.
---
#### Mecanismo de Puertos (La Clave)
Si todos usan la misma IP pública, ¿cómo sabe el router a quién entregarle la respuesta que viene de Internet? La respuesta está en los **números de puerto**:
1. **Salida:** Cada datagrama que sale de la red local lleva la misma IP pública de origen, pero el router le asigna un **número de puerto de origen único**.
2. **Tabla de Traducción NAT:** El router guarda una tabla donde anota: _"El puerto 5001 corresponde a la IP interna 10.0.0.2"_.
3. **Entrada:** Cuando llega un paquete desde Internet, el router mira el puerto de destino, consulta su tabla y redirige el paquete al dispositivo correcto dentro de la red local.
#### 1. Rangos de Direcciones Privadas

Existen tres prefijos reservados exclusivamente para redes locales. Estas direcciones **no son enrutables** en la Internet pública:

- **Clase A:** `10.0.0.0/8` (Desde 10.0.0.0 hasta 10.255.255.255). Ideal para redes muy grandes.
- **Clase B:** `172.16.0.0/12` (Desde 172.16.0.0 hasta 172.31.255.255).
- **Clase C:** `192.168.0.0/16` (Desde 192.168.0.0 hasta 192.168.255.255). El estándar en redes domésticas
#### 2. Ventajas del Espacio Privado + NAT
- **Economía de Recursos:** Solo necesitas contratar **una única dirección IP pública** con tu ISP para dar servicio a cientos de dispositivos. Esto mitigó el agotamiento de IPv4 por décadas.
- **Independencia y Flexibilidad:**
    - Puedes cambiar el direccionamiento de tus equipos internos (por ejemplo, de `10.0.0.x` a `192.168.x.x`) sin que el mundo exterior se entere.
    - Puedes cambiar de proveedor de Internet (ISP) y tu estructura de red interna permanecerá idéntica, facilitando la migración.
- **Seguridad por Oscuridad:** Los dispositivos internos son "invisibles" para el exterior. Un atacante en Internet no puede enviar un paquete directamente a la IP `10.0.0.4` de tu PC porque esa ruta no existe globalmente; el router actúa como un escudo natural.
![[Pasted image 20260504225727.png]]
### La Controversia de NAT
Para un análisis académico o técnico, debes considerar por qué muchos ingenieros de red lo consideran un "mal necesario":
- **Violación de Capas (Layer Violation):** Según el modelo OSI, un router debería trabajar solo hasta la **Capa 3 (Red)**. Sin embargo, NAT debe modificar los números de puerto, que pertenecen a la **Capa 4 (Transporte)**, rompiendo la independencia entre capas.
- **Fin del "End-to-End" (Extremo a Extremo):** El principio original de Internet dicta que los hosts deben comunicarse directamente. NAT se interpone en el camino, manipulando los paquetes y rompiendo la transparencia de la conexión.
- **Obstáculo para IPv6:** Muchos argumentan que NAT retrasó la adopción de IPv6, ya que permitió "estirar" la vida de IPv4 mucho más de lo previsto originalmente.
- **Problemas de Traversal (Atravesamiento):** Es difícil para un cliente externo iniciar una conexión con un servidor que está detrás de un NAT (por ejemplo, en juegos P2P o servidores web caseros), ya que el router no sabe a qué IP interna redirigir una solicitud entrante no solicitada.
---
##### ¿Por qué NAT es "aquí para quedarse"?
A pesar de las críticas, su adopción es masiva y estructural por razones pragmáticas:
- **Uso Universal:** Es el estándar absoluto en redes domésticas, corporativas y, crucialmente, en redes celulares **4G/5G** (donde se usa CGNAT o Carrier-Grade NAT debido a la enorme cantidad de dispositivos móviles).
- **Escalabilidad:** Permite que las instituciones crezcan internamente sin depender de la asignación de nuevas IPs públicas.
- **Seguridad Básica:** Proporciona una capa de ocultamiento de la red interna que es muy valorada en entornos institucionales.

### IPv6
![[Pasted image 20260505001144.png]]
como logramos apreciar el datagrama de IPv6 es diferenteal IPv4, no hay checksum para aumentar la velocidad, no hay fragmentación y no hay opciones.
![[Pasted image 20260505001432.png]]
carecemos de opciones pero contamos con un header mucho más simplificado.
#### El Problema de la Coexistencia
- **Incompatibilidad:** Un router que solo entiende IPv4 no puede procesar un paquete IPv6 nativo.
- **Actualización Gradual:** Dado que existen miles de millones de dispositivos, la migración es un proceso lento que requiere que ambos protocolos funcionen en la misma red simultáneamente.
---
##### Tunneling (Tunelización): La Solución "Paquete dentro de otro"
El **Tunneling** es la técnica principal para conectar "islas" de IPv6 a través de un océano de routers IPv4.
- **Mecanismo:** El datagrama IPv6 se encapsula completamente dentro del campo de datos (payload) de un datagrama IPv4.
- **Analogía:** Imagina que el paquete IPv6 es una carta que se mete dentro de un sobre con dirección IPv4 para que pueda viajar por el sistema postal antiguo.
- **El Proceso:**
    1. **Entrada al túnel:** El router IPv6 de origen toma el paquete IPv6 y le añade una cabecera IPv4.
    2. **Tránsito:** Los routers intermedios solo ven la cabecera IPv4 y mueven el paquete como si fuera tráfico normal.
    3. **Salida del túnel:** El router IPv6 de destino recibe el paquete IPv4, quita la cabecera externa ("desencapsula") y procesa el paquete IPv6 original.
---
###### resumen:

- **Uso Extenso:** Esta técnica de "packet within a packet" no es exclusiva de esta transición; se usa masivamente en redes móviles **4G/5G** para transportar datos del usuario y en redes **VPN**.
- **Dual Stack:** Aunque tu texto se centra en tunneling, la otra estrategia común es el _Dual Stack_, donde los routers corren ambos protocolos al mismo tiempo y eligen cuál usar según el destino.
- **Transparencia:** Para los dispositivos finales (los hosts), el túnel es invisible; ellos creen que están comunicándose por IPv6 nativo de extremo a extremo.
![[Pasted image 20260505002032.png]]
![[Pasted image 20260505002103.png]]
![[Pasted image 20260505002118.png]]
![[Pasted image 20260505002152.png]]
Como vemos la adopción de IPv6 ha sido sumamente lenta, 25 años y contando, es un de los problema de la ingenieria mas grande de la epoca moderna.
### Para el certamen
+ para saber cuantas redes hay en un ejercicio, necesitamos contar las líneas
## Generalized forwarding, SDN
### Generalized forwarding: match plus action
#### Abstracción "Match plus Action" (Coincidencia y Acción)
Todos los routers modernos funcionan bajo este concepto simplificado: el router mira el paquete que llega, busca una coincidencia en su tabla y ejecuta una instrucción.
##### 1. Ruteo Tradicional (Basado en el destino)
Es el modelo clásico que hemos visto hasta ahora.
- **Match:** El router solo mira la **dirección IP de destino** en el encabezado.
- **Action:** La única acción posible es **reenviar (forward)** el paquete por una interfaz específica hacia su destino.
##### 2. Ruteo Generalizado (El nuevo paradigma)
Aquí es donde la cosa se pone interesante. Ya no solo importa el destino, sino cualquier parte del paquete.
- **Match:** Se pueden evaluar **múltiples campos** del encabezado al mismo tiempo (IP de origen, IP de destino, números de puerto de la Capa 4, protocolo, etc.).
- **Action:** Las acciones son mucho más variadas y flexibles:
    - **Forward:** Reenviar a una interfaz.
    - **Drop:** Descartar el paquete (bloqueo/firewall).
    - **Copy:** Enviar una copia a otro lugar (para monitoreo o análisis).
    - **Modify:** Cambiar datos del encabezado (como hace NAT con los puertos e IPs).
    - **Log:** Registrar el paso del paquete para auditoría.

---
##### ¿Por qué es importante?
Este modelo de "ruteo generalizado" es el corazón de las **OpenFlow** y las **SDN (Software Defined Networks)**. Permite que un router se comporte como un firewall, un balanceador de carga o un dispositivo NAT, simplemente cambiando las reglas de su **Flow Table**.
![[Pasted image 20260505221835.png]]
### Abstraccion de la tabla Flow
+ **Flow:** definido por los header
+ **Generalized forwarding: simple** enrutador de paquetes siguiendo las reglas
	+ **match:** patron en los valores del header
	+ **action:** se puede: drop, forward, modify, matched packet or send to matched packet to controller
	+ **priority:** resolver patrones sobrepuestos 
	+ **counters:** contar bytes y paquetes
### OpenFlow
![[Pasted image 20260505222434.png]]
en esta imagen usamos los datos que usa para hacer match el modelo de OpenFlow
#### Ejemplo
![[Pasted image 20260505222555.png]]
![[Pasted image 20260505222611.png]]
### Abstraccion de OpenFlow
El **match+action** unifica distintos tipos de dispositivos
+ **Router**
	+ hace match por el prefijo mas largo
	+ y toma una accion para la salida
+ **Switch**
	+ hace match por la direccion MAC
	+ hace forward o flood
+ **Firewall**
	+ hace match por direccion ip y TCP/UDP numero de puerto
	+ puede denegar o aceptar
+ **NAT**
	+ hace match por direccion ip y puerto
	+ puede reescribir puerto y direccion IP
![[Pasted image 20260505223059.png]]
### Resumen
#### Abstracción "Match plus Action" (Reenvío Generalizado)
El reenvío generalizado rompe la rigidez del ruteo tradicional, permitiendo que los dispositivos de red (switches/routers) realicen operaciones complejas basadas en reglas programadas.
##### 1. Coincidencias en múltiples capas (Multi-layer Matching)
A diferencia del ruteo clásico que solo mira la IP de destino, aquí se pueden evaluar bits de cabeceras en múltiples niveles:
- **Capa de Enlace (L2):** Direcciones MAC, VLAN IDs.
- **Capa de Red (L3):** IPs de origen/destino, campos de protocolo (ICMP, IGMP).
- **Capa de Transporte (L4):** Números de puerto (TCP/UDP).
##### 2. Acciones Locales Flexibles
Una vez que un paquete coincide con una regla, el dispositivo puede ejecutar varias acciones:
- **Drop:** Bloquear el tráfico (función de Firewall).
- **Forward:** Enviar a una interfaz de salida (función de Switch/Router).
- **Modify:** Cambiar bits de la cabecera (función de NAT o reetiquetado de prioridad).
- **Send to Controller:** Enviar el paquete al "cerebro" de la red (controlador SDN) para que este decida qué hacer si no hay una regla establecida.
##### 3. Programabilidad de la Red
Este enfoque permite "programar" comportamientos en toda la red de manera centralizada:
- **Procesamiento por paquete:** Se puede definir qué le ocurre a cada flujo de datos específico.
- **Evolución técnica:** Sus raíces están en el _Active Networking_, pero hoy ha evolucionado hacia lenguajes de programación de alto nivel para redes, como **P4** (Programming Protocol-independent Packet Processors).
## Middleboxes
### ¿Qué es un Middlebox?
Es cualquier dispositivo intermedio en la ruta de datos que realiza funciones **distintas** a las de un router estándar (reenvío de paquetes basado en IP). Mientras que un router solo se preocupa por "hacia dónde va el paquete", un middlebox "mira" el contenido o manipula el flujo para otros fines.

---
#### Funciones Comunes de los Middleboxes
Como has visto en los temas anteriores, estas funciones se alejan del ruteo puro:
1. **NAT (Network Address Translation):** Modifica las direcciones IP y puertos para permitir el uso de IPs privadas.
2. **Firewalls:** Inspeccionan el tráfico para bloquear o permitir paquetes basándose en reglas de seguridad.
3. **Balanceadores de Carga (Load Balancers):** Distribuyen el tráfico entrante entre varios servidores para evitar saturaciones.
4. **IDS/IPS (Sistemas de Detección de Intrusos):** Analizan patrones de tráfico en busca de firmas de malware o ataques.
5. **Cachés de Aplicación:** Almacenan contenido web localmente para acelerar la entrega a los usuarios internos.
![[Pasted image 20260505223749.png]]
La gestión de red está sufriendo una transformación radical, moviéndose desde hardware rígido hacia soluciones flexibles basadas en software.
#### 1. Del Hardware Propietario al "Whitebox"
- **Antes:** Los middleboxes eran soluciones de hardware cerradas y propietarias (Cisco, Juniper, F5). Si querías una función nueva, tenías que comprar un equipo nuevo.
- **Ahora (Whitebox):** Se utiliza hardware estándar ("cajas blancas") que implementa **APIs abiertas**. El hardware es genérico; la inteligencia reside en el software.
- **Ventaja:** Esto permite una rápida innovación y diferenciación mediante código, sin depender de los ciclos de fabricación de hardware.
#### 2. SDN (Software Defined Networking)
- **Control Centralizado:** SDN propone un control (lógicamente) centralizado de toda la red.
- **Gestión en la Nube:** La configuración y gestión se realizan a menudo desde nubes públicas o privadas, permitiendo que un administrador cambie el comportamiento de miles de dispositivos con un solo script.
#### 3. NFV (Network Functions Virtualization)
- **Definición:** Es la virtualización de las funciones de red. En lugar de tener un firewall físico, corres una instancia de software que hace lo mismo.
- **Infraestructura:** Proporciona servicios programables sobre una base común de computación, almacenamiento y redes tipo "whitebox".
- **Relación con Match+Action:** NFV utiliza la abstracción de "coincidencia y acción" para definir cómo se procesan los paquetes de manera local pero programada globalmente.
![[Pasted image 20260505224145.png]]
![[Pasted image 20260505224212.png]]
### Principios arquitectonicos del internet
Este fragmento del **RFC 1958** define la filosofía fundamental que permitió el crecimiento de Internet. Aquí tienes el resumen ejecutivo:
#### Principios Arquitectónicos de Internet (RFC 1958)
La comunidad de Internet sostiene que más que una arquitectura rígida, existe una **tradición** basada en tres creencias pilares:
1. **El Objetivo es la Conectividad:** La prioridad absoluta de la red es permitir que los puntos se conecten entre sí. La herramienta para lograr esto es el **Protocolo IP**.
2. **Cintura Estrecha (Narrow Waist):** El protocolo IP actúa como el punto de unión central. Mientras que abajo puede haber muchas tecnologías físicas (Ethernet, WiFi, Fibra) y arriba muchas aplicaciones (Web, Email, Video), todas deben converger y "entenderse" a través de IP.
3. **Inteligencia de Extremo a Extremo (End-to-End):** La inteligencia y la complejidad deben residir en los **extremos** (en los hosts/dispositivos de los usuarios) y no dentro de la red.
    - **Red "tonta":** Los routers internos deben ser lo más simples posible, limitándose a mover paquetes.
    - **Extremos "listos":** El control de errores, la congestión y la lógica de las aplicaciones se gestionan en los dispositivos finales
---
**En resumen:** La red debe permanecer simple y dedicada a mover paquetes; la responsabilidad de que los datos lleguen correctamente y sin errores es de los dispositivos que se están comunicando.
![[Pasted image 20260505224648.png]]
![[Pasted image 20260505224711.png]]
# ch6: Link layer and LAN's
## Multiple access protocol
Hay dos tipos de conexion
+ point-to-point:
	+ punto a punto entre el switch del internet y el hotst
+ Broadcast(compartido por cable o medio)
	+ wiresless, 4g, lan, satelite, etc
Hay un unico canal compartido de broadcast, puede haber colision si llegan dos señales al mismo tiempo
### El ideal para multiple protocolos de acceso
**Dar:** multiples canales de acceso(MAC) con un ratio de R bps
1. Cuando un nodo quiere enviar algo envia un ratio R 
2. Cuando un nodo M quiere enviar datos , cada uno envia un ratio R/M
3. totalmente decentralizado
4. es simple
### MAC protocolo: taxonomia
Hay 3 clases:
+ Chanel partition:
	+ divide el canal en piezas pequeñas 
	+ estas piezas tienen un nodo para uso inclusivo
+ Random Access:
	+ El canal no esta dividido, permite colision
	+ se recupera de las colisiones
+ "taking turn":
	+ los nodos toman turnos, pero algunos nudos pueden tomar mas tiempo que otros
### Chanel partition MAC protocol: TDMA
**TDMA:** time division multiple access
+ cada canal en rondas
+ cada estacion obtiene un slot de largo limpio en cada ronda
+ los slots no usados van a inactiva
+ Ejemplo: 6 estaciones, 1,2 y 3 van a enviar paquetes, 4,5y6 van a inactivo
+ El expectro del canal lo divide en bandas de frecuencias
+ Cada estacion asigna una frecuencia de banda
![[Pasted image 20260608112848.png]]
### Random access protocol
Cuando un paquete tiene cosas que enviar:
+ transmite toda su rata a un ratio R
+ no hay cordinacion a priori
+ Dos canales pueden colisionar
+ El random access protocol especifica:
	+ Como detectar colisiones
	+ como recuperarse de colisiones
#### Slotted ALOHA
**Asume que:**
+ todos los frames tienen el mismo tamaño
+ los divide en un tiempo equitativo de tiempo
+ los nodos empiezan a transmitir solo en un slot
+ los nodos estan sincronizados
+ si dos nodos transmiten en un slot, detecta colision para todos
**La operacion:**
+ cuando  un nodo obtiene un nuevo frame, transmite en el proximo slot
	+ si no hay colision envia en el proximo slot
	+ si hay colision, se retransmite el frame en cada slot subsecuente, hasta tener una probabilidad p de exito
![[Pasted image 20260608113511.png]]
#### Eficiencia
Calculamos la eficiencia en base a las fracciones de slot correctos, por este medio la eficiencia es de solo 37% en el **Slotted ALOHA**
Pero en el **Pure ALOHA** que no tiene sinronización es de solo el 18%
#### CSMA(carrier sence multiple access)
+ Si el canal esta inactivo transmite toda la data
+ Si el canal esta ocupada no transmite
**CSMA/CD: CSMA con deteccion de colisiones**
+ las colisiones se detecta en un corto periodo de tiempo
+ la conexion colisionada es cancelada, reduciendo el uso del canal
+ la colision se detecta facil en cable pero wireless es complicado
![[Pasted image 20260608114203.png]]
Reduce la cantidad de tiempo gastado al abortar la conexion
##### Algoritmo CSMA/CD en ethernet
![[Pasted image 20260608114310.png]]
![[Pasted image 20260608114321.png]]
Es mas eficiente que aloha, simple barato y decentralizado
### Taking turn MAC protocol
**Channel partition:**
Es lo bueno cuando hay mucha carga, pero no tanto cuando la carga es baja
**Random Access:**
es bueno cuando hay baja carga pero no muy bueno cuando hay alta carga
**Taking Turn:**
Es lo mejor de los mundos

--- 
+ Crea como una cola para que cada nodo transmita su parte
+ Se usa en dispositivos tontos
+ considerar:
	+ saturación de la cola
	+ latencia
	+ un solo punto de fallo
**Transferencia de token**
+ Cada token pasa de un nodo al siguiente, en secuencia
![[Pasted image 20260608114901.png]]
![[Pasted image 20260608114952.png]]
![[Pasted image 20260608115016.png]]
Hay un canal de subida y otro de bajada
### Resumen
**Channel partition:** 
+ division en tiempo o en frecuencia
**Random Access:** 
+ ALOHA, S-ALOHA,CSMA,CSMA/CD
+ facil en cable dificil si es wireless
+ CSMA/CD : usado en cable
+ CSMA/CA:  usado en wireless
**Taking turn:**
+ cola del sitio central, pasa el token
+ Bluethoot,FDDI, anillo de token
## LANs
### MAC addresses
32 bits ip addresses
+ usado en la capa de conexion
MAC(o lan o fisico o internet) dirección:
+ Es usada localmente para darle una direccion o una interfaz a los usuarios conectados
+ Es de 48 bit la direccion mac y esta quemada en la NIC ROM
+ ej: 1A-2F-BB-76-09-AD
#### Direcciones MAC
cada interfaz LAN:
+ tiene 48 bits de MAC address
+ nos da un unica direccion de 32 bits
![[Pasted image 20260608120438.png]]
+ Las direcciones MAC estan administradas por IEEE
+ Los diseñaddores compran una porcion de direcciones MAC
+ El MAC es como el RUT y la IP es la direccion 
+ Se puede mover de una red lan a otra
### ARP: adrress resolution protocol
**Tabla ARP:** cada nado IP en LAN tiene una tabla
+ IP/MAC la dirección mapea algunos  nodos lan
+ TTL tiempo de vida antes de que la tabla sea olvidada
![[Pasted image 20260608120953.png]]
![[Pasted image 20260608121002.png]]
![[Pasted image 20260608121036.png]]
![[Pasted image 20260608121042.png]]
### Ruta desde otra subnet: direccion
![[Pasted image 20260608121227.png]]
Vamos a enviar desde A a B mediante R
+ conocemos la direccion IP de B
+ conocemos la dirección IP de R ya que es nuestra puerta de enlace
+ conocemos la MAC de R debido a que nos la da cuando consultamos con la IP usando ARP
Luego:
+ Creamos un IP datagrama con origen de A y destino de B
+ Creamos una capa  de conexion entre A y B usando un datagrama IP
	+  la direccion MAC de R es un frame de destino
![[Pasted image 20260608121958.png]]
por decir asi la direcion MAC de destino es la de la puerta de enlace del lado que es el emisor, ya que no podemos conocer las MAC de las otras subnet
![[Pasted image 20260608122658.png]]
![[Pasted image 20260608122724.png]]
![[Pasted image 20260608122806.png]]
### Ethernet
Es la tecnologia dominante en redes cableadas LAN
+ simple y barata
+ mantiene una velocidad 10 mbps - 400 gbps
+ un chip con multiples velocidades
#### Topologia
![[Pasted image 20260608123120.png]]
![[Pasted image 20260608123222.png]]
![[Pasted image 20260608123603.png]]
**Preamble:** 
+ Usado para sinclonizar al receptor a un ratio de reloj
**Dirección:**
+ 6 byte de de origen y de destino MAC
**Type:**
+ comun IP pero no  la unica
+ usado por los demultiplexores
**CRC:**
+ si error es detectado dropea el frame
#### Ethernet, no confiable y sin conexión
+ no hay handshake
+ no es confiable ya que no existe los Ack
+ el ethernet con protocolo MAC , no tiene slot CSMA/CD con backoff binario
![[Pasted image 20260608123853.png]]
#### Port-based vLANs
![[Pasted image 20260611150751.png]]

**VLAN(virtual local area network) :** si tuvieramos un unico broadcast tendriamos problemas de eficiencia, seguridad y privacidad, y tambien nos genera problemas administrativos. Por eso se crearon las VLANs, para crearlas tenemos switcher que tienen la capacidad de crear estas VLANs
![[Pasted image 20260611150822.png]]
En resumen agrupamos lans en unos puertos para que estos queden en una red VLAN aparte
+ Aislación del trafico: frames del 1 al 8 que tiene origenen alguno de estos solo pueden alcanzar desde el puerto 1 al 8, o sea que estan aislados, tambien podemos definirlo por MAC
+ Membresia dinamica: Los puertos pueden ser dinámicamente asignada atravez de las VLANs
+ Forwarding a travez de las VLANs: Es similar a como lo hacen los switches via routing
#### VLANs que abarcan varios switches
![[Pasted image 20260611151950.png]]
**Trunk port:** Lleva frames a travez de las VLANs por un medio fisico 
+ Los frames que se llevan a travez de las VLANs no pueden ser 802.1 estandar ya que requiere un header para saber llegar a la VLANs
+ 802.1 q añaden y remueven headers para que  puedan usar los trunk ports
![[Pasted image 20260611152047.png]]
## Link virtualization: MPLS
### Multiprotocol label switching (MPLS)
Nuestro objetivo es tener un forwarding de alta velocidad con routers con capacidad de MPLS usando un largo fijo de identificador
+ rapidamente usa el identificador de longitud fija
+ Usa un enfoque parecido a las circuitos virtuales
+ El datagrama sigue usando la IP
![[Pasted image 20260611153200.png]]
### Routers con capacidad de MPLS
+ tambien llamados "label switches"
+ Hacen forwarding en base a el valor del identificador no le importa la IP
+ **Flexibilidad :** puede tomar decisiones sin importar la IP, a esto se le llama ingenieria de trafico en donde podemos tomar decisiones sin importar la IP 
### MPLS vs Rutas IP
**IP routing:** Solo usa la dirección IP para redireccionar
**MPLS routing :** La direccion de destio se puede basar en el origenen y en el destino
+ Similar al routing generalizado
+ Puede rapidamente redireccionar en caso de fallo