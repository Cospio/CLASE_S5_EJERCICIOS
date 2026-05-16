def saludar(nombre):
    print(f"Hola, {nombre}! Bienvenido/a a la clase de Python.")
personas_ingresan = int(input("¿Cuántas personas ingresan a la clase? "))
lista_personas = []
for i in range(personas_ingresan):
    nombre = input("Ingrese el nombre de la persona: ")
    lista_personas.append(nombre)
for nombre in lista_personas:
    saludar(nombre)
    
#Una funcion que se llame mensaje, que reciba un mensaje y lo imprima en pantalla
def Mensaje(mensaje):
    print(mensaje)
texto = input("Ingrese un mensaje: ")
Mensaje(texto)


#Una funcion que se llame despedida, que reciba un mensaje y lo imprima en pantalla
def despedida():
    nombre = input("Ingrese su nombre: ")
    print(f"¡Adiós, {nombre}! ¡Que tengas un excelente día!")
despedida()


#Una funcion que se llame sumatoria, que reciba dos numeros y devuelva la suma de ambos
def suma(a, b):
    return a + b
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
resultado = suma(a, b)
print(f"La suma de {a} y {b} es: {resultado}")

