# escucharTweets
Script Python para escuchar un hashtag twitter y guardarlo en json


Para utilizarlo en Windows se necesita lo siguiente
-Visual Studio Code
-Python 3: Ir a https://www.python.org/downloads/windows/ elegir el instalador para version 3.5 "Windows x86-64 web-based installer" y hacer la instalacion siguiendo el asistente. Elegir que se agregue python.exe al PATH.
-pip: ir a cmd y ejecutar lo siguiente:  python -m pip install -U pip
-tweepy: ejecutar lo siguiente: python -m pip install -U tweepy
-PyQt5: ejecutar lo siguiente: python -m pip install -U PyQt5
-pywin32: ir a https://sourceforge.net/projects/pywin32/files/pywin32/ e instalar el complemento para la version de python utilizada (python 3.6 64 bits en este caso)

Para ejecutar el programa:
- Descargar el repositorio Git como zip desde https://github.com/pepeleproso/escucharTweets botón "clone or download"
- Descomprimir en c:\escucharTweets
- Ejecutar cmd
- Ejecutar "cd c:\escucharTweets"
- Configurar el programa abriendo escucharTweets.json y cargando los datos (credenciales de tweeter y hashtags a buscar)
- Ejecutar "python escuchar_tweets.py -vvv"

Para Generar un .exe con Pyinstaller:

- python -m pip install -U PyInstaller
- instalar msvc100.dll > https://support.microsoft.com/en-us/kb/2977003
- Ir a C:/escucharTweets y ejecutar pyinstaller -F escuchar_tweets.py
- ir a dist y agregar el archivo escucharTweets.json
- Ahora se ejecuta el .exe desde la consola y listo


Para Usarlo:
1- Python 3: Ir a https://www.python.org/downloads/windows/ elegir el instalador para version 3.5 "Windows x86-64 web-based installer" y hacer la instalacion siguiendo el asistente. Elegir que se agregue python.exe al PATH.
2- pywin32: ir a https://sourceforge.net/projects/pywin32/files/pywin32/ e instalar el complemento para la version de python utilizada (python 3.5 64 bits en este caso)
3- Ir a la carpeta escucharTweets
4- ejecutar EscucharTweets.bat





