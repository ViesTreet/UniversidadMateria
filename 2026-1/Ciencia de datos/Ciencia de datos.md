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
# Unidad 2
![[Graphs-2_page-0018.jpg]]

![[Graphs-2_page-0017.jpg]]

![[Graphs-2_page-0016.jpg]]

![[Graphs-2_page-0015.jpg]]

![[Graphs-2_page-0014.jpg]]

![[Graphs-2_page-0013.jpg]]

![[Graphs-2_page-0012.jpg]]

![[Graphs-2_page-0011.jpg]]

![[Graphs-2_page-0010.jpg]]
![[Graphs-2_page-0009.jpg]]

![[Graphs-2_page-0008.jpg]]

![[Graphs-2_page-0007.jpg]]

![[Graphs-2_page-0006.jpg]]

![[Graphs-2_page-0005.jpg]]

![[Graphs-2_page-0004.jpg]]

![[Graphs-2_page-0003.jpg]]

![[Graphs-2_page-0002.jpg]]

![[Graphs-2_page-0001.jpg]]![[W1_8__KMeans_KNN_page-0053.jpg]]

![[W1_8__KMeans_KNN_page-0052.jpg]]
Los algoritmos KNN, buscan en una plano de n dimensiones los puntos mas cercanos y les calcula la media
![[W1_8__KMeans_KNN_page-0051.jpg]]
El KNN es costoso y requiere limpieza de outliers
![[W1_8__KMeans_KNN_page-0050.jpg]]
Menor dataset = menor k = mas sensible al ruido y outliers
mayor dataset = mas k = mas general
![[W1_8__KMeans_KNN_page-0049.jpg]]

![[W1_8__KMeans_KNN_page-0048.jpg]]

![[W1_8__KMeans_KNN_page-0047.jpg]]

![[W1_8__KMeans_KNN_page-0046.jpg]]

![[W1_8__KMeans_KNN_page-0045.jpg]]

![[W1_8__KMeans_KNN_page-0044.jpg]]

![[W1_8__KMeans_KNN_page-0043.jpg]]

![[W1_8__KMeans_KNN_page-0042.jpg]]

![[W1_8__KMeans_KNN_page-0041.jpg]]

![[W1_8__KMeans_KNN_page-0040.jpg]]
Aqui estamos usando KNN para encontrar a que etiqueta pertence el dato, en este caso es class B
![[W1_8__KMeans_KNN_page-0039.jpg]]

![[W1_8__KMeans_KNN_page-0038.jpg]]
**$N_0 =$** es el punto mas cercano
![[W1_8__KMeans_KNN_page-0037.jpg]]
**sirve para clasificación. mientras que Kmeans sirve para agrupacio**
![[W1_8__KMeans_KNN_page-0036.jpg]]

![[W1_8__KMeans_KNN_page-0035.jpg]]
KNN es **no parametrico y no requiere entrenamiento iterativo**, si no solo guardar datos en memoria
![[W1_8__KMeans_KNN_page-0034.jpg]]
KNN tambien sirve para multiclase y puede servir como algoritmoo regresivo
![[W1_8__KMeans_KNN_page-0033.jpg]]

![[W1_8__KMeans_KNN_page-0032.jpg]]

![[W1_8__KMeans_KNN_page-0031.jpg]]

![[W1_8__KMeans_KNN_page-0030.jpg]]
Usa muestra aleatorias para crear el centroide de datos o sea las clasificaciones
![[W1_8__KMeans_KNN_page-0029.jpg]]
Es mas eficiente
![[W1_8__KMeans_KNN_page-0028.jpg]]

![[W1_8__KMeans_KNN_page-0027.jpg]]

![[W1_8__KMeans_KNN_page-0026.jpg]]

![[W1_8__KMeans_KNN_page-0025.jpg]]

![[W1_8__KMeans_KNN_page-0024.jpg]]

![[W1_8__KMeans_KNN_page-0023.jpg]]

![[W1_8__KMeans_KNN_page-0022.jpg]]

![[W1_8__KMeans_KNN_page-0021.jpg]]

![[W1_8__KMeans_KNN_page-0020.jpg]]
**K-means++** elije punto mas apartados entre si para sus centrides de esa manera los centroides estan apartados
![[W1_8__KMeans_KNN_page-0019.jpg]]
**K-means** depende mucho de la seleccion de centroides
![[W1_8__KMeans_KNN_page-0018.jpg]]

![[W1_8__KMeans_KNN_page-0017.jpg]]
El metodo del codo usca la cantidad optima de cluster lo sufficiente para no tener tanto errores, pero menos que para hacer overfitting
![[W1_8__KMeans_KNN_page-0016.jpg]]

![[W1_8__KMeans_KNN_page-0015.jpg]]

![[W1_8__KMeans_KNN_page-0014.jpg]]
**La inercia** es un valor de que tan bien agrupados es tan los valores del cluster respecto al centroide
![[W1_8__KMeans_KNN_page-0013.jpg]]

![[W1_8__KMeans_KNN_page-0012.jpg]]

![[W1_8__KMeans_KNN_page-0011.jpg]]

![[W1_8__KMeans_KNN_page-0010.jpg]]

![[W1_8__KMeans_KNN_page-0009.jpg]]
el cluster divide en conjuntos el dataset, hay que minimizar las distancia
![[W1_8__KMeans_KNN_page-0008.jpg]]

![[W1_8__KMeans_KNN_page-0007.jpg]]

![[W1_8__KMeans_KNN_page-0006.jpg]]

![[W1_8__KMeans_KNN_page-0005.jpg]]

![[W1_8__KMeans_KNN_page-0004.jpg]]

![[W1_8__KMeans_KNN_page-0003.jpg]]

![[W1_8__KMeans_KNN_page-0002.jpg]]

![[W1_8__KMeans_KNN_page-0001.jpg]]![[W1_9__Bagging_and_Boosting_page-0001.jpg]]

![[W1_9__Bagging_and_Boosting_page-0002.jpg]]
**Bagging:** reduce la varianza
**Boosting:** reduce el sesgo y tambien la varianza
![[W1_9__Bagging_and_Boosting_page-0003.jpg]]
En resumen si tenemos un modelo simple puede que tengamos sesgo y varianza pero si tenemos un modelo demasiado complejo podemos tener overfitting
![[W1_9__Bagging_and_Boosting_page-0004.jpg]]
El baggin usa **paralelismo** y luego combina los modelos para obtener un modelo complejo mientras que boosting usa **iteracion** usa un modelo y luego lo va mejorando
![[W1_9__Bagging_and_Boosting_page-0005.jpg]]

![[W1_9__Bagging_and_Boosting_page-0006.jpg]]
Los arboles de decisiones suelen tener baja precision pero son faciles  de entender, su funcion es  como un arbol n-ario
![[W1_9__Bagging_and_Boosting_page-0007.jpg]]

![[W1_9__Bagging_and_Boosting_page-0008.jpg]]

![[W1_9__Bagging_and_Boosting_page-0009.jpg]]
Las hojas sin hijos seran las soluciones, y en cada nodo se tomar una condicion para elegir el camino, las condiciones pueden ser en varios ambitos, un nodo puede preguntar por el salario y otro por la edad
![[W1_9__Bagging_and_Boosting_page-0010.jpg]]

![[W1_9__Bagging_and_Boosting_page-0011.jpg]]

![[W1_9__Bagging_and_Boosting_page-0012.jpg]]

![[W1_9__Bagging_and_Boosting_page-0013.jpg]]
Lo que te está diciendo la diapositiva es que, como buscar el árbol de decisión perfecto es imposible por tiempo de cómputo, los algoritmos (como CART) toman el camino práctico: empiezan con todos los datos juntos y van haciendo cortes rápidos, binarios y "egoístas" paso a paso hasta que se cumple alguna condición de parada(no le importa el futuro).
![[W1_9__Bagging_and_Boosting_page-0014.jpg]]
Elegimos la particion que nos de menos suma de errores cuadraticos(RSS)
![[W1_9__Bagging_and_Boosting_page-0015.jpg]]

