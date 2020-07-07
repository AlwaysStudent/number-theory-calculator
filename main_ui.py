# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from PySide2.QtWebEngineWidgets import QWebEngineView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 870)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.CongruenceModEquation = QTabWidget(self.centralwidget)
        self.CongruenceModEquation.setObjectName(u"CongruenceModEquation")
        self.CongruenceModEquation.setGeometry(QRect(0, 0, 901, 231))
        self.ExtendedEuclidean = QWidget()
        self.ExtendedEuclidean.setObjectName(u"ExtendedEuclidean")
        self.widget = QWidget(self.ExtendedEuclidean)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 0, 871, 191))
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.ExtendedEuclideanAEditer = QLineEdit(self.widget)
        self.ExtendedEuclideanAEditer.setObjectName(u"ExtendedEuclideanAEditer")

        self.gridLayout_2.addWidget(self.ExtendedEuclideanAEditer, 0, 1, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.ExtendedEuclideanBEditer = QLineEdit(self.widget)
        self.ExtendedEuclideanBEditer.setObjectName(u"ExtendedEuclideanBEditer")

        self.gridLayout_2.addWidget(self.ExtendedEuclideanBEditer, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.ExtendedEuclideanMinAEditer = QLineEdit(self.widget)
        self.ExtendedEuclideanMinAEditer.setObjectName(u"ExtendedEuclideanMinAEditer")

        self.gridLayout.addWidget(self.ExtendedEuclideanMinAEditer, 0, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.ExtendedEuclideanMaxAEditer = QLineEdit(self.widget)
        self.ExtendedEuclideanMaxAEditer.setObjectName(u"ExtendedEuclideanMaxAEditer")

        self.gridLayout.addWidget(self.ExtendedEuclideanMaxAEditer, 0, 3, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.ExtendedEuclideanMinBEditer = QLineEdit(self.widget)
        self.ExtendedEuclideanMinBEditer.setObjectName(u"ExtendedEuclideanMinBEditer")

        self.gridLayout.addWidget(self.ExtendedEuclideanMinBEditer, 1, 1, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.ExtendedEuclideanMaxBEditer = QLineEdit(self.widget)
        self.ExtendedEuclideanMaxBEditer.setObjectName(u"ExtendedEuclideanMaxBEditer")

        self.gridLayout.addWidget(self.ExtendedEuclideanMaxBEditer, 1, 3, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.ExtendedEuclideanCalculateButton = QPushButton(self.widget)
        self.ExtendedEuclideanCalculateButton.setObjectName(u"ExtendedEuclideanCalculateButton")

        self.gridLayout_4.addWidget(self.ExtendedEuclideanCalculateButton, 2, 0, 1, 1)

        self.ExtendedEuclideanRandomButton = QCheckBox(self.widget)
        self.ExtendedEuclideanRandomButton.setObjectName(u"ExtendedEuclideanRandomButton")

        self.gridLayout_4.addWidget(self.ExtendedEuclideanRandomButton, 0, 0, 1, 1)

        self.ExtendedEuclidean_1_Button = QCheckBox(self.widget)
        self.ExtendedEuclidean_1_Button.setObjectName(u"ExtendedEuclidean_1_Button")

        self.gridLayout_4.addWidget(self.ExtendedEuclidean_1_Button, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 1, 1, 1)

        self.CongruenceModEquation.addTab(self.ExtendedEuclidean, "")
        self.PowerMod = QWidget()
        self.PowerMod.setObjectName(u"PowerMod")
        self.CongruenceModEquation.addTab(self.PowerMod, "")
        self.Jacobi = QWidget()
        self.Jacobi.setObjectName(u"Jacobi")
        self.CongruenceModEquation.addTab(self.Jacobi, "")
        self.CRT = QWidget()
        self.CRT.setObjectName(u"CRT")
        self.CongruenceModEquation.addTab(self.CRT, "")
        self.EulerTheorem = QWidget()
        self.EulerTheorem.setObjectName(u"EulerTheorem")
        self.CongruenceModEquation.addTab(self.EulerTheorem, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.CongruenceModEquation.addTab(self.tab, "")
        self.WebView = QWebEngineView(self.centralwidget)
        self.WebView.setObjectName(u"WebView")
        self.WebView.setGeometry(QRect(-1, 229, 901, 641))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.CongruenceModEquation.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6570\u8bba\u4e13\u7528\u8ba1\u7b97\u5e73\u53f0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u503c\uff08a\uff09", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u503c\uff08a\uff09", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u503c\uff08b\uff09", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u503c\uff08b\uff09", None))
        self.ExtendedEuclideanCalculateButton.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
        self.ExtendedEuclideanRandomButton.setText(QCoreApplication.translate("MainWindow", u"\u968f\u673a", None))
        self.ExtendedEuclidean_1_Button.setText(QCoreApplication.translate("MainWindow", u"\u9006\u5143", None))
        self.CongruenceModEquation.setTabText(self.CongruenceModEquation.indexOf(self.ExtendedEuclidean), QCoreApplication.translate("MainWindow", u"\u6269\u5c55\u6b27\u51e0\u91cc\u5f97\u7b97\u6cd5", None))
        self.CongruenceModEquation.setTabText(self.CongruenceModEquation.indexOf(self.PowerMod), QCoreApplication.translate("MainWindow", u"\u6a21\u5927\u6570\u5e42\u4e58", None))
        self.CongruenceModEquation.setTabText(self.CongruenceModEquation.indexOf(self.Jacobi), QCoreApplication.translate("MainWindow", u"Jacobi\u7b26\u53f7", None))
        self.CongruenceModEquation.setTabText(self.CongruenceModEquation.indexOf(self.CRT), QCoreApplication.translate("MainWindow", u"\u5b59\u5b50\u5b9a\u7406", None))
        self.CongruenceModEquation.setTabText(self.CongruenceModEquation.indexOf(self.EulerTheorem), QCoreApplication.translate("MainWindow", u"\u6b27\u62c9\u5b9a\u7406", None))
        self.CongruenceModEquation.setTabText(self.CongruenceModEquation.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u7ebf\u6027\u540c\u4f59\u65b9\u7a0b", None))
    # retranslateUi

