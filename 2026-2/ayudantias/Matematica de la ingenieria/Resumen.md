---
title: "Matrices y Determinantes — Ayudantía"
subtitle: "MAT021B — Matemática de Ingeniería"
---
---
title: "Matrices y Determinantes — Ayudantía"
subtitle: "MAT021B — Matemática de Ingeniería"
---

# Matrices y Determinantes

> Apunte de ayudantía: teoría + resolución completa de la Práctica 2.

---

## 1. ¿Qué es una matriz?

Una **matriz** $A$ de orden $m \times n$ es un arreglo rectangular de números distribuido en $m$ **filas** y $n$ **columnas**:

$$
A = \begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}
$$

Cada $a_{ij}$ es una **entrada**: el subíndice $i$ indica la fila, el subíndice $j$ la columna. Si $m = n$, la matriz se llama **cuadrada** de orden $n$.

> **Truco para recordar el orden**  
> $A$ es de orden $\color{blue}{m} \times \color{red}{n}$ → primero **filas** (azul), después **columnas** (rojo). "Filas por columnas", como en el cine: fila 3, asiento (columna) 5.

**Ejemplo.** $A = \begin{pmatrix} 2 & -3 \\ -4 & 5 \\ 7 & -1 \end{pmatrix}$ es de orden $3\times2$ (3 filas, 2 columnas).

---

## 2. Operaciones entre matrices

### 2.1 Suma y resta

Solo se pueden sumar/restar matrices **del mismo orden**, sumando (restando) entrada a entrada:

$$A + B = (a_{ij} + b_{ij})_{m\times n}$$

**Ejemplo.**
$$
\begin{pmatrix} 2 & -3 \\ 0 & 5 \\ 7 & -1 \end{pmatrix} + \begin{pmatrix} 1 & 0 \\ -3 & 1 \\ 2 & 2 \end{pmatrix} = \begin{pmatrix} 3 & -3 \\ -3 & 6 \\ 9 & 1 \end{pmatrix}
$$

La **matriz nula** $O_{m\times n}$ (puros ceros) es el neutro aditivo: $A + O = A$.

### 2.2 Producto por escalar

$$\alpha A = (\alpha \, a_{ij})_{m\times n}$$

Se multiplica **cada entrada** por el escalar $\alpha$.

### 2.3 Producto de matrices — la parte que hay que dominar

> **Regla de compatibilidad**  
> El producto $A \cdot B$ **solo existe** si el número de **columnas de $A$** coincide con el número de **filas de $B$**.

