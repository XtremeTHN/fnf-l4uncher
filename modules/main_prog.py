#!/usr/bin/python3
from pathlib import Path
from simple_term_menu import TerminalMenu
import sys, os, glo
from py_config import *
yes_no = ["[a] Si", "[b] No"]
class main_program:    
    def path_spaces(value):
        valor = value.replace(" ", "\ ")
        return valor
    def main():
        if os.path.exists(os.path.join(os.getcwd() + "/config.py")):
            from config import *
        else:
            print("Creando archivo de configuracion...")
            txt_obj = pyconfig.create_settings("config.py")
            fnf_path = input("Introduce el directorio de mods de Friday Night Funkin': ")
            if os.path.isdir(fnf_path) == False:
                os.remove('config.py')
                pyconfig.close(txt_obj)
                raise NotADirectoryError("Eso no es un directorio...")
            fnf_path = "'" + fnf_path + "'"
            configuracion = {
                'fnf_path':fnf_path
            }
            try:
                pyconfig.set_settings(txt_obj, configuracion)
                from config import *
            except:
                pass
            finally:
                pyconfig.close(txt_obj)
    

        try:
            if sys.argv[1] == "play":
                fnf_paths = main_program.list()
                choice = fnf_paths[TerminalMenu(fnf_paths, title = "Qué mod deseas jugar?").show()]
                ejecutable = glob.glob(os.path.join(choice + "/*.exe"))
            if str(ejecutable) == "[]":
                ejecutable = glob.glob(os.path.join(choice + "/**/*.exe"))
            os.system(f"cd {main_program.path_spaces(choice)} && wine {main_program.path_spaces(ejecutable[0])}")
            print("Si el mod no se ha iniciado, asegurese que la carpeta del mod no tenga caracteres especiales como ', -, ?, !, etc.")
        except:
            print(sys.exc_info())

    def list():
        print("Buscando mods...")
        paths = glob.glob(fnf_path+'/*')
        fnf_paths = []
        for x in paths:
            if os.path.isdir(x):
                fnf_paths.append(x)
            else:
                pass
        return fnf_paths
if __name__ == "__main__":
    if sys.argv[1] == "list":
        print("Mods encontrados:", list())
    print("No revisando actualizaciones disponibles...")
    main_program.main()
