# Form implementation generated from reading ui file 'c:\Users\Said\Desktop\HP QT\GUI\Diag.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Diagnostico(object):
    def setupUi(self, Diagnostico):
        Diagnostico.setObjectName("Diagnostico")
        Diagnostico.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        Diagnostico.resize(730, 379)
        self.home = QtWidgets.QLabel(parent=Diagnostico)
        self.home.setGeometry(QtCore.QRect(0, 0, 731, 381))
        self.home.setText("")
        self.home.setPixmap(QtGui.QPixmap("c:\\Users\\Said\\Desktop\\HP QT\\GUI\\../imagen/consulta.png"))
        self.home.setScaledContents(True)
        self.home.setObjectName("home")
        self.sig = QtWidgets.QPushButton(parent=Diagnostico)
        self.sig.setGeometry(QtCore.QRect(481, 268, 77, 93))
        self.sig.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.sig.setAutoFillBackground(False)
        self.sig.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Said\\Desktop\\HP QT\\GUI\\../imagen/siguiente.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.sig.setIcon(icon)
        self.sig.setIconSize(QtCore.QSize(265, 160))
        self.sig.setAutoDefault(True)
        self.sig.setFlat(True)
        self.sig.setObjectName("sig")
        self.pushButton = QtWidgets.QPushButton(parent=Diagnostico)
        self.pushButton.setGeometry(QtCore.QRect(655, 110, 61, 61))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\Said\\Desktop\\HP QT\\GUI\\../imagen/home.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(60, 60))
        self.pushButton.setAutoDefault(True)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Diagnostico)
        QtCore.QMetaObject.connectSlotsByName(Diagnostico)

    def retranslateUi(self, Diagnostico):
        _translate = QtCore.QCoreApplication.translate
        Diagnostico.setWindowTitle(_translate("Diagnostico", "Diagnostico"))
