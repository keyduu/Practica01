# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\window_list_with_tablewidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window_list_with_tablewidget(object):
    def setupUi(self, window_list_with_tablewidget):
        window_list_with_tablewidget.setObjectName("window_list_with_tablewidget")
        window_list_with_tablewidget.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon_mobile_phone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window_list_with_tablewidget.setWindowIcon(icon)
        window_list_with_tablewidget.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(window_list_with_tablewidget)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(200, 10, 400, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_title.sizePolicy().hasHeightForWidth())
        self.lbl_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        font.setUnderline(True)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.tbl_list = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl_list.setGeometry(QtCore.QRect(10, 70, 780, 431))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.tbl_list.setFont(font)
        self.tbl_list.setObjectName("tbl_list")
        self.tbl_list.setColumnCount(6)
        self.tbl_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_list.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_list.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_list.setHorizontalHeaderItem(5, item)
        self.tbl_list.verticalHeader().setVisible(False)
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(10, 510, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delete.setFont(font)
        self.btn_delete.setStyleSheet("    background-color:#33bdef;\n"
"    border-radius:20px;\n"
"    border:3px solid #057fd0;\n"
"    color:#ffffff;\n"
"    font-family:Verdana;\n"
"    font-size:16px;\n"
"    font-weight:bold;\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icon_delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delete.setIcon(icon1)
        self.btn_delete.setIconSize(QtCore.QSize(32, 32))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(620, 510, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_update.setFont(font)
        self.btn_update.setStyleSheet("    background-color:#33bdef;\n"
"    border-radius:20px;\n"
"    border:3px solid #057fd0;\n"
"    color:#ffffff;\n"
"    font-family:Verdana;\n"
"    font-size:16px;\n"
"    font-weight:bold;\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icon_edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_update.setIcon(icon2)
        self.btn_update.setIconSize(QtCore.QSize(32, 32))
        self.btn_update.setObjectName("btn_update")
        window_list_with_tablewidget.setCentralWidget(self.centralwidget)
        self.menu_registrar = QtWidgets.QAction(window_list_with_tablewidget)
        self.menu_registrar.setObjectName("menu_registrar")
        self.menu_listar_text = QtWidgets.QAction(window_list_with_tablewidget)
        self.menu_listar_text.setObjectName("menu_listar_text")
        self.menu_salir = QtWidgets.QAction(window_list_with_tablewidget)
        self.menu_salir.setObjectName("menu_salir")
        self.menu_listar_list = QtWidgets.QAction(window_list_with_tablewidget)
        self.menu_listar_list.setObjectName("menu_listar_list")
        self.menu_listar_table = QtWidgets.QAction(window_list_with_tablewidget)
        self.menu_listar_table.setObjectName("menu_listar_table")

        self.retranslateUi(window_list_with_tablewidget)
        QtCore.QMetaObject.connectSlotsByName(window_list_with_tablewidget)

    def retranslateUi(self, window_list_with_tablewidget):
        _translate = QtCore.QCoreApplication.translate
        window_list_with_tablewidget.setWindowTitle(_translate("window_list_with_tablewidget", "Móviles"))
        self.lbl_title.setText(_translate("window_list_with_tablewidget", "Listar móviles"))
        item = self.tbl_list.horizontalHeaderItem(0)
        item.setText(_translate("window_list_with_tablewidget", "id"))
        item = self.tbl_list.horizontalHeaderItem(1)
        item.setText(_translate("window_list_with_tablewidget", "Marca"))
        item = self.tbl_list.horizontalHeaderItem(2)
        item.setText(_translate("window_list_with_tablewidget", "Modelo"))
        item = self.tbl_list.horizontalHeaderItem(3)
        item.setText(_translate("window_list_with_tablewidget", "Sistema Operativo"))
        item = self.tbl_list.horizontalHeaderItem(4)
        item.setText(_translate("window_list_with_tablewidget", "Memoria"))
        item = self.tbl_list.horizontalHeaderItem(5)
        item.setText(_translate("window_list_with_tablewidget", "Precio"))
        self.btn_delete.setText(_translate("window_list_with_tablewidget", "Borrar"))
        self.btn_update.setText(_translate("window_list_with_tablewidget", "Modificar"))
        self.menu_registrar.setText(_translate("window_list_with_tablewidget", "Registrar móvil"))
        self.menu_listar_text.setText(_translate("window_list_with_tablewidget", "Listar móviles (TextEdit)"))
        self.menu_salir.setText(_translate("window_list_with_tablewidget", "Salir"))
        self.menu_listar_list.setText(_translate("window_list_with_tablewidget", "Listar móviles (List Widget)"))
        self.menu_listar_table.setText(_translate("window_list_with_tablewidget", "Listar móviles (Table Widget)"))
import images_rc
