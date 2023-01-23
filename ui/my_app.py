import sys
import os

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader


class MyApp:
    UI_FILE_NAME = "my_app.ui"


    def __init__(self):
        self._app = QApplication(sys.argv)
        self._ui = self._load_ui()

        self._ui.show()
        sys.exit(self._app.exec())


    def _load_ui(self):
        if hasattr(sys, '_MEIPASS'):
            ui_file_path = os.path.join(sys._MEIPASS, self.UI_FILE_NAME)
        else:
            current_file_dir = os.path.dirname(__file__)
            ui_file_path = os.path.join(current_file_dir, self.UI_FILE_NAME)

        ui_file = QFile(ui_file_path)

        if not ui_file.open(QIODevice.ReadOnly):
            raise FileNotFoundError(f"Cannot open {ui_file_path}: {ui_file.errorString()}")
            sys.exit(-1)

        loader = QUiLoader()
        ui = loader.load(ui_file)
        ui_file.close()

        return ui