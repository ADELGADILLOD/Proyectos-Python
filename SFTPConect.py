import paramiko
import time

def SFTPC(hostname: str, username: str, password: str, reconection_time: int = 2) -> [None]:
    while True:
        try:
            cliente = paramiko.SSHClient()
            cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            cliente.connect(hostname = hostname,
                    username = username,
                    password = password,
                    allow_agent = False, 
                    look_for_keys = False)
            return cliente
        except paramiko.AuthenticationException as e:
            print(f'{e}\nSe volverá a interntar la conexión en {reconection_time} minutos.')
            time.sleep({reconection_time}*60)

def SFTPD(origin_path: str, dest_path: str, cliente, reconection_time: int = 2):
    while True:
        try:
            sftp = cliente.open_sftp()
            sftp.get(origin_path,
                    dest_path)
            sftp.close()
            break
        except paramiko.AuthenticationException as e:
            print(f'{e}\nSe volverá a interntar la conexión en {reconection_time} minutos.')
            time.sleep({reconection_time}*60)