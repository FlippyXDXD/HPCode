# Form implementation generated from reading ui file 'c:\Users\Said\Desktop\HP QT\GUI\Ctrl.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Control(object):
    def setupUi(self, Control):
        Control.setObjectName("Control")
        Control.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        Control.resize(640, 423)
        self.label = QtWidgets.QLabel(parent=Control)
        self.label.setGeometry(QtCore.QRect(-2, -5, 641, 431))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("c:\\Users\\Said\\Desktop\\HP QT\\GUI\\../imagen/control.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(parent=Control)
        self.textEdit.setGeometry(QtCore.QRect(168, 228, 186, 163))
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setStyleSheet("background-color: rgb(68, 196, 124);")
        self.textEdit.setObjectName("textEdit")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=Control)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(167, 76, 187, 124))
        self.plainTextEdit.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(68, 196, 124);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalScrollBar = QtWidgets.QScrollBar(parent=Control)
        self.verticalScrollBar.setGeometry(QtCore.QRect(620, 84, 20, 304))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(parent=Control)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(620, 90, 20, 301))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.label_2 = QtWidgets.QLabel(parent=Control)
        self.label_2.setGeometry(QtCore.QRect(41, 75, 106, 112))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("c:\\Users\\Said\\Desktop\\HP QT\\GUI\\../../../Downloads/chihuahua.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Control)
        self.label_3.setGeometry(QtCore.QRect(40, 190, 101, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(parent=Control)
        self.pushButton.setGeometry(QtCore.QRect(62, 323, 61, 61))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Said\\Desktop\\HP QT\\GUI\\../imagen/home.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(60, 60))
        self.pushButton.setAutoDefault(True)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Control)
        QtCore.QMetaObject.connectSlotsByName(Control)

    def retranslateUi(self, Control):
        _translate = QtCore.QCoreApplication.translate
        Control.setWindowTitle(_translate("Control", "Control Medico"))
        self.plainTextEdit.setPlainText(_translate("Control", "Cuida bien a tu perro (:"))
        self.label_3.setText(_translate("Control", "Nombre del perro"))
