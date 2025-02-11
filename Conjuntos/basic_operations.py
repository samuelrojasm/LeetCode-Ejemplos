
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

    # Devuelve True si dos conjuntos son disjuntos.
    print("Disjuntos:")
    print(a.isdisjoint(b))

    # Adicinar solo un elemento
    a.add(6)
    print(a)

    # Agregar varios elementos
    a.update([7, 8, 9])
    print(a)

    # Remover elemento
    a.remove(6)
    a.discard(6)
    print(a)

if __name__ == "__main__":
    main()
