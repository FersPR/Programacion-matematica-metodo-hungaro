from metodo_hungaro import aplicar_metodo_hungaro_sin_interfaz  # Importa la función modificada
from resolucion import main as resolver_sin_munkres  # Importa la función main de resolucion.py

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Resolver con Munkres")
    print("2. Resolver sin Munkres")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese su opción (1, 2 o 3): ")

        if opcion == '1':
            # Lógica para resolver con Munkres
            print("Resolviendo con Munkres...")
            aplicar_metodo_hungaro_sin_interfaz()  # Llama a la función sin interfaz

        elif opcion == '2':
            # Lógica para resolver sin Munkres
            print("Resolviendo sin Munkres...")
            resolver_sin_munkres()  # Llama a la función main de resolucion.py

        elif opcion == '3':
            print("Saliendo del programa...")
            break  # Sale del bucle y termina el programa

        else:
            print("Opción no válida. Intente de nuevo.")

def ingresar_matriz():
    # Implementa aquí la lógica para ingresar la matriz
    filas = int(input("Ingrese el número de filas (empresas): "))
    columnas = int(input("Ingrese el número de columnas (centrales): "))
    
    matriz = []
    for i in range(filas):
        fila = list(map(int, input(f"Ingrese los costos de la empresa {chr(i + 65)} para cada central (separados por espacio): ").split()))
        matriz.append(fila)
    
    return matriz

if __name__ == "__main__":
    main()