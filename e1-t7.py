# En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: sumar, restar, multiplicar y dividir.
# Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.
from calculadora import *

print( dir( operaciones ) )

def main() :
    number_1 = 5
    number_2 = 4

    print( 'Calcular usando un modulo' )
    result = operaciones.sumar( number_1, number_2 )
    print( f' - { number_1 } + { number_2 } = { result }' )
    result = operaciones.restar( number_1, number_2 )
    print( f' - { number_1 } - { number_2 } = { result }' )
    result = operaciones.multiplicar( number_1, number_2 )
    print( f' - { number_1 } * { number_2 } = { result }' )
    result = operaciones.dividir( number_1, number_2 )
    print( f' - { number_1 } / { number_2 } = { result }' )

if __name__ == '__main__' :
    main()