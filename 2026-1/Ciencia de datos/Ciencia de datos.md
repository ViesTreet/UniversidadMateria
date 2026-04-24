# Introducción a el aprendizaje estadístico(Libro) 
![[Pasted image 20260408154858.png]]
En este diagrama podemos ver que según el método que usemos hay algunos que son mas interpretables mientras que otros son mas flexibles.
## División por supervisación
Podemos dividir el machine learning en dos:
+ **Supervisado:** Nosotros le entregamos "alimentación" a la máquina para de esta manera explicarle que es lo que estamos buscando
+ **No supervisado:** El sistema trata de aprender sin un "profesor"
+ **Semi-supervisado:** Nosotros alimentamos a algoritmo, pero este decide ciertas cosas, como google photos cuando agrupa por persona
+ **Auto-supervisado:** En este el algoritmo trata de elegir la mejor opcion en base a una gran cantidad de data
	![[Pasted image 20260408165451.png]]
+ **Aprendizaje reforzado:** En este el sistema recibe una recompensa o un castigo dependiendo del resultado que tiene
	![[Pasted image 20260408165715.png]]

# Procesamiento y visualización de datos(Materia)
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

# Resumen certamen 1
![[todoDel1-7_page-0001.jpg]]

![[todoDel1-7_page-0002.jpg]]

![[todoDel1-7_page-0003.jpg]]

![[todoDel1-7_page-0004.jpg]]

![[todoDel1-7_page-0005.jpg]]

![[todoDel1-7_page-0006.jpg]]

![[todoDel1-7_page-0007.jpg]]

![[todoDel1-7_page-0008.jpg]]

![[todoDel1-7_page-0009.jpg]]

![[todoDel1-7_page-0010.jpg]]

![[todoDel1-7_page-0011.jpg]]

![[todoDel1-7_page-0012.jpg]]

![[todoDel1-7_page-0013.jpg]]

![[todoDel1-7_page-0014.jpg]]

![[todoDel1-7_page-0015.jpg]]

![[todoDel1-7_page-0016.jpg]]

![[todoDel1-7_page-0017.jpg]]

![[todoDel1-7_page-0018.jpg]]

![[todoDel1-7_page-0019.jpg]]

![[todoDel1-7_page-0020.jpg]]

![[todoDel1-7_page-0021.jpg]]

![[todoDel1-7_page-0022.jpg]]

![[todoDel1-7_page-0023.jpg]]

![[todoDel1-7_page-0024.jpg]]

![[todoDel1-7_page-0025.jpg]]

![[todoDel1-7_page-0026.jpg]]

![[todoDel1-7_page-0027.jpg]]

![[todoDel1-7_page-0028.jpg]]

![[todoDel1-7_page-0029.jpg]]

![[todoDel1-7_page-0030.jpg]]

![[todoDel1-7_page-0031.jpg]]

![[todoDel1-7_page-0032.jpg]]

![[todoDel1-7_page-0033.jpg]]

![[todoDel1-7_page-0034.jpg]]

![[todoDel1-7_page-0035.jpg]]

![[todoDel1-7_page-0036.jpg]]

![[todoDel1-7_page-0037.jpg]]

![[todoDel1-7_page-0038.jpg]]

![[todoDel1-7_page-0039.jpg]]

![[todoDel1-7_page-0040.jpg]]

![[todoDel1-7_page-0041.jpg]]

![[todoDel1-7_page-0042.jpg]]

![[todoDel1-7_page-0043.jpg]]

![[todoDel1-7_page-0044.jpg]]

![[todoDel1-7_page-0045.jpg]]

![[todoDel1-7_page-0046.jpg]]

![[todoDel1-7_page-0047.jpg]]

![[todoDel1-7_page-0048.jpg]]

![[todoDel1-7_page-0049.jpg]]

![[todoDel1-7_page-0050.jpg]]

![[todoDel1-7_page-0051.jpg]]

![[todoDel1-7_page-0052.jpg]]

