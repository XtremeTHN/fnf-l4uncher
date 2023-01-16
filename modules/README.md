# libupd.py
#### Documentación
updatelib.py re-escrito para actualizar mas comodamente

#### Introduccion
Para poder empezar a usar la libreria, primero tienes que inicializarla con solo una lista conteniendo una url que de directo a un archivo conteniendo un numero que represente una version y otra url que de directo a un archivo json en donde guardes el nombre y link de descarga directo al archivo.

Se escucha dificil pero lo he hecho facil.

### libupd(url)
En el argumento url como se ha explicado anteriormente debe contener una lista con dos url, si todo pasa correctamente devolverá un objeto para poder empezar a utilizar la libreria.

Si obtienes un `libupd.UrlExceptions.UnkownUrlError` deberias revisar si las url que proporcionaste funcionan, de igual manera, la excepcion te arrojara informacion en forma de `Debug data:` y un array después, que contendrá el codigo de error y el codigo de estado de la url (404 la pagina no existe)

Ejemplo:
```python
from libupd import libupd

update_obj = libupd(["https://example.com/example.version","https://example.com/example.json"])
```

Si obtienes una excepcion como esta `libupd.UrlExceptions.UrlNotSecure` es porque tu url no utiliza el protocolo https, que si esta excepcion no existiera el modulo requests tiraria una excepcion

También si le das una variable que no sea una lista, o una de las variables de la lista no es un `str` entonces habra un error especificando que deberia ser un tipo `str`.

### checkupd(version)
Este metodo comprobará si hay una version nueva en el sistema remoto comparando la variable **version** con el contenido del archivo de la version. Retorna un numero dependiendo si hay alguna actualizacion (0 si no hay, 1 si hay una).

Ejemplo:
```python
from libupd import libupd

update_obj = libupd(["https://example.com/example.version","https://example.com/example.json"])
if update_obj.checkupd(1.0) == 0:
    print("No hay actualizaciones disponibles")
else:
    print("Actualizacion disponible")
```

### update(path=os.getcwd())
Este metodo actualizara/creará archivos al consultar el contenido del archivo json proporcionado (url), si llegas a añadir el archivo principal al archivo json, deberás cerrar el script en ejecución o puede haber problemas.

Ejemplo:
```python
from libupd import libupd

update_obj = libupd(["https://example.com/example.version","https://example.com/example.json"])
if update_obj.checkupd(1.0) == 0:
    print("No hay actualizaciones disponibles")
else:
    print("Actualizacion disponible, actualizando...")
    update_obj.update()
```

### close()
Metodo para cerrar los objetos url de requests, se usaria para cuando termines de usar el modulo, no recibe ningun argumento.
Ejemplo:
```python
from libupd import libupd

update_obj = libupd(["https://example.com/example.version","https://example.com/example.json"])
if update_obj.checkupd(1.0) == 0:
    print("No hay actualizaciones disponibles")
else:
    print("Actualizacion disponible, actualizando...")
    update_obj.update()
    print("Hecho")
    update_obj.close()
```

### __connect()
Metodo privado que no deberias poder usar, solo es creado para facilitar las cosas dentro de la clase, y si por alguna extraña razón puedes usar este metodo, no te servira de mucho.