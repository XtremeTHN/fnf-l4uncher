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
    if len(opts) < 1:
        raise IndexError("debug")
    menu = TerminalMenu(opts, title=titlex)
    return menu.show()

def run(path):
    path = os.path.split(path)
    print(path[1])
    os.system('cd {}; wine {}'.format(path[0], path[1]))

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
        "executables": [],
        "aliases": {}
    }
    with open(config_file,'w') as file:
        json.dump(configs,file,indent=4)
    fnf_paths = get_json_data(config_file)
else:
    fnf_paths = get_json_data(config_file)

parser = argparse.ArgumentParser(description="Friday Night Funkin Launcher")
parser.add_argument('-s','--start',action='store_true', dest='fnf', help="Muestra un menu en donde puedes elegir que mod jugar, solo funciona si has añadido alguna carpeta")
parser.add_argument('-a','--alias',action='store', dest='sel_alias', help="Se usa con -s, sirve para jugar juegos por su alias, antes de utilizarlo debes añadir un alias con --set-alias [alias] [directorio]")
parser.add_argument('-sa','--set-alias',type=str,nargs=2, dest='set_alias', help="Añade un alias al archivo de configuracion, necesita dos argumentos: alias y el directorio")
parser.add_argument('-afm','--add-fnf-mod',action='append', dest='fnf_mod_path', help="Añade un directorio a la lista de busqueda, si hay un archivo ejecutable en la carpeta se añade a la lista que se puede ver con el comando -s")
parser.add_argument('-dfnfp','--download-fnf-psych',action='store_true', dest='down', help="Descarga la version base de psych engine")
parser.add_argument('-pc','--print-config',action='store_true', dest='pc', help="Muestra la configuracion actual")

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
if args.set_alias != None:
    fnf_paths["aliases"][args.set_alias[0]] = args.set_alias[1]
    files = glob.glob(os.path.join(args.set_alias[1],'*.exe'))
    if len(files) > 1:
        choice = terminal(files,titlex="Se han descubierto mas de un archivo ejecutable, elige con cual quedarte")
        fnf_paths['aliases'][args.set_alias[0]] = files[choice]
    elif len(files) == 0:
        print("[WARN] La carpeta esta vacia")
    elif len(files) == 1:
        fnf_paths["aliases"][args.set_alias[0]] = files[0]
    update_json(config_file,fnf_paths)

if args.down:
    import requests, math, zipfile
    from tqdm import tqdm

    url = "https://files.gamebanana.com/mods/psychengine-windows64_a5cff.zip"
    response = requests.get(url, stream=True)

    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024
    wrote = 0
    path = os.path.join(os.getenv('HOME'),'Games','Friday Night Funkin PsychEngine','fnf.bin')
    os.system('mkdir -p ~/Games/Friday\ Night\ Funkin\ PsychEngine')
    """with open(path, "wb") as f:
        for data in tqdm(response.iter_content(block_size), total=math.ceil(total_size//block_size), unit="KB", unit_scale=True, desc="Descargando"):
            wrote = wrote + len(data)
            f.write(data)"""
    with zipfile.ZipFile(path, "r") as zip_ref:
        total_files = len(zip_ref.infolist())
        with tqdm(total=total_files, unit=" archivos") as pbar:
            for file in zip_ref.infolist():
                zip_ref.extract(file, path=os.path.split(path)[0])
                pbar.update(1)

if args.fnf:
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
    if args.sel_alias != None:
        for x in fnf_paths["aliases"]:
            if args.sel_alias != x:
                continue
            else:
                run(fnf_paths["aliases"][x])
                break
        sys.exit(0)

    try:
        print(fnf_paths["executables"])
        choice = terminal(fnf_paths["executables"], titlex="Elige el ejecutable que quieras iniciar")
        run(fnf_paths["executables"][choice])
    except IndexError:
        print("[ERR] Ninguna carpeta o ejecutable encontrado, deberias a;adir carpetas con el argumento -afm")
    