![[W1_9__Bagging_and_Boosting_page-0016.jpg]]
Luego ya no dividimos los predictores(nuestras variables) si no que partimos las regiones donde estan las decisiones(las hojas terminales son una region)
![[W1_9__Bagging_and_Boosting_page-0017.jpg]]

![[W1_9__Bagging_and_Boosting_page-0018.jpg]]

![[W1_9__Bagging_and_Boosting_page-0019.jpg]]
A pesar de representar el arbol como una figura 2D la realidad es que ocupa una superficie 3D
![[W1_9__Bagging_and_Boosting_page-0020.jpg]]
Los arboles pueden generar overfitting, por lo que es recomendable construir el arbol entero  y luego ir podandolo en vase a la validacion cruzada
![[W1_9__Bagging_and_Boosting_page-0021.jpg]]
Esta ecuacion nos permite generar subarboles mas pequeños esto se llama **poda por complejidad de costo**
![[W1_9__Bagging_and_Boosting_page-0022.jpg]]

![[W1_9__Bagging_and_Boosting_page-0023.jpg]]

![[W1_9__Bagging_and_Boosting_page-0024.jpg]]

![[W1_9__Bagging_and_Boosting_page-0025.jpg]]

![[W1_9__Bagging_and_Boosting_page-0026.jpg]]

![[W1_9__Bagging_and_Boosting_page-0027.jpg]]

![[W1_9__Bagging_and_Boosting_page-0028.jpg]]
**Los arboles de clasificación** son similares a los arboles de regresion pero su respuesta es cualitativa, se generan de manera similar a la regresion, con una division binaria recursiva pero el RSS no es aplicable
![[W1_9__Bagging_and_Boosting_page-0029.jpg]]

![[W1_9__Bagging_and_Boosting_page-0030.jpg]]
Cuando el árbol está buscando de manera **voraz** (paso a paso) dónde cortar el espacio predictor, evalúa el Índice de Gini antes y después de cada posible corte. El algoritmo **elegirá el corte que logre reducir al máximo el Índice de Gini** (es decir, el que deje los nodos hijos lo más puros posibles), trata que cada hoja solo sea una posibilidad para no dejar nodos impuros
![[W1_9__Bagging_and_Boosting_page-0031.jpg]]
Es similar a Gini pero usamos la incertidumbre para calcular la pureza, cuando el valor es 0 es que el nodo es puro:
**Usamos Gini y entropia** para crecer el arbol, pero para podralo usamos tasa de error
![[W1_9__Bagging_and_Boosting_page-0032.jpg]]

![[W1_9__Bagging_and_Boosting_page-0033.jpg]]

![[W1_9__Bagging_and_Boosting_page-0034.jpg]]

![[W1_9__Bagging_and_Boosting_page-0035.jpg]]

![[W1_9__Bagging_and_Boosting_page-0036.jpg]]
La diferencia entre un modelo lineal y un arbol de decision, es que el modelo separa todo en una linea recta, mientras que los arboles de decisiones, generan particiones en el plano donde puede caer una clasificación
![[W1_9__Bagging_and_Boosting_page-0037.jpg]]

![[W1_9__Bagging_and_Boosting_page-0038.jpg]]

![[W1_9__Bagging_and_Boosting_page-0039.jpg]]
En resumen **bagging** junta varios modelos mas debiles los cuales entrenan y luego los promedia, lo que reduce la varianza
![[W1_9__Bagging_and_Boosting_page-0040.jpg]]
Bagging genera arboles con muestras del dataframe, no los poda y promedia las prediciones, de esta manera estos arboles que tenian alta varianza, pero nulo overffiting(sesgo) logran reducir su varianza mejorando la presicion
![[W1_9__Bagging_and_Boosting_page-0041.jpg]]
Entonces cada arbol decide en donde clasificar y luego se toma por mayoria la votacion de todos los arboles para clasificar
![[W1_9__Bagging_and_Boosting_page-0042.jpg]]
### 1. El contexto: El muestreo por Bootstrap
Cuando haces _bagging_, creas muchos árboles distintos (por ejemplo, B=100 árboles). Para que no sean todos iguales, cada árbol se entrena con una muestra aleatoria de tus datos original extraída **con reemplazo** (puedes repetir filas).
- Matemáticamente, cuando haces esto, cada árbol termina usando más o menos las **2/3 partes (63.2%)** de tus datos para entrenarse.
- **El 1/3 restante (36.8%)** de los datos se queda fuera. A ese grupo de datos que el árbol "nunca vio" se le llama **Out-of-Bag (OOB)** o "fuera de la bolsa".
### 2. El truco: ¿Cómo se calcula el error OOB?
Imagina que tienes una fila de datos específica, llamémosla la **Observación i**:
1. El algoritmo busca **cuáles árboles NO usaron la observación i** durante su entrenamiento (que serán aproximadamente B/3 árboles del total). Para esos árboles específicos, la observación i es un dato totalmente nuevo (de prueba).
2. Le pides a esos árboles "ignorantes" que predigan el valor de la observación i.
3. Juntas sus respuestas: si es regresión las promedias, y si es clasificación haces una votación por mayoría.
4. Repites esto para **todas** las observaciones de tu dataset.
Al final, comparas esa predicción "limpia" de cada fila con su valor real y calculas el error global. Ese es el **Error OOB**.
### 3. ¿Por qué es tan genial?
- **Es una estimación del error de prueba ("Test Error") súper honesta:** Como la predicción de cada fila se hizo usando únicamente árboles que jamás la habían visto, no hay trampa ni sobreajuste (_overfitting_).
- **Equivalencia teórica:** La nota al pie en morado dice que si construyes suficientes árboles (B grande), el error OOB es matemáticamente casi idéntico a hacer un **Leave-One-Out Cross-Validation (LOOCV)**, pero de manera gratuita, automática y mientras entrenas el modelo.
En resumen: El error OOB es la forma que tiene Random Forest/Bagging de auto-evaluarse sobre la marcha usando los datos sobrantes de cada árbol.
![[W1_9__Bagging_and_Boosting_page-0043.jpg]]

![[W1_9__Bagging_and_Boosting_page-0044.jpg]]

![[W1_9__Bagging_and_Boosting_page-0045.jpg]]
### 1. El problema del Bagging tradicional (La correlación)
Imagina que estás entrenando un modelo de Bagging para predecir el precio de casas y tienes 13 variables ($p = 13$). Una de ellas es _"Cantidad de metros cuadrados"_, que es un predictor **ultra dominante** (tiene un peso gigante sobre el precio).
Como en Bagging cada árbol puede mirar _todas_ las variables en cada corte, **prácticamente todos los árboles elegirán "metros cuadrados" para su primera división en la raíz**.
- **El problema:** Aunque los árboles se entrenen con muestras de datos ligeramente distintas (Bootstrap), todos terminan siendo estructuralmente muy parecidos. Están altamente **correlacionados**. Si promedias muchos árboles que cometen casi los mismos errores, el beneficio del "comité" se pierde.
### 2. La solución de Random Forest: Forzar la variedad
Random Forest introduce una regla estricta para romper esa correlación: cada vez que un árbol va a hacer un corte (un split), **se le prohíbe mirar todas las variables**.
- **Muestreo aleatorio de predictores ($m$):** En cada nodo de cada árbol, el algoritmo selecciona al azar un subconjunto de solo $m$ variables de entre las $p$ totales disponibles. El árbol está obligado a elegir el mejor corte usando **únicamente** ese grupo reducido.
- **La regla de oro:** Típicamente se elige $m \approx \sqrt{p}$. Como muestra el ejemplo de la diapositiva, si tienes $p = 13$ variables en total, en cada nodo el árbol solo podrá elegir entre $m = 4$ variables seleccionadas al azar.
### 3. ¿Por qué funciona tan bien? (Menor Varianza)
Al limitar las opciones, obligas a que en muchos nodos el predictor dominante (los metros cuadrados) **ni siquiera esté disponible**. Esto fuerza a los árboles a buscar segundas y terceras mejores opciones (como la cantidad de baños o el barrio).
El resultado es brillante:
- Creas árboles muy **distintos (descorrelacionados)** entre sí.
- Algunos árboles individuales serán peores que otros por separado, pero al combinarlos (promediar sus predicciones), los errores aleatorios de uno se cancelan con los aciertos del otro.
- Matemáticamente: **Menos correlación $\rightarrow$ Menor Varianza global $\rightarrow$ El modelo generaliza mucho mejor con datos nuevos.**
### Las notas finales de la diapositiva:
- **Si $m = p$:** Si dejas que el número de variables elegidas al azar sea igual al total de variables, destruyes el truco y Random Forest se convierte exactamente en Bagging tradicional.
- **Si hay alta correlación y muchas variables ($high\ p$):** Forzar un $m$ muy pequeño ($m \ll p$) es donde Random Forest realmente destruye en rendimiento a otros modelos basados en árboles simples.
![[W1_9__Bagging_and_Boosting_page-0046.jpg]]

