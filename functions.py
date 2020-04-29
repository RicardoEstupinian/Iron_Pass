from simplecrypt import encrypt, decrypt
import subprocess
import binascii
import os.path as path

description = None
sentence = None
key = None
fileName =path.expanduser('~/IRON_PASS.txt') #Obtenemos la ruta del escritorio del usuario

def encryptPass ():
    print('[*-*-*-*-*-INICIANDO PROCESO DE ENCRIPTACION-*-*-*-*-*]')
    # Leer archivo para obtener ultimo # ID
    id=getLastId()

    # Entrada de datos
    description = input('Ingrese de que sitio es la password: ')
    sentence = input('Ingrese la password a  encriptar: ')
    key = input('Ingrese la key que utiliza para encriptar: ')
    encrypt_pass = encrypt(key,sentence) # Se encripta en base a una llave
    passwd = binascii.hexlify(encrypt_pass).decode('utf8')# Se convierte a utf-8 para mejor comprension del resultado
    print(f'Password securizada: {passwd}')

    # Agregar contraseña a TXT
    addPass(id+1,passwd,description)
    print(f'\n\n[*] Verficiar archivo: {fileName}')

    subprocess.call(['sleep','3'])

def decryptPass():
    clearConsole()
    print('[*-*-*-*-*-DESENCRIPTAR PASSWORD-*-*-*-*-*]')
    # Entrada de datos
    id=int(input('Ingrese ID de contraseña a Desencriptar (Ingrese Numero): '))

    # Obtener Password
    passwd_encrypt = getPassById(id)
    if passwd_encrypt==None:
        print('No existe una contraseña con ese ID')
        exit()
    key = input('Ingrese la key que utiliza para encriptar: ')

    #Desencriptar Password
    encrypt=binascii.unhexlify(passwd_encrypt.strip())
    sentence = decrypt(key,encrypt)
    clearConsole()

    print('Tendras 4s antes que desaparezca')
    print(f'PASSWD : {sentence.decode("utf-8")}')
    subprocess.call(['sleep','4']) # Hace un delay de 4 segundos, se pasa como arreglo los comandos que tienen mas de un argumento


def clearConsole():
    subprocess.call('clear') # Se limpia consola

def verifyExist():
    if path.exists(fileName):
        return True
    else:
        return False

def getLastId():
    id=0
    if verifyExist():
        file = open(fileName,'r')
        # Recorrer linea por linea el archivo txt para obtener el utlimo ID
        for line in file:
            if 'ID' in line: # Se verifica que en la linea se encuentra la subcadena ID
                id=int(line.split(':')[1]) # Se convierte numero la posicion 0 del array que genera el split [ID,numero]

    return id

def getPassById(idPass):
    passwd = None
    flag = False
    if verifyExist():
        file = open(fileName,'r')
        # Buscar Pass segun ID
        for line in file:
            if 'ID:'+str(idPass) in line: # Se verifica que en la linea se encuentra la subcadena ID:numeroID
                flag = True # Si lo encuentra pone la bandera en True lo que significa que la siguiente coincidencia Pass: sera la password a recuperar
            if 'Pass:' in line and flag :
                passwd = line.split(':')[1]
                return passwd
        return passwd
    else:
        return passwd

def addPass(idPass,passwd,desc):
    file = open(fileName,'a')
    file.write(f'\n\nID:{idPass}\nDescripcion: {desc}\nPass:{passwd}')
    file.close()

def getList():
    text = ''
    str = ''
    file = open(fileName,'r')
    for line in file:
        if 'ID' in line:
            str = line
        if 'Descripcion:' in line:
            text = str + line
            print(f'{text}')
