from utilidades import Resultado, mensaje_error, helper, template_sencillo, template_iterable


def inversion(uuid, deseo_ayudar):
    def decorador(f):
        def contenedora(monto_inicial, interes):
            resultados = []
            excepcion = None
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
                    excepcion = str(e)
                    break
            helper(resultados, 'inversion', uuid, error=error, deseo=deseo_ayudar, excepcion=excepcion)
        return contenedora
    return decorador

def califica_suma_test(f, uuid, deseo_ayudar):
    resultados = []
    excepcion = None
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
                excepcion = str(e)
                break
        if error:
            break
    
    helper(resultados, 't1-', 'suma_test', uuid, error=error, deseo=deseo_ayudar, excepcion=excepcion)


def califica_suma(f, uuid, deseo_ayudar):
    resultados = []
    excepcion = None
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
                excepcion = str(e)
                break
        if error:
            break
    
    helper(resultados, 't2-', 'suma', uuid, error=error, deseo=deseo_ayudar, excepcion=excepcion)

def califica_resta_test(f, uuid, deseo_ayudar):
    resultados = []
    excepcion = None
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
                excepcion = str(e)
                break
        if error:
            break
    helper(resultados, 't1-', 'resta_test', uuid, error=error, deseo=deseo_ayudar, excepcion=excepcion)


def califica_resta(f, uuid, deseo_ayudar):
    resultados = []
    excepcion = None
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
                excepcion = str(e)
                break
        if error:
            break
    helper(resultados, 't2-', 'resta', uuid, error=error, deseo=deseo_ayudar, excepcion=excepcion)


@template_sencillo("Hola, mundo!", 'saludo_test', 't1-')
def califica_saludo_test(f, uuid, deseo_ayudar):
    return f

@template_sencillo("Hola, mundo!", 'saludo', 't2-')
def califica_saludo(f, uuid, deseo_ayudar):
    return f

def califica_multiplicacion(f, uuid, deseo_ayudar):
    error = False
    resultados = []
    excepcion = None
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
                excepcion = str(e)
                break
        if error:
            break
    helper(resultados, 't2-', 'multiplicacion', uuid, error=error, deseo=deseo_ayudar, excepcion=excepcion)

def califica_multiplicacion(f, uuid, deseo_ayudar):
    error = False
    resultados = []
    excepcion = None
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
                excepcion = str(e)
                break
        if error:
            break
    helper(resultados, 't2-', 'multiplicacion', uuid, error=error, deseo=deseo_ayudar, excepcion=excepcion)

def califica_division(f, uuid, deseo_ayudar):
    error = False
    resultados = []
    excepcion = None
    for i in range(1, 4):
        for j in range(1, 6):
            try:
                resultado_resta = f(i, j)
                resultado_real = i / j
                estado = resultado_real==resultado_resta
                resultados.append(Resultado((i, j), resultado_real, resultado_resta, estado).__dict__)
            except Exception as e:
                mensaje_error(e)
                error = True
                excepcion = str(e)
                break
        if error:
            break
    helper(resultados, 't2-', 'division', uuid, error=error, deseo=deseo_ayudar, excepcion=excepcion)


def califica_division_cuidadosa(f, uuid, deseo_ayudar):
    error = False
    resultados = []
    excepcion = None
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
                excepcion = str(e)
                break
        if error:
            break
    helper(resultados, 't2-', 'division-cuidadosa', uuid, error=error, deseo=deseo_ayudar, excepcion=excepcion)

def califica_al_cuadrado(f, uuid, deseo_ayudar):
    error = False
    resultados = []
    excepcion = None
    for j in range(1, 6):
        try:
            resultado_resta = f(j)
            resultado_real = j ** 2
            estado = resultado_real==resultado_resta
            resultados.append(Resultado((j,), resultado_real, resultado_resta, estado).__dict__)
        except Exception as e:
            mensaje_error(e)
            error = True
            excepcion = str(e)
            break
        
    helper(resultados, 't2-', 'al_cuadrado', uuid, error=error, deseo=deseo_ayudar, excepcion=excepcion)


def califica_potencia(f, uuid, deseo_ayudar):
    error = False
    resultados = []
    excepcion = None
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
                excepcion = str(e)
                break
        if error:
            break
    helper(resultados, 't2-', 'potencia', uuid, error=error, deseo=deseo_ayudar, excepcion=excepcion)


