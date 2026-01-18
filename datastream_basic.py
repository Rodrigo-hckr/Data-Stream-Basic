def cargar_datos():
    """
    Etapa 1: Cargar datos
    simula la entradda de información.
    En caso real, podria leer de un archivo, base de datos o API
    
    """
    datos = [
        {"nombre": "Carlos", "edad": "25", "correo": "carlos@example.com"},
        {"nombre": "Adriana", "edad": "35", "correo": "adriana@example.com"},
        {"nombre": "Lucia", "edad": "20", "correo": "lucia@example.com"}
    ]
    return datos

def transformar_datos(datos):
    """
    Etapa 2: Transformar datos.
    Limpia y normaliza la infomración.
    Convierte la edad en entero
    Elimina espacios inecesarios
    normaliza correos en minusculas
    """
    datos_trasnformados = []
    for d in datos:
        registro = {
            "nombre": d["nombre"].strip(),
            "edad": int(d["edad"].strip()),
            "correo": d["correo"].lower()
        }
        datos_trasnformados.append(registro)
    return datos_trasnformados

def mostrar_resultados(datos):
    """
    Etapa 3: mostrar resultados.
    Impirnme los datos procesados.
    en una pipeline real, podra guardar en un archivo
    base de datos o dashboard.
    """
    print("=== Resultados de DataStream basic ===")
    for d in datos:
        print(f"nombre: {d['nombre']}, Edad: {d['edad']}, Correo: {d['correo']}")

def pipeline_datastream_basic():
    """
    Pipeline principal: DataStream Basic
    Encadena las siguientes etapas:
    Cargar datos
    Transformar datos
    Mostrar resultados
    """
    datos = cargar_datos()
    datos_transformados = transformar_datos(datos)
    mostrar_resultados(datos_transformados)
    
# punto de entrada
if __name__ == "__main__":
    pipeline_datastream_basic()