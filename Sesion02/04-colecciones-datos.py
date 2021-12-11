# Listas
dias = ['Lunes','Martes','Miercoles']

# metodo para agregar un nuevo valor
dias.append('Jueves')

print(dias)
# metodo para eliminar un valor de la lista
dias.remove('Martes')
print(dias)
dias.clear()
print(dias)

# Variables Mutables / Inmutables
lista1 = [1,2,3,4,5]

lista2 = lista1

# Tuplas
# Coleccion se parece a una lista pero la tupla no se puede modificar sus valores una vez creadas
alumnos=('Luis','Ana','Pedro')
# se usa para almacenar algunos valores que nunca va a cambiar su contenido
CONFIGURACION=(
    {
        'Nombre':'API_KEY',
        'Valor':'xxx.xxx.xxx'
    },
    {
        'Nombre':'Sengrid',
        'Valor':'dsfksdfjsd'
    }
)
CONFIGURACION=('SDFAFA','SDEWRWEREW','FGHFGHFGH')
# Si una tupla internamente itene otra posicion de datos que si se puede modificar entonces normas se podra cambiar su valor, sin embrago si tiene algin tipo de datos primitivo ahi si entrara a tallar las propiedades de la tupla que mo se íedem p,dofocar sis vañpres
#alumnos[0]='Juan'
#CONFIGURACION[0]='xd'
print(CONFIGURACION[0])
PRINT(CONFIGURACION)

#DICCIONARIOS
persona = {
    'nombre':'Luis',
    'correo':'lmcondori@outlook'
}
persona['estatura']='1.95'
#CONJUNTOS
#Es la unica coleccion de datos desordenadas
colores={'rojo','verde'}

#para agregar nuevos valores al conjunto
colores.add('mostaza')
print(colores[0])