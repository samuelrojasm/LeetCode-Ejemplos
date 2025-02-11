# Sorting Algorithms
El ordenamiento es un proceso fundamental en la informática y una de las bases de muchos problemas en LeetCode. Comprender diferentes algoritmos de ordenamiento es clave para optimizar el rendimiento de las soluciones.

En este documento, exploraremos los algoritmos de ordenamiento más utilizados, su complejidad y sus casos de uso más comunes en problemas de programación competitiva. 🚀

---

## 1️⃣ Tipos de Algoritmos de Ordenamiento

Podemos clasificar los algoritmos de ordenamiento en dos grandes categorías:

- **Ordenamiento basado en comparación**: Compara elementos entre sí para determinar su orden. Ejemplos: QuickSort, MergeSort, HeapSort.
- **Ordenamiento no basado en comparación**: Utiliza características de los números para ordenarlos sin comparaciones directas. Ejemplos: Counting Sort, Radix Sort, Bucket Sort.

---

## 2️⃣ Algoritmos Basados en Comparación

### **2.1. Bubble Sort**
- **Descripción**: Compara elementos adyacentes y los intercambia si están en el orden incorrecto. Se repite hasta que la lista esté ordenada.
- **Complejidad**:
  - Peor caso: **O(n²)**
  - Mejor caso: **O(n)** (cuando ya está ordenado con una optimización)
- **Implementación**:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
```

### **2.2. Selection Sort**
- **Descripción**: Encuentra el mínimo y lo coloca en la primera posición, luego repite para el resto.
- **Complejidad**:
  - Peor caso: **O(n²)**
  - Mejor caso: **O(n²)**
- **Implementación**:

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

### **2.3. Insertion Sort**
- **Descripción**: Inserta cada elemento en su posición correcta dentro de la parte ordenada del array.
- **Complejidad**:
  - Peor caso: **O(n²)**
  - Mejor caso: **O(n)** (cuando ya está ordenado)
- **Implementación**:

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

### **2.4. Merge Sort**
- **Descripción**: Divide el array en dos mitades, ordena cada una y luego las fusiona.
- **Complejidad**:
  - Peor caso: **O(n log n)**
  - Mejor caso: **O(n log n)**
- **Implementación**:

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)
    return arr

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

### **2.5. QuickSort**
- **Descripción**: Selecciona un pivote, coloca los elementos menores a la izquierda y los mayores a la derecha, y recursivamente ordena las particiones.
- **Complejidad**:
  - Peor caso: **O(n²)** (cuando el pivote es el menor o el mayor)
  - Mejor caso: **O(n log n)**
- **Implementación**:

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

---

## 3️⃣ Algoritmos No Basados en Comparación
### 3.1. Counting Sort
- **Descripción**: Ordena contando la frecuencia de cada elemento y reconstruyendo el array.
- **Complejidad**: **O(n + k)** (donde k es el valor máximo del array)
- **Implementación**:

```python
def counting_sort(arr):
    if not arr:
        return []
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for i, c in enumerate(count):
        sorted_arr.extend([i] * c)
    return sorted_arr
```

### 3.2. Radix Sort
- **Descripción**: Ordena números de menor a mayor posición decimal utilizando Counting Sort en cada dígito.
- **Complejidad**: O(nk) (donde k es el número de dígitos)
- **Implementación**:
```python
def radix_sort(arr):
    max_num = max(arr, default=0)
    exp = 1
    while max_num // exp > 0:
        arr = counting_sort_by_digit(arr, exp)
        exp *= 10
    return arr

