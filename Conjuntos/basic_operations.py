class ConjuntoExtra:
    def __init__(self, elementos:list=None):
        """
        Inicializa el conjunto a partir de una lista de elementos.
        """
        self.set_data = set(elementos) if elementos else set()
    
    def tiene_duplicados(self, lista:list):
        """Verifica si una lista contiene duplicados."""
        return len(lista) != len(set(lista))
    
    def elementos_comunes(self, *listas):
        """Encuentra los elementos en común en múltiples listas."""
        conjuntos = [set(lista) for lista in listas]
        return list(set.intersection(*conjuntos))
    
    def simetrica_entre_listas(self, *listas):
        """
        Diferencia simétrica entre varios conjuntos
        Da los elementos que aparecen un número impar de veces.
        Selecciona elementos basándose en su frecuencia (impar o par).
        """
        resultado = set()
        for lista in listas:
            # Aplica symmetric_difference de forma acumulativa
            resultado ^= set(lista)
            print("resultado intermedio simetrica: ",resultado)
        return list(resultado)
    
    def elementos_faltantes(self, lista1, lista2):
        """
        Comparar dos listas (cuáles elementos faltan en una respecto a otra)
        Si queremos saber qué elementos tiene una lista que la otra no tiene
        Encuentra los elementos que están en lista2 pero no en lista1.
        """
        return list(set(lista2) - set(lista1))
    
    def unicos_entre_listas(self, *listas):
        """Encuentra los elementos que no están en todas las listas."""
        conjuntos = [set(lista) for lista in listas]
        
        # Unión de todos los conjuntos (todos los elementos presentes en al menos una lista)
        union_total = set.union(*conjuntos)
        
        # Intersección de todos los conjuntos (elementos que están en TODAS las listas)
        interseccion_total = set.intersection(*conjuntos)
        
        # Elementos que están en al menos una lista, pero no en todas
        return list(union_total - interseccion_total)
    
    def es_subconjunto(self, sublista:list, lista_grande):
        """Verifica si el conjunto actual es un subconjunto de la lista dada."""
        return set(sublista).issubset(set(lista_grande))

    def to_list(self):
        """Convierte el conjunto en una lista."""
        return list(self.set_data)

    def __str__(self):
        """Devuelve una representación en string del conjunto."""
        return f"{self.set_data}"

    def is_superset(self, elements):
        """Verifica si el conjunto actual es un superconjunto de la lista dada."""
        return self.set_data.issuperset(set(elements))

    def contiene(self, elemento):
        """Verifica si el elemento está en el conjunto."""
        return elemento in self.set_data


     
def main():
    # Usar set directamente para operaciones de conjuntos
    a = {1, 2, 3}
    b = {3, 4, 5}

    # Unión → {1, 2, 3, 4, 5}
    print(a | b)
    print(a.union(b))

    # Intersección → {3}
    print(a & b)
    print(a.intersection(b))

    # Diferencia → {1, 2}
    print(a - b)
    print(a.difference(b))

    # Diferencia simétrica → {1, 2, 4, 5}
    print(a ^ b) 
    print(a.symmetric_difference(b))

    # Adicinar solo un elemento
    a.add(6)
    print(a)

    # Agregar varios elementos
    a.update([7, 8, 9])
    print(a)

    # Remover elemento
    a.remove(6)
    print(a)

    # Crear una instancia con una lista
    conjunto = ConjuntoExtra([1, 2, 3, 4, 5, 1])
    
    # Verificar duplicados
    print(conjunto.tiene_duplicados([1, 2, 3, 3]))    # True
    print(conjunto.tiene_duplicados([1, 2, 3]))       # False

    # Convertir el conjunto a lista
    print(conjunto.to_list())  # [1, 2, 3, 4, 5]

    # Encontrar elementos comunes en múltiples listas
    print(conjunto.elementos_comunes([1, 2, 3], [2, 3, 4], [3, 4, 5]))  # [3]

    # Diferencia simétrica para dos o más conjuntos
    print("Diferencia Simetrica de varios conjuntos")
    print(conjunto.simetrica_entre_listas([1, 2, 3], [2, 3, 4], [3, 4, 5]))

    # Encontrar los elementos que no están en todas las listas
    print("Elementos que no están en todas las listas")
    print(conjunto.unicos_entre_listas([1, 2, 3], [2, 3, 4], [3, 4, 5],[6, 7, 8]))

    # Verificar si todos los elementos de una lista están dentro de otra lista
    print("Verificar si es una sublista")
    lista_grande = [1, 2, 3, 4, 5, 6]
    sublista = [2, 3, 4]
    print(conjunto.es_subconjunto(sublista, lista_grande))  # True
    print(conjunto.es_subconjunto([2, 7, 10], lista_grande))   # False  

    # Verifica si un elemento es parte de la lista
    print(conjunto.contiene(11))

if __name__ == "__main__":
    main()
