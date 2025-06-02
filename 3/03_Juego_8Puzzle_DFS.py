import random

OBJETIVO = (1, 2, 3, 4, 5, 6, 7, 8, 0)
MOVS = {'arriba': -3, 'abajo': 3, 'izq': -1, 'der': 1}

def es_resoluble(estado): 
    inversions = 0
    lista = [n for n in estado if n != 0]
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                inversions += 1
    return inversions % 2 == 0

def generar_estado_aleatorio():
    while True:
        estado = tuple(random.sample(range(9), 9))
        if es_resoluble(estado):
            return estado

def funcion_sucesor(estado):
    sucesores = []
    i = estado.index(0)
    for mov, delta in MOVS.items():
        j = i + delta
        if mov == 'arriba' and i >= 3:
            pass
        elif mov == 'abajo' and i < 6:
            pass
        elif mov == 'izq' and i % 3 != 0:
            pass
        elif mov == 'der' and i % 3 != 2:
            pass
        else:
            continue
        nuevo = list(estado)
        nuevo[i], nuevo[j] = nuevo[j], nuevo[i]
        sucesores.append(tuple(nuevo))
    return sucesores

def dfs(inicial):
    pila = [(inicial, [])]
    visitados = set()

    while pila:
        estado, camino = pila.pop()
        if estado == OBJETIVO:
            return camino + [estado]
        if estado in visitados:
            continue
        visitados.add(estado)
        for sucesor in funcion_sucesor(estado):
            if sucesor not in visitados:
                pila.append((sucesor, camino + [estado]))
    return None

# Arce Mendivil Carlos Antonio
# Este codigo fue re-hecho de Java a Python.
estado_inicial = generar_estado_aleatorio()
print("Estado inicial:")
for i in range(0, 9, 3):
    print(estado_inicial[i:i+3])

solucion = dfs(estado_inicial)
if solucion:
    print(f"Pasos a la solución: {len(solucion)-1}")
    for idx, paso in enumerate(solucion):
        print(f"Paso {idx}:")
        for i in range(0, 9, 3):
            print(paso[i:i+3])
        print()
else:
    print("No se encontró solución.")
