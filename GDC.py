from googleapiclient.http import MediaFileUpload
import os
import json
import logging
from google.oauth2 import service_account

def credentials(service_account_info_path: str):
    SCOPES = ['https://www.googleapis.com/auth/drive']
    with open(service_account_info_path) as f: service_account_info = json.load(f)
    return service_account.Credentials.from_service_account_info(service_account_info, scopes=SCOPES)

def delete_files_in_folder(service, folder_id):
    
    page_token = None

    while True:
        results = service.files().list(
            q=f"'{folder_id}' in parents",
            fields="nextPageToken, files(id, name)",
            pageToken=page_token
        ).execute()

        files = results.get('files', [])
        if not files:
            logging.info('No files found in the folder.')
            break

        logging.info('Deleting files...')
        for file in files:
            try:
                service.files().delete(fileId=file['id']).execute()
                logging.info(f'Deleted: {file["name"]} {file["id"]}')
            except Exception as e:
                logging.error(f'An error occurred: {e}')

        page_token = results.get('nextPageToken')
        if not page_token: break

def list_files_in_folder(service, folder_id):
    results = service.files().list(q=f"'{folder_id}' in parents", fields="files(name)").execute()
    files = results.get('files', [])
    return [file['name'] for file in files]

def upload_files_from_folder(local_folder_path, folder_id, service, allowed_extensions: list):
    existing_files = list_files_in_folder(service, folder_id)

    for root, dirs, files in os.walk(local_folder_path):
        for file_name in files:
            _, file_extension = os.path.splitext(file_name)
            if file_extension.lower() in allowed_extensions:
                if file_name not in existing_files:
                    file_path = os.path.join(root, file_name)
                    media = MediaFileUpload(file_path, resumable=True)
                    file_metadata = {
                        'name': file_name,
                        'parents': [folder_id]
                    }

                    try:
                        logging.info(f'Intentando subir {file_name}')
                        file = service.files().create(body = file_metadata, media_body = media, fields='id, name').execute()
                        logging.info(f'Archivo ID: {file_name} {file.get("id")}')
                    except Exception as e: logging.error(f'Error al subir el archivo {file_name}: {e}')
                else: logging.warning(f'El archivo {file_name} ya existe en la carpeta y no será subido.')
            else: logging.warning(f'El archivo {file_name} tiene una extensión no permitida y no será subido a Google Drive.')