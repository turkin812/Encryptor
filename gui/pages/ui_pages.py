# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pages.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_application_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(951, 556)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_5 = QVBoxLayout(self.page_1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.page_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(222, 222, 222)")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setStyleSheet(u"color: rgb(222, 222, 222)")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(222, 222, 222)")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_6)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignBottom)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        application_pages.addWidget(self.page_1)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_7 = QVBoxLayout(self.page_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_9 = QFrame(self.page_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_9)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, 0)
        self.plainTextEdit_5 = QPlainTextEdit(self.frame_9)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_5.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_5.setSizePolicy(sizePolicy)
        self.plainTextEdit_5.setMinimumSize(QSize(0, 0))
        self.plainTextEdit_5.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_5.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(30, 110, 0, 50));\n"
"color:rgba(255, 255, 255, 210);\n"
"border-radius:15px;")
        self.plainTextEdit_5.setCursorWidth(2)

        self.horizontalLayout_15.addWidget(self.plainTextEdit_5)

        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_14)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.pushButton_15 = QPushButton(self.frame_14)
        self.pushButton_15.setObjectName(u"pushButton_15")
        font1 = QFont()
        font1.setPointSize(65)
        font1.setBold(True)
        self.pushButton_15.setFont(font1)
        self.pushButton_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet(u"QPushButton#pushButton_15{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_15:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_15:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.verticalLayout_15.addWidget(self.pushButton_15, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_16 = QPushButton(self.frame_14)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setMinimumSize(QSize(81, 71))
        font2 = QFont()
        font2.setPointSize(65)
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.pushButton_16.setFont(font2)
        self.pushButton_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_16.setStyleSheet(u"QPushButton#pushButton_16{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_16:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_16:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.verticalLayout_15.addWidget(self.pushButton_16, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_14.addLayout(self.verticalLayout_15)


        self.horizontalLayout_15.addWidget(self.frame_14)

        self.plainTextEdit_6 = QPlainTextEdit(self.frame_9)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        sizePolicy.setHeightForWidth(self.plainTextEdit_6.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_6.setSizePolicy(sizePolicy)
        self.plainTextEdit_6.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(119, 0, 0, 50));\n"
"color:rgba(255, 255, 255, 210);\n"
"border-radius:15px;")
        self.plainTextEdit_6.setCursorWidth(2)

        self.horizontalLayout_15.addWidget(self.plainTextEdit_6)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_15)


        self.verticalLayout_16.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(10, 0, 10, 0)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 50, 0)
        self.pushButton_9 = QPushButton(self.frame_10)
        self.pushButton_9.setObjectName(u"pushButton_9")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        self.pushButton_9.setFont(font3)
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"QPushButton#pushButton_9{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_9:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_9:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.pushButton_9, 0, Qt.AlignLeft)

        self.pushButton_10 = QPushButton(self.frame_10)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font3)
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"QPushButton#pushButton_10{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_10:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_10:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")
        self.pushButton_10.setAutoDefault(False)

        self.horizontalLayout_11.addWidget(self.pushButton_10, 0, Qt.AlignLeft)


        self.horizontalLayout_10.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(50, 0, 0, 0)
        self.pushButton_11 = QPushButton(self.frame_11)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font3)
        self.pushButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet(u"QPushButton#pushButton_11{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_11:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_11:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.horizontalLayout_12.addWidget(self.pushButton_11, 0, Qt.AlignRight)

        self.pushButton_12 = QPushButton(self.frame_11)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setFont(font3)
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet(u"QPushButton#pushButton_12{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_12:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_12:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.horizontalLayout_12.addWidget(self.pushButton_12)


        self.horizontalLayout_10.addWidget(self.frame_11)


        self.verticalLayout_16.addLayout(self.horizontalLayout_10)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_15)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_15)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: rgb(222, 222, 222)")

        self.verticalLayout_17.addWidget(self.label_9, 0, Qt.AlignBottom)

        self.label_8 = QLabel(self.frame_15)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: rgb(222, 222, 222)")

        self.verticalLayout_17.addWidget(self.label_8, 0, Qt.AlignTop)


        self.horizontalLayout_14.addWidget(self.frame_15)

        self.plainTextEdit_8 = QPlainTextEdit(self.frame_12)
        self.plainTextEdit_8.setObjectName(u"plainTextEdit_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plainTextEdit_8.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_8.setSizePolicy(sizePolicy1)
        self.plainTextEdit_8.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(108, 104, 12, 100));\n"
