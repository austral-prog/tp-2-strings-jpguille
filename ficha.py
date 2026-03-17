def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    
    nombre_completo = input("Nombre completo: ").strip().title()

    mail = input("Email: ").strip().lower()
    nota_uno = input("Ingrese su nota 1: ")
    nota_dos = input("Ingrese su nota 2: ")
    nota_tres = input("Ingrese su nota 3: ")

    decoracion = "========================"
    print(decoracion)
    print("    FICHA DEL ALUMNO")
    print(decoracion)

    print(f"Nombre: {nombre_completo}")
    print(f"Email: {mail}")
    print(f"Caracteres en nombre: {len(nombre_completo)}")

    segunda_inicial = nombre_completo.find(' ') + 1
    print(f"Iniciales: {nombre_completo[0]}{nombre_completo[segunda_inicial]}")

    fin_nombre = nombre_completo.find(' ')
    inicio_apellido = fin_nombre + 1
    print(f"Usuario: {nombre_completo[inicio_apellido:].lower()}.{nombre_completo[:fin_nombre].lower()}")
    print(f"Email valido: {'@' in mail}")

    inicio_dominio = mail.find('@') + 1
    print(f"Dominio: {mail[inicio_dominio:]}")

    print(f"Nombre para archivo: {nombre_completo.replace(' ', '_')}")
    print(f"Cantidad de a: {nombre_completo.count('a')}")
    print(f"Codigo secreto: {nombre_completo[::-1].upper()}")

    print(f"Nota 1: {nota_uno}")
    print(f"Nota 2: {nota_dos}")
    print(f"Nota 3: {nota_tres}")

    suma = int(nota_uno) + int(nota_dos) + int(nota_tres)
    print(f"Suma: {suma}")

    promedio = (suma) / 3
    print(f"Promedio: {promedio}")

    promedio_entero = suma // 3
    print(f"Promedio entero: {promedio_entero}")
    print(decoracion)
