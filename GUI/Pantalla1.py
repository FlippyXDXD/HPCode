from PyQt6.QtWidgets import QMainWindow
from Pantalla1_ui import Ui_Pantalla1
from Registro_ui import Ui_dlg_Registrar
from Login_ui import Ui_Login
from PyQt6 import QtWidgets

class Pantalla1(QMainWindow, Ui_Pantalla1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login_window = None
        # Conectar botones
        self.RegBtn.clicked.connect(self.open_register)
        self.IniSesBtn.clicked.connect(self.open_login)

    def open_register(self):
        self.register_window = Ui_dlg_Registrar(self)
        self.register_window.show()
        self.hide()

    def open_login(self):
        try:
            if self.login_window is None:  # Si no hay una instancia de Login
                self.login_window = Ui_Login(self)
            self.login_window.show()
            self.hide()
        except Exception as e:
           QtWidgets.QMessageBox.critical(self, "Error", f"Ocurrió un error al abrir la ventana de inicio de sesión: {str(e)}")