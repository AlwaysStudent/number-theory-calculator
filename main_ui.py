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
        self.layoutWidget = QWidget(self.ExtendedEuclidean)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 891, 201))
        self.gridLayout_5 = QGridLayout(self.layoutWidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.ExtendedEuclideanAEditer = QLineEdit(self.layoutWidget)
        self.ExtendedEuclideanAEditer.setObjectName(u"ExtendedEuclideanAEditer")

        self.gridLayout_2.addWidget(self.ExtendedEuclideanAEditer, 0, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.ExtendedEuclideanBEditer = QLineEdit(self.layoutWidget)
        self.ExtendedEuclideanBEditer.setObjectName(u"ExtendedEuclideanBEditer")

        self.gridLayout_2.addWidget(self.ExtendedEuclideanBEditer, 1, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.ExtendedEuclideanMinAEditer = QLineEdit(self.layoutWidget)
        self.ExtendedEuclideanMinAEditer.setObjectName(u"ExtendedEuclideanMinAEditer")

        self.gridLayout.addWidget(self.ExtendedEuclideanMinAEditer, 0, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.ExtendedEuclideanMaxAEditer = QLineEdit(self.layoutWidget)
        self.ExtendedEuclideanMaxAEditer.setObjectName(u"ExtendedEuclideanMaxAEditer")

        self.gridLayout.addWidget(self.ExtendedEuclideanMaxAEditer, 0, 3, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.ExtendedEuclideanMinBEditer = QLineEdit(self.layoutWidget)
        self.ExtendedEuclideanMinBEditer.setObjectName(u"ExtendedEuclideanMinBEditer")

        self.gridLayout.addWidget(self.ExtendedEuclideanMinBEditer, 1, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.ExtendedEuclideanMaxBEditer = QLineEdit(self.layoutWidget)
        self.ExtendedEuclideanMaxBEditer.setObjectName(u"ExtendedEuclideanMaxBEditer")

        self.gridLayout.addWidget(self.ExtendedEuclideanMaxBEditer, 1, 3, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.ExtendedEuclideanCalculateButton = QPushButton(self.layoutWidget)
        self.ExtendedEuclideanCalculateButton.setObjectName(u"ExtendedEuclideanCalculateButton")

        self.gridLayout_4.addWidget(self.ExtendedEuclideanCalculateButton, 2, 0, 1, 1)

        self.ExtendedEuclideanRandomButton = QCheckBox(self.layoutWidget)
        self.ExtendedEuclideanRandomButton.setObjectName(u"ExtendedEuclideanRandomButton")

        self.gridLayout_4.addWidget(self.ExtendedEuclideanRandomButton, 0, 0, 1, 1)

        self.ExtendedEuclidean_1_Button = QCheckBox(self.layoutWidget)
        self.ExtendedEuclidean_1_Button.setObjectName(u"ExtendedEuclidean_1_Button")

        self.gridLayout_4.addWidget(self.ExtendedEuclidean_1_Button, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 1, 1, 1)

        self.CongruenceModEquation.addTab(self.ExtendedEuclidean, "")
        self.PowerMod = QWidget()
        self.PowerMod.setObjectName(u"PowerMod")
        self.layoutWidget1 = QWidget(self.PowerMod)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 10, 891, 191))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.PowerModA = QLineEdit(self.layoutWidget1)
        self.PowerModA.setObjectName(u"PowerModA")

        self.horizontalLayout.addWidget(self.PowerModA)

        self.label_8 = QLabel(self.layoutWidget1)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.PowerModB = QLineEdit(self.layoutWidget1)
        self.PowerModB.setObjectName(u"PowerModB")

        self.horizontalLayout.addWidget(self.PowerModB)

        self.label_9 = QLabel(self.layoutWidget1)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)

        self.PowerModP = QLineEdit(self.layoutWidget1)
        self.PowerModP.setObjectName(u"PowerModP")

        self.horizontalLayout.addWidget(self.PowerModP)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.PowerModRandomButton = QPushButton(self.layoutWidget1)
        self.PowerModRandomButton.setObjectName(u"PowerModRandomButton")

        self.verticalLayout.addWidget(self.PowerModRandomButton)

        self.PowerModCalculateButton = QPushButton(self.layoutWidget1)
        self.PowerModCalculateButton.setObjectName(u"PowerModCalculateButton")

        self.verticalLayout.addWidget(self.PowerModCalculateButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.CongruenceModEquation.addTab(self.PowerMod, "")
        self.Jacobi = QWidget()
        self.Jacobi.setObjectName(u"Jacobi")
        self.widget = QWidget(self.Jacobi)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(2, 2, 891, 201))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_3.addWidget(self.label_13)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_2.addWidget(self.label_11)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_2.addWidget(self.label_10)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_3.addWidget(self.label_12)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.JacobiEditorA = QLineEdit(self.widget)
        self.JacobiEditorA.setObjectName(u"JacobiEditorA")

        self.verticalLayout_3.addWidget(self.JacobiEditorA)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.JacobiEditorM = QLineEdit(self.widget)
        self.JacobiEditorM.setObjectName(u"JacobiEditorM")

        self.verticalLayout_3.addWidget(self.JacobiEditorM)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_3.addWidget(self.label_15)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_6.addWidget(self.label_17, 0, 0, 1, 1)

        self.JacobiEditorMinA = QLineEdit(self.widget)
        self.JacobiEditorMinA.setObjectName(u"JacobiEditorMinA")

        self.gridLayout_6.addWidget(self.JacobiEditorMinA, 0, 1, 1, 1)

        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 0, 2, 1, 1)

        self.JacobiEditorMaxA = QLineEdit(self.widget)
        self.JacobiEditorMaxA.setObjectName(u"JacobiEditorMaxA")

        self.gridLayout_6.addWidget(self.JacobiEditorMaxA, 0, 3, 1, 1)

        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_6.addWidget(self.label_18, 1, 0, 1, 1)

        self.JacobiEditorMinM = QLineEdit(self.widget)
        self.JacobiEditorMinM.setObjectName(u"JacobiEditorMinM")

        self.gridLayout_6.addWidget(self.JacobiEditorMinM, 1, 1, 1, 1)

        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_6.addWidget(self.label_16, 1, 2, 1, 1)

        self.JacobiEditorMaxM = QLineEdit(self.widget)
        self.JacobiEditorMaxM.setObjectName(u"JacobiEditorMaxM")

        self.gridLayout_6.addWidget(self.JacobiEditorMaxM, 1, 3, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_6)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.JacobiLegendreCheckBox = QCheckBox(self.widget)
        self.JacobiLegendreCheckBox.setObjectName(u"JacobiLegendreCheckBox")

        self.verticalLayout_4.addWidget(self.JacobiLegendreCheckBox)

        self.JacobiRandomPushButton = QPushButton(self.widget)
        self.JacobiRandomPushButton.setObjectName(u"JacobiRandomPushButton")

        self.verticalLayout_4.addWidget(self.JacobiRandomPushButton)

        self.JacobiCalculatePushButton = QPushButton(self.widget)
        self.JacobiCalculatePushButton.setObjectName(u"JacobiCalculatePushButton")

        self.verticalLayout_4.addWidget(self.JacobiCalculatePushButton)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.CongruenceModEquation.addTab(self.Jacobi, "")
        self.CRT = QWidget()
        self.CRT.setObjectName(u"CRT")
        self.label_29 = QLabel(self.CRT)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(471, 23, 93, 16))
        self.widget1 = QWidget(self.CRT)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 0, 891, 201))
        self.horizontalLayout_6 = QHBoxLayout(self.widget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_19 = QLabel(self.widget1)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_9.addWidget(self.label_19)

        self.label_21 = QLabel(self.widget1)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_9.addWidget(self.label_21)

        self.label_23 = QLabel(self.widget1)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_9.addWidget(self.label_23)

        self.label_25 = QLabel(self.widget1)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_9.addWidget(self.label_25)

        self.label_27 = QLabel(self.widget1)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_9.addWidget(self.label_27)


        self.horizontalLayout_5.addLayout(self.verticalLayout_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.CRTRemainder1 = QLineEdit(self.widget1)
        self.CRTRemainder1.setObjectName(u"CRTRemainder1")

        self.verticalLayout_8.addWidget(self.CRTRemainder1)

        self.CRTRemainder2 = QLineEdit(self.widget1)
        self.CRTRemainder2.setObjectName(u"CRTRemainder2")

        self.verticalLayout_8.addWidget(self.CRTRemainder2)

        self.CRTRemainder3 = QLineEdit(self.widget1)
        self.CRTRemainder3.setObjectName(u"CRTRemainder3")

        self.verticalLayout_8.addWidget(self.CRTRemainder3)

        self.CRTRemainder4 = QLineEdit(self.widget1)
        self.CRTRemainder4.setObjectName(u"CRTRemainder4")

        self.verticalLayout_8.addWidget(self.CRTRemainder4)

        self.CRTRemainder5 = QLineEdit(self.widget1)
        self.CRTRemainder5.setObjectName(u"CRTRemainder5")

        self.verticalLayout_8.addWidget(self.CRTRemainder5)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_20 = QLabel(self.widget1)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_7.addWidget(self.label_20)

        self.label_22 = QLabel(self.widget1)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_7.addWidget(self.label_22)

        self.label_24 = QLabel(self.widget1)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_7.addWidget(self.label_24)

        self.label_26 = QLabel(self.widget1)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_7.addWidget(self.label_26)

        self.label_28 = QLabel(self.widget1)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_7.addWidget(self.label_28)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.CRTMod1 = QLineEdit(self.widget1)
        self.CRTMod1.setObjectName(u"CRTMod1")

        self.verticalLayout_6.addWidget(self.CRTMod1)

        self.CRTMod2 = QLineEdit(self.widget1)
        self.CRTMod2.setObjectName(u"CRTMod2")

        self.verticalLayout_6.addWidget(self.CRTMod2)

        self.CRTMod3 = QLineEdit(self.widget1)
        self.CRTMod3.setObjectName(u"CRTMod3")

        self.verticalLayout_6.addWidget(self.CRTMod3)

        self.CRTMod4 = QLineEdit(self.widget1)
        self.CRTMod4.setObjectName(u"CRTMod4")

        self.verticalLayout_6.addWidget(self.CRTMod4)

        self.CRTMod5 = QLineEdit(self.widget1)
        self.CRTMod5.setObjectName(u"CRTMod5")

        self.verticalLayout_6.addWidget(self.CRTMod5)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_30 = QLabel(self.widget1)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_10.addWidget(self.label_30)

        self.label_31 = QLabel(self.widget1)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_10.addWidget(self.label_31)

        self.CRTCalculateButton = QPushButton(self.widget1)
        self.CRTCalculateButton.setObjectName(u"CRTCalculateButton")

        self.verticalLayout_10.addWidget(self.CRTCalculateButton)


        self.horizontalLayout_6.addLayout(self.verticalLayout_10)

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

        self.CongruenceModEquation.setCurrentIndex(3)


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
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u")^(", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u") mod ", None))
        self.PowerModRandomButton.setText(QCoreApplication.translate("MainWindow", u"\u968f\u673a", None))
        self.PowerModCalculateButton.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
        self.CongruenceModEquation.setTabText(self.CongruenceModEquation.indexOf(self.PowerMod), QCoreApplication.translate("MainWindow", u"\u6a21\u5927\u6570\u5e42\u4e58", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u")=(", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u503c\uff08a\uff09", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u503c\uff08a\uff09", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u503c\uff08b\uff09", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u503c\uff08b\uff09", None))
        self.JacobiLegendreCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u8981\u6c42\u4e3aLegendre\u7b26\u53f7", None))
        self.JacobiRandomPushButton.setText(QCoreApplication.translate("MainWindow", u"\u968f\u673a", None))
        self.JacobiCalculatePushButton.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
        self.CongruenceModEquation.setTabText(self.CongruenceModEquation.indexOf(self.Jacobi), QCoreApplication.translate("MainWindow", u"Jacobi\u7b26\u53f7", None))
        self.label_29.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"= mod", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"= mod", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"= mod", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"= mod", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"= mod", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u5982\u679c\u8be5\u884c\u4e0d\u9700\u8981", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u5728\u524d\u540e\u90fd\u8f93\u5165-1", None))
        self.CRTCalculateButton.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
        self.CongruenceModEquation.setTabText(self.CongruenceModEquation.indexOf(self.CRT), QCoreApplication.translate("MainWindow", u"\u5b59\u5b50\u5b9a\u7406", None))
        self.CongruenceModEquation.setTabText(self.CongruenceModEquation.indexOf(self.EulerTheorem), QCoreApplication.translate("MainWindow", u"\u6b27\u62c9\u5b9a\u7406", None))
        self.CongruenceModEquation.setTabText(self.CongruenceModEquation.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u7ebf\u6027\u540c\u4f59\u65b9\u7a0b", None))
    # retranslateUi