def califica_suma_mas_dos(f, uuid, deseo_ayudar):
    error = False
    resultados = []
    excepcion = None
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
                excepcion = str(e)
                break
        if error:
            break
    helper(resultados, 't2-', 'suma_mas_dos', uuid, error=error, deseo=deseo_ayudar, excepcion=excepcion)

def califica_resta_menos_veinte(f, uuid, deseo_ayudar):
    error = False
    resultados = []
    excepcion = None
    for i in range(-2, 2):
        for j in range(1, 6):
            try:
                resultado_resta = f(i, j)
                resultado_intermedio = j - i
                resultado_real = resultado_intermedio - 20
                estado = resultado_real==resultado_resta
                resultados.append(Resultado((i, j), resultado_real, resultado_resta, estado).__dict__)
            except Exception as e:
                mensaje_error(e)
                error = True
                excepcion = str(e)
                break
        if error:
            break
    helper(resultados, 't2-', 'resta_menos_veinte', uuid, error=error, deseo=deseo_ayudar, excepcion=excepcion)

@template_iterable([
    [[1], 1],
    [[2], 2],
    [[-3], 3],
    [[-3.6], 3.6],
    [[-100000], 100000]
], 'valor_absoluto', 't2-')
def califica_valor_absoluto(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[3.4], 3],
    [["2"], 2],
    [[-3.2], -3],
    [["3"], 3]
], 'convertir_a_entero', 't2-')
def califica_convertir_a_entero(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[3], 3.0],
    [[1.2], 1.2],
    [["2.2"], 2.2]
], 'convertir_a_float', 't2-')
def califica_convertir_a_float(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[3.5, 1], 3.5],
    [[100.9, 1], 100.9],
    [[-3.689, 2], -3.69]
], 'redondear_a_n_digitos', 't2-')
def califica_redondear_a_n_digitos(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[6,3], 0],
    [[1,3], 1],
    [[100,67], 33],
    [[23,5], 3]
], 'modulo', 't2-')
def califica_modulo(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[100, 10], 10.0],
    [[1010, 10], 101.0],
    [[34, 34], 1.0],
    [[-6, 4], -2],
    [[.5, 1], 0.0],
], 'división_entera', 't2-')
def califica_division_entera(f, uuid, deseo_ayudar):
    return f

@template_sencillo("HOLA, MUNDO", "en_mayusculas", 't2-', ["hola, mundo"])
def califica_en_mayusculas(f, uuid, deseo_ayudar):
    return f

@template_sencillo("hola, mundo", 'en_minusculas', 't2-', ["HOLA, MUNDO"])
def califica_en_minusculas(f, uuid, deseo_ayudar):
    return f

@template_iterable([
        [["Hola"], 'H'],
        [["mundo",], 'm'],
        [["me"], 'm'],
        [["gusta"], 'g'],
        [["este"], 'e'],
        [["curso"], 'c'],
        [["y las"], 'y'],
        [["'t2-'s"], '\''],
        [["están"], 'e'],
        [["geniales"], 'g']
    ], 'primer_caracter', 't2-')
def califica_primer_caracter(f, uuid, deseo_ayudar):
    return f

@template_iterable([
        [["Esta",], 't'],
        [["'t2-'",], '-'],
        [["está",], 't'],
        [["curiosa",], 's'],
        [["eso de",], 'd'],
        [["usar",], 'a'],
        [["índices",], 'e'],
        [["negativos",], 'o'],
        [["es",], 'e'],
        [["nuevo",], 'v']
    ], 'penultimo_caracter', 't2-')
def califica_penultimo_caracter(f, uuid, deseo_ayudar):
    return f

@template_iterable([
        [[1,2,3], "a = 1, b = 2 y c = 3"],
        [[4,5,6], "a = 4, b = 5 y c = 6"],
        [[7,8,9], "a = 7, b = 8 y c = 9"],
        [[10, 11, 12], "a = 10, b = 11 y c = 12"],
        [[13, 14, 15], "a = 13, b = 14 y c = 15"]
    ], 'mostrar_numeros', 't2-')
