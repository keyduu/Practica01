# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\window_list.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window_list(object):
    def setupUi(self, window_list):
        window_list.setObjectName("window_list")
        window_list.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon_mobile_phone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window_list.setWindowIcon(icon)
        window_list.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(window_list)
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
        self.txt_list = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_list.setGeometry(QtCore.QRect(10, 70, 780, 494))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.txt_list.setFont(font)
        self.txt_list.setObjectName("txt_list")
        window_list.setCentralWidget(self.centralwidget)
        self.menu_registrar = QtWidgets.QAction(window_list)
        self.menu_registrar.setObjectName("menu_registrar")
        self.menu_listar_text = QtWidgets.QAction(window_list)
        self.menu_listar_text.setObjectName("menu_listar_text")
        self.menu_salir = QtWidgets.QAction(window_list)
        self.menu_salir.setObjectName("menu_salir")
        self.menu_listar_list = QtWidgets.QAction(window_list)
        self.menu_listar_list.setObjectName("menu_listar_list")
        self.menu_listar_table = QtWidgets.QAction(window_list)
        self.menu_listar_table.setObjectName("menu_listar_table")

        self.retranslateUi(window_list)
        QtCore.QMetaObject.connectSlotsByName(window_list)

    def retranslateUi(self, window_list):
        _translate = QtCore.QCoreApplication.translate
        window_list.setWindowTitle(_translate("window_list", "Móviles"))
        self.lbl_title.setText(_translate("window_list", "Listar móviles"))
        self.menu_registrar.setText(_translate("window_list", "Registrar móvil"))
        self.menu_listar_text.setText(_translate("window_list", "Listar móviles (TextEdit)"))
        self.menu_salir.setText(_translate("window_list", "Salir"))
        self.menu_listar_list.setText(_translate("window_list", "Listar móviles (List Widget)"))
        self.menu_listar_table.setText(_translate("window_list", "Listar móviles (Table Widget)"))
import images_rc