def counting_sort_by_digit(arr, exp):
    output = [0] * len(arr)
    count = [0] * 10
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for num in reversed(arr):
        index = (num // exp) % 10
        output[count[index] - 1] = num
        count[index] -= 1
    return output
```

### 3.3. Bucket Sort
- **Descripción**: Es un algoritmo de ordenación basado en la idea de dividir el conjunto de elementos en "cubos" (buckets) y ordenar cada cubo individualmente. Luego, los elementos de los cubos se combinan para obtener la secuencia ordenada.

- **Complejidad**:
    - **Mejor Caso:**  
  O(n + k), donde `n` es el número de elementos y `k` es el número de cubos. Si los elementos están distribuidos uniformemente, cada cubo tiene aproximadamente `n/k` elementos, lo que puede hacer que la ordenación dentro de cada cubo sea eficiente.
    - **Peor Caso:**  
  O(n²), cuando todos los elementos caen en un solo cubo y el algoritmo de ordenación dentro del cubo tiene una complejidad O(n²), como Insertion Sort.
    - **Promedio:**  
  O(n + k + n²/k), dependiendo de cómo estén distribuidos los elementos y la estrategia de ordenación interna.
    - **Espacio Extra:**  
  O(n + k), debido a los cubos y la lista de entrada.

- **Implementación**:
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    
    # Paso 1: Encontrar el rango de los elementos
    min_value = min(arr)
    max_value = max(arr)
    
    # Paso 2: Crear los cubos
    bucket_count = len(arr)  # Número de cubos
    buckets = [[] for _ in range(bucket_count)]
    
    # Paso 3: Distribuir los elementos en los cubos
    for num in arr:
        index = (num - min_value) * (bucket_count - 1) // (max_value - min_value) if max_value != min_value else 0
        buckets[index].append(num)
    
    # Paso 4: Ordenar los cubos y combinar
    sorted_arr = []
    for bucket in buckets:
        insertion_sort(bucket)  # Ordenar cada cubo con Insertion Sort
        sorted_arr.extend(bucket)  # Concatenar los cubos ordenados
    
    return sorted_arr

# Ejemplo de uso
arr = [0.42, 0.32, 0.23, 0.53, 0.51, 0.12, 0.24, 0.44]
print("Lista ordenada:", bucket_sort(arr))
```

---

## 4️⃣ Comparación de Algoritmos
A continuación, se presenta una comparación de los algoritmos de ordenamiento en términos de complejidad temporal en diferentes escenarios (mejor caso, peor caso y caso promedio). Esta tabla permite visualizar qué algoritmos son más eficientes según la situación:

---

| Algoritmo      | Mejor Caso | Peor Caso | Promedio | Estable | In-Place |
|---------------|------------|------------|------------|------------|------------|
| Bubble Sort   | O(n)       | O(n²)      | O(n²)      | ✔️  | ✔️ |
| Selection Sort| O(n²)      | O(n²)      | O(n²)      | ❌ | ✔️ |
| Insertion Sort| O(n)       | O(n²)      | O(n²)      | ✔️  | ✔️ |
| Merge Sort    | O(n log n) | O(n log n) | O(n log n) | ✔️  | ❌ |
| QuickSort     | O(n log n) | O(n²)      | O(n log n) | ❌ | ✔️ |
| Counting Sort | O(n + k)   | O(n + k)   | O(n + k)   | ✔️  | ❌ |
| Radix Sort    | O(nk)      | O(nk)      | O(nk)      | ✔️  | ❌ |


- **Algoritmos como QuickSort y MergeSort** son eficientes para listas grandes con una complejidad promedio de **O(n log n)**, aunque QuickSort puede degradarse a **O(n²)** en el peor caso sin una buena elección del pivote.
- **Bubble Sort, Selection Sort e Insertion Sort** son más ineficientes en listas grandes debido a su complejidad **O(n²)**, aunque Insertion Sort es eficiente para listas casi ordenadas.
- **Counting Sort y otros algoritmos no basados en comparación** pueden ser más rápidos que **O(n log n)** en ciertos casos, pero requieren restricciones en el dominio de los datos (como números en un rango limitado).

Esta comparación es clave para seleccionar el algoritmo adecuado dependiendo de las restricciones del problema. 🚀

### 📌 Explicación de la tabla:
#### Columna "Estable"
La columna "Estable" indica si el algoritmo es estable o no. Un algoritmo de ordenación se considera estable si, cuando dos elementos tienen el mismo valor, mantienen su orden relativo original después de ser ordenados.

Es decir, si dos elementos en la lista son iguales, un algoritmo estable los mantendrá en el mismo orden en el que aparecían antes de la ordenación, mientras que un algoritmo inestable podría cambiarlos de lugar.

Por ejemplo:

- Bubble Sort, Insertion Sort y Merge Sort son algoritmos estables porque no alteran el orden relativo de los elementos iguales.
- QuickSort, Selection Sort, Counting Sort y Radix Sort no son estables (a menos que se implementen específicamente para serlo).

En la tabla:

- ✔️ indica que el algoritmo es estable.
- ❌ indica que el algoritmo no es estable.

#### Columna "In-Place"
La columna "In-Place" indica si el algoritmo de ordenación modifica los elementos directamente en el espacio de memoria original, sin necesidad de usar espacio adicional significativo. Un algoritmo se considera "in-place" si no requiere memoria extra proporcional al tamaño de la entrada, es decir, si puede realizar la ordenación con una cantidad de espacio constante (en general, O(1)).

En la tabla:

- ✔️ en la columna "In-Place" significa que el algoritmo es in-place, es decir, realiza la ordenación sin usar espacio adicional significativo.
- ❌ indica que el algoritmo no es in-place, lo que implica que utiliza espacio adicional para realizar la ordenación.

Por ejemplo:

- Bubble Sort es in-place, ya que solo intercambia los elementos en el arreglo original.
- Merge Sort no es in-place, ya que necesita un arreglo adicional para realizar la combinación de las partes ordenadas.

---