![[todoDel1-7_page-0053.jpg]]

![[todoDel1-7_page-0054.jpg]]

![[todoDel1-7_page-0055.jpg]]

![[todoDel1-7_page-0056.jpg]]

![[todoDel1-7_page-0057.jpg]]

![[todoDel1-7_page-0058.jpg]]

![[todoDel1-7_page-0059.jpg]]

![[todoDel1-7_page-0060.jpg]]

![[todoDel1-7_page-0061.jpg]]

![[todoDel1-7_page-0062.jpg]]

![[todoDel1-7_page-0063.jpg]]

![[todoDel1-7_page-0064.jpg]]

![[todoDel1-7_page-0065.jpg]]

![[todoDel1-7_page-0066.jpg]]

![[todoDel1-7_page-0067.jpg]]

![[todoDel1-7_page-0068.jpg]]

![[todoDel1-7_page-0069.jpg]]

![[todoDel1-7_page-0070.jpg]]

![[todoDel1-7_page-0071.jpg]]

![[todoDel1-7_page-0072.jpg]]

![[todoDel1-7_page-0073.jpg]]

![[todoDel1-7_page-0074.jpg]]

![[todoDel1-7_page-0075.jpg]]

![[todoDel1-7_page-0076.jpg]]

![[todoDel1-7_page-0077.jpg]]

![[todoDel1-7_page-0078.jpg]]

![[todoDel1-7_page-0079.jpg]]

![[todoDel1-7_page-0080.jpg]]

![[todoDel1-7_page-0081.jpg]]

![[todoDel1-7_page-0082.jpg]]

![[todoDel1-7_page-0083.jpg]]

![[todoDel1-7_page-0084.jpg]]

![[todoDel1-7_page-0085.jpg]]
**Defining the projet scope:** se establecen las metas y como se planea lograrlo
![[todoDel1-7_page-0086.jpg]]

![[todoDel1-7_page-0087.jpg]]
**Data understanding:** es la fase donde se aplica la ciencia y se trata de entender los datos, sus orígenes , problemas, etc.
![[todoDel1-7_page-0088.jpg]]

![[todoDel1-7_page-0089.jpg]]
**Data collection:** corresponde a los medios y de donde recolectaremos los datos.
![[todoDel1-7_page-0090.jpg]]
**Data preparation:** requiere a aplicar tecnicas para manejar outliers, Nan y normalizacion
![[todoDel1-7_page-0091.jpg]]

![[todoDel1-7_page-0092.jpg]]

![[todoDel1-7_page-0093.jpg]]

![[todoDel1-7_page-0094.jpg]]
**Analysis and modeling:** encontramos patrones de datos, y contruimos  un modelo capaz de predecir los datos
![[todoDel1-7_page-0095.jpg]]
**Validation:** aplicamos distintos test para evaluar que el modelo es robusto y da resultados validos
![[todoDel1-7_page-0096.jpg]]

![[todoDel1-7_page-0097.jpg]]
**Interpretation:** Buscamos las conclusiones y buscamos en que podemos contribuir
![[todoDel1-7_page-0098.jpg]]
**Publishing and presentation:** Buscamos difundir y facilitar  el acceso a los resultados
![[todoDel1-7_page-0099.jpg]]

![[todoDel1-7_page-0100.jpg]]

![[todoDel1-7_page-0101.jpg]]

![[todoDel1-7_page-0102.jpg]]

![[todoDel1-7_page-0103.jpg]]

![[todoDel1-7_page-0104.jpg]]

![[todoDel1-7_page-0105.jpg]]

![[todoDel1-7_page-0106.jpg]]

![[todoDel1-7_page-0107.jpg]]

![[todoDel1-7_page-0108.jpg]]

![[todoDel1-7_page-0109.jpg]]

![[todoDel1-7_page-0110.jpg]]

![[todoDel1-7_page-0111.jpg]]

![[todoDel1-7_page-0112.jpg]]

![[todoDel1-7_page-0113.jpg]]

