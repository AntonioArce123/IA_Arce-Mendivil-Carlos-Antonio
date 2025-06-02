class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.relaciones = []

    def agregar_relacion(self, tipo_relacion, otro_nodo):
        self.relaciones.append((tipo_relacion, otro_nodo))

    def mostrar_relaciones(self):
        for tipo, nodo in self.relaciones:
            print(f"{self.nombre} --{tipo}--> {nodo.nombre}")


animal = Nodo("Animal")
perro = Nodo("Perro")
gato = Nodo("Gato")
mamifero = Nodo("Mamífero")
canino = Nodo("Canino")
felino = Nodo("Felino")

perro.agregar_relacion("es_un", canino)
gato.agregar_relacion("es_un", felino)
canino.agregar_relacion("es_un", mamifero)
felino.agregar_relacion("es_un", mamifero)
mamifero.agregar_relacion("es_un", animal)

print("Red Semántica:")
for nodo in [perro, gato, canino, felino, mamifero, animal]:
    nodo.mostrar_relaciones()
