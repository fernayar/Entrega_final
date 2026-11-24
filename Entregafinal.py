import json

productos = []

try:
    with open("datos.json","r") as archivo:
        productos = json.load(archivo)

except FileNotFoundError:
    with open("datos.json","w") as archivo:
        productos = []


def actualizar():
    with open("datos.json","w") as archivo:
        json.dump(productos,archivo)

def agregar_producto():

    while True:
       prod_ = input("\nProducto: ").strip().title()

       if not prod_:
          print("El nombre del producto no puede estar vacío.")
          continue
       break


    while True:
       try:
          precio = float(input("\nPrecio: "))
          if precio < 0:
             print("El precio no puede ser negativo.")
             continue
          break
       except ValueError:
          print("Ingrese un número válido.")
       continue    

    while True:
       categoria = input("\nCategoria: ").strip().title()
       if categoria == "":
          print("La categoría no puede estar vacía.")
          continue
       break
                    
    elProducto = [prod_,precio,categoria]
    productos.append(elProducto)
    print(f"{prod_} agregado con éxito")

def buscar_producto():
    buscar = input("\nProducto a buscar: ").strip().title()

    for id, producto in enumerate(productos, start=1):
       if producto[0] == buscar:
          print(f"{id}) Producto: {producto[0]} | Precio: {producto[1]} | Categoria: {producto[2]}")
          break
    else:
       print("Producto no encontrado")

def listar_productos():
    if not productos:
        print("No hay productos para listar.")
        return
    for id, producto in enumerate(productos, start=1):
       print(f"{id}) Producto: {producto[0]} | Precio: {producto[1]} | Categoria: {producto[2]}")
    

def remover_producto():
     quitar = input("\nProducto a remover: ").strip().title()

     for producto in productos:
       if producto[0] == quitar:
          productos.remove(producto)
          print(f"{quitar} removido con éxito")
          break
     else:
        print(f"{quitar} no encontrado")

while True:
    opciones = input("\n*** Menu principal ***\n\nA - Agregar\nB - Buscar\nL - Listar\nR - Remover\nS - Salir\n\n").strip().title()
    
    match opciones:

        case "A":
            agregar_producto()
                        
            actualizar()
                       
        case "B":
            buscar_producto()
                       
        case "L":
            listar_productos()

        case "R":
            remover_producto()

            actualizar()

        case "S":
            print("\nSaliendo del programa...")
            break

        case _:
            print("\nOpción inválida. Intente nuevamente.")