"color:rgba(255, 255, 255, 210);\n"
"border-radius:15px;")
        self.plainTextEdit_8.setCursorWidth(2)

        self.horizontalLayout_14.addWidget(self.plainTextEdit_8, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_17 = QFrame(self.frame_12)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_17)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.pushButton_19 = QPushButton(self.frame_17)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setFont(font3)
        self.pushButton_19.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_19.setStyleSheet(u"QPushButton#pushButton_19{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_19:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_19:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.verticalLayout_18.addWidget(self.pushButton_19, 0, Qt.AlignLeft)

        self.pushButton_20 = QPushButton(self.frame_17)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setFont(font3)
        self.pushButton_20.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_20.setStyleSheet(u"QPushButton#pushButton_20{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_20:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_20:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.verticalLayout_18.addWidget(self.pushButton_20, 0, Qt.AlignLeft)


        self.horizontalLayout_14.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.frame_12)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_16)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_16)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: rgb(222, 222, 222)")

        self.verticalLayout_19.addWidget(self.label_10, 0, Qt.AlignBottom)

        self.label_7 = QLabel(self.frame_16)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(222, 222, 222)")

        self.verticalLayout_19.addWidget(self.label_7, 0, Qt.AlignTop)


        self.horizontalLayout_14.addWidget(self.frame_16)

        self.plainTextEdit_4 = QPlainTextEdit(self.frame_12)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        sizePolicy1.setHeightForWidth(self.plainTextEdit_4.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_4.setSizePolicy(sizePolicy1)
        self.plainTextEdit_4.setMinimumSize(QSize(0, 1))
        self.plainTextEdit_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(108, 104, 12, 100));\n"
"color:rgba(255, 255, 255, 210);\n"
"border-radius:15px;")
        self.plainTextEdit_4.setCursorWidth(2)
        self.plainTextEdit_4.setMaximumBlockCount(-5)
        self.plainTextEdit_4.setCenterOnScroll(False)

        self.horizontalLayout_14.addWidget(self.plainTextEdit_4)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_13)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.pushButton_13 = QPushButton(self.frame_13)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setFont(font3)
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet(u"QPushButton#pushButton_13{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_13:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_13:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.verticalLayout_13.addWidget(self.pushButton_13, 0, Qt.AlignLeft)

        self.pushButton_14 = QPushButton(self.frame_13)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setFont(font3)
        self.pushButton_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet(u"QPushButton#pushButton_14{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_14:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_14:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.verticalLayout_13.addWidget(self.pushButton_14, 0, Qt.AlignLeft)


        self.horizontalLayout_14.addWidget(self.frame_13)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_14)


        self.gridLayout_2.addWidget(self.frame_12, 0, 0, 1, 1)


        self.verticalLayout_16.addLayout(self.gridLayout_2)


        self.verticalLayout_7.addWidget(self.frame_9)

        application_pages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_8 = QVBoxLayout(self.page_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_18 = QFrame(self.page_5)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_18)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 0, -1, 0)
        self.plainTextEdit_10 = QPlainTextEdit(self.frame_18)
        self.plainTextEdit_10.setObjectName(u"plainTextEdit_10")
        sizePolicy.setHeightForWidth(self.plainTextEdit_10.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_10.setSizePolicy(sizePolicy)
        self.plainTextEdit_10.setMinimumSize(QSize(0, 0))
        self.plainTextEdit_10.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_10.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(30, 110, 0, 50));\n"
