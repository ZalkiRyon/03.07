import random

diccionario = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4
}

def numeroRandom(min = 100, max = 200):
    valor = random.randint(min, max)
    return valor

def actualizarDiccionario(diccionario):
    for key in diccionario:
        diccionario[key] = numeroRandom()
    

actualizarDiccionario(diccionario)
print(diccionario)


