import numpy as np
import matplotlib.pyplot as plt
import csv

def resolver_sistema():
    print("Resolviendo un sistema de ecuaciones lineales...")
    # Definir una matriz de coeficientes y un vector de términos independientes
    A = np.array([[3, 1, -1], [2, 4, 1], [-1, 2, 5]])
    b = np.array([4, 1, 1])
    # Resolver el sistema Ax = b
    try:
        x = np.linalg.solve(A, b)
        print("Solución del sistema:")
        for i, valor in enumerate(x, start=1):
            print(f"x{i} = {valor:.4f}")
        return x
    except np.linalg.LinAlgError:
        print("No se puede resolver el sistema, puede que no tenga solución.")
        return None

def graficar_soluciones(soluciones):
    if soluciones is not None:
        plt.plot(soluciones, 'o')
        plt.title("Soluciones del sistema")
        plt.xlabel("Índice de la variable")
        plt.ylabel("Valor de la solución")
        # Guardar el gráfico como imagen
        plt.savefig("soluciones.png")
        plt.close()
        print("Gráfico guardado como 'soluciones.png'")
    else:
        print("No se puede generar el gráfico debido a la falta de soluciones.")

def guardar_resultados_csv(soluciones):
    if soluciones is not None:
        print("Guardando resultados en un archivo CSV...")
        # Escribir las soluciones en un archivo CSV
        with open("resultados.csv", mode="w", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["Variable", "Valor"])
            for i, valor in enumerate(soluciones, start=1):
                escritor.writerow([f"x{i}", f"{valor:.4f}"])
        print("Resultados guardados en 'resultados.csv'")
    else:
        print("No se pueden guardar los resultados debido a la falta de soluciones.")

def main():
    print("=== Sistema de Ecuaciones Lineales ===")
    # Resolver el sistema
    soluciones = resolver_sistema()
    # Graficar las soluciones
    graficar_soluciones(soluciones)
    # Guardar los resultados en un archivo CSV
    guardar_resultados_csv(soluciones)

if __name__ == "__main__":
    main()