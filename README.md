# Iron_Pass
## By Ricardo Estupinian
Script python sencillo y fácil de utilizar, para encriptar y desencriptar constraseñas, que se almacenan en un archivo de texto local. 
**Nota**: Probado unicamente en Debian 10 utilizando Python 3.

**Proposito**: Ayuda a mantener nuestras contraseñas de manera segura en nuestro computador local, y solo es necesario tener una contraseña global que es la llave de encriptacion para poder acceder a todas las contraseñas almacenadas en el archivo de texto. Es de gran ayuda cuando se tienen varias cuentas de sitios con diferentes contraseñas. (Personas que olvidan todo :v)

### Documentacion:

 [ \- ] Se instalo el modulo simplecrypt usando el comando: pip3 install simple-crypt
 
 [ \- ] Se importo la libreria subprocess para ejecutar comandos bash desde python.
 
 [ \- ] El modulo que se utiliza para convertir de bytes(binario) a UTF-8 ya se encontraba instalada junto con python3 en Debian 10 (Nombre del modulo: binascii) de no estar disponible instalarlo.
 
### Instalacion
1. Clonamos el repositorio: `git clone https://github.com/RicardoEstupinian/Iron_Pass.git`
2. Instalamos simplecrypt `pip3 install simple-crypt`, para esto se requiere tener instalado PIP 3
3. Ya puede ser utilizado.

**Nota**: Si surge algun problema en la ejecucion del programa verificar si se tiene instalado binascii.

### Pasos para utilizarlo
1. Entrar a la carpeta del proyecto clonado.
2. Ejecutar: `python3 main.py`
3. Se desplegara el menu de opciones siguiente: 

  ```Bienvenido Ing.Ricardo Estupinian
  
  [*] Menu de Opciones

  [1] Agregar una nueva password

  [2] Obtener password

  [3] Mostrar ID's

  [4] Salir

  Ingrese Opcion del Menu:
  ```
**Agregar nueva contraseña**

Ejemplo de registro de una nueva contraseña: 
```
[*-*-*-*-*-INICIANDO PROCESO DE ENCRIPTACION-*-*-*-*-*]
Ingrese de que sitio es la password: Contraseña del correo pruebita@dominio.com
Ingrese la password a  encriptar: contraseñaDeCorreo
Ingrese la key que utiliza para encriptar: key_de_encriptacion

Password securizada: 73630002795898fb34fdec7ba01ab868058f96a242c6d6f482c7350131162c0ecfb3e8d1f0c6537f139460f6d898a5b115e07d5578b7286da052cd810c5df5a26f03d5e461


[*] Verficiar archivo: ~/IRON_PASS.txt

```
**Obtener Password segun ID**
```
[*-*-*-*-*-DESENCRIPTAR PASSWORD-*-*-*-*-*]
Ingrese ID de contraseña a Desencriptar (Ingrese Numero): 1
Ingrese la key que utiliza para encriptar: key_de_encriptacion

Tendras 4s antes que desaparezca
PASSWD : contraseñaDeCorreo

```
**Nota**: Por el momento si escribe una llave incorrecta enviara error de python: Bad Password or Corrupt. Falta mostrar mensaje mas amigable al usuario :v