"color:rgba(255, 255, 255, 210);\n"
"border-radius:15px;")
        self.plainTextEdit_10.setCursorWidth(2)

        self.horizontalLayout_21.addWidget(self.plainTextEdit_10)

        self.frame_26 = QFrame(self.frame_18)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_26)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.pushButton_27 = QPushButton(self.frame_26)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setFont(font1)
        self.pushButton_27.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_27.setStyleSheet(u"QPushButton#pushButton_27{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_27:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_27:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.verticalLayout_25.addWidget(self.pushButton_27, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_28 = QPushButton(self.frame_26)
        self.pushButton_28.setObjectName(u"pushButton_28")
        sizePolicy.setHeightForWidth(self.pushButton_28.sizePolicy().hasHeightForWidth())
        self.pushButton_28.setSizePolicy(sizePolicy)
        self.pushButton_28.setMinimumSize(QSize(81, 71))
        self.pushButton_28.setFont(font2)
        self.pushButton_28.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_28.setStyleSheet(u"QPushButton#pushButton_28{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_28:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_28:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.verticalLayout_25.addWidget(self.pushButton_28, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_24.addLayout(self.verticalLayout_25)


        self.horizontalLayout_21.addWidget(self.frame_26)

        self.plainTextEdit_11 = QPlainTextEdit(self.frame_18)
        self.plainTextEdit_11.setObjectName(u"plainTextEdit_11")
        sizePolicy.setHeightForWidth(self.plainTextEdit_11.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_11.setSizePolicy(sizePolicy)
        self.plainTextEdit_11.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(119, 0, 0, 50));\n"
"color:rgba(255, 255, 255, 210);\n"
"border-radius:15px;")
        self.plainTextEdit_11.setCursorWidth(2)

        self.horizontalLayout_21.addWidget(self.plainTextEdit_11)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_21)


        self.verticalLayout_26.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(10, 0, 10, 0)
        self.frame_24 = QFrame(self.frame_18)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 50, 0)
        self.pushButton_23 = QPushButton(self.frame_24)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setFont(font3)
        self.pushButton_23.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_23.setStyleSheet(u"QPushButton#pushButton_23{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_23:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_23:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.horizontalLayout_18.addWidget(self.pushButton_23, 0, Qt.AlignLeft)

        self.pushButton_24 = QPushButton(self.frame_24)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setFont(font3)
        self.pushButton_24.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_24.setStyleSheet(u"QPushButton#pushButton_24{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_24:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_24:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")
        self.pushButton_24.setAutoDefault(False)

        self.horizontalLayout_18.addWidget(self.pushButton_24, 0, Qt.AlignLeft)


        self.horizontalLayout_17.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_18)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(50, 0, 0, 0)
        self.pushButton_25 = QPushButton(self.frame_25)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setFont(font3)
        self.pushButton_25.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_25.setStyleSheet(u"QPushButton#pushButton_25{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_25:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_25:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.horizontalLayout_19.addWidget(self.pushButton_25, 0, Qt.AlignRight)

        self.pushButton_26 = QPushButton(self.frame_25)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setFont(font3)
        self.pushButton_26.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_26.setStyleSheet(u"QPushButton#pushButton_26{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_26:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_26:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.horizontalLayout_19.addWidget(self.pushButton_26)


        self.horizontalLayout_17.addWidget(self.frame_25)


        self.verticalLayout_26.addLayout(self.horizontalLayout_17)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.plainTextEdit_12 = QPlainTextEdit(self.frame_18)
        self.plainTextEdit_12.setObjectName(u"plainTextEdit_12")
        self.plainTextEdit_12.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(108, 104, 12, 100));\n"
"color:rgba(255, 255, 255, 210);\n"
"border-radius:15px;")

        self.gridLayout_3.addWidget(self.plainTextEdit_12, 1, 1, 1, 1)

        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_20)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_20)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: rgb(222, 222, 222)")

        self.verticalLayout_20.addWidget(self.label_11, 0, Qt.AlignRight|Qt.AlignBottom)

        self.label_12 = QLabel(self.frame_20)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color: rgb(222, 222, 222)")

        self.verticalLayout_20.addWidget(self.label_12, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout_16.addWidget(self.frame_20)

        self.plainTextEdit_9 = QPlainTextEdit(self.frame_19)
        self.plainTextEdit_9.setObjectName(u"plainTextEdit_9")
        sizePolicy1.setHeightForWidth(self.plainTextEdit_9.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_9.setSizePolicy(sizePolicy1)
        self.plainTextEdit_9.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(108, 104, 12, 100));\n"
"color:rgba(255, 255, 255, 210);\n"
"border-radius:15px;")
        self.plainTextEdit_9.setCursorWidth(2)

        self.horizontalLayout_16.addWidget(self.plainTextEdit_9, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_21)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.pushButton_21 = QPushButton(self.frame_21)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setFont(font3)
        self.pushButton_21.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_21.setStyleSheet(u"QPushButton#pushButton_21{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_21:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_21:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.verticalLayout_21.addWidget(self.pushButton_21, 0, Qt.AlignLeft)

        self.pushButton_22 = QPushButton(self.frame_21)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setFont(font3)
        self.pushButton_22.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_22.setStyleSheet(u"QPushButton#pushButton_22{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_22:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_22:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.verticalLayout_21.addWidget(self.pushButton_22, 0, Qt.AlignLeft)


        self.horizontalLayout_16.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_22)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_22)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color: rgb(222, 222, 222)")

        self.verticalLayout_22.addWidget(self.label_13, 0, Qt.AlignRight|Qt.AlignBottom)

        self.label_14 = QLabel(self.frame_22)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"color: rgb(222, 222, 222)")

        self.verticalLayout_22.addWidget(self.label_14, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout_16.addWidget(self.frame_22)

        self.plainTextEdit_7 = QPlainTextEdit(self.frame_19)
        self.plainTextEdit_7.setObjectName(u"plainTextEdit_7")
        sizePolicy1.setHeightForWidth(self.plainTextEdit_7.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_7.setSizePolicy(sizePolicy1)
        self.plainTextEdit_7.setMinimumSize(QSize(0, 1))
        self.plainTextEdit_7.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(108, 104, 12, 100));\n"
"color:rgba(255, 255, 255, 210);\n"
"border-radius:15px;")
        self.plainTextEdit_7.setCursorWidth(2)
        self.plainTextEdit_7.setMaximumBlockCount(-5)
        self.plainTextEdit_7.setCenterOnScroll(False)

        self.horizontalLayout_16.addWidget(self.plainTextEdit_7)

        self.frame_23 = QFrame(self.frame_19)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_23)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.pushButton_17 = QPushButton(self.frame_23)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setFont(font3)
        self.pushButton_17.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_17.setStyleSheet(u"QPushButton#pushButton_17{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_17:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_17:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.verticalLayout_23.addWidget(self.pushButton_17, 0, Qt.AlignLeft)

        self.pushButton_18 = QPushButton(self.frame_23)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setFont(font3)
        self.pushButton_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_18.setStyleSheet(u"QPushButton#pushButton_18{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_18:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_18:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.verticalLayout_23.addWidget(self.pushButton_18, 0, Qt.AlignLeft)


        self.horizontalLayout_16.addWidget(self.frame_23)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_16)


        self.gridLayout_3.addWidget(self.frame_19, 0, 1, 1, 1)

        self.label_4 = QLabel(self.frame_18)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(222, 222, 222)")

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1, Qt.AlignRight)

        self.pushButton_29 = QPushButton(self.frame_18)
        self.pushButton_29.setObjectName(u"pushButton_29")
        font4 = QFont()
        font4.setPointSize(12)
        self.pushButton_29.setFont(font4)
        self.pushButton_29.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_29.setStyleSheet(u"QPushButton#pushButton_29{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_29:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_29:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.pushButton_29, 0, 0, 1, 1, Qt.AlignLeft)


        self.verticalLayout_26.addLayout(self.gridLayout_3)


        self.verticalLayout_8.addWidget(self.frame_18)

        application_pages.addWidget(self.page_5)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.page_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.plainTextEdit = QPlainTextEdit(self.frame_3)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMinimumSize(QSize(0, 0))
        self.plainTextEdit.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(30, 110, 0, 50));\n"
