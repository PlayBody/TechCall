from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
import json
import os
import markdown
from moc.mainwindow import Ui_MainWindow
from services.logic import MainLogic
from store import app_dir

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
                self.LIST_THEME.addItem(value["title"])
        except:
            pass
        
        keyfile = os.path.join(app_dir, 'resources\\apikey')
        try:
            json_file = open(keyfile, 'r')
            key = json_file.readline()
            self.logic.setApiKey(key)
        except:
            pass

        self.EDIT_API_KEY.textChanged.connect(self.onEditApiKeyTextChanged)
        self.LIST_THEME.itemDoubleClicked.connect(self.onListThemeDoubleClicked)

    def onEditApiKeyTextChanged(self, key):
        self.logic.setApiKey(key)

    def onListThemeDoubleClicked(self, item):
        row = self.LIST_THEME.currentRow()
        result = self.logic.run(row, self.EDIT_PROMPT.toPlainText())
        self.EDIT_ANSWER.setHtml(markdown.markdown(result))
