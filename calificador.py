from utilidades import Resultado, mensaje_error, helper, tarea


def inversion(uuid, deseo_ayudar):
    def decorador(f):
        def contenedora(monto_inicial, interes):
            resultados = []
            error = False
            for i in range(1, 10):
                total = 0
                for _ in range(12):
                    total += i * 1000 * (1 + interes)
                try:
                    r = f(i * 1000, interes)
                    resultados.append(Resultado((i * 1000, interes), total, r, total==r).__dict__)
                except Exception as e:
                    mensaje_error(e)
                    error = True
                    break
            helper(resultados, 'inversion', uuid, error, deseo_ayudar)
        return contenedora
    return decorador

def califica_suma(f, uuid, deseo_ayudar):
    resultados = []
    error = False
    for i in range(5):
        for j in range(-2, 2):
            try:
                resultado_suma = f(i, j)
                resultado_real = i + j
                estado = resultado_suma==resultado_real
                resultados.append(Resultado((i, j), resultado_real, resultado_suma, estado).__dict__)
            except Exception as e:
                mensaje_error(e)
                error = True
                break
        if error:
            break
    
    helper(resultados, tarea+'suma', uuid, error, deseo_ayudar)

def califica_resta(f, uuid, deseo_ayudar):
    resultados = []
    error = False
    for i in range(5):
        for j in range(-2, 2):
            try:
                resultado_resta = f(i, j)
                resultado_real = i - j
                estado = resultado_real==resultado_resta
                resultados.append(Resultado((i, j), resultado_real, resultado_resta, estado).__dict__)
            except Exception as e:
                mensaje_error(e)
                error = True
                break
        if error:
            break
    helper(resultados, tarea+'resta', uuid, error, deseo_ayudar)

def califica_saludo(f, uuid, deseo_ayudar):
    error = False
    resultados = []
    try:
        r = f()
        esperado = "Hola, mundo!"
        estado = r==esperado
        resultados.append(Resultado(None, esperado, r, estado).__dict__)
    except Exception as e:
        mensaje_error(e)
        error = True

    helper(resultados, tarea+'saludo', uuid, error=error, deseo=deseo_ayudar)

def califica_multiplicacion(f, uuid, deseo_ayudar):
    error = False
    resultados = []
    for i in range(5):
        for j in range(-2, 2):
            try:
                resultado_resta = f(i, j)
                resultado_real = i * j
                estado = resultado_real==resultado_resta
                resultados.append(Resultado((i, j), resultado_real, resultado_resta, estado).__dict__)
            except Exception as e:
                mensaje_error(e)
                error = True
                break
        if error:
            break
    helper(resultados, tarea+'multiplicacion', uuid, error, deseo_ayudar)


def califica_division(f, uuid, deseo_ayudar):
    error = False
    resultados = []
    for i in range(-2, 2):
        for j in range(1, 6):
            try:
                resultado_resta = f(i, j)
                resultado_real = i / j
                estado = resultado_real==resultado_resta
                resultados.append(Resultado((i, j), resultado_real, resultado_resta, estado).__dict__)
            except Exception as e:
                mensaje_error(e)
                error = True
                break
        if error:
            break
    helper(resultados, tarea+'division', uuid, error, deseo_ayudar)

def califica_al_cuadrado(f, uuid, deseo_ayudar):
    error = False
    resultados = []
    for j in range(1, 6):
        try:
            resultado_resta = f(j)
            resultado_real = j ** 2
            estado = resultado_real==resultado_resta
            resultados.append(Resultado((j), resultado_real, resultado_resta, estado).__dict__)
        except Exception as e:
            mensaje_error(e)
            error = True
            break
        
    helper(resultados, tarea+'al_cuadrado', uuid, error, deseo_ayudar)


def califica_potencia(f, uuid, deseo_ayudar):
    error = False
    resultados = []
    for i in range(-2, 2):
        for j in range(1, 6):
            try:
                resultado_resta = f(i, j)
                resultado_real = i ** j
                estado = resultado_real==resultado_resta
                resultados.append(Resultado((i, j), resultado_real, resultado_resta, estado).__dict__)
            except Exception as e:
                mensaje_error(e)
                error = True
                break
        if error:
            break
    helper(resultados, tarea+'potencia', uuid, error, deseo_ayudar)


def califica_suma_mas_dos(f, uuid, deseo_ayudar):
    error = False
    resultados = []
    for i in range(-2, 2):
        for j in range(1, 6):
            try:
                resultado_resta = f(i, j)
                resultado_intermedio = i + j
                resultado_real = resultado_intermedio + 2
                estado = resultado_real==resultado_resta
                resultados.append(Resultado((i, j), resultado_real, resultado_resta, estado).__dict__)
            except Exception as e:
                mensaje_error(e)
                error = True
                break
        if error:
            break
    helper(resultados, tarea+'suma_mas_dos', uuid, error, deseo_ayudar)

