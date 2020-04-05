import sys

from PyQt5.QtWidgets import QApplication

from clases.aplicacion import Aplicacion

app = QApplication(sys.argv)
ventana = Aplicacion()
ventana.show()

sys.exit(app.exec())
