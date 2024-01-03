import re
import os
from typing import List, Union

def create_config():
    f = open('config.txt', "a")
    f.write('SFTP Config:\n' +
            '\thostname = \n' +
            '\tusername = \n' +
            '\tpassword = \n\t' +
            r'origin_path = ' +
            '\n\torigin_name = \n\t' +
            r'dest_path = ' +
            '\n\tdest_name = \n' +
        'Google Drive Config:\n\t' +
            r'service_account_info_path = ' +
            '\n\tservice_account_info_name = \n' +
            '\tfolder_id = \n' +
        'Google Drive Load Data:\n\t' +
            r'local_folder_path = ' +
        '\nLog Config:\n\t' +
            r'output_log_path = ' +
            '\n\toutput_log_name = \n' +
        'Update time:\n' +
            '\tseconds = 0\n' +
            '\tminutes = 5\n' +
            '\thours = 0\n' +
        'Config App:\n' +
            '\tswitch_off = \n'+
            '\tallowed_extensions = ')
    
def config(tipoConfig: str, list_ = False) -> Union[str, List[str], None]:
    if not os.path.exists('config.txt'): 
        create_config()
        input('Introduce tu configuración en el archivo, después, presiona enter:')
    with open('config.txt', 'r') as archivo:
        for linea in archivo:
            if tipoConfig in linea and not list_: return linea.split(' = ')[1].strip()
            if tipoConfig in linea and list_: return re.split(';', linea.split(' = ')[1].strip())
            
def completePath(path: str, name: str, val = True):
    if not val: return os.path.join(config(path), config(name))
    while True:
        if os.path.exists(config(path)) or config(path) == '': 
            if os.path.exists(config(name)): 
                if os.path.exists(os.path.join(config(path), config(name))): return os.path.join(config(path), config(name))
                else: print (f'La ruta {config(path)}{config(name)} no existe,cambia la dirección en el archivo config.txt ')
            else: print (f'El archivo {config(name)} no existe, cambia la dirección en el archivo config.txt')
        else: print (f'La dirección {config(path)} no existe, cambia la dirección en el archivo config.txt')
        input()