![[W1_9__Bagging_and_Boosting_page-0047.jpg]]

![[W1_9__Bagging_and_Boosting_page-0048.jpg]]
**Boosting** a diferencia de baggin, toma un modelo debil y va mejorando iterativamente el modelo anterior, se usa el mismo conjunto de entrenamiento y se ajusta con los residuos
![[W1_9__Bagging_and_Boosting_page-0049.jpg]]
### El proceso secuencial de Boosting
En lugar de intentar predecir el precio real de la casa desde el principio con un árbol gigante, Boosting hace lo siguiente:
1. **Árbol 1 (El modelo inicial):** Hace una predicción muy vaga y simple (a veces un árbol de un solo corte o una constante). Comete muchos errores.
2. **Calcular Residuos:** El algoritmo calcula qué tan lejos se quedó el Árbol 1 para cada fila de datos.
3. **Árbol 2 (Ajustado a los residuos):** Aquí está la clave. La variable objetivo de este segundo árbol **ya no es el precio real de la casa**, sino **los residuos del Árbol 1**. Este árbol se entrena para predecir el error.
4. **Actualizar el modelo:** Ahora tu predicción global es: $\text{Predicción} = \text{Árbol 1} + \lambda(\text{Árbol 2})$ (donde $\lambda$ es una tasa de aprendizaje pequeña).
5. **Repetir:** Se vuelven a calcular los nuevos residuos (lo que todavía no se ha podido explicar) y el Árbol 3 se entrena para predecir esos nuevos errores.
### Una analogía para entenderlo a la primera
Imagina que estás esculpiendo una estatua en un bloque de piedra:
- **El Árbol 1** toma un martillo gigante y le da un golpe tosco a la piedra. Le da una forma vaga, pero comete muchos errores (deja mucha piedra sobrante). Esa piedra sobrante son los **residuos**.
- **El Árbol 2** no vuelve a golpear el bloque desde cero. Mira fijamente dónde se equivocó el primer golpe (los residuos) y usa un cincel más pequeño para quitar los trozos sobrantes específicos.
- **El Árbol 3** viene a corregir lo que le faltó al Árbol 2.
Al final, si sumas el trabajo de los 100 árboles secuenciales, obtienes una escultura perfecta.
### En resumen:
Que Boosting se ajuste con los residuos significa que **cada árbol nuevo ignora lo que el modelo ya sabe hacer bien y se enfoca exclusivamente en lo que el modelo todavía está haciendo mal**. Esto hace que sea un algoritmo increíblemente preciso, aunque más propenso al sobreajuste si no se controla el número de árboles.
![[W1_9__Bagging_and_Boosting_page-0050.jpg]]

![[W1_9__Bagging_and_Boosting_page-0051.jpg]]

![[W1_9__Bagging_and_Boosting_page-0052.jpg]]

![[W1_10__Support_Vector_Machine_page-0001.jpg]]

![[W1_10__Support_Vector_Machine_page-0002.jpg]]
Las **SVM** permiten realizar tareas de clasificación y regresion usando el metodo del kernel cuando los datos no se pueden separar linealmente:
en términos sencillos, el kernel es una **función matemática que toma datos que no se pueden separar en su dimensión actual y los proyecta a una dimensión más alta (añade más variables ficticias) donde sí se pueden separar con un corte recto**.
### La analogía clásica para entenderlo visualmente
Imagina que tienes una mesa y sobre ella hay un montón de fichas de juego rojas y azules. Las fichas azules están todas en el centro formando un círculo, y las fichas rojas las rodean por fuera.
1. **El problema:** Te doy una regla de madera (un separador lineal) y te pido que la pongas sobre la mesa de forma que separe perfectamente las rojas de las azules. **Es imposible.** No importa cómo gires la regla, siempre vas a mezclar colores porque la frontera real es un círculo. Los datos _no son linealmente separables_ en 2D.
2. **El truco del Kernel:** Imagina que golpeas la mesa por debajo con un patrón específico (esa es la función de kernel). Al golpear, todas las fichas azules del centro **salen volando hacia arriba (ganan altura, una tercera dimensión $Z$)**, mientras que las rojas de los bordes se quedan abajo en la mesa.
3. **La solución lineal:** Ahora que las azules están flotando en el aire y las rojas están abajo, puedes pasar tu regla de madera de forma completamente plana (un hiperplano en 3D) por el espacio vacío entre ellas. ¡Las separaste perfectamente con un corte recto!
Cuando devuelves esa hoja de corte al plano original de la mesa (2D), se ve como una frontera circular perfecta.
### ¿Cómo se ve esto matemáticamente?
Un kernel toma tus variables originales, por ejemplo $(X_1, X_2)$, y calcula combinaciones no lineales entre ellas para inventarse una nueva dimensión.
Un ejemplo matemático muy básico es el **Kernel Polinómico**:
- Tienes tus datos en 2D: $(X_1, X_2)$ donde están mezclados.
- El kernel los transforma a 3D añadiendo una combinación cuadrática como: $(X_1, X_2, X_1^2 + X_2^2)$. Esa tercera componente es la que les da "altura" y permite que pasemos un plano recto para dividirlos.
### Los Kernels más famosos que vas a escuchar:
- **Lineal:** No hace ninguna transformación (asume que ya se pueden separar con una línea recta).
- **Polinómico:** Eleva las variables a potencias (como el ejemplo anterior).
- **RBF (Radial Basis Function / Gausiano):** Es el más usado y potente. Proyecta los datos a una dimensión **infinita** basándose en la distancia entre los puntos. Es capaz de modelar fronteras curvas ultra complejas.
En resumen: El kernel es un **atajo matemático**. Te permite disfrutar de la simplicidad y potencia de los cortes rectos de un modelo lineal, pero aplicados a problemas que son completamente curvos y complejos en el mundo real.
![[W1_10__Support_Vector_Machine_page-0003.jpg]]

![[W1_10__Support_Vector_Machine_page-0004.jpg]]

![[W1_10__Support_Vector_Machine_page-0005.jpg]]
### 1. Clasificador de Margen Máximo (_Maximal Margin Classifier_)
Es el ancestro directo de la SVM y el concepto más idealista.
- **La idea:** Imagina que tienes puntos rojos y azules perfectamente separados en el plano. Podrías trazar muchas líneas diagonales distintas que los dividan bien, pero este clasificador busca **la línea perfecta**: aquella que pase exactamente por el medio, maximizando la distancia (el "margen") entre la línea y los puntos más cercanos de cada clase.
- **El gran problema (la frase en morado):** Exige que las clases sean **perfectamente separables por una línea**. Si un solo punto azul se cruza al lado de los rojos (ruido en los datos), el algoritmo se rompe matemáticamente y no puede encontrar una solución. Es demasiado rígido para el mundo real.
### 2. Clasificador de Soporte Vectorial (_Support Vector Classifier_ o SVC)
Como el anterior fallaba con datos reales (donde siempre hay un poco de mezcla o ruido), los científicos crearon esta extensión. También se le conoce como **Clasificador de Margen Blando** (_Soft Margin Classifier_).
- **La solución:** Mantiene la idea de trazar una línea recta con el máximo margen posible, pero introduce una "tolerancia". **Permite que algunos puntos se metan dentro del margen o que incluso queden clasificados en el lado incorrecto** a cambio de mantener una frontera estable y equilibrada.
- A los puntos críticos que tocan el margen, se meten en él o lo cruzan se les llama **Vectores de Soporte** (porque son los que "sostienen" y definen la posición de la línea).
### 3. Máquina de Soporte Vectorial (_Support Vector Machine_ o SVM)
¿Qué pasa si los datos no son para nada una línea recta, sino que tienen formas curvas complejas o circulares? Ahí es donde entra la **SVM** real.
- La SVM es la combinación del **Support Vector Classifier (SVC)** + **El truco del Kernel** que vimos en la diapositiva anterior.
- Toma el clasificador de margen blando (SVC), proyecta los datos a una dimensión más alta usando el kernel y ahí arriba traza la línea recta óptima.
![[W1_10__Support_Vector_Machine_page-0006.jpg]]

