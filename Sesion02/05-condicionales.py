#condicional if else
edad = 30
edad_minima = 18

if edad >= edad_minima:
    print('1')
else:
    print('2')


#Tengo el siguiente numero
numero = 10
#como saber si es par o impar
operacion = numero % 2
#luego de haber hecho con el if hacer el uso del operador ternario
resultado = 'par' if operacion == 0 else 'impar'
print(resultado)

persona={
    'nombre':'Raul',
    'nacionalidad':'Boliviana',
    'sexo':'M'
}
#vALIDAR SI LA PERSONA ES rAUL Y ES PERUANA
if persona['nombre']=='Raul' and persona['nacionalidad']=='Peruana':
    print('Si, La persona es ' + persona['nombre'] + ' y su nacionalidad es ' + persona['nacionalidad'])
else:
    print('No, La persona es ' + persona['nombre'] + ' y su nacionalidad es ' + persona['nacionalidad'])