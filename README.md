Esta es una herramienta simple en Python que realiza un ataque de "spray" contra un servidor de Protocolo de Escritorio Remoto (RDP) utilizando combinaciones de nombres de usuario y contraseñas proporcionadas en archivos de texto.

## Requisitos

- [xfreerdp](https://github.com/FreeRDP/FreeRDP) - Asegúrate de tener esta aplicación instalada en tu sistema. Se utiliza para la conexión RDP.

## Uso

- Ejecuta el script Generator.py
- El script generará nombres de usuario y contraseñas aleatorios y los guardará en los archivos `users.txt` y `passwords.txt`. Puedes ajustar la cantidad y complejidad de las credenciales generadas modificando el código fuente.

## RDP

- Luego ejecuta el programa con Python y proporciona la dirección IP o nombre del servidor RDP al que deseas realizar intentos de inicio de sesión.

- Ejemplo:

- `python rdp_spray.py --target {IP}`

- Reemplaza `{IP}` con la dirección IP o nombre del servidor RDP de destino.

- A medida que el programa se ejecuta, verás los resultados en la terminal. La herramienta intentará iniciar sesión con todas las combinaciones de usuario y contraseña en `users.txt` y `passwords.txt`.

## OWA

- Ejecuta el programa con Python y proporciona la URL del servidor OWA al que deseas realizar intentos de inicio de sesión.

- Ejemplo:

- `python owa_spray.py --url https://owa.example.com`

- A medida que el programa se ejecuta, verás los resultados en la terminal. La herramienta intentará iniciar sesión con todas las combinaciones de usuario y contraseña en `users.txt` y `passwords.txt`.

## Resultados

- El programa mostrará mensajes que indican si los intentos de inicio de sesión fueron exitosos o fallidos para cada combinación.

- Puedes personalizar los archivos `users.txt` y `passwords.txt` con tus propias combinaciones de usuario y contraseña.

## Nota

- Este código "Basico modificable" lo comparto solo con fines educativos y de demostración. Asegúrate de usarlo de manera ética y en entornos autorizados.
