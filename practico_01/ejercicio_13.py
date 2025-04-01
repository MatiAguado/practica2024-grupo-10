"""Clousures, Generadores, Generadores Delegados

Esta guia muestra uno de los patrones avanzados de programación para evitar
el uso de variables globales. El método descripto se llama closure y consiste
en vincular una función con datos que persistan luego de la ejecución, sin
recurrir a variables globales. Esto se hace mediante la declaración de una
función dentro de otra y permite comportamiento que sería imposible lograr de
otra manera.
"""


from typing import Iterator, Callable


def generar_pares_clousure(initial: int = 0) -> Callable[[], int]:
    """Toma un número inicial y devuelve una función que cada vez que es
    invocada devuelve el número par siguiente al devuelto la última vez que
    fue invocada.

    Restricciones:
        - Usar closures
        - Usar el modificador nonlocal
    """

    # Esta variable guardara el ultimo nro iterado
    ultimo = initial
    def generar_pares():
        # nonlocal para manipular la variable externa a generar_pares
        nonlocal ultimo
        # Para la primera invocacion, devolvemos initial si es par
        # Pero tambien aumentamos el valor de ultimo para la prox iteracion
        if ultimo==initial and initial % 2 == 0:
            ultimo +=2
            return initial
        # Si es la primer invocacion, e initial no es par, devolvemos el siguiente par
        elif ultimo == initial:
            ultimo +=1
            return ultimo
        # En las iteraciones que siguen, ya habran numeros pares, asi que 
        # siempre sumaremos 2 respecto al ultimo
        else:
            ant = ultimo
            ultimo+=2
            return ant

    return generar_pares
    pass # Completar


# NO MODIFICAR - INICIO
generador_pares = generar_pares_clousure(0)
assert generador_pares() == 0
assert generador_pares() == 2
assert generador_pares() == 4
# NO MODIFICAR - FIN


###############################################################################


"""Este tipo de comportamiento es conocido com semi-corutina, las semi-corutinas
en Python son llamadas funciones generadoras y se caracterizan por utilizar el
yield en lugar del return.
"""


def generar_pares_generator(initial: int = 0) -> Iterator[int]:
    """Re-Escribir utilizando Generadores
    Referencia: https://docs.python.org/3/howto/functional.html?highlight=generator#generators
    """
     # Seteamos la primer variable
    i = initial if initial % 2 == 0 else initial + 1

    # Y esto es lo que se ejecutara siempre. yield funciona como el return, pero guardande el valor de i para la prox iteracion
    # Se puede aumentar el valor de i despues del yield
    while True:
        yield i 
        i+=2
    pass # Completar

    


# NO MODIFICAR - INICIO
generador_pares = generar_pares_generator()
assert next(generador_pares) == 0
assert next(generador_pares) == 2
assert next(generador_pares) == 4
# NO MODIFICAR - FIN


###############################################################################


def generar_pares_generator_send(initial: int = 0) -> Iterator[int]:
    """CHALLENGE OPCIONAL: Re-Escribir utilizando send para saltear numeros"""
    # Seteamos la primer variable, igual que antes
    i = initial if initial % 2 == 0 else initial + 1

    # Y esto es lo que se ejecutara siempre. yield funciona como el return, pero guardande el valor de i para la prox iteracion
    # Se puede aumentar el valor de i despues del yield
    while True:
        # valor_enviado es el valor que habria si se usa .send(value)
        valor_enviado = (yield i)

        # Si hay valor enviado, lo devolvemos si es par, sino devolvemos el siguiente
        if valor_enviado is not None:
            i = valor_enviado if valor_enviado % 2 == 0 else valor_enviado + 1
        # Si no hay valor enviado, devolvemos el siguiente par
        else:
            i+=2

    pass # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    generador_pares = generar_pares_generator_send()
    assert next(generador_pares) == 0
    assert next(generador_pares) == 2
    assert next(generador_pares) == 4
    assert generador_pares.send(10) == 10
    assert next(generador_pares) == 12
    assert next(generador_pares) == 14
    assert next(generador_pares) == 16
# NO MODIFICAR - FIN


###############################################################################


def generar_pares_delegados(initial: int = 0) -> Iterator[int]:
    """CHALLENGE OPCIONAL: Re-Escribir utilizando Generadores delegados (yield from)"""    
    pass # Completar


# NO MODIFICAR - INICIO
if __name__ == "__main__":
    generador_pares = generar_pares_delegados()
    assert next(generador_pares) == 0
    assert next(generador_pares) == 2
    assert next(generador_pares) == 4
# NO MODIFICAR - FIN
