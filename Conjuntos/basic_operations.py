class ConjuntoExtra:
    def __init__(self, elementos:list=None):
        """
        Inicializa el conjunto a partir de una lista de elementos.
        """
        self.set_data = set(elementos) if elementos else set()
    
    def tiene_duplicados(self, lista:list):
        """Verifica si una lista contiene duplicados."""
        return len(lista) != len(set(lista))
    
    def to_list(self):
        """Convierte el conjunto en una lista."""
        return list(self.set_data)

    def __str__(self):
        """Devuelve una representación en string del conjunto."""
        return f"{self.set_data}"
     
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

    # Crear una instancia con una lista
    conjunto = ConjuntoExtra([1, 2, 3, 4, 5, 1])
    
    # Verificar duplicados
    print(conjunto.tiene_duplicadosicates([1, 2, 3, 3]))    # True
    print(conjunto.tiene_duplicados([1, 2, 3]))             # False

    # Convertir el conjunto a lista
    print(conjunto.to_list())  # [1, 2, 3, 4, 5]

if __name__ == "__main__":
    main()
