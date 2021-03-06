# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/window_list_with_tablewidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_window_list_with_tablewidget(object):
    def setupUi(self, window_list_with_tablewidget):
        window_list_with_tablewidget.setObjectName("window_list_with_tablewidget")
        window_list_with_tablewidget.resize(800, 600)
        window_list_with_tablewidget.setMinimumSize(QtCore.QSize(800, 600))
        window_list_with_tablewidget.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        window_list_with_tablewidget.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\images/icons/icon_mobile_phone.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window_list_with_tablewidget.setWindowIcon(icon)
        window_list_with_tablewidget.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(window_list_with_tablewidget)
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
        self.tbl_list = QtWidgets.QTableWidget(self.centralwidget)
        self.tbl_list.setGeometry(QtCore.QRect(10, 60, 780, 440))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.tbl_list.setFont(font)
        self.tbl_list.setStyleSheet("border-radius: 10px; border: 2px solid navy;")
        self.tbl_list.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tbl_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbl_list.setObjectName("tbl_list")
        self.tbl_list.setColumnCount(9)
        self.tbl_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        item.setFont(font)
        self.tbl_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        item.setFont(font)
        self.tbl_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        item.setFont(font)
        self.tbl_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        item.setFont(font)
        self.tbl_list.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        item.setFont(font)
        self.tbl_list.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        item.setFont(font)
        self.tbl_list.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        item.setFont(font)
        self.tbl_list.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        item.setFont(font)
        self.tbl_list.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        item.setFont(font)
        self.tbl_list.setHorizontalHeaderItem(8, item)
        self.tbl_list.horizontalHeader().setHighlightSections(False)
        self.tbl_list.verticalHeader().setVisible(False)
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(10, 510, 170, 54))
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
        icon1.addPixmap(QtGui.QPixmap("ui\\images/icons/icon_delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_delete.setIcon(icon1)
        self.btn_delete.setIconSize(QtCore.QSize(32, 32))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(620, 510, 170, 54))
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
        icon2.addPixmap(QtGui.QPixmap("ui\\images/icons/icon_edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_update.setIcon(icon2)
        self.btn_update.setIconSize(QtCore.QSize(32, 32))
        self.btn_update.setObjectName("btn_update")
        window_list_with_tablewidget.setCentralWidget(self.centralwidget)

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
        item.setText(_translate("window_list_with_tablewidget", "SS.OO."))
        item = self.tbl_list.horizontalHeaderItem(4)
        item.setText(_translate("window_list_with_tablewidget", "Memoria"))
        item = self.tbl_list.horizontalHeaderItem(5)
        item.setText(_translate("window_list_with_tablewidget", "Precio"))
        item = self.tbl_list.horizontalHeaderItem(6)
        item.setText(_translate("window_list_with_tablewidget", "Oferta"))
        item = self.tbl_list.horizontalHeaderItem(7)
        item.setText(_translate("window_list_with_tablewidget", "Tecnología"))
        item = self.tbl_list.horizontalHeaderItem(8)
        item.setText(_translate("window_list_with_tablewidget", "Foto"))
        self.btn_delete.setText(_translate("window_list_with_tablewidget", "Borrar"))
        self.btn_update.setText(_translate("window_list_with_tablewidget", "Modificar"))