"color:rgba(255, 255, 255, 210);\n"
"border-radius:15px;")
        self.plainTextEdit.setCursorWidth(2)

        self.horizontalLayout_6.addWidget(self.plainTextEdit)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton#pushButton_2{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.verticalLayout_10.addWidget(self.pushButton_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QSize(81, 71))
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton#pushButton_3{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_3:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_3:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.verticalLayout_10.addWidget(self.pushButton_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)


        self.horizontalLayout_6.addWidget(self.frame_4)

        self.plainTextEdit_2 = QPlainTextEdit(self.frame_3)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        sizePolicy.setHeightForWidth(self.plainTextEdit_2.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_2.setSizePolicy(sizePolicy)
        self.plainTextEdit_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(119, 0, 0, 50));\n"
"color:rgba(255, 255, 255, 210);\n"
"border-radius:15px;")
        self.plainTextEdit_2.setCursorWidth(2)

        self.horizontalLayout_6.addWidget(self.plainTextEdit_2)


        self.horizontalLayout.addLayout(self.horizontalLayout_6)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 0, 10, 0)
        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 50, 0)
        self.pushButton_6 = QPushButton(self.frame_8)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font3)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"QPushButton#pushButton_6{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_6:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_6:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.pushButton_6, 0, Qt.AlignLeft)

        self.pushButton_7 = QPushButton(self.frame_8)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font3)
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"QPushButton#pushButton_7{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_7:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_7:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")
        self.pushButton_7.setAutoDefault(False)

        self.horizontalLayout_8.addWidget(self.pushButton_7, 0, Qt.AlignLeft)


        self.horizontalLayout_5.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(50, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_7)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font3)
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"QPushButton#pushButton_4{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_4:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_4:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.pushButton_4, 0, Qt.AlignRight)

        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font3)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.horizontalLayout_9.addWidget(self.pushButton)


        self.horizontalLayout_5.addWidget(self.frame_7)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 40, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(222, 222, 222)")

        self.horizontalLayout_4.addWidget(self.label_2, 0, Qt.AlignRight)

        self.plainTextEdit_3 = QPlainTextEdit(self.frame_6)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        sizePolicy1.setHeightForWidth(self.plainTextEdit_3.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_3.setSizePolicy(sizePolicy1)
        self.plainTextEdit_3.setMinimumSize(QSize(0, 1))
        self.plainTextEdit_3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(108, 104, 12, 100));\n"
