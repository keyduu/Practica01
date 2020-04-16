# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/window_list_with_listwidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window_list_with_listwidget(object):
    def setupUi(self, window_list_with_listwidget):
        window_list_with_listwidget.setObjectName("window_list_with_listwidget")
        window_list_with_listwidget.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        window_list_with_listwidget.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\images/icons/icon_mobile_phone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window_list_with_listwidget.setWindowIcon(icon)
        window_list_with_listwidget.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(window_list_with_listwidget)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(200, 10, 400, 40))
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
        self.lst_list.setGeometry(QtCore.QRect(10, 60, 780, 504))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.lst_list.setFont(font)
        self.lst_list.setStyleSheet("border-radius: 10px; border: 2px solid navy;")
        self.lst_list.setObjectName("lst_list")
        window_list_with_listwidget.setCentralWidget(self.centralwidget)

        self.retranslateUi(window_list_with_listwidget)
        QtCore.QMetaObject.connectSlotsByName(window_list_with_listwidget)

    def retranslateUi(self, window_list_with_listwidget):
        _translate = QtCore.QCoreApplication.translate
        window_list_with_listwidget.setWindowTitle(_translate("window_list_with_listwidget", "Móviles"))
        self.lbl_title.setText(_translate("window_list_with_listwidget", "Listar móviles"))