def califica_mostrar_numeros(f, uuid, deseo_ayudar):
    return f

@template_iterable([
        [["Hola, ", "mundo"], 'Hola, mundo'],
        [["Estoy ", "aprendiendo"], "Estoy aprendiendo"],
        [["a ", "programar"], 'a programar'],
        [["en ", "Python"], 'en Python']
    ], 'concatenar_cadenas', 't2-')
def califica_concatenar_cadenas(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[10], 98.10000000000001],
    [[34], 333.54],
    [[54], 529.74],
    [[98], 961.38],
    [[8.3], 81.42300000000002],
], 'peso_de_un_cuerpo', 't2-')
def califica_peso_de_un_cuerpo(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[30, 25], 1.2],
    [[456, 234], 1.9487179487179487],
    [[89, 23], 3.869565217391304],
    [[1567, 1268], 1.2358044164037856],
    [[45, 87], 0.5172413793103449],
], 'calculo_de_velocidad_constante', 't2-')
def califica_calculo_de_velocidad_constante(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[30, 30, 100], 3030],
    [[20, 10, 130], 1320],
    [[45, 89, 78], 6987],
    [[487, 65, 10], 1137],
    [[1000, 10, 10], 1100],
], 'calculo_de_velocidad_con_aceleracion', 't2-')
def califica_calculo_de_velocidad_con_aceleracion(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[0, 10, 60, 10], 18600.0],
    [[10, 20, 120, 5], 38410.0],
    [[20, 30, 180, 100], 1625420.0],
    [[0, 5, 30, 5], 2400.0],
], 'calculo_de_posicion_de_un_cuerpo_en_movimiento_con_aceleracion_constante', 't2-')
def califica_calculo_de_posicion_de_un_cuerpo_en_movimiento_con_aceleracion_constante(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[50.0, 1.60, 110.0, 1.90, 80.0, 1.50], 28.51923989432646],
    [[55.0, 1.50, 130.0, 1.60, 85.0, 1.55], 36.86850237985123],
    [[65.0, 1.65, 150.0, 1.50, 83.0, 1.62], 40.722685977705304],
    [[30.0, 1.30, 87.0, 1.80, 40.0, 1.32], 22.52005742681733],
    [[85.0, 1.80, 67.0, 1.40, 80.0, 1.56], 31.097117055603018],
], 'promedio_inidice_masa_corporal', 't2-')
def califica_promedio_inidice_masa_corporal(f, uuid, deseo_ayudar):
    return f
####################################################################################################
#                                       Tarea 4
####################################################################################################

@template_sencillo([], 'creacion_de_lista_vacia', 't4-')
def califica_creacion_de_lista_vacia(f, uuid, deseo_ayudar):
    return f

@template_sencillo((), 'creacion_de_una_tupla_vacia', 't4-')
def califica_creacion_de_una_tupla_vacia(f, uuid, deseo_ayudar):
    return f
    
@template_sencillo({}, 'creacion_de_un_diccionario_vacio', 't4-')    
def califica_creacion_de_un_diccionario_vacio(f, uuid, deseo_ayudar):
    return f

@template_iterable([
        ([[]], 0),
        ([[1,2,3]], 3),
        ([[1,2,3,4,5,6,7,8,9,10]], 10),
        ([list(range(100))], 100)
    ], 'obtener_longitu_de_una_lista', 't4-')
def califica_obtener_longitud_de_una_lista(f, uuid, deseo_ayudar):
    return f

@template_iterable([
        ([()], 0),
        ([(1,2,3)], 3),
        ([(1,2,3,4,5,6,7,8,9,10)], 10),
        ([tuple(range(100))], 100)
    ], 'obtener_longitud_de_una_tupla', 't4-')
def califica_obtener_longitud_de_una_tupla(f, uuid, deseo_ayudar):
    return f


@template_iterable([
        ([{}], 0),
        ([{"Uno": 1,"Dos": 2, "Tres": 3}], 3),
        ([{"Dia": "Martes"}], 1),
        ([{"Curso": "Python de la a a la z", "Fecha": "17 de enero"}], 2)
    ], 'obtener_longitud_de_un_diccionario', 't4-')
def califica_obtener_longitud_de_un_diccionario(f, uuid, deseo_ayudar):
    return f

