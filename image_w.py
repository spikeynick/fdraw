from PySide6.QtCore import QLine, QPoint, Qt, QTimer, Slot, Signal
from PySide6.QtWidgets import QApplication, QWidget, QFrame
from PySide6.QtGui import QPainter
from PySide6 import QtGui



class Line(QLine):
    def length(self):
        return (self.dx()**2 + self.dy()**2)**.5




class ImageW(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.points = []
        self.time_incr = 10
        self.step_incr = 1
        self.stop_size = 5
        self.rotate_val = .1
        self.refresh()
        self.drawing = False

    def set_points(self, points):
        self.points = points
        self.refresh()

    def refresh(self, ):

        self.draw_start = 0
        self.draw_end = 0
        self.segments = []
        self.sides = len(self.points)
        if not self.sides:
            return
        self.cleared = False
        p1 = self.points[0]
        for p2 in self.points[1:]:
            self.segments.append(Line(p1,p2))
            p1 = p2
        p2 = self.points[0]
        self.segments.append(Line(p1,p2))


        start = self.segments[0].p1()
        while self.segments[-1].length() > self.stop_size:

            print("Line: ", self.segments[-1].length())
            next_line = self.segments[-(self.sides-1)]
            x = next_line.dx()*self.rotate_val
            y = next_line.dy()*self.rotate_val
            p = next_line.p1()
            np = QPoint(p.x()+x, p.y()+y)
            ns = Line(start,np)
            start = np
            self.segments.append(ns)
            print("FINISHED %d Segments"%len(self.segments))


    @Slot()
    def incr_draw(self):
        if not self.drawing:
            return
        if self.draw_end < len(self.segments):
            self.draw_end+= self.step_incr
        elif self.draw_start < self.draw_end:
            self.draw_start += self.step_incr
        else:
            self.draw_start = 0
            self.draw_end = self.sides
        QTimer.singleShot(self.time_incr, self.incr_draw)
        #self.repaint(self.rect())
        self.update()

    def paintEvent(self, event):
#        print("PAINT EVENT")
        painter = QPainter(self)

        painter.setPen(Qt.black)

        if self.cleared:
            self.sides = len(self.points)
            for p in self.points:
                painter.drawEllipse(p,5,5)


        if not self.drawing:
            self.draw_start = 0
            self.draw_end = self.sides



        for line in self.segments[self.draw_start:self.draw_end]:
            painter.drawLine(line.x1(), line.y1(), line.x2(), line.y2())

        painter.end()


    @Slot(int)
    def update_stop(self, val):
        self.stop_size = val
        self.refresh()

    @Slot(int)
    def update_speed(self, val):
        if val > 0:
            self.time_incr = 10
            self.step_incr = val
        elif val < 0:
            self.step_incr = 1
            self.time_incr = -10 * val
        else:
            self.time_incr = 10
            self.step_incr = 1

    @Slot(float)
    def update_rotate(self, val):
        self.rotate_val = val
        self.refresh()


    @Slot()
    def go_toggle(self, ):
        if self.drawing:
            self.drawing = False
        else:
            self.refresh()
            self.drawing = True
            self.incr_draw()

    @Slot()
    def do_clear(self, ):
        self.drawing = False
        self.cleared = True
        self.points = []
        self.segments = []
        self.update()


    def mouseReleaseEvent(self, event):
        if self.cleared:
            self.points.append(QPoint(event.x(), event.y()))
            self.update()
