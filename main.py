import os,glob,multiprocessing, sys
from modules.libupd import libupd
from pynput import keyboard
from modules.getch import getch
version = 0.1
def run():
    os.system("python main.py")

upd_obj = libupd(["https://raw.githubusercontent.com/XtremeTHN/fnf-l4uncher/main/VERSION","https://raw.githubusercontent.com/XtremeTHN/fnf-l4uncher/main/modules/files.json"])
if upd_obj.checkupd(version) == 1:
    print("Deseas actualizar? (S/N)")
    if getch() != 'N':
        print("Actualizando...")
        upd_obj.update()
        print("Hecho, reiniciando...")
        new_proc = multiprocessing.Process(target=run,daemon=True)
        new_proc.start()
        sys.exit()