@template_iterable([
        ([1], [1]),
        ([{"Uno": 1,"Dos": 2, "Tres": 3}], [{"Uno": 1,"Dos": 2, "Tres": 3}]),
        ([{"Dia": "Martes"}], [{"Dia": "Martes"}]),
        ([{"Curso": "Python de la a a la z", "Fecha": "17 de enero"}], [{"Curso": "Python de la a a la z", "Fecha": "17 de enero"}])
    ], 'creacion_de_una_lista_con_exactamente_un_elemento', 't4-')
def califica_creacion_de_una_lista_con_exactamente_un_elemento(f, uuid, deseo_ayudar):
    return f

@template_iterable([
        ([1], (1,)),
        ([{"Uno": 1,"Dos": 2, "Tres": 3}], ({"Uno": 1,"Dos": 2, "Tres": 3},)),
        ([{"Dia": "Martes"}], ({"Dia": "Martes"},)),
        ([{"Curso": "Python de la a a la z", "Fecha": "17 de enero"}], ({"Curso": "Python de la a a la z", "Fecha": "17 de enero"},))
    ], 'creacion_de_una_tupla_con_exactamente_un_elemento', 't4-')
def califica_creacion_de_una_tupla_con_exactamente_un_elemento(f, uuid, deseo_ayudar):
    return f

@template_iterable([
        ([27], {'edad': 27}), 
        ([60], {'edad': 60}) 
    ], 'creacion_de_un_diccionario_con_clave_edad', 't4-')
def califica_creacion_de_un_diccionario_con_clave_edad(f, uuid, deseo_ayudar):
    return f


@template_sencillo(['a', 'b', 'c'], 'creacion_de_una_lista_con_tres_elementos', 't4-')
def califica_creacion_de_una_lista_con_tres_elementos(f, uuid, deseo_ayudar):
    return f

@template_sencillo(('a', '1', 'b'), 'creacion_de_una_tupla_con_tres_elementos', 't4-')
def califica_creacion_de_una_tupla_con_tres_elementos(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[[1,2,3,4,5,6]], 6],
    [[['a', 'b', 'c', 'd', 'e', 'f']], 'f'],
    [[[10, 11, 12, 13, 14, 15, 16, 17]], 15]
], 'acceder_al_elemento_5', 't4-')
def califica_acceder_al_elemento_5(f, uuid, deseo_ayudar):
    return f

@template_iterable([
            [[27], 26], 
            [[60], 59],
            [[101], 100],
        ], 'acceder_al_ultimo_elemento_de_una_tupla_en_rango', 't4-')
def califica_acceder_al_ultimo_elemento_de_una_tupla_en_rango(f, uuid, deseo_ayudar):
        return f


@template_sencillo({1,2,3,4,5}, 'conjunto_con_elementos_del_1_al_5', 't4-')
def califica_conjunto_con_elementos_del_1_al_5(f, uuid, deseo_ayudar):
    return f
    
@template_iterable([
    [['Hola', 'Aloha', 'Saludos'], {'Hola', 'Aloha', 'Saludos'}]
], 'conjunto_con_tres_palabras', 't4-')
def califica_conjunto_con_tres_palabras(f, uuid, deseo_ayudar):
    return f


@template_sencillo({
    'estado': 'Activo',
    'datos': {
        'curso': 'Python de la A a la Z',
        'tareas': 3
    }
}, 'creacion_de_diccionario_dentro_de_otro_diccionario', 't4-')
def califica_creacion_de_diccionario_dentro_de_otro_diccionario(f, uuid, deseo_ayudar):
    return f

@template_sencillo([
    {"pais": "México", "nombre oficial": "Estados Unidos Mexicanos"},
    {"pais": "Estados Unidos", "nombre oficial": "Estados Unidos de América"}
], 'creacion_de_lista_de_diccionarios', 't4-')
def califica_creacion_de_lista_de_diccionarios(f, uuid, deseo_ayudar):
    return f

@template_sencillo({
        "tarea1": [
            10, 10, 8
        ],
        "tarea2": [
            10, 8, 7
        ]
    }, 'creacion_de_diccionario_con_listas', 't4-')
