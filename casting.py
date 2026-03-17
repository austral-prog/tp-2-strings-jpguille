def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    
    precio = int(input("Ingresar precio: "))
    descuento = float(input("Ingresar descuento: "))
    precio_descuento = float(precio - descuento)
    cantidad = float(input("Ingresar cantidad: "))
    total = precio_descuento * cantidad

    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio_descuento}")
    print(f"Total: {total}")
