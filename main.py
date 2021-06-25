from PySide6.QtCore import QLine, QPoint, Qt, QTimer, Slot, Signal
from PySide6.QtWidgets import QApplication, QWidget, QFrame
from PySide6.QtGui import QPainter
from PySide6 import QtGui

from box import Ui_boxDraw




class BoxDraw(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_boxDraw()
        self.ui.setupUi(self)

        self.ui.stopBox.valueChanged.connect(self.ui.canvas.update_stop)
        self.ui.rotateBox.valueChanged.connect(self.ui.canvas.update_rotate)
        self.ui.speedBox.valueChanged.connect(self.ui.canvas.update_speed)
        self.ui.goBtn.clicked.connect(self.ui.canvas.go_toggle)
        self.ui.clearBtn.clicked.connect(self.ui.canvas.do_clear)
        self.ui.colorBox.valueChanged.connect(self.ui.canvas.update_color)
        self.ui.globalCheck.toggled.connect(self.ui.canvas.update_global_color)
        self.ui.penWidthBox.valueChanged.connect(self.ui.canvas.update_pen_width)

    def set_points(self, points):
        self.ui.canvas.set_points(points)




if __name__ == "__main__":

    app = QApplication([])

    w = BoxDraw()
    w.set_points([QPoint(10,10), QPoint(10,710), QPoint(710, 710), QPoint(710,10)])





    w.show()
    app.exec()