![[todoDel1-7_page-0114.jpg]]

![[todoDel1-7_page-0115.jpg]]

![[todoDel1-7_page-0116.jpg]]

![[todoDel1-7_page-0117.jpg]]

![[todoDel1-7_page-0118.jpg]]

![[todoDel1-7_page-0119.jpg]]

![[todoDel1-7_page-0120.jpg]]

![[todoDel1-7_page-0121.jpg]]

![[todoDel1-7_page-0122.jpg]]
En resumen es un modelo el cual usa los parametros para estimar un Y, es simple pero el modelo puede estar mal especificado
![[todoDel1-7_page-0123.jpg]]
Buscan una estimación que se acerque lo más posible al dato, es flexible pero puede ser complejo
![[todoDel1-7_page-0124.jpg]]

![[todoDel1-7_page-0125.jpg]]

![[todoDel1-7_page-0126.jpg]]

![[todoDel1-7_page-0127.jpg]]

![[todoDel1-7_page-0128.jpg]]

![[todoDel1-7_page-0129.jpg]]

![[todoDel1-7_page-0130.jpg]]

![[todoDel1-7_page-0131.jpg]]
Las variables numericas usan regresiones lineales y las cualitativas usan regresion logistica.
![[todoDel1-7_page-0132.jpg]]

![[todoDel1-7_page-0133.jpg]]

![[todoDel1-7_page-0134.jpg]]

![[todoDel1-7_page-0135.jpg]]

![[todoDel1-7_page-0136.jpg]]

![[todoDel1-7_page-0137.jpg]]

![[todoDel1-7_page-0138.jpg]]

![[todoDel1-7_page-0139.jpg]]

![[todoDel1-7_page-0140.jpg]]

![[todoDel1-7_page-0141.jpg]]

![[todoDel1-7_page-0142.jpg]]

![[todoDel1-7_page-0143.jpg]]

![[todoDel1-7_page-0144.jpg]]

![[todoDel1-7_page-0145.jpg]]

![[todoDel1-7_page-0146.jpg]]

![[todoDel1-7_page-0147.jpg]]

![[todoDel1-7_page-0148.jpg]]

![[todoDel1-7_page-0149.jpg]]

![[todoDel1-7_page-0150.jpg]]

![[todoDel1-7_page-0151.jpg]]

![[todoDel1-7_page-0152.jpg]]

![[todoDel1-7_page-0153.jpg]]

![[todoDel1-7_page-0154.jpg]]

![[todoDel1-7_page-0155.jpg]]

![[todoDel1-7_page-0156.jpg]]

![[todoDel1-7_page-0157.jpg]]

![[todoDel1-7_page-0158.jpg]]

![[todoDel1-7_page-0159.jpg]]

![[todoDel1-7_page-0160.jpg]]
Para explicarlo de la forma más sencilla posible, imagina que estás en la **cima de una montaña** y hay mucha niebla, por lo que no puedes ver el camino hacia el fondo del valle. Tu objetivo es llegar al punto más bajo (el **mínimo** de la función de error).

Así es como funciona el descenso por gradiente paso a paso:

1. **Siente la inclinación:** Como no ves el mapa completo, solo puedes sentir hacia dónde se inclina el suelo bajo tus pies. En matemáticas, esa inclinación es el **gradiente**.
2. **Da un paso hacia abajo:** Una vez que sabes hacia dónde está la bajada, das un paso en esa dirección. En el algoritmo, esto significa que **actualizas los parámetros** del modelo para que el error sea un poco más pequeño.
3. **El tamaño del paso (Tasa de aprendizaje):** Esto es qué tan grande es el salto que das.
    - Si el paso es **muy grande**, podrías pasarte de largo del fondo del valle.
    - Si el paso es **muy pequeño**, tardarás una eternidad en llegar.
4. **Repite hasta llegar al fondo:** Sigues dando pasos y volviendo a sentir la inclinación hasta que el suelo esté plano. En ese momento, habrás encontrado los **mejores parámetros** para tu modelo, donde el error es lo más bajo posible.

