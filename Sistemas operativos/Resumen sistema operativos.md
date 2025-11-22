# Certamen 2
## Deadlocks
### Definiciones
en resumen un deadlock es cuando un grupo de hebras espera una acción que no va a ocurrir, donde cada hebra retiene el recurso y espera obtener un recurso obtenido por otra hebra 
![[Pasted image 20251122143005.png]]
### Deadlocks y starvation(inanición)
En la inanición una hebra queda detenida por un tiempo indefinido.
Un deadlock se considera una inanición especial ya que es imposible continuar.
En el caso de los RWLocks, puede producirse inanición de un lector, si llegan muchos escritores.
Existe la posibilidad de que a la hora de probar un programa no se presente ningún síntoma por eso es necesario tratar de diseñar el software aprueba de estos errores.
### Condiciones necesarias para el deadlock
1. Recursos limitados: número finito de hebras que comparten el acceso a recursos finitos.
2. No se pueden quitar: cuando una hebra adquiere el recurso no se le puede quitar externamente.
3. Espera y retención: Una hebra retiene un recurso, mientras que otro se desocupe.
4. Espera circular: Existe un conjunto de hebras que esperan y cada hebra espera que se libere un recurso que tiene otra hebra del grupo.
![[Pasted image 20251122145450.png]]
En resumen hay que ver que hay dos tipos distintos de flechas, de recurso a proceso es que este proceso tiene ese recurso, y de proceso a recurso es que este proceso espera este recurso, el deadlock ocurre cuando se forma un ciclo de espera, puede haber ciclos sin que sea deadlock siempre que no sean de espera.
![[Pasted image 20251122145853.png]]
### Prevención de deadlocks
#### 1. limitar el comportamiento
* Podemos proporcionar mas recursos
* Eliminar la retención y espera
* Eliminar la espera circular
#### 2. Pronosticar el futuro
* Se utiliza el algoritmo del banquero
	* Se determinan los valores máximos  disponibles en el sistema para cada recurso.
	* se realiza una comparación entre los recursos solicitados y los disponibles.
	* En el caso que se dispongan todos los recursos solicitados, se otorgan(se marcan como utilizados) para garantizar que la tarea se lleve a cabo
* No se presta mas dinero del que se dispone.
#### 3. Detección y reparación
* Podemos usar grafos para detectar deadlocks y repararlos
#### 4. Suponer que no van a ocurrir
### Detectar y recuperar: algoritmo Wait-for
Invocar un algoritmo que busca ciclos en el grafo, si detecta un ciclo, entonces hay un deadlock
![[Pasted image 20251122151100.png]]
### Algoritmo del banquero para evitar deadlocks
Una opción es esperar a que existan disponibles todos los recursos solicitados y cuando esta condición se cumpla asignarlos todos atómicamente.
Una hebra que comienza a ejecutarse establece los requerimientos máximos de recursos, pero los adquiere y libera de manera incremental.
La idea es intercalando recursos.
#### Estados de un proceso
1. Estado seguro: Existe al menos una secuencia segura de procesar el requerimiento, puede requerir espera.
2. Estado inseguro: Existe al menos una secuencia que lleven al deadlock
3. Deadlock: El sistema tiene al menos un deadlock

![[Pasted image 20251122152416.png]]
#### Ejemplo
![[Pasted image 20251122152907.png]]
cuando un proceso se pone en wait, guarda los recursos que se le asignaron antes de ponerse en ese estado.
y si vemos las paginas crecen en diagonal.
### Detección y recuperación de deadlocks
Algunos sistemas permiten los deadlocks ya que si son raros, no vale la pena gastar recursos en detectarlos.
Existen dos aproximaciones:
1. Proseguir sin el recurso: ya estará disponible.
2. Transacciones rollback/retry: revoca los recursos previamente dado y luego se vuelve a ejecutar, es mas lento.
## Scheduling

### Introducción 

- Scheduling: Decide qué tarea se ejecuta en el procesador durante un cambio de contexto.

- Se aplica en recursos escasos: CPU, disco, red, energía.