def califica_creacion_de_diccionario_con_listas(f, uuid, deseo_ayudar):
    return f

@template_sencillo({
        "historial": ((3,5,1,6), (56,2,1,7), (62,4,78,3))
    }, 'creacion_de_diccionario_con_tuplas', 't4-')
def califica_creacion_de_diccionario_con_tuplas(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [['edad', 27], {'edad': 27}],
    [['Nombre', "Pepito"], {'Nombre': 'Pepito'}],
    [[1, 27], {1: 27}],
    [["Calif", 100], {'Calif': 100}],
], 'creacion_de_diccionario_a_partir_de_clave', 't4-')
def califica_creacion_de_diccionario_a_partir_de_clave(f, uuid, deseo_ayudar):
    return f

@template_sencillo(
    list(range(10001)), 'lista_hasta_10000', 't4-'
)
def califica_lista_hasta_10000(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[10], list(range(10))],
    [[100], list(range(100))],
    [[110], list(range(110))],
    [[2], list(range(2))],
    [[3], list(range(3))],
], 'lista_en_rango', 't4-')
def califica_lista_en_rango(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[10, 20], list(range(10, 20))],
    [[38, 40], list(range(38, 40))],
    [[12, 22], list(range(12, 22))],
    [[-2, 32], list(range(-2, 32))],
    [[-29, 20], list(range(-29, 20))],
], 'lista_en_rango_v_2', 't4-')
def califica_lista_en_rango_v_2(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[[1,2,3], 4,5,6], [1,2,3,4,5,6]],
    [[[1,2,3], 'hola', 'adios', 'saludos'], [1,2,3,'hola', 'adios', 'saludos']],
    [[[2, "", 1], "4,5,6", {}, ()], [2, "", 1,"4,5,6", {}, ()]]
], 'agregar_elementos_al_final_de_una_lista', 't4-')
def califica_agregar_elementos_al_final_de_una_lista(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[[1,2,3], [4,5,6]], [1,2,3,4,5,6]],
    [[['a', 'e'], ['i', 'o', 'u']], ['a', 'e','i', 'o', 'u']],
], 'extender_lista_con_otra_lista', 't4-')
def califica_extender_lista_con_otra_lista(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[[1,3], 2, 1], [1,2,3]],
    [[["Hola, ", "mundo", " de nuevo"] , " soy yo", 2], ["Hola, ", "mundo", " soy yo", " de nuevo"]]
], 'insertar_elementos_en_una_posicion', 't4-')
def califica_insertar_elementos_en_una_posicion(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[[1,2,3,4,5,6,7,8,9], 0], [2,3,4,5,6,7,8,9]],
    [[[1,2,3,4,5,6,7,8,9], 1], [1,3,4,5,6,7,8,9]],
    [[[1,2,3,4,5,6,7,8,9], 2], [1,2,4,5,6,7,8,9]],
    [[[1,2,3,4,5,6,7,8,9], 3], [1,2,3,5,6,7,8,9]],
    [[[1,2,3,4,5,6,7,8,9], 4], [1,2,3,4,6,7,8,9]],
    [[[1,2,3,4,5,6,7,8,9], 5], [1,2,3,4,5,7,8,9]],
], 'borrar_elemento_por_indice', 't4-')
def califica_borrar_elemento_por_indice(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[[1, 'hola', 2, 'salduo', 3, 'adiós'], 1], ['hola', 2, 'salduo', 3, 'adiós']],
    [[[1, 'hola', 2, 'salduo', 3, 'adiós'], 'hola'], [1, 2, 'salduo', 3, 'adiós']]
], '_borrar_coincidencia', 't4-')
def califica_borrar_coincidencia(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[[9,8,6,7,4,5,3,1,2]], [1,2,3,4,5,6,7,8,9]],
    [[[5,6,7,4,8,3,9,2,1]], [1,2,3,4,5,6,7,8,9]],
], 'ordenar_lista', 't4-')
def califica_ordenar_lista(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[[1,2,3,4,5,6,7,8,9], 1000], [1,2,3,4,5,1000,7,8,9]],
    [[[1,2,3,4,5,6,7,8,9], "Hola"], [1,2,3,4,5,"Hola",7,8,9]],
    [[[1,2,3,4,5,6,7,8,9], "Sorpresa"], [1,2,3,4,5,"Sorpresa",7,8,9]],
], 'asignar_en_5', 't4-')
def califica_asignar_en_5(f, uuid, deseo_ayudar):
    return f

