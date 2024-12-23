# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SelectThema.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_SelectThema(object):
    def setupUi(self, SelectThema):
        if not SelectThema.objectName():
            SelectThema.setObjectName(u"SelectThema")
        SelectThema.resize(212, 92)
        icon = QIcon()
        icon.addFile(u":/icons/ico.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        SelectThema.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(SelectThema)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(SelectThema)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.combobox_thema = QComboBox(self.frame)
        self.combobox_thema.addItem("")
        self.combobox_thema.addItem("")
        self.combobox_thema.setObjectName(u"combobox_thema")
        font = QFont()
        font.setStyleStrategy(QFont.PreferAntialias)
        self.combobox_thema.setFont(font)
        self.combobox_thema.setContextMenuPolicy(Qt.NoContextMenu)
        self.combobox_thema.setLayoutDirection(Qt.LeftToRight)
        self.combobox_thema.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.verticalLayout_2.addWidget(self.combobox_thema)

        self.bnt_okay = QPushButton(self.frame)
        self.bnt_okay.setObjectName(u"bnt_okay")

        self.verticalLayout_2.addWidget(self.bnt_okay)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(SelectThema)

        QMetaObject.connectSlotsByName(SelectThema)
    # setupUi

    def retranslateUi(self, SelectThema):
        SelectThema.setWindowTitle(QCoreApplication.translate("SelectThema", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("SelectThema", u"Selecione o Tema :", None))
        self.combobox_thema.setItemText(0, QCoreApplication.translate("SelectThema", u"Escuro", None))
        self.combobox_thema.setItemText(1, QCoreApplication.translate("SelectThema", u"Claro", None))

        self.bnt_okay.setText(QCoreApplication.translate("SelectThema", u"Okay", None))
    # retranslateUi