- Impacto real: 100ms extra en respuesta → pérdida del 5%-10% de clientes (Google/Amazon).

  

 ### Definiciones básicas

- Tarea (task/job): Requerimiento del usuario.

- Tiempo de respuesta: Tiempo percibido por el usuario para completar la tarea.

- Predictibilidad: Baja varianza en tiempos de respuesta.

- Throughput: Tasa de ejecución de tareas.

- Overhead: Costo de cambiar de tarea.

- Equidad: Igualdad en recursos.

- Starvation: Tarea no avanza por falta de recursos.

- Workload: Conjunto de tareas con tiempos de llegada y duración.

- Preemptive: Recursos pueden ser quitados.

- Conservador de trabajo: Nunca deja CPU ociosa si hay tareas.

  

 ### Criterios de optimización

- Maximizar utilización CPU.

- Maximizar throughput.

- Minimizar tiempo de espera.

- Minimizar tiempo de respuesta.

  

---

  

 ### Perfiles de carga

- CPU bound: Uso intensivo de CPU (ej: cálculos numéricos).

- I/O bound: Espera E/S (ej: descarga de archivo).

- Mixto: Compilador, navegador, juegos.

  

---

  

 ### Algoritmos de planificación en uniprocesador

 #### FIFO (First In First Out / FCFS)

- Procesos se ejecutan en orden de llegada.

- Ventajas: Bajo overhead, buen throughput, equidad.

- Desventaja: Problema con tareas largas seguidas de cortas → alto tiempo de espera promedio.

- Ejemplo:

  - Orden P1(24), P2(3), P3(3) → Espera promedio = 17.
![[Pasted image 20251122155124.png]]
  - Reordenado P2, P3, P1 → Espera promedio = 3.
![[Pasted image 20251122155153.png]]
  

 #### SJF (Shortest Job First)

- Elige la tarea con menor tiempo restante.

- Ideal para minimizar tiempo de respuesta.

- Problemas:

  - Starvation para tareas largas.

  - Difícil saber tiempo restante.

  - Más cambios de contexto si llegan muchas tareas cortas.

  

 #### Round Robin (RR)

- Cada tarea recibe un quantum (q).

- Si no termina en q → se interrumpe y pasa a la siguiente.
![[Pasted image 20251122155507.png]]
- Ventajas: Sin inanición.

- Elección de q:

  - q → 0 → alto overhead.

  - q → ∞ → se comporta como FIFO.

- RR es punto medio entre FIFO y SJF.

- Problemas:

  - Mal desempeño con cargas mixtas (CPU + I/O).

  - Tareas I/O bound pueden esperar demasiado.

  
![[Pasted image 20251122155646.png]]

---

  

 ### Equidad Min-Max

- Garantiza mínimo de recursos a cada proceso.

- Si todos son CPU bound → RR.

- Si hay I/O bound → se les da lo que necesitan, resto se reparte.

- Implementación: Elegir tarea con menor tiempo acumulado.

  

---

  

 ### Colas Multinivel con Retroalimentación (MFQ)

- Usado en sistemas modernos (Windows, Linux, MacOS).

- Objetivos:

  - Buen tiempo de respuesta (similar a SJF).

  - Bajo overhead (similar a FIFO).

  - Sin inanición (similar a RR).

- Características:

  - Varias colas con distinta prioridad y quantum.

  - Alta prioridad → quantum pequeño.

  - Tareas bajan prioridad si no terminan en su quantum.

  - Nivel más bajo puede ser FIFO o RR.

  - Operaciones de E/S pueden subir prioridad.
![[Pasted image 20251122155920.png]]
- Problemas:

  - No garantiza equidad Max-Min.

  - Puede haber inanición si muchas tareas I/O bound.

  - Solución: Ajuste dinámico de prioridades (ej: Linux).

  

---

  

 ### Planificación en multiprocesadores

- Desafíos:

  - ¿Cómo usar múltiples CPUs para tareas secuenciales?

  - ¿Cómo adaptar algoritmos para tareas paralelas?

