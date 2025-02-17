import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Pantalla1_ui import Ui_Pantalla1  # Ventana principal generada por Qt Designer
from Registro import RegistrationPage  # Ventana de registro generada
from Login import Login  # Importa la clase Login

class MainWindow(QMainWindow, Ui_Pantalla1):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)

        # Crear las ventanas
        self.register_window = RegistrationPage(self)  # Ventana de registro del cachorro
        self.login_window = None  # Inicializa la ventana de inicio de sesión como None

        # Conectar los botones de la ventana principal
        self.RegBtn.clicked.connect(self.show_register_window)  # Botón de registro
        self.IniSesBtn.clicked.connect(self.show_login_window)  # Botón de inicio de sesión

    def show_register_window(self):
        """Abre la ventana de registro (Registro del Cachorro)."""
        self.register_window.show()  # Muestra la ventana de registro
        self.hide()  # Oculta la ventana principal

    def show_login_window(self):
        """Abre la ventana de inicio de sesión."""
        if self.login_window is None:  # Si no hay una instancia de Login
            self.login_window = Login()  # Crear una nueva instancia de Login
        self.login_window.show()  # Mostrar la ventana de inicio de sesión
        self.hide()  # Ocultar la ventana principal

# Iniciar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())