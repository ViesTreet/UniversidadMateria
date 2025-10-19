# Datos bivariados 
### Tabla de registro de datos bivariados 
* Es una tabla de datos compuesta por 3 columnas, la primera siendo los datos en análisis y las otras dos siendo las variables X e Y.
*![[Pasted image 20251015233947.png]]

### Tabla de frecuencia bidimensional
* Es una tabla que resume los datos de dos variables simultáneamente, mostrando la frecuencia.

| Variable Y /Variable X                   | Categoría 1             | Categoría 2             | ... | Categoría n             | Total  fila (Frecuencia absoluta X) |
| ---------------------------------------- | ----------------------- | ----------------------- | --- | ----------------------- | ----------------------------------- |
| Categoría 1                              | *n11*                   | *n12*                   | ... | *n1p*                   | $\sum_{i=1}^{p} n_{1i}$             |
| Categoría 2                              | *n21*                   | *n22*                   | ... | ...                     | $\sum_{i=1}^{p} n_{2i}$             |
| ...                                      | ...                     | ...                     | ... | ...                     | ...                                 |
| Categoría k                              | *nk1*                   | *nk2*                   | ... | *nkp*                   | $\sum_{i=1}^{p} n_{ki}$             |
| Total columna (Frecuencia absoluta de Y) | $\sum_{i=1}^{p} n_{i1}$ | $\sum_{i=1}^{p} n_{i2}$ | ... | $\sum_{i=1}^{p} n_{ip}$ | *n*                                 |
### Frecuencia absoluta conjunta
* Pertenece a la clase conjunta de $X_iY_j$ .
* Se denota por $n_{ij}$
* La suma de todas las frecuencias absolutas conjuntas debería ser la cantidad de datos n, esto es:
$$\sum_{i=1}^p\sum_{j=1}^kn_{ij}=n$$ 

### Frecuencia relativa conjunta 
* Pertenece a la clase conjunta de $X_iY_j$ respecto a la cantidad de datos n.
* Se denota por $f_{ij}$ 
* la formula es:
$$f_{ij} = \frac{n_{ij}}{n}$$
* También la suma de las frecuencias relativas conjuntas debería ser 1.
	$$\sum_{i=1}^p\sum_{j=1}^kf_{ij}=1$$
* Si es expresada en porcentajes el resultado tiene que ser 100%.

#### Observaciones
1) Si ambos datos son de tipo cualitativo la tabla bidimensional se llama "tabla de contingencia".
2) La tabla bidimensional también puede ser representada por frecuencia relativa conjunta o frecuencia relativa conjunta porcentual
3) A partir de la distribuciones bidimensional se pueden obtener distribuciones unidimensionales como la tabla marginal y/o condicionada.

### Distribuciones marginales
Muestra como se distribuye una de las variables, ya sea X o Y, sin tomar en cuenta la otra.
![[Pasted image 20251016232305.png]]
![[Pasted image 20251016232315.png]]
### Distribuciones condicionadas
Muestra como se distribuye una de las variables X o Y en base a una condición dada.
![[Pasted image 20251016232439.png]]
las frecuencia se obtiene en base al total de datos de una variable.

### Covarianza
La covarianza se define como:
$$S_{xy}=\frac{\sum_{i=1}^n(x_i-\bar{X})(y_i-\bar{Y})}{n-1}$$

 - si $S_{xy}>0$ entonces ambas variables aumenta simultáneamente.
 - si $S_{xy}<0$ entonces una variable aumenta mientras la otra disminuye.
 -  si $S_{xy}=0$ entonces no hay una relación lineal entre ambas variables o la tendencia positiva y negativa se contrarrestan.
 
 #### Correlación
 se define como:
 $$r=\frac{S_{XY}}{S_XS_Y}$$
 El coeficiente de correlación de Pearson mide la asociación lineal entre dos variables, mide que tan bien se asocian en relación a una función lineal las variables. 
 ![[Pasted image 20251016233703.png]]
### Modelo de regresión lineal simple
Busca crear una función lineal que se ajuste lo mas posible a lo datos, buscando que los datos estén relativamente cerca de la función creada.
Se define como:
$$Y=\beta_1X+\beta_0$$
Para encontrar $\beta_1$:
$$\beta_1=\frac{\sum_{i=1}^nx_iy_i-n\bar{X}\bar{Y}}{\sum_{i=1}^nx_i^2-n\bar{X}^2}$$
para encontrar $\beta_0$:
$$\beta_0=\bar{Y}-\beta_1\bar{X}$$

# Probabilidades

Conteo de probabilidades:
### Caso 1 dos operaciones que no se pueden hacer juntas:
En caso de que una operaciones se pueda hacer $n_1$ formas y también de $n_2$ formas, pero no se pueden hacer juntas entonces la cantidad de operaciones que se pueden hacer serán $n_1+n_2$.
Si se realizan k operaciones distintas que no pueden llevarse a cabo de manera simultanea, solo se pueden llevar de $n_k$ formas, entonces la operación será: $n_1+n_2+...+n_k$

