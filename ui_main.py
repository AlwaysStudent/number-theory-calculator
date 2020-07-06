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
        MainWindow.resize(800, 600)
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.WebView = QWebEngineView(self.centralwidget)
        self.WebView.setObjectName(u"WebView")
        self.WebView.setGeometry(QRect(330, 0, 471, 571))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 26))
        self.ExtendedEuclideanMenu = QMenu(self.menuBar)
        self.ExtendedEuclideanMenu.setObjectName(u"ExtendedEuclideanMenu")
        self.PowerModMenu = QMenu(self.menuBar)
        self.PowerModMenu.setObjectName(u"PowerModMenu")
        self.JacobiMenu = QMenu(self.menuBar)
        self.JacobiMenu.setObjectName(u"JacobiMenu")
        self.CRTMenu = QMenu(self.menuBar)
        self.CRTMenu.setObjectName(u"CRTMenu")
        self.CongruenceModMenu = QMenu(self.menuBar)
        self.CongruenceModMenu.setObjectName(u"CongruenceModMenu")
        self.EulerTheoremMenu = QMenu(self.menuBar)
        self.EulerTheoremMenu.setObjectName(u"EulerTheoremMenu")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.ExtendedEuclideanMenu.menuAction())
        self.menuBar.addAction(self.PowerModMenu.menuAction())
        self.menuBar.addAction(self.JacobiMenu.menuAction())
        self.menuBar.addAction(self.CRTMenu.menuAction())
        self.menuBar.addAction(self.CongruenceModMenu.menuAction())
        self.menuBar.addAction(self.EulerTheoremMenu.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6570\u8bba\u4e13\u7528\u8ba1\u7b97\u5e73\u53f0", None))
        self.ExtendedEuclideanMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u6269\u5c55\u6b27\u51e0\u91cc\u5f97\u7b97\u6cd5", None))
        self.PowerModMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u6a21\u5927\u6570\u5e42\u4e58", None))
        self.JacobiMenu.setTitle(QCoreApplication.translate("MainWindow", u"Jacobi\u7b26\u53f7", None))
        self.CRTMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u5b59\u5b50\u5b9a\u7406", None))
        self.CongruenceModMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u7ebf\u6027\u540c\u4f59\u65b9\u7a0b", None))
        self.EulerTheoremMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u6b27\u62c9\u5b9a\u7406", None))
    # retranslateUi

