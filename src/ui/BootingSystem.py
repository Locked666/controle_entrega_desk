# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BootingSystem.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QSizePolicy, QVBoxLayout, QWidget)

class Ui_booting_system(object):
    def setupUi(self, booting_system):
        if not booting_system.objectName():
            booting_system.setObjectName(u"booting_system")
        booting_system.resize(680, 400)
        self.centralwidget = QWidget(booting_system)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {	\n"
"	background-color: rgb(56, 58, 89);	\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 90, 661, 61))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 160, 661, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(14)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 280, 561, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	background-color: rgb(98, 114, 164);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progressBar.setValue(0)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(0, 320, 661, 21))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        self.label_loading.setFont(font2)
        self.label_loading.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(20, 350, 621, 21))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        self.label_credits.setFont(font3)
        self.label_credits.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_loading_execu = QLabel(self.dropShadowFrame)
        self.label_loading_execu.setObjectName(u"label_loading_execu")
        self.label_loading_execu.setGeometry(QRect(0, 250, 661, 21))
        self.label_loading_execu.setFont(font2)
        self.label_loading_execu.setStyleSheet(u"color: rgb(98, 114, 164);")
        self.label_loading_execu.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        booting_system.setCentralWidget(self.centralwidget)

        self.retranslateUi(booting_system)

        QMetaObject.connectSlotsByName(booting_system)
    # setupUi

    def retranslateUi(self, booting_system):
        booting_system.setWindowTitle(QCoreApplication.translate("booting_system", u"Inicializando", None))
        self.label_title.setText(QCoreApplication.translate("booting_system", u"<strong>Inicializando . . .</strong> ", None))
        self.label_description.setText(QCoreApplication.translate("booting_system", u"<strong>Sistema de Controle de Viagens</strong> ", None))
        self.progressBar.setFormat(QCoreApplication.translate("booting_system", u"%p%", None))
        self.label_loading.setText(QCoreApplication.translate("booting_system", u"Carregando...", None))
        self.label_credits.setText(QCoreApplication.translate("booting_system", u"<strong>Version</strong>: 1.0.0.0", None))
        self.label_loading_execu.setText(QCoreApplication.translate("booting_system", u"...", None))
    # retranslateUi

