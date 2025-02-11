# 🌲 Trees vs. Graphs 🕸️
Tanto los árboles (*trees*) como los gráficos (*graphs*) son estructuras de datos fundamentales en informática y aparecen frecuentemente en problemas de LeetCode. Aunque están relacionados, tienen diferencias clave en su estructura y en cómo se utilizan.

---

## 1️⃣ Definiciones
### **Graph (Grafo)**
Un **grafo** es una colección de **nodos (vértices)** conectados por **aristas (edges)**. Puede ser dirigido o no dirigido y puede contener ciclos.

- **Vértices (nodes)**: Representan entidades o puntos de datos.
- **Aristas (edges)**: Representan conexiones entre los vértices.

Tipos de grafos:
- **Dirigidos**: Las aristas tienen una dirección específica.
- **No dirigidos**: Las aristas no tienen dirección.
- **Pesados**: Cada arista tiene un peso o costo asociado.
- **Cíclicos / Acíclicos**: Un grafo es cíclico si contiene ciclos, de lo contrario, es acíclico.

Ejemplo de grafo no dirigido:

```plaintext
    A --- B
    |     |
    C --- D
```

### **Tree (Árbol)**
Un **árbol** es un caso especial de grafo que cumple ciertas reglas:
- Es un **grafo acíclico y conectado**.
- Tiene un **nodo raíz** desde donde comienza la estructura.
- Cada nodo (excepto la raíz) tiene exactamente **un único padre**.
- Posee **N nodos y N-1 aristas**.

Ejemplo de árbol binario:

```plaintext
      1
     / \
    2   3
   / \
  4   5
```

---

## 2️⃣ Diferencias Clave entre Árboles y Grafos

| Característica    | Árbol | Grafo |
|------------------|-------|-------|
| Estructura       | Conectado y acíclico | Puede ser cíclico o acíclico |
| Conectividad     | Siempre conectado | Puede ser conectado o desconectado |
| Relación Padre-Hijo | Sí (excepto en grafos generales) | No siempre |
| Número de aristas | Exactamente N-1 | Varía según el tipo |
| Dirección        | Generalmente dirigido (raíz a hojas) | Puede ser dirigido o no dirigido |

---

## 3️⃣ Uso en Problemas de LeetCode
- **Árboles**: Se utilizan en problemas de búsqueda binaria (BST), recorrido DFS/BFS, árboles de segmentación, etc.
- **Grafos**: Aparecen en problemas de rutas, redes, análisis de conexiones, caminos mínimos (Dijkstra, Floyd-Warshall), etc.

---

## 4️⃣ Algoritmos Comunes

### **Para Árboles**
- DFS (Inorder, Preorder, Postorder)
- BFS (Nivel por nivel)
- Lowest Common Ancestor (LCA)
- Construcción y transformación de árboles

### **Para Grafos**
- BFS / DFS para búsqueda de caminos
- Algoritmos de caminos mínimos (Dijkstra, Bellman-Ford)
- Algoritmos de detección de ciclos
- Algoritmos de conectividad (Union-Find, Kruskal, Prim)

---

## 5️⃣ Conclusión
Mientras que **todos los árboles son grafos, no todos los grafos son árboles**. La elección de la estructura de datos correcta depende del problema específico. Los árboles ofrecen una estructura jerárquica clara, mientras que los grafos permiten representar relaciones más complejas.