import sys
import os

# IMPORT QT CORE
from qt_core import *

# IMPORT MAIN WINDOW
from gui.windows.main_window.ui_main_window import UI_MainWindow

# IMPORT DES
from DES1 import MyDES

from gui.pages.ui_pages import Ui_application_pages

# MAIN WINDOW
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Шифровальчик")

		# SETUP MAIN WINDOW
		self.ui = UI_MainWindow()
		self.ui.setup_ui(self)

		# Toggle button
		self.ui.toggle_button.clicked.connect(self.toggle_button)

		# Btn home
		self.ui.btn_1.clicked.connect(self.show_page_1)

		# Btn widgets
		self.ui.btn_2.clicked.connect(self.show_page_2)

		# Btn RSA
		self.ui.btn_3.clicked.connect(self.show_page_4)

		# Btn ELGAMAL
		self.ui.btn_4.clicked.connect(self.show_page_5)

		# Btn settings
		self.ui.settings_btn.clicked.connect(self.show_page_3)


		# EXBI A MOSSA APLICATION
		self.show()

	def reset_selection(self):
		for bin in self.ui.left_menu.findChildren(QPushButton):
			try:
				btn.set_active(False)
			except:
				pass


	def show_page_1(self):
		self.reset_selection()
		self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
		self.ui.btn_1.set_active(True)
# Здесь ваша реализация DES	
	def show_page_2(self):
		self.reset_selection()
		self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
		self.ui.btn_2.set_active(True)

	def show_page_3(self):
		self.reset_selection()
		self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
		self.ui.settings_btn.set_active(True)

# Здесь ваша реализация RSA
	def show_page_4(self):
		self.reset_selection()
		self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_4)
		self.ui.btn_3.set_active(True)

# Здесь ваша реализация ELGAMAL
	def show_page_5(self):
		self.reset_selection()
		self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_5)
		self.ui.btn_4.set_active(True)

	def toggle_button(self):
		# Get menu wigth
		menu_width = self.ui.left_menu.width()

		# Check with
		width = 50
		if menu_width == 50:
			width = 240

		# Start animation
		self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
		self.animation.setStartValue(menu_width)
		self.animation.setEndValue(width)
		self.animation.setDuration(500)
		self.animation.setEasingCurve(QEasingCurve.InOutCirc)
		self.animation.start()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	sys.exit(app.exec())