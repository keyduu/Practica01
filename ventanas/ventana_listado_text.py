# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_listado_text.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_titulo = QtWidgets.QLabel(self.centralwidget)
        self.label_titulo.setGeometry(QtCore.QRect(200, 10, 400, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_titulo.sizePolicy().hasHeightForWidth())
        self.label_titulo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_titulo.setFont(font)
        self.label_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titulo.setObjectName("label_titulo")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 70, 780, 494))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuM_viles = QtWidgets.QMenu(self.menubar)
        self.menuM_viles.setObjectName("menuM_viles")
        MainWindow.setMenuBar(self.menubar)
        self.menu_registrar = QtWidgets.QAction(MainWindow)
        self.menu_registrar.setObjectName("menu_registrar")
        self.menu_listar_text = QtWidgets.QAction(MainWindow)
        self.menu_listar_text.setObjectName("menu_listar_text")
        self.menu_salir = QtWidgets.QAction(MainWindow)
        self.menu_salir.setObjectName("menu_salir")
        self.menu_listar_list = QtWidgets.QAction(MainWindow)
        self.menu_listar_list.setObjectName("menu_listar_list")
        self.menu_listar_table = QtWidgets.QAction(MainWindow)
        self.menu_listar_table.setObjectName("menu_listar_table")
        self.menuM_viles.addAction(self.menu_registrar)
        self.menuM_viles.addAction(self.menu_listar_text)
        self.menuM_viles.addAction(self.menu_listar_list)
        self.menuM_viles.addAction(self.menu_listar_table)
        self.menuM_viles.addSeparator()
        self.menuM_viles.addAction(self.menu_salir)
        self.menubar.addAction(self.menuM_viles.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Móviles"))
        self.label_titulo.setText(_translate("MainWindow", "Listar móviles"))
        self.menuM_viles.setTitle(_translate("MainWindow", "Móviles"))
        self.menu_registrar.setText(_translate("MainWindow", "Registrar móvil"))
        self.menu_listar_text.setText(_translate("MainWindow", "Listar móviles (TextEdit)"))
        self.menu_salir.setText(_translate("MainWindow", "Salir"))
        self.menu_listar_list.setText(_translate("MainWindow", "Listar móviles (List Widget)"))
        self.menu_listar_table.setText(_translate("MainWindow", "Listar móviles (Table Widget)"))