¿Por qué lo usamos?

A veces, calcular la solución perfecta de un solo viaje (la solución analítica) es como intentar teletransportarse: es demasiado pesado o imposible si tienes muchísimos datos. El descenso por gradiente es más eficiente porque va **aprendiendo poco a poco** a través de la práctica (iteraciones).

En resumen:

- **Función de costo:** Es la montaña (qué tan mal lo está haciendo el modelo).
- **Gradiente:** Es la dirección de la bajada.
- **Tasa de aprendizaje (**α**):** Es el tamaño de tus pasos.
- **Objetivo:** Llegar al lugar más bajo posible para que el modelo sea preciso.
![[todoDel1-7_page-0161.jpg]]

![[todoDel1-7_page-0162.jpg]]

![[todoDel1-7_page-0163.jpg]]

![[todoDel1-7_page-0164.jpg]]

![[todoDel1-7_page-0165.jpg]]

![[todoDel1-7_page-0166.jpg]]

![[todoDel1-7_page-0167.jpg]]

![[todoDel1-7_page-0168.jpg]]

![[todoDel1-7_page-0169.jpg]]

![[todoDel1-7_page-0170.jpg]]

![[todoDel1-7_page-0171.jpg]]

![[todoDel1-7_page-0172.jpg]]

![[todoDel1-7_page-0173.jpg]]

![[todoDel1-7_page-0174.jpg]]

![[todoDel1-7_page-0175.jpg]]

![[todoDel1-7_page-0176.jpg]]

![[todoDel1-7_page-0177.jpg]]

![[todoDel1-7_page-0178.jpg]]

![[todoDel1-7_page-0179.jpg]]

![[todoDel1-7_page-0180.jpg]]

![[todoDel1-7_page-0181.jpg]]

![[todoDel1-7_page-0182.jpg]]

![[todoDel1-7_page-0183.jpg]]

![[todoDel1-7_page-0184.jpg]]

![[todoDel1-7_page-0185.jpg]]

![[todoDel1-7_page-0186.jpg]]

![[todoDel1-7_page-0187.jpg]]

![[todoDel1-7_page-0188.jpg]]

![[todoDel1-7_page-0189.jpg]]

![[todoDel1-7_page-0190.jpg]]

![[todoDel1-7_page-0191.jpg]]

![[todoDel1-7_page-0192.jpg]]

![[todoDel1-7_page-0193.jpg]]

![[todoDel1-7_page-0194.jpg]]

![[todoDel1-7_page-0195.jpg]]

![[todoDel1-7_page-0196.jpg]]

![[todoDel1-7_page-0197.jpg]]

![[todoDel1-7_page-0198.jpg]]

![[todoDel1-7_page-0199.jpg]]

![[todoDel1-7_page-0200.jpg]]

![[todoDel1-7_page-0201.jpg]]

![[todoDel1-7_page-0202.jpg]]

![[todoDel1-7_page-0203.jpg]]

![[todoDel1-7_page-0204.jpg]]

![[todoDel1-7_page-0205.jpg]]

![[todoDel1-7_page-0206.jpg]]

![[todoDel1-7_page-0207.jpg]]

![[todoDel1-7_page-0208.jpg]]

![[todoDel1-7_page-0209.jpg]]

![[todoDel1-7_page-0210.jpg]]

![[todoDel1-7_page-0211.jpg]]

![[todoDel1-7_page-0212.jpg]]

![[todoDel1-7_page-0213.jpg]]

![[todoDel1-7_page-0214.jpg]]
Para explicarlo de la forma más sencilla posible, imagina que estás en la **cima de una montaña** y hay mucha niebla, por lo que no puedes ver el camino hacia el fondo del valle. Tu objetivo es llegar al punto más bajo (el **mínimo** de la función de error).

Así es como funciona el descenso por gradiente paso a paso:

1. **Siente la inclinación:** Como no ves el mapa completo, solo puedes sentir hacia dónde se inclina el suelo bajo tus pies. En matemáticas, esa inclinación es el **gradiente**.
2. **Da un paso hacia abajo:** Una vez que sabes hacia dónde está la bajada, das un paso en esa dirección. En el algoritmo, esto significa que **actualizas los parámetros** del modelo para que el error sea un poco más pequeño.
3. **El tamaño del paso (Tasa de aprendizaje):** Esto es qué tan grande es el salto que das.
    - Si el paso es **muy grande**, podrías pasarte de largo del fondo del valle.
    - Si el paso es **muy pequeño**, tardarás una eternidad en llegar.
4. **Repite hasta llegar al fondo:** Sigues dando pasos y volviendo a sentir la inclinación hasta que el suelo esté plano. En ese momento, habrás encontrado los **mejores parámetros** para tu modelo, donde el error es lo más bajo posible.

¿Por qué lo usamos?

A veces, calcular la solución perfecta de un solo viaje (la solución analítica) es como intentar teletransportarse: es demasiado pesado o imposible si tienes muchísimos datos. El descenso por gradiente es más eficiente porque va **aprendiendo poco a poco** a través de la práctica (iteraciones).

En resumen:

- **Función de costo:** Es la montaña (qué tan mal lo está haciendo el modelo).
- **Gradiente:** Es la dirección de la bajada.
- **Tasa de aprendizaje (**α**):** Es el tamaño de tus pasos.
- **Objetivo:** Llegar al lugar más bajo posible para que el modelo sea preciso.
![[todoDel1-7_page-0215.jpg]]

![[todoDel1-7_page-0216.jpg]]

![[todoDel1-7_page-0217.jpg]]

![[todoDel1-7_page-0218.jpg]]

![[todoDel1-7_page-0219.jpg]]

![[todoDel1-7_page-0220.jpg]]

![[todoDel1-7_page-0221.jpg]]

![[todoDel1-7_page-0222.jpg]]

![[todoDel1-7_page-0223.jpg]]

![[todoDel1-7_page-0224.jpg]]

![[todoDel1-7_page-0225.jpg]]

![[todoDel1-7_page-0226.jpg]]

![[todoDel1-7_page-0227.jpg]]

![[todoDel1-7_page-0228.jpg]]

![[todoDel1-7_page-0229.jpg]]

![[todoDel1-7_page-0230.jpg]]

![[todoDel1-7_page-0231.jpg]]

![[todoDel1-7_page-0232.jpg]]

![[todoDel1-7_page-0233.jpg]]

![[todoDel1-7_page-0234.jpg]]

![[todoDel1-7_page-0235.jpg]]

![[todoDel1-7_page-0236.jpg]]

![[todoDel1-7_page-0237.jpg]]

![[todoDel1-7_page-0238.jpg]]

![[todoDel1-7_page-0239.jpg]]

![[todoDel1-7_page-0240.jpg]]

![[todoDel1-7_page-0241.jpg]]

![[todoDel1-7_page-0242.jpg]]

![[todoDel1-7_page-0243.jpg]]

![[todoDel1-7_page-0244.jpg]]

![[todoDel1-7_page-0245.jpg]]

![[todoDel1-7_page-0246.jpg]]

![[todoDel1-7_page-0247.jpg]]

![[todoDel1-7_page-0248.jpg]]

![[todoDel1-7_page-0249.jpg]]

![[todoDel1-7_page-0250.jpg]]

![[todoDel1-7_page-0251.jpg]]

![[todoDel1-7_page-0252.jpg]]

![[todoDel1-7_page-0253.jpg]]

![[todoDel1-7_page-0254.jpg]]

![[todoDel1-7_page-0255.jpg]]

![[todoDel1-7_page-0256.jpg]]

![[todoDel1-7_page-0257.jpg]]

![[todoDel1-7_page-0258.jpg]]

![[todoDel1-7_page-0259.jpg]]

![[todoDel1-7_page-0260.jpg]]

