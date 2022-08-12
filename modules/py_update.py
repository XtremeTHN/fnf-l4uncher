import requests, os, sys

class pyupdate:
    def check_updates(version, url):
        ver = requests.get(url[0])
        if float(ver.content) > current_version:
            return True
        else:
            return False
    def update(version, url):
        print("Descargando...")
        updated_files = requests.get(url[0])
        return updated_files.content

if __name__ == "__main__":
    obj = open('version.py','w+b').write(pyupdate.update(1.0, url = ["https://raw.githubusercontent.com/XtremeTHN/fnf-l4uncher/main/updates/version.py"]))
