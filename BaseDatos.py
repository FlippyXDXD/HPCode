import sqlite3
import os

class Conexion(): 
    def __init__(self): 
        try: 
            # Crear la carpeta 'data' si no existe
            if not os.path.exists("data"):
                os.makedirs("data")
            
            # Ruta completa al archivo de base de datos
            db_path = os.path.join("data", "healthy_puppy.db")
            print(f"Ruta de la base de datos: {db_path}")  # Para verificar la ruta

            # Conectar a la base de datos
            self.conec = sqlite3.connect(db_path) 
            self.crear_tablas() 
        except Exception as ex: 
            print(f"ERROR: Al crear la Base de Datos \n{ex} \n")

    def crear_tablas(self):
        cursor = self.conec.cursor()

        # Crear la tabla de dueños (owners)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS owners (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                Contraseña TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)

        # Crear la tabla de perros (dogs)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS dogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                breed TEXT NOT NULL,
                gender TEXT NOT NULL,
                owner_id INTEGER NOT NULL,
                FOREIGN KEY (owner_id) REFERENCES owners (id)
            )
        """)

        self.conec.commit()
        self.conec.close()
        print("Base de datos creada con éxito.")

# Ejecutar la conexión y creación de tablas
if __name__ == "__main__":
    Conexion()