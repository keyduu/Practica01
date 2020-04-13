import sys

from PyQt5.QtWidgets import QApplication

from classes.application import Application

app = QApplication(sys.argv)
ventana = Application()
ventana.show()

sys.exit(app.exec())
