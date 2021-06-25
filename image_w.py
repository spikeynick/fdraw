from PySide6.QtCore import QLine, QPoint, Qt, QTimer, Slot, Signal
from PySide6.QtWidgets import QApplication, QWidget, QFrame
from PySide6.QtGui import QPainter
from PySide6 import QtGui

import math

class Line(QLine):
    def length(self):
        return (self.dx()**2 + self.dy()**2)**.5




class ImageW(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.h = 0
        self.points = []
        self.time_incr = 10
        self.step_incr = 1
        self.stop_size = 5
        self.rotate_val = .1
        self.refresh()
        self.drawing = False
        self.color_step = 5
        self.global_color = False
        self.pen_width = 1
        self.pen_map = {}
        self.draw_start = 0
        self.draw_end = 0
        

    @Slot(int)
    def update_color(self, new_step):
        self.color_step = new_step
    @Slot(bool)
    def update_global_color(self, is_global):
        self.global_color = is_global

    @Slot(int)
    def update_pen_width(self, width):
        self.pen_width = width
        for p in self.pen_map.values():
            p.setWidth(width)


    def set_points(self, points):
        self.points = points
        self.refresh()

    def refresh(self, ):

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

            # attempt at shifting by a certain angle instead of going by percentage of line length
            # something's not quite right here though
            if False:
                line1 = self.segments[-self.sides]
                lineA = Line(line1.p1(),next_line.p2())
                a2 = lineA.dx()**2 + lineA.dy()**2
                b2 = line1.dx()**2 + line1.dy()**2
                b = b2**.5
                c2 = next_line.dx()**2 + next_line.dy()**2
                c = c2**.5

                cos_a = (b2+c2 - a2) / (2*b*c)
                print(cos_a)
                angle_a = math.degrees(math.acos(cos_a))

                new_angle = 45 * self.rotate_val

                angle_b = 180 - angle_a - new_angle

                print("POINTS: ", line1.p1(), line1.p2(), next_line.p1(), next_line.p2())
                print("Angles: ",new_angle, angle_a, angle_b)


                div_len = math.sin(math.radians(new_angle)) * b

                new_line_len = div_len / math.sin(math.radians(angle_b))
                ratio = new_line_len / c
                print("RATIO",ratio,new_line_len,c)

            else:
                ratio = self.rotate_val


            x = next_line.dx()*ratio
            y = next_line.dy()*ratio
            print("X %s, Y %s"%(x,y))

            p = next_line.p1()
            np = QPoint(p.x()+x, p.y()+y)
            ns = Line(start,np)
            print("NS",ns)
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



        if self.cleared:
            pen = painter.pen()
            pen.setWidth(self.pen_width)
            pen.setColor(Qt.black)
            self.sides = len(self.points)
            for p in self.points:
                painter.drawEllipse(p,5,5)

        if self.global_color:
            self.h += self.color_step
            self.h = self.h % 360
        else:
            self.h = 0
        if self.h not in self.pen_map:
            pen = painter.pen()
            color = QtGui.QColor.fromHsv(self.h,255/2,255/2)
            pen.setColor(color)
            pen.setWidth(self.pen_width)
        else:
            pen = self.pen_map[self.h]
        painter.setPen(pen)
        if not self.drawing:
            self.draw_start = 0
            self.draw_end = self.sides

        if not self.global_color:
                self.h += self.color_step * self.draw_start
                self.h = self.h % 360



        for line in self.segments[self.draw_start:self.draw_end]:
            if not self.global_color:
                self.h += self.color_step
                self.h = self.h % 360
                if self.h not in self.pen_map:
                    pen = painter.pen()
                    color = QtGui.QColor.fromHsv(self.h,255/2,255/2)
                    pen.setColor(color)
                    pen.setWidth(self.pen_width)
                else:
                    pen = self.pen_map[self.h]
                painter.setPen(pen)

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