![[W1_10__Support_Vector_Machine_page-0007.jpg]]

![[W1_10__Support_Vector_Machine_page-0008.jpg]]

![[W1_10__Support_Vector_Machine_page-0009.jpg]]

![[W1_10__Support_Vector_Machine_page-0010.jpg]]

![[W1_10__Support_Vector_Machine_page-0011.jpg]]
La diapositiva te está diciendo que clasificar con un hiperplano es como trazar una frontera donde la propia línea vale exactamente `0`. Cualquier dato que evalúes en la ecuación te dará un número: si es positivo está en el territorio de los azules, y si es negativo está en el territorio de los púrpuras. Así es como el modelo decide matemáticamente a qué grupo pertenece cada observación.
![[W1_10__Support_Vector_Machine_page-0012.jpg]]

![[W1_10__Support_Vector_Machine_page-0013.jpg]]

![[W1_10__Support_Vector_Machine_page-0014.jpg]]

![[W1_10__Support_Vector_Machine_page-0015.jpg]]

![[W1_10__Support_Vector_Machine_page-0016.jpg]]
### 1. "Existirá un número infinito de tales hiperplanos"
Imagina que tienes puntos azules a un lado y puntos rojos al otro, con un espacio vacío en el medio. Puedes trazar una línea diagonal para separarlos. Si la mueves un milímetro a la izquierda, sigue separándolos. Si cambias un poco su ángulo, también.
- **El concepto:** Matemáticamente hay infinitas líneas rectas válidas que logran separar los datos de entrenamiento sin cometer errores. El problema es: ¿cuál de todas elegimos?
### 2. La elección natural: "El hiperplano de margen máximo"
Como no queremos elegir cualquier línea al azar, buscamos la más segura y robusta para cuando lleguen datos nuevos. Esa línea óptima es la que pasa **exactamente por la mitad del camino**, manteniéndose lo más lejos posible de los datos de ambas clases.
### 3. ¿Qué es el "Margen"?
Para entenderlo formalmente, el algoritmo hace lo siguiente de forma interna:
1. Mide la **distancia perpendicular** desde la línea divisoria hasta el punto más cercano de todos (ya sea rojo o azul).
2. A esa distancia mínima (la zona de seguridad o "tierra de nadie" a cada lado de la línea) se le conoce como el **Margen**.
### 4. El criterio de optimización
El último punto resume el objetivo matemático del modelo: el algoritmo ajusta la orientación y posición de la línea con un único propósito en mente: **hacer que ese margen sea lo más ancho (máximo) posible**.
Los puntos del dataset que quedan justo en el borde de ese margen (rozando la zona de seguridad) son los únicos que determinan dónde se coloca la línea. Si mueves cualquier otro punto que esté lejos, la línea no se altera; pero si mueves uno de estos puntos del borde, la frontera cambia. Por eso a esos puntos clave se les llama **Vectores de Soporte**.
### En resumen:
La diapositiva explica que el _Maximal Margin Classifier_ no busca cualquier separación recta, sino **la calle más ancha posible** entre los dos grupos de datos, garantizando que la línea divisoria pase justo por el centro de esa calle.
![[W1_10__Support_Vector_Machine_page-0017.jpg]]

![[W1_10__Support_Vector_Machine_page-0018.jpg]]
Cuando el _Maximal Margin Classifier_ (o el SVC) está optimizando la ecuación del hiperplano, descarta la gran mayoría de los datos y se queda solo con los puntos que quedaron "rozando" o cruzando el margen (las casas de la orilla).
Matemáticamente, los coeficientes $\beta$ (los que definen la inclinación y posición de la línea) se calculan basándose **únicamente en las coordenadas de estos vectores de soporte**.
Por eso se dice que son el subconjunto de datos más importante: si limpiaras tu base de datos y borraras todos los puntos que _no_ son vectores de soporte, y volvieras a entrenar el modelo, **obtendrías exactamente la misma línea recta**.
![[W1_10__Support_Vector_Machine_page-0019.jpg]]

![[W1_10__Support_Vector_Machine_page-0020.jpg]]
### 1. El objetivo supremo: Maximizar $M$
El texto en rojo define la meta del algoritmo: encontrar la calle más ancha posible entre las dos clases.
- $M$ representa el **ancho del margen** (la distancia mínima desde la línea divisoria hasta cualquier punto de entrenamiento). Queremos que $M$ sea lo más grande posible para garantizar la máxima seguridad al clasificar datos nuevos.
### 2. ¿Qué significa que $M$ sea positivo?
Si el algoritmo encuentra una solución donde $M > 0$, significa que **los datos son perfectamente separables de forma lineal**. No hay ningún punto rojo invadiendo el territorio azul, ni viceversa; todos los puntos quedaron en el lado correcto de la frontera con un espacio libre de separación.
### 3. La restricción del "Lado Correcto"
El texto menciona una restricción matemática basada en una ecuación. Para asegurar que cada observación $i$ esté en su territorio correspondiente, el algoritmo exige que:

$$y_i(\beta_0 + \beta_1x_{i1} + \dots + \beta_px_{ip}) \geq M$$

¿Por qué funciona este truco?
- Si un punto es de la clase **Azul** ($y_i = 1$), la ecuación del hiperplano debe dar un número positivo mayor o igual a $M$. $(+1) \times (\text{positivo}) \geq M \rightarrow$ **Correcto**.
- Si un punto es de la clase **Púrpura** ($y_i = -1$), la ecuación del hiperplano debe dar un número negativo. Al multiplicarlo por el $y_i$, se vuelve positivo: $(-1) \times (\text{negativo}) \geq M \rightarrow$ **Correcto**.
Si algún punto estuviera en el lado incorrecto, esa multiplicación daría un número negativo, rompiendo la restricción.
### 4. El problema de la escala (La explicación de las notas al pie)
El último párrafo y las notas de la diapositiva abordan un tecnicismo algebraico muy importante.
Si tienes una línea recta como $X_1 + X_2 - 5 = 0$, y multiplicas toda la ecuación por $2$ ($2X_1 + 2X_2 - 10 = 0$), **la línea recta sigue estando exactamente en el mismo lugar del plano**. Geométricamente no ha cambiado nada.
Sin embargo, si intentas medir la distancia matemática desde un punto a la línea usando los coeficientes ($\beta$), al haberlos multiplicado por 2, las distancias calculadas se duplicarían artificialmente sin que la línea se haya movido.
Para evitar que el algoritmo haga "trampa" agrandando el margen $M$ simplemente multiplicando los coeficientes por un número grande ($k$), se introduce una **restricción de normalización**:

$$\sum_{j=1}^{p} \beta_j^2 = 1$$

Esto obliga a que la magnitud del vector de coeficientes sea fija. Al bloquear la escala, la única forma que tiene el modelo de aumentar el margen $M$ es **moviendo y rotando la línea real** hasta encontrar la orientación óptima.
### En resumen:
Esta diapositiva resume el problema de optimización que resuelve el modelo: **Maximizar el ancho de la calle ($M$) sujeto a que nadie se cruce de bando (restricción de signo) y a que las distancias estén bien medidas (restricción de escala de los $\beta$).**
![[W1_10__Support_Vector_Machine_page-0021.jpg]]

