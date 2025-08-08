import os
import sys
import importlib
import traceback

from colorama import init, Fore

def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    """
    Muestra el menú CLI con un estilo moderno.
    """
    # Inicializa colorama para habilitar los códigos de color ANSI
    init(autoreset=True)

    # Estilos básicos para el menú
    title = f"{Fore.GREEN}--- Menú de Automatización ---{Fore.RESET}"
    separator = f"{Fore.WHITE}{'─' * 40}"  # Línea separadora
    options_header = f"{Fore.BLUE}Elige una opción:{Fore.RESET}"
    footer = f"{Fore.WHITE}(Usa el número correspondiente para seleccionar){Fore.RESET}"

    # Mostrar el título y la separación
    print(f"\n{title}")
    print(f"{separator}")
    print(f"\n{options_header}")

    # Mostrar los ejercicios con estilo
    for i in range(1, 11):  # Ajusta el rango según el número de ejercicios
        print(f"{Fore.CYAN}[{i}]{Fore.RESET} Ejercicio {i}")

    # Opciones finales
    print(f"{Fore.RED}[0]{Fore.RESET} Salir")
    print(f"\n{footer}")
    print(f"{separator}")




def execute_exercise(exercise_number):
    """
    Ejecuta el script del ejercicio seleccionado.
    """
    try:
        # Intentar cargar el módulo dinámicamente
        exercise_module = importlib.import_module(f"src.ejercicio_{exercise_number}")
        print(f"\nEjecutando Ejercicio {exercise_number}...")
        
        
        
    except ModuleNotFoundError:
        print(f"Error: No se encontró el módulo para el Ejercicio {exercise_number}.")
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el Ejercicio {exercise_number}: {e}")
        traceback.print_exc()

def main():
    while True:
        show_menu()
        
        # Leer la opción del usuario
        try:
            choice = int(input("Selecciona una opción: "))
        except ValueError:
            print("Opción no válida. Por favor ingresa un número.")
            continue
        
        # Ejecutar la opción seleccionada
        if choice == 0:
            print("Saliendo del programa.")
            break
        elif 1 <= choice <= 10:  # Ajusta el rango según el número de ejercicios
            execute_exercise(choice)
        else:
            print("Opción no válida. Por favor selecciona un número entre 1 y 5.")

if __name__ == "__main__":
    main()
