# updatelib.py
"Libreria" hecha por mi para actualizar/descargar cosas
### check_updates(version, url)
Version: Se espera un numero float, representando la version de algo
Url: Se espera una cadena con una url
La cadena url deberá contener un link directo a un archivo con la version nueva ya que esto funciona comparando lo que diga la url con la variable version
Devuelve True si se detecta que el primer argumento es menor que el archivo de texto de la url, False si no se detectó nada
Ejemplo:
       from updatelib import *
       if updatelib.check_updates(1.0, "https://raw.githubusercontent.com/XtremeTHN/fnf-l4uncher/main/updates/version"):
          print("Actualización disponible")

### get_dict_of_files(url)
    url: Se espera una cadena con una url
    Se obtiene un archivo py con un diccionario para saber que archivos debe de descargar
    La cadena url deberá contener un link directo a un archivo py con un diccionario mostrando el nombre y la url de lo que se desea actualizar
    Se recomienda guardar la informacion en un archivo con `open(filename, 'w+b')`
    Devuelve el contenido de la url (tipo byte)
    Ejemplo:
       from updatelib import *
       if updatelib.check_updates(1.0, "https://raw.githubusercontent.com/XtremeTHN/fnf-l4uncher/main/updates/version"):
          print("Actualización disponible")
          print(updatelib.get_dict_of_files("https://raw.githubusercontent.com/XtremeTHN/fnf-l4uncher/main/updates/version.py").decode("utf-8"))
    Produccion:
       Actualización disponible
       Comprobando actualizaciones...
       files = {"py_config.py":"https://raw.githubusercontent.com/XtremeTHN/fnf-l4uncher/main/modules/py_config.py"}\n
       
update(files)
    files: Se espera un diccionario 
    Actualiza varios archivos, se recomienda usarlo en conjunto con `get_dict_of_files()`
    El diccionario url debe contener el nombre y la url de descarga del archivo
    Ejemplo:
      from updatelib import *
       if updatelib.check_updates(1.0, "https://raw.githubusercontent.com/XtremeTHN/fnf-l4uncher/main/updates/version"):
          print("Actualización disponible")
          updatelib.update(updatelib.get_dict_of_files("https://raw.githubusercontent.com/XtremeTHN/fnf-l4uncher/main/updates/version.py").decode("utf-8"))  
