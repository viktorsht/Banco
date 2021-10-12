# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_autenticacao.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from Telas.estilos import Estilos

class Ui_Tela_Autenticacao(object):

    def __init__(self):
        self.tela_index = 0
        self.estilo_aut = Estilos()


    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(1000, 500)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("font-weight: bold; font-size: 11px; color: #333333;")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem4)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setStyleSheet("background-color: transparent; color: #333333;font-size: 12px; font-weight: bold; text-align: left;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Assets/bank-account.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.le_aut_cpf = QtWidgets.QLineEdit(Form)
        self.le_aut_cpf.setStyleSheet(self.estilo_aut.estilo_entradas())
        self.le_aut_cpf.setObjectName("le_aut_cpf")
        self.verticalLayout.addWidget(self.le_aut_cpf)
        spacerItem5 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem5)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setStyleSheet("background-color: transparent; color: #333333;font-size: 12px; font-weight: bold; text-align: left;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Assets/key.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.le_aut_senha = QtWidgets.QLineEdit(Form)
        self.le_aut_senha.setStyleSheet(self.estilo_aut.estilo_entradas())
        self.le_aut_senha.setObjectName("le_aut_senha")
        self.verticalLayout.addWidget(self.le_aut_senha)
        spacerItem6 = QtWidgets.QSpacerItem(20, 45, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_aut_confirmar = QtWidgets.QPushButton(Form)
        self.btn_aut_confirmar.setStyleSheet(self.estilo_aut.estilo_botoes_confirmacao())
        self.btn_aut_confirmar.setObjectName("btn_aut_confirmar")
        self.horizontalLayout_4.addWidget(self.btn_aut_confirmar)
        self.btn_aut_cancelar = QtWidgets.QPushButton(Form)
        self.btn_aut_cancelar.setStyleSheet(self.estilo_aut.estilo_botoes_cancelamento())
        self.btn_aut_cancelar.setObjectName("btn_aut_cancelar")
        self.horizontalLayout_4.addWidget(self.btn_aut_cancelar)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Preencha os campos com os dados corretamente"))
        self.pushButton.setText(_translate("Form", "CPF"))
        self.pushButton_2.setText(_translate("Form", "Senha"))
        self.btn_aut_confirmar.setText(_translate("Form", "Logar"))
        self.btn_aut_cancelar.setText(_translate("Form", "Cancelar"))