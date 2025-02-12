# 🟢 Conjuntos en Python (`set`)
- Los **conjuntos** en Python son una estructura de datos que almacena elementos **únicos y desordenados**. 
- Son especialmente útiles para realizar operaciones matemáticas como **unión, intersección y diferencia**, además de ser eficientes para comprobar si un elemento pertenece a un conjunto.

---

## ✨ Características de los conjuntos (`set`):
- No permiten elementos duplicados.  
- No garantizan un orden específico.  
- Son más rápidos que las listas para buscar elementos.  
- Admiten operaciones matemáticas como unión, intersección y diferencia.  

## 🚀 Aplicaciones prácticas:
✅ Eliminación de duplicados en listas.  
✅ Verificación rápida de pertenencia (x in conjunto).  
✅ Operaciones matemáticas en conjuntos de datos.  
✅ Comparación eficiente de listas.  

---

## Operaciones de conjuntos directamente en Python
### 1️⃣ Convertir una lista a conjunto (eliminar duplicados)
```python
lista = [1, 2, 3, 3, 4, 5, 1]
conjunto = set(lista)
print(conjunto)  # {1, 2, 3, 4, 5}
```

---

### 2️⃣ Unión de conjuntos (∪)
```python
a = set([1, 2, 3])
b = set([3, 4, 5])

union = a | b  # También puedes usar a.union(b)
print(union)  # {1, 2, 3, 4, 5}
```

---

###  3️⃣ Intersección de conjuntos (∩)
```python
interseccion = a & b  # También a.intersection(b)
print(interseccion)  # {3}
```

---

### 4️⃣ Diferencia de conjuntos (-)
```python
diferencia = a - b  # También a.difference(b)
print(diferencia)  # {1, 2}
```

---

### 5️⃣ Diferencia simétrica (⊕)
```python
diferencia_simetrica = a ^ b  # También a.symmetric_difference(b)
print(diferencia_simetrica)  # {1, 2, 4, 5}
```

---

### 6️⃣ Verificar si hay duplicados en una lista
```python
def tiene_duplicados(lista):
    return len(lista) != len(set(lista))

print(tiene_duplicados([1, 2, 3, 4]))  # False
print(tiene_duplicados([1, 2, 3, 3]))  # True
```
---

### 7️⃣ Agregar elementos a un conjunto
```python
conjunto = {1, 2, 3}
conjunto.add(4)  # Agregar un solo elemento
conjunto.update([5, 6, 7])  # Agregar varios elementos
print(conjunto)  # {1, 2, 3, 4, 5, 6, 7}
```

---

### 8️⃣ Convertir un conjunto a lista
```python
lista_sin_duplicados = list(set([1, 2, 3, 3, 4, 5, 1]))
print(lista_sin_duplicados)  # [1, 2, 3, 4, 5]
```

---

## Usar Listas (list) para interactuar con Conjuntos (set)
### ✅ Ventajas:  
- Es fácil convertir una lista a un conjunto con  **`set(lista)`**, eliminando duplicados rápidamente.
- Puedes realizar operaciones de conjuntos como **`union()`**, **`intersection()`**, etc., de manera sencilla.
- Es útil cuando los datos ya están en forma de listas y necesitas filtrarlos.

### ❌ Desventajas:
- Las listas tienen búsqueda O(n) (comparado con O(1) en **`set`**).
- No permiten acceso rápido a elementos únicos.

---

### Ejemplo: Convertir una lista en conjunto y eliminar duplicados
```python
numeros = [1, 2, 3, 3, 4, 5, 1]
conjunto = set(numeros)
print(conjunto)  # {1, 2, 3, 4, 5}
```

---

## Usar Diccionarios (dict) para trabajar con Conjuntos (set)
Python implementa los diccionarios internamente como tablas hash, lo que permite acceso rápido a claves únicas.

---

### ✅ Ventajas:  
- Los diccionarios tienen búsqueda y acceso O(1) (como los conjuntos).
- Puedes usar un **`dict`** para contar la frecuencia de elementos, algo que un **`set`** no permite.
- Son útiles cuando necesitas almacenar valores adicionales además de la existencia de un elemento.

---

### ❌ Desventajas:
- Ocupan más memoria porque almacenan pares clave-valor.
- Para operaciones clásicas de conjuntos (unión, intersección, etc.), un **`set`** es más directo.

---

### Ejemplo: Usar un diccionario para contar elementos
```python
from collections import Counter

numeros = [1, 2, 3, 3, 4, 5, 1]
conteo = Counter(numeros)
print(conteo)  # {1: 2, 2: 1, 3: 2, 4: 1, 5: 1}
```
📌 Esto nos dice cuántas veces aparece cada número.

---

## Comparativo de sasos de uso de set y dict