![[W1_10__Support_Vector_Machine_page-0022.jpg]]

![[W1_10__Support_Vector_Machine_page-0023.jpg]]
### 1. El gráfico: La geometría del margen
La imagen ilustra perfectamente lo que veníamos hablando en la diapositiva anterior:
- Tienes la línea azul central ($x^T\beta + \beta_0 = 0$).
- Tienes la "calle" amarilla que representa el **margen**.
- Los puntos verdes y rojos que están justo en el borde de la zona amarilla son tus **vectores de soporte**.
- Nota que las ecuaciones de los bordes del margen están etiquetadas con una constante $C = \frac{1}{\|\beta\|}$. Esto conecta directamente la geometría con el álgebra: **minimizar la magnitud de los pesos ($\|\beta\|$) es matemáticamente equivalente a maximizar el ancho del margen**.
### 2. Formulación Primal vs. Formulación Dual
Para resolver la optimización, puedes plantear las ecuaciones de dos maneras distintas:
- **La representación Primal (El enfoque directo):**
    - Se enfoca en buscar directamente los valores óptimos de las variables del hiperplano ($\beta$ y $\beta_0$).
    - **Su problema:** Si tienes pocas filas ($n$) pero **muchísimas variables ($p$)**, el costo computacional de la forma primal se dispara porque depende fuertemente de la dimensión del espacio.
- **La representación Dual (El enfoque alternativo):**
    - En lugar de buscar los pesos $\beta$, el problema se transforma para buscar un conjunto de coeficientes llamados **multiplicadores de Lagrange** ($\alpha_i$), donde hay un coeficiente por cada fila de datos.
    - **Por qué es brillante:** En la forma dual, los datos solo aparecen en la ecuación en forma de **productos punto** ($x_i \cdot x_j$). Esto significa que el algoritmo solo necesita saber qué tan similares son los puntos entre sí, no la dimensión en la que viven.
### 3. ¿Por qué importa esto para las SVM?
La relación primal-dual a través de Lagrange es el secreto que permite que existan los **Kernels** que vimos al principio.
Como la formulación **Dual** depende exclusivamente de productos punto entre vectores, si quieres llevar tus datos a una dimensión infinita para separar curvas complejas, **no necesitas calcular las coordenadas en esa dimensión infinita** (lo cual sería imposible). Solo necesitas reemplazar el producto punto tradicional por una función de Kernel.
![[Pasted image 20260623153011.png]]
![[W1_10__Support_Vector_Machine_page-0024.jpg]]

![[W1_10__Support_Vector_Machine_page-0025.jpg]]

![[W1_10__Support_Vector_Machine_page-0026.jpg]]

![[W1_10__Support_Vector_Machine_page-0027.jpg]]
Al buscar el hiperplano perfecto provocamos sensibilidad a casos especificos que talvez no representan a la media, esto puede generar **sobreajuste**
![[W1_10__Support_Vector_Machine_page-0028.jpg]]

![[W1_10__Support_Vector_Machine_page-0029.jpg]]
### 1. Permitir errores para mejorar el resultado global
El texto en rojo plantea una estrategia de sacrificio muy inteligente: _"SVC puede clasificar erróneamente unas pocas observaciones de entrenamiento con el fin de hacer un mejor trabajo en la clasificación de las observaciones restantes"_.
- **Por qué se hace:** Si intentas forzar una línea recta que deje al 100% de los puntos en el bando correcto cuando hay datos mezclados, la línea quedará en una posición sumamente forzada, torcida o inestable.
- Al permitirle al algoritmo equivocarse con un par de puntos aislados (puntos ruidosos o _outliers_), la línea resultante se mantiene recta, estable y mucho más representativa de la tendencia general de los datos.
### 2. ¿Cómo funciona la tolerancia?
El segundo punto detalla las dos formas en que las observaciones pueden "romper las reglas":
1. **Meterse dentro del margen:** El punto está en el lado correcto de la línea divisoria, pero cruzó la línea amarilla del "margen de seguridad".
2. **Quedar en el lado incorrecto:** El punto cruzó completamente el hiperplano y quedó clasificado de manera errónea en el bando contrario.
### 3. El Margen Suave (_Soft Margin_)
La frase en morado resume el concepto central: **El margen es suave**.
En lugar de ser una muralla de concreto infranqueable (como en el _Maximal Margin Classifier_), el margen del SVC actúa más bien como una **cerca elástica**. Los puntos pueden empujarla, meterse en ella o cruzarla. El algoritmo controla qué tan elástica es esta cerca mediante un parámetro de penalización (comúnmente llamado $C$).
### Un detalle clave sobre los Vectores de Soporte aquí:
Recuerdas que antes dijimos que los vectores de soporte eran _solo_ los puntos que tocaban el borde del margen? En el SVC, al ser un margen blando, los **vectores de soporte se expanden**:
- Los puntos que tocan el borde del margen.
- Todos los puntos que se meten dentro del margen.
- Todos los puntos que cruzan la línea y quedan mal clasificados.
Cualquier observación que viole el margen de alguna forma se convierte automáticamente en un vector de soporte y ayuda a definir la posición final de la línea.
### En resumen:
Esta diapositiva te explica que el SVC prefiere **diseñar una frontera equilibrada y realista permitiendo un par de errores controlados**, en lugar de volverse loco buscando una perfección geométrica imposible que arruinaría la capacidad del modelo para generalizar con datos nuevos.
![[W1_10__Support_Vector_Machine_page-0030.jpg]]

![[W1_10__Support_Vector_Machine_page-0031.jpg]]

![[W1_10__Support_Vector_Machine_page-0032.jpg]]

![[W1_10__Support_Vector_Machine_page-0033.jpg]]

![[W1_10__Support_Vector_Machine_page-0034.jpg]]
### 1. ¿Qué son las variables de holgura ($\xi_i$)?
Arriba en la diapositiva ves la expresión $\xi_i \geq 0$ (se lee "xi sub i"). Cada observación de tu dataset tiene su propia variable de holgura:
- Si $\xi_i = 0$, el punto está perfectamente clasificado y fuera del margen (cumple la regla estricta).
- Si $0 < \xi_i \leq 1$, el punto violó el margen de seguridad, pero todavía está en el lado correcto de la línea divisoria.
- Si $\xi_i > 1$, el punto es un error total: cruzó el hiperplano y está clasificado en el bando equivocado.
### 2. El rol de $C$: El "presupuesto de errores"
La sumatoria $\sum_{i=1}^{n} \xi_i \leq C$ significa que si sumamos todas las violaciones al margen que cometen los puntos, **el total no puede superar un presupuesto máximo fijado por el valor de $C$**.
Aquí es donde se controla el dilema de **Sesgo vs. Varianza** (los últimos puntos de la diapositiva):
#### Si $C = 0$ (Cero tolerancia):
El presupuesto de errores es nulo. Obligas a todas las variables de holgura $\xi_i$ a ser cero. El modelo se vuelve rígido y se transforma exactamente en el **Maximal Margin Classifier** (MMC). Solo funciona si los datos son perfectamente separables.
#### Si $C$ es bajo (Tolerancia estricta):
- El modelo permite muy pocas violaciones al margen.
- **Margen resultante:** Se vuelve más **estrecho**.
- **Efecto:** El modelo es muy fiel a los datos de entrenamiento. Tiene **bajo sesgo** pero **alta varianza** (riesgo de sobreajuste o _overfitting_ ante el ruido).
#### Si $C$ es alto (Gran tolerancia):
- El modelo es súper permisivo; deja que muchos puntos invadan el margen o queden mal clasificados con tal de mantener una línea suave.
- **Margen resultante:** Se vuelve mucho más **ancho**.
- **Efecto:** Al ignorar los puntos ruidosos y enfocarse en la masa general, el modelo gana estabilidad. Tiene **baja varianza** (generaliza mejor) pero a costa de un **mayor sesgo** en el entrenamiento.
### En resumen:
El parámetro $C$ es la perilla que tú, como desarrollador, mueves mediante **validación cruzada** (Cross-Validation) para encontrar el equilibrio perfecto. Determina si prefieres una frontera que intente imitar con obsesión matemática cada punto del dataset ($C$ bajo) o una frontera más robusta y general que acepte sacrificar algunos datos con tal de tener un margen amplio ($C$ alto).
![[W1_10__Support_Vector_Machine_page-0035.jpg]]

