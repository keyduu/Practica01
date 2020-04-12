class Mobile_phone:
    
    def __init__(self, id_mobile_phone=0, brand="", model="", os="", memory=0, price=0.0):
        self.brand = brand
        self.model = model
        self.os = os
        self.memory = memory
        self.price = price
        self.id_mobile_phone = id_mobile_phone
        
    def to_text(self):
        text = "Id: {:d} - Marca: {} - Modelo: {} - Sistema Operativo: {} - Memoria: {:d} - Precio: {:.2f}"
        return text.format(self.id_mobile_phone, self.brand, self.model, self.os, self.memory, self.price)