![[todoDel1-7_page-0261.jpg]]

![[todoDel1-7_page-0262.jpg]]

![[todoDel1-7_page-0263.jpg]]

![[todoDel1-7_page-0264.jpg]]

![[todoDel1-7_page-0265.jpg]]

![[todoDel1-7_page-0266.jpg]]

![[todoDel1-7_page-0267.jpg]]

![[todoDel1-7_page-0268.jpg]]
**Z-score**

El **Z-score** (o estandarización) es una medida que indica cuántas desviaciones estándar se aleja un valor de la media. Según las fuentes, tiene dos aplicaciones principales:

- **Procesamiento de datos:** Se utiliza para normalizar variables, transformándolas para que tengan una media de cero y una desviación estándar de uno mediante la fórmula x′=σx−μ​.
- **Detección de valores atípicos:** Permite identificar _outliers_ basándose en qué tan lejos se encuentra un punto del patrón general del conjunto de datos.
- **En regresión:** Se menciona que el Z-score (a menudo llamado **t-score** en este ámbito) mide cuántas desviaciones estándar está un coeficiente estimado (β^​i​) del valor cero.

**t-value (o t-score)**

El **t-value** es el estadístico de prueba utilizado específicamente en los modelos de regresión para determinar si un coeficiente es significativamente distinto de cero.

- **Cálculo:** Se obtiene dividiendo el coeficiente estimado (β^​i​) por su error estándar (SE(β^​i​)).
- **Interpretación:** Un valor de t alejado de cero (generalmente con un valor absoluto mayor a 2) sugiere que la variable tiene un efecto significativo sobre la variable de respuesta (y) y no es simplemente ruido. Si el valor es cercano a 0, el coeficiente no se considera significativo.

**p-value**

El **p-value** es la probabilidad de obtener un valor de t tan extremo como el observado, asumiendo que la hipótesis nula (H0​:βi​=0) es cierta.

- **Interpretación:**
    - **p-valor pequeño (p < 0.05):** Indica que hay evidencia estadística suficiente para rechazar la hipótesis nula, lo que significa que la variable es **significativa** para el modelo.
    - **p-valor grande (p > 0.05):** Indica que no hay evidencia suficiente para afirmar que la variable influye en el resultado, por lo que podría ser irrelevante.
- **Uso gráfico:** Se visualiza como el área bajo la curva de la distribución t de Student en los extremos (colas) a partir del valor de t observado.

**¿Para qué sirven en conjunto?**

Estos indicadores son esenciales para la **selección de características (Feature Selection)**. Sirven para:

1. **Identificar variables relevantes:** Ayudan a decidir qué predictores deben mantenerse en el modelo y cuáles descartarse por ser redundantes o inútiles.
2. **Reducir el sobreajuste (overfitting):** Al eliminar variables no significativas basadas en su p-valor (como en el método de _Backward Selection_), se mejora la capacidad de generalización del modelo.
3. **Simplificar el modelo:** Permiten construir modelos más fáciles de interpretar y que requieren menos tiempo de entrenamiento.
![[todoDel1-7_page-0269.jpg]]

![[todoDel1-7_page-0270.jpg]]

![[todoDel1-7_page-0271.jpg]]

![[todoDel1-7_page-0272.jpg]]

![[todoDel1-7_page-0273.jpg]]

![[todoDel1-7_page-0274.jpg]]

![[todoDel1-7_page-0275.jpg]]

![[todoDel1-7_page-0276.jpg]]

![[todoDel1-7_page-0277.jpg]]

![[todoDel1-7_page-0278.jpg]]

![[todoDel1-7_page-0279.jpg]]

![[todoDel1-7_page-0280.jpg]]

![[todoDel1-7_page-0281.jpg]]

![[todoDel1-7_page-0282.jpg]]

![[todoDel1-7_page-0283.jpg]]

![[todoDel1-7_page-0284.jpg]]

![[todoDel1-7_page-0285.jpg]]