from PySide6.QtWidgets import QApplication, QMainWindow
import sys
from GUI_ui import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)      # Inicializa la interfaz
    MainWindow.show()           # Muestra la ventana
    sys.exit(app.exec())        # Ejecuta el bucle de la app