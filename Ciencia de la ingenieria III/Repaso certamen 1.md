#### Proceso de desarrollo

![[Pasted image 20251012222054.png]]
Podemos decir que existen 3 ramas principales, la de producción(desarrollo), la de gestión y la de calidad 
* La linea de producción se basa en el diseño del producto, todo lo que tiene que ver con el desarrollo.
* la linea de gestión tiene que ver con la planificación del producto, ver contratiempos y las relaciones. 
* y la linea de calidad tiene que ver con todo lo que sea posterior al producto, capacitación y mantención.
#### metodología
![[Pasted image 20251012222548.png]]
guía para realizar algo

##### fase de análisis
![[Pasted image 20251012222641.png]]
En esta fase nuestro objetivo es identificar y diseñar modelos e informes para tener un proceso ya planificado.
###### Ficha general
la ficha general tiene la siguiente estructura:
Nombre del caso de uso: nombre que le asignaremos a la acción que se realizara.
Código: código alfanumérico para nombrar el proceso.
Actores: personas que participaran en la acción.
Descripción: descripción del proceso que ocurrirá, habitualmente empieza con "se describe …", es mas técnico.
Resumen: pequeño contexto de lo que esta ocurriendo en lenguaje simple.
###### Curso normal de los eventos(paso a paso)
en esta podemos apreciar una tabla la cual al lado izquierdo veremos la acciones ocurridas entre los actores y a la derecha veremos lo que realiza el sistema, esta enumerado en el orden en que ocurren 
![[Pasted image 20251012223403.png]]

###### Excepciones
en este apartado pondremos en que paso puede ocurrir algo inesperado o que no se toma en cuenta en la tabla original.
![[Pasted image 20251012223529.png]]

###### Diagrama de casos de uso
aquí podremos realizar un pequeño diagrama de lo que ocurrió, tiene a los actores y la acción que ocurrió.
![[Pasted image 20251012223701.png]]

##### Identificación de requerimientos
En este apartado usaremos la tabla de curso normal para extraer los métodos que se usaran en el programa, en resumen buscamos las funciones del código y luego la diagramamos 
![[Pasted image 20251012223917.png]]

#### Modelo de clases

Esta es una manera un poco mas compleja de mostrar un objeto, en esta podremos ver un objeto con sus atributos y además los métodos o operaciones que pueden realizar 
![[Pasted image 20251012224217.png]]
Esto lo extraemos de la tabla de caso de uso y de esta también podemos extraer la tabla de sustantivos la cual tiene como función definir que dato es un atributo o una clase y además pueden tener observaciones 
![[Pasted image 20251012224354.png]]
#### Asociación entre clases 
existen 3 tipos: 
* Agregación/Composición: para saber si una relación es de este tipo podemos preguntarnos si esta clase pertenece a la otra
![[Pasted image 20251012224623.png]]

* Herencia: para saber si es una herencia podemos preguntarnos si una clase es un tipo de otra clase
![[Pasted image 20251012224753.png]]

* Simple: relación simple entre objetos.


#### Interfaces y modelado dinámico
##### Modelo interfaces
Describe la interfaz de usuario que se utilizara en el proceso según la planificación 
Sirve para validar el sistema.
![[Pasted image 20251012225116.png]]
##### Desarrollo de diagramas de interacción
Identificar los objetos que participaran en la acción.
Se analiza el requerimiento.
![[Pasted image 20251012225252.png]]

Tenemos 3 maneras de representar en este diagrama:
ClaseA: Nos estamos refiriendo a la clase
:ClaseA: Estamos representando un objeto de la clase A
obj1:ClaseA: estamos diciendo que hay un objeto llamado obj1 generado a partir de la claseA 
![[Pasted image 20251012225540.png]]
![[Pasted image 20251012225632.png]]
El primer mensaje no se enumera, el resto si, también podemos representar anidación usando x.1, x.2, etc.
![[Pasted image 20251012225730.png]]
también podemos usar condicionales, lo que indica que solo pasara a la otra clase siempre que se cumpla la condición.
![[Pasted image 20251012225854.png]]
Aquí tenemos condicionales mutuamente excluyentes. si no se cumple la condición del "a" pasara a la linea "b".
![[Pasted image 20251012230002.png]]
Aquí tenemos iteraciones para el diagrama, el proceso ocurrirá N cantidad de veces 
##### Diagrama de secuencia
Es una alternativa a los diagramas de colaboración antes vistos.
![[Pasted image 20251012230209.png]]
En esta la linea solida es el mensaje y la punteada la respuesta, esta en orden de arriba hacia abajo por eso no se usa enumeración.
![[Pasted image 20251012230312.png]]
Condicionales excluyentes en el diagrama de secuencia.
![[Pasted image 20251012230345.png]]
Mensajes con iteración.
![[Pasted image 20251012230412.png]]
Bloque de mensaje con iteración, todo dentro del bloque se iterara N cantidad de veces.
#### Patrones
Sistematización de guías para saber que objeto toma la responsabilidad de recibir el mensaje.
Su rol es definir los criterios de decisión para mantener lineada la red de clases.
![[Pasted image 20251012230643.png]]
![[Pasted image 20251012230948.png]]
![[Pasted image 20251012230958.png]]
![[Pasted image 20251012231010.png]]
![[Pasted image 20251012231020.png]]
![[Pasted image 20251012231030.png]]
![[Pasted image 20251012231041.png]]
![[Pasted image 20251012231051.png]]

#### POO

Cuando estamos hablando de POO, hablamos de un modelo que simula algo de la realidad.

Cuando hablamos de objetos nos estamos refiriendo a una instancia de una clase, es casi un sinónimo de objeto.

##### Instancia y signatura del método

Podemos comunicarnos con los objetos invocando sus métodos, los valores que requieren algunos métodos se denominan parámetros. Cuando hablamos de signatura del método nos referimos a la información que proporciona el parámetro por ejemplo "int distancia" se espera un entero que nos referiremos a distancia(el encabezado del método).

Se pueden crear muchos objetos(instancias múltiples) a partir de una clase.

##### Estado 

Los objetos tienen un estado. El estado esta representado por los valores almacenados en sus campos(atributos).

Todos los objetos de una misma clase tienen los mismos estados y métodos, pero cambian sus valores o a quien le afectan.

Los objetos pueden ser entregados como parámetros a otros objetos, estos objetos "padres" pueden usar las funciones de los objetos "hijos"
##### Código fuente

Es el código en java que define el comportamiento de la clase.

##### Valores de retorno

Los métodos pueden devolver información.
