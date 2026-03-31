"""
Ejercicio 2:
Dado un número entero positivo N, retornar la suma de los primeros N números.

Debe implementar:
- suma_ciclo(n)
- suma_recursiva(n)
"""

def suma_ciclo(n):
    """
    Retorna la suma de los primeros n números usando un ciclo.
    """
    for i in range(n):
        acomulador= acomulador+i
    
    return acomulador

def suma_recursiva(n):
    """
    Retorna la suma de los primeros n números usando recursividad.
    """
    return n+suma_recursiva(n-1)
