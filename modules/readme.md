# updatelib.py
"Libreria" hecha por mi para actualizar/descargar cosas
### check_updates(version, url)
Puedes revisar si hay una nueva actualizacion con esta función, el funcionamiento es simple, compara la variable **version** con el contenido de la variable **url** (que por cierto ***DEBE*** de ser una url), si le pasas una variable que no sea `float` o `str` te saltara un error. Devuelve True si **version** es menor que **url**, False si es mayor.
Ejemplo:
```python
from updatelib import *
if updatelib.check_updates(1.0, "https://raw.githubusercontent.com/XtremeTHN/fnf-l4uncher/main/updates/version"):
	print("Actualización disponible")
```

### get_dict_of_files(url)
Esta funcion acepta solamente un argumento, una cadena que contenga una url que lleve a un archivo conteniendo el nombre y la url, esto se puede hacer con un diccionario de python, asi `files = {'test':'https://example.com'}`. Se puede guardar la informacion en un archivo con `open(filename, 'w+b')` o simplemente añadiendo al final un `.decode("utf-8")` (la funcion devuelve el contenido de la url en bytes). Ejemplo:
```python
from updatelib import *
if updatelib.check_updates(1.0, "https://raw.githubusercontent.com/XtremeTHN/fnf-l4uncher/main/updates/version"):
	print("Actualización disponible")
	print(updatelib.get_dict_of_files("https://raw.githubusercontent.com/XtremeTHN/fnf-l4uncher/main/updates/version.py").decode("utf-8"))
```
Produccion:
```
Actualización disponible
Comprobando actualizaciones...
files = {"py_config.py":"https://raw.githubusercontent.com/XtremeTHN/fnf-l4uncher/main/modules/py_config.py"}
```

### update(files)
Con esta funcion puedes actualizar los archivos que especifiques, con un diccionario (debe contener el nombre del archivo y la url como en `get_dict_of_files()`), solo acepta un argumento que es **files**, si le pasas a esta funcion algo que no sea un diccionario lanzará un error. Recomiendo usarlo junto a `get_dict_of_files()` sin olvidar el `.decode("utf-8")`.
Ejemplo:
```python
from updatelib import *
if updatelib.check_updates(1.0, "https://raw.githubusercontent.com/XtremeTHN/fnf-l4uncher/main/updates/version"):
	print("Actualización disponible")
	updatelib.update(updatelib.get_dict_of_files("https://raw.githubusercontent.com/XtremeTHN/fnf-l4uncher/main/updates/version.py").decode("utf-8"))  
```

# pyconfiglib.py
Libreria hecha por mi para crear archivos de configuracion py
### create_settings(filename)
Crea un archivo de configuracion (py), si el archivo ya existe, se lanzará un error, devuelve el objeto de la funcion `open()` este objeto se ocupa para las demás funciones.
Ejemplo:
```python
import pyconfiglib as config
config.create_settings(file_name)
```
