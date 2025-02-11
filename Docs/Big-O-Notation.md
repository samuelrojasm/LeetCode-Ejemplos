# 📈 Big-O Notation: Análisis de Complejidad Computacional 

Este documento (`Big-O-Notation.md`) proporciona una explicación detallada de la **Notación Big-O**, una herramienta fundamental en la informática utilizada para analizar la eficiencia de algoritmos en términos de **tiempo de ejecución** y **uso de memoria**.  

## 📌 ¿Qué es la Notación Big-O?  
La **Notación Big-O** describe el **comportamiento asintótico** de un algoritmo, es decir, **cómo su rendimiento escala a medida que aumenta el tamaño de la entrada** \(n\). Nos permite comparar la eficiencia de diferentes algoritmos sin necesidad de ejecutar código.

💡 **Ejemplo:** Si un algoritmo tiene una complejidad de **O(n)**, significa que el tiempo de ejecución crece proporcionalmente con el tamaño de la entrada.  

---

## 📖 Contenido del Documento  

✅ **Conceptos clave** sobre la notación Big-O.  
✅ **Diferentes tipos de complejidad temporal y cantidad de memoria.**  
✅ **Ejemplos de análisis de algoritmos con Big-O.**  
✅ **Casos Peor, Mejor y Promedio.**   
✅ **Tabla de complejidades comunes y su impacto.**  
✅ **Factores Claves para un Algoritmo Eficiente.**  
✅ **Crecimiento de Diferentes Complejidades**  

---

## 🎯 ¿Por qué es importante Big-O?  
✅ Permite comparar algoritmos y seleccionar el más eficiente.  
✅ Ayuda a evitar soluciones que se vuelven ineficientes en grandes volúmenes de datos.  
✅ Es fundamental en entrevistas técnicas de programación.  

---

## ⚡ Complejidades Comunes en Big-O  

| Notación | Nombre | Ejemplo |
|----------|-------------------|--------------------|
| **O(1)** | Tiempo constante | Acceder a un elemento en un array |
| **O(log n)** | Tiempo logarítmico | Búsqueda binaria |
| **O(n)** | Tiempo lineal | Recorrer un array |
| **O(n log n)** | Tiempo casi lineal | MergeSort, QuickSort (mejor caso) |
| **O(n²)** | Tiempo cuadrático | Algoritmo de burbuja, bucles anidados |
| **O(2ⁿ)** | Tiempo exponencial | Algoritmos de backtracking (ej. N-Reinas) |
| **O(n!)** | Tiempo factorial | Algoritmo de fuerza bruta en permutaciones, Problema del viajero (TSP) |

📌 **Mientras menor sea la complejidad, más eficiente será el algoritmo.**  

---

## 🛠 Ejemplo de Análisis con Big-O  

**Ejemplo 1: Algoritmo con O(n)** 
- Este algoritmo recorre 𝑛 elementos, por lo que su complejidad es O(n)
- El tiempo de ejecución crece proporcionalmente con el tamaño de la entrada.
```python
def print_numbers(n):
    for i in range(n):
        print(i)

# Llamar a print_numbers(5) imprimirá 0,1,2,3,4 -> O(n)
```

**Ejemplo 2: Algoritmo con O(n²)**
- Dado que hay un bucle dentro de otro, la complejidad se vuelve O(n²)
```python
def print_pairs(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# Doble ciclo anidado -> O(n²)
```

---

## **📊 Tabla de Complejidades Comunes y su Impacto** 

| **Notación**      | **Nombre**              | **Ejemplo de Algoritmo**          | **Impacto en el Rendimiento**  |
|------------------|------------------------|----------------------------------|-------------------------------|
| **O(1)**         | Tiempo constante        | Acceder a un elemento en un array | Excelente, sin importar el tamaño del input. |
| **O(log n)**     | Tiempo logarítmico      | Búsqueda binaria                 | Muy eficiente incluso para grandes entradas. |
| **O(n)**         | Tiempo lineal           | Búsqueda en una lista no ordenada | Aceptable para tamaños moderados. |
| **O(n log n)**   | Tiempo casi lineal      | MergeSort, QuickSort (promedio)   | Bueno para ordenamiento eficiente. |
| **O(n²)**        | Tiempo cuadrático       | Bubble Sort, Insertion Sort       | Malo para grandes volúmenes de datos. |
| **O(2ⁿ)**        | Tiempo exponencial      | Recursión en la serie de Fibonacci | Impráctico para grandes `n`. |
| **O(n!)**        | Tiempo factorial        | Algoritmos de fuerza bruta en combinaciones | Extremadamente lento incluso para `n=20`. |

