# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trabalho/inserir.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from trabalho.Banco import *

class Ui_MainWindow(object):
    db = Banco()

    def salvar(self):
        produto = self.comboBox_2.currentText()
        tipo = self.comboBox.currentText()
        quantidade = self.spinBox.value()
        valor = self.doubleSpinBox.value()
        self.db.inserir_produto((produto, tipo, valor, quantidade))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(736, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 0, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 4, 1, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 3, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.salvar)
        self.gridLayout.addWidget(self.pushButton, 6, 1, 1, 1)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 736, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Quantidade:"))
        self.label_3.setText(_translate("MainWindow", "Tipo:"))
        self.label_2.setText(_translate("MainWindow", "Preço unitário:"))
        self.label_4.setText(_translate("MainWindow", "Produto:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Arroz"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Detergente"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Desinfetante"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Água sanitária"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Sabão em Pó"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Sabão em pedra"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Amaciante"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Álcool"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "Lustra móveis"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "Inseticida"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "Saco de Lixo"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "Papel Toalha"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "Feijão"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "Guardanapo"))
        self.comboBox_2.setItemText(14, _translate("MainWindow", "Papel Alumínio"))
        self.comboBox_2.setItemText(15, _translate("MainWindow", "Filme plástico"))
        self.comboBox_2.setItemText(16, _translate("MainWindow", "Açúcar"))
        self.comboBox_2.setItemText(17, _translate("MainWindow", "Esponja de aço"))
        self.comboBox_2.setItemText(18, _translate("MainWindow", "Café"))
        self.comboBox_2.setItemText(19, _translate("MainWindow", "Rodo / vassoura"))
        self.comboBox_2.setItemText(20, _translate("MainWindow", "Fósforo"))
        self.comboBox_2.setItemText(21, _translate("MainWindow", "Vela"))
        self.comboBox_2.setItemText(22, _translate("MainWindow", "Lâmpada"))
        self.comboBox_2.setItemText(23, _translate("MainWindow", "Palito de dente"))
        self.comboBox_2.setItemText(24, _translate("MainWindow", "Filtro para café"))
        self.comboBox_2.setItemText(25, _translate("MainWindow", "Shampoo"))
        self.comboBox_2.setItemText(26, _translate("MainWindow", "Condicionador"))
        self.comboBox_2.setItemText(27, _translate("MainWindow", "Sabonete"))
        self.comboBox_2.setItemText(28, _translate("MainWindow", "Desodorante"))
        self.comboBox_2.setItemText(29, _translate("MainWindow", "Papel higiênico"))
        self.comboBox_2.setItemText(30, _translate("MainWindow", "Creme dental"))
        self.comboBox_2.setItemText(31, _translate("MainWindow", "Fio dental"))
        self.comboBox_2.setItemText(32, _translate("MainWindow", "Escova de dentes"))
        self.comboBox_2.setItemText(33, _translate("MainWindow", "Cotonete"))
        self.comboBox_2.setItemText(34, _translate("MainWindow", "Algodão"))
        self.comboBox_2.setItemText(35, _translate("MainWindow", "Chá"))
        self.comboBox_2.setItemText(36, _translate("MainWindow", "Absorvente"))
        self.comboBox_2.setItemText(37, _translate("MainWindow", "Bife"))
        self.comboBox_2.setItemText(38, _translate("MainWindow", "Carne Moída"))
        self.comboBox_2.setItemText(39, _translate("MainWindow", "Carne de frango"))
        self.comboBox_2.setItemText(40, _translate("MainWindow", "Presunto"))
        self.comboBox_2.setItemText(41, _translate("MainWindow", "Mussarela"))
        self.comboBox_2.setItemText(42, _translate("MainWindow", "Mortadela"))
        self.comboBox_2.setItemText(43, _translate("MainWindow", "Salsicha"))
        self.comboBox_2.setItemText(44, _translate("MainWindow", "Linguiça"))
        self.comboBox_2.setItemText(45, _translate("MainWindow", "Achocolatado"))
        self.comboBox_2.setItemText(46, _translate("MainWindow", "Leite"))
        self.comboBox_2.setItemText(47, _translate("MainWindow", "Pão"))
        self.comboBox_2.setItemText(48, _translate("MainWindow", "Farinha de Trigo"))
        self.comboBox_2.setItemText(49, _translate("MainWindow", "Farinha de Rosca"))
        self.comboBox_2.setItemText(50, _translate("MainWindow", "Amido de Milho"))
        self.comboBox_2.setItemText(51, _translate("MainWindow", "Fermento"))
        self.comboBox_2.setItemText(52, _translate("MainWindow", "Macarrão"))
        self.comboBox_2.setItemText(53, _translate("MainWindow", "Molho de Tomate"))
        self.comboBox_2.setItemText(54, _translate("MainWindow", "Leite condensado"))
        self.comboBox_2.setItemText(55, _translate("MainWindow", "Creme de leite"))
        self.comboBox_2.setItemText(56, _translate("MainWindow", "Gelatina"))
        self.comboBox_2.setItemText(57, _translate("MainWindow", "Ketchup"))
        self.comboBox_2.setItemText(58, _translate("MainWindow", "Maionese"))
        self.comboBox_2.setItemText(59, _translate("MainWindow", "Óleo"))
        self.comboBox_2.setItemText(60, _translate("MainWindow", "Azeite"))
        self.comboBox_2.setItemText(61, _translate("MainWindow", "Vinagre"))
        self.comboBox_2.setItemText(62, _translate("MainWindow", "Tempero Pronto"))
        self.comboBox_2.setItemText(63, _translate("MainWindow", "Alface"))
        self.comboBox_2.setItemText(64, _translate("MainWindow", "Repolho"))
        self.comboBox_2.setItemText(65, _translate("MainWindow", "Vagem"))
        self.comboBox_2.setItemText(66, _translate("MainWindow", "Tomate"))
        self.comboBox_2.setItemText(67, _translate("MainWindow", "Pepino"))
        self.comboBox_2.setItemText(68, _translate("MainWindow", "Cebola"))
        self.comboBox_2.setItemText(69, _translate("MainWindow", "Batata"))
        self.comboBox_2.setItemText(70, _translate("MainWindow", "Cenoura"))
        self.comboBox_2.setItemText(71, _translate("MainWindow", "Pimentão"))
        self.comboBox_2.setItemText(72, _translate("MainWindow", "Chuchu"))
        self.comboBox_2.setItemText(73, _translate("MainWindow", "Limão"))
        self.comboBox_2.setItemText(74, _translate("MainWindow", "Banana"))
        self.comboBox_2.setItemText(75, _translate("MainWindow", "Mamão"))
        self.comboBox_2.setItemText(76, _translate("MainWindow", "Melão"))
        self.comboBox_2.setItemText(77, _translate("MainWindow", "Laranja"))
        self.comboBox_2.setItemText(78, _translate("MainWindow", "Abacaxi"))
        self.comboBox_2.setItemText(79, _translate("MainWindow", "Morango"))
        self.comboBox_2.setItemText(80, _translate("MainWindow", "Maçã"))
        self.comboBox_2.setItemText(81, _translate("MainWindow", "Maracujá"))
        self.comboBox_2.setItemText(82, _translate("MainWindow", "Melancia"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Alimento"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Frutas e Verduras"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Bebidas"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Utilidades / Limpeza"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Higiene"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Açouge / Carnes"))
        self.pushButton.setText(_translate("MainWindow", "Salvar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

