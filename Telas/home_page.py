# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Telas.estilos import Estilos

from Telas.dialogs import Dialogs

from Telas.tela_apresentacao import Ui_tela_apresentacao
from Telas.tela_cadastro import Ui_Tela_Cadastro
from Telas.tela_autenticacao import Ui_Tela_Autenticacao
from Telas.tela_saque import Ui_Tela_Saque
from Telas.tela_transferencia import Ui_Tela_Transferencia
from Telas.tela_deposito import Ui_Tela_Deposito
from Telas.tela_extrato import Ui_Tela_Extrato

from Modelos.contas import Contas
from Modelos.conta import Conta
from Modelos.cliente import Cliente

class Ui_MainHomePage(object):

    def __init__(self):
        self.estilo = Estilos()
        self.tela_index = 0
        self.contas = Contas()
        self._tempConta = None
        self.show_password_flag = True

        #------clientes teste
        cliente1 = Cliente("joao", "de sousa", "111")
        conta1 = Conta(cliente1, "111")
        conta1.depositar(200)
        self.contas.salvar_conta(conta1)

        cliente2 = Cliente("vitor", "santos de lima", "222")
        conta2 = Conta(cliente2, "222")
        self.contas.salvar_conta(conta2)

    def reset_botoes_acoes(self):
        self.btn_goto_tela_cadastro.setStyleSheet(self.estilo.estilo_botao_navegacao())
        self.btn_goto_tela_saque.setStyleSheet(self.estilo.estilo_botao_navegacao())
        self.btn_goto_tela_transferencia.setStyleSheet(self.estilo.estilo_botao_navegacao())
        self.btn_goto_tela_deposito.setStyleSheet(self.estilo.estilo_botao_navegacao())
        self.btn_goto_tela_extrato.setStyleSheet(self.estilo.estilo_botao_navegacao())
        self.btn_got_tela_ajuda.setStyleSheet(self.estilo.estilo_botao_navegacao())

    def set_estilo_clique(self, tela_selecao:str):

        self.reset_botoes_acoes()

        if tela_selecao == "cadastro":
            self.btn_goto_tela_cadastro.setStyleSheet(self.estilo.estilo_botao_navegacao_clicado())
        elif tela_selecao == "saque":
            self.btn_goto_tela_saque.setStyleSheet(self.estilo.estilo_botao_navegacao_clicado())
        elif tela_selecao == "transferencia":
            self.btn_goto_tela_transferencia.setStyleSheet(self.estilo.estilo_botao_navegacao_clicado())
        elif tela_selecao == "deposito":
            self.btn_goto_tela_deposito.setStyleSheet(self.estilo.estilo_botao_navegacao_clicado())
        elif tela_selecao == "extrato":
            self.btn_goto_tela_extrato.setStyleSheet(self.estilo.estilo_botao_navegacao_clicado())
        elif tela_selecao == "ajuda":
            self.btn_got_tela_ajuda.setStyleSheet(self.estilo.estilo_botao_navegacao_clicado())

    def setup_telas(self):

        #-------------tela apresentacao------------------
        self.widget_tela_apresentacao = QtWidgets.QWidget()
        self.widget_tela_apresentacao.setObjectName("widget_tela_apresentacao")
        self.tela_apresentacao = Ui_tela_apresentacao()
        self.tela_apresentacao.setupUi(self.widget_tela_apresentacao)
        self.stack_telas.addWidget(self.widget_tela_apresentacao)

        #-------------tela autenteticação------------------
        self.widget_tela_autenticacao = QtWidgets.QWidget()
        self.widget_tela_autenticacao.setObjectName("widget_tela_autenticacao")
        self.tela_autenticacao = Ui_Tela_Autenticacao()
        self.tela_autenticacao.setupUi(self.widget_tela_autenticacao)
        self.stack_telas.addWidget(self.widget_tela_autenticacao)


        # -------------tela cadastro------------------
        self.widget_tela_cadastro = QtWidgets.QWidget()
        self.widget_tela_cadastro.setObjectName("widget_tela_cadastro")
        self.tela_cadastro = Ui_Tela_Cadastro()
        self.tela_cadastro.setupUi(self.widget_tela_cadastro)

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_tela_cadastro)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stack_telas.addWidget(self.widget_tela_cadastro)

        # -------------tela saque------------------
        self.widget_tela_saque = QtWidgets.QWidget()
        self.widget_tela_saque.setObjectName("widget_tela_saque")
        self.tela_saque = Ui_Tela_Saque()
        self.tela_saque.setupUi(self.widget_tela_saque)

        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_tela_saque)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.stack_telas.addWidget(self.widget_tela_saque)

        # -------------tela transferencia------------------
        self.widget_tela_transferencia = QtWidgets.QWidget()
        self.widget_tela_transferencia.setObjectName("widget_tela_transferencia")
        self.tela_transferencia = Ui_Tela_Transferencia()
        self.tela_transferencia.setupUi(self.widget_tela_transferencia)

        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_tela_transferencia)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.stack_telas.addWidget(self.widget_tela_transferencia)

        # -------------tela deposito------------------
        self.widget_tela_deposito = QtWidgets.QWidget()
        self.widget_tela_deposito.setObjectName("widget_tela_deposito")
        self.tela_deposito = Ui_Tela_Deposito()
        self.tela_deposito.setupUi(self.widget_tela_deposito)

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_tela_deposito)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stack_telas.addWidget(self.widget_tela_deposito)

        # -------------tela extrato------------------
        self.widget_tela_extrato = QtWidgets.QWidget()
        self.widget_tela_extrato.setObjectName("widget_tela_extrato")
        self.tela_extrato = Ui_Tela_Extrato()
        self.tela_extrato.setupUi(self.widget_tela_extrato)

        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_tela_extrato)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.stack_telas.addWidget(self.widget_tela_extrato)


    #ao clicar no botão de salvar na tela de cadastro
    def salvar_novo_cadastro(self):

        nome = self.tela_cadastro.le_cad_nome.text()
        sobre_nome = self.tela_cadastro.le_cad_sobrenome.text()
        cpf = self.tela_cadastro.le_cad_cpf.text()
        senha = self.tela_cadastro.le_cad_senha.text()

        if nome == '' or sobre_nome == '' or cpf  == '' or senha == '':
            Dialogs.alert_mensage('⚠ Algun(s) campo(s) estão vazio(s) ', "ERRO")
        else:
            cliente = Cliente(nome, sobre_nome, cpf)
            conta = Conta(cliente, senha)
            if self.contas.salvar_conta(conta):
                Dialogs.alert_mensage("✅ Cadastro realizado com sucesso. ", "OK")
                Dialogs.alert_mensage(f"✅ Número da sua conta é: {conta.numero}", "OK")
            else:
                Dialogs.alert_mensage('⚠ Erro na criação da conta. Tente Novamente mais tarde ', "ERRO")

            self.limpar_campos()
            self.goto_tela_apresentacao()

    #ao clicar no botão "sacar" da tela de saque
    def realizar_deposito(self):
        if self._tempConta is not None:
            if self.tela_deposito.le_dep_valor.text() != '':
                try:
                    valor_deposito = float(self.tela_deposito.le_dep_valor.text())

                    self._tempConta.depositar(valor_deposito)
                    Dialogs.alert_mensage("✔ Deposito realizado com sucesso", "OK")
                    novo_deposito = Dialogs.confirmation_mensage("Deseja relizar outro deposito ? ", "Novo deposito")
                    if novo_deposito is False:
                        self.goto_tela_apresentacao()

                except:
                    Dialogs.alert_mensage("⚠ Valor informado invalido", "ERRO")
            else:
                Dialogs.alert_mensage("⚠ Campo de saldo vazio", "ERRO")

    def realizar_saque(self):

        if self._tempConta is not None:
            if self.tela_saque.le_saque_valor.text() != '':
                try:
                    valor_saque = float(self.tela_saque.le_saque_valor.text())
                    sacou = self._tempConta.sacar(valor_saque)

                    if sacou:
                        Dialogs.alert_mensage(f"✅ Saque realizado com sucesso. Saldo restante na conta: R$ {self._tempConta.saldo}", "OK")
                        novo_saque = Dialogs.confirmation_mensage("Deseja relizar outro saque ? ", "Novo Saque")

                        if novo_saque is False:
                            self.goto_tela_apresentacao()
                    else:
                        Dialogs.alert_mensage(f"⚠ Saque não realizado! Por favor, confira o valor informado. Saldo disponivel na conta: R$ {self._tempConta.saldo}", "ERRO")
                        novo_saque = Dialogs.confirmation_mensage("Deseja tentar novamente com um novo valor ? ", "Novo Saque")

                        if novo_saque is False:
                            self.goto_tela_apresentacao()
                except:
                    Dialogs.alert_mensage("⚠ Valor informado invalido", "ERRO")
            else:
                Dialogs.alert_mensage("⚠ Campo de saldo vazio", "ERRO")

    def realizar_transferencia(self):
        try:
            numero_conta = self.tela_transferencia.le_tran_conta.text()
            valor = float(self.tela_transferencia.le_tran_valor_transferencia.text())
            if(numero_conta != ''):
                if(valor > 0):
                    conta_destino = self.contas.get_conta_numero(numero_conta)
                    if(conta_destino != None):
                        if(self._tempConta.transfere(conta_destino,valor) is True):
                            Dialogs.alert_mensage(f"✅ Transferencia realizada com sucesso. Saldo restante na conta: R$ {self._tempConta.saldo}", "OK")
                            nova_transferencia = Dialogs.confirmation_mensage("Deseja relizar outra transferencia? ", "Nova Transferencia")
                            if(nova_transferencia is False):
                                self.goto_tela_apresentacao()
                        else:
                             Dialogs.alert_mensage(f"⚠ Transferencia não realizada! Saldo insuficiente", "ERRO")
                    else:
                        Dialogs.alert_mensage(f"⚠ Transferencia não realizada! Conta destino não encontrada", "ERRO")
                        nova_transferencia = Dialogs.confirmation_mensage("Deseja tentar novamente? ", "Nova Transferencia")
                        if(nova_transferencia is False):
                            self.goto_tela_apresentacao()
                else:
                    Dialogs.alert_mensage("⚠ Valor informado invalido", "ERRO")
            else:
                Dialogs.alert_mensage("⚠ Valor informado invalido", "ERRO")
        except:
            Dialogs.alert_mensage("⚠ Valor informado invalido", "ERRO")


    def set_tela(self):

        cpf = self.tela_autenticacao.le_aut_cpf.text()
        senha = self.tela_autenticacao.le_aut_senha.text()

        self._tempConta = self.contas.get_conta_cpf(cpf)

        if self._tempConta is not None and senha == self._tempConta.senha:

            if self.tela_index == 3:
                self.tela_saque.lbl_saque_usuario.setText(f"Cliente: {self._tempConta.titular.nome} {self._tempConta.titular.sobre_node}")
                self.stack_telas.setCurrentIndex(3)

            elif self.tela_index == 4:
                self.tela_transferencia.lbl_tran_usuario.setText(f"Cliente: {self._tempConta.titular.nome} {self._tempConta.titular.sobre_node}")
                self.stack_telas.setCurrentIndex(4)

            elif self.tela_index == 5:
                self.tela_deposito.lbl_dep_usuario.setText(f"Cliente: {self._tempConta.titular.nome} {self._tempConta.titular.sobre_node}")
                self.stack_telas.setCurrentIndex(5)

            elif self.tela_index == 6:
                self.tela_extrato.lbl_extr_usuario.setText(f"Cliente: {self._tempConta.titular.nome} {self._tempConta.titular.sobre_node}")
                for historico in self._tempConta._historico.historico_transacoes:
                    self.tela_extrato.lw_extrato.addItem(self.tela_extrato.create_item(historico))

                self.stack_telas.setCurrentIndex(6)

            elif self.tela_index == 7:
                pass

            self.limpar_campos()
        else:
            Dialogs.alert_mensage("⚠️Usuario ou senha invalidos", "ERRO")

    def exibir_password(self):
        if(self.show_password_flag == True):
            self.tela_cadastro.le_cad_senha.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.show_password_flag = False
        else:
            self.tela_cadastro.le_cad_senha.setEchoMode(QtWidgets.QLineEdit.Password)
            self.show_password_flag = True


    def acoes_botoes(self):
        self.btn_goto_tela_cadastro.clicked.connect(self.goto_tela_cadastro)
        self.btn_goto_tela_saque.clicked.connect(self.goto_tela_saque)
        self.btn_goto_tela_transferencia.clicked.connect(self.goto_tela_transferencia)
        self.btn_goto_tela_deposito.clicked.connect(self.goto_tela_deposito)
        self.btn_goto_tela_extrato.clicked.connect(self.goto_tela_extrato)
        self.btn_got_tela_ajuda.clicked.connect(self.goto_tela_ajuda)

        self.tela_autenticacao.btn_aut_confirmar.clicked.connect(self.set_tela)
        self.tela_cadastro.btn_cad_salvar.clicked.connect(self.salvar_novo_cadastro)
        self.tela_cadastro.btn_cad_exibir_senha.clicked.connect(self.exibir_password)
        self.tela_deposito.btn_dep_depositar.clicked.connect(self.realizar_deposito)

        self.tela_autenticacao.btn_aut_cancelar.clicked.connect(self.goto_tela_apresentacao)
        self.tela_cadastro.btn_cad_cancelar.clicked.connect(self.goto_tela_apresentacao)
        self.tela_saque.btn_saque_cancelar.clicked.connect(self.goto_tela_apresentacao)
        self.tela_transferencia.btn_tran_cancelar.clicked.connect(self.goto_tela_apresentacao)
        self.tela_deposito.btn_dep_cancelar.clicked.connect(self.goto_tela_apresentacao)
        self.tela_extrato.btn_ext_fechar.clicked.connect(self.goto_tela_apresentacao)

        self.tela_saque.btn_saque_confirmar.clicked.connect(self.realizar_saque)

        self.tela_transferencia.btn_tran_transferir.clicked.connect(self.realizar_transferencia)

    def limpar_campos(self):

        #tela autenticacao
        self.tela_autenticacao.le_aut_cpf.setText('')
        self.tela_autenticacao.le_aut_senha.setText('')

        #tela cadastro
        self.tela_cadastro.le_cad_nome.setText('')
        self.tela_cadastro.le_cad_sobrenome.setText('')
        self.tela_cadastro.le_cad_cpf.setText('')
        self.tela_cadastro.le_cad_senha.setText('')

        # tela saque
        self.tela_saque.le_saque_valor.setText('')
        #tela deposito
        self.tela_deposito.le_dep_valor.setText('')
        # tela transferencia
        self.tela_transferencia.le_tran_conta.setText('')
        # self.tela_transferencia.le_tran_agencia.setText('')
        self.tela_transferencia.le_tran_valor_transferencia.setText('')
        # tela extrato


    def goto_tela_apresentacao(self):
        Dialogs.alert_mensage("Operação finalizada ✅", "finalizado")
        self.tela_index = 0
        self._tempConta = None
        self.stack_telas.setCurrentIndex(0)
        self.reset_botoes_acoes()
        self.limpar_campos()
        self.tela_extrato.lw_extrato.clear()

    def goto_tela_autenticacao(self):
        self.stack_telas.setCurrentIndex(1)

    def goto_tela_cadastro(self):
        self.stack_telas.setCurrentIndex(2)
        self.set_estilo_clique("cadastro")

    def goto_tela_saque(self):
        self.goto_tela_autenticacao()
        self.set_estilo_clique("saque")
        self.tela_index = 3

    def goto_tela_transferencia(self):
        self.goto_tela_autenticacao()
        self.set_estilo_clique("transferencia")
        self.tela_index = 4

    def goto_tela_deposito(self):
        self.goto_tela_autenticacao()
        self.set_estilo_clique("deposito")
        self.tela_index = 5

    def goto_tela_extrato(self):
        self.goto_tela_autenticacao()
        self.set_estilo_clique("extrato")
        self.tela_index = 6

    def goto_tela_ajuda(self):
        self.goto_tela_autenticacao()
        self.set_estilo_clique("ajuda")
        self.tela_index = 7

    def setupUi(self, MainHomePage):
        MainHomePage.setObjectName("MainHomePage")
        MainHomePage.setWindowModality(QtCore.Qt.NonModal)
        MainHomePage.resize(1200, 600)
        MainHomePage.setMinimumSize(QtCore.QSize(1200, 600))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        MainHomePage.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Assets/ico.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainHomePage.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainHomePage)
        self.centralwidget.setStyleSheet("background-color: #F4F5F7;")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.navegacao = QtWidgets.QFrame(self.centralwidget)
        self.navegacao.setMinimumSize(QtCore.QSize(160, 0))
        self.navegacao.setStyleSheet("background-color: #333333;")
        self.navegacao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navegacao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navegacao.setObjectName("navegacao")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.navegacao)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.logo = QtWidgets.QPushButton(self.navegacao)
        self.logo.setStyleSheet("background-color: transparent; color: white; font-weight: bold; font-size: 20px; text-align: left;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Assets/money.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logo.setIcon(icon1)
        self.logo.setFlat(True)
        self.logo.setIconSize(QtCore.QSize(32, 32))
        self.logo.setObjectName("logo")
        self.horizontalLayout_5.addWidget(self.logo)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.btn_goto_tela_cadastro = QtWidgets.QPushButton(self.navegacao)
        self.btn_goto_tela_cadastro.setStyleSheet(self.estilo.estilo_botao_navegacao())
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./Assets/website.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_goto_tela_cadastro.setIcon(icon2)
        self.btn_goto_tela_cadastro.setIconSize(QtCore.QSize(20, 20))
        self.btn_goto_tela_cadastro.setFlat(False)
        self.btn_goto_tela_cadastro.setObjectName("btn_goto_tela_cadastro")
        self.verticalLayout.addWidget(self.btn_goto_tela_cadastro)
        self.btn_goto_tela_saque = QtWidgets.QPushButton(self.navegacao)
        self.btn_goto_tela_saque.setStyleSheet(self.estilo.estilo_botao_navegacao())
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./Assets/withdraw.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_goto_tela_saque.setIcon(icon3)
        self.btn_goto_tela_saque.setIconSize(QtCore.QSize(20, 20))
        self.btn_goto_tela_saque.setFlat(True)
        self.btn_goto_tela_saque.setObjectName("btn_goto_tela_saque")
        self.verticalLayout.addWidget(self.btn_goto_tela_saque)
        self.btn_goto_tela_transferencia = QtWidgets.QPushButton(self.navegacao)
        self.btn_goto_tela_transferencia.setStyleSheet(self.estilo.estilo_botao_navegacao())
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./Assets/money-transfer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_goto_tela_transferencia.setIcon(icon4)
        self.btn_goto_tela_transferencia.setIconSize(QtCore.QSize(20, 20))
        self.btn_goto_tela_transferencia.setFlat(True)
        self.btn_goto_tela_transferencia.setObjectName("btn_goto_tela_transferencia")
        self.verticalLayout.addWidget(self.btn_goto_tela_transferencia)
        self.btn_goto_tela_deposito = QtWidgets.QPushButton(self.navegacao)
        self.btn_goto_tela_deposito.setStyleSheet(self.estilo.estilo_botao_navegacao())
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./Assets/savings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_goto_tela_deposito.setIcon(icon5)
        self.btn_goto_tela_deposito.setIconSize(QtCore.QSize(20, 20))
        self.btn_goto_tela_deposito.setFlat(True)
        self.btn_goto_tela_deposito.setObjectName("btn_goto_tela_deposito")
        self.verticalLayout.addWidget(self.btn_goto_tela_deposito)
        self.btn_goto_tela_extrato = QtWidgets.QPushButton(self.navegacao)
        self.btn_goto_tela_extrato.setStyleSheet(self.estilo.estilo_botao_navegacao())
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./Assets/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_goto_tela_extrato.setIcon(icon6)
        self.btn_goto_tela_extrato.setIconSize(QtCore.QSize(20, 20))
        self.btn_goto_tela_extrato.setFlat(True)
        self.btn_goto_tela_extrato.setObjectName("btn_goto_tela_extrato")
        self.verticalLayout.addWidget(self.btn_goto_tela_extrato)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.btn_got_tela_ajuda = QtWidgets.QPushButton(self.navegacao)
        self.btn_got_tela_ajuda.setStyleSheet(self.estilo.estilo_botao_navegacao())
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./Assets/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_got_tela_ajuda.setIcon(icon7)
        self.btn_got_tela_ajuda.setIconSize(QtCore.QSize(25, 25))
        self.btn_got_tela_ajuda.setShortcut("")
        self.btn_got_tela_ajuda.setFlat(True)
        self.btn_got_tela_ajuda.setObjectName("btn_got_tela_ajuda")
        self.verticalLayout.addWidget(self.btn_got_tela_ajuda)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.navegacao)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)

        self.stack_telas = QtWidgets.QStackedWidget(self.centralwidget)
        self.stack_telas.setObjectName("stack_telas")

        self.horizontalLayout.addWidget(self.stack_telas)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainHomePage.setCentralWidget(self.centralwidget)

        self.setup_telas()
        self.acoes_botoes()

        self.retranslateUi(MainHomePage)
        self.stack_telas.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainHomePage)

    def retranslateUi(self, MainHomePage):
        _translate = QtCore.QCoreApplication.translate
        MainHomePage.setWindowTitle(_translate("MainHomePage", "Banco Real"))
        self.logo.setText(_translate("MainHomePage", "  Banco real"))
        self.btn_goto_tela_cadastro.setText(_translate("MainHomePage", "   Cadastro"))
        self.btn_goto_tela_saque.setText(_translate("MainHomePage", "   Saque"))
        self.btn_goto_tela_transferencia.setText(_translate("MainHomePage", "   Transferencia"))
        self.btn_goto_tela_deposito.setText(_translate("MainHomePage", "   Deposito"))
        self.btn_goto_tela_extrato.setText(_translate("MainHomePage", "   Extrato"))
        self.btn_got_tela_ajuda.setText(_translate("MainHomePage", "   Ajuda"))