![[W1_10__Support_Vector_Machine_page-0036.jpg]]

![[W1_10__Support_Vector_Machine_page-0037.jpg]]

![[W1_10__Support_Vector_Machine_page-0038.jpg]]

![[W1_10__Support_Vector_Machine_page-0039.jpg]]
### 1. Clasificador de Margen Máximo (MMC)
Es el modelo ideal y el ancestro de todos. Su único objetivo es trazar una línea recta (o hiperplano) que separe perfectamente las dos clases, maximizando el espacio vacío ("margen") entre la línea y los puntos más cercanos.
- **Su debilidad:** Es extremadamente sensible. Si un solo punto de la clase A se mezcla levemente en el territorio de la clase B (ruido), el algoritmo colapsa matemáticamente porque exige que la separación sea perfecta. No sirve para el mundo real.
### 2. Clasificador de Soporte Vectorial (SVC)
También conocido como _Clasificador de Margen Blando_ (_Soft Margin_). Nace para solucionar la rigidez del MMC introduciendo **tolerancia al error**. Sigue trazando una línea recta, pero ahora permite que algunos puntos "violen" el margen (metiéndose dentro de la zona de seguridad o incluso cruzando al bando incorrecto) a cambio de mantener una frontera estable y robusta.
- **El parámetro clave ($C$):** Tú controlas qué tan permisivo es mediante un presupuesto de error ($C$). Si $C$ es muy pequeño o cero, se comporta estrictamente como un MMC. Si $C$ es alto, ensancha el margen tolerando muchas fallas con tal de capturar la tendencia general.
### 3. Máquina de Soporte Vectorial (SVM)
Es la evolución final y la que se usa en la práctica para problemas complejos. ¿Qué pasa si tus datos están distribuidos en forma de espiral, círculos concéntricos o patrones donde una línea recta (por más blanda que sea) comete muchísimos errores?
- **El truco del Kernel:** La SVM toma la estructura del SVC (el margen blando con parámetro $C$) y le añade una **función de Kernel**. El kernel proyecta matemáticamente tus datos a una dimensión mucho más alta donde sí se pueden separar con un corte recto. Al devolver ese corte plano al espacio original, se transforma en una **frontera de decisión curva y ultra flexible**.
![[W1_10__Support_Vector_Machine_page-0040.jpg]]

![[W1_10__Support_Vector_Machine_page-0041.jpg]]
Cuando tenemos problemas que no puedan ser separado por metodo lineal, podemos ampliar la dimensionalidad para encontrar un hiperplano
![[W1_10__Support_Vector_Machine_page-0042.jpg]]

![[W1_10__Support_Vector_Machine_page-0043.jpg]]

![[W1_10__Support_Vector_Machine_page-0044.jpg]]

![[W1_10__Support_Vector_Machine_page-0045.jpg]]

![[W1_10__Support_Vector_Machine_page-0046.jpg]]

![[W1_10__Support_Vector_Machine_page-0047.jpg]]

![[W1_10__Support_Vector_Machine_page-0048.jpg]]

![[W1_10__Support_Vector_Machine_page-0049.jpg]]

![[W1_10__Support_Vector_Machine_page-0050.jpg]]

![[W1_10__Support_Vector_Machine_page-0051.jpg]]

