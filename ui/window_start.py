# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\window_start.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window_start(object):
    def setupUi(self, window_start):
        window_start.setObjectName("window_start")
        window_start.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        window_start.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon_mobile_phone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window_start.setWindowIcon(icon)
        window_start.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(window_start)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_welcome = QtWidgets.QLabel(self.centralwidget)
        self.lbl_welcome.setGeometry(QtCore.QRect(0, 0, 800, 320))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_welcome.setFont(font)
        self.lbl_welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_welcome.setObjectName("lbl_welcome")
        self.lbl_image = QtWidgets.QLabel(self.centralwidget)
        self.lbl_image.setGeometry(QtCore.QRect(0, 320, 800, 250))
        self.lbl_image.setText("")
        self.lbl_image.setPixmap(QtGui.QPixmap(":/images/image_mobile_phone.png"))
        self.lbl_image.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_image.setObjectName("lbl_image")
        window_start.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(window_start)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.mobile_menu = QtWidgets.QMenu(self.menubar)
        self.mobile_menu.setObjectName("mobile_menu")
        window_start.setMenuBar(self.menubar)
        self.menu_register = QtWidgets.QAction(window_start)
        self.menu_register.setObjectName("menu_register")
        self.menu_list = QtWidgets.QAction(window_start)
        self.menu_list.setObjectName("menu_list")
        self.menu_exit = QtWidgets.QAction(window_start)
        self.menu_exit.setObjectName("menu_exit")
        self.menu_list_with_listwidget = QtWidgets.QAction(window_start)
        self.menu_list_with_listwidget.setObjectName("menu_list_with_listwidget")
        self.menu_list_with_tablewidget = QtWidgets.QAction(window_start)
        self.menu_list_with_tablewidget.setObjectName("menu_list_with_tablewidget")
        self.mobile_menu.addAction(self.menu_register)
        self.mobile_menu.addAction(self.menu_list)
        self.mobile_menu.addAction(self.menu_list_with_listwidget)
        self.mobile_menu.addAction(self.menu_list_with_tablewidget)
        self.mobile_menu.addSeparator()
        self.mobile_menu.addAction(self.menu_exit)
        self.menubar.addAction(self.mobile_menu.menuAction())

        self.retranslateUi(window_start)
        QtCore.QMetaObject.connectSlotsByName(window_start)

    def retranslateUi(self, window_start):
        _translate = QtCore.QCoreApplication.translate
        window_start.setWindowTitle(_translate("window_start", "Móviles"))
        self.lbl_welcome.setText(_translate("window_start", "¡Bienvenido!"))
        self.mobile_menu.setTitle(_translate("window_start", "Móviles"))
        self.menu_register.setText(_translate("window_start", "Registrar móvil"))
        self.menu_list.setText(_translate("window_start", "Listar móviles (TextEdit)"))
        self.menu_exit.setText(_translate("window_start", "Salir"))
        self.menu_list_with_listwidget.setText(_translate("window_start", "Listar móviles (List Widget)"))
        self.menu_list_with_tablewidget.setText(_translate("window_start", "Listar móviles (Table Widget)"))
import images_rc
