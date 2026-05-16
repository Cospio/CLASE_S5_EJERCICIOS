while True:
    print("Bienvenido al sistema de compras")
    print("1. Entrar")
    print("2. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        print("Entrando al sistema de compras...")
    elif opcion == "2":
        print("Saliendo del sistema de compras...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")