def saludar(nombre):
    print(f"Hola, {nombre}! Bienvenido/a a la clase de Python.")
personas_ingresan = int(input("¿Cuántas personas ingresan a la clase? "))
lista_personas = []
for i in range(personas_ingresan):
    nombre = input("Ingrese el nombre de la persona: ")
    lista_personas.append(nombre)
for nombre in lista_personas:
    saludar(nombre)