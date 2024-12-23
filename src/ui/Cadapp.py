# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CadApp.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLCDNumber, QLabel, QLayout, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_CadApp(object):
    def setupUi(self, CadApp):
        if not CadApp.objectName():
            CadApp.setObjectName(u"CadApp")
        CadApp.resize(660, 266)
        self.verticalLayout = QVBoxLayout(CadApp)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(CadApp)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.lcd_id = QLCDNumber(self.frame_3)
        self.lcd_id.setObjectName(u"lcd_id")
        self.lcd_id.setGeometry(QRect(10, 10, 64, 23))
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 110, 81, 16))
        self.plain_obs = QPlainTextEdit(self.frame_3)
        self.plain_obs.setObjectName(u"plain_obs")
        self.plain_obs.setGeometry(QRect(100, 110, 541, 51))
        self.text_nome = QLineEdit(self.frame_3)
        self.text_nome.setObjectName(u"text_nome")
        self.text_nome.setGeometry(QRect(10, 60, 611, 20))
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(11, 41, 171, 16))

        self.verticalLayout_3.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(1000, 94))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, -1, -1, 10)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.lbl_total = QLabel(self.frame_2)
        self.lbl_total.setObjectName(u"lbl_total")

        self.horizontalLayout_4.addWidget(self.lbl_total)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bnt_back_full = QPushButton(self.frame_2)
        self.bnt_back_full.setObjectName(u"bnt_back_full")
        self.bnt_back_full.setMinimumSize(QSize(75, 23))
        self.bnt_back_full.setMaximumSize(QSize(75, 23))
        self.bnt_back_full.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.bnt_back_full)

        self.bnt_back = QPushButton(self.frame_2)
        self.bnt_back.setObjectName(u"bnt_back")
        self.bnt_back.setMinimumSize(QSize(75, 23))
        self.bnt_back.setMaximumSize(QSize(75, 23))
        self.bnt_back.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.bnt_back)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.bnt_next = QPushButton(self.frame_2)
        self.bnt_next.setObjectName(u"bnt_next")
        self.bnt_next.setMinimumSize(QSize(75, 23))
        self.bnt_next.setMaximumSize(QSize(75, 23))
        self.bnt_next.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.bnt_next)

        self.bnt_next_full = QPushButton(self.frame_2)
        self.bnt_next_full.setObjectName(u"bnt_next_full")
        self.bnt_next_full.setMinimumSize(QSize(75, 23))
        self.bnt_next_full.setMaximumSize(QSize(75, 23))
        self.bnt_next_full.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.bnt_next_full)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.bnt_alterar = QPushButton(self.frame_2)
        self.bnt_alterar.setObjectName(u"bnt_alterar")
        self.bnt_alterar.setMinimumSize(QSize(100, 30))
        self.bnt_alterar.setMaximumSize(QSize(131, 41))
        icon = QIcon()
        icon.addFile(u":/icons/pencil.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_alterar.setIcon(icon)
        self.bnt_alterar.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.bnt_alterar)

        self.horizontalSpacer = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.bnt_adicionar = QPushButton(self.frame_2)
        self.bnt_adicionar.setObjectName(u"bnt_adicionar")
        self.bnt_adicionar.setEnabled(True)
        self.bnt_adicionar.setMinimumSize(QSize(100, 30))
        self.bnt_adicionar.setMaximumSize(QSize(131, 41))
        icon1 = QIcon()
        icon1.addFile(u":/icons/adicionar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_adicionar.setIcon(icon1)
        self.bnt_adicionar.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.bnt_adicionar)

        self.bnt_salvar = QPushButton(self.frame_2)
        self.bnt_salvar.setObjectName(u"bnt_salvar")
        self.bnt_salvar.setEnabled(False)
        self.bnt_salvar.setMinimumSize(QSize(100, 0))
        self.bnt_salvar.setMaximumSize(QSize(100, 36))
        icon2 = QIcon()
        icon2.addFile(u":/icons/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_salvar.setIcon(icon2)
        self.bnt_salvar.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.bnt_salvar)

        self.bnt_search = QPushButton(self.frame_2)
        self.bnt_search.setObjectName(u"bnt_search")
        self.bnt_search.setMinimumSize(QSize(100, 29))
        self.bnt_search.setMaximumSize(QSize(100, 41))
        icon3 = QIcon()
        icon3.addFile(u":/icons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_search.setIcon(icon3)
        self.bnt_search.setIconSize(QSize(17, 17))
        self.bnt_search.setCheckable(False)
        self.bnt_search.setChecked(False)
        self.bnt_search.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.bnt_search)

        self.bnt_excluir = QPushButton(self.frame_2)
        self.bnt_excluir.setObjectName(u"bnt_excluir")
        self.bnt_excluir.setMinimumSize(QSize(100, 20))
        self.bnt_excluir.setMaximumSize(QSize(131, 41))
        icon4 = QIcon()
        icon4.addFile(u":/icons/excluir.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_excluir.setIcon(icon4)
        self.bnt_excluir.setIconSize(QSize(25, 25))
        self.bnt_excluir.setCheckable(False)
        self.bnt_excluir.setChecked(False)
        self.bnt_excluir.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.bnt_excluir)

        self.bnt_cancelar = QPushButton(self.frame_2)
        self.bnt_cancelar.setObjectName(u"bnt_cancelar")
        self.bnt_cancelar.setMinimumSize(QSize(100, 30))
        self.bnt_cancelar.setMaximumSize(QSize(131, 41))
        icon5 = QIcon()
        icon5.addFile(u":/icons/error.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_cancelar.setIcon(icon5)
        self.bnt_cancelar.setIconSize(QSize(25, 25))
        self.bnt_cancelar.setCheckable(False)
        self.bnt_cancelar.setChecked(False)
        self.bnt_cancelar.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.bnt_cancelar)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        QWidget.setTabOrder(self.text_nome, self.plain_obs)
        QWidget.setTabOrder(self.plain_obs, self.bnt_alterar)
        QWidget.setTabOrder(self.bnt_alterar, self.bnt_adicionar)
        QWidget.setTabOrder(self.bnt_adicionar, self.bnt_cancelar)
        QWidget.setTabOrder(self.bnt_cancelar, self.bnt_search)
        QWidget.setTabOrder(self.bnt_search, self.bnt_excluir)
        QWidget.setTabOrder(self.bnt_excluir, self.bnt_next)
        QWidget.setTabOrder(self.bnt_next, self.bnt_next_full)
        QWidget.setTabOrder(self.bnt_next_full, self.bnt_back)
        QWidget.setTabOrder(self.bnt_back, self.bnt_back_full)
        QWidget.setTabOrder(self.bnt_back_full, self.bnt_salvar)

        self.retranslateUi(CadApp)

        QMetaObject.connectSlotsByName(CadApp)
    # setupUi

    def retranslateUi(self, CadApp):
        CadApp.setWindowTitle(QCoreApplication.translate("CadApp", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("CadApp", u"Observa\u00e7\u00e3o :", None))
        self.label.setText(QCoreApplication.translate("CadApp", u"Nome :", None))
        self.label_2.setText(QCoreApplication.translate("CadApp", u"Quantidade de cadastros:", None))
        self.lbl_total.setText(QCoreApplication.translate("CadApp", u"0", None))
#if QT_CONFIG(tooltip)
        self.bnt_back_full.setToolTip(QCoreApplication.translate("CadApp", u"<html><head/><body><p>Ir para o primeiro...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_back_full.setText(QCoreApplication.translate("CadApp", u"<<", None))
#if QT_CONFIG(tooltip)
        self.bnt_back.setToolTip(QCoreApplication.translate("CadApp", u"<html><head/><body><p>Voltar...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_back.setText(QCoreApplication.translate("CadApp", u"<", None))
#if QT_CONFIG(tooltip)
        self.bnt_next.setToolTip(QCoreApplication.translate("CadApp", u"<html><head/><body><p>Pr\u00f3ximo...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_next.setText(QCoreApplication.translate("CadApp", u">", None))
#if QT_CONFIG(tooltip)
        self.bnt_next_full.setToolTip(QCoreApplication.translate("CadApp", u"<html><head/><body><p><span style=\" font-weight:600;\">Ir para o fim.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_next_full.setText(QCoreApplication.translate("CadApp", u">>", None))
        self.bnt_alterar.setText(QCoreApplication.translate("CadApp", u"&Alterar", None))
        self.bnt_adicionar.setText(QCoreApplication.translate("CadApp", u"&Incluir", None))
#if QT_CONFIG(shortcut)
        self.bnt_adicionar.setShortcut(QCoreApplication.translate("CadApp", u"Alt+I", None))
#endif // QT_CONFIG(shortcut)
        self.bnt_salvar.setText(QCoreApplication.translate("CadApp", u"&Salvar", None))
#if QT_CONFIG(shortcut)
        self.bnt_salvar.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.bnt_search.setText(QCoreApplication.translate("CadApp", u"&Pesquisar", None))
#if QT_CONFIG(shortcut)
        self.bnt_search.setShortcut(QCoreApplication.translate("CadApp", u"Alt+P", None))
#endif // QT_CONFIG(shortcut)
        self.bnt_excluir.setText(QCoreApplication.translate("CadApp", u"&Excluir", None))
#if QT_CONFIG(shortcut)
        self.bnt_excluir.setShortcut(QCoreApplication.translate("CadApp", u"Alt+E", None))
#endif // QT_CONFIG(shortcut)
        self.bnt_cancelar.setText(QCoreApplication.translate("CadApp", u"&Cancelar", None))
#if QT_CONFIG(shortcut)
        self.bnt_cancelar.setShortcut(QCoreApplication.translate("CadApp", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

