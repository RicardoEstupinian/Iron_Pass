from functions import *

def menu ():
    clearConsole()
    print('Bienvenido Ing.Ricardo Estupinian\n[*] Menu de Opciones')
    print('\n[1] Agregar una nueva password')
    print('\n[2] Obtener password')
    print('\n[3] Mostrar ID\'s')
    print('\n[4] Salir')

    # Ingreso de opcion a seleccionar
    flag = int(input('\nIngrese Opcion del Menu: '))

    #Opciones
    if flag == 1:
        clearConsole()
        encryptPass()
        menu()
    elif flag == 2 :
        clearConsole()
        decryptPass()
        menu()
    elif flag == 3 :
        getList()
    elif flag == 4 :
        print('Nos vemos pronto.')
    else :
        print('Seleccione opcion valida')
