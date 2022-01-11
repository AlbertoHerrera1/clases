import requests
from datetime import datetime

tarea = 't1-'

class Resultado:
    def __init__(self, argumentos, esperado, obtenido, estado):
        self.argumentos = argumentos
        self.esperado = esperado
        self.obtenido = obtenido
        self.estado = estado

def mandar_a_firestore(uuid, ejercicio, calificacion, resultados, opinion):
    resp = requests \
        .post("https://us-central1-cursos-mios-01.cloudfunctions.net/calificar", \
        json={"uuid": uuid, \
        "curso": "pythondelaaalaz", \
        "ejercicio": ejercicio, \
        "tarea": '1', \
        "calificacion": calificacion, \
        "resultados": resultados, \
        "fecha": str(datetime.today()), \
        "opinion": opinion \
        })
    if resp.status_code != 200:
        print("""
            Hubo un error inesperado del lado del servidor, por favor
            revisa si tu calificación fue agregada.
        """)

def deseo_ayudar():
    return int(input("""
    Del 0 al 5, donde 0 es no me sirvió en lo absoluto
    y 5 es me sirvió muchísimo
    ¿Qué tanto te gustó este ejercicio?: 
    """))
    
    
def helper(resultados, nombre, uuid, error=False, deseo=False):
    if not error:
        assert uuid != None, "Ingresa tu clave"
        assert uuid != "TU CLAVE", "Ingresa tu clave"
        print(f"=====================================================================\n")
        print(f"============> Calificando {nombre} <============\n")
        print(f"=====================================================================\n")
        aciertos_arr = []
        errores_arr = []
        for resultado in resultados:
            if resultado['estado']:
                aciertos_arr.append(resultado)
            else:
                errores_arr.append(resultado)
        total = len(resultados)
        errores = len(errores_arr)
        aciertos = len(aciertos_arr)
        if total != 0:
            calificacion = (aciertos / total) * 100
            
            print(f"======> Calificación: {calificacion} <======\n")
            print(f"======> Aciertos: {aciertos} <======\n")
            print(f"======> Errores: {errores} <======\n")
            print("======> Casos existosos: <======\n")
            
            for resultado in aciertos_arr:
                print(f"Valores de entrada: {resultado['argumentos']}. \
                Valor esperado: {resultado['esperado']}. \
                Valor obtenido: {resultado['obtenido']}")
            
            
            print("======> Casos con error <======\n")
            for resultado in errores_arr:
                print(f"Valores de entrada: {resultado['argumentos']}. \
                Valor esperado: {resultado['esperado']}. \
                Valor obtenido: {resultado['obtenido']}")
            if errores == 0:
                print("======> No hubo errores :D <======\n")

            if deseo:
                opinion = deseo_ayudar()
                mandar_a_firestore(uuid, nombre, calificacion, resultados, opinion)

def mensaje_error(error):
    print("Hubo un error y no se pudo ejecutar el código, la tarea no fue calificada")
    print(f"El error es: {error}")