@template_sencillo({
        'tiendas': {
            'Don Pepe Chuy': [
                {
                    'Ventas': [100, 200, 300] 
                },
                {
                    'Ventas': [100, 200, 300]
                }
            ],
            'El Ruki': [
                {
                    'Ventas': [234, 543, 654]
                },
                {
                    'Ventas': [980, 579, 123] 
                }
            ]
        }
    }, 'borrar_elemento_en_estructura_compleja', 't4-', argumentos=[
        {
        'tiendas': {
            'Don Pepe Chuy': [
                {
                    'Ventas': [100, 200, 300, -1]
                },
                {
                    'Ventas': [100, 200, 300]
                }
            ],
            'El Ruki': [
                {
                    'Ventas': [234, 543, 654]
                },
                {
                    'Ventas': [980, 579, 123, 0]
                }
            ]
        }
    }
    ])
def califica_borrar_elemento_en_estructura_compleja(f, uuid, deseo_ayudar):
    return f

@template_sencillo(
    {'Pepe': 9.5, 'Juan': 9.5},
    'obtener_promedio', 't4-',
    argumentos=[
            {
            'Pepe':[
                    {'nombre': 'primer parcial', 'calif': 9},
                    {'nombre': 'segundo parcial', 'calif': 10}
                ],
            'Juan': [
                    {'nombre': 'primer parcial', 'calif': 9},
                    {'nombre': 'segundo parcial', 'calif': 10}
                ]
            }
        ]
    )
def califica_obtener_promedio(f, uuid, deseo_ayudar):
    return f
####################################################################################################
#                                       Tarea 3
####################################################################################################

@template_iterable([
    [["Hola", "Hola"], "Son iguales"],
    [['Hola', 'Hola'], "Son iguales"],
    [["Hola", "hola"], "Son diferentes"],
    [["Mi nombre es:", "Mi nombre es"], "Son diferentes"],
    [["Tengo ... años", "Tengo --- años"], "Son diferentes"],
], 'son_iguales', 't3-')
def califica_son_iguales(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[2], True],
    [[201], False],
    [[3333], False],
    [[1234], True],
    [[209872], True],
], 'es_par', 't3-')
def califica_es_par(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[17], "Eres menor de edad"],
    [[18], "Eres mayor de edad"],
    [[12], "Eres menor de edad"],
    [[81], "Eres mayor de edad"],
    [[99], "Eres mayor de edad"],
], 'mayor_de_edad', 't3-')
def califica_mayor_de_edad(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[2,2], 1.0],
    [[4,2], 2.0],
    [[10,5], 2.0],
    [[23,0], "No puedo dividir entre cero"],
    [[1567,0], "No puedo dividir entre cero"],
], 'division_cuidadosa', 't3-')
def califica_division_cuidadosa(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[3,2], "El primero es mayor"],
    [[29834,209], "El primero es mayor"],
    [[1,2], "El segundo es mayor"],
    [[89,89], "Son iguales"],
    [[2,2], "Son iguales"],
], 'es_mayor', 't3-')
def califica_es_mayor(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[21], "Pertenece"],
    [[30], "Pertenece"],
    [[20], "No pertenece"],
    [[16], "No pertenece"],
    [[28], "Pertenece"],
], 'en_medio', 't3-')
def califica_en_medio(f, uuid, deseo_ayudar):
    return f


