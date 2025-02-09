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

## 📊 Análisis de Complejidad: Casos Peor, Mejor y Promedio  

Cuando analizamos la eficiencia de un algoritmo, es importante considerar tres escenarios distintos:  

1️⃣ **Peor Caso (Worst Case, O)**  
2️⃣ **Mejor Caso (Best Case, Ω)**  
3️⃣ **Caso Promedio (Average Case, Θ)**

- El Peor Caso es el más útil para garantizar eficiencia. Sin embargo, el Caso Promedio suele reflejar mejor el rendimiento real. 🚀

---

### **1️⃣ Peor Caso (Worst Case - O)**  
🔹 Representado por **O (Big-O Notation)** 
🔹 Es el tiempo máximo que tomará el algoritmo en ejecutarse.
🔹 Se usa para garantizar que un algoritmo no supere un cierto límite de tiempo.

#### **Ejemplo: Búsqueda en un arreglo desordenado (O(n))**
- 📌 Peor caso: Si el objetivo está al final de la lista o no está presente, se recorre toda la lista → O(n)
```python
def buscar(lista, objetivo):
    for elemento in lista:
        if elemento == objetivo:
            return True
    return False
```

### **2️⃣ Mejor Caso (Best Case - Ω)**
🔹 Representado por Ω (Omega Notation).
🔹 Es el tiempo mínimo que puede tomar el algoritmo en ejecutarse.
🔹 No siempre es útil, porque no siempre ocurre en la práctica.

#### **Ejemplo: Búsqueda en una lista ordenada (Ω(1))**
- 📌 Mejor caso: Si el objetivo está en la primera posición, se encuentra en O(1).
```python
def buscar(lista, objetivo):
    if lista[0] == objetivo:
        return True
    return buscar(lista[1:], objetivo)  # Continúa la búsqueda
```

### **3️⃣ Caso Promedio (Average Case - Θ)**
🔹 Representado por Θ (Theta Notation)
🔹 Es el tiempo esperado si todas las entradas son igualmente probables.
🔹 Se usa en análisis probabilístico cuando el peor caso no siempre es realista.

#### Ejemplo: Búsqueda en un arreglo desordenado
- 📌 Caso promedio: En una lista de tamaño n, se asume que el elemento se encuentra en la mitad → O(n/2) ≈ O(n).
    - Si el objetivo está al inicio → O(1)
    - Si el objetivo está en el medio → O(n/2)
    - Si el objetivo no está → O(n)

### **🔎 Ejemplo con Algoritmo de Ordenamiento: QuickSort**  

| **Caso**         | **Descripción** | **Complejidad** |
|-----------------|----------------|----------------|
| **Peor Caso (O)** | Ocurre cuando siempre elegimos el peor pivote, es decir, el elemento más pequeño o más grande, y el array está ordenado inversamente. | **O(n²)** |
| **Mejor Caso (Ω)** | Se da cuando siempre elegimos el pivote ideal, dividiendo el array en partes iguales en cada iteración. | **O(n log n)** |
| **Caso Promedio (Θ)** | En la mayoría de los casos, QuickSort se comporta de manera eficiente al dividir los elementos de forma más equilibrada. | **O(n log n)** |

### **📌 Resumen**  

| **Tipo de Caso**  | **Notación**  | **Cuándo ocurre**  |
|------------------|-------------|------------------|
| **Peor Caso**    | **O(f(n))**  | Cuando el algoritmo tarda lo máximo posible en ejecutarse. |
| **Mejor Caso**   | **Ω(f(n))**  | Cuando el algoritmo se ejecuta en el menor tiempo posible. |
| **Caso Promedio** | **Θ(f(n))**  | Tiempo esperado considerando una entrada aleatoria. |


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

---

🔎 **Ejemplo práctico:**  
Si tienes `n = 1,000,000`, una búsqueda en **O(log n)** tomará alrededor de **20 operaciones**, mientras que una en **O(n)** tomará **1,000,000 operaciones**. ¡Elegir bien la complejidad hace una gran diferencia! 🚀

---

## 🎯 ¿Por qué es importante Big-O?  
✅ Permite comparar algoritmos y seleccionar el más eficiente.  
✅ Ayuda a evitar soluciones que se vuelven ineficientes en grandes volúmenes de datos.  
✅ Es fundamental en entrevistas técnicas de programación.  

---

## 📂 Contenido del Archivo `Big-O-Notation.md`  
En el documento `Big-O-Notation.md` encontrarás:  
✔️ Explicaciones detalladas de cada complejidad.  
✔️ Ejemplos de código en Python y C++.  
✔️ Diagramas para ilustrar el crecimiento de la complejidad.  
✔️ Comparaciones entre diferentes enfoques algorítmicos.  

---

## 📚 Recursos Adicionales  
📖 [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)  
🎥 [Video Explicativo en YouTube](https://www.youtube.com/watch?v=__vX2sjlpXU) 
📖 [CS50 Harvard - Introducción a Algoritmos](https://cs50.harvard.edu/)

---


---