"color:rgba(255, 255, 255, 210);\n"
"border-radius:15px;")
        self.plainTextEdit_3.setCursorWidth(2)
        self.plainTextEdit_3.setMaximumBlockCount(-5)
        self.plainTextEdit_3.setCenterOnScroll(False)

        self.horizontalLayout_4.addWidget(self.plainTextEdit_3, 0, Qt.AlignVCenter)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(10, 0, 10, 0)
        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font3)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"QPushButton#pushButton_5{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_5:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_5:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.verticalLayout_12.addWidget(self.pushButton_5, 0, Qt.AlignLeft)

        self.pushButton_8 = QPushButton(self.frame_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font3)
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"QPushButton#pushButton_8{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color:rgba(85, 98, 112, 255);\n"
"border-radius:30px;\n"
"}\n"
"QPushButton#pushButton_8:hover{\n"
"color: rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_8:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color: rgba(115, 128, 142, 255);\n"
"}\n"
"")

        self.verticalLayout_12.addWidget(self.pushButton_8, 0, Qt.AlignLeft)


        self.horizontalLayout_4.addWidget(self.frame_5)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)


        self.gridLayout.addWidget(self.frame_6, 0, 0, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.frame_3)

        application_pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        application_pages.addWidget(self.page_3)

        self.retranslateUi(application_pages)

        application_pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(application_pages)
    # setupUi

    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("application_pages", u"StackedWidget", None))
        self.label_3.setText(QCoreApplication.translate("application_pages", u"Hi, I'm a cryptographer", None))
        self.label_5.setText(QCoreApplication.translate("application_pages", u"Choose one of 3 encryption algorithms", None))
        self.label_6.setText(QCoreApplication.translate("application_pages", u"Click on the menu icon on the top left", None))
        self.plainTextEdit_5.setPlaceholderText(QCoreApplication.translate("application_pages", u"    Entet text", None))
        self.pushButton_15.setText(QCoreApplication.translate("application_pages", u"\u00ab", None))
        self.pushButton_16.setText(QCoreApplication.translate("application_pages", u"\u00bb", None))
        self.plainTextEdit_6.setPlaceholderText(QCoreApplication.translate("application_pages", u"    Enter cipher text", None))
        self.pushButton_9.setText(QCoreApplication.translate("application_pages", u" DOWNLOAD ", None))
        self.pushButton_10.setText(QCoreApplication.translate("application_pages", u" UNLOAD ", None))
        self.pushButton_11.setText(QCoreApplication.translate("application_pages", u" DOWNLOAD ", None))
        self.pushButton_12.setText(QCoreApplication.translate("application_pages", u" UNLOAD ", None))
        self.label_9.setText(QCoreApplication.translate("application_pages", u"PUBLIC ", None))
        self.label_8.setText(QCoreApplication.translate("application_pages", u"KEY", None))
        self.plainTextEdit_8.setPlaceholderText(QCoreApplication.translate("application_pages", u"    Entet public key", None))
        self.pushButton_19.setText(QCoreApplication.translate("application_pages", u" DOWNLOAD ", None))
        self.pushButton_20.setText(QCoreApplication.translate("application_pages", u" UNLOAD ", None))
        self.label_10.setText(QCoreApplication.translate("application_pages", u"PRIVATE ", None))
        self.label_7.setText(QCoreApplication.translate("application_pages", u"KEY", None))
        self.plainTextEdit_4.setPlaceholderText(QCoreApplication.translate("application_pages", u"    Entet private key", None))
        self.pushButton_13.setText(QCoreApplication.translate("application_pages", u" DOWNLOAD ", None))
        self.pushButton_14.setText(QCoreApplication.translate("application_pages", u" UNLOAD ", None))
        self.plainTextEdit_10.setPlaceholderText(QCoreApplication.translate("application_pages", u"    Entet text", None))
        self.pushButton_27.setText(QCoreApplication.translate("application_pages", u"\u00ab", None))
        self.pushButton_28.setText(QCoreApplication.translate("application_pages", u"\u00bb", None))
        self.plainTextEdit_11.setPlaceholderText(QCoreApplication.translate("application_pages", u"    Enter cipher text", None))
        self.pushButton_23.setText(QCoreApplication.translate("application_pages", u" DOWNLOAD ", None))
        self.pushButton_24.setText(QCoreApplication.translate("application_pages", u" UNLOAD ", None))
        self.pushButton_25.setText(QCoreApplication.translate("application_pages", u" DOWNLOAD ", None))
        self.pushButton_26.setText(QCoreApplication.translate("application_pages", u" UNLOAD ", None))
        self.plainTextEdit_12.setPlaceholderText(QCoreApplication.translate("application_pages", u"    Session key", None))
        self.label_11.setText(QCoreApplication.translate("application_pages", u"PUBLIC ", None))
        self.label_12.setText(QCoreApplication.translate("application_pages", u"KEY ", None))
        self.plainTextEdit_9.setPlaceholderText(QCoreApplication.translate("application_pages", u"    Entet public key", None))
        self.pushButton_21.setText(QCoreApplication.translate("application_pages", u" DOWNLOAD ", None))
        self.pushButton_22.setText(QCoreApplication.translate("application_pages", u" UNLOAD ", None))
        self.label_13.setText(QCoreApplication.translate("application_pages", u"PRIVATE ", None))
        self.label_14.setText(QCoreApplication.translate("application_pages", u"KEY ", None))
        self.plainTextEdit_7.setPlaceholderText(QCoreApplication.translate("application_pages", u"    Entet private key", None))
        self.pushButton_17.setText(QCoreApplication.translate("application_pages", u" DOWNLOAD ", None))
        self.pushButton_18.setText(QCoreApplication.translate("application_pages", u" UNLOAD ", None))
        self.label_4.setText(QCoreApplication.translate("application_pages", u"Session key ", None))
        self.pushButton_29.setText(QCoreApplication.translate("application_pages", u"Key generation", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("application_pages", u"    Entet text", None))
        self.pushButton_2.setText(QCoreApplication.translate("application_pages", u"\u00ab", None))
        self.pushButton_3.setText(QCoreApplication.translate("application_pages", u"\u00bb", None))
        self.plainTextEdit_2.setPlaceholderText(QCoreApplication.translate("application_pages", u"    Enter cipher text", None))
        self.pushButton_6.setText(QCoreApplication.translate("application_pages", u" DOWNLOAD ", None))
        self.pushButton_7.setText(QCoreApplication.translate("application_pages", u" UNLOAD ", None))
        self.pushButton_4.setText(QCoreApplication.translate("application_pages", u" DOWNLOAD ", None))
        self.pushButton.setText(QCoreApplication.translate("application_pages", u" UNLOAD ", None))
        self.label_2.setText(QCoreApplication.translate("application_pages", u"KEY    ", None))
        self.plainTextEdit_3.setPlaceholderText(QCoreApplication.translate("application_pages", u"    Entet key", None))
        self.pushButton_5.setText(QCoreApplication.translate("application_pages", u" DOWNLOAD ", None))
        self.pushButton_8.setText(QCoreApplication.translate("application_pages", u" UNLOAD ", None))
        self.label.setText(QCoreApplication.translate("application_pages", u"There will be an agreement", None))
    # retranslateUi

