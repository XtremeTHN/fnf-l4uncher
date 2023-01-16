import os,glob,subprocess, sys
from modules.libupd import libupd

version = 0.1
def run():
    print("asd")

upd_obj = libupd(["https://raw.githubusercontent.com/XtremeTHN/fnf-l4uncher/main/VERSION","https://raw.githubusercontent.com/XtremeTHN/fnf-l4uncher/main/modules/files.json"])
if upd_obj.checkupd(version) == 1:
    print("Deseas actualizar? (S/N)")
    var = input()
    print(var)
    if var != 'N':
        print("Actualizando...")
        upd_obj.update()
        print("Hecho, reiniciando...")
        subprocess.Popen(['python3', ], shell=True, start_new_session=True)
        sys.exit()
