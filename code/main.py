from mainWindow import Ui_MainWindow

from plot1Dim import plot_1d_prob_density, plot_1d_wave_function
from plot2Dim import plot_2d_prob_density, plot_2d_wave_function
from plot3Dim import plot_3d_prob_density, plot_3d_wave_function

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

        # 1 Dimensional setup
        self.ui.btnProb1Dim.clicked.connect(self.display_1d_prob)
        self.ui.btnWave1Dim.clicked.connect(self.display_1d_wave)
        
        # 2 Dimensional setup
        self.ui.btnProb2Dim.clicked.connect(self.display_2d_prob)
        self.ui.btnWave2Dim.clicked.connect(self.display_2d_wave)

        # 3 Dimensional setup
        self.ui.btnProb3Dim.clicked.connect(self.display_3d_prob)
        self.ui.btnWave3Dim.clicked.connect(self.display_3d_wave)

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

    # 1 Dimensional probability density display function
    def display_1d_prob(self):
        try:
            l_x, n_x = float(self.ui.lnLx1Dim.text()), int(self.ui.lnNx1Dim.text())
        except ValueError:
            QMessageBox.information(self, "Error", "The input value for the length of the box must be a valid float and the value for the energy level must be a valid integer!")
        else:
            plot_1d_prob_density(l_x, n_x)

    # 1 Dimensional wave function display function
    def display_1d_wave(self):
        try:
            l_x, n_x = float(self.ui.lnLx1Dim.text()), int(self.ui.lnNx1Dim.text())
        except ValueError:
            QMessageBox.information(self, "Error", "The input value for the length of the box must be a valid float and the value for the energy level must be a valid integer!")
        else:
            plot_1d_wave_function(l_x, n_x)

    # 2 Dimensional probabilty density display function
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
            l_x, l_y, n_x, n_y = float(self.ui.lnLx2Dim.text()), float(self.ui.lnLy2Dim.text()), int(self.ui.lnNx2Dim.text()), int(self.ui.lnNy2Dim.text())
        except ValueError:
            QMessageBox.information(self, "Error", "The input values for the lengths must be valid floats and the input values for the energy levels must be valid integers!")
        else:
            plot_2d_wave_function(l_x, l_y, n_x, n_y)
    
    # 3 Dimensional probability density display function
    def display_3d_prob(self):
        try:
            l_x, l_y, l_z, n_x, n_y, n_z = float(self.ui.lnLx3Dim.text()), float(self.ui.lnLy3Dim.text()), float(self.ui.lnLz3Dim.text()), int(self.ui.lnNx3Dim.text()), int(self.ui.lnNy3Dim.text()), int(self.ui.lnNz3Dim.text())
        except ValueError:
            QMessageBox.information(self, "Error", "The input values for the lengths must be valid floats and the input values for the energy levels must be valid integers!")
        else:
            plot_3d_prob_density(l_x, l_y, l_z, n_x, n_y, n_z)

    # 3 Dimensional wave function display function
    def display_3d_wave(self):
        try:
            l_x, l_y, l_z, n_x, n_y, n_z = float(self.ui.lnLx3Dim.text()), float(self.ui.lnLy3Dim.text()), float(self.ui.lnLz3Dim.text()), int(self.ui.lnNx3Dim.text()), int(self.ui.lnNy3Dim.text()), int(self.ui.lnNz3Dim.text())
        except ValueError:
            QMessageBox.information(self, "Error", "The input values for the lengths must be valid floats and the input values for the energy levels must be valid integers!")
        else:
            plot_3d_wave_function(l_x, l_y, l_z, n_x, n_y, n_z)    

if __name__ == "__main__":
    app = QApplication([])
    mainWindow = mainWindow()
    mainWindow.show()
    app.exec()
