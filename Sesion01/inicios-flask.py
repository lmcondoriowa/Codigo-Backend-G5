from flask import Flask

# en python tenemos varias variables que son de uso propio de python no podemos modificar ni alterar
# esta variable sirve para indicar si estamos en el archivo principal del proyecto

ejemplo = Flask(__name__)

ejemplo.run()
