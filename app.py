import sys, os
from PyQt6 import QtGui, QtWidgets
from widgets.MainWindow import MainWindow
from store import app_dir

try:
    from ctypes import windll  # Only exists on Windows.
    myappid = 'psg.myapp.openai.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.join(app_dir, 'resources/logo.ico')))
    window = MainWindow()
    window.show()
    app.exec()