- Estrategias:

  - MFQ por procesador (evita contención).
![[Pasted image 20251122160053.png]]
  - Afinidad de procesador: Mejora uso de caché.

  - Robo de tareas: CPUs ocupados pueden tomar tareas de otros (penalización posible).

  

---

  

 ### Casos prácticos

- Servidor Web:

  - Muchas hebras E/S bound → favorecer tareas cortas.

  - MFQ centralizado puede causar contención → mejor MFQ por CPU.
![[Pasted image 20251122160150.png]]
- Datacenter:

  - Balanceo de carga entre back-ends.

  - Afinidad para mantener coherencia.

  - Predicción para asignar recursos.
![[Pasted image 20251122160217.png]]
## Traducción de Direcciones (Memoria Virtual)

  

 ### Introducción

- Objetivo: Crear una realidad virtual para los programas.

- El programa no debe preocuparse por dónde está almacenado.

- Conversión de direcciones virtuales → físicas: concepto simple pero poderoso.

- Separa espacio de direcciones físicas del espacio virtual.

  

---

  

 ### ¿Qué puede hacer el SO con memoria virtual?

- Aislar procesos: Protección de espacios de memoria.

- Comunicación entre procesos: Compartir memoria de forma transparente.

- Compartir código: Reduce huella de memoria.

- Inicialización parcial: Ejecutar sin cargar todo en memoria.

- Asignación dinámica: Expandir espacios de forma transparente.

- Manejo de caché: Coloreo de páginas.

- E/S eficiente: Transferencias seguras.

- Archivos memory-mapped: Mapear archivos al espacio de direcciones.

- Checkpoint & restart: Reanudar tras falla.

- Migración de procesos: Balanceo de carga.

- Control de flujo: Seguridad adicional.

- Memoria compartida distribuida: Sistemas paralelos.

  

---

  

 ### Objetivos de la traducción de direcciones

- Protección: No toda memoria accesible por todos.

- Compartir memoria: Reduce presión del recurso.

- Ubicación flexible: Procesos en cualquier parte.

- Dispersión: Regiones dinámicas.

- Eficiencia: Conversión rápida (cada instrucción).

- Tablas compactas: Bajo overhead.

- Portabilidad: Independencia de arquitectura.

  

---

  

 ### Métodos de traducción

  

 #### Base y Límite

- Dos registros: `base` y `bound`.

- Direcciones virtuales comienzan en 0; físicas = base + offset.

- Ventajas: Protección general.

- Desventajas: Difícil compartir memoria.

![[Pasted image 20251122161209.png]]  

 #### Segmentación

- Vector de pares (base, bound) → múltiples segmentos.

- Cada segmento contiguo en espacio virtual, disperso en físico.

- Permisos por segmento.

- Falla de segmentación: Referencia fuera de segmento.

- Compartir segmentos entre procesos.

- Copy on Write (CoW):

  - Fork copia tabla de segmentos.
- Se copia la tabla de segmentos al hijo. 
- Se marcan los segmentos del padre y el hijo como readonly (solo lectura). -
- Se activa el proceso hijo recién creado. Se retorna desde fork en el padre.
- Si el padre o el hijo intentan modificar datos en sus segmentos, se genera un trap en el kernel. En este caso, señaliza al kernel que haga una copia del segmento para el proceso que desea escribir, al retornar el control.
  - Marca readonly; si se escribe → trap → copia real.
![[Pasted image 20251122161517.png]]
- Zero on Reference:

  - Limpia memoria bajo demanda.

  - Permite iniciar procesos con heap/stack en 0.

- Limitaciones de la segmentación:

  - Overhead por muchos segmentos.

  - Fragmentación externa → compactación.

  

 #### Paginación

- Memoria en frames fijos.

- Conversión mediante tabla de páginas.

- Espacio virtual continuo, físico disperso.

- Mapa de bits para frames libres.
![[Pasted image 20251122161728.png]]
- Carga bajo demanda:

  - Páginas inválidas → trap → carga → marcar válida.

- Core Map: Registra qué procesos usan cada frame.

