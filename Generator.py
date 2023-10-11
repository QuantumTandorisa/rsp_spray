import random
import string

# Función para generar nombres de usuario aleatorios
def generate_random_username():
    return ''.join(random.choices(string.ascii_lowercase, k=6))  # Genera un nombre de usuario de 6 caracteres aleatorios

# Función para generar contraseñas aleatorias
def generate_random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=12))  # Genera una contraseña de 12 caracteres aleatorios

# Genera 200 nombres de usuario aleatorios
usernames = [generate_random_username() for _ in range(200)]

# Genera 200 contraseñas aleatorias
passwords = [generate_random_password() for _ in range(200)]

# Guarda los nombres de usuario en users.txt
with open("users.txt", "w") as user_file:
    user_file.write('\n'.join(usernames))

# Guarda las contraseñas en passwords.txt
with open("passwords.txt", "w") as password_file:
    password_file.write('\n'.join(passwords))

print("Nombres de usuario y contraseñas generados y guardados en archivos.")