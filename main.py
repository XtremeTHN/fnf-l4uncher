import os,glob,subprocess, sys
from modules.libupd import libupd

version = 0.2
def run():
    print("asd")

upd_obj = libupd(["https://raw.githubusercontent.com/XtremeTHN/fnf-l4uncher/main/VERSION","https://raw.githubusercontent.com/XtremeTHN/fnf-l4uncher/main/modules/files.json"])
if upd_obj.checkupd(version) == 1:
    var = input("Deseas actualizar? (S/N)")
    print(var)
    if var not in ['N','n','no','nO','No']:
        print("Actualizando...")
        upd_obj.update()
        print("Hecho...")
        sys.exit()