- Limitaciones:

  - Tabla proporcional a memoria virtual.

  - Fragmentación interna si frames grandes.

  

---

  

 ### Traducciones multinivel

- Reemplaza tablas por árboles.

- Ventajas:

  - Asignación eficiente (mapa de bits).

  - Transferencias disco eficientes.

  - Conversión rápida.

  - Búsqueda inversa eficiente (Core Map).

  - Granularidad en permisos.

- Implementaciones:

  - Segmentación paginada.
![[Pasted image 20251122161952.png]]
  - Paginación multinivel.

  - Segmentación paginada multinivel (x86).

  
![[Pasted image 20251122162017.png]]
---

  

 ### Eficiencia: TLB (Translation Lookaside Buffer)
![[Pasted image 20251122162116.png]]
- Caché en hardware para traducciones recientes.

- Entrada TLB: {Página virtual, Frame físico, Permisos}.

- TLB hit: Traducción rápida.

- TLB miss: Conversión completa.
![[Pasted image 20251122162205.png]]
- Costo:$Costo=Costo(TLB lookup)+Costo(conversion real)*(1-P(Hit))$
- Alta P(Hit) = eficiencia.  
## Sistemas de Archivos

 ### Introducción

- Objetivos del sistema de archivos:

  - Confiabilidad: Datos intactos incluso ante fallas.

  - Alta capacidad y bajo costo.

  - Alto desempeño: Acceso rápido.

  - Espacio de nombres: Organización clara.

  - Seguridad: Control de acceso.

- Persistencia:

  - RAM es volátil; almacenamiento no-volátil (HDD/SSD) más lento pero persistente.

  - Acceso por bloques (512B a 4KiB).

  - HDD: ~10ms vs RAM: ~10ns.

  

---

  

 ### Problemas de desempeño

- Archivos grandes con auto-guardado:

  - Desempeño bajo: Reescribir completo por cambios pequeños.

  - Corrupción: Fallo durante escritura → inconsistencia.

  - Pérdida total: Si se sobrescribe original y falla.

  

---

  

 ### Abstracción del sistema de archivos

- Definición: Conjunto de datos (archivo) + nombres (directorios).

- Ejemplo: `/home/javier/Documentos/Filesystem.pdf`.

- Metadata: Tamaño, fecha, permisos.

- Datos = arreglo de bytes sin tipo (interpretación por el proceso).

  

---

  

 ### Directorios y volúmenes

- POSIX:

  - `/` raíz.

  - `.` directorio actual.

  - `..` padre.

  - `~` home usuario.

- Volumen:

  - Recurso lógico que agrupa almacenamiento físico.

  - Puede ser un disco, partición o conjunto de discos.

- Montaje:

  - Volumen debe montarse en un punto del sistema (`/media/disk-1`).

  ![[Pasted image 20251122162907.png]]

---

  

 ### Arquitectura del sistema de archivos
![[Pasted image 20251122162926.png]]
- Cache de bloques:

  - Mantiene bloques en RAM para optimizar lecturas/escrituras.

  - Prefetching: Leer anticipadamente bloques próximos.

- Dispositivos físicos:

  - HDD: Sectores 512B, seek ~12ms, rotación 7200RPM.

  - SSD: Celdas 128KB-512KB, borrado antes de escribir, desgaste limitado.

- Comparativa HDD vs SSD:

  - HDD: Mejor costo/capacidad, peor velocidad aleatoria.

  - SSD: Mejor velocidad, menor tolerancia a apagado prolongado.

  

---

  

 ### Archivos y directorios: desafíos
![[Pasted image 20251122163059.png]]
- Rendimiento: Independiente del medio físico.

- Flexibilidad: Diferentes tamaños, tipos, dueños.

- Persistencia: Datos y metadatos consistentes.

- Confiabilidad: Mantener datos ante fallas.

  

---

  

 ### Implementación

- Directorios: Mapean nombres a bloques.

- Índices: Árboles que relacionan nombres con bloques físicos.

- Mapas de espacio libre: Bitmap para bloques disponibles.

