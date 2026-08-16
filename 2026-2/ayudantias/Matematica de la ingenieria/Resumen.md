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

> [!tip] Truco para recordar el orden
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

> [!warning] Regla de compatibilidad
> El producto $A \cdot B$ **solo existe** si el número de **columnas de $A$** coincide con el número de **filas de $B$**.

$$
\underbrace{A}_{\color{blue}{m}\ \times\ \color{#e74c3c}{n}} \quad \cdot \quad \underbrace{B}_{\color{#e74c3c}{n}\ \times\ \color{blue}{p}} \quad = \quad \underbrace{C}_{\color{blue}{m}\ \times\ \color{blue}{p}}
$$

- 🔴 Los números **rojos** ($n$) deben ser **iguales**: eso es lo que se revisa para saber si "se puede multiplicar".
- 🔵 Los números **azules** ($m$ y $p$) sobreviven y forman el **orden del resultado** $C$.

> [!example] Regla mnemotécnica
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

> [!danger] Ojo
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

> [!important] Teorema (existencia)
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
4x+y-2z=-3\\
3x-y+4z=-2\\
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

> [!success] Resumen rápido de fórmulas
> - $2\times2$: $\det = ad-bc$
> - $A$ invertible $\iff \det(A)\neq0$
> - $A^{-1}=\dfrac{1}{\det A}(\mathrm{Cof}\,A)^T$
> - $AX=B \Rightarrow X=A^{-1}B$ — pero $XA=B \Rightarrow X=B\,A^{-1}$ (¡el lado importa!)
