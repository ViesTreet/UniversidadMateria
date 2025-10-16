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