📌 **Conclusión:**  
- **O(1), O(log n) y O(n log n)** son ideales para algoritmos eficientes.  
- **O(n²), O(2ⁿ) y O(n!)** deben evitarse en entradas grandes.  

🔎 **Ejemplo práctico:**  
- Si tienes `n = 1,000,000`, una búsqueda en **O(log n)** tomará alrededor de **20 operaciones**, mientras que una en **O(n)** tomará **1,000,000 operaciones**. ¡Elegir bien la complejidad hace una gran diferencia! 🚀

---

## 📊 Análisis de Complejidad: Casos Peor, Mejor y Promedio  

Cuando analizamos la eficiencia de un algoritmo, es importante considerar tres escenarios distintos:  

1️⃣ **Peor Caso (Worst Case, O)**  
2️⃣ **Mejor Caso (Best Case, Ω)**  
3️⃣ **Caso Promedio (Average Case, Θ)**  

📌 **El Peor Caso** es el más útil para garantizar eficiencia. Sin embargo, el **Caso Promedio** suele reflejar mejor el rendimiento real. 🚀

---

### **1️⃣ Peor Caso (Worst Case - O)**  
🔹 Representado por **O (Big-O Notation)**  
🔹 Es el tiempo máximo que tomará el algoritmo en ejecutarse.  
🔹 Se usa para garantizar que un algoritmo no supere un cierto límite de tiempo.  

#### **Ejemplo: Búsqueda en un arreglo desordenado (O(n))**
📌 **Peor caso**: Si el objetivo está al final de la lista o no está presente, se recorre toda la lista → O(n)  
```python
def buscar(lista, objetivo):
    for elemento in lista:
        if elemento == objetivo:
            return True
    return False
```

---

### **2️⃣ Mejor Caso (Best Case - Ω)**
🔹 Representado por Ω (Omega Notation).  
🔹 Es el tiempo mínimo que puede tomar el algoritmo en ejecutarse.  
🔹 No siempre es útil, porque no siempre ocurre en la práctica.  

#### **Ejemplo: Búsqueda en una lista ordenada (Ω(1))**
📌 **Mejor caso**: Si el objetivo está en la primera posición, se encuentra en O(1).  
```python
def buscar(lista, objetivo):
    if lista[0] == objetivo:
        return True
    return buscar(lista[1:], objetivo)  # Continúa la búsqueda
```

---

### **3️⃣ Caso Promedio (Average Case - Θ)**
🔹 Representado por Θ (Theta Notation)  
🔹 Es el tiempo esperado si todas las entradas son igualmente probables.  
🔹 Se usa en análisis probabilístico cuando el peor caso no siempre es realista.  

#### Ejemplo: Búsqueda en un arreglo desordenado
📌 **Caso promedio**: En una lista de tamaño n, se asume que el elemento se encuentra en la mitad → O(n/2) ≈ O(n).
    - Si el objetivo está al inicio → O(1)
    - Si el objetivo está en el medio → O(n/2)
    - Si el objetivo no está → O(n)

---

### **🔎 Ejemplo con Algoritmo de Ordenamiento: QuickSort**  

| **Caso**         | **Descripción** | **Complejidad** |
|-----------------|----------------|----------------|
| **Peor Caso (O)** | Ocurre cuando siempre elegimos el peor pivote, es decir, el elemento más pequeño o más grande, y el array está ordenado inversamente. | **O(n²)** |
| **Mejor Caso (Ω)** | Se da cuando siempre elegimos el pivote ideal, dividiendo el array en partes iguales en cada iteración. | **O(n log n)** |
| **Caso Promedio (Θ)** | En la mayoría de los casos, QuickSort se comporta de manera eficiente al dividir los elementos de forma más equilibrada. | **O(n log n)** |

---

### 📊 **Resumen de Análisis de Complejidad**  

| **Tipo de Caso**  | **Notación**  | **Cuándo ocurre**  |
|------------------|-------------|------------------|
| **Peor Caso**    | **O(f(n))**  | Cuando el algoritmo tarda lo máximo posible en ejecutarse. |
| **Mejor Caso**   | **Ω(f(n))**  | Cuando el algoritmo se ejecuta en el menor tiempo posible. |
| **Caso Promedio** | **Θ(f(n))**  | Tiempo esperado considerando una entrada aleatoria. |

