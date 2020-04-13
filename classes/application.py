import sys
from classes.mobile_phone import Mobile_phone
from functions import validations
from ui import window_update, window_start, window_register, window_list_with_tablewidget, window_list, \
    window_list_with_listwidget
from database import sql_operations
from PyQt5.Qt import QTableWidgetItem, QMainWindow, QApplication, QMessageBox
from _functools import partial


class Application(QMainWindow):

    def __init__(self):
        super().__init__()
        # Se crean las ventanas.
        self.window_start = window_start.Ui_window_start()
        self.window_register = window_register.Ui_window_register()
        self.window_list = window_list.Ui_window_list()
        self.window_list_with_listwidget = window_list_with_listwidget.Ui_window_list_with_listwidget()
        self.window_list_with_tablewidget = window_list_with_tablewidget.Ui_window_list_with_tablewidget()
        self.window_update = window_update.Ui_window_update()

        self.show_window_start()

        self.show()
        return

    def show_window_start(self):
        self.window_start.setupUi(self)
        self.window_start.menu_register.triggered.connect(self.show_window_register)
        self.window_start.menu_list.triggered.connect(self.show_window_list)
        self.window_start.menu_list_with_listwidget.triggered.connect(self.show_window_list_with_listwidget)
        self.window_start.menu_list_with_tablewidget.triggered.connect(self.show_window_list_with_tablewidget)
        self.window_start.menu_exit.triggered.connect(sys.exit)
        return

    def show_window_register(self):
        self.window_register.setupUi(self)
        self.window_register.btn_register.clicked.connect(self.register_mobile_phone)
        return

    def show_window_list(self):
        self.window_list.setupUi(self)
        listado = sql_operations.get_mobile_phones()
        texto = ""
        for movil in listado:
            texto += movil.to_text() + "\n"
        self.window_list.txt_list.setText(texto)
        return

    def show_window_list_with_listwidget(self):
        self.window_list_with_listwidget.setupUi(self)
        mobile_phones_list = sql_operations.get_mobile_phones()
        for mobile in mobile_phones_list:
            mobile_text = mobile.to_text()
            self.window_list_with_listwidget.lst_list.addItem(mobile_text)
        self.window_list_with_listwidget.lst_list.itemDoubleClicked.connect(partial(self.show_detail, ))
        return

    def show_window_list_with_tablewidget(self):
        self.window_list_with_tablewidget.setupUi(self)
        mobiles_list = sql_operations.get_mobile_phones()
        row = 0
        for mobile_phone in mobiles_list:
            self.window_list_with_tablewidget.tbl_list.insertRow(row)
            cell = QTableWidgetItem(str(mobile_phone.id_mobile_phone))
            self.window_list_with_tablewidget.tbl_list.setItem(row, 0, cell)
            cell = QTableWidgetItem(mobile_phone.brand)
            self.window_list_with_tablewidget.tbl_list.setItem(row, 1, cell)
            cell = QTableWidgetItem(mobile_phone.model)
            self.window_list_with_tablewidget.tbl_list.setItem(row, 2, cell)
            cell = QTableWidgetItem(mobile_phone.os)
            self.window_list_with_tablewidget.tbl_list.setItem(row, 3, cell)
            cell = QTableWidgetItem(str(mobile_phone.memory))
            self.window_list_with_tablewidget.tbl_list.setItem(row, 4, cell)
            cell = QTableWidgetItem(str(mobile_phone.price))
            self.window_list_with_tablewidget.tbl_list.setItem(row, 5, cell)
            row += 1
        self.window_list_with_tablewidget.btn_delete.clicked.connect(self.btn_clicked_delete)
        self.window_list_with_tablewidget.btn_update.clicked.connect(self.btn_clicked_update)
        return

    def show_window_update(self, mobile_phone):
        self.window_update.setupUi(self)
        self.window_update.txt_brand.setText(mobile_phone.brand)
        self.window_update.txt_model.setText(mobile_phone.model)
        self.window_update.txt_os.setText(mobile_phone.os)
        self.window_update.txt_memory.setText(str(mobile_phone.memory))
        self.window_update.txt_price.setText(str(mobile_phone.price))
        self.window_update.btn_save.clicked.connect(partial(self.btn_clicked_save, mobile_phone))
        return

    def show_detail(self):
        item = self.window_list_with_listwidget.lst_list.selectedItems()
        detail_text = item[0].text().replace(" - ", "\n")
        QMessageBox.about(self, "Info", detail_text)
        return

    def register_mobile_phone(self):
        mobile_phone = Mobile_phone()

        error = ""
        if not validations.check_brand(self.window_register.txt_brand.text()):
            error = "Los siguientes campos no están correctos:"
            error += "\nLa marca debe ser una o más palabras."
        if not validations.check_model(self.window_register.txt_model.text()):
            if error == "":
                error = "Los siguientes campos no están correctos:"
            error += "\nEl modelo debe ser una o más palabras."
        if not validations.check_os(self.window_register.txt_os.text()):
            if error == "":
                error = "Los siguientes campos no están correctos:"
            error += "\nEl sistema operativo debe ser Android, iOS, Windows Phone u otros."
        if not validations.check_memory(self.window_register.txt_memory.text()):
            if error == "":
                error = "Los siguientes campos no están correctos:"
            error += "\nLa cantidad de memoria debe ser un número entero mayor que cero."
        if not validations.check_price(self.window_register.txt_price.text()):
            if error == "":
                error = "Los siguientes campos no están correctos:"
            error += "\nEl precio debe ser un número mayor que cero."

        if error == "":
            mobile_phone.brand = self.window_register.txt_brand.text()
            mobile_phone.model = self.window_register.txt_model.text()
            mobile_phone.os = self.window_register.txt_os.text()
            mobile_phone.memory = int(self.window_register.txt_memory.text())
            mobile_phone.price = float(self.window_register.txt_price.text())

            sql_operations.register_mobile_phone(mobile_phone)
            QMessageBox.information(self, "info", "Se ha introducido el móvil en la Base de Datos.")
            self.show_window_start()
        else:
            QMessageBox.warning(self, "Error", error)
        return

    def btn_clicked_delete(self):
        selected = self.window_list_with_tablewidget.tbl_list.currentRow()
        if selected != -1:  # Se ha seleccionado algun fila
            id_borrar = self.window_list_with_tablewidget.tbl_list.item(selected, 0).text()
            button_reply = QMessageBox.question(self, "¿Está seguro?", "¿Está seguro de que desea eliminar el móvil?",
                                                QMessageBox.Yes | QMessageBox.No)
            if button_reply == QMessageBox.Yes:
                sql_operations.delete_mobile_phone(id_borrar)
                QMessageBox.information(self, "info", "Se ha eliminado el móvil de la Base de Datos.")
        self.show_window_list_with_tablewidget()
        return

    def btn_clicked_update(self):
        selected = self.window_list_with_tablewidget.tbl_list.currentRow()
        if selected != -1:  # Se comprueba si hay alguna fila seleccionada.
            # se selecciona la celda de la primera columna de la fila seleccionada.
            mobile_phone_id = self.window_list_with_tablewidget.tbl_list.item(selected, 0).text()
            mobile_phone = sql_operations.get_mobile_phone_by_id(mobile_phone_id)
            self.show_window_update(mobile_phone)
        else:
            QMessageBox.information(self, "Información", "Se debe elegir alguna columna.")
        return

    def btn_clicked_save(self, mobile_phone):
        error = ""
        if not validations.check_brand(self.window_update.txt_brand.text()):
            error = "Los siguientes campos no están correctos:"
            error += "\nLa marca debe ser una o más palabras."
        if not validations.check_model(self.window_update.txt_model.text()):
            if error == "":
                error = "Los siguientes campos no están correctos:"
            error += "\nEl modelo debe ser una o más palabras."
        if not validations.check_os(self.window_update.txt_os.text()):
            if error == "":
                error = "Los siguientes campos no están correctos:"
            error += "\nEl sistema operativo debe ser Android, iOS, Windows Phone u otros."
        if not validations.check_memory(self.window_update.txt_memory.text()):
            if error == "":
                error = "Los siguientes campos no están correctos:"
            error += "\nLa cantidad de memoria debe ser un número entero mayor que cero."
        if not validations.check_price(self.window_update.txt_price.text()):
            if error == "":
                error = "Los siguientes campos no están correctos:"
            error += "\nEl precio debe ser un número mayor que cero."

        if error == "":  # si todas las validaciones han sido correctas.
            button_reply = QMessageBox.question(self, "¿Está seguro?", "¿Está seguro de que desea modificar el móvil?",
                                                QMessageBox.Yes | QMessageBox.No)
            if button_reply == QMessageBox.Yes:
                mobile_phone.brand = self.window_update.txt_brand.text()
                mobile_phone.model = self.window_update.txt_model.text()
                mobile_phone.os = self.window_update.txt_os.text()
                mobile_phone.memory = int(self.window_update.txt_memory.text())
                mobile_phone.price = float(self.window_update.txt_price.text())

                sql_operations.update_mobile_phone(mobile_phone)
                QMessageBox.information(self, "info", "Se ha modificado el móvil en la Base de Datos.")
                self.show_window_list_with_tablewidget()
            else:
                self.show_window_list_with_tablewidget()
        else:
            QMessageBox.warning(self, "Error", error)
        return


"""
Para pruebas.
"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Application()
    ventana.show()

    sys.exit(app.exec())
