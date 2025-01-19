from PyQt6.QtWidgets import QMainWindow, QMessageBox
from Registro_ui import Ui_dlg_Registrar
from Regcuidador import Regcuidador
import sqlite3

class RegistrationPage(QMainWindow, Ui_dlg_Registrar):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        
        # Botones conectados a funciones
        self.sig.clicked.connect(self.goto_regcuidador)  # Botón "->"
        self.ant.clicked.connect(self.goto_parent)    # Botón "<-"

    def goto_regcuidador(self):
        # Capturar datos del cachorro
        name = self.Nombre.text().strip()  # Corresponde al campo "Nombre"
        breed = self.raza.currentText()  # Corresponde al ComboBox "raza"
        gender = "Masculino" if self.radioButtonmale.isChecked() else "Femenino" if self.radioButtonfemale.isChecked() else ""

        # Validar los campos requeridos
        if not name or not gender:
            QMessageBox.warning(self, "Error", "Por favor completa todos los campos requeridos.")
            return

        # Abrir la ventana de registro del cuidador y pasar los datos
        try:
            self.regcuidador = Regcuidador(self.parent, name, breed, gender)
            self.regcuidador.show()
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error al abrir la ventana de registro del cuidador: {str(e)}")

    def goto_parent(self):
        """Regresa a la ventana principal."""
        self.parent.show()
        self.close()