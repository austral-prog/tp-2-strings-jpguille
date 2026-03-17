def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    base = int(input("Ingrese valor de base: "))
    print (f"Base: {base}")

    altura = int(input("ingrese valor de altura"))
    print(f"Altura: {altura}")

    area = base * altura
    perimetro = (base * 2) + (altura *2)

    print(f"Area: {area}")
    print(f"Perimetro: {perimetro}")