| **Operación**                          | **Usar `set`** ✅ | **Usar `dict`** ✅ |
|-----------------------------------------|------------------|------------------|
| **Eliminar duplicados**                 | ✅ Sí            | ❌ No es ideal   |
| **Búsqueda rápida (`O(1)`)**            | ✅ Sí            | ✅ Sí            |
| **Contar elementos (frecuencia)**       | ❌ No            | ✅ Sí            |
| **Operaciones de conjuntos (∪, ∩, -)**  | ✅ Sí            | ❌ No es eficiente |
| **Almacenar datos extra (clave-valor)** | ❌ No            | ✅ Sí            |

### 🚀 Conclusión:
- Si solo necesitas elementos únicos y operaciones de conjuntos, usa `set`.  
- Si necesitas **asociar valores a los elementos (como contar frecuencia)**, usa `dict`. 
- Ambas estructuras son eficientes, pero para conjuntos puros, `set` es la opción más natural.

---

## 📋 Operaciones Comunes Usando Conjuntos en Listas
Usar `set` para filtrar listas hace que las búsquedas sean **O(1)** en lugar de **O(n)**, lo que acelera el código en listas grandes. Aquí están los casos comunes y sus implicaciones:

---

| **Operación**                                      | **Método**                         | **Ejemplo**                                     |
|----------------------------------------------------|-------------------------------------|------------------------------------------------|
| **Filtrar elementos que están en otra lista**      | `intersection`                     | `[x for x in lista if x in set(permitidos)]`   |
| **Filtrar elementos que no están en otra lista**   | `difference`                       | `[x for x in lista if x not in set(prohibidos)]` |
| **Encontrar elementos únicos entre dos listas**    | `symmetric_difference`             | `list(set(lista1) ^ set(lista2))`              |
| **Encontrar elementos en común entre dos listas**  | `intersection`                     | `list(set(lista1) & set(lista2))`              |
| **Eliminar duplicados manteniendo el orden**       | `set()` con list comprehension      | `eliminar_duplicados(lista)`                   |

¡Implementar estos trucos con conjuntos hará que tu código sea más rápido y eficiente! 🚀🔥

---

### 📌 Notas
1. **Uso de `set`**: 
   - Ideal para operaciones rápidas, ya que las búsquedas en un conjunto son **O(1)** en promedio.
   - Más eficiente para búsquedas en listas grandes.
   - Sin embargo, el uso de `set` no garantiza mantener el orden de los elementos.

2. **Mantener el orden**: 
   - Si necesitas preservar el orden original, combina conjuntos con list comprehensions.
   - Útiles cuando el orden original es importante.
   - Más lentas para listas grandes debido a las búsquedas lineales (**O(n)**).

Selecciona el método según la operación que necesites realizar. 🚀

---

## 📚 Recursos Adicionales  
📖 [Tutorial de Python sobre conjuntos y teoría de conjuntos](https://www.datacamp.com/es/tutorial/sets-in-python)  
📖 [Conjuntos en Python (Sets)](https://medium.com/@diego.coder/conjuntos-en-python-sets-4355f7ee703a)  
📖 [Métodos de los conjuntos](https://docs.hektorprofe.net/python/metodos-de-las-colecciones/metodos-de-los-conjuntos/)   
📖 [Conjuntos en Python: El tipo set y operaciones más comunes](https://j2logo.com/python/tutorial/tipo-set-python/)  

---

## 🚀 Propuesta de crecimineto del repo
```
/Sets (set)  
│
├── README.md                # Guía general sobre el uso de conjuntos, explicación del subdirectorio
├── operations.md            # Detalles sobre operaciones básicas y avanzadas de conjuntos
├── patterns_and_techniques.md  # Patrones y técnicas comunes con conjuntos en LeetCode
├── examples/                # Ejemplos prácticos de código
│   ├── basic_operations.py   # Código de operaciones básicas (add, remove, in, etc.)
│   ├── advanced_operations.py # Código de operaciones avanzadas (unión, intersección, etc.)
│   └── problem_examples.py   # Ejemplos de problemas de LeetCode resueltos con conjuntos
├── problems/                # Problemas resueltos en LeetCode que usan conjuntos
│   ├── intersection_of_two_arrays.py
│   ├── contains_duplicate.py
│   ├── subset.py
│   └── set_matrix_zeroes.py
├── time_complexity.md       # Análisis de la complejidad temporal de las operaciones de conjuntos
├── references/              # Recursos adicionales, documentación y enlaces útiles
│   ├── python_set_docs.md   # Documentación oficial sobre sets en Python
│   └── external_resources.md  # Enlaces a tutoriales y artículos adicionales
└── quick_reference.md       # Resumen rápido de operaciones y complejidades
```

---