def obtener_nota(nombre):
    """
    Solicita al usuario la nota para una actividad y verifica que esté en el rango válido.
    :param nombre: Nombre de la actividad para la que se solicita la nota.
    :return: Nota válida ingresada por el usuario.
    """
    while True:
        try:
            nota = float(input(f"Ingrese la nota para {nombre} (de 1.0 a 5.0): "))
            if 1.0 <= nota <= 5.0:
                return nota
            else:
                print("La nota debe estar entre 1.0 y 5.0. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")


def calcular_nota_final():
    """
    Calcula la nota final del curso considerando los pesos de cada actividad y muestra el resultado.
    """
    # Pesos de cada actividad
    pesos = {
        'Taller 1': 0.20,
        'Taller 2': 0.15,
        'Cuestionario 1': 0.22,
        'Cuestionario 2': 0.10,
        'Proyecto final': 0.33
    }

    # Lectura de notas
    notas = {}
    for actividad in pesos:
        notas[actividad] = obtener_nota(actividad)

    # Cálculo de la nota final
    nota_final = sum(notas[actividad] * pesos[actividad] for actividad in pesos)

    # Imprimir la nota final redondeada a dos decimales
    print(f"La nota final calculada es: {nota_final:.2f}")


if __name__ == "__main__":
    calcular_nota_final()










