from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenu, QMenuBar


class EQMenuBar(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.file_menu: QMenu = self.addMenu("File")
        self.edit_menu: QMenu = self.addMenu("Edit")
        self.view_menu: QMenu = self.addMenu("View")

        self.edit_menu.setEnabled(False)  # For now

        self.open_file_action: QAction = QAction("&Open File", self)
        self.open_file_action.setShortcut("Ctrl+O")
        self.open_file_action.setStatusTip('Open a Wave file (.wav)')
        # self.open_file_action.triggered.connect(lambda: self.on_open())
        self.file_menu.addAction(self.open_file_action)

        self.save_file_action: QAction = QAction("&Save File", self)
        self.save_file_action.setShortcut("Ctrl+S")
        self.save_file_action.setStatusTip('Save as Wave File (.wav)')
        # self.save_file_action.triggered.connect(lambda: self.on_save())
        self.file_menu.addAction(self.save_file_action)

        self.exit_app_action: QAction = QAction("&Exit", self)
        self.exit_app_action.setShortcut('Alt+F4')
        self.exit_app_action.setStatusTip('Exit the Application')
        # self.exit_app_action.triggered.connect(lambda: self.on_exit())
        self.file_menu.addAction(self.exit_app_action)

        self.copy_content_action: QAction = QAction("&Copy", self)
        self.copy_content_action.setShortcut("Ctrl+C")
        self.copy_content_action.setStatusTip('Copy content to clipboard')
        # self.copy_content_action.triggered.connect(lambda: None)
        self.edit_menu.addAction(self.copy_content_action)

        self.paste_content_action: QAction = QAction("&Paste", self)
        self.paste_content_action.setShortcut("Ctrl+V")
        self.paste_content_action.setStatusTip('Paste content from clipboard')
        # self.paste_content_action.triggered.connect(lambda: None)
        self.edit_menu.addAction(self.paste_content_action)

        self.change_view_to_time_action: QAction = QAction("&Time domain", self)
        self.change_view_to_time_action.setStatusTip('Show Time Domain Representation')
        # self.change_view_to_time_action.triggered.connect(lambda: self.update_plot('time'))
        self.view_menu.addAction(self.change_view_to_time_action)

        self.change_view_to_freq_action: QAction = QAction("&Frequency domain", self)
        self.change_view_to_freq_action.setStatusTip('Show Frequency Domain Representation')
        # self.change_view_to_freq_action.triggered.connect(lambda: self.update_plot('frequency'))
        self.view_menu.addAction(self.change_view_to_freq_action)

        self.change_view_to_freqdb_action: QAction = QAction("&Frequency domain (dBFS)", self)
        self.change_view_to_freqdb_action.setStatusTip('Show Frequency Domain Representation (dBFS)')
        # self.change_view_to_freqdb_action.triggered.connect(lambda: self.update_plot('frequency-db'))
        self.view_menu.addAction(self.change_view_to_freqdb_action)
