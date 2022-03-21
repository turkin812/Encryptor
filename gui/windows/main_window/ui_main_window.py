# IMPORT QT CORE
from qt_core import *

# IMPORT PAGES
from gui.pages.ui_pages import Ui_application_pages

# IMPORT CUSTOM WIDGETS
from gui.widgets.py_push_button import PyPushButton
#from os.path import basename, splitext
import pathlib

# IMPORT SHIFR.py
import sys
from DES1 import MyDES
from RSSA import MyRSA
from ELGAMAL import MyELGAMAL
import numpy as np
import random
from math import pow


class UI_MainWindow(QMainWindow, object):
	def setup_ui(self, parent):
		if not parent.objectName():
			parent.setObjectName("MainWindow")

		# SWT INITIAL PARAMETERS
		parent.resize(800, 500)
		parent.setMinimumSize(300, 200)

		# CREATE CENTRAL WIDGET
		self.central_frame = QFrame()
		self.central_frame.setStyleSheet("background-color: #282a36")

		# CREATE MAIN LAYOUT
		self.main_layout = QHBoxLayout(self.central_frame)
		self.main_layout.setContentsMargins(0, 0, 0, 0)
		self.main_layout.setSpacing(0)

		# LEFT MENU
		self.left_menu = QFrame()
		self.left_menu.setStyleSheet("background-color: #44475a")
		self.left_menu.setMaximumWidth(50)
		self.left_menu.setMinimumWidth(50)

		# LEFT MENU LAYOUT
		self.left_menu_layout = QVBoxLayout(self.left_menu)
		self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
		self.left_menu_layout.setSpacing(0)

		# TOP FRAME MENU
		self.left_menu_top_frame = QFrame()
		self.left_menu_top_frame.setMinimumHeight(40)
		self.left_menu_top_frame.setObjectName("left_menu_top_frame")

		# TOP FRAME LAYOUT
		self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
		self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
		self.left_menu_top_layout.setSpacing(0)

		# TOP BTNS
		self.toggle_button = PyPushButton(
			text = "MENU",
			icon_path = "icon_menu.svg",
			icon_color = "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 146, 0, 185));"
		)
		self.btn_1 = PyPushButton(
			text = "HOME",
			is_active = True,
			icon_path = "icon_home.svg"
		)
		self.btn_2 = PyPushButton(
			text = "DES",
			icon_path = "icons_des.svg"
		)
		self.btn_3 = PyPushButton(
			text = "RSA",
			icon_path = "icons_rsa.svg"
		)
		self.btn_4 = PyPushButton(
			text = "ELGAMAL",
			icon_path = "icons_elgamal.svg"
		)

		# ADD BTNS TO LAYOUT
		self.left_menu_top_layout.addWidget(self.toggle_button)
		self.left_menu_top_layout.addWidget(self.btn_1)
		self.left_menu_top_layout.addWidget(self.btn_2)
		self.left_menu_top_layout.addWidget(self.btn_3)
		self.left_menu_top_layout.addWidget(self.btn_4)

		# MENU SPACER
		self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

		# BOTTOM FRAME MENU
		self.left_menu_bottom_frame = QFrame()
		self.left_menu_bottom_frame.setMinimumHeight(40)
		self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")

		self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
		self.left_menu_bottom_layout.setContentsMargins(0, 0, 0, 0)
		self.left_menu_bottom_layout.setSpacing(0)

		# BOTTOM BTNS
		self.settings_btn = PyPushButton(
			text = "Settings",
			icon_path = "icons_settings.svg"
		)
		
		# ADD BTNS TO LAYOUT
		self.left_menu_bottom_layout.addWidget(self.settings_btn)

		# LABEL VERSION
		self.left_menu_label_version = QLabel("v1.0.0")
		self.left_menu_label_version.setAlignment(Qt.AlignCenter)
		self.left_menu_label_version.setMinimumHeight(30)
		self.left_menu_label_version.setMaximumHeight(30)
		self.left_menu_label_version.setStyleSheet("color: #c3ccdf")

		# ADD TO LAYOUT
		self.left_menu_layout.addWidget(self.left_menu_top_frame)
		self.left_menu_layout.addItem(self.left_menu_spacer)
		self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
		self.left_menu_layout.addWidget(self.left_menu_label_version)

		# CONTENT
		self.content = QFrame()
		self.content.setStyleSheet("background-color: #282a36")

		# Content Layout
		self.content_layout = QVBoxLayout(self.content)
		self.content_layout.setContentsMargins(0, 0, 0, 0)
		self.content_layout.setSpacing(0)

		# TOP BAR
		self.top_bar = QFrame()
		self.top_bar.setMinimumHeight(30)
		self.top_bar.setMaximumHeight(30)
		self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
		self.top_bar_layout = QHBoxLayout(self.top_bar)
		self.top_bar_layout.setContentsMargins(10, 0, 10, 0)

		# Left Label
		self.top_label_left = QLabel("")
		
		# Top spacer
		self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		# Right label
		self.top_label_right = QLabel("Implementation of encryption algorithms")
		self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

		# Add to layout
		self.top_bar_layout.addWidget(self.top_label_left)
		self.top_bar_layout.addItem(self.top_spacer)
		self.top_bar_layout.addWidget(self.top_label_right)

		# Application pages
		self.pages = QStackedWidget()
		self.pages.setStyleSheet("color: #f8f8f2")
		self.ui_pages = Ui_application_pages()
		self.ui_pages.setupUi(self.pages)
		self.pages.setCurrentWidget(self.ui_pages.page_1)

		# TOP BAR
		self.bottom_bar = QFrame()
		self.bottom_bar.setMinimumHeight(30)
		self.bottom_bar.setMaximumHeight(30)
		self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")

		self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
		self.bottom_bar_layout.setContentsMargins(10, 0, 10, 0)

		# Left Label
		self.bottom_label_left = QLabel("Author: Igor Turkin")
		
		# Top spacer
		self.bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

		# Right label
		self.bottom_label_right = QLabel("©2021")
		self.bottom_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")

		# Add to layout
		self.bottom_bar_layout.addWidget(self.bottom_label_left)
		self.bottom_bar_layout.addItem(self.bottom_spacer)
		self.bottom_bar_layout.addWidget(self.bottom_label_right)

		# Add to content Layout
		self.content_layout.addWidget(self.top_bar)
		self.content_layout.addWidget(self.pages)
		self.content_layout.addWidget(self.bottom_bar)

		# ADD WIDGETS TO APP
		self.main_layout.addWidget(self.left_menu)
		self.main_layout.addWidget(self.content)

		##########################################################

		# ЗАГРУЗКА ТЕКСТА ИЗ ФАЙЛА
		self.ui_pages.pushButton_4.clicked.connect(self.on_pushButton_download_4)
		self.ui_pages.pushButton_5.clicked.connect(self.on_pushButton_download_5)
		self.ui_pages.pushButton_6.clicked.connect(self.on_pushButton_download_6)

		# ВЫГРУЗКА ТЕКСТА В ФАЙЛ
		self.ui_pages.pushButton.clicked.connect(self.on_pushButton_unload)
		self.ui_pages.pushButton_7.clicked.connect(self.on_pushButton_unload_7)
		self.ui_pages.pushButton_8.clicked.connect(self.on_pushButton_unload_8)

		# ШИФРОВАНИЕ/ДЕШИФРОВАНИЕ
		self.ui_pages.pushButton_3.clicked.connect(self.shifrDES)
		self.ui_pages.pushButton_2.clicked.connect(self.deshifrDES)
		

		##########################################################

		# ЗАГРУЗКА ТЕКСТА ИЗ ФАЙЛА
		self.ui_pages.pushButton_9.clicked.connect(self.on_pushButton_download_9)
		self.ui_pages.pushButton_11.clicked.connect(self.on_pushButton_download_11)
		self.ui_pages.pushButton_19.clicked.connect(self.on_pushButton_download_19)
		self.ui_pages.pushButton_13.clicked.connect(self.on_pushButton_download_13)

		# ВЫГРУЗКА ТЕКСТА В ФАЙЛ
		self.ui_pages.pushButton_10.clicked.connect(self.on_pushButton_unload_10)
		self.ui_pages.pushButton_12.clicked.connect(self.on_pushButton_unload_12)
		self.ui_pages.pushButton_20.clicked.connect(self.on_pushButton_unload_20)
		self.ui_pages.pushButton_14.clicked.connect(self.on_pushButton_unload_14)


		# ШИФРОВАНИЕ/ДЕШИФРОВАНИЕ
		self.ui_pages.pushButton_16.clicked.connect(self.shifrRSA)
		self.ui_pages.pushButton_15.clicked.connect(self.deshifrRSA)
		

		##########################################################

		# ЗАГРУЗКА ТЕКСТА ИЗ ФАЙЛА
		self.ui_pages.pushButton_23.clicked.connect(self.on_pushButton_download_23)
		self.ui_pages.pushButton_25.clicked.connect(self.on_pushButton_download_25)
		self.ui_pages.pushButton_21.clicked.connect(self.on_pushButton_download_21)
		self.ui_pages.pushButton_17.clicked.connect(self.on_pushButton_download_17)

		# ВЫГРУЗКА ТЕКСТА В ФАЙЛ
		self.ui_pages.pushButton_24.clicked.connect(self.on_pushButton_unload_24)
		self.ui_pages.pushButton_26.clicked.connect(self.on_pushButton_unload_26)
		self.ui_pages.pushButton_22.clicked.connect(self.on_pushButton_unload_22)
		self.ui_pages.pushButton_18.clicked.connect(self.on_pushButton_unload_18)


		# ШИФРОВАНИЕ/ДЕШИФРОВАНИЕ
		self.ui_pages.pushButton_28.clicked.connect(self.shifrELGAMAL)
		self.ui_pages.pushButton_27.clicked.connect(self.deshifrELGAMAL)
		

		##########################################################

		self.ui_pages.pushButton_29.clicked.connect(self.KEYKEYKEY)

		# SET CENTRAL WIDGET
		parent.setCentralWidget(self.central_frame)

	

	def on_pushButton_download_4(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file', r'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not fname:
			return
		try:
			with open(fname[0], 'r') as f:
				data = f.read()
				self.ui_pages.plainTextEdit_2.setPlainText(data)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.fname = fname


	def on_pushButton_download_5(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file', r'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not fname:
			return
		try:
			with open(fname[0], 'r') as f:
				data = f.read()
				self.ui_pages.plainTextEdit_3.setPlainText(data)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.fname = fname

	def on_pushButton_download_6(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file', r'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not fname:
			return
		try:
			with open(fname[0], 'r') as f:
				data = f.read()
				self.ui_pages.plainTextEdit.setPlainText(data)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.fname = fname


	def on_pushButton_unload(self):
		path, filter = QFileDialog.getSaveFileName(self, 'Save file', 'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not path:
			return
		self._save_to_path(path)

	def _save_to_path(self, path):
		text = self.ui_pages.plainTextEdit_2.toPlainText()
		try:
			with open(path, 'w') as f:
				f.write(text)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.path = path

	def on_pushButton_unload_7(self):
		path, filter = QFileDialog.getSaveFileName(self, 'Save file', 'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not path:
			return
		self._save_to_path_7(path)

	def _save_to_path_7(self, path):
		text = self.ui_pages.plainTextEdit.toPlainText()
		try:
			with open(path, 'w') as f:
				f.write(text)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.path = path

	def on_pushButton_unload_8(self):
		path, filter = QFileDialog.getSaveFileName(self, 'Save file', 'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not path:
			return
		self._save_to_path_8(path)

	def _save_to_path_8(self, path):
		text = self.ui_pages.plainTextEdit_3.toPlainText()
		try:
			with open(path, 'w') as f:
				f.write(text)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.path = path
	def dialog_critical(self, s):
		dig = QMessageBox(self)
		dig.setText(s)
		dig.setIcon(QMessageBox.Critical)
		dig.show()

	#########################################################################################

	def shifrDES(self):                         # Шифрованный текст в файл
		key = self.ui_pages.plainTextEdit_3.toPlainText()      # Взятие ключа из поля
		md = MyDES()                      # Создание объекта класса
		text = self.ui_pages.plainTextEdit.toPlainText()  # Взятие текста из поля
		shifr = md.encode(text, key)  # Шифрованное сообщение
		self.ui_pages.plainTextEdit_2.setPlainText(shifr)
		self.ui_pages.plainTextEdit_3.setPlainText(key)

	def deshifrDES(self):                 # Вывод дешифрованного сообщения
		key = self.ui_pages.plainTextEdit_3.toPlainText()
		md = MyDES()
		text = self.ui_pages.plainTextEdit_2.toPlainText()
		noshifr1 = md.decode(text, key)
		noshifr = noshifr1.rstrip('\x00')
		self.ui_pages.plainTextEdit.setPlainText(noshifr)

	#########################################################################################

	def on_pushButton_download_9(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file', r'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not fname:
			return
		try:
			with open(fname[0], 'r') as f:
				data = f.read()
				self.ui_pages.plainTextEdit_5.setPlainText(data)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.fname = fname

	def on_pushButton_download_11(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file', r'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not fname:
			return
		try:
			with open(fname[0], 'r') as f:
				data = f.read()
				self.ui_pages.plainTextEdit_6.setPlainText(data)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.fname = fname

	def on_pushButton_download_19(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file', r'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not fname:
			return
		try:
			with open(fname[0], 'r') as f:
				data = f.read()
				self.ui_pages.plainTextEdit_8.setPlainText(data)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.fname = fname

	def on_pushButton_download_13(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file', r'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not fname:
			return
		try:
			with open(fname[0], 'r') as f:
				data = f.read()
				self.ui_pages.plainTextEdit_4.setPlainText(data)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.fname = fname


	def on_pushButton_unload_10(self):
		path, filter = QFileDialog.getSaveFileName(self, 'Save file', 'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not path:
			return
		self._save_to_path(path)

	def _save_to_path_10(self, path):
		text = self.ui_pages.plainTextEdit_5.toPlainText()
		try:
			with open(path, 'w') as f:
				f.write(text)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.path = path

	def on_pushButton_unload_12(self):
		path, filter = QFileDialog.getSaveFileName(self, 'Save file', 'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not path:
			return
		self._save_to_path(path)

	def _save_to_pat_12(self, path):
		text = self.ui_pages.plainTextEdit_6.toPlainText()
		try:
			with open(path, 'w') as f:
				f.write(text)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.path = path

	def on_pushButton_unload_20(self):
		path, filter = QFileDialog.getSaveFileName(self, 'Save file', 'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not path:
			return
		self._save_to_path(path)

	def _save_to_path_20(self, path):
		text = self.ui_pages.plainTextEdit_8.toPlainText()
		try:
			with open(path, 'w') as f:
				f.write(text)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.path = path

	def on_pushButton_unload_14(self):
		path, filter = QFileDialog.getSaveFileName(self, 'Save file', 'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not path:
			return
		self._save_to_path(path)

	def _save_to_path_14(self, path):
		text = self.ui_pages.plainTextEdit_4.toPlainText()
		try:
			with open(path, 'w') as f:
				f.write(text)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.path = path

	def shifrRSA(self):                 # Вывод шифрованного сообщения
		md = MyRSA()                      # Создание объекта класса
		text = self.ui_pages.plainTextEdit_5.toPlainText()  # Взятие текста из поля
		global N, e, f
		ret, N, e, f = md.encode_RSA(text)
		r, d, y = md.ext_gcd(e, f)
		self.ui_pages.plainTextEdit_4.setPlainText(str(d))
		self.ui_pages.plainTextEdit_8.setPlainText(str(e))
		shifr = " ".join(map(str, ret))
		self.ui_pages.plainTextEdit_6.setPlainText(shifr)

	def deshifrRSA(self):
		text = self.ui_pages.plainTextEdit_6.toPlainText()
		#e = self.key.toPlainText()
		md = MyRSA()
		r, d, y = md.ext_gcd(e, f)
		# self.ui_pages.plainTextEdit_4.setPlainText(str(d))
		noshifr21 = text.split()
		noshifr2 = [int(item) for item in noshifr21]
		noshifr1 = md.decode_RSA(noshifr2, N, e, f, r, d, y)
		noshifr = "".join(map(str, noshifr1))
		self.ui_pages.plainTextEdit_5.setPlainText(noshifr)


############################################### ELGAMAL ############################################


	def on_pushButton_download_23(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file', r'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not fname:
			return
		try:
			with open(fname[0], 'r') as f:
				data = f.read()
				self.ui_pages.plainTextEdit_10.setPlainText(data)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.fname = fname

	def on_pushButton_download_25(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file', r'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not fname:
			return
		try:
			with open(fname[0], 'r') as f:
				data = f.read()
				self.ui_pages.plainTextEdit_11.setPlainText(data)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.fname = fname

	def on_pushButton_download_21(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file', r'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not fname:
			return
		try:
			with open(fname[0], 'r') as f:
				data = f.read()
				self.ui_pages.plainTextEdit_9.setPlainText(data)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.fname = fname

	def on_pushButton_download_17(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file', r'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not fname:
			return
		try:
			with open(fname[0], 'r') as f:
				data = f.read()
				self.ui_pages.plainTextEdit_7.setPlainText(data)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.fname = fname


	def on_pushButton_unload_24(self):
		path, filter = QFileDialog.getSaveFileName(self, 'Save file', 'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not path:
			return
		self._save_to_path(path)

	def _save_to_path_24(self, path):
		text = self.ui_pages.plainTextEdit_10.toPlainText()
		try:
			with open(path, 'w') as f:
				f.write(text)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.path = path

	def on_pushButton_unload_26(self):
		path, filter = QFileDialog.getSaveFileName(self, 'Save file', 'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not path:
			return
		self._save_to_path(path)

	def _save_to_pat_26(self, path):
		text = self.ui_pages.plainTextEdit_11.toPlainText()
		try:
			with open(path, 'w') as f:
				f.write(text)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.path = path

	def on_pushButton_unload_22(self):
		path, filter = QFileDialog.getSaveFileName(self, 'Save file', 'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not path:
			return
		self._save_to_path(path)

	def _save_to_path_22(self, path):
		text = self.ui_pages.plainTextEdit_9.toPlainText()
		try:
			with open(path, 'w') as f:
				f.write(text)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.path = path

	def on_pushButton_unload_18(self):
		path, filter = QFileDialog.getSaveFileName(self, 'Save file', 'C:\\Users\\User\\Desktop', 'Text files (*.txt)')
		if not path:
			return
		self._save_to_path(path)

	def _save_to_path_18(self, path):
		text = self.ui_pages.plainTextEdit_7.toPlainText()
		try:
			with open(path, 'w') as f:
				f.write(text)
		except Exception as e:
			self.dialog_critical(str(e))
		else:
			self.path = path

# Вывод шифрованного сообщения
	def shifrELGAMAL(self):
		md = MyELGAMAL()              
		text = self.ui_pages.plainTextEdit_10.toPlainText()  # Взятие текста из поля
		p_q = self.ui_pages.plainTextEdit_9.toPlainText()
		P = int(p_q.split('-')[0])
		Y = int(p_q.split('-')[2])
		G = int(p_q.split('-')[1])

		R = random.randint(0, P - 1) # Сессионный ключ
		C1 = md.modexp(G, R, P)
		shifrtxt = []
		shifrtxt.append(str(C1))
		shifrtxt += '-'
		for i in range(0, len(text)):
			a = ord(text[i])
			
			C2 = ((a%P)*(md.modexp(Y, R, P)%P))%P
			shifrtxt += str(C2)
			shifrtxt += '-'
		shifr = "".join(map(str, shifrtxt))
		self.ui_pages.plainTextEdit_11.setPlainText(shifr)
		self.ui_pages.plainTextEdit_12.setPlainText(str(R))

		# Генерация сессионного ключа
		# --- k = md.gen_key(q)
		# --- self.ui_pages.plainTextEdit_12.setPlainText(str(k)) # SESSIA
		# k = int(self.ui_pages.plainTextEdit_12.toPlainText())
		# --- p_q = self.ui_pages.plainTextEdit_9.toPlainText()
		# --- q = int(p_q.split('-')[0])
		# --- en_text, p = md.encrypt(text, k, h, g, q) # шифрование
		# self.ui_pages.plainTextEdit_7.setPlainText(str(key)) # PRIVATE KEY
		# self.ui_pages.plainTextEdit_9.setPlainText(str(q) + "-" + str(g) + "-" + str(h)) # PUBLIC KEY (q, g, h)
		# shifr = " ".join(map(str, ret))
		# --- shifr = " ".join(map(str, en_text))
		# --- self.ui_pages.plainTextEdit_11.setPlainText(shifr + "-" + str(p))

	def deshifrELGAMAL(self):
		md = MyELGAMAL()
		n = 0
		C1 = 0
		key = self.ui_pages.plainTextEdit_9.toPlainText()
		#print(key)
		P = int(key.split('-')[0])
		A = int(self.ui_pages.plainTextEdit_7.toPlainText())

		text1 = self.ui_pages.plainTextEdit_11.toPlainText()
		text = text1.split('-')
		#C1 = int(text[0])
		#C2 = int(text[1])
		#for i in range(0,)


		S = int(text[0])
		obrC = md.invmod(S, P)
		C1 = md.modexp(obrC, A, P)
		text_msg = []
		#print("obrC = " +str(obrC))
		#print("S = " +str(S))
		#print("C1 = " +str(C1))
		#print("P = " +str(P))
		for i in range(1, len(text)-1):
			M = int(text[i])
			D = ((M%P)*(C1%P))%P

			text_msg.append(chr(D))
		noshifr = "".join(map(str, text_msg))
		self.ui_pages.plainTextEdit_10.setPlainText(noshifr)

		

		# --- key = int(self.ui_pages.plainTextEdit_7.toPlainText())
		# --- p1 = self.ui_pages.plainTextEdit_11.toPlainText()
		# --- p = int(p1.split('-')[1])
		# --- p_q = self.ui_pages.plainTextEdit_9.toPlainText()
		# --- q = int(p_q.split('-')[0])
		#h = int(p_q.split('-')[2])
		
		# --- noshifr21 = text.split()
		# --- noshifr2 = [int(item) for item in noshifr21]
		# --- text_msg = md.decrypt(noshifr2, key, p, q)
		
		# --- noshifr = "".join(map(str, text_msg))
		# --- self.ui_pages.plainTextEdit_10.setPlainText(noshifr)

	def KEYKEYKEY(self):
		md = MyELGAMAL()
		n = 0
		while n != 10:
			n = 0
			rnd = "1"
			b = [0]*10
			for i in range(0, 21):
				rnd += str(random.randint(0, 1))
			rnd += "1"
			bmodp = 0
			p = int(rnd, 2)

			# Тест ферма
			for j in range(10):
				b[j] = random.randint(0, p - 1)
				bmodp = md.modexp(b[j], p - 1, p)
				if bmodp != 1:
					break
				else:
					n += 1

		g = md.generator(p) # Первообразный корень
		a = random.randint(0, p - 2) # Секретный ключ
		y = md.modexp(g, a, p)
		P = p
		G = g
		Y = y
		A = a
		self.ui_pages.plainTextEdit_9.setPlainText(str(P) + "-" + str(G) + "-" + str(Y)) # PUBLIC KEY
		self.ui_pages.plainTextEdit_7.setPlainText(str(A)) # PRIVATE KEY





		
		# q = md.generator_p()
		# g = md.generator_g(q)
		# a = random.randint(0, q - 2)
		# --- q = random.randint(pow(10, 20), pow(10, 50)) # p 
		# --- g = random.randint(2, q) # g (число 1 < g < p)
		# --- key = md.gen_key(q)
		# --- h = md.power(g, key, q) # g^key * mod p
		# k = md.gen_key(q)
		# --- self.ui_pages.plainTextEdit_9.setPlainText(str(q) + "-" + str(g) + "-" + str(h)) # PUBLIC KEY (q, g, h)
		# === self.ui_pages.plainTextEdit_7.setPlainText(str(key)) # PRIVATE KEY
		# ---self.ui_pages.plainTextEdit_7.setPlainText(str(key)) # PRIVATE KEY
		# self.ui_pages.plainTextEdit_12.setPlainText(str(k)) # SESSIA