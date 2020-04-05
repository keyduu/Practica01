# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_inicio.ui'
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 574))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
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
        self.label.setText(_translate("MainWindow", "Bienvenido!"))
        self.menuM_viles.setTitle(_translate("MainWindow", "Móviles"))
        self.menu_registrar.setText(_translate("MainWindow", "Registrar móvil"))
        self.menu_listar_text.setText(_translate("MainWindow", "Listar móviles (TextEdit)"))
        self.menu_salir.setText(_translate("MainWindow", "Salir"))
        self.menu_listar_list.setText(_translate("MainWindow", "Listar móviles (List Widget)"))
        self.menu_listar_table.setText(_translate("MainWindow", "Listar móviles (Table Widget)"))
