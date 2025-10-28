<h1 style="text-align:center">Repaso</h1>
# Cinemática

Se refiere a la descripción del movimiento de un objeto sin considerar las fuerzas que originan el movimiento. Se utilizan cantidades físicas como velocidad y aceleración.

**Distancia recorrida:** Es la distancia que se abarca a través de la trayectoria. 

**Rapidez media $v_m$:** es un ESCALAR definido como distancia recorrida dividida en el tiempo se usa (m/s):
$$v_m=\frac{d}{t}$$

**Posición $\vec{r}$:** Vector que va desde el origen hasta la ubicación del objeto.

**Desplazamiento $\Delta{\vec{r}}$:** Vector que va desde una posición inicial hasta una final.

**Velocidad media $\vec{v}$:** Es un vector que se define como el desplazamiento dividido por el tiempo, se mide en (m/s):
$$\vec{v}=\frac{\Delta{\vec{r}}}{t}$$

**Aceleración $\vec{a}$:** Vector que indica el cambio de velocidad durante una cantidad de tiempo.
$$\vec{a}=\frac{\Delta{\vec{v}}}{t}$$

#### Cantidades físicas en 1 dimensión:

Si el movimiento ocurre en una sola dimensión no es necesario usar vectores, a esto se le llama "forma escalar". 
* **Velocidad:** $v(t)=v_i+at$
* **Posición:** $r(t)=r_i+v_it$ 
* **Ecuación auxiliar:** $v_{f}^{2}=v_i^2+2ad$ 

#### MRUA y MRUR:

Cuando nos referimos a MRUA nos referimos a un movimiento que se acelera y cuando nos referimos a MRUR nos referimos a un movimiento retardado.

##### Movimientos de proyectiles:

Se refiere al movimiento de un objeto que queda a merced de la fuerza de la gravedad después que se lanza, el eje x tiene **MRU** y el eje vertical y tiene **MRUA o MRUR** dependiendo si sube o bajada.
![[Pasted image 20251026184453.png]]
La velocidad inicial debe separarse en sus componentes.
![[Pasted image 20251026184722.png]]

# Movimiento circular
### Radianes

Forma de medir ángulos:
$$2\pi rad=360°$$
$$1 rad\approx 57.3°$$
Es la razón entre el radio del circulo y el Angulo que se abarca.
$$\theta=\frac{s}{r}$$
donde s es la superficie del circulo, también llamada longitud de arco o amplitud.
![[Pasted image 20251026185403.png]]
una formula auxiliar muy útil es:
$$s=r\theta$$ 
### Cantidades físicas básicas:
* Periodo(T): tiempo en dar una vuelta o revolución completa
$$T=\frac{t}{rev}$$
* Frecuencia(f): Cantidad de vueltas en un tiempo determinado
$$f=\frac{rev}{t}$$
se usan unidades de medida como rev/s=rps=hz.
* Rapidez angular($\omega$): Angulo que recorre en una cierta cantidad de tiempo. 
$$\omega=\frac{\Delta{\theta}}{t}$$
$$\omega=\frac{2\pi}{T}=2\pi{f}$$

* Rapidez tangencial o lineal: es la velocidad a cierta distancia del centro, se mide en (m/s):
$$v=\omega*r$$

##### Correas de transmisión:

Se usa para transmitir potencia entre dos ejes, la relación básica es:
$$v_A=v_B$$
es decir:
$$\omega_A*r_A=\omega_B*r_B$$

* Aceleración centrípeta: aceleración que va hacia el centro cuando un objeto gira en círculos.
$$a_c=\frac{v^2}{r}=\omega^2*r$$
* Aceleración angular: se relaciona con el cambio de rapidez angular.
$$\alpha=\frac{\Delta{\omega}}{t}$$

### Ecuaciones de rapidez angular y de dirección

Similar al MRUR y al MRUA, pero en movimientos circulares:
$$\omega(t)=\omega_0+\alpha{t}$$
$$\theta(t)=\theta_{0}+\omega_{0}t+\frac{\alpha{t}^2}{2}$$

# Leyes de newton
* **Primera ley:** Todo objeto continua en reposo o en MRU hasta que se aplique una fuerza:
$$\sum{\vec{F}}=0$$
* **Segunda ley:** La aceleración es proporcional a la fuerza neta:
$$\sum{\vec{F}}=ma$$
* **Tercera ley:** Cuando un objeto ejerce fuerza sobre otro, el otro objeto ejerce fuerza sobre el primero.

# Trabajo y energía mecánica

**Energía:** Es una cantidad escalar, que sea asocia a un sistema de uno mas objetos.

* **Trabajo(W):** se define como la energía transferida desde un objeto hacia otro a través de una fuerza que actúa sobre el. La energía transferida hacia el objeto es W **positivo** y la energía transferida desde el objeto representa W **negativo** 
$$W=Fdcos(\theta)$$
![[Pasted image 20251028000254.png]]
corresponde en términos simples al producto punto entre el vector fuerza y el vector desplazamiento.
$$W=\int_{x_1}^{x_2}F(x)dx$$
![[Pasted image 20251028000504.png]]

* **Potencia mecánica:** Se refiere a la "rapidez" con la que se realiza un trabajo mecánico:
$$p=\frac{W}{t}$$

* **Energía cinética:**  capacidad de realizar trabajo debido al movimiento:
$$K=\frac{1}{2}mv^2$$
* **Teorema del trabajo y la energía cinética:** Se puede relacionar el trabajo realizado sobre un objeto con el CAMBIO de su energía cinética:
$$W=\Delta{K}=\frac{m}{2}(v_2^2-v_1^2)$$
* **Energía total:** Es la suma de las dos energía, energía potencial y la energía cinética.