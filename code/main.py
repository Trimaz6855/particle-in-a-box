from mainWindow import Ui_MainWindow

from plot2Dim import plot_2d_prob_density, plot_2d_wave_function

from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox

class mainWindow(QMainWindow):

    # Constructor method
    def __init__(self):

        # Main window setup
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Particle in a box probability program")
        self.ui.swgMain.setCurrentIndex(0)

        # Arrow button setup
        self.ui.btnNext.clicked.connect(self.next)
        self.ui.btnPrev.clicked.connect(self.prev)
        
        # 2 Dimensional setup
        self.ui.btnProb2Dim.clicked.connect(self.display_2d_prob)
        self.ui.btnWave2Dim.clicked.connect(self.display_2d_wave)

    # Arrow next function
    def next(self):
        id_current = self.ui.swgMain.currentIndex()
        if id_current != 2:
            id_current += 1
            self.ui.swgMain.setCurrentIndex(id_current)
        else:
            id_current = 0
            self.ui.swgMain.setCurrentIndex(id_current)
    
    # Arrow previous function
    def prev(self):
        id_current = self.ui.swgMain.currentIndex()
        if id_current != 0:
            id_current -= 1
            self.ui.swgMain.setCurrentIndex(id_current)
        else:
            id_current = 2
            self.ui.swgMain.setCurrentIndex(id_current)

    # 2 Dimensional probabilty display function
    def display_2d_prob(self):
        try:
            l_x, l_y, n_x, n_y = float(self.ui.lnLx2Dim.text()), float(self.ui.lnLy2Dim.text()), int(self.ui.lnNx2Dim.text()), int(self.ui.lnNy2Dim.text())
        except ValueError:
            QMessageBox.information(self, "Error", "The input values for the lengths must be valid floats and the input values for the energy levels must be valid integers!")
        else:
            plot_2d_prob_density(l_x, l_y, n_x, n_y)

    # 2 Dimensional wave function display function
    def display_2d_wave(self):
        try:
            l_x, l_y, n_x, n_y = int(self.ui.lnLx2Dim.text()), int(self.ui.lnLy2Dim.text()), int(self.ui.lnNx2Dim.text()), int(self.ui.lnNy2Dim.text())
        except ValueError:
            QMessageBox.information(self, "Error", "The input values for the lengths must be valid floats and the input values for the energy levels must be valid integers!")
        else:
            plot_2d_wave_function(l_x, l_y, n_x, n_y)

if __name__ == "__main__":
    app = QApplication([])
    mainWindow = mainWindow()
    mainWindow.show()
    app.exec()