def califica_resta_menos_veinte(f, uuid, deseo_ayudar):
    error = False
    resultados = []
    for i in range(-2, 2):
        for j in range(1, 6):
            try:
                resultado_resta = f(i, j)
                resultado_intermedio = j - i
                resultado_real = resultado_intermedio + 20
                estado = resultado_real==resultado_resta
                resultados.append(Resultado((i, j), resultado_real, resultado_resta, estado).__dict__)
            except Exception as e:
                mensaje_error(e)
                error = True
                break
        if error:
            break
    helper(resultados, tarea+'resta_menos_veinte', uuid, error, deseo_ayudar)

def califica_en_mayusculas(f, uuid, deseo_ayudar):
    error = False
    resultados = []
    try:
        r = f("hola, mundo")
        esperado = "HOLA, MUNDO"
        estado = r==esperado
        resultados.append(Resultado(None, esperado, r, estado).__dict__)
    except Exception as e:
        mensaje_error(e)
        error = True

    helper(resultados, tarea+'en_mayusculas', uuid, error=error, deseo=deseo_ayudar)

def califica_en_minusculas(f, uuid, deseo_ayudar):
    error = False
    resultados = []
    try:
        r = f("HOLA, MUNDO")
        esperado = "hola, mundo"
        estado = r==esperado
        resultados.append(Resultado(None, esperado, r, estado).__dict__)
    except Exception as e:
        mensaje_error(e)
        error = True

    helper(resultados, tarea+'en_minusculas', uuid, error=error, deseo=deseo_ayudar)

def califica_primer_letra(f, uuid, deseo_ayudar):
    error = False
    resultados = []
    palabras = [
        "Hola",
        "mundo",
        "me",
        "gusta",
        "este",
        "curso",
        "y las",
        "tareas",
        "están",
        "geniales"
    ]
    try:
        for palabra in palabras:
            letra_obtenida = f(palabra)
            letra_esperada = palabra[0]
            estado = letra_obtenida == letra_esperada
            resultados.append(Resultado(palabra, letra_esperada, letra_obtenida, estado).__dict__)
    except Exception as e:
        mensaje_error(e)
        error = True
    
    helper(resultados, tarea+'primer_letra', uuid, error=error, deseo=deseo_ayudar)

def califica_penultima_letra(f, uuid, deseo_ayudar):
    error = False
    resultados = []
    palabras = [
        "Esta",
        "tarea",
        "está",
        "curiosa",
        "eso de",
        "usar",
        "índices",
        "negativos",
        "es",
        "nuevo"
    ]
    try:
        for palabra in palabras:
            letra_obtenida = f(palabra)
            letra_esperada = palabra[-2]
            estado = letra_obtenida == letra_esperada
            resultados.append(Resultado(palabra, letra_esperada, letra_obtenida, estado).__dict__)
    except Exception as e:
        mensaje_error(e)
        error = True
    
    helper(resultados, tarea+'penultima_letra', uuid, error=error, deseo=deseo_ayudar)


def califica_mostrar_numeros(f, uuid, deseo_ayudar):
    error = False
    resultados = []
    numeros = [
        (1,2,3),
        (4,5,6),
        (7,8,9),
        (10, 11, 12),
        (13, 14, 15)
    ]
    try:
        for tupla in numeros:
            resultado_obtenido = f(tupla[0], tupla[1], tupla[2])
            resultado_esperado = f"a = {tupla[0]}, b = {tupla[1]} y c = {tupla[2]}"
            estado = resultado_obtenido == resultado_esperado
            resultados.append(Resultado(tupla, resultado_esperado, resultado_obtenido, estado).__dict__)
    except Exception as e:
        mensaje_error(e)
        error = True
    
    helper(resultados, tarea+'mostrar_numeros', uuid, error=error, deseo=deseo_ayudar)

def califica_concatenar_cadenas(f, uuid, deseo_ayudar):
    error = False
    resultados = []
    cadenas = [
        ("Hola, ", "mundo"),
        ("Estoy ", "aprendiendo"),
        ("a ", "programar"),
        ("en ", "Python")
    ]
    try:
        for tupla in cadenas:
            resultado_obtenido = f(tupla[0], tupla[1])
            resultado_esperado = tupla[0] + tupla[1]
            estado = resultado_obtenido == resultado_esperado
            resultados.append(Resultado(tupla, resultado_esperado, resultado_obtenido, estado).__dict__)
    except Exception as e:
        mensaje_error(e)
        error = True
    
    helper(resultados, tarea+'concatenar_cadenas', uuid, error=error, deseo=deseo_ayudar)