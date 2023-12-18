from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
import json
import os
import markdown
from moc.mainwindow import Ui_MainWindow
from services.logic import MainLogic
from store import app_dir
import pyperclip

class MainWindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.logic = MainLogic()

        config_path = os.path.join(app_dir, 'resources\\config.json')
        try:
            json_file = open(config_path, 'r')
            configs = json.load(json_file)
            self.logic.setConfig(configs)
            for value in configs:
                self.LIST_THEME.addItem(value["prompt"])
        except:
            pass
        
        self.LIST_THEME.itemClicked.connect(self.onListThemeClicked)
        self.setWindowFlags(QtCore.Qt.WindowType.WindowStaysOnTopHint)

    def onEditApiKeyTextChanged(self, key):
        self.logic.setApiKey(key)

    def onListThemeClicked(self, item):
        row = self.LIST_THEME.currentRow()
        result = self.logic.run(row)
        pyperclip.copy(result)
        self.LIST_THEME.setCurrentRow(-1)
