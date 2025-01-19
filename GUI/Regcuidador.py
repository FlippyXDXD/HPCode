from PyQt6.QtWidgets import QMainWindow, QMessageBox
from Regcuidador_ui import Ui_Dialog  # Interfaz de la ventana de registro del cuidador generada
import sqlite3

class Regcuidador(QMainWindow, Ui_Dialog):
    def __init__(self, parent, dog_name, dog_breed, dog_gender):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.dog_name = dog_name
        self.dog_breed = dog_breed
        self.dog_gender = dog_gender

        # Conectar el botón "Siguiente" para guardar los datos
        self.pushButton.clicked.connect(self.save_data)

    

    def save_data(self):
        # Capturar los datos del dueño
        owner_name = self.nombre.text()
        owner_email = self.correo.text()
        owner_password = self.pasw.text()
        owner_age = self.edad.value()

        # Validar los campos
        if not owner_name or not owner_email or not owner_password:
            QMessageBox.warning(self, "Error", "Por favor completa todos los campos requeridos.")
            return

        # Guardar en la base de datos
        connection = sqlite3.connect("data/healthy_puppy.db")
        cursor = connection.cursor()

        cursor.execute("INSERT INTO owners (name, Contraseña, email) VALUES (?, ?, ?)",
                       (owner_name, owner_password, owner_email))
        owner_id = cursor.lastrowid

        cursor.execute("INSERT INTO dogs (name, breed, gender, owner_id) VALUES (?, ?, ?, ?)",
                       (self.dog_name, self.dog_breed, self.dog_gender, owner_id))

        connection.commit()
        connection.close()

        QMessageBox.information(self, "Éxito", "Datos guardados exitosamente. Ahora inicie sesion")
        self.parent.show()
        self.close()

    def return_to_parent(self):
        """Regresa a la ventana principal."""
        self.parent.show()
        self.close()
