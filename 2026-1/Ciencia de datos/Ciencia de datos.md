# Procesamiento y visualización de datos
- variable: característica que se mide u observa en un conjunto de datos
- Observación: conjunto de valores que se registran para una variable en particular
- Distribución: característica o atributo que se mide
- Correlación: relación entre datos
## Tipo de datos
### Datos estructurados
![[Pasted image 20260306112856.png]]
### Datos no estructurados
![[Pasted image 20260306112927.png]]
### Datos semi-estructurados
## Fuente de datos
registro, sensores, bases de datos, investigaciones, métodos de consulta,etc. Todos esos son métodos para obtener datos.
![[Pasted image 20260306113213.png]]
## Procesamiento de datos
**Problema de datos:**
+ Valores faltantes o duplicados
+ Valores inconsistentes
+ Ruido
+ Errores de formato
**Técnica y herramientas:**
+ Eliminación y/o remplazo de datos faltantes
+ Corrección de formato
+ Eliminación de duplicados
![[Pasted image 20260306113651.png]]
## Medida de tendencia central y dispersión
![[Pasted image 20260306113755.png]]
 
![[Pasted image 20260306113851.png]]
![[Pasted image 20260306113947.png]]
![[Pasted image 20260306114537.png]]
![[Pasted image 20260306114941.png]]
![[Pasted image 20260306115255.png]]
![[Pasted image 20260306115310.png]]
![[Pasted image 20260306115459.png]]
![[Pasted image 20260306115840.png]]
![[Pasted image 20260306120007.png]]
![[Pasted image 20260306120021.png]]
### Histograma de imagen blanco y negro
Imaginemos un histograma de una imagen en blanco y negro donde :
$$h(t)=n_k$$
donde k es = {0,...,L} donde L es el nivel de grises y $n_k$ el numero de píxeles con valores de grises, también podemos normalizarlo por el valor de grises como 
$$p(k)=\frac{n_k}{n}$$
n = numero total de  pixeles en la imagen
### Distribución gausiana (normal)
Una variable X que sigue la distribución normal:
$$f(x)=\frac{1}{\sigma \sqrt{2\pi}}e^{-\frac{(x-\mu)²}{2\sigma²}}$$
## Feature selection for lineal regression
![[Pasted image 20260408111635.png]]
hay veces en las que necesitamos filtrar datos en bases a características 
![[Pasted image 20260408111730.png]]
![[Pasted image 20260408111757.png]]
![[Pasted image 20260408111851.png]]
En ridge buscamos reducir los betas, mientras que en lasso eliminamos características
### z-score
![[Pasted image 20260408111925.png]]
Evalúa el z-score que tanto efecto tiene sobre y, si el valor es alto significa que es relevante si es bajo no es importante
![[Pasted image 20260408112038.png]]
Cuando ajustamos el modelo, obtenemos el valor de prediccion, y cuando calulamos esta prediccion podemos calcular la varianza residual que nos dice cuanta varianza hay entre nuestro modelo con la predicción
![[Pasted image 20260408112211.png]]
cada beta nos dara un valor t

![[Pasted image 20260408112601.png]]
los valores cercanos a 0 se deberían ignorar, los positivos y negativos grandes son importantes
![[Pasted image 20260408112847.png]]
![[Pasted image 20260408112921.png]]
![[Pasted image 20260408113010.png]]
![[Pasted image 20260408113051.png]]
### Backward selection
![[Pasted image 20260408113154.png]]
### p-value
![[Pasted image 20260408113223.png]]
![[Pasted image 20260408113328.png]]
en la distribución t-student es como una gaussiana pero desconocemos la desviación estandar
![[Pasted image 20260408113547.png]]
![[Pasted image 20260408113613.png]]
### Forward step-wise selection
Es una combinación del backward y el forward
![[Pasted image 20260408113800.png]]
![[Pasted image 20260408113808.png]]
![[Pasted image 20260408113825.png]]
![[Pasted image 20260408113959.png]]
![[Pasted image 20260408114123.png]]
### Q-Q plot
![[Pasted image 20260408114328.png]]
![[Pasted image 20260408114406.png]]
![[Pasted image 20260408114419.png]]
![[Pasted image 20260408114546.png]]
![[Pasted image 20260408114555.png]]
![[Pasted image 20260408114606.png]]
![[Pasted image 20260408114615.png]]