- Heurísticas de localidad: Minimizar seek entre datos y metadatos.

  

---

  

 ### POSIX: inodos
![[Pasted image 20251122163214.png]]
- Bloques especiales para metadatos.
- En POSIX, los bloques que contienen metadatos de archivos son llamados inodes, estos son bloques convencionales que el sistema de archivo reserva para esta función.
- Funcionalidades:

  - Lectura secuencial y aleatoria.

  - Soporte para archivos grandes.

  - Metadata: permisos, dueño, fecha.

  

---

  

 ### Comparativa de sistemas
![[Pasted image 20251122163315.png]]
- FAT:

  - Lista enlazada de clusters.

  - Ventajas: Simple, compatible.

  - Desventajas: Fragmentación, acceso aleatorio lento, sin journaling.
![[Pasted image 20251122163419.png]]
![[Pasted image 20251122163436.png]]
- EXT3/EXT4:

  - Tabla de inodos.

  - Punteros directos (12), indirectos simples/dobles/triples.

  - Soporta archivos sparse.

  - Bitmap para espacio libre.

  - Heurísticas: grupos de bloques para optimizar localidad.
  - Cada archivo está representado en el Sistema de Archivos como un árbol, lo que permite una búsqueda eficiente de bloques.
  - Cada nodo en el árbol tiene un alto grado: Minimiza las búsquedas. Con un tamaño de 4KB, un bloque indirecto apunta a 1024 bloques. 
  - Estructura fija: Los primeros 12 punteros siempre apuntan a los primeros 12 bloques. 
  - Soporta archivos poco densos (sparse), es decir, archivos que contienen espacios vacíos sin datos. Por ejemplo un archivo puede contener solo bloques directos y un bloque indirecto triple al final sin solicitar bloques para sus posiciones intermedias.
  ![[Pasted image 20251122163500.png]]
![[Pasted image 20251122163909.png]]
![[Pasted image 20251122163918.png]]
![[Pasted image 20251122163931.png]]
![[Pasted image 20251122163953.png]]
---

  

 ### Disponibilidad y redundancia

- Problemas:

  - Fallas eléctricas → inconsistencia.

  - Fallas físicas → pérdida de datos.

- Soluciones:

  - Transacciones: Propiedades ACID (Atomicity, Consistency, Isolation, Durability).

  - Redundancia: Replicación en múltiples dispositivos.
![[Pasted image 20251122164047.png]]
- Técnicas:

  - Códigos de corrección de errores:Estrategia útil para detectar y corregir errores menores en la transferencia y almacenamiento de datos. Al transferir datos para almacenarlos en el discos se agregan bits de redundancia adicional. Estos bits permiten corregir en forma transparente un error, o en casos graves detectar que se produjo un error. Normalmente los errores varían de un sector por cada $10^{14}$ a $10^{16}$ bits

  - Re-mapeo de sectores dañados:Tanto en discos mecánicos como en los de estado sólido se consideran sectores de repuesto. Al detectar fallas en un sector, el controlador intenta re-asignar el sector dañado. En discos de estado sólido puede realizarse de manera transparente al incluir celdas adicionales

- MTTF y CAFR: Métricas de confiabilidad.
![[Pasted image 20251122164330.png]]
- SMART: Monitoreo preventivo.

  

---

  

 ### RAID

- Objetivo: Redundancia y disponibilidad.

- Niveles:

  - RAID 0: Sin redundancia, solo mejora rendimiento.
![[Pasted image 20251122164407.png]]
  - RAID 1: Espejo, redundancia total, capacidad = 50%.
![[Pasted image 20251122164417.png]]
  - RAID 5: Paridad rotada, requiere ≥3 discos, capacidad = (n-1).
![[Pasted image 20251122164428.png]]
![[Pasted image 20251122164505.png]]

  - RAID 6: Doble paridad, tolera 2 fallas, ≥4 discos.
![[Pasted image 20251122164516.png]]
  - RAID 10: Combina RAID 0 + RAID 1.
