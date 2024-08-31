#Mostrar lista de producto de la empresa poder comprar el producto

inventario = {
    'locion hombre': {'cantidad': 15, 'precio': 3500},
    'locion mujer': {'cantidad': 10, 'precio': 2500},
    'prueba': {'cantidad': 12, 'precio': 1000}
}
validar=True
while validar:
    print("Opciones:")
    print("1. Mostrar todos los productos")
    print("2. Comprar un producto")
    print("3. Salir")
    
    opcion = input("Seleccione una opción (1-3): ")
    
    if opcion == '1':
        print("Inventario de la tienda:")
        for producto, info in inventario.items():
            print(f"{producto.capitalize()}: {info['cantidad']} disponibles, Precio: ${info['precio']} cada uno")
    
    elif opcion == '2':
        producto = input("Ingrese el nombre del producto que desea comprar: ").lower()
        cantidad = int(input("Ingrese la cantidad que desea comprar: "))
        
        if producto in inventario and cantidad <= inventario[producto]['cantidad']:
            costo_total = cantidad * inventario[producto]['precio']
            inventario[producto]['cantidad'] -= cantidad
            print(f"Compra realizada. El costo total es: ${costo_total}")
        else:
            print("Lo siento, no hay suficiente cantidad disponible o el producto no existe.")
        continuar = input("¿Desea comprar otro producto? (si o no): ").lower()
        if continuar != 'si':
            print("Gracias por usar el sistema de inventario. ¡Adiós!")
            validar= False
    else:
        print("Opción no válida. Por favor, elija una opción entre 1 y 3.")