$$
\underbrace{A}_{\color{blue}{m}\ \times\ \color{#e74c3c}{n}} \quad \cdot \quad \underbrace{B}_{\color{#e74c3c}{n}\ \times\ \color{blue}{p}} \quad = \quad \underbrace{C}_{\color{blue}{m}\ \times\ \color{blue}{p}}
$$

- 🔴 Los números **rojos** ($n$) deben ser **iguales**: eso es lo que se revisa para saber si "se puede multiplicar".
- 🔵 Los números **azules** ($m$ y $p$) sobreviven y forman el **orden del resultado** $C$.

> **Regla mnemotécnica**  
> Escribe los dos órdenes seguidos: $(m \times \color{#e74c3c}{n})(\color{#e74c3c}{n} \times p)$. Si los números del medio (rojos) **chocan y son iguales**, se cancelan, y quedan los de las puntas (azules): el resultado es $m \times p$.

**¿Cómo se calcula cada entrada del resultado?**

Cada entrada $c_{ij}$ de $C = AB$ se obtiene multiplicando la **fila $i$ de $A$** por la **columna $j$ de $B$**, término a término, y sumando.

**Ejemplo (2×3 por 3×3):**
$$
A = \begin{pmatrix} \color{blue}{-1} & \color{blue}{0} & \color{blue}{2} \\ 2 & -1 & -3 \end{pmatrix}_{2\times 3}
\qquad
B = \begin{pmatrix} \color{#e74c3c}{3} & 1 & -2 \\ \color{#e74c3c}{1} & -1 & 2 \\ \color{#e74c3c}{2} & -2 & 0 \end{pmatrix}_{3\times 3}
$$

Como $A$ tiene 3 columnas y $B$ tiene 3 filas → **sí se puede multiplicar**, y el resultado será de orden $2\times 3$.

Para obtener $c_{11}$ (fila 1 de $A$ 🔵, columna 1 de $B$ 🔴):

$$
c_{11} = \color{blue}{(-1)}\cdot\color{#e74c3c}{3} + \color{blue}{(0)}\cdot\color{#e74c3c}{1} + \color{blue}{(2)}\cdot\color{#e74c3c}{2} = -3+0+4 = 1
$$

Repitiendo fila por columna para cada casillero se obtiene:

$$
AB = \begin{pmatrix} 1 & -5 & 2 \\ -1 & 9 & -6 \end{pmatrix}
$$

> **Ojo**  
> El producto de matrices **no es conmutativo**: en general $AB \neq BA$. De hecho, en el ejemplo anterior, $B \cdot A$ **ni siquiera está definido**, porque $B$ es $3\times3$ y $A$ es $2\times3$: las columnas de $B$ (3) no coinciden con las filas de $A$ (2).

### 2.4 Matriz identidad

$$
I_n = \begin{pmatrix} 1&0&\cdots&0\\0&1&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&1\end{pmatrix}
$$

Es el **neutro multiplicativo**: $A\,I_n = I_n\,A = A$.

### 2.5 Matriz transpuesta

$A^T$ se obtiene intercambiando filas por columnas.

**Ejemplo.** Si $A = \begin{pmatrix}-1&7\\5&0\\2&3\end{pmatrix}$ entonces $A^T = \begin{pmatrix}-1&5&2\\7&0&3\end{pmatrix}$.

---

## 3. Determinantes

El determinante $\det(A)$ (o $|A|$) es un número real asociado a **toda matriz cuadrada**. Es la llave que abre la puerta a la matriz inversa.

### 3.1 Caso $2\times 2$

$$
\det\begin{pmatrix}\color{#e74c3c}{a_{11}}&a_{12}\\a_{21}&\color{#e74c3c}{a_{22}}\end{pmatrix} = \color{#e74c3c}{a_{11}a_{22}} - \color{blue}{a_{12}a_{21}}
$$

🔴 diagonal principal (se suma) — 🔵 diagonal secundaria (se resta).

**Ejemplo.** $\det\begin{pmatrix}-3&-2\\4&5\end{pmatrix} = (-3)(5)-(-2)(4) = -15+8=-7$.

### 3.2 Cofactores

El cofactor del elemento $a_{ij}$ es:

$$c_{ij} = (-1)^{i+j}\det(A_{ij})$$

donde $A_{ij}$ es la matriz que queda al **tachar la fila $i$ y la columna $j$**. El signo $(-1)^{i+j}$ sigue un patrón de tablero de ajedrez:

$$
\begin{pmatrix} \color{#e74c3c}{+}&\color{blue}{-}&\color{#e74c3c}{+}&\cdots\\ \color{blue}{-}&\color{#e74c3c}{+}&\color{blue}{-}&\cdots \\ \color{#e74c3c}{+}&\color{blue}{-}&\color{#e74c3c}{+}&\cdots\\ \vdots&\vdots&\vdots&\ddots\end{pmatrix}
$$

### 3.3 Caso general — desarrollo por cofactores

$$\det(A) = \sum_j a_{ij}\,c_{ij} \quad \text{(desarrollando por cualquier fila } i \text{, o análogo por columna)}$$

**Consejo:** elige la fila o columna con **más ceros**, así se anulan varios términos.

### 3.4 Regla de Sarrus (solo para $3\times 3$)

Se repiten las dos primeras columnas a la derecha, y se suman las diagonales 🔴 (hacia abajo-derecha) restando las diagonales 🔵 (hacia abajo-izquierda):

$$
\begin{array}{ccc|cc}
a_{11}&a_{12}&a_{13}&a_{11}&a_{12}\\
a_{21}&a_{22}&a_{23}&a_{21}&a_{22}\\
a_{31}&a_{32}&a_{33}&a_{31}&a_{32}
\end{array}
$$

$$
\det(A)=\color{#e74c3c}{(a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32})} - \color{blue}{(a_{13}a_{22}a_{31}+a_{11}a_{23}a_{32}+a_{12}a_{21}a_{33})}
$$

**Ejemplo.** $A=\begin{pmatrix}1&0&-1\\2&1&-1\\3&2&1\end{pmatrix}$

$$\det(A) = \color{#e74c3c}{[(1)(1)(1)+(0)(-1)(3)+(-1)(2)(2)]} - \color{blue}{[(-1)(1)(3)+(1)(-1)(2)+(0)(2)(1)]} = -3-(-5) = 2$$

---

## 4. Matriz inversa

Dada $A$ cuadrada, buscamos $B$ tal que $A\cdot B = B \cdot A = I_n$. Si existe, $B = A^{-1}$.

> **Teorema (existencia)**  
> $A$ es invertible $\iff \det(A) \neq 0$.

### 4.1 Método 1: operaciones elementales por filas

Se arma la matriz ampliada $[A \mid I_n]$ y se aplican operaciones de fila hasta llegar a $[I_n \mid A^{-1}]$.

Operaciones permitidas: (1) intercambiar filas, (2) multiplicar una fila por $\lambda\neq0$, (3) sumar a una fila un múltiplo de otra.

### 4.2 Método 2: matriz de cofactores

$$A^{-1} = \frac{1}{\det(A)}\big(\mathrm{Cof}(A)\big)^T$$

donde $\mathrm{Cof}(A) = (c_{ij})$ es la matriz de todos los cofactores de $A$ (¡ojo con la transpuesta al final!).

### 4.3 Aplicación: sistemas lineales

Un sistema $AX=b$ se resuelve como $X = A^{-1}b$ (si $A$ es invertible).

---
---

# Práctica 2 — Solución

## Ejercicio 1

Encontrar $k$ tal que $\det(A) = \det(B)$, con

$$A=\begin{pmatrix}k-2&4&25\\0&1&0\\1&0&k-4\end{pmatrix} \qquad B=\begin{pmatrix}k-5&3&4\\1&k+2&2\\1&0&1\end{pmatrix}$$

**Desarrollo de $\det(A)$** (por la fila 2, que tiene dos ceros):

$$\det(A) = 1\cdot(-1)^{2+2}\begin{vmatrix}k-2&25\\1&k-4\end{vmatrix} = (k-2)(k-4)-25 = k^2-6k-17$$

**Desarrollo de $\det(B)$** (por Sarrus o cofactores):

$$\det(B) = k^2-7k-15$$

**Igualando:**

$$k^2-6k-17 = k^2-7k-15 \;\Longrightarrow\; -6k-17=-7k-15 \;\Longrightarrow\; k = 2$$

$$\boxed{k=2}$$

---

## Ejercicio 2

Valores de $a$ para que $A=\begin{pmatrix}1&0&0\\0&a+1&3\\0&4&a-3\end{pmatrix}$ **no** tenga inversa $\iff \det(A)=0$.

Desarrollando por la primera fila (o notando que es un bloque $2\times2$ abajo a la derecha multiplicado por el $1$ de arriba):

$$\det(A) = 1\cdot\big[(a+1)(a-3)-12\big] = a^2-2a-3-12 = a^2-2a-15 = (a-5)(a+3)$$

$$\det(A)=0 \iff a=5 \ \lor\ a=-3$$

$$\boxed{a\in\{-3,\ 5\}}$$

---

## Ejercicio 3 (P)

Valores de $m$ para que $B=\begin{pmatrix}m&1&0\\0&m&2\\\tfrac{3}{2}&2&1\end{pmatrix}$ no tenga inversa.

Por Sarrus:

$$\det(B) = \left[m\cdot m\cdot 1 + 1\cdot2\cdot\tfrac32 + 0\right] - \left[0 + m\cdot2\cdot2 + 1\cdot0\cdot1\right] = \left(m^2+3\right) - 4m = m^2-4m+3$$

$$\det(B)=0 \iff (m-1)(m-3)=0$$

$$\boxed{m\in\{1,\ 3\}}$$

---

## Ejercicio 4 — Inversas por operaciones elementales

### a) $A=\begin{pmatrix}3&4\\5&7\end{pmatrix}$

$$\left(\begin{array}{cc|cc}3&4&1&0\\5&7&0&1\end{array}\right) \xrightarrow[]{F_1 \to \frac13F_1} \left(\begin{array}{cc|cc}1&\tfrac43&\tfrac13&0\\5&7&0&1\end{array}\right)\xrightarrow[]{F_2-5F_1\to F_2}\left(\begin{array}{cc|cc}1&\tfrac43&\tfrac13&0\\0&\tfrac13&-\tfrac53&1\end{array}\right)$$

$$\xrightarrow[]{F_2\to 3F_2} \left(\begin{array}{cc|cc}1&\tfrac43&\tfrac13&0\\0&1&-5&3\end{array}\right)\xrightarrow[]{F_1-\frac43F_2\to F_1}\left(\begin{array}{cc|cc}1&0&7&-4\\0&1&-5&3\end{array}\right)$$

$$\boxed{A^{-1}=\begin{pmatrix}7&-4\\-5&3\end{pmatrix}}$$

*(Verificación rápida con la fórmula $2\times2$: $\det A = 21-20=1$, y $A^{-1}=\dfrac{1}{\det A}\begin{pmatrix}7&-4\\-5&3\end{pmatrix}$ ✓, misma respuesta.)*

### b) $B=\begin{pmatrix}0&-2\\1&5\end{pmatrix}$

Como el $(1,1)$ es $0$, intercambiamos filas primero:

$$\left(\begin{array}{cc|cc}0&-2&1&0\\1&5&0&1\end{array}\right)\xrightarrow[]{F_1\leftrightarrow F_2}\left(\begin{array}{cc|cc}1&5&0&1\\0&-2&1&0\end{array}\right)\xrightarrow[]{F_2\to-\frac12F_2}\left(\begin{array}{cc|cc}1&5&0&1\\0&1&-\tfrac12&0\end{array}\right)$$

$$\xrightarrow[]{F_1-5F_2\to F_1}\left(\begin{array}{cc|cc}1&0&\tfrac52&1\\0&1&-\tfrac12&0\end{array}\right)$$

$$\boxed{B^{-1}=\begin{pmatrix}\tfrac52&1\\-\tfrac12&0\end{pmatrix}}$$

### c) (P) $E=\begin{pmatrix}-1&-4&4\\1&0&1\\2&-1&3\end{pmatrix}$

$$\left(\begin{array}{ccc|ccc}-1&-4&4&1&0&0\\1&0&1&0&1&0\\2&-1&3&0&0&1\end{array}\right)\xrightarrow[F_3+2F_1\to F_3]{F_2+F_1\to F_2}\left(\begin{array}{ccc|ccc}-1&-4&4&1&0&0\\0&-4&5&1&1&0\\0&-9&11&2&0&1\end{array}\right)$$

$$\xrightarrow[]{F_1\to -F_1}\left(\begin{array}{ccc|ccc}1&4&-4&-1&0&0\\0&-4&5&1&1&0\\0&-9&11&2&0&1\end{array}\right)\xrightarrow[]{F_2\to-\frac14F_2}\left(\begin{array}{ccc|ccc}1&4&-4&-1&0&0\\0&1&-\tfrac54&-\tfrac14&-\tfrac14&0\\0&-9&11&2&0&1\end{array}\right)$$

$$\xrightarrow[]{F_3+9F_2\to F_3}\left(\begin{array}{ccc|ccc}1&4&-4&-1&0&0\\0&1&-\tfrac54&-\tfrac14&-\tfrac14&0\\0&0&-\tfrac14&-\tfrac14&-\tfrac94&1\end{array}\right)\xrightarrow[]{F_3\to-4F_3}\left(\begin{array}{ccc|ccc}1&4&-4&-1&0&0\\0&1&-\tfrac54&-\tfrac14&-\tfrac14&0\\0&0&1&1&9&-4\end{array}\right)$$

$$\xrightarrow[F_2+\frac54F_3\to F_2]{F_1+4F_3\to F_1}\left(\begin{array}{ccc|ccc}1&4&0&3&36&-16\\0&1&0&1&11&-5\\0&0&1&1&9&-4\end{array}\right)\xrightarrow[]{F_1-4F_2\to F_1}\left(\begin{array}{ccc|ccc}1&0&0&-1&-8&4\\0&1&0&1&11&-5\\0&0&1&1&9&-4\end{array}\right)$$

$$\boxed{E^{-1}=\begin{pmatrix}-1&-8&4\\1&11&-5\\1&9&-4\end{pmatrix}}$$

---

## Ejercicio 5

$$A=\begin{pmatrix}1&2&-1\\3&0&2\\2&3&-1\end{pmatrix}\qquad B=\begin{pmatrix}1&0\\-1&0\\1&1\end{pmatrix}$$

### a) $A^{-1}$

Primero, $\det(A)$ por Sarrus: $\det(A) = (0+8-9)-(0+6-6)=-1-0=-1\neq0$, así que sí existe.

Por operaciones elementales:

$$\left(\begin{array}{ccc|ccc}1&2&-1&1&0&0\\3&0&2&0&1&0\\2&3&-1&0&0&1\end{array}\right)\xrightarrow[F_3-2F_1\to F_3]{F_2-3F_1\to F_2}\left(\begin{array}{ccc|ccc}1&2&-1&1&0&0\\0&-6&5&-3&1&0\\0&-1&1&-2&0&1\end{array}\right)$$

$$\xrightarrow[]{F_2\leftrightarrow F_3}\left(\begin{array}{ccc|ccc}1&2&-1&1&0&0\\0&-1&1&-2&0&1\\0&-6&5&-3&1&0\end{array}\right)\xrightarrow[]{F_2\to-F_2}\left(\begin{array}{ccc|ccc}1&2&-1&1&0&0\\0&1&-1&2&0&-1\\0&-6&5&-3&1&0\end{array}\right)$$

$$\xrightarrow[]{F_3+6F_2\to F_3}\left(\begin{array}{ccc|ccc}1&2&-1&1&0&0\\0&1&-1&2&0&-1\\0&0&-1&9&1&-6\end{array}\right)\xrightarrow[]{F_3\to-F_3}\left(\begin{array}{ccc|ccc}1&2&-1&1&0&0\\0&1&-1&2&0&-1\\0&0&1&-9&-1&6\end{array}\right)$$

$$\xrightarrow[F_2+F_3\to F_2]{F_1+F_3\to F_1}\left(\begin{array}{ccc|ccc}1&2&0&-8&-1&6\\0&1&0&-7&-1&5\\0&0&1&-9&-1&6\end{array}\right)\xrightarrow[]{F_1-2F_2\to F_1}\left(\begin{array}{ccc|ccc}1&0&0&6&1&-4\\0&1&0&-7&-1&5\\0&0&1&-9&-1&6\end{array}\right)$$

$$\boxed{A^{-1}=\begin{pmatrix}6&1&-4\\-7&-1&5\\-9&-1&6\end{pmatrix}}$$

### b) $X$ tal que $\tfrac12 AX = B$

$$\tfrac12 AX = B \;\Longrightarrow\; AX = 2B \;\Longrightarrow\; X = A^{-1}(2B) = 2\,A^{-1}B$$

$$A^{-1}B = \begin{pmatrix}6&1&-4\\-7&-1&5\\-9&-1&6\end{pmatrix}\begin{pmatrix}1&0\\-1&0\\1&1\end{pmatrix} = \begin{pmatrix}1&-4\\-1&5\\-2&6\end{pmatrix}$$

$$\boxed{X = 2A^{-1}B = \begin{pmatrix}2&-8\\-2&10\\-4&12\end{pmatrix}}$$

---

## Ejercicio 6

Dada $A=\begin{pmatrix}2&-4\\-1&4\end{pmatrix}$, hallar $X$ tal que $XA=\begin{pmatrix}6&-4\\-2&8\end{pmatrix}$.

Como $X$ multiplica a $A$ **por la derecha**, despejamos multiplicando por $A^{-1}$ **por la derecha** en ambos lados:

$$XA = C \;\Longrightarrow\; X = C\,A^{-1}$$

$\det(A) = 8-4=4$, luego $A^{-1} = \dfrac14\begin{pmatrix}4&4\\1&2\end{pmatrix} = \begin{pmatrix}1&1\\ \tfrac14&\tfrac12\end{pmatrix}$

$$X = \begin{pmatrix}6&-4\\-2&8\end{pmatrix}\begin{pmatrix}1&1\\ \tfrac14&\tfrac12\end{pmatrix} = \begin{pmatrix}6-1&6-2\\-2+2&-2+4\end{pmatrix} = \begin{pmatrix}5&4\\0&2\end{pmatrix}$$

$$\boxed{X=\begin{pmatrix}5&4\\0&2\end{pmatrix}}$$

*(Comprobación: $XA = \begin{pmatrix}5&4\\0&2\end{pmatrix}\begin{pmatrix}2&-4\\-1&4\end{pmatrix} = \begin{pmatrix}10-4&-20+16\\0-2&0+8\end{pmatrix}=\begin{pmatrix}6&-4\\-2&8\end{pmatrix}$ ✓)*

---

## Ejercicio 7 — ¿Admiten inversa?

Para cada matriz calculamos primero $\det$; si es $\neq 0$, entregamos $A^{-1}$ usando el **método de cofactores** ($A^{-1}=\frac{1}{\det A}(\mathrm{Cof}\,A)^T$), que es rápido y ordenado para matrices numéricas.

### a) $A=\begin{pmatrix}1&-1\\2&3\end{pmatrix}$

$\det(A) = 3+2=5\neq0$ → **sí tiene inversa**.

$$A^{-1} = \frac15\begin{pmatrix}3&1\\-2&1\end{pmatrix}$$

### b) $B=\begin{pmatrix}3&1&-1\\2&1&0\\1&2&4\end{pmatrix}$

Por Sarrus: $\det(B) = (12+0-4)-(-1+0+8)=8-7=1\neq0$ → **sí tiene inversa**.

Cofactores fila a fila:

$$c_{11}=\begin{vmatrix}1&0\\2&4\end{vmatrix}=4,\; c_{12}=-\begin{vmatrix}2&0\\1&4\end{vmatrix}=-8,\; c_{13}=\begin{vmatrix}2&1\\1&2\end{vmatrix}=3$$
$$c_{21}=-\begin{vmatrix}1&-1\\2&4\end{vmatrix}=-6,\; c_{22}=\begin{vmatrix}3&-1\\1&4\end{vmatrix}=13,\; c_{23}=-\begin{vmatrix}3&1\\1&2\end{vmatrix}=-5$$
$$c_{31}=\begin{vmatrix}1&-1\\1&0\end{vmatrix}=1,\; c_{32}=-\begin{vmatrix}3&-1\\2&0\end{vmatrix}=-2,\; c_{33}=\begin{vmatrix}3&1\\2&1\end{vmatrix}=1$$

$$\mathrm{Cof}(B)=\begin{pmatrix}4&-8&3\\-6&13&-5\\1&-2&1\end{pmatrix} \Longrightarrow B^{-1}=\big(\mathrm{Cof}\,B\big)^T = \begin{pmatrix}4&-6&1\\-8&13&-2\\3&-5&1\end{pmatrix}$$

### c) $C=\begin{pmatrix}1&-1&2\\2&-1&2\\2&3&0\end{pmatrix}$

$\det(C)=6\neq0$ → **sí tiene inversa**.

$$C^{-1} = \begin{pmatrix}-1&1&0\\ \tfrac23&-\tfrac23&\tfrac13\\ \tfrac43&-\tfrac56&\tfrac16\end{pmatrix}$$

### d) $D=\begin{pmatrix}1&0&-1\\2&1&1\\0&1&3\end{pmatrix}$

Por Sarrus: $\det(D) = (3+0-2)-(0+1+0)=1-1=0$

$$\boxed{\det(D)=0 \Rightarrow D \text{ \bf no tiene inversa}}$$

### e) (P) $E=\begin{pmatrix}2&-1&1\\1&1&0\\3&2&1\end{pmatrix}$ — método de cofactores

$$\det(E) = 2\begin{vmatrix}1&0\\2&1\end{vmatrix}-(-1)\begin{vmatrix}1&0\\3&1\end{vmatrix}+1\begin{vmatrix}1&1\\3&2\end{vmatrix}=2(1)+1(1)+1(-1)=2$$

Como $\det(E)=2\neq0$, existe $E^{-1}$. Calculamos **todos** los cofactores:

$$c_{11}=\begin{vmatrix}1&0\\2&1\end{vmatrix}=1,\;\; c_{12}=-\begin{vmatrix}1&0\\3&1\end{vmatrix}=-1,\;\; c_{13}=\begin{vmatrix}1&1\\3&2\end{vmatrix}=-1$$
$$c_{21}=-\begin{vmatrix}-1&1\\2&1\end{vmatrix}=3,\;\; c_{22}=\begin{vmatrix}2&1\\3&1\end{vmatrix}=-1,\;\; c_{23}=-\begin{vmatrix}2&-1\\3&2\end{vmatrix}=-7$$
$$c_{31}=\begin{vmatrix}-1&1\\1&0\end{vmatrix}=-1,\;\; c_{32}=-\begin{vmatrix}2&1\\1&0\end{vmatrix}=1,\;\; c_{33}=\begin{vmatrix}2&-1\\1&1\end{vmatrix}=3$$

$$\mathrm{Cof}(E)=\begin{pmatrix}1&-1&-1\\3&-1&-7\\-1&1&3\end{pmatrix} \Longrightarrow \big(\mathrm{Cof}\,E\big)^T=\begin{pmatrix}1&3&-1\\-1&-1&1\\-1&-7&3\end{pmatrix}$$

$$\boxed{E^{-1}=\frac12\begin{pmatrix}1&3&-1\\-1&-1&1\\-1&-7&3\end{pmatrix}=\begin{pmatrix}\tfrac12&\tfrac32&-\tfrac12\\-\tfrac12&-\tfrac12&\tfrac12\\-\tfrac12&-\tfrac72&\tfrac32\end{pmatrix}}$$

### f) $F=\begin{pmatrix}1&0&-1\\2&1&-1\\0&2&1\end{pmatrix}$

Por Sarrus: $\det(F) = (1+0-4)-(0-2+0)=-3+2=-1\neq0$ → **sí tiene inversa**.

$$F^{-1} = \begin{pmatrix}-3&2&-1\\2&-1&1\\-4&2&-1\end{pmatrix}$$

---

## Ejercicio 8 (P)

$$M=\begin{pmatrix}-1&3&2\\2&1&2\\-2&1&-1\end{pmatrix}\qquad N=\begin{pmatrix}1&0\\0&1\\-1&-1\end{pmatrix}$$

### a) ¿$M$ tiene inversa?

Por Sarrus: $\det(M) = \big[(-1)(1)(-1)+(3)(2)(-2)+(2)(2)(1)\big]-\big[(2)(1)(-2)+(-1)(2)(1)+(3)(2)(-1)\big]$

$$= (1-12+4)-(-4-2-6) = -7-(-12)=5\neq0$$

**Sí tiene inversa.** Usando cofactores:

$$c_{11}=\begin{vmatrix}1&2\\1&-1\end{vmatrix}=-3,\; c_{12}=-\begin{vmatrix}2&2\\-2&-1\end{vmatrix}=-2,\; c_{13}=\begin{vmatrix}2&1\\-2&1\end{vmatrix}=4$$
$$c_{21}=-\begin{vmatrix}3&2\\1&-1\end{vmatrix}=5,\; c_{22}=\begin{vmatrix}-1&2\\-2&-1\end{vmatrix}=5,\; c_{23}=-\begin{vmatrix}-1&3\\-2&1\end{vmatrix}=-5$$
$$c_{31}=\begin{vmatrix}3&2\\1&2\end{vmatrix}=4,\; c_{32}=-\begin{vmatrix}-1&2\\2&2\end{vmatrix}=6,\; c_{33}=\begin{vmatrix}-1&3\\2&1\end{vmatrix}=-7$$

$$\mathrm{Cof}(M)=\begin{pmatrix}-3&-2&4\\5&5&-5\\4&6&-7\end{pmatrix}\Longrightarrow M^{-1}=\frac15\begin{pmatrix}-3&5&4\\-2&5&6\\4&-5&-7\end{pmatrix}=\begin{pmatrix}-\tfrac35&1&\tfrac45\\-\tfrac25&1&\tfrac65\\ \tfrac45&-1&-\tfrac75\end{pmatrix}$$

### b) $X$ tal que $MX=-5N$

$$X = M^{-1}(-5N) = -5\,M^{-1}N$$

$$M^{-1}N = \begin{pmatrix}-\tfrac35&1&\tfrac45\\-\tfrac25&1&\tfrac65\\ \tfrac45&-1&-\tfrac75\end{pmatrix}\begin{pmatrix}1&0\\0&1\\-1&-1\end{pmatrix} = \begin{pmatrix}-\tfrac75&\tfrac15\\-\tfrac85&-\tfrac15\\ \tfrac{11}{5}&\tfrac25\end{pmatrix}$$

$$\boxed{X = -5\,M^{-1}N = \begin{pmatrix}7&-1\\8&1\\-11&-2\end{pmatrix}}$$

---

## Ejercicio 9

Sistema:
$$
\begin{cases}
4x+y-2z=-3 \\
3x-y+4z=-2 \\
-x+y+z=5
\end{cases}
$$

### a) Forma matricial

$$
\underbrace{\begin{pmatrix}4&1&-2\\3&-1&4\\-1&1&1\end{pmatrix}}_{A}\underbrace{\begin{pmatrix}x\\y\\z\end{pmatrix}}_{X} = \underbrace{\begin{pmatrix}-3\\-2\\5\end{pmatrix}}_{B}
$$

### b) Resolver el sistema ($X=A^{-1}B$)

Por Sarrus: $\det(A) = \big[4(-1)(1)+1(4)(-1)+(-2)(3)(1)\big]-\big[(-2)(-1)(-1)+4(4)(1)+1(3)(1)\big]$

$$= (-4-4-6)-(-2+16+3) = -14-17=-31\neq0$$

Como $\det(A)\neq0$, el sistema tiene **solución única**. Con el método de cofactores se obtiene:

$$A^{-1} = \frac{1}{-31}\begin{pmatrix}-5&-3&2\\-7&2&-22\\2&-5&-7\end{pmatrix} = \begin{pmatrix}\tfrac{5}{31}&\tfrac{3}{31}&-\tfrac{2}{31}\\[2pt]\tfrac{7}{31}&-\tfrac{2}{31}&\tfrac{22}{31}\\[2pt]-\tfrac{2}{31}&\tfrac{5}{31}&\tfrac{7}{31}\end{pmatrix}$$

$$X = A^{-1}B = \begin{pmatrix}\tfrac{5}{31}&\tfrac{3}{31}&-\tfrac{2}{31}\\[2pt]\tfrac{7}{31}&-\tfrac{2}{31}&\tfrac{22}{31}\\[2pt]-\tfrac{2}{31}&\tfrac{5}{31}&\tfrac{7}{31}\end{pmatrix}\begin{pmatrix}-3\\-2\\5\end{pmatrix} = \begin{pmatrix}-1\\3\\1\end{pmatrix}$$

$$\boxed{x=-1,\quad y=3,\quad z=1}$$

*(Comprobación: $4(-1)+3-2(1)=-4+3-2=-3$ ✓; $3(-1)-3+4(1)=-3-3+4=-2$ ✓; $-(-1)+3+1=1+3+1=5$ ✓)*

---

> **Resumen rápido de fórmulas**  
> - $2\times2$: $\det = ad-bc$
> - $A$ invertible $\iff \det(A)\neq0$
> - $A^{-1}=\dfrac{1}{\det A}(\mathrm{Cof}\,A)^T$
> - $AX=B \Rightarrow X=A^{-1}B$ — pero $XA=B \Rightarrow X=B\,A^{-1}$ (¡el lado importa!)

---

---

# Sistemas de Ecuaciones Lineales

> Apunte de ayudantía: teoría + resolución completa de la Práctica 3.

---

## 1. Sistema lineal y forma matricial

Un **sistema lineal** de $m$ ecuaciones con $n$ incógnitas se escribe como:

$$
\begin{cases}
a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1 \\
a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2 \\
\quad \vdots \\
a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m
\end{cases}
$$

que en forma matricial es $A \cdot X = B$, con $A$ la **matriz de coeficientes** ($m\times n$), $X$ el vector de incógnitas y $B$ el vector de términos independientes.

Para resolverlo trabajamos con la **matriz ampliada** $[A \mid B]$, que junta los coeficientes con los términos independientes en una sola matriz.

> **¿Por qué ampliada?**  
> Aplicar operaciones de fila sobre $[A\mid B]$ es exactamente lo mismo que operar sobre las ecuaciones del sistema (sumarlas, restarlas, multiplicarlas por una constante), pero de forma mucho más ordenada.

---

## 2. Eliminación de Gauss-Jordan

Se aplican operaciones elementales por fila sobre $[A\mid B]$ hasta llevar $A$ a su **forma escalonada reducida** (un $1$ como **pivote** en cada fila no nula, con ceros arriba y abajo de cada pivote):

$$ [A\mid B] \xrightarrow{\text{operaciones de fila}} [A' \mid B'] $$

**Ejemplo rápido.** Para $\begin{cases}x+y=5 \\ 2x-y=1\end{cases}$:

$$ \left(\begin{array}{cc|c}1&1&5\\2&-1&1\end{array}\right)\xrightarrow[]{F_2-2F_1\to F_2}\left(\begin{array}{cc|c}1&1&5\\0&-3&-9\end{array}\right)\xrightarrow[]{F_2\to-\frac13F_2}\left(\begin{array}{cc|c}1&1&5\\0&1&3\end{array}\right)\xrightarrow[]{F_1-F_2\to F_1}\left(\begin{array}{cc|c}1&0&2\\0&1&3\end{array}\right) $$

Se lee directamente: $x=2,\ y=3$.

---

## 3. ¿Cuándo tiene solución? — Teorema de Rouché-Frobenius

Sea $n$ el número de incógnitas, $\mathrm{rg}(A)$ el rango de la matriz de coeficientes y $\mathrm{rg}(A\mid B)$ el rango de la matriz ampliada.

$$ \boxed{\mathrm{rg}(A) \neq \mathrm{rg}(A\mid B)} \Longrightarrow \color{#e74c3c}{\textbf{Sistema incompatible}} \text{ (sin solución)} $$

$$ \mathrm{rg}(A) = \mathrm{rg}(A\mid B) \Longrightarrow \color{#2ecc71}{\textbf{Sistema compatible}} 
\begin{cases} 
\mathrm{rg}(A) = n \Rightarrow \textbf{Determinado (solución única)} \\ 
\mathrm{rg}(A) < n \Rightarrow \textbf{Indeterminado (infinitas soluciones, con } n-\mathrm{rg}(A) \textbf{ parámetros libres)} 
\end{cases} $$

> **Cómo se ve en la forma escalonada**  
> 
> - **Incompatible:** aparece una fila del tipo $\left(0\ 0\ \cdots\ 0 \mid \color{#e74c3c}{k}\right)$ con $k\neq0$ — una ecuación imposible como $0=k$.
> - **Determinado:** cada columna de $A$ tiene un pivote (no quedan variables "libres").
> - **Indeterminado:** sobran columnas sin pivote → esas variables quedan como **parámetros libres**.

---

## 4. Sistemas homogéneos

Un sistema es **homogéneo** cuando $B=O$ (todos los términos independientes son $0$). Siempre es compatible (al menos tiene la solución trivial $X=O$), y es indeterminado (infinitas soluciones) exactamente cuando $\mathrm{rg}(A)<n$.

## 5. Sistemas con un parámetro

Cuando el sistema depende de un parámetro (llamémoslo $m$ o $\alpha$), la estrategia es:

1. Calcular $\det(A)$ en función del parámetro (si $A$ es cuadrada).
2. Los valores que anulan $\det(A)$ son los **candidatos** a no tener solución única — ahí NO se puede usar la regla de Cramer ni invertir $A$.
3. Para cada uno de esos valores, **reemplazar y comparar** $\mathrm{rg}(A)$ con $\mathrm{rg}(A\mid B)$ para decidir si es incompatible o compatible indeterminado.
4. Para todos los demás valores del parámetro: solución única ($\det(A)\neq0$).

---

---

# Práctica 3 — Solución

## Ejercicio 1 — Compatibilidad y solución de cada sistema

### a) $\begin{cases}-2x+y+z=6 \\ 3x-z=-7 \\ -x-5y+2z=7\end{cases}$

$$ \left(\begin{array}{ccc|c}-2&1&1&6\\3&0&-1&-7\\-1&-5&2&7\end{array}\right) \xrightarrow{\text{Gauss-Jordan}} \left(\begin{array}{ccc|c}1&0&0&-\frac{6}{5}\\0&1&0&\frac{1}{5}\\0&0&1&\frac{17}{5}\end{array}\right) $$

$\mathrm{rg}(A)=\mathrm{rg}(A|B)=3=n$ → **Compatible determinado**.

$$\boxed{x=-\frac{6}{5},\quad y=\frac{1}{5},\quad z=\frac{17}{5}}$$

### b) $\begin{cases}-3x+y-z=-4 \\ 5x-2y+z=6 \\ -x+y+3z=0\end{cases}$

$$ \left(\begin{array}{ccc|c}-3&1&-1&-4\\5&-2&1&6\\-1&1&3&0\end{array}\right) \xrightarrow{\text{Gauss-Jordan}} \left(\begin{array}{ccc|c}1&0&0&2\\0&1&0&2\\0&0&1&0\end{array}\right) $$

**Compatible determinado.**

$$\boxed{x=2,\quad y=2,\quad z=0}$$

### c) (P) $\begin{cases}-2x+y-z=0 \\ x-2y+3z=13 \\ -x+y+4z=9\end{cases}$

$$ \left(\begin{array}{ccc|c}-2&1&-1&0\\1&-2&3&13\\-1&1&4&9\end{array}\right)\xrightarrow[F_3-F_2\to F_3]{F_1+2F_2\to F_1}\left(\begin{array}{ccc|c}0&-3&5&26\\1&-2&3&13\\0&3&1&-4\end{array}\right) $$

$$ \xrightarrow[]{F_1\leftrightarrow F_2}\left(\begin{array}{ccc|c}1&-2&3&13\\0&-3&5&26\\0&3&1&-4\end{array}\right)\xrightarrow[]{F_3+F_2\to F_3}\left(\begin{array}{ccc|c}1&-2&3&13\\0&-3&5&26\\0&0&6&22\end{array}\right) $$

Despejando desde la última fila hacia arriba: $z=\frac{22}{6}=\frac{11}{3}$... completando el escalonado reducido se llega a:

$$ \left(\begin{array}{ccc|c}1&0&0&-\frac{7}{2}\\0&1&0&-\frac{9}{2}\\0&0&1&\frac{5}{2}\end{array}\right) $$

**Compatible determinado.**

$$\boxed{x=-\frac{7}{2},\quad y=-\frac{9}{2},\quad z=\frac{5}{2}}$$

### d) $\begin{cases}x+y+z+t=1 \\ x-y+z-t=0 \\ x+y-z-t=-1 \\ x+y+z-t=2\end{cases}$

$$ \left(\begin{array}{cccc|c}1&1&1&1&1\\1&-1&1&-1&0\\1&1&-1&-1&-1\\1&1&1&-1&2\end{array}\right) \xrightarrow{\text{Gauss-Jordan}} \left(\begin{array}{cccc|c}1&0&0&0&-1\\0&1&0&0&1\\0&0&1&0&\frac{3}{2}\\0&0&0&1&-\frac{1}{2}\end{array}\right) $$

$\mathrm{rg}(A)=\mathrm{rg}(A|B)=4=n$ → **Compatible determinado**.

$$\boxed{x=-1,\quad y=1,\quad z=\frac{3}{2},\quad t=-\frac{1}{2}}$$

### e) (P) $\begin{cases}x-2y-z+3t=0 \\ 2x+4y+5z-5t=3 \\ 3x-6y-6z+8t=2\end{cases}$

$$ \left(\begin{array}{cccc|c}1&-2&-1&3&0\\2&4&5&-5&3\\3&-6&-6&8&2\end{array}\right)\xrightarrow[F_3-3F_1\to F_3]{F_2-2F_1\to F_2}\left(\begin{array}{cccc|c}1&-2&-1&3&0\\0&8&7&-11&3\\0&0&-3&-1&2\end{array}\right) $$

Aquí solo **3 pivotes para 4 incógnitas** ($x,y,z,t$): la columna de $t$ queda sin pivote → $t$ es **parámetro libre**. Terminando el escalonamiento:

$$ \left(\begin{array}{cccc|c}1&0&0&0&\frac{5}{4}\\0&1&0&-\frac{5}{3}&\frac{23}{24}\\0&0&1&\frac{1}{3}&-\frac{2}{3}\end{array}\right) $$

$\mathrm{rg}(A)=\mathrm{rg}(A|B)=3<n=4$ → **Compatible indeterminado** (1 parámetro libre).

$$\boxed{x=\frac{5}{4},\quad y=\frac{23}{24}+\frac{5}{3} t,\quad z=-\frac{2}{3}-\frac{1}{3} t,\quad t\in\mathbb{R}}$$

### f) $\begin{cases}x-5y+4z=-3 \\ 2x-7y+3z=-2 \\ -2x+y+7z=-1\end{cases}$

$$ \left(\begin{array}{ccc|c}1&-5&4&-3\\2&-7&3&-2\\-2&1&7&-1\end{array}\right) \xrightarrow{\text{Gauss-Jordan}} \left(\begin{array}{ccc|c}1&0&-\frac{13}{3}&0\\0&1&-\frac{5}{3}&0\\0&0&0&\color{#e74c3c}{1}\end{array}\right) $$

La última fila dice $0x+0y+0z=\color{#e74c3c}{1}$: una contradicción. $\mathrm{rg}(A)=2\neq\mathrm{rg}(A|B)=3$.

$$\boxed{\textbf{Sistema incompatible — no tiene solución}}$$

### g) $\begin{cases}x-y+z+t=0 \\ x+y+z-t=2 \\ x-y-z+t=2\end{cases}$

$$ \left(\begin{array}{cccc|c}1&-1&1&1&0\\1&1&1&-1&2\\1&-1&-1&1&2\end{array}\right) \xrightarrow{\text{Gauss-Jordan}} \left(\begin{array}{cccc|c}1&0&0&0&2\\0&1&0&-1&1\\0&0&1&0&-1\end{array}\right) $$

3 pivotes para 4 incógnitas → columna de $t$ libre. $\mathrm{rg}(A)=\mathrm{rg}(A|B)=3<n=4$ → **Compatible indeterminado**.

$$\boxed{x=2,\quad y=1+t,\quad z=-1,\quad t\in\mathbb{R}}$$

### h) $\begin{cases}5x-y+3z=-6 \\ x+3y-z=10 \\ 2x-y+4z=-2\end{cases}$

$$ \left(\begin{array}{ccc|c}5&-1&3&-6\\1&3&-1&10\\2&-1&4&-2\end{array}\right) \xrightarrow{\text{Gauss-Jordan}} \left(\begin{array}{ccc|c}1&0&0&-1\\0&1&0&4\\0&0&1&1\end{array}\right) $$

**Compatible determinado.**

$$\boxed{x=-1,\quad y=4,\quad z=1}$$

### i) (P) $\begin{cases}x-3y+3z=9 \\ 2x-y+z=3 \\ 3x+y-z=-3 \\ 2x+4y-4z=-12\end{cases}$

$$ \left(\begin{array}{ccc|c}1&-3&3&9\\2&-1&1&3\\3&1&-1&-3\\2&4&-4&-12\end{array}\right)\xrightarrow[\substack{F_3-3F_1\to F_3 \\ F_4-2F_1\to F_4}]{F_2-2F_1\to F_2}\left(\begin{array}{ccc|c}1&-3&3&9\\0&5&-5&-15\\0&10&-10&-30\\0&10&-10&-30\end{array}\right) $$

Las filas 3 y 4 quedan proporcionales a la fila 2 ($\times2$) → se anulan al restar, y solo quedan **2 filas no nulas** para 3 incógnitas. Escalonando:

$$ \left(\begin{array}{ccc|c}1&0&0&0\\0&1&-1&-3\\0&0&0&0\\0&0&0&0\end{array}\right) $$

$\mathrm{rg}(A)=\mathrm{rg}(A|B)=2<n=3$ → **Compatible indeterminado** (1 parámetro libre, $z$).

$$\boxed{x=0,\quad y=-3+z,\quad z\in\mathbb{R}}$$

### j) $\begin{cases}2x-3y+z=6 \\ x+y-z=-2 \\ 4x-y-z=2\end{cases}$

$$ \left(\begin{array}{ccc|c}2&-3&1&6\\1&1&-1&-2\\4&-1&-1&2\end{array}\right) \xrightarrow{\text{Gauss-Jordan}} \left(\begin{array}{ccc|c}1&0&-\frac{2}{5}&0\\0&1&-\frac{3}{5}&-2\\0&0&0&0\end{array}\right) $$

$\mathrm{rg}(A)=\mathrm{rg}(A|B)=2<n=3$ → **Compatible indeterminado** (parámetro $z$).

$$\boxed{x=\frac{2}{5} z,\quad y=-2+\frac{3}{5} z,\quad z\in\mathbb{R}}$$

### k) $\begin{cases}-3x+y-z=-4 \\ 5x-2y+z=6 \\ -x+y+3z=0\end{cases}$

Es exactamente el mismo sistema que el **ítem b)**.

$$\boxed{x=2,\quad y=2,\quad z=0}$$

### l) $\begin{cases}x+y+z=6 \\ x-y-z=-4 \\ 3x+y+z=7\end{cases}$

$$ \left(\begin{array}{ccc|c}1&1&1&6\\1&-1&-1&-4\\3&1&1&7\end{array}\right) \xrightarrow{\text{Gauss-Jordan}} \left(\begin{array}{ccc|c}1&0&0&0\\0&1&1&0\\0&0&0&\color{#e74c3c}{1}\end{array}\right) $$

$\mathrm{rg}(A)=2\neq\mathrm{rg}(A|B)=3$.

$$\boxed{\textbf{Sistema incompatible — no tiene solución}}$$

---

## Ejercicio 2 (P) — Valores de $m$

$$\begin{cases}2x+3y+5z=8 \\ 4x+4y+2mz=12 \\ x+y+2z=3\end{cases}$$

$$ A=\begin{pmatrix}2&3&5\\4&4&2m\\1&1&2\end{pmatrix},\qquad \det(A)=2m-8 $$

$$\det(A)=0 \iff m=4$$

**Analizamos $m=4$:** la matriz ampliada escalona a

$$ \left(\begin{array}{ccc|c}1&0&1&1\\0&1&1&2\\0&0&0&0\end{array}\right) $$

$\mathrm{rg}(A)=\mathrm{rg}(A|B)=2<3$ → compatible **indeterminado**, nunca incompatible en este caso.

$$\boxed{\text{a) Solución única: } m\neq4} \qquad \boxed{\text{b) No tiene solución: para ningún valor de } m} \qquad \boxed{\text{c) Infinitas soluciones: } m=4}$$

*(Dato curioso: para $m\neq4$ la solución única resulta ser siempre $(x,y,z)=(1,2,0)$, independiente de $m$, porque el coeficiente $2m$ multiplica a $z=0$.)*

---

## Ejercicio 3 — Valores de $\alpha$

$$\begin{cases}x+\alpha y+2z=1 \\ x+(2\alpha-1)y+z=1 \\ x+\alpha y+(\alpha+3)z=2\alpha-1\end{cases}$$

$$ A=\begin{pmatrix}1&\alpha&2\\1&2\alpha-1&1\\1&\alpha&\alpha+3\end{pmatrix},\qquad \det(A) = (\alpha-1)(\alpha+1) $$

$$\det(A)=0 \iff \alpha=1 \ \lor\ \alpha=-1$$

**Caso $\alpha=-1$:** $\mathrm{rg}(A)=2$, $\mathrm{rg}(A|B)=3$ → **incompatible**.

**Caso $\alpha=1$:** el sistema queda $\begin{cases}x+y+2z=1 \\ x+y+z=1 \\ x+y+4z=1\end{cases}$, que escalona a

$$ \left(\begin{array}{ccc|c}1&1&0&1\\0&0&1&0\\0&0&0&0\end{array}\right) $$

$\mathrm{rg}(A)=\mathrm{rg}(A|B)=2<3$ → **compatible indeterminado**.

$$\boxed{\text{a) Solución única: } \alpha\notin\{-1,1\}} \qquad \boxed{\text{b) No tiene solución: } \alpha=-1} \qquad \boxed{\text{c) Infinitas soluciones: } \alpha=1}$$

Para $\alpha\notin\{-1,1\}$, resolviendo con la fórmula $X=A^{-1}B$ se obtiene la solución única:

$$x=\frac{5(1-\alpha)}{\alpha+1},\qquad y=\frac{2}{\alpha+1},\qquad z=\frac{2(\alpha-1)}{\alpha+1}$$

---

## Ejercicio 4 — Problemas de planteo

### a) Los tres números

Sean $a,b,c$ los números. "El segundo es 1 más que tres veces el primero" → $b=3a+1$. "El tercero es 1 menos que el doble del segundo" → $c=2b-1$. Y $a+b+c=12$.

Sustituyendo en la suma:

$$a+(3a+1)+\big(2(3a+1)-1\big)=12 \;\Longrightarrow\; 10a+2=12 \;\Longrightarrow\; a=1$$

$$\boxed{a=1,\quad b=4,\quad c=7}$$

*(Comprobación: $1+4+7=12$ ✓)*

### b) (P) Plan de comidas — carne, pescado y verduras

Sean $C$, $P$, $V$ las raciones de carne, pescado y verduras.

$$ \begin{cases} 15C+12P+4V=514 & \text{(proteína total)}\\ C+P+V=44 & \text{(raciones totales)}\\ C=P+V & \text{(condición de carne)} \end{cases} $$

De la 2ª y 3ª ecuación: $C+C=44 \Rightarrow C=22$, y por lo tanto $P+V=22$.

Reemplazando en la 1ª: $15(22)+12P+4V=514 \Rightarrow 12P+4V=184 \Rightarrow 3P+V=46$.

Con $V=22-P$: $3P+(22-P)=46 \Rightarrow 2P=24 \Rightarrow P=12$, luego $V=10$.

$$\boxed{\text{Carne: 22 raciones}\quad\text{Pescado: 12 raciones}\quad\text{Verduras: 10 raciones}}$$

### c) Votación del viaje de curso

Sean $Pu$ (Pucón), $PV$ (Puerto Varas) y $PA$ (Punta Arenas). $Pu=3PA$. "El 40% de $PV$ coincide con la quinta parte de la suma de los otros dos" → $0.4\,PV = \frac{1}{5}(Pu+PA)$. Además $Pu+PV+PA=30$.

Como $Pu=3PA$: $Pu+PA=4PA$, entonces $0.4\,PV=\frac{1}{5}(4PA)=0.8PA \Rightarrow PV=2PA$.

$$3PA+2PA+PA=30 \;\Longrightarrow\; 6PA=30 \;\Longrightarrow\; PA=5$$

$$\boxed{\text{Pucón: 15 votos}\quad\text{Puerto Varas: 10 votos}\quad\text{Punta Arenas: 5 votos}}$$

### d) Fotografías de Andrea

Sean $S$, $M$, $L$ el número de fotos pequeñas, medianas y grandes. "Vende tantas pequeñas como medianas y grandes juntas" → $S=M+L$. "El doble de medianas que grandes" → $M=2L$. Costo del puesto: $1000S+1500M+4000L=30000$.

$$S=M+L=2L+L=3L$$

$$1000(3L)+1500(2L)+4000L=30000 \;\Longrightarrow\; 10,000L=30,000 \;\Longrightarrow\; L=3$$

$$\boxed{\text{Pequeñas: } S=9 \quad \text{Medianas: } M=6 \quad \text{Grandes: } L=3}$$

*(18 fotos en total; comprobación: $9(1000)+6(1500)+3(4000)=9000+9000+12000=30,000$ ✓)*

### e) Parábola por tres puntos

Buscamos $y=Ax^2+Bx+C$ que pase por $(2,-7),(3,-1),(4,9)$. Cada punto entrega una ecuación lineal en $A,B,C$:

$$ \begin{cases} 4A+2B+C=-7 \\ 9A+3B+C=-1 \\ 16A+4B+C=9 \end{cases} $$

Resolviendo el sistema (Gauss-Jordan o restando ecuaciones consecutivas para eliminar $C$):

$$\boxed{A=2,\quad B=-4,\quad C=-7 \qquad\Longrightarrow\qquad y=2x^2-4x-7}$$

*(Comprobación en $x=2$: $2(4)-4(2)-7=8-8-7=-7$ ✓)*

---

> **Resumen rápido — Rouché-Frobenius**  
> 
> - $\mathrm{rg}(A)\neq\mathrm{rg}(A|B)$ → **incompatible** (aparece una fila $0=k$, $k\neq0$).
> - $\mathrm{rg}(A)=\mathrm{rg}(A|B)=n$ → **compatible determinado** (solución única).
> - $\mathrm{rg}(A)=\mathrm{rg}(A|B)<n$ → **compatible indeterminado** (infinitas soluciones, $n-\mathrm{rg}(A)$ parámetros libres).

---
title: "Ensayo Certamen 1 — Solución"
subtitle: "MAT021B — Matemática de Ingeniería"

# Ensayo Certamen 1 — Solución

Resolución paso a paso. La teoría de matrices, determinantes, inversa y sistemas lineales usada aquí está desarrollada en los apuntes de Práctica 2 y Práctica 3.

## Ejercicio 1

$$M=\begin{pmatrix}1&3&0\\-1&0&-1\\1&1&2\end{pmatrix}\qquad N=\begin{pmatrix}2&6\\-1&-1\\-3&4\end{pmatrix}$$

### a) ¿$M$ tiene inversa?

Por Sarrus:

$$\det(M) = \big[(1)(0)(2)+(3)(-1)(1)+(0)(-1)(1)\big]-\big[(0)(0)(1)+(1)(-1)(1)+(3)(-1)(2)\big]$$

$$=(0-3+0)-(0-1-6) = -3-(-7)=4 \neq 0$$

Sí tiene inversa. La calculamos con operaciones elementales por fila:

$$
\begin{pmatrix}1&3&0&1&0&0\\-1&0&-1&0&1&0\\1&1&2&0&0&1\end{pmatrix}\xrightarrow[F_3-F_1\to F_3]{F_2+F_1\to F_2}\begin{pmatrix}1&3&0&1&0&0\\0&3&-1&1&1&0\\0&-2&2&-1&0&1\end{pmatrix}
$$

$$
\xrightarrow[]{F_2\to\frac{1}{3}F_2}\begin{pmatrix}1&3&0&1&0&0\\0&1&-\frac{1}{3}&\frac{1}{3}&\frac{1}{3}&0\\0&-2&2&-1&0&1\end{pmatrix}\xrightarrow[]{F_3+2F_2\to F_3}\begin{pmatrix}1&3&0&1&0&0\\0&1&-\frac{1}{3}&\frac{1}{3}&\frac{1}{3}&0\\0&0&\frac{4}{3}&-\frac{1}{3}&\frac{2}{3}&1\end{pmatrix}
$$

$$
\xrightarrow[]{F_3\to\frac{3}{4}F_3}\begin{pmatrix}1&3&0&1&0&0\\0&1&-\frac{1}{3}&\frac{1}{3}&\frac{1}{3}&0\\0&0&1&-\frac{1}{4}&\frac{1}{2}&\frac{3}{4}\end{pmatrix}\xrightarrow[F_2+\frac{1}{3}F_3\to F_2]{F_1-3F_2\to F_1}\begin{pmatrix}1&0&0&\frac{1}{4}&-\frac{3}{2}&-\frac{3}{4}\\0&1&0&\frac{1}{4}&\frac{1}{2}&\frac{1}{4}\\0&0&1&-\frac{1}{4}&\frac{1}{2}&\frac{3}{4}\end{pmatrix}
$$

$$\boxed{M^{-1}=\begin{pmatrix}\frac{1}{4}&-\frac{3}{2}&-\frac{3}{4}\\[2pt]\frac{1}{4}&\frac{1}{2}&\frac{1}{4}\\[2pt]-\frac{1}{4}&\frac{1}{2}&\frac{3}{4}\end{pmatrix}}$$

### b) $X$ tal que $4M\cdot X = N$

$$4MX=N \implies MX=\frac{1}{4}N \implies X = M^{-1}\left(\frac{1}{4}N\right) = \frac{1}{4}M^{-1}N$$

Primero $M^{-1}N$:

$$
M^{-1}N=\begin{pmatrix}\frac{1}{4}&-\frac{3}{2}&-\frac{3}{4}\\[2pt]\frac{1}{4}&\frac{1}{2}&\frac{1}{4}\\[2pt]-\frac{1}{4}&\frac{1}{2}&\frac{3}{4}\end{pmatrix}\begin{pmatrix}2&6\\-1&-1\\-3&4\end{pmatrix}=\begin{pmatrix}\frac{17}{4}&0\\[2pt]-\frac{3}{4}&2\\[2pt]-\frac{13}{4}&1\end{pmatrix}
$$

*(Fila 1, columna 1: $\frac{1}{4}(2)+(-\frac{3}{2})(-1)+(-\frac{3}{4})(-3)=\frac{1}{2}+\frac{3}{2}+\frac{9}{4}=\frac{17}{4}$, y así con el resto de entradas.)*

$$\boxed{X=\frac{1}{4}M^{-1}N=\begin{pmatrix}\frac{17}{16}&0\\[2pt]-\frac{3}{16}&\frac{1}{2}\\[2pt]-\frac{13}{16}&\frac{1}{4}\end{pmatrix}}$$

---

## Ejercicio 2

$$P=\begin{pmatrix}0&1\\k&-1\\0&2\end{pmatrix}\qquad Q=\begin{pmatrix}1&k&0\\1&0&1\end{pmatrix}$$

Buscamos $k$ tal que $(Q-P^T)\cdot P = \begin{pmatrix}0&1\\5&-3\end{pmatrix}$.

**Paso 1 — Transponer $P$:**
$$P^T=\begin{pmatrix}0&k&0\\1&-1&2\end{pmatrix}$$

**Paso 2 — Calcular $Q-P^T$** *(mismo orden $2\times3$, se restan entrada a entrada)*:
$$Q-P^T=\begin{pmatrix}1-0&k-k&0-0\\1-1&0-(-1)&1-2\end{pmatrix}=\begin{pmatrix}1&0&0\\0&1&-1\end{pmatrix}$$

>[!tip] Observación
>El parámetro $k$ se cancela al restar, porque tanto $Q$ como $P^T$ tienen un $k$ en la misma posición $(1,2)$. Esto significa que $k$ solo puede aparecer más adelante a través de la matriz $P$ en la multiplicación.

**Paso 3 — Multiplicar por $P$** *($2\times3$ por $3\times2 \to$ resultado $2\times2$)*:
$$(Q-P^T)\cdot P = \begin{pmatrix}1&0&0\\0&1&-1\end{pmatrix}\begin{pmatrix}0&1\\k&-1\\0&2\end{pmatrix} = \begin{pmatrix}1(0)+0(k)+0(0) & 1(1)+0(-1)+0(2)\\0(0)+1(k)+(-1)(0) & 0(1)+1(-1)+(-1)(2)\end{pmatrix}=\begin{pmatrix}0&1\\k&-3\end{pmatrix}$$

**Paso 4 — Igualar con el resultado pedido:**
$$\begin{pmatrix}0&1\\k&-3\end{pmatrix}=\begin{pmatrix}0&1\\5&-3\end{pmatrix} \implies k=5$$

$$\boxed{k=5}$$

---

## Ejercicio 3

$$\begin{cases}-x+3y+(a-1)z=-1\\(a-1)x+y+z=-2\\x+(a-1)y+z=1\end{cases}$$

### a) Para $a=2$: ¿compatible?

Con $a=2$, tenemos $a-1=1$, y el sistema queda:

$$\begin{cases}-x+3y+z=-1\\x+y+z=-2\\x+y+z=1\end{cases}$$

>[!warning] Contradicción inmediata
>Las ecuaciones 2 y 3 tienen exactamente el mismo lado izquierdo ($x+y+z$) pero distinto lado derecho ($-2$ y $1$). Eso ya basta para concluir sin más cálculo.
>Confirmando con rango: $\mathrm{rg}(A)=2$ pero $\mathrm{rg}(A|B)=3$.

$$\boxed{\text{Para } a=2 \text{ el sistema es \textbf{incompatible}}}$$

### b) Para $a=-1$: compatible indeterminado + 4 soluciones particulares

Con $a=-1$, $a-1=-2$, y el sistema es:

$$\begin{cases}-x+3y-2z=-1\\-2x+y+z=-2\\x-2y+z=1\end{cases}$$

Escalonando la matriz ampliada:

$$
\begin{pmatrix}-1&3&-2&-1\\-2&1&1&-2\\1&-2&1&1\end{pmatrix} \xrightarrow{\text{Gauss-Jordan}} \begin{pmatrix}1&0&-1&1\\0&1&-1&0\\0&0&0&0\end{pmatrix}
$$

$\mathrm{rg}(A)=\mathrm{rg}(A|B)=2 < n=3 \implies$ compatible indeterminado, con $z$ como parámetro libre:

$$\boxed{x=1+z,\qquad y=z,\qquad z\in\mathbb{R}}$$

**Cuatro soluciones particulares** (reemplazando $z$ por valores distintos):

| $z$ | Solution $(x,y,z)$ |
| :---: | :---: |
| $0$ | $(1,0,0)$ |
| $1$ | $(2,1,1)$ |
| $2$ | $(3,2,2)$ |
| $-1$ | $(0,-1,-1)$ |

*(Comprobación con $(2,1,1)$: $-2+3-2=-1$ ✓; $-4+1+1=-2$ ✓; $2-2+1=1$ ✓)*

---

## Ejercicio 4 — Presupuesto de remodelación

Sean $C$, $F$, $Al$ los metros cuadrados de cerámica, piso flotante y alfombra respectivamente.

**Datos:**
* Área total: $C+F+Al=180$
* Costo cerámica: $\$6.000/\text{m}^2$.
* Piso flotante ($25\%$ más barato): $\$6.000 \times 0{,}75 = \$4.500/\text{m}^2$.
* Alfombra: $\$3.000/\text{m}^2$.
* Presupuesto total: $6000C+4500F+3000Al=900.000$
* La alfombra excede en $24\,\text{m}^2$ al piso flotante: $Al=F+24$

**Sistema:**
$$\begin{cases}C+F+Al=180\\6000C+4500F+3000Al=900.000\\Al-F=24\end{cases}$$

Sustituyendo $Al=F+24$ en las otras dos ecuaciones:

$$C+F+(F+24)=180 \implies C+2F=156 \quad (\star)$$

$$6000C+4500F+3000(F+24)=900.000 \implies 6000C+7500F=828.000 \implies 4C+5F=552 \quad (\star\star)$$

De $(\star)$: $C=156-2F$. Reemplazando en $(\star\star)$:

$$4(156-2F)+5F=552 \implies 624-8F+5F=552 \implies -3F=-72 \implies F=24$$

$$C=156-2(24)=108,\qquad Al=24+24=48$$

$$\boxed{\text{Cerámica: } 108\ \text{m}^2 \qquad \text{Piso flotante: } 24\ \text{m}^2 \qquad \text{Alfombra: } 48\ \text{m}^2}$$

*(Comprobación: Área $108+24+48=180$ ✓; Costo $6000(108)+4500(24)+3000(48)=648.000+108.000+144.000=900.000$ ✓; $Al-F=48-24=24$ ✓)*

---
title: "Ensayo Certamen 1 — Solución"
subtitle: "MAT021B — Matemática de Ingeniería"
---

# Ensayo Certamen 1 — Solución

Resolución paso a paso. La teoría de matrices, determinantes, inversa y sistemas lineales usada aquí está desarrollada en los apuntes de Práctica 2 y Práctica 3.

## Ejercicio 1

$$M=\begin{pmatrix}1&3&0\\-1&0&-1\\1&1&2\end{pmatrix}\qquad N=\begin{pmatrix}2&6\\-1&-1\\-3&4\end{pmatrix}$$

### a) ¿$M$ tiene inversa?

Por Sarrus:

$$\det(M) = \big[(1)(0)(2)+(3)(-1)(1)+(0)(-1)(1)\big]-\big[(0)(0)(1)+(1)(-1)(1)+(3)(-1)(2)\big]$$

$$=(0-3+0)-(0-1-6) = -3-(-7)=4 \neq 0$$

Sí tiene inversa. La calculamos con operaciones elementales por fila:

$$
\begin{pmatrix}1&3&0&1&0&0\\-1&0&-1&0&1&0\\1&1&2&0&0&1\end{pmatrix}\xrightarrow[F_3-F_1\to F_3]{F_2+F_1\to F_2}\begin{pmatrix}1&3&0&1&0&0\\0&3&-1&1&1&0\\0&-2&2&-1&0&1\end{pmatrix}
$$

$$
\xrightarrow[]{F_2\to\frac{1}{3}F_2}\begin{pmatrix}1&3&0&1&0&0\\0&1&-\frac{1}{3}&\frac{1}{3}&\frac{1}{3}&0\\0&-2&2&-1&0&1\end{pmatrix}\xrightarrow[]{F_3+2F_2\to F_3}\begin{pmatrix}1&3&0&1&0&0\\0&1&-\frac{1}{3}&\frac{1}{3}&\frac{1}{3}&0\\0&0&\frac{4}{3}&-\frac{1}{3}&\frac{2}{3}&1\end{pmatrix}
$$

$$
\xrightarrow[]{F_3\to\frac{3}{4}F_3}\begin{pmatrix}1&3&0&1&0&0\\0&1&-\frac{1}{3}&\frac{1}{3}&\frac{1}{3}&0\\0&0&1&-\frac{1}{4}&\frac{1}{2}&\frac{3}{4}\end{pmatrix}\xrightarrow[F_2+\frac{1}{3}F_3\to F_2]{F_1-3F_2\to F_1}\begin{pmatrix}1&0&0&\frac{1}{4}&-\frac{3}{2}&-\frac{3}{4}\\0&1&0&\frac{1}{4}&\frac{1}{2}&\frac{1}{4}\\0&0&1&-\frac{1}{4}&\frac{1}{2}&\frac{3}{4}\end{pmatrix}
$$

$$\boxed{M^{-1}=\begin{pmatrix}\frac{1}{4}&-\frac{3}{2}&-\frac{3}{4}\\[2pt]\frac{1}{4}&\frac{1}{2}&\frac{1}{4}\\[2pt]-\frac{1}{4}&\frac{1}{2}&\frac{3}{4}\end{pmatrix}}$$

### b) $X$ tal que $4M\cdot X = N$

$$4MX=N \implies MX=\frac{1}{4}N \implies X = M^{-1}\left(\frac{1}{4}N\right) = \frac{1}{4}M^{-1}N$$

Primero $M^{-1}N$:

$$
M^{-1}N=\begin{pmatrix}\frac{1}{4}&-\frac{3}{2}&-\frac{3}{4}\\[2pt]\frac{1}{4}&\frac{1}{2}&\frac{1}{4}\\[2pt]-\frac{1}{4}&\frac{1}{2}&\frac{3}{4}\end{pmatrix}\begin{pmatrix}2&6\\-1&-1\\-3&4\end{pmatrix}=\begin{pmatrix}\frac{17}{4}&0\\[2pt]-\frac{3}{4}&2\\[2pt]-\frac{13}{4}&1\end{pmatrix}
$$

*(Fila 1, columna 1: $\frac{1}{4}(2)+(-\frac{3}{2})(-1)+(-\frac{3}{4})(-3)=\frac{1}{2}+\frac{3}{2}+\frac{9}{4}=\frac{17}{4}$, y así con el resto de entradas.)*

$$\boxed{X=\frac{1}{4}M^{-1}N=\begin{pmatrix}\frac{17}{16}&0\\[2pt]-\frac{3}{16}&\frac{1}{2}\\[2pt]-\frac{13}{16}&\frac{1}{4}\end{pmatrix}}$$

---

## Ejercicio 2

$$P=\begin{pmatrix}0&1\\k&-1\\0&2\end{pmatrix}\qquad Q=\begin{pmatrix}1&k&0\\1&0&1\end{pmatrix}$$

Buscamos $k$ tal que $(Q-P^T)\cdot P = \begin{pmatrix}0&1\\5&-3\end{pmatrix}$.

**Paso 1 — Transponer $P$:**
$$P^T=\begin{pmatrix}0&k&0\\1&-1&2\end{pmatrix}$$

**Paso 2 — Calcular $Q-P^T$** *(mismo orden $2\times3$, se restan entrada a entrada)*:
$$Q-P^T=\begin{pmatrix}1-0&k-k&0-0\\1-1&0-(-1)&1-2\end{pmatrix}=\begin{pmatrix}1&0&0\\0&1&-1\end{pmatrix}$$

>[!tip] Observación
>El parámetro $k$ se cancela al restar, porque tanto $Q$ como $P^T$ tienen un $k$ en la misma posición $(1,2)$. Esto significa que $k$ solo puede aparecer más adelante a través de la matriz $P$ en la multiplicación.

**Paso 3 — Multiplicar por $P$** *($2\times3$ por $3\times2 \to$ resultado $2\times2$)*:
$$(Q-P^T)\cdot P = \begin{pmatrix}1&0&0\\0&1&-1\end{pmatrix}\begin{pmatrix}0&1\\k&-1\\0&2\end{pmatrix} = \begin{pmatrix}1(0)+0(k)+0(0) & 1(1)+0(-1)+0(2)\\0(0)+1(k)+(-1)(0) & 0(1)+1(-1)+(-1)(2)\end{pmatrix}=\begin{pmatrix}0&1\\k&-3\end{pmatrix}$$

**Paso 4 — Igualar con el resultado pedido:**
$$\begin{pmatrix}0&1\\k&-3\end{pmatrix}=\begin{pmatrix}0&1\\5&-3\end{pmatrix} \implies k=5$$

$$\boxed{k=5}$$

---

## Ejercicio 3

$$\begin{cases}-x+3y+(a-1)z=-1\\(a-1)x+y+z=-2\\x+(a-1)y+z=1\end{cases}$$

### a) Para $a=2$: ¿compatible?

Con $a=2$, tenemos $a-1=1$, y el sistema queda:

$$\begin{cases}-x+3y+z=-1\\x+y+z=-2\\x+y+z=1\end{cases}$$

>[!warning] Contradicción inmediata
>Las ecuaciones 2 y 3 tienen exactamente el mismo lado izquierdo ($x+y+z$) pero distinto lado derecho ($-2$ y $1$). Eso ya basta para concluir sin más cálculo.
>Confirmando con rango: $\mathrm{rg}(A)=2$ pero $\mathrm{rg}(A|B)=3$.

$$\boxed{\text{Para } a=2 \text{ el sistema es \textbf{incompatible}}}$$

### b) Para $a=-1$: compatible indeterminado + 4 soluciones particulares

Con $a=-1$, $a-1=-2$, y el sistema es:

$$\begin{cases}-x+3y-2z=-1\\-2x+y+z=-2\\x-2y+z=1\end{cases}$$

Escalonando la matriz ampliada:

$$
\begin{pmatrix}-1&3&-2&-1\\-2&1&1&-2\\1&-2&1&1\end{pmatrix} \xrightarrow{\text{Gauss-Jordan}} \begin{pmatrix}1&0&-1&1\\0&1&-1&0\\0&0&0&0\end{pmatrix}
$$

$\mathrm{rg}(A)=\mathrm{rg}(A|B)=2 < n=3 \implies$ compatible indeterminado, con $z$ como parámetro libre:

$$\boxed{x=1+z,\qquad y=z,\qquad z\in\mathbb{R}}$$

**Cuatro soluciones particulares** (reemplazando $z$ por valores distintos):

| $z$ | Solution $(x,y,z)$ |
| :---: | :---: |
| $0$ | $(1,0,0)$ |
| $1$ | $(2,1,1)$ |
| $2$ | $(3,2,2)$ |
| $-1$ | $(0,-1,-1)$ |

*(Comprobación con $(2,1,1)$: $-2+3-2=-1$ ✓; $-4+1+1=-2$ ✓; $2-2+1=1$ ✓)*

---

## Ejercicio 4 — Presupuesto de remodelación

Sean $C$, $F$, $Al$ los metros cuadrados de cerámica, piso flotante y alfombra respectivamente.

**Datos:**
* Área total: $C+F+Al=180$
* Costo cerámica: $\$6.000/\text{m}^2$.
* Piso flotante ($25\%$ más barato): $\$6.000 \times 0{,}75 = \$4.500/\text{m}^2$.
* Alfombra: $\$3.000/\text{m}^2$.
* Presupuesto total: $6000C+4500F+3000Al=900.000$
* La alfombra excede en $24\,\text{m}^2$ al piso flotante: $Al=F+24$

**Sistema:**
$$\begin{cases}C+F+Al=180\\6000C+4500F+3000Al=900.000\\Al-F=24\end{cases}$$

Sustituyendo $Al=F+24$ en las otras dos ecuaciones:

$$C+F+(F+24)=180 \implies C+2F=156 \quad (\star)$$

$$6000C+4500F+3000(F+24)=900.000 \implies 6000C+7500F=828.000 \implies 4C+5F=552 \quad (\star\star)$$

De $(\star)$: $C=156-2F$. Reemplazando en $(\star\star)$:

$$4(156-2F)+5F=552 \implies 624-8F+5F=552 \implies -3F=-72 \implies F=24$$

$$C=156-2(24)=108,\qquad Al=24+24=48$$

$$\boxed{\text{Cerámica: } 108\ \text{m}^2 \qquad \text{Piso flotante: } 24\ \text{m}^2 \qquad \text{Alfombra: } 48\ \text{m}^2}$$

*(Comprobación: Área $108+24+48=180$ ✓; Costo $6000(108)+4500(24)+3000(48)=648.000+108.000+144.000=900.000$ ✓; $Al-F=48-24=24$ ✓)*

---
title: "Práctica 5 — Soluciones"
subtitle: "MAT021B — Matemática de Ingeniería"
tags: [matemáticas, integrales, fracciones-parciales]
---

# Práctica 5 — Fracciones Parciales

Resolución paso a paso de las integrales indefinidas mediante el método de fracciones parciales.

---

## Ejercicio 1.a

$$\int \frac{3}{2(x^2 + 5x - 14)}\, dx$$

### Paso 1: Factorizar el denominador
$$x^2 + 5x - 14 = (x + 7)(x - 2)$$

### Paso 2: Descomponer en fracciones parciales
$$\frac{3}{2(x+7)(x-2)} = \frac{1}{2} \left[ \frac{A}{x+7} + \frac{B}{x-2} \right]$$

$$3 = A(x - 2) + B(x + 7)$$

* Para $x = 2$: $3 = B(9) \implies B = \frac{1}{3}$
* Para $x = -7$: $3 = A(-9) \implies A = -\frac{1}{3}$

### Paso 3: Integrar
$$\int \frac{3}{2(x^2 + 5x - 14)}\, dx = \frac{1}{2} \int \left( \frac{-1/3}{x+7} + \frac{1/3}{x-2} \right) dx$$

$$= \frac{1}{6} \left( -\ln|x+7| + \ln|x-2| \right) + C = \frac{1}{6} \ln\left| \frac{x-2}{x+7} \right| + C$$

$$\boxed{\frac{1}{6} \ln\left| \frac{x-2}{x+7} \right| + C}$$

---

## Ejercicio 1.b

$$\int \frac{x + 14}{(x + 5)(x - 2)}\, dx$$

### Paso 1: Descomponer en fracciones parciales
$$\frac{x + 14}{(x + 5)(x - 2)} = \frac{A}{x + 5} + \frac{B}{x - 2}$$

$$x + 14 = A(x - 2) + B(x + 5)$$

* Para $x = 2$: $16 = B(7) \implies B = \frac{16}{7}$
* Para $x = -5$: $9 = A(-7) \implies A = -\frac{9}{7}$

### Paso 2: Integrar
$$\int \left( \frac{-9/7}{x + 5} + \frac{16/7}{x - 2} \right) dx = -\frac{9}{7} \ln|x + 5| + \frac{16}{7} \ln|x - 2| + C$$

$$\boxed{-\frac{9}{7} \ln|x + 5| + \frac{16}{7} \ln|x - 2| + C}$$

---

## Ejercicio 1.c

$$\int \frac{x + 3}{1 - x^2}\, dx$$

### Paso 1: Factorizar el denominador
$$1 - x^2 = (1 - x)(1 + x)$$

### Paso 2: Descomponer en fracciones parciales
$$\frac{x + 3}{(1 - x)(1 + x)} = \frac{A}{1 - x} + \frac{B}{1 + x}$$

$$x + 3 = A(1 + x) + B(1 - x)$$

* Para $x = 1$: $4 = A(2) \implies A = 2$
* Para $x = -1$: $2 = B(2) \implies B = 1$

### Paso 3: Integrar
$$\int \left( \frac{2}{1 - x} + \frac{1}{1 + x} \right) dx$$

*(Cuidado con la derivada de $1 - x$, que aporta un signo negativo)*:

$$= -2 \ln|1 - x| + \ln|1 + x| + C$$

$$\boxed{-2 \ln|1 - x| + \ln|1 + x| + C}$$

---

## Ejercicio 1.d (P)

$$\int \frac{4x^2 + 13x - 9}{x^3 + 2x^2 - 3x}\, dx$$

### Paso 1: Factorizar el denominador
$$x^3 + 2x^2 - 3x = x(x^2 + 2x - 3) = x(x + 3)(x - 1)$$

### Paso 2: Descomponer en fracciones parciales
$$\frac{4x^2 + 13x - 9}{x(x + 3)(x - 1)} = \frac{A}{x} + \frac{B}{x + 3} + \frac{C}{x - 1}$$

$$4x^2 + 13x - 9 = A(x + 3)(x - 1) + B x(x - 1) + C x(x + 3)$$

* Para $x = 0$: $-9 = A(3)(-1) \implies A = 3$
* Para $x = 1$: $4 + 13 - 9 = C(1)(4) \implies 8 = 4C \implies C = 2$
* Para $x = -3$: $36 - 39 - 9 = B(-3)(-4) \implies -12 = 12B \implies B = -1$

### Paso 3: Integrar
$$\int \left( \frac{3}{x} - \frac{1}{x + 3} + \frac{2}{x - 1} \right) dx = 3 \ln|x| - \ln|x + 3| + 2 \ln|x - 1| + C$$

$$\boxed{3 \ln|x| - \ln|x + 3| + 2 \ln|x - 1| + C}$$

---

## Ejercicio 1.e

$$\int \frac{1}{x^3 - x}\, dx$$

### Paso 1: Factorizar el denominador
$$x^3 - x = x(x^2 - 1) = x(x - 1)(x + 1)$$

### Paso 2: Descomponer en fracciones parciales
$$\frac{1}{x(x - 1)(x + 1)} = \frac{A}{x} + \frac{B}{x - 1} + \frac{C}{x + 1}$$

$$1 = A(x - 1)(x + 1) + B x(x + 1) + C x(x - 1)$$

* Para $x = 0$: $1 = A(-1)(1) \implies A = -1$
* Para $x = 1$: $1 = B(1)(2) \implies B = \frac{1}{2}$
* Para $x = -1$: $1 = C(-1)(-2) \implies C = \frac{1}{2}$

### Paso 3: Integrar
$$\int \left( -\frac{1}{x} + \frac{1/2}{x - 1} + \frac{1/2}{x + 1} \right) dx = -\ln|x| + \frac{1}{2} \ln|x - 1| + \frac{1}{2} \ln|x + 1| + C$$

$$\boxed{-\ln|x| + \frac{1}{2} \ln|x^2 - 1| + C}$$

---

## Ejercicio 1.f

$$\int \frac{6x^2 + 6}{x^3 - 4x^2 + 3x}\, dx$$

### Paso 1: Factorizar el denominador
$$x^3 - 4x^2 + 3x = x(x^2 - 4x + 3) = x(x - 1)(x - 3)$$

### Paso 2: Descomponer en fracciones parciales
$$\frac{6x^2 + 6}{x(x - 1)(x - 3)} = \frac{A}{x} + \frac{B}{x - 1} + \frac{C}{x - 3}$$

$$6x^2 + 6 = A(x - 1)(x - 3) + B x(x - 3) + C x(x - 1)$$

* Para $x = 0$: $6 = A(-1)(-3) \implies A = 2$
* Para $x = 1$: $12 = B(1)(-2) \implies B = -6$
* Para $x = 3$: $60 = C(3)(2) \implies C = 10$

### Paso 3: Integrar
$$\int \left( \frac{2}{x} - \frac{6}{x - 1} + \frac{10}{x - 3} \right) dx = 2 \ln|x| - 6 \ln|x - 1| + 10 \ln|x - 3| + C$$

$$\boxed{2 \ln|x| - 6 \ln|x - 1| + 10 \ln|x - 3| + C}$$

---

## Ejercicio 1.g

$$\int \frac{5x - 2}{(x + 3)^2}\, dx$$

### Paso 1: Descomponer en fracciones parciales
$$\frac{5x - 2}{(x + 3)^2} = \frac{A}{x + 3} + \frac{B}{(x + 3)^2}$$

$$5x - 2 = A(x + 3) + B$$

* Para $x = -3$: $-17 = B$
* Igualando coeficientes de $x$: $A = 5$

### Paso 2: Integrar
$$\int \left( \frac{5}{x + 3} - \frac{17}{(x + 3)^2} \right) dx = 5 \ln|x + 3| + \frac{17}{x + 3} + C$$

$$\boxed{5 \ln|x + 3| + \frac{17}{x + 3} + C}$$

---

## Ejercicio 1.h

$$\int \frac{x^2 - 5x + 16}{(2x - 1)(x - 2)^2}\, dx$$

### Paso 1: Descomponer en fracciones parciales
$$\frac{x^2 - 5x + 16}{(2x - 1)(x - 2)^2} = \frac{A}{2x - 1} + \frac{B}{x - 2} + \frac{C}{(x - 2)^2}$$

$$x^2 - 5x + 16 = A(x - 2)^2 + B(2x - 1)(x - 2) + C(2x - 1)$$

* Para $x = 2$: $10 = C(3) \implies C = \frac{10}{3}$
* Para $x = \frac{1}{2}$: $\frac{55}{4} = A\left(-\frac{3}{2}\right)^2 \implies A = \frac{55}{9}$
* Para $x = 0$: $16 = 4A + 2B - C \implies 16 = \frac{220}{9} + 2B - \frac{10}{3} \implies B = -\frac{23}{9}$

### Paso 2: Integrar
$$\int \left( \frac{55/9}{2x - 1} - \frac{23/9}{x - 2} + \frac{10/3}{(x - 2)^2} \right) dx$$

$$= \frac{55}{18} \ln|2x - 1| - \frac{23}{9} \ln|x - 2| - \frac{10}{3(x - 2)} + C$$

$$\boxed{\frac{55}{18} \ln|2x - 1| - \frac{23}{9} \ln|x - 2| - \frac{10}{3(x - 2)} + C}$$

---

## Ejercicio 1.i (P)

$$\int \frac{3x^3 - 8x^2 + 10}{x(x - 1)^3}\, dx$$

### Paso 1: Descomponer en fracciones parciales
$$\frac{3x^3 - 8x^2 + 10}{x(x - 1)^3} = \frac{A}{x} + \frac{B}{x - 1} + \frac{C}{(x - 1)^2} + \frac{D}{(x - 1)^3}$$

* Para $x = 0$: $10 = -A \implies A = -10$
* Para $x = 1$: $5 = D$
* Coeficiente de $x^3$: $3 = A + B \implies B = 13$
* Evaluando en $x = 2$: $2 = -10 + 26 + 2C + 10 \implies C = -12$

### Paso 2: Integrar
$$\int \left( -\frac{10}{x} + \frac{13}{x - 1} - \frac{12}{(x - 1)^2} + \frac{5}{(x - 1)^3} \right) dx$$

$$\boxed{-10 \ln|x| + 13 \ln|x - 1| + \frac{12}{x - 1} - \frac{5}{2(x - 1)^2} + C}$$

---

## Ejercicio 1.j

$$\int \frac{1}{s^2(s - 1)^2}\, ds$$

### Paso 1: Descomponer en fracciones parciales
$$\frac{1}{s^2(s - 1)^2} = \frac{A}{s} + \frac{B}{s^2} + \frac{C}{s - 1} + \frac{D}{(s - 1)^2}$$

* Para $s = 0$: $1 = B$
* Para $s = 1$: $1 = D$
* Coeficiente de $s^3$: $0 = A + C \implies C = -A$
* Evaluando en $s = 2$: $1 = 2A + 1 - 4A + 4 \implies A = 2 \implies C = -2$

### Paso 2: Integrar
$$\int \left( \frac{2}{s} + \frac{1}{s^2} - \frac{2}{s - 1} + \frac{1}{(s - 1)^2} \right) ds$$

$$\boxed{2 \ln\left|\frac{s}{s - 1}\right| - \frac{1}{s} - \frac{1}{s - 1} + C}$$

---

## Ejercicio 1.k (P)

$$\int \frac{9t^2}{(t - 1)^2(t + 2)^2}\, dt$$

### Paso 1: Descomponer en fracciones parciales
$$\frac{9t^2}{(t - 1)^2(t + 2)^2} = \frac{A}{t - 1} + \frac{B}{(t - 1)^2} + \frac{C}{t + 2} + \frac{D}{(t + 2)^2}$$

* Para $t = 1$: $9 = 9B \implies B = 1$
* Para $t = -2$: $36 = 9D \implies D = 4$
* Coeficiente de $t^3$: $0 = A + C \implies C = -A$
* Evaluando en $t = 0$: $0 = -4A + 4 - 2A + 4 \implies A = \frac{4}{3} \implies C = -\frac{4}{3}$

### Paso 2: Integrar
$$\int \left( \frac{4/3}{t - 1} + \frac{1}{(t - 1)^2} - \frac{4/3}{t + 2} + \frac{4}{(t + 2)^2} \right) dt$$

$$\boxed{\frac{4}{3} \ln\left|\frac{t - 1}{t + 2}\right| - \frac{1}{t - 1} - \frac{4}{t + 2} + C}$$

---

## Ejercicio 1.l

$$\int \frac{x^2 + 1}{(x - 3)^2 x^3}\, dx$$

### Paso 1: Descomponer en fracciones parciales
$$\frac{x^2 + 1}{x^3(x - 3)^2} = \frac{A}{x} + \frac{B}{x^2} + \frac{C}{x^3} + \frac{D}{x - 3} + \frac{E}{(x - 3)^2}$$

* Para $x = 0$: $1 = 9C \implies C = \frac{1}{9}$
* Para $x = 3$: $10 = 27E \implies E = \frac{10}{27}$
* Resolviendo sistema para $A$, $B$, $D$: $A = \frac{4}{27}$, $B = \frac{2}{27}$, $D = -\frac{4}{27}$

### Paso 2: Integrar
$$\int \left( \frac{4/27}{x} + \frac{2/27}{x^2} + \frac{1/9}{x^3} - \frac{4/27}{x - 3} + \frac{10/27}{(x - 3)^2} \right) dx$$

$$\boxed{\frac{4}{27} \ln\left|\frac{x}{x - 3}\right| - \frac{2}{27x} - \frac{1}{18x^2} - \frac{10}{27(x - 3)} + C}$$