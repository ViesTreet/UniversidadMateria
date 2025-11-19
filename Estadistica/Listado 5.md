1. Por invertir en unas acciones en particular, una persona puede obtener ganancias de $4000 con una probabilidad de 0.3; o una pérdida de $1000 con una probabilidad de 0.7 ¿Cuál es la ganancia que espera esta persona?
$$E[X]=\sum x_i*p_i$$
$$E[X]=(4000)(0.3)+(-1000)(0.7)$$
$$E[X]=500$$
Se espera una ganancia de 500
*¿Qué es la esperanza?
La **esperanza matemática** es el **promedio teórico** que se obtendría si el experimento se repitiera muchísimas veces.*
![[Pasted image 20251118011038.png]]
*Discreta*
![[Pasted image 20251118011103.png]]
*Continua*

2. Suponga que un distribuidor de joyas antiguas está interesado en comprar un collar de oro para el cual las probabilidades son 0.22; 0.36; 0.28 y 0.14 respectivamente, de que la poseedora estaría dispuesta a venderla en $250000, en $150000, al costo $100000 o con una pérdida de $150000 ¿Cuál es la utilidad que ella espera?
$$E[X]=(0.22*250000)+(0.36*150000)+(0.28*100000)+(0.14*-150000)$$
$$E[X]=116000$$
3. Si la utilidad de un distribuidor , en unidades de $1000, en un nuevo automóvil puede considerarse como una variable aleatoria X con función de densidad:
	$$f(x)=2(1-x),0\leq x\leq 1$$
	$$f(x)=0,enOtroCaso$$
	Encuentre la utilidad promedio por automóvil.
$$E[X]=\int_{0}^{1}x*2(1-x)dx$$
$$E[X]=\frac{1}{3}$$
$$\frac{1}{3}*1000=333.33$$
4. Si X representa el resultado cuando se lanza un dado balanceado. Encuentre la esperanza y la varianza de la variable $g(X)=3X^2+4$  
$$x\in[1,2,3,4,5,6]$$
$$v.a=\frac{1}{6}$$
**Esperanza:**

| x   | $g(x)=3x^2+4$ |
| --- | ------------- |
| 1   | 7             |
| 2   | 16            |
| 3   | 31            |
| 4   | 52            |
| 5   | 79            |
| 6   | 112           |
$E[g(X)]=\frac{1}{6}(7+16+31+52+79+112)$
$E[g(X)]=49.5$

**Varianza**

| x   | $g(x)^2$      |
| --- | ------------- |
| 1   | $7^2=49$      |
| 2   | $16^2=256$    |
| 3   | $31^2=961$    |
| 4   | $52^2=2704$   |
| 5   | $79^2=6241$   |
| 6   | $112^2=12544$ |
$$Var(g(X))=E[g(X)^2]-(E[g(X)])^2$$

$$E[g(X)^2]=\frac{1}{6}(49+256+961+2704+6241+12544)=\frac{18755}{6}$$

$$(E[g(X)])^2=49.5^2=2450.25$$

$$Var(g(X))=\frac{18755}{6}-2450.25$$
$$Var(g(X))=675.58$$

**Hipotetico**
![[Pasted image 20251119061141.png]]
![[Pasted image 20251119061152.png]]
![[Pasted image 20251119061214.png]]

8. Se sabe que el 30 % de las piezas defectuosas de un proceso de manufactura pueden quedar bien mediante un trabajo de reprocesado
- ¿Cuál es la probabilidad de que en un lote de seis piezas defectuosas se puedan reprocesar por lo menos tres de ellas?
**Usamos distribución binomial:** 
$X\sim \mathrm{Binomial}(n=6,p=0.3)$
$P(X=k)={n \choose k}p^k(1-p)^{n-k}$
$P(X\geq 3)=1-P(X\leq 2)=1-[P(0)+P(1)+P(2)]$
$P(0)={6 \choose 0}(0.3)^0(0.7)^6=1\cdot 1\cdot 0.117649=0.1176$
$P(1)={6 \choose 1}(0.3)^1(0.7)^5=6\cdot 0.3\cdot 0.16807=0.3025$
$P(2)={6 \choose 2}(0.3)^2(0.7)^4=15\cdot 0.09\cdot 0.2401=0.3241$
$P(X\leq 2)=0.1176+0.3025+0.3241=0.7442$
**Recordar que:**
${n \choose k}=\frac{n!}{k!(n-k)!}$ 
entonces:
$P(X\geq 3)=1-0.7442=0.2558$

- ¿Cuál es la probabilidad de que ninguna de ellas se puedan reprocesar?
$P(0)={6 \choose 0}(0.3)^0(0.7)^6=1\cdot 1\cdot 0.117649=0.1176$
- ¿Cuál es la probabilidad de que todas ellas se puedan reprocesar?
$P(2)={6 \choose 6}(0.3)^6(0.7)^0=1\cdot 0.000729\cdot 1=0.000729$
14. Las piezas de pan de centeno distribuidas a las tiendas locales por una cierta pastelería tienen una longitud promedio de 30 cm. y una desviación estándar de 2 cm. Suponiendo que las longitudes están normalmente distribuidas, ¿Qué porcentaje de las piezas son
* de más de 31.7 cm de longitud?
Media: $\mu=30$ cm
Desviación estándar= $\sigma =2$ cm
Distribución: $X \sim N(30,2^2)$

$Z=\frac{X-\mu}{\sigma}$

$Z\frac{31.7-30}{2}=0.85$
$P(X>31.7)=P(Z>0.85)$
en la tabla se establece que 0.85 es 0.8023
$P(X>31.7)=(1-0.8023)*100=19.77$
* entre 29.3 y 33.5 cm de longitud?
Para 29.3: $Z=\frac{29.3-30}{2}=-0.35$
Para 33.5: $Z=\frac{33.5-30}{2}=1.75$
$P(-0.35<Z<1.75)=(P(Z<1.75)-P(Z<-0.35))*100=59.97$

* de una longitud menor que 25.5 cm?
$Z=\frac{25.5-30}{2}=-2.25$
aproximadamente 1.22
*En la tabla no aparece negativo, por lo que seria 1-valor de la tabla*
