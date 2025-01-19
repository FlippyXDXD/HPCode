from Diag_ui import Ui_Diagnostico
from PyQt6 import QtWidgets
from resultado_ui import Ui_Resultado
import sys

class Dianostico(QtWidgets.QMainWindow, Ui_Diagnostico):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sig.clicked.connect(self.mostrar_resultado)
    
    def mostrar_resultado(self):
        self.diag_window = QtWidgets.QMainWindow()  # Crear una nueva ventana
        self.diag_ui = Ui_Resultado()  # Crear la interfaz de la ventana de diagnóstico
        self.diag_ui.setupUi(self.diag_window)  # Configurar la interfaz
        self.diag_window.show()  # Mostrar la ventana de resultados
        self.hide()  # Ocultar la ventana principal
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Dianostico()
    main_window.show()
    sys.exit(app.exec())
        