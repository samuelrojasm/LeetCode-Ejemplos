"""
Usar conjuntos (set) para filtrar listas en Python
es una excelente manera de mejorar la eficiencia,
ya que las búsquedas en set tienen una complejidad de O(1)
en promedio, mientras que las listas (list) tienen O(n).
"""

class FiltrarListas:
    def __init__(self, elementos:list=None):
        """
        Inicializa el conjunto a partir de una lista de elementos.
        """
        self.set_data = set(elementos) if elementos else set()

    def filtrar_permitidos(self, lista:list, permitidos:list, mantener_orden=False):
        """
        Filtrar solo los elementos que están en otro conjunto (intersección)
        Si queremos obtener solo los elementos de una lista que están en otra, 
        en lugar de usar un for con if x in lista, usamos conjuntos
        """
        # Convertimos la lista de permitidos a conjunto para una búsqueda más eficiente
        permitido_set = set(permitidos)
        # Filtramos
        if mantener_orden:
            # Filtramos la lista manteniendo el orden original
            # usando lista por comprensión
            return [x for x in lista if x in permitido_set]
        else:
            # Usamos intersección directa, no mantiene el orden
            return list(permitido_set & set(lista))
 
    def filtrar_no_permitidos(self, lista:list, no_permitidos,mantener_orden=False):
        """
        Filtrar elementos que NO están en otro conjunto (diferencia)
        Si queremos remover elementos de una lista que están 
        en otra, podemos usar la diferencia de conjuntos.
        Usos:
            Eliminar palabras prohibidas en procesamiento de texto.
            Filtrar usuarios bloqueados en una aplicación.
        """
         # Convertimos la lista de no permitidos a conjunto para una búsqueda más eficiente
        no_permitidos_set = set(no_permitidos)
         # Filtramos
        if mantener_orden:
            return [x for x in lista if x not in no_permitidos_set]
        else:
            # Usamos diferencia directa, no mantiene el orden
            return list(set(lista) - no_permitidos_set)
    
    def elementos_unicos(self, lista1:list, lista2:list):
        """
        Encontrar elementos únicos entre dos listas.
        Si queremos encontrar los elementos que solo 
        están en una de las dos listas, podemos usar
        la diferencia simétrica.
        Usos:
            Comparar diferencias entre dos datasets.
            Encontrar nuevos elementos agregados o eliminados.
        """
         # Operador XOR (^)
        return list(set(lista1) ^ set(lista2))
        
    def elementos_comunes(self, lista1:list, lista2:list):
        """
        Obtener solo los elementos comunes en dos listas
        Si queremos solo los elementos que están en ambas listas,
        usamos la intersección.
        Usos:
            Encontrar clientes en común entre dos bases de datos.
            Determinar elementos compartidos en múltiples listas
        """
        return list(set(lista1) & set(lista2))
    
    def eliminar_duplicados(self, lista:list):
        """
        Eliminar duplicados manteniendo el orden.
        Si queremos eliminar duplicados pero manteniendo el orden original, 
        no podemos usar set(lista), porque un conjunto no mantiene el orden.
        """
        seen = set()
        return [x for x in lista if not (x in seen or seen.add(x))]
    
    def filtrar_multiplos_conjuntos_ordenados(self,lista:list, divisor:int):
        """
        Filtra los elementos de una lista que son múltiplos de un divisor dado
        utilizando conjuntos para eficiencia y manteniendo el orden.

        Args:
            lista (list): Lista de números a filtrar.
            divisor (int): Número para determinar los múltiplos.

        Returns:
            list: Lista ordenada de números que son múltiplos del divisor.
        """
        if divisor == 0:
            raise ValueError("El divisor no puede ser cero.")
        
         # Crear conjunto para búsquedas rápidas
        multiplos_set = {n for n in lista if n % divisor == 0}
        # Usar el conjunto para filtrar manteniendo el orden
        return [n for n in lista if n in multiplos_set]

def main():
    #Filtrar por permitidos
    datos = [1, 2, 3, 4, 5, 6, 7, 8]
    permitidos = [2, 4, 6, 8]
    filtros = FiltrarListas()
    print("Filtro por permitidos:")
    print(filtros.filtrar_permitidos(datos, permitidos))

    #Filtrar por NO permitidos
    prohibidos = [2, 4, 6, 8]
    print("Filtro por NO permitidos:")
    print(filtros.filtrar_no_permitidos(datos,  prohibidos))

    # Encontrar elementos únicos entre dos listas
    lista_a = [1, 2, 3, 4]
    lista_b = [3, 4, 5, 6]
    print("Elementos unicos:")
    print(filtros.elementos_unicos(lista_a,  lista_b))

    # Obtener solo los elementos comunes en dos listas
    lista_a = [1, 2, 3, 4]
    lista_b = [3, 4, 5, 6]
    print("Elementos comunes:")
    print(filtros.elementos_comunes(lista_a,  lista_b))

    # Eliminar duplicados manteniendo el orden
    lista = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
    print("Eliminar duplicados:")
    print(filtros.eliminar_duplicados(lista))  # [1, 2, 3, 4, 5, 6, 7]

    # Filtra los elementos de una lista que son múltiplos de un divisor dado
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    resultado = filtros.filtrar_multiplos_conjuntos_ordenados(numeros, 3)
    print("Múltiplos de un divisor dado:")
    print(resultado)  # [3, 6, 9] (el orden se conserva)

if __name__ == "__main__":
        main()