import pathlib


class Mobile_phone:

    def __init__(self, id_mobile_phone=0, brand="", model="", os="", memory=0, price=0.0, technology="3G", deal = "SI", photo_path=""):
        self.id_mobile_phone = id_mobile_phone
        self.brand = brand
        self.model = model
        self.os = os
        self.memory = memory
        self.price = price
        self.technology = technology
        self.deal = deal
        self.photo_path = photo_path

    def to_text(self):
        text = "Id: {:d} - Marca: {} - Modelo: {} - Sistema Operativo: {} - Memoria: {:d} - Precio: {:.2f} - Tecnología: {} - En oferta: {}"
        return text.format(self.id_mobile_phone, self.brand, self.model, self.os, self.memory, self.price, self.technology, self.deal)

    def exist_image(self):
        return pathlib.Path(self.photo_path).is_file()