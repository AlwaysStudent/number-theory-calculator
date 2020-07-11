"""
Author: AlwaysStudent
PythonVersion: 3.7
"""
from main_ui import *
from PySide2 import QtWebEngineWidgets
import sys
import random
from pkg import ExtendedEuclidean
from pkg import PowerMod
from pkg import Jacobi
from pkg import CRT
from pkg import EulerTheorem
from pkg import CongruenceModEquation
from pkg import RSA


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.WebView.page().settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.ShowScrollBars, True)
        self.RSAInit()
        self.CongruenceModEquationInit()
        self.EulerTheoremInit()
        self.CRTInit()
        self.JacobiInit()
        self.PowerModInit()
        self.ExtendedEuclideanInit()
        self.RSAObject = None

    def RSAInit(self):
        self.ui.RSABitLenEditor.setText("200")
        self.ui.RSAMethedComboBox.setCurrentIndex(0)
        self.ui.RSAPlaintextEdit.setText("abcdefghijklmnopqrstuvwxyz")
        self.ui.RSAGenerateButton.clicked.connect(self.RSAGenerateKey)
        self.ui.RSACryptoButton.clicked.connect(self.RSACryptoText)

    def RSAGenerateKey(self):
        if self.ui.RSABitLenEditor.text().isdigit():
            bit_len = int(self.ui.RSABitLenEditor.text())
            mode = self.ui.RSAMethedComboBox.currentText()
            self.RSAObject = RSA.RSA(bit_len, mode)
            self.Display(self.RSAObject)
        else:
            ErrorMessageBox("位数缺失或为非数字")

    def RSACryptoText(self):
        plain_text = self.ui.RSAPlaintextEdit.toPlainText()
        crypto_text, result_text = self.RSAObject.encrypto(plain_text)
        _, temp_text = self.RSAObject.decrypto(crypto_text)
        result = result_text + temp_text
        self.ui.RSACryptotextEdit.setText(crypto_text)
        self.Display(result)


    def CongruenceModEquationInit(self):
        self.ui.CongruenceModEquationNumEditor.setText("1")
        self.CongruenceModEquationRandomHandle()
        self.ui.CongruenceModEquationRandomButton.clicked.connect(self.CongruenceModEquationRandomHandle)
        self.ui.CongruenceModEquationCalculateButton.clicked.connect(self.CongruenceModEquationCalculateHandle)

    def CongruenceModEquationRandomHandle(self):
        if self.ui.CongruenceModEquationNumEditor.text().isdigit():
            num = int(self.ui.CongruenceModEquationNumEditor.text())
            a = random.randint(50, 200)
            b = random.randint(50, 200)
            m = random.randint(50, 200)
            e = CongruenceModEquation.CongruenceModEquation(a, b, m, num)
            while not CongruenceModEquation.check(e):
                a = random.randint(50, 200)
                b = random.randint(50, 200)
                m = random.randint(50, 200)
                e = CongruenceModEquation.CongruenceModEquation(a, b, m, num)
            self.ui.CongruenceModEquationAEditor.setText(str(a))
            self.ui.CongruenceModEquationBEditor.setText(str(b))
            self.ui.CongruenceModEquationMEditor.setText(str(m))
        else:
            ErrorMessageBox("所需的文本框未填写或包含非数字")

    def CongruenceModEquationCalculateHandle(self):
        if self.ui.CongruenceModEquationAEditor.text().isdigit() and \
                self.ui.CongruenceModEquationBEditor.text().isdigit() and \
                self.ui.CongruenceModEquationMEditor.text().isdigit() and \
                self.ui.CongruenceModEquationNumEditor.text().isdigit():
            num = int(self.ui.CongruenceModEquationNumEditor.text())
            a = int(self.ui.CongruenceModEquationAEditor.text())
            b = int(self.ui.CongruenceModEquationBEditor.text())
            m = int(self.ui.CongruenceModEquationMEditor.text())
            e = CongruenceModEquation.CongruenceModEquation(a, b, m, num)
            self.Display(e)
        else:
            ErrorMessageBox("所需的文本框未填写或包含非数字")

    def EulerTheoremInit(self):
        self.EulerTheoremRandomHandle()
        self.ui.EulerTheoremRandomButton.clicked.connect(self.EulerTheoremRandomHandle)
        self.ui.EulerTheoremCalculateButton.clicked.connect(self.EulerTheoremCalculateHandle)

    def EulerTheoremRandomHandle(self):
        a = random.randint(3, 100)
        b = random.randint(500, 9999)
        p = random.randint(100, 500)
        e = EulerTheorem.EulerTheorem(a, b, p)
        while not EulerTheorem.check(e):
            a = random.randint(3, 100)
            b = random.randint(500, 9999)
            p = random.randint(100, 500)
            e = EulerTheorem.EulerTheorem(a, b, p)
        self.ui.EulerTheoremAEditor.setText(str(a))
        self.ui.EulerTheoremBEditor.setText(str(b))
        self.ui.EulerTheoremPEditor.setText(str(p))

    def EulerTheoremCalculateHandle(self):
        if self.ui.EulerTheoremAEditor.text().isdigit() and \
                self.ui.EulerTheoremBEditor.text().isdigit() and \
                self.ui.EulerTheoremPEditor.text().isdigit():
            a = int(self.ui.EulerTheoremAEditor.text())
            b = int(self.ui.EulerTheoremBEditor.text())
            p = int(self.ui.EulerTheoremPEditor.text())
            e = EulerTheorem.EulerTheorem(a, b, p)
            self.Display(e)
        else:
            ErrorMessageBox("所需的文本框未填写或包含非数字")

    def CRTInit(self):
        self.ui.CRTRemainder1.setText("-1")
        self.ui.CRTRemainder2.setText("-1")
        self.ui.CRTRemainder3.setText("-1")
        self.ui.CRTRemainder4.setText("-1")
        self.ui.CRTRemainder5.setText("-1")
        self.ui.CRTMod1.setText("-1")
        self.ui.CRTMod2.setText("-1")
        self.ui.CRTMod3.setText("-1")
        self.ui.CRTMod4.setText("-1")
        self.ui.CRTMod5.setText("-1")
        self.ui.CRTCalculateButton.clicked.connect(self.CRTCalculateHandle)

    def CRTCalculateHandle(self):
        remainder = []
        mod = []
        if self.ui.CRTRemainder1.text().isdigit() and self.ui.CRTMod1.text().isdigit():
            if self.ui.CRTRemainder1.text() != "-1" and self.ui.CRTMod1.text() != "-1":
                remainder.append(int(self.ui.CRTRemainder1.text()))
                mod.append(int(self.ui.CRTMod1.text()))
        if self.ui.CRTRemainder2.text().isdigit() and self.ui.CRTMod2.text().isdigit():
            if self.ui.CRTRemainder2.text() != "-1" and self.ui.CRTMod2.text() != "-1":
                remainder.append(int(self.ui.CRTRemainder2.text()))
                mod.append(int(self.ui.CRTMod2.text()))
        if self.ui.CRTRemainder3.text().isdigit() and self.ui.CRTMod3.text().isdigit():
            if self.ui.CRTRemainder3.text() != "-1" and self.ui.CRTMod3.text() != "-1":
                remainder.append(int(self.ui.CRTRemainder3.text()))
                mod.append(int(self.ui.CRTMod3.text()))
        if self.ui.CRTRemainder4.text().isdigit() and self.ui.CRTMod4.text().isdigit():
            if self.ui.CRTRemainder4.text() != "-1" and self.ui.CRTMod4.text() != "-1":
                remainder.append(int(self.ui.CRTRemainder4.text()))
                mod.append(int(self.ui.CRTMod4.text()))
        if self.ui.CRTRemainder5.text().isdigit() and self.ui.CRTMod5.text().isdigit():
            if self.ui.CRTRemainder5.text() != "-1" and self.ui.CRTMod5.text() != "-1":
                remainder.append(int(self.ui.CRTRemainder5.text()))
                mod.append(int(self.ui.CRTMod5.text()))
        if CRT.judge_mod(mod):
            e = CRT.CRT(remainder, mod)
            self.Display(e)
        else:
            ErrorText = "模数不互素"
            ErrorMessageBox(ErrorText)

    def JacobiInit(self):
        self.ui.JacobiEditorMinA.setText("200")
        self.ui.JacobiEditorMinM.setText("199")
        self.ui.JacobiEditorMaxA.setText("1000")
        self.ui.JacobiEditorMaxM.setText("1001")
        self.ui.JacobiLegendreCheckBox.setChecked(True)
        self.JacobiRandomHandle()
        self.ui.JacobiRandomPushButton.clicked.connect(self.JacobiRandomHandle)
        self.ui.JacobiCalculatePushButton.clicked.connect(self.JacobiCalculateHandle)

    def JacobiRandomHandle(self):
        if self.ui.JacobiEditorMaxA.text().isdigit() and \
                self.ui.JacobiEditorMaxM.text().isdigit() and \
                self.ui.JacobiEditorMinA.text().isdigit() and \
                self.ui.JacobiEditorMinM.text().isdigit():
            MaxA = int(self.ui.JacobiEditorMaxA.text())
            MinA = int(self.ui.JacobiEditorMinA.text())
            MaxM = int(self.ui.JacobiEditorMaxM.text())
            MinM = int(self.ui.JacobiEditorMinM.text())
            A = random.randrange(MinA, MaxA)
            M = random.randrange(MinM, MaxM)
            if self.ui.JacobiLegendreCheckBox.isChecked():
                e = Jacobi.Jacobi(A, M)
                while not Jacobi.is_Legendre(e):
                    A = random.randrange(MinA, MaxA)
                    M = random.randrange(MinM, MaxM, 2)
                    e = Jacobi.Jacobi(A, M)
            self.ui.JacobiEditorA.setText(str(A))
            self.ui.JacobiEditorM.setText(str(M))
        else:
            ErrorText = "所需的文本框未填写或包含非数字"
            ErrorMessageBox(ErrorText)

    def JacobiCalculateHandle(self):
        if self.ui.JacobiEditorA.text().isdigit() and self.ui.JacobiEditorM.text().isdigit():
            a = int(self.ui.JacobiEditorA.text())
            m = int(self.ui.JacobiEditorM.text())
            e = Jacobi.Jacobi(a, m)
            if Jacobi.is_Legendre(e):
                self.ui.JacobiLegendreCheckBox.setChecked(True)
            else:
                self.ui.JacobiLegendreCheckBox.setChecked(False)
            self.Display(e)

    def PowerModInit(self):
        self.PowerModRandomHandle()
        self.ui.PowerModRandomButton.clicked.connect(self.PowerModRandomHandle)
        self.ui.PowerModCalculateButton.clicked.connect(self.PowerModCalculateHandle)

    def PowerModRandomHandle(self):
        self.ui.PowerModA.setText(str(random.randint(20, 100)))
        self.ui.PowerModB.setText(str(random.randint(50, 100)))
        self.ui.PowerModP.setText(str(random.randint(50, 100)))

    def PowerModCalculateHandle(self):
        if self.ui.PowerModA.text().isdigit() and \
                self.ui.PowerModB.text().isdigit() and \
                self.ui.PowerModP.text().isdigit():
            a = int(self.ui.PowerModA.text())
            b = int(self.ui.PowerModB.text())
            p = int(self.ui.PowerModP.text())
            e = PowerMod.PowerMod(a, b, p)
            self.Display(e)
        else:
            ErrorText = "所需的文本框未填写或包含非数字"
            ErrorMessageBox(ErrorText)


    def ExtendedEuclideanInit(self):
        self.ui.ExtendedEuclideanMaxAEditer.setText("200")
        self.ui.ExtendedEuclideanMaxBEditer.setText("200")
        self.ui.ExtendedEuclideanMinAEditer.setText("50")
        self.ui.ExtendedEuclideanMinBEditer.setText("50")
        self.ui.ExtendedEuclidean_1_Button.click()
        self.ui.ExtendedEuclideanRandomButton.click()
        self.ui.ExtendedEuclideanCalculateButton.clicked.connect(self.ExtendedEuclideanHandle)

    def ExtendedEuclideanHandle(self):
        e = None
        if self.ui.ExtendedEuclideanRandomButton.isChecked() and \
                self.ui.ExtendedEuclideanMinAEditer.text().isdigit() and \
                self.ui.ExtendedEuclideanMinBEditer.text().isdigit() and \
                self.ui.ExtendedEuclideanMaxAEditer.text().isdigit() and \
                self.ui.ExtendedEuclideanMaxBEditer.text().isdigit():
            max_a = int(self.ui.ExtendedEuclideanMaxAEditer.text())
            min_a = int(self.ui.ExtendedEuclideanMinAEditer.text())
            max_b = int(self.ui.ExtendedEuclideanMaxBEditer.text())
            min_b = int(self.ui.ExtendedEuclideanMinBEditer.text())
            a = random.randint(min_a, max_a)
            b = random.randint(min_b, max_b)
            if self.ui.ExtendedEuclidean_1_Button.isChecked():
                while True:
                    a = random.randint(min_a, max_a)
                    b = random.randint(min_b, max_b)
                    if a == b:
                        continue
                    e = ExtendedEuclidean.ExtendedEuclidean(a, b)
                    if e.value()[0] == 1:
                        break
            else:
                e = ExtendedEuclidean.ExtendedEuclidean(a, b)
            self.ui.ExtendedEuclideanAEditer.setText(str(a))
            self.ui.ExtendedEuclideanBEditer.setText(str(b))
        elif not self.ui.ExtendedEuclideanRandomButton.isChecked() and \
                self.ui.ExtendedEuclideanAEditer.text().isdigit() and \
                self.ui.ExtendedEuclideanBEditer.text().isdigit():
            a = int(self.ui.ExtendedEuclideanAEditer.text())
            b = int(self.ui.ExtendedEuclideanBEditer.text())
            e = ExtendedEuclidean.ExtendedEuclidean(a, b)
        else:
            ErrorText = "所需的文本框未填写或包含非数字"
            ErrorMessageBox(ErrorText)
        self.Display(e)

    def Display(self, e):
        if not e:
            return
        with open("temporary.html", "w") as f1:
            with open("index.html", "r") as f2:
                index_text = f2.read()
                if type(e) == type(""):
                    index_text = index_text.format(e)
                else:
                    index_text = index_text.format(e.process())
                f1.write(index_text)
        self.ui.WebView.load(QUrl("file:///temporary.html"))


def ErrorMessageBox(title):
    message_box = QMessageBox()
    message_box.setWindowTitle("Error")
    message_box.setText("[错误] %s" % title)
    message_box.exec_()


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

