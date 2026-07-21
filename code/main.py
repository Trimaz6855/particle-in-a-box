from mainWindow import Ui_MainWindow

from plot2Dim import plot_2d_prob_density, plot_2d_wave_function

from PyQt6.QtWidgets import QMainWindow, QApplication

class mainWindow(QMainWindow):

    # Constructor method
    def __init__(self):

        # Main window setup
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Particle in a box probability program")

        # Arrow button setup
        self.ui.btnNext.clicked.connect(self.next)
        self.ui.btnPrev.clicked.connect(self.prev)
        
        # 2 Dimensional setup
        self.ui.btnProb2Dim.clicked.connect(self.display_2d_prob)

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

    # 2 Dimensional display function
    def display_2d_prob(self):
        l_x, l_y, n_x, n_y = int(self.ui.lnLx2Dim.text()), int(self.ui.lnLy2Dim.text()), int(self.ui.lnNx2Dim.text()), int(self.ui.lnNy2Dim.text())
        plot_2d_prob_density(l_x, l_y, n_x, n_y)

if __name__ == "__main__":
    app = QApplication([])
    mainWindow = mainWindow()
    mainWindow.show()
    app.exec()
