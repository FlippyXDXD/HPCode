import sys
from PyQt6 import QtWidgets
import sqlite3
from Login_ui import Ui_Login  # Asegúrate de que este archivo esté correctamente importado
from Pantalla1 import Pantalla1  # Asegúrate de que este archivo esté correctamente importado 

class Login(QtWidgets.QMainWindow, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sig.clicked.connect(self.handle_login)  # Conectar el botón de inicio de sesión
        self.ant.clicked.connect(self.go_back)  # Conectar el botón "ant" para regresar a Pantalla1

    def handle_login(self):
        username = self.ingresar_user.text()
        password = self.ingresar_passw.text()

        # Validar que los campos no estén vacíos
        if not username or not password:
            QtWidgets.QMessageBox.warning(self, "Error", "Por favor completa todos los campos.")
            return

        # Conectar a la base de datos y verificar las credenciales
        connection = sqlite3.connect("data/healthy_puppy.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM owners WHERE name = ? AND Contraseña = ?", (username, password))
        result = cursor.fetchone()

        connection.close()

        if result:
            QtWidgets.QMessageBox.information(self, "Éxito", "Inicio de sesión exitoso.")
            self.open_main_window()
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Credenciales incorrectas.")

    def open_main_window(self):
        """Abre la ventana principal."""
        from Principal import Principal  # Asegúrate de que este archivo esté correctamente importado
        self.main_window = Principal()  # Crear una nueva instancia de Principal
        self.main_window.show()  # Mostrar la ventana principal
        self.close()  # Cierra la ventana de login

    def go_back(self):
        """Reg resa a Pantalla1."""
        self.pantalla1 = Pantalla1()  # Crear una instancia de Pantalla1
        self.pantalla1.show()  # Mostrar Pantalla1
        self.close()  # Cerrar la ventana de login

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec())