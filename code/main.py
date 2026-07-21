from mainWindow import Ui_MainWindow

from PyQt6.QtWidgets import QMainWindow, QApplication

class mainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Particle in a box probability program")


if __name__ == "__main__":
    app = QApplication([])
    mainWindow = mainWindow()
    mainWindow.show()
    app.exec()