![[Pasted image 20251122164527.png]]
  - RAID 50: Combina RAID 5 + RAID 0.
![[Pasted image 20251122164545.png]]
- RAID + Spare: Disco de repuesto para reconstrucción automática.

  

---

  ## Caché y Memoria Virtual

  

 ### Introducción a las memorias caché

- Objetivo: Mejorar el desempeño mediante jerarquías de memoria.

- Basado en localidad temporal (datos usados recientemente) y localidad espacial (datos cercanos).

- Ejemplos:

  - TLB: Traducción rápida de páginas.

  - Caché de direcciones virtuales y físicas.

- Desafíos del diseño:

  - Localizar copia cacheada.

  - Política de reemplazo.

  - Coherencia (mantener datos actualizados).

  

---

  

 ### Jerarquía de memoria (tiempos aproximados)

- L1 / TLB: 1 ns, 64 KB.

- L2: 4 ns, 256 KB.

- L3: 12 ns, 2 MB.

- DRAM local: 100 ns, 10 GB.

- DRAM datacenter: 100 µs, 100 TB.

- Disco local: 10 ms, 1 TB.

- Disco remoto: 200 ms, 1 EB.

  ![[Pasted image 20251122165332.png]]

---

  

 ### Operación de caché

- Cache hit: Dato encontrado en caché.

- Cache miss: Buscar en nivel inferior.

- Condición: `costo(hit) < costo(miss)`.

  

---

  

 ### Estrategias de búsqueda en caché

- Completamente asociativa:

  - Máxima flexibilidad.

  - Verifica toda la tabla (costoso).
![[Pasted image 20251122165424.png]]
- Directamente mapeada:

  - Cada dirección en un único lugar (hash).

  - Rápida pero menos flexible.
![[Pasted image 20251122165442.png]]
- Set associative:

  - Mezcla de ambas.

  - Búsquedas en paralelo.
![[Pasted image 20251122165459.png]]
  

---

  

 ### Políticas de reemplazo

- Random: Entrada aleatoria (rápido, impredecible).

- FIFO: Reemplaza la más antigua (mal rendimiento en ciclos).

- MIN (óptimo): Bloque usado más tarde (no implementable).

- LRU: Menos recientemente usado (considera localidad temporal).

- LFU: Menos frecuentemente usado (mantiene páginas populares).

  

---

  

 ### Efectividad y Working Set

- Working Set: Conjunto mínimo de páginas para buena tasa de hits.

- Thrashing: Caché muy pequeña → muchos misses.

- Tasa de hits aumenta con tamaño de caché hasta punto de inflexión.
![[Pasted image 20251122165700.png]]
  

---

  

 ### Paginación bajo demanda

- Permite usar más memoria que la física disponible.

- Fallo de página: SO carga página desde disco.

- Usado en:

  - Archivos mapeados en memoria:

    - Archivo tratado como segmento de memoria.

    - Ventajas:

      - Transparencia.

      - Zero copy I/O.

      - Pipelining.

      - IPC (compartir memoria entre procesos).
![[Pasted image 20251122165815.png]]
  - Memoria virtual:

    - Frames del proceso pueden copiarse al disco.
    - Todas los frames del proceso (codigo, heap, stack, bibliotecas, etc) pueden ser copiados al disco, como estrategia para liberar memoria física del sistema. Aquí es donde se pone lento el pc.
    - Flexibilidad: SO sigue funcionando aunque memoria física esté llena.

  

---

  

 ### Problemas y soluciones

- Thrashing:

  - Si suma de Working Sets ≥ memoria física.

  - Disco maneja ~100 fallos/s vs CPU 10^10 instrucciones/s.
![[Pasted image 20251122165951.png]]
- Auto-paginación:

  - Distribuye marcos equitativamente.

  - Evita que procesos monopolicen memoria.

- Swapping:

  - Desaloja procesos completos al disco para liberar memoria.

  - Impacta rendimiento global.

  

---

  

 ### Herramientas

- vmstat: Muestra estado de memoria virtual en sistemas POSIX.

  

---

  



