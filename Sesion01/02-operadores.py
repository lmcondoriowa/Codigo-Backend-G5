# Operadores aritmeticos
# Suma, resta, multiplicacion, division, exponente, cociente, modulo

numero1 = 10
numero2 = 30

resultado = numero1 + numero2
print(resultado)
print('El resultado es: ', resultado)
print('El resultado es {} y nada mas'.format(resultado))
print(f'El resultado es {resultado}')
print('El resultado es {0} y nada mas'.format(resultado))

resultado = numero1 - numero2
resultado = numero1 * numero2
resultado = numero1 / numero2

print('{:.1f}'.format(resultado))
print(f'{resultado:.1f}')

# el modulo
resultado = numero1 % numero2
print('El modeulo es : ', resultado)


# el cociente
resultado = numero1 // numero2
print('El cociente es : ', resultado)


texto = "Hola mi nombre es Luis"
print(texto[:5])
print(texto)