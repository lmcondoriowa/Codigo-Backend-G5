# variable numerica
numero = 10
numero2 = 10.5

numero = "Febrero"

# variables de texto  o string
nombre = "Luis"
apellido = "Condori"
html = '''
'''

html = """
"""

fecha = 0

print('hola :)')

print(type(nombre))
#str = string
# int = integer
#float = float
print(type(numero))
print(type(numero2))
#bool = boolean

soltero = True
calor=False
print(type(soltero))

# VARIABLES que tienen varios VALORES
# ARREGLOS > LISTAS LIST
edades = [ 10, 12 ,40 , 'Luis', 15.1, False]
print(edades[1:20])

# JSON (JavaScript Object Notation) | Diccionario
curso = {
    'nombre': 'Backend',
    'nombre': 'Frontend',
    'dificultad': 'Dificil',
    'skills': [
        {
            'nombre':'Base de Datos',
            'nivel':'Intermedio'
        },
        {
            'nombre':'ORM',
            'nivel':'Avanzado'
        }
    ]
}

print(curso['dificultad'])

# quiero el nivel del skill ORM
print(curso['skills'][1]['nivel'])

personas = [{
    'nombre': 'Eduardo',
    'nacionalidad': 'peruano',
    'hobbies':[
        {
            'nombre': 'Volar drones',
            'experiencia': '2 años'
        },{
            'nombre':'Programar',
            'experiencia': '1 mes'
        }
    ]
},{
    'nombre': 'Juliana',
    'nacionalidad': 'colombiana',
    'hobbies':[
        {
            'nombre': 'Montar bici',
            'experiencia': '4 años'
        },{
            'nombre':'Bases de datos',
            'experiencia': '8 mes'
        }
    ]
}]

# nacionalidad de la primera persona
print(personas[0]['nacionalidad'])

# los hobbies de la segunda persona
print(personas[1]['hobbies'])

# la experiencia del segundo hobbie de la primera persona
print(personas[0]['hobbies'][1]['experiencia'])