from __future__ import print_function
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from configtxt import config, completePath
import SFTPConect as SFTP
import GDC
import os
import time

def __main__(creds,
            local_folder_path = config('local_folder_path'),
            folder_id = config('folder_id')
            ):

    service = build('drive', 'v3', credentials=creds)

    os.system('cls')
    
    SFTP.SFTPD(origin_path = config('origin_path') + config('origin_name'),
            dest_path = completePath('dest_path', 'dest_name', val = False),
            cliente = SFTP.SFTPC(hostname = config('hostname'),
                                username = config('username'),
                                password = config('password')))
    GDC.delete_files_in_folder(service, folder_id)
    GDC.upload_files_from_folder(local_folder_path, folder_id, service, config('allowed_extensions', list_ = True))

while config('switch_off') != 'True':
    seconds = int(config('seconds'))
    minutes = int(config('minutes'))
    hours = int(config('hours'))
    GDC.credentials(completePath('service_account_info_path', 'service_account_info_name'))
    __main__(GDC.credentials(completePath('service_account_info_path', 'service_account_info_name')))
    print(f'Proxima validación de actualización: {datetime.now() + timedelta(seconds = seconds, minutes = minutes, hours = hours)}')
    print('Puedes cambiar la configuración antes de la proxima actualización')
    time.sleep(seconds + minutes*60 + hours*60*60)