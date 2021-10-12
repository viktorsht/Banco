# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_deposito.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Telas.estilos import Estilos

class Ui_Tela_Deposito(object):
    def __init__(self):
        self.estilos_dep = Estilos()
    def setupUi(self, Ui_Tela_Deposito):
        Ui_Tela_Deposito.setObjectName("Ui_Tela_Deposito")
        Ui_Tela_Deposito.resize(1000, 500)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Ui_Tela_Deposito)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.lbl_dep_usuario = QtWidgets.QLabel(Ui_Tela_Deposito)
        self.lbl_dep_usuario.setStyleSheet("font-weight: bold; font-size: 14px; color: #333333;")
        self.lbl_dep_usuario.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_dep_usuario.setObjectName("lbl_dep_usuario")
        self.verticalLayout.addWidget(self.lbl_dep_usuario)
        self.label = QtWidgets.QLabel(Ui_Tela_Deposito)
        self.label.setStyleSheet("font-weight: bold; font-size: 11px; color: #333333;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(Ui_Tela_Deposito)
        self.pushButton.setStyleSheet("background-color: transparent; color: #333333;font-size: 12px; font-weight: bold; text-align: left;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Assets/dollar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.le_dep_valor = QtWidgets.QLineEdit(Ui_Tela_Deposito)
        self.le_dep_valor.setStyleSheet(self.estilos_dep.estilo_entradas())
        self.le_dep_valor.setObjectName("le_dep_valor")
        self.verticalLayout.addWidget(self.le_dep_valor)
        spacerItem3 = QtWidgets.QSpacerItem(20, 45, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_dep_depositar = QtWidgets.QPushButton(Ui_Tela_Deposito)
        self.btn_dep_depositar.setStyleSheet(self.estilos_dep.estilo_botoes_confirmacao())
        self.btn_dep_depositar.setObjectName("btn_dep_depositar")
        self.horizontalLayout_3.addWidget(self.btn_dep_depositar)
        self.btn_dep_cancelar = QtWidgets.QPushButton(Ui_Tela_Deposito)
        self.btn_dep_cancelar.setStyleSheet(self.estilos_dep.estilo_botoes_cancelamento())
        self.btn_dep_cancelar.setObjectName("btn_dep_cancelar")
        self.horizontalLayout_3.addWidget(self.btn_dep_cancelar)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Ui_Tela_Deposito)
        QtCore.QMetaObject.connectSlotsByName(Ui_Tela_Deposito)

    def retranslateUi(self, Ui_Tela_Deposito):
        _translate = QtCore.QCoreApplication.translate
        Ui_Tela_Deposito.setWindowTitle(_translate("Ui_Tela_Deposito", "Form"))
        self.lbl_dep_usuario.setText(_translate("Ui_Tela_Deposito", "Usuario: Fulano de tal"))
        self.label.setText(_translate("Ui_Tela_Deposito", "Defina o valor do deposito no campo de \"valor de deposito\""))
        self.pushButton.setText(_translate("Ui_Tela_Deposito", "   Valor do deposito"))
        self.btn_dep_depositar.setText(_translate("Ui_Tela_Deposito", "Depositar"))
        self.btn_dep_cancelar.setText(_translate("Ui_Tela_Deposito", "Cancelar"))