@template_iterable([
    [[10000, 'Educación'], '8%'],
    [[15000, 'Educación'], '10%'],
    [[25000, 'Educación'], '10%'],
    [[10000, 'Ganadería'], '8%'],
    [[15000, 'Ganadería'], '10%'],
    [[25000, 'Ganadería'], '10%'],
    [[10000, 'Textiles'], '12%'],
    [[15000, 'Textiles'], '14%'],
    [[25000, 'Textiles'], '14%'],
    [[10000, 'Tecnología'], '12%'],
    [[15000, 'Tecnología'], '14%'],
    [[25000, 'Tecnología'], '14%'],
], 'impuestos', 't3-')
def califica_impuestos(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[5.5], 'Pasaste'],
    [[5.6], 'Pasaste'],
    [[10], 'Pasaste'],
    [[4.6], 'Prueba de nuevo'],
    [[5.4], 'Prueba de nuevo'],
], 'calificacion_aprobatoria', 't3-')
def califica_calificacion_aprobatoria(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[1.40], "Puede subir :D"],
    [[1.23], "No puede subir :("],
    [[1.80], "Puede subir :D"]
], 'puede_subir', 't3-')
def califica_puede_subir(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[1,2,3], "Escaleno"],
    [[3,3,3], "Equilátero"],
    [[1,2,2], "Isósceles"],
], 'tipo_de_triangulo', 't3-')
def califica_tipo_de_triangulo(f, uuid, deseo_ayudar):
    return f

####################################################################################################
#                              Tarea 5 (tarea 4 ya que la uno no fue tarea)
####################################################################################################


@template_iterable([
    [["ae22"], (2,2)],
    [["1bq22"], (0,3)],
    [["aeiou"], (5,0)],
    [["12345"], (0,5)],
    [["12345aeiou"], (5,5)],
], 'contar_vocales_y_numeros', 't5-')
def califica_contar_vocales_y_numeros(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[{"alumnos": [10, 10]}], 10],
    [[{"alumnos": [5, 10]}], 7.5],
    [[{"alumnos": [5, 10, 5, 10]}], 7.5],
    [[{"alumnos": [8, 7, 6, 5, 10]}], 7.2],
    [[{"alumnos": [2, .5, 10, 10, 10]}], 6.5],
], 'obtener_promedio', 't5-')
def califica_obtener_promedio(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[3], 6],
    [[4], 24],
    [[5], 120],
    [[6], 720],
    [[7], 5040],
    [[8], 40320],
], 'calcular_factorial', 't5-')
def califica_calcular_factorial(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[[1,2,3], [2,4,6]], True],
    [[[10,20,30], [20,40,60]], True],
    [[[1,2,3], [2,4,5]], False],
    [[[4,3,8], [8,6,16]], True],
    [[[1], [1]], False]
], 'pares_un_medio', 't5-')
def califica_pares_un_medio(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[[1,2,3,4,5,6,7,8,9,10]], [5,10]],
    [[[10, 20, 30, 40, 50]], [10, 20, 30, 40, 50]],
    [[[1]], []],
    [[[33,44,55,66,77,88,99]], [55]],
    [[[101, 105, 104, 100]], [105, 100]],
], 'multiplos_de_5', 't5-')
def califica_multiplos_de_5(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[[1,2,3,4,5,6]], (4.0, 3.0)],
    [[[3,4,5,1,7,3,2]], (3.0, 3.8)],
    [[[1,2,3,5,6,10,11,200,32,13]], (50.0, 6.6)],
    [[[2,8,6,3,7,4,83,21,45]], (5.0, 31.8)],
    [[[97,5,3,2,34,5,6,766]], (202.0, 27.5)],
], 'promedios', 't5-')
def califica_promedios(f, uuid, deseo_ayudar):
    return f


@template_iterable([
    [[10, 20], [10, 12, 14, 16, 18, 20]],
    [[100, 200], [100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]],
    [[1, 2], [2]],
    [[2, 4], [2, 4]],
    [[3, 100], [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]],
], 'pares_en_rango', 't5-')
def califica_pares_en_rango(f, uuid, deseo_ayudar):
    return f

@template_iterable([
    [[[("tacos", 300), ("enchiladas", 200), ("sopes", 150)]], 650],
    [[[("Macbook Pro", 50), ("Macbook Air", 200), ("IPhone", 1000)]], 1250],
    [[[("Asus ROG", 5), ("Black Shark 4 Pro", 2), ("Realme GT Neo", 3), ("Nubia Red Magic 6", 4), ("Lenovo Legion Phone Duel 2", 1)]], 15],
    [[[("Sony MDR", 28), ("Cheelom", 34), ("Dinden", 3)]], 65],
    [[[("XYZ", 278), ("AYX", 312), ("KJO", 123)]], 713],
], 'suma_totales', 't5-')
def califica_suma_totales(f, uuid, deseo_ayudar):
    return f