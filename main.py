import os, glob, sys, argparse,json
from modules.libupd import libupd
from simple_term_menu import TerminalMenu
config_file = 'modules/config.json'
def update_json(filename,data):
    with open(filename,'w') as file:
        json.dump(data,file,indent=4)

def get_json_data(filename):
    with open(filename,'r') as file:
        return json.load(file)

def terminal(opts,titlex="placeholder"):
    if len(opts) < 2:
        raise IndexError("debug")
    menu = TerminalMenu(opts, title=titlex)
    return menu.show()

version = 1.0
try:
    upd_obj = libupd(["https://raw.githubusercontent.com/XtremeTHN/fnf-l4uncher/main/VERSION","https://raw.githubusercontent.com/XtremeTHN/fnf-l4uncher/main/modules/files.json"])
    if upd_obj.checkupd(version) == 1:
        var = input("[INFO] Actualizacion disponible, desea actualizar? (S/N): ")
        if var not in ['N','n','no','nO','No']:
            print("[INFO] Actualizando...")
            upd_obj.update()
            print("Hecho...")
            sys.exit()
except:
    pass
if not os.path.exists(config_file):
    configs = {
        "paths": [],
        "executables": []
    }
    with open(config_file,'w+') as file:
        json.dump(configs,file,indent=4)
        fnf_paths = json.load(file)
else:
    fnf_paths = json.load(open(config_file,'r'))

parser = argparse.ArgumentParser(description="Friday Night Funkin Launcher")
parser.add_argument('-s','--start',action='store', dest='fnf')
parser.add_argument('-afm','--add-fnf-mod',action='append', dest='fnf_mod_path')
parser.add_argument('-pc','--print-config',action='store_true', dest='pc')

args = parser.parse_args()
if args.fnf_mod_path != None:
    for x in args.fnf_mod_path:
        if x not in fnf_paths['paths']:
            fnf_paths['paths'].append(x)
    update_json(config_file,fnf_paths)
    fnf_paths = get_json_data(config_file)
if args.pc:
    data = get_json_data(config_file)
    for x in data:
        print("Clave: {} Contenido: {}".format(x,data[x]))
if args.fnf != None:
    # Chequeo por si alguna carpeta no tiene el archivo ejecutable o si este no existe
    for x in fnf_paths['paths']:
        files = glob.glob(os.path.join(x,'*.exe'))
        if len(files) > 1:
            choice = terminal(files,titlex="Se han descubierto mas de un archivo ejecutable, elige con cual quedarte")
            if files[choice] not in fnf_paths['executables']:
                fnf_paths['executables'].append(files[choice])
        elif len(files) == 0:
            print("[WARN] Una carpeta vacia encontrada")
            continue
        elif len(files) == 1:
            if files[0] not in fnf_paths['executables']:
                fnf_paths["executables"].append(files[0])
    for x in fnf_paths["executables"]:
        if not os.path.exists(x):
            print("[INFO] Un ejecutable no se encontro, se eliminara la entrada de la configuracion")
            fnf_paths["executables"].remove(x)
    update_json(config_file,fnf_paths)
    try:
        choice = terminal(fnf_paths["executables"], titlex="Elige el ejecutable que quieras iniciar")
        os.system('wine {}'.format(fnf_paths["executables"][choice]))
    except IndexError:
        print("[ERR] Ninguna carpeta o ejecutable encontrado, deberias a;adir carpetas con el argumento -afm")
    
