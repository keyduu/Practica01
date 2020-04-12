# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\window_list_with_listwidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window_list_with_listwidget(object):
    def setupUi(self, window_list_with_listwidget):
        window_list_with_listwidget.setObjectName("window_list_with_listwidget")
        window_list_with_listwidget.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon_mobile_phone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window_list_with_listwidget.setWindowIcon(icon)
        window_list_with_listwidget.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(window_list_with_listwidget)
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
        self.lst_list = QtWidgets.QListWidget(self.centralwidget)
        self.lst_list.setGeometry(QtCore.QRect(10, 70, 780, 494))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.lst_list.setFont(font)
        self.lst_list.setObjectName("lst_list")
        window_list_with_listwidget.setCentralWidget(self.centralwidget)
        self.menu_registrar = QtWidgets.QAction(window_list_with_listwidget)
        self.menu_registrar.setObjectName("menu_registrar")
        self.menu_listar_text = QtWidgets.QAction(window_list_with_listwidget)
        self.menu_listar_text.setObjectName("menu_listar_text")
        self.menu_salir = QtWidgets.QAction(window_list_with_listwidget)
        self.menu_salir.setObjectName("menu_salir")
        self.menu_listar_list = QtWidgets.QAction(window_list_with_listwidget)
        self.menu_listar_list.setObjectName("menu_listar_list")
        self.menu_listar_table = QtWidgets.QAction(window_list_with_listwidget)
        self.menu_listar_table.setObjectName("menu_listar_table")

        self.retranslateUi(window_list_with_listwidget)
        QtCore.QMetaObject.connectSlotsByName(window_list_with_listwidget)

    def retranslateUi(self, window_list_with_listwidget):
        _translate = QtCore.QCoreApplication.translate
        window_list_with_listwidget.setWindowTitle(_translate("window_list_with_listwidget", "Móviles"))
        self.lbl_title.setText(_translate("window_list_with_listwidget", "Listar móviles"))
        self.menu_registrar.setText(_translate("window_list_with_listwidget", "Registrar móvil"))
        self.menu_listar_text.setText(_translate("window_list_with_listwidget", "Listar móviles (TextEdit)"))
        self.menu_salir.setText(_translate("window_list_with_listwidget", "Salir"))
        self.menu_listar_list.setText(_translate("window_list_with_listwidget", "Listar móviles (List Widget)"))
        self.menu_listar_table.setText(_translate("window_list_with_listwidget", "Listar móviles (Table Widget)"))
import images_rc