![[W1_10__Support_Vector_Machine_page-0052.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0001.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0002.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0003.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0004.jpg]]
**Las series de tiempo** son algoritmos que  consideran el historias de la variable y para sus predicciones
![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0005.jpg]]
Este nos permite evaluar aspectos mas reales que ocurren en el mundo
![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0006.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0007.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0008.jpg]]
Exploraremos sistemas como **Medias moviles(MA), Modelos autoregresivos(AR) y ARIMA**
![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0009.jpg]]
Asimumos que el futuro sera igual a los ultimos valores observados
![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0010.jpg]]
**La media movil** es un metodo simple que suaviza series de tiempo, para ello usamos una ventana que se refiere que tan al paso tomas los datos, la ventana va recorriendo la serie
![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0011.jpg]]
Ejemplo de **MA** con una ventana de 12
![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0012.jpg]]
Tambien podemos usar el **promedio movil** para predecir un mes que todavia no existe
![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0013.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0014.jpg]]
**Las medias moviles ponderadas(WMA)** le asignan distintos pesos a cada punto de la ventana, permitiendo capturar tendencias mas recientes y el **Suavizado exponencial** hace que los pesos sean mayores en ventanas mas recientes
+ este modelo es solo a corto plazo
![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0015.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0016.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0017.jpg]]
Con estos podemos obtener:
+ **Tendencias($T_t$):** la evolucion, caidas, etc
+ **Estacionalidad($S_t$):** Patrones que se repiten en intervalos regulares
+ **Residuo($R_t$):** variaciones no explicadas por los anteriores, puntos que no encajan en el resto
**Todo lo anterior** se usa para predicciones
![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0018.jpg]]
**La estacionalidad** son patrones fijos y predecibles, mientras que **los ciclos** son fluctuaciones sin periodicidad fija y no son predecibles con *t*, suelen quedar en el residuo 
![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0019.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0020.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0021.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0022.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0023.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0024.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0025.jpg]]
### 1. Modelo Aditivo
En este modelo, simplemente **sumas** los componentes para reconstruir el valor real de la serie:
$$y_t = T_t + S_t + R_t$$
- **La regla de oro:** La amplitud de las fluctuaciones estacionales **se mantiene constante en el tiempo**, sin importar si la tendencia general va hacia arriba o hacia abajo.
- **Ejemplo intuitivo:** Imagina las ventas de una tienda de helados. Si cada verano (estacionalidad) vendes exactamente **$5,000 extra** en comparación con el promedio del año, el modelo es aditivo. Si en el año 1 el promedio era de $10,000, en verano vendes $15,000. Si en el año 5 la tienda creció y el promedio es de $50,000, en verano vendes $55,000. El pico veraniego siempre suma la misma cantidad fija.
### 2. Modelo Multiplicativo
Aquí, los componentes **se multiplican**:
$$y_t = T_t \times S_t \times R_t$$
- **La regla de oro:** La amplitud de las fluctuaciones estacionales **cambia en proporción directa con la tendencia**. Si la tendencia sube, los picos estacionales se vuelven más altos y los valles más profundos (la variación se amplifica).
- **El truco matemático (Tu diapositiva):** Como es multiplicativo, la estacionalidad ($S_t$) y el residuo ($R_t$) no se miden en las mismas unidades físicas que los datos, sino como **porcentajes o factores de escala**. Por eso para aislar la tendencia divides la serie por la estacionalidad ($y_t / S_t$), y el residuo se calcula dividiendo el valor real por la multiplicación de los otros dos ($R_t = \frac{y_t}{T_t \times S_t}$).
- **Ejemplo intuitivo:** Volvamos a la heladería. El verano no te da una cantidad fija de dinero, sino que **duplica tus ventas habituales** ($S_{\text{verano}} = 2.0$). Si el promedio inicial es de $10,000, en verano vendes $20,000 (un pico de +$10,000). Pero si en el año 5 tu promedio subió a $50,000, en verano vendes $100,000 (¡un pico de +$50,000!). El gráfico se va abriendo como un abanico.
**Todo esto pertence a los promedios moviles**
![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0026.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0027.jpg]]
**Los modelos autorregresivos(AR)** modelan series temporales donde el valor actual depende linealmente de los valores pesados
![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0028.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0029.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0030.jpg]]
Los valores de entradas se multiplica por un peso y se le suma un intercepto, a diferencias del **MA** trata de reducir el error cuadratico medio, no es necesario que sume uno e incluye el intercepto
![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0031.jpg]]
**El modelo AR** asume que es estacionaria la serie, o sea que la media y la varianza son constante en el tiempo, no muestra tenndencias ni estacionalidad persistentes
![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0032.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0033.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0034.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0035.jpg]]
### 1. El problema: La Estacionariedad
Un modelo autorregresivo clásico (**AR**) tiene una regla matemática estricta: **la serie temporal debe ser estacionaria**. Esto significa que su media, su varianza y su co-varianza no deben cambiar a lo largo del tiempo (gráficamente, la serie debe fluctuar de forma constante alrededor de una línea horizontal fija).
- **El problema real:** La inmensa mayoría de las series de tiempo del mundo real (como el precio de una acción, el PIB o el crecimiento de usuarios de una app) **no son estacionarias**: tienen tendencias alcistas o bajistas estables.
- Si le aplicas un modelo **AR** directo a una serie con tendencia, las predicciones matemáticamente fallarán por completo.
### 2. La solución: Diferenciación
Para eliminar la tendencia y forzar a la serie a volverse horizontal (estacionaria), en lugar de analizar los valores absolutos directamente, calculas la **variación o cambio neto entre un periodo y el anterior**.
$$\Delta Y_t = Y_t - Y_{t-1}$$
- **El grado de diferenciación ($dd$):** Si diferencias una vez ($d=1$) y la serie todavía mantiene una ligera curva o tendencia, puedes volver a aplicar el proceso sobre la serie ya diferenciada ($\Delta(\Delta Y_t)$). A esto se le conoce como **grado de diferenciación**. Típicamente con $d=1$ o $d=2$ es suficiente para limpiar cualquier tendencia.
### 3. Diferencia entre un AR normal y este enfoque (AR con Diferenciación / ARI)
La diferencia estructural en las ecuaciones te lo dejará clarísimo:
#### Modelo AR(1) Normal (Sin Diferenciación)
Intenta predecir el valor absoluto de hoy ($Y_t$) usando una proporción del valor absoluto de ayer ($Y_{t-1}$):
$$Y_t = c + \phi_1 Y_{t-1} + \epsilon_t$$
- **Cuándo se usa:** Solo si tus datos originales ya fluctúan en un canal plano sin ninguna tendencia.
#### Modelo ARI(1, 1) (AR con 1 grado de Diferenciación)
Como los datos originales tenían tendencia, primero aplicamos la resta ($Y_t - Y_{t-1}$). El modelo ahora predice el **cambio o crecimiento de hoy** basándose en el **cambio o crecimiento que hubo ayer**:
$$\Delta Y_t = c + \phi_1 \Delta Y_{t-1} + \epsilon_t$$
$$(Y_t - Y_{t-1}) = c + \phi_1 (Y_{t-1} - Y_{t-2}) + \epsilon_t$$
- **Cuándo se usa:** Siempre que tus datos muestren una tendencia marcada a subir o bajar en el tiempo.
### En resumen:
La diferencia es que el **AR normal** trabaja con los datos en bruto y asume que no tienen tendencia; mientras que este enfoque **"estabiliza" la serie primero mediante restas consecutivas (diferenciación)** para luego poder aplicar de forma segura la lógica autorregresiva sobre las puras variaciones limpias. Al final, el software simplemente "reinvierte" la resta para entregarte la proyección en los niveles reales de la serie original.
![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0036.jpg]]
Para la prueba reservamos una muestra aleatoria, por ejemplo los ultimos 12 meses y con eso evaluamos el modelo, penalizamos los errores con el RMSE
![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0037.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0038.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0039.jpg]]
**ARIMA:** combina autorregresion, integración y media movil
**SARIMA:** extiende ARIMA incorporando estacionalidades explicitas
**SARIMAX:** incluye variables que estan fuera de la serie que queremos modelar
**Prophet:** modelo aditivo que incorpora multiples estacionalidades y eventos especiales
![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0040.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0041.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0042.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0043.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0044.jpg]]
Si bien podemos usar modelos clasicos para predecir secuencias temporales hay que cambiar el enfoque y definir una ventana en donde los meses por ejemplo sean los inputs, esto puede capturar patrones pero carece de memoria, por eso tenemos opciones como **LSTM(Long Short-Term Memory), GRU(Gated Recurrent Unit), CNNs temporales y Transformers para series de tiempo**
![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0045.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0046.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0047.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0048.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0049.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0050.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0051.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0052.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0053.jpg]]
### 1. La definición formal ($h(k) = n_k$)
Imagina una imagen en blanco y negro (escala de grises).
- **$k$ representa el nivel de gris:** Va desde `0` (negro absoluto) hasta un valor máximo $L$ (blanco puro). En las imágenes digitales típicas de 8 bits, $L = 255$, por lo que tienes 256 niveles posibles de gris.
- **$n_k$ es el contador de píxeles:** Te dice cuántos píxeles de toda la imagen tienen exactamente el tono de gris $k$.
- **$h(k)$ es la función del histograma:** Si graficas esto, el eje horizontal ($X$) muestra los tonos de gris (de negro a blanco) y el eje vertical ($Y$) muestra la cantidad de píxeles.
### 2. El Histograma Normalizado ($p(k) = \frac{n_k}{n}$)
El segundo y tercer punto explican un truco estadístico muy usado. Si tienes una imagen gigante de $4000 \times 3000$ píxeles y otra pequeña de $400 \times 300$, sus histogramas directos se verán altísimos en una y bajísimos en la otra, haciendo imposible compararlas matemáticamente aunque sean la misma foto.
Para solucionarlo, se calcula la **versión normalizada**: divides la cantidad de píxeles de cada tono ($n_k$) por el **número total de píxeles que tiene la imagen ($n$)**.
- Al hacer esto, los valores del eje $Y$ ya no son cantidades absolutas, sino que quedan acotados en un rango de **0 a 1** (o de 0% a 100%).
- **La interpretación probabilística:** Como bien dice la slide, puedes interpretar $p(k)$ como **la probabilidad de que, si eliges un píxel al azar en esa imagen, este sea del color o tono de gris $k$**.
### 3. ¿Para qué sirve? Aplicación en Segmentación en Tiempo Real
El último punto destaca por qué es una herramienta tan potente. El histograma te da una "radiografía" instantánea de la iluminación y el contraste de una escena:
- Si las barras están todas agrupadas a la izquierda, la imagen es muy oscura.
- Si están agrupadas a la derecha, está muy iluminada o sobreexpuesta.
- Si hay dos "montañas" muy claras y separadas (por ejemplo, una montaña de píxeles oscuros y otra de píxeles claros), tienes una imagen con un objeto oscuro sobre un fondo claro.
Esto último permite hacer **Segmentación por Umbralización (Thresholding)**: puedes decirle a la computadora _"busca el punto medio entre las dos montañas del histograma y corta la imagen ahí; todo lo que sea más oscuro es el fondo y todo lo que sea más claro es el objeto"_.
Como calcular un histograma es simplemente recorrer la matriz de la imagen contando píxeles, es una operación **súper rápida y de muy bajo costo computacional**, ideal para algoritmos de visión artificial que necesitan correr en **tiempo real** (como cámaras de seguridad, sensores industriales o filtros de video).
![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0054.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0055.jpg]]

