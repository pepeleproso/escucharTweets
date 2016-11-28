# escucharTweets
Script Python para escuchar un hashtag twitter y guardarlo en json


Para utilizarlo en Windows se necesita lo siguiente

-Python 2: Ir a https://www.python.org/downloads/release/python-2712/ elegir el instalador msi y hacer la instalacion siguiendo el asistente. Elegir que se agregue python.exe al PATH.
-pip: ir a cmd y ejecutar lo siguiente:  python -m pip install -U pip
-tweepy: ejecutar lo siguiente: python -m pip install -U tweepy
-pywin32: ir a https://sourceforge.net/projects/pywin32/files/pywin32/ e instalar el complemento para la version de python utilizada (python 2.7 en este caso)

Para ejecutar el programa:
- Descargar el repositorio Git como zip desde https://github.com/pepeleproso/escucharTweets botón "clone or download"
- Descomprimir en c:\escucharTweets
- Ejecutar cmd
- Ejecutar "cd c:\escucharTweets"
- Configurar el programa abriendo escucharTweets.json y cargando los datos (credenciales de tweeter y hashtags a buscar)
- Ejecutar "python escucharTweets.py"



Para Generar un .exe con Pyinstaller:

- python -m pip install -U PyInstaller
- instalar msvc100.dll > https://support.microsoft.com/en-us/kb/2977003
- Ir a C:/escucharTweets y ejecutar pyinstaller -F escucharTweets.py
- ir a dist y agregar el archivo escucharTweets.json
- Ahora se ejecuta el .exe desde la consola y listo
