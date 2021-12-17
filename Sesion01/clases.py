class Persona:
    # variables > atributos
    #nombre = ''
    #edad = 0
    #estatura = 0.0

    # function > metodo
    def saludar():
        print('Hola')

    # contrsuctor > es el encargado de iniciarlizar los atributos de la clase
    def __init__(self, nombre_de_la_persona, edad_persona, estaturoa_persona):
        self.nombre = nombre_de_la_persona
        self.edad = edad_persona
        self.estatura = estaturoa_persona
        self.sexo = 'NS/NO'

eduardo = Persona(nombre = 'Eduardo', edad = 20, estatura =1.89)
eduardo.nombre = 'Eduardo'
eduardo = 25
eduardo.saludar()

