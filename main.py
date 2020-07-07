"""
Author: AlwaysStudent
PythonVersion: 3.7
"""
from main_ui import *
import sys
import random
from pkg import ExtendedEuclidean


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
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
            message_box = QMessageBox()
            message_box.setWindowTitle("错误")
            message_box.setText("[错误] 所需的文本框未填写或包含非数字")
            message_box.exec_()
        self.ExtendedEuclideanDisplay(e)

    def ExtendedEuclideanDisplay(self, e):
        with open("ExtendedEuclidean.html", "w") as f1:
            with open("index.html", "r") as f2:
                index_text = f2.read()
                index_text = index_text.format(e.process())
                f1.write(index_text)
        self.ui.WebView.load(QUrl("file:///ExtendedEuclidean.html"))



def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

