import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from ventanas import ventana_inicio, ventana_registrar, ventana_listado_text, ventana_listado_list
from ventanas import ventana_listado_table


class Aplicacion(QMainWindow):
    def __init__(self):
        super().__init__()
        # Se crean las ventanas.
        self.ventana_inicio = ventana_inicio.Ui_MainWindow()
        self.ventana_registrar = ventana_registrar.Ui_MainWindow()
        self.ventana_listado_text = ventana_listado_text.Ui_MainWindow()
        self.ventana_listado_listwidget = ventana_listado_list.Ui_MainWindow()
        self.ventana_listado_tablewidget = ventana_listado_table.Ui_MainWindow()
        self.ventana_inicio.setupUi(self)
        self.ventana_inicio.menu_registrar.triggered.connect(self.mostrar_registrar)
        self.ventana_inicio.menu_listar_text.triggered.connect(self.mostrar_listar_text)
        self.ventana_inicio.menu_listar_list.triggered.connect(self.mostrar_listar_list)
        self.ventana_inicio.menu_listar_table.triggered.connect(self.mostrar_listar_table)
        self.ventana_inicio.menu_salir.triggered.connect(lambda: sys.exit())

        self.show()

    def preparar_menu(self, ventana):
        ventana.menu_registrar.triggered.connect(self.mostrar_registrar)
        ventana.menu_listar_text.triggered.connect(self.mostrar_listar_text)
        ventana.menu_listar_list.triggered.connect(self.mostrar_listar_list)
        ventana.menu_listar_table.triggered.connect(self.mostrar_listar_table)
        ventana.menu_salir.triggered.connect(lambda: sys.exit())

    def mostrar_registrar(self):
        self.ventana_registrar.setupUi(self)
        self.preparar_menu(self.ventana_registrar)

    def mostrar_listar_text(self):
        self.ventana_listado_text.setupUi(self)
        self.preparar_menu(self.ventana_listado_text)

    def mostrar_listar_list(self):
        self.ventana_listado_listwidget.setupUi(self)
        self.preparar_menu(self.ventana_listado_listwidget)

    def mostrar_listar_table(self):
        self.ventana_listado_tablewidget.setupUi(self)
        self.preparar_menu(self.ventana_listado_tablewidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Aplicacion()
    ventana.show()

    sys.exit(app.exec())