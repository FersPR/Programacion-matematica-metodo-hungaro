""" obtiene los datos por teclado """
def obtnrTabla():

    # Solicitar dimensiones de la matriz
    filas = int(input(f"Ingrese el número de filas: "))
    columnas = int(input(f"Ingrese el número de columnas: "))

    # Inicializar la matriz de costos
    cost_matrix = []
    for i in range(filas):
        fila = list(map(int, input(f"Ingrese los costos de la fila {chr(i + 65)} para cada columna (separados por espacio): ").split()))
        cost_matrix.append(fila)

    # Balancear la matriz si es necesario
    if filas != columnas:
        # Agregar filas o columnas con ceros para balancear
        while len(cost_matrix) < columnas:
            cost_matrix.append([0] * columnas)
        while len(cost_matrix[0]) < filas:
            for row in cost_matrix:
                row.append(0)


    return cost_matrix 




