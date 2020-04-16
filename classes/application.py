import os
import pathlib
import shutil
import sys

from database import db_operations
from validations import validations
from classes.mobile_phone import Mobile_phone
from ui import window_update, window_start, window_register, window_list_with_tablewidget, window_list, \
    window_list_with_listwidget
from PyQt5.Qt import QTableWidgetItem, QMainWindow, QApplication, QMessageBox, QPixmap, \
    QLabel, QFileDialog, QWidget
from functools import partial


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
        mobile_phone = Mobile_phone()
        self.window_register.setupUi(self)
        self.window_register.btn_register.clicked.connect(partial(self.save_mobile_phone, self.window_register,
                                                                  mobile_phone))
        self.window_register.btn_select_image.clicked.connect(partial(self.btn_clicked_select_file,
                                                                      self.window_register, mobile_phone))
        return

    def show_window_list(self):
        self.window_list.setupUi(self)
        try:
            listado = db_operations.get_mobile_phones()
        except Exception as e:
            print(e)
            return
        text = ""
        for movil in listado:
            text += movil.to_text() + "\n"
        self.window_list.txt_list.setText(text)
        return

    def show_window_list_with_listwidget(self):
        self.window_list_with_listwidget.setupUi(self)
        try:
            mobile_phones_list = db_operations.get_mobile_phones()
        except Exception as e:
            print(e)
            return
        for mobile_phone in mobile_phones_list:
            mobile_text = mobile_phone.to_text()
            self.window_list_with_listwidget.lst_list.addItem(mobile_text)
        self.window_list_with_listwidget.lst_list.itemDoubleClicked.connect(self.show_detail)
        return

    def show_window_list_with_tablewidget(self):
        self.window_list_with_tablewidget.setupUi(self)
        try:
            mobiles_list = db_operations.get_mobile_phones()
        except Exception as e:
            print(e)
            return
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
            cell = QTableWidgetItem(str(mobile_phone.deal))
            self.window_list_with_tablewidget.tbl_list.setItem(row, 6, cell)
            cell = QTableWidgetItem(str(mobile_phone.technology))
            self.window_list_with_tablewidget.tbl_list.setItem(row, 7, cell)
            try:
                if pathlib.Path(mobile_phone.photo_path).is_file():
                    image = QLabel()
                    pixmap = QPixmap(mobile_phone.photo_path).scaledToHeight(50)
                    image.setPixmap(pixmap)
                    self.window_list_with_tablewidget.tbl_list.setCellWidget(row, 8, image)
            except Exception as e:
                print(e)
                return

            row += 1
        self.window_list_with_tablewidget.btn_delete.clicked.connect(self.btn_clicked_delete)
        self.window_list_with_tablewidget.btn_update.clicked.connect(self.btn_clicked_update)
        return

    def show_window_update(self, mobile_phone):
        self.window_update.setupUi(self)
        self.window_update.txt_brand.setText(mobile_phone.brand)
        self.window_update.txt_model.setText(mobile_phone.model)
        self.window_update.cmb_os.setCurrentText(mobile_phone.os)
        self.window_update.txt_memory.setText(str(mobile_phone.memory))
        self.window_update.txt_price.setText(str(mobile_phone.price))
        if mobile_phone.deal == "SI":
            self.window_update.chk_deal.setChecked(True)
        else:
            self.window_update.chk_deal.setChecked(False)
        if mobile_phone.technology == "3G":
            self.window_update.rbtn_3g.setChecked(True)
        else:
            self.window_update.rbtn_3g.setChecked(False)
        if mobile_phone.technology == "4G":
            self.window_update.rbtn_4g.setChecked(True)
        else:
            self.window_update.rbtn_4g.setChecked(False)

        if mobile_phone.technology == "5G":
            self.window_update.rbtn_5g.setChecked(True)
        else:
            self.window_update.rbtn_5g.setChecked(False)
        if mobile_phone.photo_path != "":
            image = self.window_update.lbl_image
            label_height = self.window_update.lbl_image.height()
            pixmap = QPixmap(mobile_phone.photo_path).scaledToHeight(label_height)
            image.setPixmap(pixmap)

        self.window_update.btn_save.clicked.connect(partial(self.save_mobile_phone, self.window_update, mobile_phone))
        self.window_update.btn_select_image.clicked.connect(partial(self.btn_clicked_select_file, self.window_update,
                                                                    mobile_phone))
        return

    def show_detail(self):
        item = self.window_list_with_listwidget.lst_list.selectedItems()
        detail_text = item[0].text().replace(" - ", "\n")
        QMessageBox.about(self, "Info", detail_text)
        return

    def btn_clicked_select_file(self, window, mobile_phone):
        try:
            file = QFileDialog.getOpenFileName(self)
        except Exception as e:
            print(e)
            return
        filepath = file[0]
        filename = filepath.split("/")[-1]  # Se obtiene el nombre del archivo sin ruta.
        temp_path = "images/temp/" + filename
        shutil.copy(filepath, temp_path)
        label_height = window.lbl_image.height()
        image = QPixmap(temp_path).scaledToHeight(label_height)
        window.lbl_image.setPixmap(image)
        mobile_phone.photo_path = temp_path
        return

    def save_mobile_phone(self, window, mobile_phone):
        error = ""
        if not validations.check_brand(window.txt_brand.text()):
            error = "Los siguientes campos no están correctos:"
            error += "\nLa marca debe ser una o más palabras."
            window.txt_brand.setStyleSheet("border-radius: 10px 10px; border: 2px solid red;")
        else:
            window.txt_brand.setStyleSheet("border-radius: 10px 10px; border: 2px solid navy;")
        if not validations.check_model(window.txt_model.text()):
            if error == "":
                error = "Los siguientes campos no están correctos:"
            error += "\nEl modelo debe ser una o más palabras."
            window.txt_model.setStyleSheet("border-radius: 10px 10px; border: 2px solid red;")
        else:
            window.txt_model.setStyleSheet("border-radius: 10px 10px; border: 2px solid navy;")

        if not validations.check_memory(window.txt_memory.text()):
            if error == "":
                error = "Los siguientes campos no están correctos:"
            error += "\nLa cantidad de memoria debe ser un número entero mayor que cero."
            window.txt_memory.setStyleSheet("border-radius: 10px 10px; border: 2px solid red;")
        else:
            window.txt_memory.setStyleSheet("border-radius: 10px 10px; border: 2px solid navy;")
        if not validations.check_price(window.txt_price.text().replace(",", ".")):
            if error == "":
                error = "Los siguientes campos no están correctos:"
            error += "\nEl precio debe ser un número mayor que cero."
            window.txt_price.setStyleSheet("border-radius: 10px 10px; border: 2px solid red;")
        else:
            window.txt_price.setStyleSheet("border-radius: 10px 10px; border: 2px solid navy;")
        if error == "":
            mobile_phone.brand = window.txt_brand.text()
            mobile_phone.model = window.txt_model.text()
            mobile_phone.os = window.cmb_os.currentText()
            mobile_phone.memory = int(window.txt_memory.text())
            mobile_phone.price = float(window.txt_price.text().replace(",", "."))
            if window.chk_deal.isChecked():
                mobile_phone.deal = "SI"
            else:
                mobile_phone.deal = "NO"
            if window.rbtn_3g.isChecked():
                mobile_phone.technology = "3G"
            elif window.rbtn_4g.isChecked():
                mobile_phone.technology = "4G"
            else:
                mobile_phone.technology = "5G"

            try:
                if mobile_phone.id_mobile_phone == 0:  # si es un registro nuevo, lo guarda para obtener el id.
                    mobile_phone.id_mobile_phone = db_operations.register_mobile_phone(mobile_phone)
                if mobile_phone.photo_path != "":
                    if pathlib.Path(mobile_phone.photo_path).is_file():
                        file_extension = mobile_phone.photo_path.split(".")[-1]  # obtiene la extensión del archivo,
                        # para guardarlo con el mismo formato que la imagen original.
                        path = "images/image" + str(mobile_phone.id_mobile_phone) + "." + file_extension
                        shutil.move(mobile_phone.photo_path, path)
                        mobile_phone.photo_path = path
                    else:
                        mobile_phone.photo_path = ""  # Si el archivo ya no existe, se quita de la base de datos.
                    db_operations.update_mobile_phone(mobile_phone)
            except Exception as e:
                print(e)
                return

            QMessageBox.information(self, "info", "Se ha guardado el móvil en la Base de Datos.")
            self.show_window_list_with_tablewidget()
        else:
            QMessageBox.warning(self, "Error", error)
        return

    def btn_clicked_delete(self):
        selected = self.window_list_with_tablewidget.tbl_list.currentRow()
        if selected != -1:  # Se ha seleccionado algun fila
            id_to_delete = self.window_list_with_tablewidget.tbl_list.item(selected, 0).text()
            mobile_phone = db_operations.get_mobile_phone_by_id(id_to_delete)
            button_reply = QMessageBox.question(self, "¿Está seguro?", "¿Está seguro de que desea eliminar el móvil?",
                                                QMessageBox.Yes | QMessageBox.No)
            if button_reply == QMessageBox.Yes:
                try:
                    db_operations.delete_mobile_phone(id_to_delete)
                    if pathlib.Path(mobile_phone.photo_path).is_file():
                        os.remove(mobile_phone.photo_path)  # Para borrar la foto del directorio.
                except Exception as e:
                    print(e)
                    return
                QMessageBox.information(self, "info", "Se ha eliminado el móvil de la Base de Datos.")
        self.show_window_list_with_tablewidget()
        return

    def btn_clicked_update(self):
        selected = self.window_list_with_tablewidget.tbl_list.currentRow()
        if selected != -1:  # Se comprueba si hay alguna fila seleccionada.
            # se selecciona la celda de la primera columna de la fila seleccionada.
            mobile_phone_id = self.window_list_with_tablewidget.tbl_list.item(selected, 0).text()
            try:
                mobile_phone = db_operations.get_mobile_phone_by_id(mobile_phone_id)
            except Exception as e:
                print(e)
                return
            self.show_window_update(mobile_phone)
        else:
            QMessageBox.information(self, "Información", "Se debe elegir alguna columna.")
        return


"""
Para pruebas.
"""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Application()
    ventana.show()

    sys.exit(app.exec())
