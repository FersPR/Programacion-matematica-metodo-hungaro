from munkres import Munkres
from tabulate import tabulate

def aplicar_metodo_hungaro_sin_interfaz():
    # Solicitar la unidad a utilizar
    unidad_filas = input("Ingrese la unidad para las filas (ej. camiones): ")
    unidad_columnas = input("Ingrese la unidad para las columnas (ej. conductores): ")
    unidad_costo = input("Ingrese la unidad para el costo (ej. dolar): ")
    
    # Solicitar dimensiones de la matriz
    filas = int(input(f"Ingrese el número de {unidad_filas}: "))
    columnas = int(input(f"Ingrese el número de {unidad_columnas}: "))

    # Inicializar la matriz de costos
    cost_matrix = []
    for i in range(filas):
        fila = list(map(int, input(f"Ingrese los costos de la {unidad_filas} {chr(i + 65)} para cada {unidad_columnas} (separados por espacio): ").split()))
        cost_matrix.append(fila)

    # Balancear la matriz si es necesario
    if filas != columnas:
        # Agregar filas o columnas con ceros para balancear
        while len(cost_matrix) < columnas:
            cost_matrix.append([0] * columnas)
        while len(cost_matrix[0]) < filas:
            for row in cost_matrix:
                row.append(0)

    m = Munkres()
    matriz_original = [fila[:] for fila in cost_matrix]  # Guardar la matriz inicial

    print("Matriz inicial de costos:")
    print(tabulate(matriz_original, headers=[f"C{i}" for i in range(len(matriz_original[0]))], tablefmt="grid"))
    print()

    # Restar el valor mínimo de cada fila
    for row in cost_matrix:
        min_val = min(row)
        for j in range(len(row)):
            row[j] -= min_val

    print("Matriz después de restar el mínimo de cada fila:")
    print(tabulate(cost_matrix, headers=[f"C{i}" for i in range(len(cost_matrix[0]))], tablefmt="grid"))
    print()

    # Restar el valor mínimo de cada columna
    for j in range(len(cost_matrix[0])):
        col = [cost_matrix[i][j] for i in range(len(cost_matrix))]
        min_val = min(col)
        for i in range(len(cost_matrix)):
            cost_matrix[i][j] -= min_val

    print("Matriz después de restar el mínimo de cada columna:")
    print(tabulate(cost_matrix, headers=[f"C{i}" for i in range(len(cost_matrix[0]))], tablefmt="grid"))
    print()

    # Realizar asignación óptima
    asignacion = m.compute(cost_matrix)
    asignacion_optima = []
    costo_total = 0

    for row, col in asignacion:
        costo = matriz_original[row][col]
        asignacion_optima.append((row + 1, col + 1, costo))  # Guardar también el costo (1-indexed)
        costo_total += costo

    # Imprimir matriz restaurada al estado inicial
    print("\nMatriz restaurada al estado inicial:")
    print(tabulate(matriz_original, headers=[f"C{i}" for i in range(len(cost_matrix[0]))], tablefmt="grid"))
    print()

    # Crear tabla de resultados
    headers = [unidad_columnas.capitalize(), unidad_filas.capitalize(), "Costo"]
    table = [(col, row, costo) for row, col, costo in asignacion_optima]

    print("\nAsignación óptima final:", asignacion_optima)
    print(tabulate(table, headers=headers, tablefmt="grid"))

    print("Costo total:", costo_total, unidad_costo)
    print()

    return asignacion_optima, costo_total











