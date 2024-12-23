# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LancAbastecimento.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateTimeEdit,
    QDialog, QFrame, QGroupBox, QHBoxLayout,
    QLCDNumber, QLabel, QLayout, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)
import icons_rc

class Ui_LancAbastecimento(object):
    def setupUi(self, LancAbastecimento):
        if not LancAbastecimento.objectName():
            LancAbastecimento.setObjectName(u"LancAbastecimento")
        LancAbastecimento.resize(668, 459)
        LancAbastecimento.setMinimumSize(QSize(668, 459))
        LancAbastecimento.setMaximumSize(QSize(700, 500))
        icon = QIcon()
        icon.addFile(u":/icons/ico.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        LancAbastecimento.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(LancAbastecimento)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(LancAbastecimento)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(668, 409))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_3 = QTabWidget(self.frame)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setMaximumSize(QSize(700, 500))
        self.tabWidget_3Page1 = QWidget()
        self.tabWidget_3Page1.setObjectName(u"tabWidget_3Page1")
        self.lcd_id = QLCDNumber(self.tabWidget_3Page1)
        self.lcd_id.setObjectName(u"lcd_id")
        self.lcd_id.setGeometry(QRect(40, 10, 64, 23))
        self.lcd_id.setMaximumSize(QSize(64, 23))
        self.layoutWidget = QWidget(self.tabWidget_3Page1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 40, 565, 271))
        self.verticalLayout_16 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.date_lanc_abastecimento = QDateTimeEdit(self.layoutWidget)
        self.date_lanc_abastecimento.setObjectName(u"date_lanc_abastecimento")
        self.date_lanc_abastecimento.setWrapping(False)
        self.date_lanc_abastecimento.setFrame(True)
        self.date_lanc_abastecimento.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.date_lanc_abastecimento.setAccelerated(True)
        self.date_lanc_abastecimento.setProperty(u"showGroupSeparator", False)
        self.date_lanc_abastecimento.setDateTime(QDateTime(QDate(2024, 11, 1), QTime(0, 0, 0)))
        self.date_lanc_abastecimento.setCalendarPopup(True)
        self.date_lanc_abastecimento.setTimeSpec(Qt.LocalTime)

        self.verticalLayout_5.addWidget(self.date_lanc_abastecimento)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_9.addWidget(self.label_8)

        self.combobox_tipo_combustivel = QComboBox(self.layoutWidget)
        self.combobox_tipo_combustivel.addItem("")
        self.combobox_tipo_combustivel.addItem("")
        self.combobox_tipo_combustivel.addItem("")
        self.combobox_tipo_combustivel.addItem("")
        self.combobox_tipo_combustivel.setObjectName(u"combobox_tipo_combustivel")

        self.verticalLayout_9.addWidget(self.combobox_tipo_combustivel)


        self.horizontalLayout_2.addLayout(self.verticalLayout_9)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(5, 5, 5, 5)
        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_14.addWidget(self.label_13)

        self.combobox_tipo_pagamento = QComboBox(self.layoutWidget)
        self.combobox_tipo_pagamento.addItem("")
        self.combobox_tipo_pagamento.addItem("")
        self.combobox_tipo_pagamento.addItem("")
        self.combobox_tipo_pagamento.addItem("")
        self.combobox_tipo_pagamento.setObjectName(u"combobox_tipo_pagamento")

        self.verticalLayout_14.addWidget(self.combobox_tipo_pagamento)


        self.horizontalLayout_2.addLayout(self.verticalLayout_14)


        self.verticalLayout_15.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(221, 139))
        self.layoutWidget_2 = QWidget(self.groupBox)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 80, 81, 52))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 9)
        self.label_6 = QLabel(self.layoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)

        self.text_media_lt = QLineEdit(self.layoutWidget_2)
        self.text_media_lt.setObjectName(u"text_media_lt")

        self.verticalLayout_7.addWidget(self.text_media_lt)

        self.layoutWidget1 = QWidget(self.groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(100, 20, 81, 49))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.label_5 = QLabel(self.layoutWidget1)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.text_trip = QLineEdit(self.layoutWidget1)
        self.text_trip.setObjectName(u"text_trip")

        self.verticalLayout_6.addWidget(self.text_trip)

        self.layoutWidget2 = QWidget(self.groupBox)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 20, 81, 52))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.layoutWidget2)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.text_km_rodados = QLineEdit(self.layoutWidget2)
        self.text_km_rodados.setObjectName(u"text_km_rodados")
        self.text_km_rodados.setInputMethodHints(Qt.ImhFormattedNumbersOnly)

        self.verticalLayout_4.addWidget(self.text_km_rodados)


        self.horizontalLayout_5.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(321, 121))
        self.layoutWidget_4 = QWidget(self.groupBox_2)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 80, 111, 52))
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 9)
        self.label_9 = QLabel(self.layoutWidget_4)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_10.addWidget(self.label_9)

        self.text_valor_lt = QLineEdit(self.layoutWidget_4)
        self.text_valor_lt.setObjectName(u"text_valor_lt")

        self.verticalLayout_10.addWidget(self.text_valor_lt)

        self.layoutWidget_5 = QWidget(self.groupBox_2)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(10, 20, 291, 53))
        self.verticalLayout_11 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 10)
        self.label_10 = QLabel(self.layoutWidget_5)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_11.addWidget(self.label_10)

        self.text_nome_posto = QLineEdit(self.layoutWidget_5)
        self.text_nome_posto.setObjectName(u"text_nome_posto")
        self.text_nome_posto.setDragEnabled(True)
        self.text_nome_posto.setClearButtonEnabled(True)

        self.verticalLayout_11.addWidget(self.text_nome_posto)

        self.layoutWidget_6 = QWidget(self.groupBox_2)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(130, 80, 81, 52))
        self.verticalLayout_12 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 9)
        self.label_11 = QLabel(self.layoutWidget_6)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_12.addWidget(self.label_11)

        self.text_qt_lt = QLineEdit(self.layoutWidget_6)
        self.text_qt_lt.setObjectName(u"text_qt_lt")

        self.verticalLayout_12.addWidget(self.text_qt_lt)

        self.layoutWidget_7 = QWidget(self.groupBox_2)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(220, 80, 81, 52))
        self.verticalLayout_13 = QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 9)
        self.label_12 = QLabel(self.layoutWidget_7)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_13.addWidget(self.label_12)

        self.text_valor_total = QLineEdit(self.layoutWidget_7)
        self.text_valor_total.setObjectName(u"text_valor_total")

        self.verticalLayout_13.addWidget(self.text_valor_total)


        self.horizontalLayout_5.addWidget(self.groupBox_2)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_15.addLayout(self.horizontalLayout_5)


        self.verticalLayout_16.addLayout(self.verticalLayout_15)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(81, 16))

        self.horizontalLayout_7.addWidget(self.label_3)

        self.plain_obs = QPlainTextEdit(self.layoutWidget)
        self.plain_obs.setObjectName(u"plain_obs")
        self.plain_obs.setMaximumSize(QSize(468, 51))

        self.horizontalLayout_7.addWidget(self.plain_obs)


        self.verticalLayout_16.addLayout(self.horizontalLayout_7)

        self.tabWidget_3.addTab(self.tabWidget_3Page1, "")

        self.verticalLayout_3.addWidget(self.tabWidget_3)

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
        icon1 = QIcon()
        icon1.addFile(u":/icons/pencil.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_alterar.setIcon(icon1)
        self.bnt_alterar.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.bnt_alterar)

        self.horizontalSpacer = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.bnt_adicionar = QPushButton(self.frame_2)
        self.bnt_adicionar.setObjectName(u"bnt_adicionar")
        self.bnt_adicionar.setEnabled(True)
        self.bnt_adicionar.setMinimumSize(QSize(100, 30))
        self.bnt_adicionar.setMaximumSize(QSize(131, 41))
        icon2 = QIcon()
        icon2.addFile(u":/icons/adicionar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_adicionar.setIcon(icon2)
        self.bnt_adicionar.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.bnt_adicionar)

        self.bnt_salvar = QPushButton(self.frame_2)
        self.bnt_salvar.setObjectName(u"bnt_salvar")
        self.bnt_salvar.setEnabled(False)
        self.bnt_salvar.setMinimumSize(QSize(100, 0))
        self.bnt_salvar.setMaximumSize(QSize(100, 36))
        icon3 = QIcon()
        icon3.addFile(u":/icons/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_salvar.setIcon(icon3)
        self.bnt_salvar.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.bnt_salvar)

        self.bnt_search = QPushButton(self.frame_2)
        self.bnt_search.setObjectName(u"bnt_search")
        self.bnt_search.setMinimumSize(QSize(100, 29))
        self.bnt_search.setMaximumSize(QSize(100, 41))
        icon4 = QIcon()
        icon4.addFile(u":/icons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_search.setIcon(icon4)
        self.bnt_search.setIconSize(QSize(17, 17))
        self.bnt_search.setCheckable(False)
        self.bnt_search.setChecked(False)
        self.bnt_search.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.bnt_search)

        self.bnt_excluir = QPushButton(self.frame_2)
        self.bnt_excluir.setObjectName(u"bnt_excluir")
        self.bnt_excluir.setMinimumSize(QSize(100, 20))
        self.bnt_excluir.setMaximumSize(QSize(131, 41))
        icon5 = QIcon()
        icon5.addFile(u":/icons/excluir.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_excluir.setIcon(icon5)
        self.bnt_excluir.setIconSize(QSize(25, 25))
        self.bnt_excluir.setCheckable(False)
        self.bnt_excluir.setChecked(False)
        self.bnt_excluir.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.bnt_excluir)

        self.bnt_cancelar = QPushButton(self.frame_2)
        self.bnt_cancelar.setObjectName(u"bnt_cancelar")
        self.bnt_cancelar.setMinimumSize(QSize(100, 30))
        self.bnt_cancelar.setMaximumSize(QSize(131, 41))
        icon6 = QIcon()
        icon6.addFile(u":/icons/error.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_cancelar.setIcon(icon6)
        self.bnt_cancelar.setIconSize(QSize(25, 25))
        self.bnt_cancelar.setCheckable(False)
        self.bnt_cancelar.setChecked(False)
        self.bnt_cancelar.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.bnt_cancelar)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        QWidget.setTabOrder(self.date_lanc_abastecimento, self.combobox_tipo_combustivel)
        QWidget.setTabOrder(self.combobox_tipo_combustivel, self.combobox_tipo_pagamento)
        QWidget.setTabOrder(self.combobox_tipo_pagamento, self.text_km_rodados)
        QWidget.setTabOrder(self.text_km_rodados, self.text_trip)
        QWidget.setTabOrder(self.text_trip, self.text_media_lt)
        QWidget.setTabOrder(self.text_media_lt, self.text_nome_posto)
        QWidget.setTabOrder(self.text_nome_posto, self.text_valor_lt)
        QWidget.setTabOrder(self.text_valor_lt, self.text_qt_lt)
        QWidget.setTabOrder(self.text_qt_lt, self.text_valor_total)
        QWidget.setTabOrder(self.text_valor_total, self.plain_obs)
        QWidget.setTabOrder(self.plain_obs, self.bnt_cancelar)
        QWidget.setTabOrder(self.bnt_cancelar, self.bnt_salvar)
        QWidget.setTabOrder(self.bnt_salvar, self.bnt_alterar)
        QWidget.setTabOrder(self.bnt_alterar, self.bnt_adicionar)
        QWidget.setTabOrder(self.bnt_adicionar, self.bnt_excluir)
        QWidget.setTabOrder(self.bnt_excluir, self.bnt_search)
        QWidget.setTabOrder(self.bnt_search, self.bnt_next_full)
        QWidget.setTabOrder(self.bnt_next_full, self.bnt_next)
        QWidget.setTabOrder(self.bnt_next, self.bnt_back)
        QWidget.setTabOrder(self.bnt_back, self.bnt_back_full)

        self.retranslateUi(LancAbastecimento)

        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(LancAbastecimento)
    # setupUi

    def retranslateUi(self, LancAbastecimento):
        LancAbastecimento.setWindowTitle(QCoreApplication.translate("LancAbastecimento", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("LancAbastecimento", u"Data do Lan\u00e7amento :", None))
        self.label_8.setText(QCoreApplication.translate("LancAbastecimento", u"Tipo de Combustivel", None))
        self.combobox_tipo_combustivel.setItemText(0, QCoreApplication.translate("LancAbastecimento", u"Gasolina", None))
        self.combobox_tipo_combustivel.setItemText(1, QCoreApplication.translate("LancAbastecimento", u"Gasolina Aditivada", None))
        self.combobox_tipo_combustivel.setItemText(2, QCoreApplication.translate("LancAbastecimento", u"Alcool", None))
        self.combobox_tipo_combustivel.setItemText(3, QCoreApplication.translate("LancAbastecimento", u"Alcool Aditivado", None))

        self.label_13.setText(QCoreApplication.translate("LancAbastecimento", u"Forma de Pagamento :", None))
        self.combobox_tipo_pagamento.setItemText(0, QCoreApplication.translate("LancAbastecimento", u"Cr\u00e9dito ", None))
        self.combobox_tipo_pagamento.setItemText(1, QCoreApplication.translate("LancAbastecimento", u"D\u00e9bito", None))
        self.combobox_tipo_pagamento.setItemText(2, QCoreApplication.translate("LancAbastecimento", u"Dinheiro", None))
        self.combobox_tipo_pagamento.setItemText(3, QCoreApplication.translate("LancAbastecimento", u"Outros", None))

        self.groupBox.setTitle(QCoreApplication.translate("LancAbastecimento", u"Informa\u00e7\u00f5es Inciais do Ve\u00edculo. ", None))
        self.label_6.setText(QCoreApplication.translate("LancAbastecimento", u"Media/ Lt :", None))
#if QT_CONFIG(tooltip)
        self.text_media_lt.setToolTip(QCoreApplication.translate("LancAbastecimento", u"<html><head/><body><p>M\u00e9dia de Km/Lt feito pelo ve\u00edculo at\u00e9 o momento. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.text_media_lt.setText(QCoreApplication.translate("LancAbastecimento", u"0", None))
        self.label_5.setText(QCoreApplication.translate("LancAbastecimento", u"Trip :", None))
#if QT_CONFIG(tooltip)
        self.text_trip.setToolTip(QCoreApplication.translate("LancAbastecimento", u"<html><head/><body><p><span style=\" font-size:10pt;\">Marcador de KM por abasteciemento </span><span style=\" font-size:10pt; font-weight:600;\">Se houver</span><span style=\" font-size:10pt;\"> !!</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.text_trip.setText(QCoreApplication.translate("LancAbastecimento", u"0", None))
        self.label.setText(QCoreApplication.translate("LancAbastecimento", u"Km rodados :", None))
#if QT_CONFIG(tooltip)
        self.text_km_rodados.setToolTip(QCoreApplication.translate("LancAbastecimento", u"<html><head/><body><p><span style=\" font-size:10pt;\">Quantidade de Km rodados no veiculo. </span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.text_km_rodados.setInputMask("")
        self.text_km_rodados.setText(QCoreApplication.translate("LancAbastecimento", u"0", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("LancAbastecimento", u"Informa\u00e7\u00f5es do abastecimento", None))
        self.label_9.setText(QCoreApplication.translate("LancAbastecimento", u"Valor Lt :", None))
#if QT_CONFIG(tooltip)
        self.text_valor_lt.setToolTip(QCoreApplication.translate("LancAbastecimento", u"<html><head/><body><p>Valor pago por Litro</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.text_valor_lt.setText(QCoreApplication.translate("LancAbastecimento", u"0", None))
        self.label_10.setText(QCoreApplication.translate("LancAbastecimento", u"Nome do Posto ", None))
#if QT_CONFIG(tooltip)
        self.text_nome_posto.setToolTip(QCoreApplication.translate("LancAbastecimento", u"<html><head/><body><p><span style=\" font-size:10pt;\">Nome do Posto Abastecido</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("LancAbastecimento", u"Qt de Lt :", None))
#if QT_CONFIG(tooltip)
        self.text_qt_lt.setToolTip(QCoreApplication.translate("LancAbastecimento", u"<html><head/><body><p>Quantidade de litros Abastecidos</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.text_qt_lt.setText(QCoreApplication.translate("LancAbastecimento", u"0", None))
        self.label_12.setText(QCoreApplication.translate("LancAbastecimento", u"Valor Total :", None))
#if QT_CONFIG(tooltip)
        self.text_valor_total.setToolTip(QCoreApplication.translate("LancAbastecimento", u"<html><head/><body><p>Valor Total Abastecido</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.text_valor_total.setInputMask("")
        self.text_valor_total.setText(QCoreApplication.translate("LancAbastecimento", u"0", None))
        self.label_3.setText(QCoreApplication.translate("LancAbastecimento", u"Observa\u00e7\u00e3o :", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tabWidget_3Page1), QCoreApplication.translate("LancAbastecimento", u"Principal", None))
        self.label_2.setText(QCoreApplication.translate("LancAbastecimento", u"Quantidade de cadastros:", None))
        self.lbl_total.setText(QCoreApplication.translate("LancAbastecimento", u"0", None))
#if QT_CONFIG(tooltip)
        self.bnt_back_full.setToolTip(QCoreApplication.translate("LancAbastecimento", u"<html><head/><body><p>Ir para o primeiro...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_back_full.setText(QCoreApplication.translate("LancAbastecimento", u"<<", None))
#if QT_CONFIG(tooltip)
        self.bnt_back.setToolTip(QCoreApplication.translate("LancAbastecimento", u"<html><head/><body><p>Voltar...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_back.setText(QCoreApplication.translate("LancAbastecimento", u"<", None))
#if QT_CONFIG(tooltip)
        self.bnt_next.setToolTip(QCoreApplication.translate("LancAbastecimento", u"<html><head/><body><p>Pr\u00f3ximo...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_next.setText(QCoreApplication.translate("LancAbastecimento", u">", None))
#if QT_CONFIG(tooltip)
        self.bnt_next_full.setToolTip(QCoreApplication.translate("LancAbastecimento", u"<html><head/><body><p><span style=\" font-weight:600;\">Ir para o fim.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_next_full.setText(QCoreApplication.translate("LancAbastecimento", u">>", None))
        self.bnt_alterar.setText(QCoreApplication.translate("LancAbastecimento", u"&Alterar", None))
        self.bnt_adicionar.setText(QCoreApplication.translate("LancAbastecimento", u"&Incluir", None))
#if QT_CONFIG(shortcut)
        self.bnt_adicionar.setShortcut(QCoreApplication.translate("LancAbastecimento", u"Alt+I", None))
#endif // QT_CONFIG(shortcut)
        self.bnt_salvar.setText(QCoreApplication.translate("LancAbastecimento", u"&Salvar", None))
#if QT_CONFIG(shortcut)
        self.bnt_salvar.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.bnt_search.setText(QCoreApplication.translate("LancAbastecimento", u"&Pesquisar", None))
#if QT_CONFIG(shortcut)
        self.bnt_search.setShortcut(QCoreApplication.translate("LancAbastecimento", u"Alt+P", None))
#endif // QT_CONFIG(shortcut)
        self.bnt_excluir.setText(QCoreApplication.translate("LancAbastecimento", u"&Excluir", None))
#if QT_CONFIG(shortcut)
        self.bnt_excluir.setShortcut(QCoreApplication.translate("LancAbastecimento", u"Alt+E", None))
#endif // QT_CONFIG(shortcut)
        self.bnt_cancelar.setText(QCoreApplication.translate("LancAbastecimento", u"&Cancelar", None))
#if QT_CONFIG(shortcut)
        self.bnt_cancelar.setShortcut(QCoreApplication.translate("LancAbastecimento", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

