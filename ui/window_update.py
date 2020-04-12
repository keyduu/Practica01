# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\window_update.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window_update(object):
    def setupUi(self, window_update):
        window_update.setObjectName("window_update")
        window_update.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(window_update.sizePolicy().hasHeightForWidth())
        window_update.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        window_update.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icon_mobile_phone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window_update.setWindowIcon(icon)
        window_update.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(window_update)
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
        self.lbl_model = QtWidgets.QLabel(self.centralwidget)
        self.lbl_model.setGeometry(QtCore.QRect(150, 130, 245, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_model.sizePolicy().hasHeightForWidth())
        self.lbl_model.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.lbl_model.setFont(font)
        self.lbl_model.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_model.setObjectName("lbl_model")
        self.txt_model = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_model.setGeometry(QtCore.QRect(400, 130, 245, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_model.sizePolicy().hasHeightForWidth())
        self.txt_model.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.txt_model.setFont(font)
        self.txt_model.setObjectName("txt_model")
        self.lbl_os = QtWidgets.QLabel(self.centralwidget)
        self.lbl_os.setGeometry(QtCore.QRect(150, 180, 245, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_os.sizePolicy().hasHeightForWidth())
        self.lbl_os.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.lbl_os.setFont(font)
        self.lbl_os.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_os.setObjectName("lbl_os")
        self.txt_os = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_os.setGeometry(QtCore.QRect(400, 180, 245, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_os.sizePolicy().hasHeightForWidth())
        self.txt_os.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.txt_os.setFont(font)
        self.txt_os.setObjectName("txt_os")
        self.lbl_memory = QtWidgets.QLabel(self.centralwidget)
        self.lbl_memory.setGeometry(QtCore.QRect(150, 230, 245, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_memory.sizePolicy().hasHeightForWidth())
        self.lbl_memory.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_memory.setFont(font)
        self.lbl_memory.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_memory.setObjectName("lbl_memory")
        self.txt_memory = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_memory.setGeometry(QtCore.QRect(400, 230, 245, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_memory.sizePolicy().hasHeightForWidth())
        self.txt_memory.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.txt_memory.setFont(font)
        self.txt_memory.setObjectName("txt_memory")
        self.lbl_price = QtWidgets.QLabel(self.centralwidget)
        self.lbl_price.setGeometry(QtCore.QRect(150, 280, 245, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_price.sizePolicy().hasHeightForWidth())
        self.lbl_price.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_price.setFont(font)
        self.lbl_price.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_price.setObjectName("lbl_price")
        self.txt_price = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_price.setGeometry(QtCore.QRect(400, 280, 245, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_price.sizePolicy().hasHeightForWidth())
        self.txt_price.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.txt_price.setFont(font)
        self.txt_price.setObjectName("txt_price")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(300, 514, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save.setFont(font)
        self.btn_save.setStyleSheet("    background-color:#33bdef;\n"
"    border-radius:20px;\n"
"    border:3px solid #057fd0;\n"
"    color:#ffffff;\n"
"    font-family:Verdana;\n"
"    font-size:16px;\n"
"    font-weight:bold;\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icon_save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon1)
        self.btn_save.setIconSize(QtCore.QSize(32, 32))
        self.btn_save.setObjectName("btn_save")
        self.lbl_brand = QtWidgets.QLabel(self.centralwidget)
        self.lbl_brand.setGeometry(QtCore.QRect(150, 80, 245, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_brand.sizePolicy().hasHeightForWidth())
        self.lbl_brand.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.lbl_brand.setFont(font)
        self.lbl_brand.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_brand.setObjectName("lbl_brand")
        self.txt_brand = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_brand.setGeometry(QtCore.QRect(400, 80, 245, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_brand.sizePolicy().hasHeightForWidth())
        self.txt_brand.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.txt_brand.setFont(font)
        self.txt_brand.setObjectName("txt_brand")
        window_update.setCentralWidget(self.centralwidget)
        self.menu_registrar = QtWidgets.QAction(window_update)
        self.menu_registrar.setObjectName("menu_registrar")
        self.menu_listar_text = QtWidgets.QAction(window_update)
        self.menu_listar_text.setObjectName("menu_listar_text")
        self.menu_salir = QtWidgets.QAction(window_update)
        self.menu_salir.setObjectName("menu_salir")
        self.menu_listar_list = QtWidgets.QAction(window_update)
        self.menu_listar_list.setObjectName("menu_listar_list")
        self.menu_listar_table = QtWidgets.QAction(window_update)
        self.menu_listar_table.setObjectName("menu_listar_table")

        self.retranslateUi(window_update)
        QtCore.QMetaObject.connectSlotsByName(window_update)

    def retranslateUi(self, window_update):
        _translate = QtCore.QCoreApplication.translate
        window_update.setWindowTitle(_translate("window_update", "Móviles"))
        self.lbl_title.setText(_translate("window_update", "Modificar móvil"))
        self.lbl_model.setText(_translate("window_update", "Modelo:"))
        self.lbl_os.setText(_translate("window_update", "Sistema operativo:"))
        self.lbl_memory.setText(_translate("window_update", "Memoria:"))
        self.lbl_price.setText(_translate("window_update", "Precio:"))
        self.btn_save.setText(_translate("window_update", "Guardar"))
        self.lbl_brand.setText(_translate("window_update", "Marca:"))
        self.menu_registrar.setText(_translate("window_update", "Registrar móvil"))
        self.menu_listar_text.setText(_translate("window_update", "Listar móviles (TextEdit)"))
        self.menu_salir.setText(_translate("window_update", "Salir"))
        self.menu_listar_list.setText(_translate("window_update", "Listar móviles (List Widget)"))
        self.menu_listar_table.setText(_translate("window_update", "Listar móviles (Table Widget)"))
import images_rc
