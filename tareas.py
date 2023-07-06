class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self):
        tarea = input("Ingrese una nueva tarea: ")
        self.tareas.append(tarea)
        print("Tarea agregada.")

    def eliminar_tarea(self):
        tarea = input("Ingrese la tarea que desea eliminar: ")
        if tarea in self.tareas:
            self.tareas.remove(tarea)
            print("Tarea eliminada.")
        else:
            print("La tarea no existe.")

    def marcar_completada(self):
        tarea = input("Ingrese la tarea completada: ")
        if tarea in self.tareas:
            print("¡Felicidades por completar la tarea!")
            self.tareas.remove(tarea)
        else:
            print("La tarea no existe.")

    def mostrar_tareas(self):
        print("Lista de tareas:")
        for i, tarea in enumerate(self.tareas, 1):
            print(f"{i}. {tarea}")

    def menu(self):
        while True:
            print("\n--- Gestión de Tareas ---")
            print("1. Agregar tarea")
            print("2. Eliminar tarea")
            print("3. Marcar tarea como completada")
            print("4. Mostrar tareas")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_tarea()
            elif opcion == "2":
                self.eliminar_tarea()
            elif opcion == "3":
                self.marcar_completada()
            elif opcion == "4":
                self.mostrar_tareas()
            elif opcion == "5":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Intente nuevamente.")


lista_tareas = ListaTareas()
lista_tareas.menu()
