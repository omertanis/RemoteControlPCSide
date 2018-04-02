import sys
import multiprocessing

from PySide import QtGui
from PySide import QtCore


def factorial():
        f = 4
        r = 1
        for i in reversed(range(1, f+1)):
            r *= i
        print 'factorial', r


class MainGui(QtGui.QWidget):
    def __init__(self):
        super(MainGui, self).__init__()

        self.initGui()

    def initGui(self):
        b = QtGui.QPushButton('click', self)
        b.move(30, 30)
        b.clicked.connect(self.onClick)
        self.resize(600, 400)
        self.show()

    def onClick(self):
        print 'button clicked'
        self.forkProcess()

    def forkProcess(self):
        p = multiprocessing.Process(target=factorial)
        p.daemon = True
        p.start()



if __name__ == "__main__":
    print 'ok'

    app = QtGui.QApplication(sys.argv)
    ex = MainGui()
    sys.exit(app.exec_())