---

## 🎯 Factores Claves para un Algoritmo Eficiente

Al crear un **algoritmo eficiente** para **análisis de datos**, es crucial considerar los siguientes puntos para asegurarte de que cumple con los parámetros adecuados en términos de **tiempo** y **uso de memoria**.  

---

### **1️⃣ Complejidad Temporal (Tiempo de Ejecución - O(f(n)))**
🔹 Evalúa el **número de operaciones** que realiza el algoritmo en función del tamaño de los datos `n`.  
🔹 Evita **complejidades ineficientes** (`O(n²)`, `O(2ⁿ)`, `O(n!)`).  
🔹 Prefiere estructuras eficientes como **búsqueda binaria (`O(log n)`)** o **dividir y vencer (`O(n log n)`)**.  

#### **✔ Solución:**
- Usa **estructuras de datos eficientes** como `set`, `dict` en Python o `HashMap` en Java.
- Prefiere algoritmos con menor crecimiento de complejidad, como **búsqueda binaria** y **ordenamiento eficiente**.  

#### **Ejemplo:**
**Búsqueda en una lista ordenada usando búsqueda binaria (O(log n)):**  
```python
def busqueda_binaria(lista, objetivo):
    bajo = 0
    alto = len(lista) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1
```
📌 **Complejidad: O(log n)**, ya que reduce el tamaño del problema a la mitad en cada iteración.  

---

### **2️⃣ Complejidad Espacial (Uso de Memoria - O(f(n)))**  
🔹 Determina cuánto espacio adicional usa el algoritmo más allá de los datos de entrada.  
🔹 Evita estructuras innecesarias que dupliquen la memoria utilizada.  
🔹 Ten cuidado con la recursividad profunda, ya que consume espacio en la pila de ejecución (stack).  

#### **✔ Solución:**
- Usa iteraciones en lugar de recursión cuando sea posible.  
- Evita copiar grandes estructuras, usa referencias para manejar datos.  
- Procesa los datos en streaming para no cargar todo en memoria.  

#### **Ejemplo:**
Uso de yield para procesamiento en streaming.  
```python
def leer_lineas(archivo):
    with open(archivo, 'r') as f:
        for linea in f:
            yield linea.strip()
```
📌 Complejidad espacial: O(1), ya que solo mantiene una línea de texto en memoria a la vez.  

---

### **3️⃣ Estructuras de Datos Adecuadas**  
🔹 Elegir la estructura de datos correcta reduce la complejidad de las operaciones que realizas en el algoritmo.  

#### 📊 Tabla: Estructuras de Datos y su Complejidad  

| **Tarea**                  | **Estructura Recomendada**       | **Complejidad** |
|----------------------------|---------------------------------|-----------------|
| **Buscar elemento rápido**  | `Hash Table` (`dict`, `HashMap`) | **O(1)**       |
| **Ordenar datos**          | `Heap`, Árboles Balanceados      | **O(n log n)**  |
| **Acceder por índice**      | `Array`, `Lista`                | **O(1)**       |
| **Insertar en cualquier parte** | `Lista Enlazada`          | **O(1) - O(n)** |
| **Procesar en orden FIFO**  | `Cola` (`Queue`)                | **O(1)**       |
| **Procesar en orden LIFO**  | `Pila` (`Stack`)                | **O(1)**       |

📌 Ejemplo: Si necesitas buscar valores rápidamente, usa un **set** o **dict**, ya que la búsqueda es O(1) en lugar de O(n) con listas.  

---

### **4️⃣ Evitar Bucles Ineficientes** 
🔹 Evita bucles anidados innecesarios (O(n²)) si se puede usar una estructura más eficiente.  
🔹 Ejemplo malo:  
```python
# O(n²) - Ineficiente
for i in lista:
    for j in otra_lista:
        if i == j:
            print(i)
```

🔹 Ejemplo mejorado (O(n)) con **set**:  
```python
# O(n) - Eficiente
conjunto = set(otra_lista)
for i in lista:
    if i in conjunto:
        print(i)
```
📌 Mejoramos de O(n²) a O(n) usando un set! 🚀  

---