### Caso 2 dos operaciones que si por cada una se puede llevar acabo de otra forma:
Si una operación se puede realizar de $n_1$ formas y por cada una des estas se puede realizar también de $n_2$ forma, entonces la operación se podrá realizar de $n_1*n_2$ formas.

Similar a lo anterior teniendo en cuenta de k casos entonces: $n_1*n_2*...*n_k$

### Caso 3 permutación lineal, el caso donde el orden importa:
En este caso estamos hablando de cuando tratamos de ordenar algo y que un cambio en este orden significa una disposición distinta ABC , no será lo mismo que BAC, la permutación de n objetos distinto será n!:
$$n!=n*(n-1)*(n-2)...1$$

#### Permutaciones circulares:
El caso de las permutaciones circulares puede resultar un poco confuso, si por ejemplo tenemos a unas personas alrededor de una mesa redonda, se considerara que es una posición distinta cuando sus vecinos cambien, no cuando roten de silla. su formula es $(n-1)!$ 

#### Permutaciones con elementos repetidos:
Es un caso diferente, en este tomamos en cuenta cuando existen n objetos del tipo $n_1$ o de $n_2$ , la ecuación es:
$$\frac{n!}{n_1!*n_2!...n_k!}$$
##### Observaciones
==Hablamos de un experimento aleatorio cuando el resultado es incierto y se denota por $\epsilon$ y se denomina experimento determinístico cuando se sabe el resultado de antemano ==

==Una acción no es un experimento estadístico, lanzar una moneda es una acción, pero a nosotros nos interesa el resultado==


##### Espacio muestral:
Es el conjunto de todos los posibles resultados asociados a un experimento. Su símbolo es Ω, si el espacio muestral tiene numero finito de elementos o infinitos numerables entonces se dice que es discreto, si el intervalo son todos los puntos de algún intervalo real, entonces es continuo. 

Se denomina Evento o Suceso a cualquier subconjunto del espacio muestral y se denota por las letras mayúsculas.
![[Pasted image 20251018234530.png]]

En particular el propio espacio muestral es un evento y se llama suceso seguro, mientras que el conjunto vacío ϕ, es un evento y se llama suceso imposible.

Como los eventos son subconjuntos es posible aplicar la teoría de los conjuntos para obtener nuevos eventos, Si A y B son eventos, entonces también lo son A ∪ B, A ∩ B, $A^c$

Diremos que dos eventos A y B son mutuamente excluyentes o disjuntos si no pueden ocurrir juntos, es decir A ∩ B = ϕ.


#### Probabilidad:
Si $\Omega$ es un espacio muestral con n elementos, entonces la probabilidad de que un evento A ocurra será: 
$$P(A)=\frac{m}{n}$$
donde m es el numero de elementos de A.
Se conoce como regla de Laplace y solo funciona en un espacio finito equiprobable.

##### Preposición:
1) $P(\Omega)=1$
2) $P(A)\geq0$
3) $P(A\cup B)=P(A)+P(B)$ Si $A\cap B=\emptyset$
##### Teorema:
1) $P(\emptyset)=0$
2) $P(A^c)=1-P(A)$
3) $P(A\cup B)=P(A)+P(B)-P(A\cap B)$

#### Probabilidad Condicional:
Cuando se calcula la probabilidad de un evento A en particular y se tiene información de la ocurrencia de otro evento B, se le conoce como probabilidad condicional, se denota por $P(A|B)$ se lee "Probabilidad de A dado B" y se define como:
$$P(A|B)=\frac{P(A\cap B)}{P(B)}$$ con $P(B)\neq0$
![[Pasted image 20251019000741.png]]

#### Regla multiplicativa:
**Eventos independientes:**
$$P(A\cap B)=P(A)*P(B)$$
**Evento Dependiente:**
$$P(A\cap B)=P(A)*P(B|A)$$
$$P(A\cap B)=P(B)*P(A|B)$$![[Pasted image 20251019001029.png]]

#### Probabilidad total:
##### Teorema(probabilidad total)
Sea $A_1,A_2,...,A_n$ una partición de $\Omega$
1) $\cup_{i=1}^nA_i=\Omega$
2) $A_i\cap A_j=\emptyset$
Sea A otro evento de $\Omega$, entonces 
$$P(A)=\sum_{i=1}^nP(A|A_i)*P(A_i)$$
![[Pasted image 20251019001647.png]]

#### Teorema de Bayes:
Sea $A_1,A_2,...,A_n$ una partición de $\Omega$ y B otro evento de $\Omega$, entonces
$$P(A_i|B)=\frac{P(B|A_i)*P(A_i)}{\sum_{i=1}^nP(B|A_i)*P(A_i)}$$
![[Pasted image 20251019001925.png]]
