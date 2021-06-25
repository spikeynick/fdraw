# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'box.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from image_w import ImageW


class Ui_boxDraw(object):
    def setupUi(self, boxDraw):
        if not boxDraw.objectName():
            boxDraw.setObjectName(u"boxDraw")
        boxDraw.resize(1151, 990)
        self.verticalLayout_2 = QVBoxLayout(boxDraw)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.canvas = ImageW(boxDraw)
        self.canvas.setObjectName(u"canvas")

        self.verticalLayout_2.addWidget(self.canvas)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(boxDraw)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.rotateBox = QDoubleSpinBox(boxDraw)
        self.rotateBox.setObjectName(u"rotateBox")
        self.rotateBox.setDecimals(3)
        self.rotateBox.setMinimum(0.001000000000000)
        self.rotateBox.setMaximum(1.000000000000000)
        self.rotateBox.setSingleStep(0.001000000000000)
        self.rotateBox.setValue(0.100000000000000)

        self.horizontalLayout.addWidget(self.rotateBox)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(boxDraw)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.stopBox = QSpinBox(boxDraw)
        self.stopBox.setObjectName(u"stopBox")
        self.stopBox.setMinimum(1)
        self.stopBox.setMaximum(99999)
        self.stopBox.setValue(5)

        self.horizontalLayout_2.addWidget(self.stopBox)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(boxDraw)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.speedBox = QSpinBox(boxDraw)
        self.speedBox.setObjectName(u"speedBox")
        self.speedBox.setMinimum(-99)

        self.horizontalLayout_3.addWidget(self.speedBox)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.goBtn = QPushButton(boxDraw)
        self.goBtn.setObjectName(u"goBtn")

        self.horizontalLayout_4.addWidget(self.goBtn)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.clearBtn = QPushButton(boxDraw)
        self.clearBtn.setObjectName(u"clearBtn")

        self.horizontalLayout_4.addWidget(self.clearBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(boxDraw)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.colorBox = QSpinBox(boxDraw)
        self.colorBox.setObjectName(u"colorBox")
        self.colorBox.setMaximum(359)

        self.horizontalLayout_5.addWidget(self.colorBox)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.globalCheck = QCheckBox(boxDraw)
        self.globalCheck.setObjectName(u"globalCheck")

        self.horizontalLayout_7.addWidget(self.globalCheck)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(boxDraw)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.penWidthBox = QSpinBox(boxDraw)
        self.penWidthBox.setObjectName(u"penWidthBox")
        self.penWidthBox.setMinimum(1)

        self.horizontalLayout_6.addWidget(self.penWidthBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2.setStretch(0, 1)

        self.retranslateUi(boxDraw)

        QMetaObject.connectSlotsByName(boxDraw)
    # setupUi

    def retranslateUi(self, boxDraw):
        boxDraw.setWindowTitle(QCoreApplication.translate("boxDraw", u"Form", None))
        self.label.setText(QCoreApplication.translate("boxDraw", u"Rotate:", None))
        self.label_2.setText(QCoreApplication.translate("boxDraw", u"Stop Size", None))
        self.label_3.setText(QCoreApplication.translate("boxDraw", u"Speed", None))
        self.goBtn.setText(QCoreApplication.translate("boxDraw", u"Start", None))
        self.clearBtn.setText(QCoreApplication.translate("boxDraw", u"Clear", None))
        self.label_4.setText(QCoreApplication.translate("boxDraw", u"Color Shift:", None))
        self.globalCheck.setText(QCoreApplication.translate("boxDraw", u"Global Shift", None))
        self.label_5.setText(QCoreApplication.translate("boxDraw", u"Line Thickness", None))
    # retranslateUi