### **5️⃣ Uso Eficiente de Librerías y Paralelismo**  
🔹 En Python, usa librerías optimizadas como **NumPy**, **Pandas**, multiprocessing para acelerar cálculos.
🔹 En Big Data, usa frameworks distribuidos como **Apache Spark** o **Dask**.
🔹 Implementa **paralelismo** y **concurrencia** para procesar datos en varios núcleos de CPU.

#### **✔ Solución:**
```python
# Uso de multiprocessing en Python para dividir el trabajo
from multiprocessing import Pool

def calcular(x):
    return x * x

datos = [1, 2, 3, 4, 5]
with Pool() as p:
    resultados = p.map(calcular, datos)
print(resultados)
```
📌 Mejora el tiempo de ejecución al usar múltiples núcleos del procesador para realizar cálculos en paralelo.  

---

### 📊  **Resumen de Factores Claves para un Algoritmo Eficiente**

| **Factor**                          | **¿Qué hacer?** |
|--------------------------------------|-----------------|
| **Tiempo de ejecución (`O(f(n))`)**  | Optimiza estructuras de datos, evita bucles innecesarios. |
| **Uso de memoria (`O(f(n))`)**       | Reduce duplicaciones, usa `yield` o `iterables`. |
| **Estructuras adecuadas**            | Usa `set`, `dict`, `heap`, `queue` según la necesidad. |
| **Bucles eficientes**                | Evita `O(n²)`, usa `set` o `dict` para búsquedas. |
| **Paralelismo**                      | Usa `multiprocessing`, `NumPy`, `Spark` en Big Data. |

📌 Si optimizas estos puntos, tu algoritmo será eficiente y escalable en términos de tiempo y memoria. 🚀

---

## 📈 Crecimiento de Diferentes Complejidades  
El crecimiento de la complejidad de un algoritmo describe cómo aumentan el **tiempo de ejecución** y el **uso de memoria** en función del tamaño de la entrada (`n`).  
Podemos representar estas **complejidades comunes** con gráficos que ilustran su comportamiento.  

---

### 💡 Crecimiento de algunas funciones de complejidad comunes
🔎  **Explicación:**  
- **O(1):** Tiempo constante, no importa el tamaño de `n`.  
- **O(log n):** Crece lentamente, ejemplo: búsqueda binaria.  
- **O(n):** Crecimiento lineal, ejemplo: recorrido de una lista.  
- **O(n log n):** Crece más rápido, pero sigue siendo eficiente, ejemplo: QuickSort.  
- **O(n²):** Cuadrático, se vuelve lento con `n` grande, ejemplo: bubble sort.  
- **O(2ⁿ):** Exponencial, muy ineficiente para valores altos de `n`.  

---

### 📊 Comparación en Tabla  

| **Complejidad** | **Ejemplo de Algoritmo**    | **Crecimiento** |
|----------------|---------------------------|----------------|
| **O(1)**       | Acceso a un array (`arr[i]`) | Constante |
| **O(log n)**   | Búsqueda binaria           | Muy lento |
| **O(n)**       | Recorrer una lista         | Lineal |
| **O(n log n)** | QuickSort, MergeSort       | Cuasi-lineal |
| **O(n²)**      | Bubble Sort, Selection Sort | Cuadrático |
| **O(2ⁿ)**      | Algoritmo de fuerza bruta  | Exponencial |

---

### 🔢 Código en Python para Generar el Gráfico  
Si deseas generar tu propio gráfico de crecimiento de complejidad, usa el siguiente código en Python:  
```python
import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(1, 10, 100)

plt.figure(figsize=(8, 6))
plt.plot(n, np.ones_like(n), label="O(1)", linestyle='dashed')
plt.plot(n, np.log2(n), label="O(log n)")
plt.plot(n, n, label="O(n)")
plt.plot(n, n * np.log2(n), label="O(n log n)")
plt.plot(n, n**2, label="O(n²)")
plt.plot(n, 2**n, label="O(2ⁿ)")

plt.ylim(0, 100)
plt.legend()
plt.xlabel("Tamaño de Entrada (n)")
plt.ylabel("Operaciones")
plt.title("Crecimiento de Complejidad")
plt.show()
```

---

## 📚 Recursos Adicionales  
📖 [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)  
🎥 [Video Explicativo en YouTube](https://www.youtube.com/watch?v=__vX2sjlpXU)  
📖 [CS50 Harvard - Introducción a Algoritmos](https://cs50.harvard.edu/)  
