import requests, os, sys

class updatelib:
    def check_updates(version, url):
        if isinstance(url, str) and isinstance(version, float):
            ver = requests.get(url)
            if float(ver.content) > version:
                return True
            else:
                return False
        else:
            raise TypeError("String and float class expected, {} and {} was given".format(type(url), type(version)))
    def update(files):
        if isinstance(url, dict):
            try:
                for x in files:
                    updated_files = requests.get(files[x])
                    with open("modules/" + x, 'w+b') as file:
                        file.write(updated_files.content)

            except:
                print(sys.exc_info()[0], sys.exc_info()[1])
                sys.exit(1)
        else:
            raise TypeError("Dict class expected, {} was given".format(type(url)))

        def get_dict_of_files(url):
        if isinstance(url, str):
            print("Comprobando actualizaciones...")
            updated_files = requests.get(url)
            return updated_files.content
        else:
            raise TypeError("String class expected, {} was given".format(type(url)))