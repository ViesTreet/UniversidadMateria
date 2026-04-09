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
