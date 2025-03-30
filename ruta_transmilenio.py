# Diccionario de estaciones y sus conexiones (rutas disponibles)
conexiones = {
    "Portal 80": ["Humedal Córdoba", "Prado"],
    "Humedal Córdoba": ["Portal 80", "Prado", "Terminal"],
    "Prado": ["Portal 80", "Humedal Córdoba", "Terminal", "Calle 76"],
    "Terminal": ["Humedal Córdoba", "Prado", "Calle 76", "Marly"],
    "Calle 76": ["Prado", "Terminal", "Marly"],
    "Marly": ["Terminal", "Calle 76", "Av. Jiménez"],
    "Av. Jiménez": ["Marly", "Universidades"]
}

# Reglas de tiempo aproximado entre estaciones (en minutos)
tiempos = {
    ("Portal 80", "Humedal Córdoba"): 5,
    ("Portal 80", "Prado"): 7,
    ("Humedal Córdoba", "Terminal"): 10,
    ("Prado", "Terminal"): 15,
    ("Terminal", "Calle 76"): 20,
    ("Calle 76", "Marly"): 25,
    ("Marly", "Av. Jiménez"): 30,
    ("Av. Jiménez", "Universidades"): 45
    
}
from collections import deque  # Importa una cola eficiente para el algoritmo

def encontrar_ruta(conexiones, inicio, fin):
    # Inicializa una cola con la estación inicial y la ruta que solo la contiene
    cola = deque()
    cola.append((inicio, [inicio]))  
    visitadas = set()  # Conjunto para evitar revisitar estaciones

    while cola:  # Mientras haya nodos por procesar
        estacion, ruta = cola.popleft()  # Extrae el primer elemento de la cola

        if estacion == fin:  # Si llegamos al destino
            return ruta  # Retorna la ruta encontrada

        for vecino in conexiones[estacion]:  # Explora estaciones conectadas
            if vecino not in visitadas:  # Si no se ha visitado
                visitadas.add(vecino)  # Márcalo como visitado
                cola.append((vecino, ruta + [vecino]))  # Agrega a la cola con la ruta actualizada

    return None  # Si no se encontró ruta
def main():
    print("=== Sistema de Ruta TransMilenio Bogotá ===")
    print("Estaciones disponibles:", list(conexiones.keys()))

    while True:  # Loop hasta que ingresen datos válidos
        inicio = input("\nIngresa estación de inicio: ").strip()
        fin = input("Ingresa estación de destino: ").strip()

        if inicio not in conexiones:
            print(f"Error: '{inicio}' no es una estación válida.")
        elif fin not in conexiones:
            print(f"Error: '{fin}' no es una estación válida.")
        else:
            break  # Datos correctos, sal del loop

    ruta = encontrar_ruta(conexiones, inicio, fin)

    if ruta:
        print(f"\nMejor ruta ({len(ruta)-1} transbordos):")
        print(" → ".join(ruta))
        
        # Opcional: Calcular tiempo total (si tienes datos en 'tiempos')
        tiempo_total = 0
        for i in range(len(ruta)-1):
            tramo = (ruta[i], ruta[i+1])
            tiempo_total += tiempos.get(tramo, 0)  # Usa 0 si el tramo no está en 'tiempos'
        print(f"Tiempo estimado: {tiempo_total} minutos")
    else:
        print("\nNo hay ruta disponible entre las estaciones.")

if __name__ == "__main__":
    main()