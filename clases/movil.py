class Movil:
    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.sistema_operativo = ""
        self.memoria = 0
        self.precio = 0.0
        self.id = 0

    def a_texto(self):
        texto = "Id: {:d} - Marca: {} - Modelo: {} - Sistema Operativo: {} - Memoria: {:d} - Precio: {:.2f}"
        texto.format(self.id, self.marca, self.modelo, self.sistema_operativo, self.memoria, self.precio)
        return texto
