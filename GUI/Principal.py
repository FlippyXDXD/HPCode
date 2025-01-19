import sys
from PyQt6 import QtWidgets
from Principal_ui import Ui_MainWindow  # Asegúrate de que este archivo esté correctamente importado
from Calen_ui import Ui_Calendario  # Asegúrate de que este archivo esté correctamente importado
from Ctrl_ui import Ui_Control  # Asegúrate de que este archivo esté correctamente importado
from Sobre_perro_ui import Ui_SobrePerro  # Asegúrate de que este archivo esté correctamente importado
from Ajustes_ui import Ui_Ajustes  # Asegúrate de que este archivo esté correctamente importado
from diag import Dianostico

class Principal(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Conectar botones a sus respectivas funciones
        self.Diagnostico.clicked.connect(self.open_diagnostico_window)
        self.Calendario.clicked.connect(self.open_calendario_window)
        self.ctrl_med.clicked.connect(self.open_control_medico_window)
        self.info_perro.clicked.connect(self.open_info_perro_window)
        self.config.clicked.connect(self.open_config_window)

    def open_diagnostico_window(self):
        self.diag_window = Dianostico()  # Crear una nueva instancia de Dianostico
        self.diag_window.show()  # Mostrar la ventana de diagnóstico

    def open_calendario_window(self):
        self.cal_window = QtWidgets.QMainWindow()  # Crear una nueva ventana
        self.cal_ui = Ui_Calendario()  # Crear la interfaz de la ventana de calendario
        self.cal_ui.setupUi(self.cal_window)  # Configurar la interfaz
        self.cal_window.show()  # Mostrar la ventana

    def open_control_medico_window(self):
        self.control_window = QtWidgets.QMainWindow()  # Crear una nueva ventana
        self.control_ui = Ui_Control()  # Crear la interfaz de la ventana de control médico
        self.control_ui.setupUi(self.control_window)  # Configurar la interfaz
        self.control_window.show()  # Mostrar la ventana

    def open_info_perro_window(self):
        self.info_window = QtWidgets.QMainWindow()  # Crear una nueva ventana
        self.info_ui = Ui_SobrePerro()  # Crear la interfaz de la ventana de información del perro
        self.info_ui.setupUi(self.info_window)  # Configurar la interfaz
        self.info_window.show()  # Mostrar la ventana

    def open_config_window(self):
        self.config_window = QtWidgets.QMainWindow()  # Crear una nueva ventana
        self.config_ui = Ui_Ajustes()  # Crear la interfaz de la ventana de configuración
        self.config_ui.setupUi(self.config_window)  # Configurar la interfaz
        self.config_window.show()  # Mostrar la ventana

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Principal()
    main_window.show()
    sys.exit(app.exec())