![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0056.jpg]]
### 1. El concepto geométrico y el rango $[0, 1]$
La Distancia de Bhattacharyya mide el **grado de superposición (overlap)** entre dos distribuciones estadísticas (en este caso, tus dos histogramas, $h_1$ y $h_2$).
- Entrega un valor normalizado que va **estrictamente entre 0 y 1**.
- **Si el resultado es 0:** Significa que los dos histogramas son **idénticos** (tienen la misma forma exacta, cero distancia).
- **Si el resultado es 1:** Significa que los histogramas son **completamente disjuntos** (no comparten ningún tono, por ejemplo, uno es puramente negro y el otro puramente blanco; distancia máxima).
### 2. La ecuación matemática
La fórmula que ves en la slide es:
$$D_B(h_1, h_2) = \sqrt{1 - \sum_{i=1}^{N} \sqrt{h_1^{(i)} \times h_2^{(i)}}}$$
- **$N$:** Es el número de "bins" o barras que tienen tus histogramas.
- **La sumatoria ($\sum \sqrt{h_1 \times h_2}$):** Se conoce como el _Coeficiente de Bhattacharyya_. Multiplica barra por barra el valor del primer histograma con el del segundo. Si en un tono gris específico ambos histogramas tienen muchos píxeles, esa multiplicación da un número grande; si uno de los dos tiene cero, se anula. Es una medida de **similitud**.
- **El complemento ($1 - \text{similitud}$):** Al restarle esa similitud a $1$, transformas la métrica de "qué tan parecidos son" a **"qué tan distantes están"**.
### 3. El código en C++ (El bloque azul)
El recuadro azul te muestra una implementación real y limpia en código (utilizando tipos de datos `float` y `double`)
- El ciclo `for` calcula el Coeficiente de Bhattacharyya acumulando la raíz cuadrada de la multiplicación de cada posición de los arreglos (`D += sqrt(h1[i] * h2[i])`).
- Al final, la línea `return 1 - D < 0 ? 0.0 : sqrt(1 - D);` es un control de seguridad numérica por si acaso por errores de redondeo flotante `1 - D` diera un número negativo muy pequeño, evitando que la función `sqrt` (raíz cuadrada) falle. Devuelve el valor final de la distancia.
### 4. ¿Para qué se usa en la práctica? (El último punto)
Como dice la frase final: _"Se puede usar para clasificar regiones, según objetos de interés"_.
Imagina que estás construyendo un algoritmo para rastrear una pelota de tenis amarilla en un video:
1. Calculas el histograma de referencia de la pelota (tu objetivo).
2. En el siguiente fotograma del video, analizas diferentes regiones o ventanas de la imagen y calculas sus respectivos histogramas.
3. Calculas la **Distancia de Bhattacharyya** entre el histograma de referencia y el de cada ventana.
4. La región de la imagen que entregue la **distancia más cercana a 0** es, con altísima probabilidad, la pelota que estás buscando.
Es una técnica clásica y sumamente eficiente para tareas de seguimiento (_tracking_), segmentación de texturas y recuperación de imágenes por contenido.
![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0057.jpg]]
### 1. Los Parámetros de la Función `cv::threshold`
- **`src` y `dst`:** La imagen de entrada (`source`) y dónde se guardará el resultado (`destination`). Tienen que ser de un solo canal (habitualmente escala de grises).
- **`threshold`:** El valor límite o corte (la línea roja punteada en los gráficos).
- **`max_value`:** El valor que se le asignará al píxel si cumple la condición del algoritmo (por ejemplo, `255` para volverlo blanco puro).
- **`type`:** El número que define la estrategia matemática que se va a aplicar.
### 2. Los Métodos Visualizados en las Gráficas
Imagina que la línea azul u ondulada de la primera gráfica (`Original`) representa los niveles de gris de una fila de píxeles. La línea roja punteada es tu umbral. Mira cómo cambia según el `type`:
- **0: Binario (`Binary`):** * _La regla:_ Todo lo que esté por **encima** del umbral se convierte en el valor máximo (blanco) y todo lo que esté por **debajo** se vuelve `0` (negro). El resultado es puramente blanco o negro (una onda cuadrada perfecta).
- **1: Binario Invertido (`Binary Inverted`):** * _La regla:_ Al revés del anterior. Lo que está por **debajo** del umbral se vuelve blanco y lo que está por **arriba** se vuelve negro.
- **2: Truncado (`Truncated`):** * _La regla:_ Todo lo que supere al umbral "se corta" y se queda exactamente en el valor del umbral. Lo que esté por debajo del umbral no se toca, mantiene sus valores originales. Por eso la gráfica se ve plana arriba pero conserva las curvas abajo.
- **3: Umbral a Cero (`To Zero`):** * _La regla:_ Si el píxel está por **debajo** del umbral, se destruye (se vuelve `0`, negro). Si está por **encima**, no se altera en absoluto, mantiene su tono original. (Ideal para limpiar ruidos oscuros de fondo manteniendo los detalles del objeto luminoso).
### ¿Cómo se conecta esto con el examen o laboratorio?
Si en el código de tu proyecto necesitas separar, por ejemplo, un texto negro sobre una hoja blanca, usas `cv::threshold` con tipo `0` o `1`. Al elegir el valor del corte en base al punto medio del histograma, puedes convertir toda la imagen en una máscara binaria ultra limpia de alto contraste, facilitando que el algoritmo reconozca las formas en tiempo real.
![[W1_12__Basic_Image_Processing_and_Time_Series_Analysis_page-0058.jpg]]
![[W1_13__Deployment_page-0001.jpg]]

![[W1_13__Deployment_page-0002.jpg]]

![[W1_13__Deployment_page-0003.jpg]]

![[W1_13__Deployment_page-0004.jpg]]

![[W1_13__Deployment_page-0005.jpg]]

![[W1_13__Deployment_page-0006.jpg]]

![[W1_13__Deployment_page-0007.jpg]]
Un **sistema embebido** (o sistema empotrado/integrado) es un sistema de computación diseñado para realizar **una función específica o un conjunto muy limitado de tareas dedicadas**, frecuentemente dentro de un sistema mecánico o eléctrico más grande.
![[W1_13__Deployment_page-0008.jpg]]

![[W1_13__Deployment_page-0009.jpg]]

![[W1_13__Deployment_page-0010.jpg]]

![[W1_13__Deployment_page-0011.jpg]]

![[W1_13__Deployment_page-0012.jpg]]

![[W1_13__Deployment_page-0013.jpg]]

![[W1_13__Deployment_page-0014.jpg]]

![[W1_13__Deployment_page-0015.jpg]]

![[W1_13__Deployment_page-0016.jpg]]

![[W1_13__Deployment_page-0017.jpg]]

![[W1_13__Deployment_page-0018.jpg]]

![[W1_13__Deployment_page-0019.jpg]]

![[W1_13__Deployment_page-0020.jpg]]

![[W1_13__Deployment_page-0021.jpg]]

![[W1_13__Deployment_page-0022.jpg]]

![[W1_13__Deployment_page-0023.jpg]]

![[W1_13__Deployment_page-0024.jpg]]

![[W1_13__Deployment_page-0025.jpg]]

![[W1_13__Deployment_page-0026.jpg]]

![[W1_13__Deployment_page-0027.jpg]]

![[W1_13__Deployment_page-0028.jpg]]

![[W1_13__Deployment_page-0029.jpg]]

![[W1_13__Deployment_page-0030.jpg]]

![[W1_13__Deployment_page-0031.jpg]]

![[W1_13__Deployment_page-0032.jpg]]

![[W1_13__Deployment_page-0033.jpg]]

![[W1_13__Deployment_page-0034.jpg]]

![[W1_13__Deployment_page-0035.jpg]]

![[W1_13__Deployment_page-0036.jpg]]

![[W1_13__Deployment_page-0037.jpg]]

![[W1_13__Deployment_page-0038.jpg]]

![[W1_13__Deployment_page-0039.jpg]]

![[W1_13__Deployment_page-0040.jpg]]

![[W1_13__Deployment_page-0041.jpg]]

![[W1_13__Deployment_page-0042.jpg]]

![[W1_13__Deployment_page-0043.jpg]]

![[W1_13__Deployment_page-0044.jpg]]

![[W1_13__Deployment_page-0045.jpg]]

![[W1_13__Deployment_page-0046.jpg]]

![[W1_13__Deployment_page-0047.jpg]]

![[W1_13__Deployment_page-0048.jpg]]

![[W1_13__Deployment_page-0049.jpg]]

![[W1_13__Deployment_page-0050.jpg]]

![[W1_13__Deployment_page-0051.jpg]]

![[W1_13__Deployment_page-0052.jpg]]

![[W1_13__Deployment_page-0053.jpg]]

![[W1_13__Deployment_page-0054.jpg]]

![[W1_13__Deployment_page-0055.jpg]]

![[W1_13__Deployment_page-0056.jpg]]

