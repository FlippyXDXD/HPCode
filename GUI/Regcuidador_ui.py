# Form implementation generated from reading ui file 'c:\Users\Said\Desktop\HP QT\GUI\Regcuidador.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(443, 300)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: rgb(62, 178, 113);")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(370, 230, 61, 61))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Said\\Desktop\\HP QT\\GUI\\../imagen/siguiente.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(250, 120))
        self.pushButton.setAutoDefault(True)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(-10, 0, 451, 311))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("c:\\Users\\Said\\Desktop\\HP QT\\GUI\\../imagen/cuidador.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.nombre = QtWidgets.QLineEdit(parent=Dialog)
        self.nombre.setGeometry(QtCore.QRect(99, 91, 221, 21))
        self.nombre.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.nombre.setObjectName("nombre")
        self.correo = QtWidgets.QLineEdit(parent=Dialog)
        self.correo.setGeometry(QtCore.QRect(16, 190, 341, 21))
        self.correo.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.correo.setText("")
        self.correo.setObjectName("correo")
        self.pasw = QtWidgets.QLineEdit(parent=Dialog)
        self.pasw.setGeometry(QtCore.QRect(145, 235, 181, 22))
        self.pasw.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pasw.setObjectName("pasw")
        self.edad = QtWidgets.QSpinBox(parent=Dialog)
        self.edad.setGeometry(QtCore.QRect(75, 129, 42, 22))
        self.edad.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.edad.setObjectName("edad")
        self.label.raise_()
        self.pushButton.raise_()
        self.nombre.raise_()
        self.correo.raise_()
        self.pasw.raise_()
        self.edad.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "GJAS: CUIDADOR"))
        self.nombre.setPlaceholderText(_translate("Dialog", "Usuario"))
        self.correo.setPlaceholderText(_translate("Dialog", "abcdefg@gmail.com"))
        self.pasw.setPlaceholderText(_translate("Dialog", "*********"))
