# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QFrame, QHBoxLayout, QHeaderView, QLCDNumber,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTabWidget,
    QTableView, QTimeEdit, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(928, 688)
        MainWindow.setMinimumSize(QSize(928, 688))
        icon = QIcon()
        icon.addFile(u":/icons/ico.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionAplicativos = QAction(MainWindow)
        self.actionAplicativos.setObjectName(u"actionAplicativos")
        self.actionAbastecimento = QAction(MainWindow)
        self.actionAbastecimento.setObjectName(u"actionAbastecimento")
        icon1 = QIcon()
        icon1.addFile(u":/icons/abastecer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAbastecimento.setIcon(icon1)
        self.actionViagens = QAction(MainWindow)
        self.actionViagens.setObjectName(u"actionViagens")
        self.actionRelAbastecimento = QAction(MainWindow)
        self.actionRelAbastecimento.setObjectName(u"actionRelAbastecimento")
        self.actionTema = QAction(MainWindow)
        self.actionTema.setObjectName(u"actionTema")
        self.actionManutencao = QAction(MainWindow)
        self.actionManutencao.setObjectName(u"actionManutencao")
        icon2 = QIcon()
        icon2.addFile(u":/icons/mechanic.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionManutencao.setIcon(icon2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_18 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, -1, 5, -1)
        self.frm_widget_info = QFrame(self.tab)
        self.frm_widget_info.setObjectName(u"frm_widget_info")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_widget_info.sizePolicy().hasHeightForWidth())
        self.frm_widget_info.setSizePolicy(sizePolicy)
        self.frm_widget_info.setMinimumSize(QSize(0, 200))
        self.frm_widget_info.setMaximumSize(QSize(16777215, 200))
        self.frm_widget_info.setFrameShape(QFrame.StyledPanel)
        self.frm_widget_info.setFrameShadow(QFrame.Raised)
        self.lcd_id = QLCDNumber(self.frm_widget_info)
        self.lcd_id.setObjectName(u"lcd_id")
        self.lcd_id.setGeometry(QRect(10, 20, 64, 23))
        self.lcd_id.setMinimumSize(QSize(64, 23))
        self.lcd_id.setMaximumSize(QSize(64, 23))
        self.layoutWidget = QWidget(self.frm_widget_info)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(480, 70, 391, 111))
        self.verticalLayout_24 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.layoutWidget)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_24.addWidget(self.label_20)

        self.lanc_diario_plain_obs = QPlainTextEdit(self.layoutWidget)
        self.lanc_diario_plain_obs.setObjectName(u"lanc_diario_plain_obs")
        self.lanc_diario_plain_obs.setMinimumSize(QSize(389, 90))
        self.lanc_diario_plain_obs.setMaximumSize(QSize(389, 90))

        self.verticalLayout_24.addWidget(self.lanc_diario_plain_obs)

        self.layoutWidget1 = QWidget(self.frm_widget_info)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(480, 10, 391, 53))
        self.horizontalLayout_13 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 9)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_10 = QLabel(self.layoutWidget1)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_11.addWidget(self.label_10)

        self.lanc_diario_text_media_lt = QLineEdit(self.layoutWidget1)
        self.lanc_diario_text_media_lt.setObjectName(u"lanc_diario_text_media_lt")
        self.lanc_diario_text_media_lt.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_11.addWidget(self.lanc_diario_text_media_lt)


        self.horizontalLayout_13.addLayout(self.verticalLayout_11)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_11 = QLabel(self.layoutWidget1)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_13.addWidget(self.label_11)

        self.lanc_diario_spinbox_entregas = QSpinBox(self.layoutWidget1)
        self.lanc_diario_spinbox_entregas.setObjectName(u"lanc_diario_spinbox_entregas")
        self.lanc_diario_spinbox_entregas.setMaximumSize(QSize(62, 20))

        self.verticalLayout_13.addWidget(self.lanc_diario_spinbox_entregas)


        self.horizontalLayout_13.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_12 = QLabel(self.layoutWidget1)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_14.addWidget(self.label_12)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lb_cifrao = QLabel(self.layoutWidget1)
        self.lb_cifrao.setObjectName(u"lb_cifrao")

        self.horizontalLayout_8.addWidget(self.lb_cifrao)

        self.lanc_diario_text_total_recebido = QLineEdit(self.layoutWidget1)
        self.lanc_diario_text_total_recebido.setObjectName(u"lanc_diario_text_total_recebido")
        self.lanc_diario_text_total_recebido.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_8.addWidget(self.lanc_diario_text_total_recebido)


        self.verticalLayout_14.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_13.addLayout(self.verticalLayout_14)

        self.horizontalSpacer_4 = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)

        self.layoutWidget2 = QWidget(self.frm_widget_info)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(100, 70, 328, 129))
        self.verticalLayout_21 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 9)
        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.lanc_diario_time_hora_inicial = QTimeEdit(self.layoutWidget2)
        self.lanc_diario_time_hora_inicial.setObjectName(u"lanc_diario_time_hora_inicial")
        self.lanc_diario_time_hora_inicial.setMinimumSize(QSize(90, 20))
        self.lanc_diario_time_hora_inicial.setMaximumSize(QSize(90, 20))
        self.lanc_diario_time_hora_inicial.setWrapping(False)
        self.lanc_diario_time_hora_inicial.setCalendarPopup(True)

        self.verticalLayout_4.addWidget(self.lanc_diario_time_hora_inicial)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 9)
        self.label_6 = QLabel(self.layoutWidget2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.lanc_diario_text_km_inicial = QLineEdit(self.layoutWidget2)
        self.lanc_diario_text_km_inicial.setObjectName(u"lanc_diario_text_km_inicial")
        self.lanc_diario_text_km_inicial.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_3.addWidget(self.lanc_diario_text_km_inicial)


        self.verticalLayout_8.addLayout(self.verticalLayout_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 9)
        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_7.addWidget(self.label_5)

        self.lanc_diario_time_hora_final = QTimeEdit(self.layoutWidget2)
        self.lanc_diario_time_hora_final.setObjectName(u"lanc_diario_time_hora_final")
        self.lanc_diario_time_hora_final.setMinimumSize(QSize(90, 20))
        self.lanc_diario_time_hora_final.setMaximumSize(QSize(90, 20))
        self.lanc_diario_time_hora_final.setCalendarPopup(True)

        self.verticalLayout_7.addWidget(self.lanc_diario_time_hora_final)


        self.verticalLayout_22.addLayout(self.verticalLayout_7)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, -1, 9)
        self.label_7 = QLabel(self.layoutWidget2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_9.addWidget(self.label_7)

        self.lanc_diario_text_km_final = QLineEdit(self.layoutWidget2)
        self.lanc_diario_text_km_final.setObjectName(u"lanc_diario_text_km_final")
        self.lanc_diario_text_km_final.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_9.addWidget(self.lanc_diario_text_km_final)


        self.verticalLayout_22.addLayout(self.verticalLayout_9)


        self.horizontalLayout_5.addLayout(self.verticalLayout_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, -1, -1, 9)
        self.label_8 = QLabel(self.layoutWidget2)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_10.addWidget(self.label_8)

        self.lanc_diario_text_qt_horas = QLineEdit(self.layoutWidget2)
        self.lanc_diario_text_qt_horas.setObjectName(u"lanc_diario_text_qt_horas")
        self.lanc_diario_text_qt_horas.setMaximumSize(QSize(100, 16777215))
        self.lanc_diario_text_qt_horas.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.lanc_diario_text_qt_horas)


        self.verticalLayout_23.addLayout(self.verticalLayout_10)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, -1, -1, 9)
        self.label_9 = QLabel(self.layoutWidget2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_12.addWidget(self.label_9)

        self.lanc_diario_text_km_total = QLineEdit(self.layoutWidget2)
        self.lanc_diario_text_km_total.setObjectName(u"lanc_diario_text_km_total")
        self.lanc_diario_text_km_total.setMaximumSize(QSize(100, 16777215))

        self.verticalLayout_12.addWidget(self.lanc_diario_text_km_total)


        self.verticalLayout_23.addLayout(self.verticalLayout_12)


        self.horizontalLayout_5.addLayout(self.verticalLayout_23)


        self.verticalLayout_21.addLayout(self.horizontalLayout_5)

        self.lbl_error_diario = QLabel(self.layoutWidget2)
        self.lbl_error_diario.setObjectName(u"lbl_error_diario")
        self.lbl_error_diario.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_21.addWidget(self.lbl_error_diario)

        self.label = QLabel(self.frm_widget_info)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(102, 22, 181, 16))
        self.lanc_diario_combobox_app = QComboBox(self.frm_widget_info)
        self.lanc_diario_combobox_app.setObjectName(u"lanc_diario_combobox_app")
        self.lanc_diario_combobox_app.setGeometry(QRect(102, 41, 201, 20))
        self.lanc_diario_combobox_app.setMinimumSize(QSize(200, 20))
        self.label_3 = QLabel(self.frm_widget_info)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 20, 121, 16))
        self.lanc_diario_date_dia_lanc = QDateEdit(self.frm_widget_info)
        self.lanc_diario_date_dia_lanc.setObjectName(u"lanc_diario_date_dia_lanc")
        self.lanc_diario_date_dia_lanc.setGeometry(QRect(320, 40, 91, 20))
        self.lanc_diario_date_dia_lanc.setMaximumSize(QSize(109, 20))
        self.lanc_diario_date_dia_lanc.setCalendarPopup(True)

        self.verticalLayout_2.addWidget(self.frm_widget_info)

        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 45))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_2.addWidget(self.label_14)

        self.combobox_set_totalizado = QComboBox(self.frame_2)
        self.combobox_set_totalizado.addItem("")
        self.combobox_set_totalizado.addItem("")
        self.combobox_set_totalizado.addItem("")
        self.combobox_set_totalizado.addItem("")
        self.combobox_set_totalizado.setObjectName(u"combobox_set_totalizado")
        self.combobox_set_totalizado.setMinimumSize(QSize(131, 20))
        self.combobox_set_totalizado.setMaximumSize(QSize(131, 20))

        self.horizontalLayout_2.addWidget(self.combobox_set_totalizado)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_5 = QSpacerItem(652, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.lanc_diario_tableView = QTableView(self.tab)
        self.lanc_diario_tableView.setObjectName(u"lanc_diario_tableView")
        self.lanc_diario_tableView.setFrameShape(QFrame.Box)
        self.lanc_diario_tableView.setFrameShadow(QFrame.Raised)
        self.lanc_diario_tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lanc_diario_tableView.setProperty(u"showDropIndicator", False)
        self.lanc_diario_tableView.setAlternatingRowColors(True)
        self.lanc_diario_tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.lanc_diario_tableView.setSortingEnabled(True)
        self.lanc_diario_tableView.verticalHeader().setProperty(u"showSortIndicator", True)
        self.lanc_diario_tableView.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_2.addWidget(self.lanc_diario_tableView)

        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.frame_3.setFont(font)
        self.frame_3.setFocusPolicy(Qt.TabFocus)
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_36 = QLabel(self.frame_3)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_16.addWidget(self.label_36)

        self.lbl_total_viagens = QLabel(self.frame_3)
        self.lbl_total_viagens.setObjectName(u"lbl_total_viagens")

        self.horizontalLayout_16.addWidget(self.lbl_total_viagens)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_28 = QLabel(self.frame_3)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_10.addWidget(self.label_28)

        self.lbl_media_consumo = QLabel(self.frame_3)
        self.lbl_media_consumo.setObjectName(u"lbl_media_consumo")

        self.horizontalLayout_10.addWidget(self.lbl_media_consumo)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_32 = QLabel(self.frame_3)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_14.addWidget(self.label_32)

        self.lbl_total_recebido = QLabel(self.frame_3)
        self.lbl_total_recebido.setObjectName(u"lbl_total_recebido")

        self.horizontalLayout_14.addWidget(self.lbl_total_recebido)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_14)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_38 = QLabel(self.frame_3)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_17.addWidget(self.label_38)

        self.lbl_media_viagens = QLabel(self.frame_3)
        self.lbl_media_viagens.setObjectName(u"lbl_media_viagens")

        self.horizontalLayout_17.addWidget(self.lbl_media_viagens)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_30 = QLabel(self.frame_3)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_11.addWidget(self.label_30)

        self.lbl_media_horas = QLabel(self.frame_3)
        self.lbl_media_horas.setObjectName(u"lbl_media_horas")

        self.horizontalLayout_11.addWidget(self.lbl_media_horas)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_34 = QLabel(self.frame_3)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_15.addWidget(self.label_34)

        self.lbl_media_vlr_recebido = QLabel(self.frame_3)
        self.lbl_media_vlr_recebido.setObjectName(u"lbl_media_vlr_recebido")

        self.horizontalLayout_15.addWidget(self.lbl_media_vlr_recebido)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_15)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_17 = QVBoxLayout(self.tab_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(5, 0, 5, 0)
        self.frm_widger_entrega = QFrame(self.tab_2)
        self.frm_widger_entrega.setObjectName(u"frm_widger_entrega")
        self.frm_widger_entrega.setMinimumSize(QSize(0, 200))
        self.frm_widger_entrega.setFrameShape(QFrame.StyledPanel)
        self.frm_widger_entrega.setFrameShadow(QFrame.Raised)
        self.lcdNumber = QLCDNumber(self.frm_widger_entrega)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(10, 10, 64, 23))
        self.layoutWidget3 = QWidget(self.frm_widger_entrega)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(450, 10, 310, 123))
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_23 = QLabel(self.layoutWidget3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(16777215, 28))

        self.verticalLayout_25.addWidget(self.label_23)

        self.lanc_entrega_plain_obs = QPlainTextEdit(self.layoutWidget3)
        self.lanc_entrega_plain_obs.setObjectName(u"lanc_entrega_plain_obs")
        self.lanc_entrega_plain_obs.setMaximumSize(QSize(256, 100))

        self.verticalLayout_25.addWidget(self.lanc_entrega_plain_obs)


        self.horizontalLayout_12.addLayout(self.verticalLayout_25)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.lanc_entrega_bnt_add = QPushButton(self.layoutWidget3)
        self.lanc_entrega_bnt_add.setObjectName(u"lanc_entrega_bnt_add")
        icon3 = QIcon()
        icon3.addFile(u":/icons/adicionar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.lanc_entrega_bnt_add.setIcon(icon3)
        self.lanc_entrega_bnt_add.setIconSize(QSize(30, 30))
        self.lanc_entrega_bnt_add.setFlat(True)

        self.verticalLayout_31.addWidget(self.lanc_entrega_bnt_add)

        self.lanc_entrega_bnt_delete = QPushButton(self.layoutWidget3)
        self.lanc_entrega_bnt_delete.setObjectName(u"lanc_entrega_bnt_delete")
        icon4 = QIcon()
        icon4.addFile(u":/icons/excluir.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.lanc_entrega_bnt_delete.setIcon(icon4)
        self.lanc_entrega_bnt_delete.setIconSize(QSize(30, 30))
        self.lanc_entrega_bnt_delete.setFlat(True)

        self.verticalLayout_31.addWidget(self.lanc_entrega_bnt_delete)


        self.horizontalLayout_12.addLayout(self.verticalLayout_31)

        self.lanc_entrega_combobox_tp_pagamento = QComboBox(self.frm_widger_entrega)
        self.lanc_entrega_combobox_tp_pagamento.addItem("")
        self.lanc_entrega_combobox_tp_pagamento.addItem("")
        self.lanc_entrega_combobox_tp_pagamento.addItem("")
        self.lanc_entrega_combobox_tp_pagamento.addItem("")
        self.lanc_entrega_combobox_tp_pagamento.addItem("")
        self.lanc_entrega_combobox_tp_pagamento.addItem("")
        self.lanc_entrega_combobox_tp_pagamento.addItem("")
        self.lanc_entrega_combobox_tp_pagamento.setObjectName(u"lanc_entrega_combobox_tp_pagamento")
        self.lanc_entrega_combobox_tp_pagamento.setGeometry(QRect(202, 140, 200, 20))
        self.lanc_entrega_combobox_tp_pagamento.setMinimumSize(QSize(200, 20))
        self.label_13 = QLabel(self.frm_widger_entrega)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(202, 120, 191, 16))
        self.lanc_entrega_time_hora_inicial_2 = QTimeEdit(self.frm_widger_entrega)
        self.lanc_entrega_time_hora_inicial_2.setObjectName(u"lanc_entrega_time_hora_inicial_2")
        self.lanc_entrega_time_hora_inicial_2.setGeometry(QRect(93, 31, 90, 20))
        self.lanc_entrega_time_hora_inicial_2.setMinimumSize(QSize(90, 20))
        self.lanc_entrega_time_hora_inicial_2.setMaximumSize(QSize(90, 20))
        self.label_15 = QLabel(self.frm_widger_entrega)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(93, 12, 60, 16))
        self.lanc_entrega_time_hora_final_2 = QTimeEdit(self.frm_widger_entrega)
        self.lanc_entrega_time_hora_final_2.setObjectName(u"lanc_entrega_time_hora_final_2")
        self.lanc_entrega_time_hora_final_2.setGeometry(QRect(195, 32, 90, 20))
        self.lanc_entrega_time_hora_final_2.setMinimumSize(QSize(90, 20))
        self.lanc_entrega_time_hora_final_2.setMaximumSize(QSize(90, 20))
        self.label_16 = QLabel(self.frm_widger_entrega)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(195, 13, 55, 16))
        self.label_17 = QLabel(self.frm_widger_entrega)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(293, 13, 52, 16))
        self.lanc_entrega_text_qt_horas_2 = QLineEdit(self.frm_widger_entrega)
        self.lanc_entrega_text_qt_horas_2.setObjectName(u"lanc_entrega_text_qt_horas_2")
        self.lanc_entrega_text_qt_horas_2.setGeometry(QRect(293, 32, 100, 20))
        self.lanc_entrega_text_qt_horas_2.setMaximumSize(QSize(100, 16777215))
        self.lanc_entrega_text_qt_horas_2.setReadOnly(True)
        self.lanc_entrega_text_km_total_3 = QLineEdit(self.frm_widger_entrega)
        self.lanc_entrega_text_km_total_3.setObjectName(u"lanc_entrega_text_km_total_3")
        self.lanc_entrega_text_km_total_3.setGeometry(QRect(313, 87, 100, 20))
        self.lanc_entrega_text_km_total_3.setMaximumSize(QSize(100, 16777215))
        self.label_21 = QLabel(self.frm_widger_entrega)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(313, 68, 101, 16))
        self.label_19 = QLabel(self.frm_widger_entrega)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(205, 68, 101, 16))
        self.lanc_entrega_text_km_final_2 = QLineEdit(self.frm_widger_entrega)
        self.lanc_entrega_text_km_final_2.setObjectName(u"lanc_entrega_text_km_final_2")
        self.lanc_entrega_text_km_final_2.setGeometry(QRect(205, 87, 100, 20))
        self.lanc_entrega_text_km_final_2.setMaximumSize(QSize(100, 16777215))
        self.lbl_error_entregas = QLabel(self.frm_widger_entrega)
        self.lbl_error_entregas.setObjectName(u"lbl_error_entregas")
        self.lbl_error_entregas.setGeometry(QRect(80, 170, 312, 16))
        self.lbl_error_entregas.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.lbl_error_entregas.setWordWrap(True)
        self.label_22 = QLabel(self.frm_widger_entrega)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(90, 121, 78, 16))
        self.lanc_entrega_text_total_recebido = QLineEdit(self.frm_widger_entrega)
        self.lanc_entrega_text_total_recebido.setObjectName(u"lanc_entrega_text_total_recebido")
        self.lanc_entrega_text_total_recebido.setGeometry(QRect(90, 140, 100, 20))
        self.lanc_entrega_text_total_recebido.setMaximumSize(QSize(100, 20))
        self.lanc_entrega_text_km_inicial_3 = QLineEdit(self.frm_widger_entrega)
        self.lanc_entrega_text_km_inicial_3.setObjectName(u"lanc_entrega_text_km_inicial_3")
        self.lanc_entrega_text_km_inicial_3.setGeometry(QRect(93, 86, 100, 20))
        self.lanc_entrega_text_km_inicial_3.setMaximumSize(QSize(100, 16777215))
        self.label_18 = QLabel(self.frm_widger_entrega)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(93, 67, 91, 16))

        self.verticalLayout_17.addWidget(self.frm_widger_entrega)

        self.tableView_2 = QTableView(self.tab_2)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setFrameShape(QFrame.StyledPanel)
        self.tableView_2.setFrameShadow(QFrame.Sunken)
        self.tableView_2.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_17.addWidget(self.tableView_2)

        self.frame_4 = QFrame(self.tab_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setFont(font)
        self.frame_4.setFocusPolicy(Qt.TabFocus)
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame_4)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 891, 20))
        self.horizontalLayout_22 = QHBoxLayout(self.widget)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_37 = QLabel(self.widget)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_19.addWidget(self.label_37)

        self.lbl_total_viagens_detalhamento = QLabel(self.widget)
        self.lbl_total_viagens_detalhamento.setObjectName(u"lbl_total_viagens_detalhamento")

        self.horizontalLayout_19.addWidget(self.lbl_total_viagens_detalhamento)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_35 = QLabel(self.widget)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_21.addWidget(self.label_35)

        self.lbl_media_vlr_recebido_detalhamento = QLabel(self.widget)
        self.lbl_media_vlr_recebido_detalhamento.setObjectName(u"lbl_media_vlr_recebido_detalhamento")

        self.horizontalLayout_21.addWidget(self.lbl_media_vlr_recebido_detalhamento)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_33 = QLabel(self.widget)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_20.addWidget(self.label_33)

        self.lbl_total_recebido_detalhamento = QLabel(self.widget)
        self.lbl_total_recebido_detalhamento.setObjectName(u"lbl_total_recebido_detalhamento")

        self.horizontalLayout_20.addWidget(self.lbl_total_recebido_detalhamento)


        self.horizontalLayout_22.addLayout(self.horizontalLayout_20)


        self.verticalLayout_17.addWidget(self.frame_4)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_18.addWidget(self.tabWidget)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(1600000, 94))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, -1, -1, 10)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.lbl_total = QLabel(self.frame)
        self.lbl_total.setObjectName(u"lbl_total")

        self.horizontalLayout_4.addWidget(self.lbl_total)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(178, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bnt_back_full = QPushButton(self.frame)
        self.bnt_back_full.setObjectName(u"bnt_back_full")
        self.bnt_back_full.setMinimumSize(QSize(75, 23))
        self.bnt_back_full.setMaximumSize(QSize(75, 23))

        self.horizontalLayout_3.addWidget(self.bnt_back_full)

        self.bnt_back = QPushButton(self.frame)
        self.bnt_back.setObjectName(u"bnt_back")
        self.bnt_back.setMinimumSize(QSize(75, 23))
        self.bnt_back.setMaximumSize(QSize(75, 23))

        self.horizontalLayout_3.addWidget(self.bnt_back)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.bnt_next = QPushButton(self.frame)
        self.bnt_next.setObjectName(u"bnt_next")
        self.bnt_next.setMinimumSize(QSize(75, 23))
        self.bnt_next.setMaximumSize(QSize(75, 23))

        self.horizontalLayout_3.addWidget(self.bnt_next)

        self.bnt_next_full = QPushButton(self.frame)
        self.bnt_next_full.setObjectName(u"bnt_next_full")
        self.bnt_next_full.setMinimumSize(QSize(75, 23))
        self.bnt_next_full.setMaximumSize(QSize(75, 23))

        self.horizontalLayout_3.addWidget(self.bnt_next_full)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.bnt_alterar = QPushButton(self.frame)
        self.bnt_alterar.setObjectName(u"bnt_alterar")
        self.bnt_alterar.setMinimumSize(QSize(100, 30))
        self.bnt_alterar.setMaximumSize(QSize(131, 41))
        icon5 = QIcon()
        icon5.addFile(u":/icons/pencil.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_alterar.setIcon(icon5)
        self.bnt_alterar.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.bnt_alterar)

        self.horizontalSpacer = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.bnt_adicionar = QPushButton(self.frame)
        self.bnt_adicionar.setObjectName(u"bnt_adicionar")
        self.bnt_adicionar.setEnabled(True)
        self.bnt_adicionar.setMinimumSize(QSize(100, 30))
        self.bnt_adicionar.setMaximumSize(QSize(131, 41))
        self.bnt_adicionar.setIcon(icon3)
        self.bnt_adicionar.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.bnt_adicionar)

        self.bnt_salvar = QPushButton(self.frame)
        self.bnt_salvar.setObjectName(u"bnt_salvar")
        self.bnt_salvar.setEnabled(False)
        self.bnt_salvar.setMinimumSize(QSize(100, 0))
        self.bnt_salvar.setMaximumSize(QSize(100, 36))
        icon6 = QIcon()
        icon6.addFile(u":/icons/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_salvar.setIcon(icon6)
        self.bnt_salvar.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.bnt_salvar)

        self.bnt_excluir = QPushButton(self.frame)
        self.bnt_excluir.setObjectName(u"bnt_excluir")
        self.bnt_excluir.setMinimumSize(QSize(100, 30))
        self.bnt_excluir.setMaximumSize(QSize(131, 41))
        self.bnt_excluir.setIcon(icon4)
        self.bnt_excluir.setIconSize(QSize(25, 25))
        self.bnt_excluir.setCheckable(False)
        self.bnt_excluir.setChecked(False)
        self.bnt_excluir.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.bnt_excluir)

        self.bnt_cancelar = QPushButton(self.frame)
        self.bnt_cancelar.setObjectName(u"bnt_cancelar")
        self.bnt_cancelar.setMinimumSize(QSize(100, 30))
        self.bnt_cancelar.setMaximumSize(QSize(131, 41))
        icon7 = QIcon()
        icon7.addFile(u":/icons/error.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_cancelar.setIcon(icon7)
        self.bnt_cancelar.setIconSize(QSize(25, 25))
        self.bnt_cancelar.setCheckable(False)
        self.bnt_cancelar.setChecked(False)
        self.bnt_cancelar.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.bnt_cancelar)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_18.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 928, 21))
        self.menuCadastro = QMenu(self.menubar)
        self.menuCadastro.setObjectName(u"menuCadastro")
        self.menuRelat_rios = QMenu(self.menubar)
        self.menuRelat_rios.setObjectName(u"menuRelat_rios")
        self.menuLan_amento = QMenu(self.menubar)
        self.menuLan_amento.setObjectName(u"menuLan_amento")
        self.menuSistema = QMenu(self.menubar)
        self.menuSistema.setObjectName(u"menuSistema")
        MainWindow.setMenuBar(self.menubar)
#if QT_CONFIG(shortcut)
        self.label_20.setBuddy(self.lanc_diario_plain_obs)
        self.label_10.setBuddy(self.lanc_diario_text_media_lt)
        self.label_11.setBuddy(self.lanc_diario_spinbox_entregas)
        self.label_12.setBuddy(self.lanc_diario_text_total_recebido)
        self.label_4.setBuddy(self.lanc_diario_time_hora_inicial)
        self.label_6.setBuddy(self.lanc_diario_text_km_inicial)
        self.label_5.setBuddy(self.lanc_diario_time_hora_final)
        self.label_7.setBuddy(self.lanc_diario_text_km_final)
        self.label_8.setBuddy(self.lanc_diario_text_qt_horas)
        self.label_9.setBuddy(self.lanc_diario_text_km_total)
        self.label.setBuddy(self.lanc_diario_combobox_app)
        self.label_3.setBuddy(self.lanc_diario_date_dia_lanc)
        self.label_23.setBuddy(self.lanc_entrega_plain_obs)
        self.label_13.setBuddy(self.lanc_entrega_combobox_tp_pagamento)
        self.label_15.setBuddy(self.lanc_entrega_time_hora_inicial_2)
        self.label_16.setBuddy(self.lanc_entrega_time_hora_final_2)
        self.label_17.setBuddy(self.lanc_entrega_text_qt_horas_2)
        self.label_21.setBuddy(self.lanc_entrega_text_km_total_3)
        self.label_19.setBuddy(self.lanc_entrega_text_km_final_2)
        self.label_22.setBuddy(self.lanc_entrega_text_total_recebido)
        self.label_18.setBuddy(self.lanc_entrega_text_km_inicial_3)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lanc_diario_combobox_app, self.lanc_diario_date_dia_lanc)
        QWidget.setTabOrder(self.lanc_diario_date_dia_lanc, self.lanc_diario_time_hora_inicial)
        QWidget.setTabOrder(self.lanc_diario_time_hora_inicial, self.lanc_diario_time_hora_final)
        QWidget.setTabOrder(self.lanc_diario_time_hora_final, self.lanc_diario_text_km_inicial)
        QWidget.setTabOrder(self.lanc_diario_text_km_inicial, self.lanc_diario_text_km_final)
        QWidget.setTabOrder(self.lanc_diario_text_km_final, self.lanc_diario_text_km_total)
        QWidget.setTabOrder(self.lanc_diario_text_km_total, self.lanc_diario_text_media_lt)
        QWidget.setTabOrder(self.lanc_diario_text_media_lt, self.lanc_diario_spinbox_entregas)
        QWidget.setTabOrder(self.lanc_diario_spinbox_entregas, self.lanc_diario_text_total_recebido)
        QWidget.setTabOrder(self.lanc_diario_text_total_recebido, self.lanc_diario_plain_obs)
        QWidget.setTabOrder(self.lanc_diario_plain_obs, self.bnt_salvar)
        QWidget.setTabOrder(self.bnt_salvar, self.bnt_adicionar)
        QWidget.setTabOrder(self.bnt_adicionar, self.bnt_alterar)
        QWidget.setTabOrder(self.bnt_alterar, self.bnt_cancelar)
        QWidget.setTabOrder(self.bnt_cancelar, self.bnt_next_full)
        QWidget.setTabOrder(self.bnt_next_full, self.bnt_next)
        QWidget.setTabOrder(self.bnt_next, self.bnt_back)
        QWidget.setTabOrder(self.bnt_back, self.bnt_back_full)
        QWidget.setTabOrder(self.bnt_back_full, self.bnt_excluir)
        QWidget.setTabOrder(self.bnt_excluir, self.lanc_diario_tableView)
        QWidget.setTabOrder(self.lanc_diario_tableView, self.lanc_entrega_time_hora_inicial_2)
        QWidget.setTabOrder(self.lanc_entrega_time_hora_inicial_2, self.lanc_entrega_time_hora_final_2)
        QWidget.setTabOrder(self.lanc_entrega_time_hora_final_2, self.lanc_entrega_text_km_inicial_3)
        QWidget.setTabOrder(self.lanc_entrega_text_km_inicial_3, self.lanc_entrega_text_km_final_2)
        QWidget.setTabOrder(self.lanc_entrega_text_km_final_2, self.lanc_entrega_text_km_total_3)
        QWidget.setTabOrder(self.lanc_entrega_text_km_total_3, self.lanc_entrega_text_total_recebido)
        QWidget.setTabOrder(self.lanc_entrega_text_total_recebido, self.lanc_entrega_plain_obs)
        QWidget.setTabOrder(self.lanc_entrega_plain_obs, self.lanc_entrega_bnt_add)
        QWidget.setTabOrder(self.lanc_entrega_bnt_add, self.lanc_entrega_bnt_delete)
        QWidget.setTabOrder(self.lanc_entrega_bnt_delete, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.lanc_diario_text_qt_horas)
        QWidget.setTabOrder(self.lanc_diario_text_qt_horas, self.lanc_entrega_text_qt_horas_2)
        QWidget.setTabOrder(self.lanc_entrega_text_qt_horas_2, self.tableView_2)

        self.menubar.addAction(self.menuSistema.menuAction())
        self.menubar.addAction(self.menuCadastro.menuAction())
        self.menubar.addAction(self.menuLan_amento.menuAction())
        self.menubar.addAction(self.menuRelat_rios.menuAction())
        self.menuCadastro.addAction(self.actionAplicativos)
        self.menuRelat_rios.addAction(self.actionViagens)
        self.menuRelat_rios.addSeparator()
        self.menuRelat_rios.addAction(self.actionRelAbastecimento)
        self.menuLan_amento.addAction(self.actionAbastecimento)
        self.menuLan_amento.addAction(self.actionManutencao)
        self.menuSistema.addAction(self.actionTema)

        self.retranslateUi(MainWindow)
        self.lanc_diario_text_media_lt.returnPressed.connect(self.lanc_diario_spinbox_entregas.setFocus)
        self.lanc_diario_text_qt_horas.returnPressed.connect(self.lanc_diario_text_km_inicial.setFocus)
        self.lanc_diario_text_km_inicial.returnPressed.connect(self.lanc_diario_text_km_final.setFocus)
        self.lanc_diario_text_km_final.returnPressed.connect(self.lanc_diario_text_km_total.setFocus)
        self.lanc_diario_text_km_total.returnPressed.connect(self.lanc_diario_text_media_lt.setFocus)
        self.lanc_diario_text_total_recebido.returnPressed.connect(self.bnt_salvar.click)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Controle de Entregas", None))
        self.actionAplicativos.setText(QCoreApplication.translate("MainWindow", u"Aplicativos", None))
        self.actionAbastecimento.setText(QCoreApplication.translate("MainWindow", u"Abastecimento", None))
#if QT_CONFIG(shortcut)
        self.actionAbastecimento.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionViagens.setText(QCoreApplication.translate("MainWindow", u"Viagens", None))
        self.actionRelAbastecimento.setText(QCoreApplication.translate("MainWindow", u"Abastecimento", None))
        self.actionTema.setText(QCoreApplication.translate("MainWindow", u"Tema", None))
        self.actionManutencao.setText(QCoreApplication.translate("MainWindow", u"Manuten\u00e7\u00e3o", None))
#if QT_CONFIG(shortcut)
        self.actionManutencao.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+M", None))
#endif // QT_CONFIG(shortcut)
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Media de Lt :", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Qt viagens:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"         Total Recebido :", None))
        self.lb_cifrao.setText(QCoreApplication.translate("MainWindow", u"R$ :", None))
        self.lanc_diario_text_total_recebido.setInputMask("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Hora Inicial :", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Km Inicial :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Hora Final :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Km Final :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"QT Horas :", None))
#if QT_CONFIG(tooltip)
        self.lanc_diario_text_qt_horas.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>O Calculo da Quantidade de horas \u00e9 feito autom\u00e1ticamente.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Total :", None))
        self.lbl_error_diario.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"App Utilizado :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Data do Lan\u00e7amento : ", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Totalizar por : ", None))
        self.combobox_set_totalizado.setItemText(0, QCoreApplication.translate("MainWindow", u"Geral", None))
        self.combobox_set_totalizado.setItemText(1, QCoreApplication.translate("MainWindow", u"Di\u00e1rio", None))
        self.combobox_set_totalizado.setItemText(2, QCoreApplication.translate("MainWindow", u"Semanal", None))
        self.combobox_set_totalizado.setItemText(3, QCoreApplication.translate("MainWindow", u"Mensal", None))

        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Total de Viagens", None))
        self.lbl_total_viagens.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"M\u00e9dia de Consumo:", None))
        self.lbl_media_consumo.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Total Recebido :", None))
        self.lbl_total_recebido.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Media de Viagens", None))
        self.lbl_media_viagens.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"M\u00e9dia de Horas:", None))
        self.lbl_media_horas.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"M\u00e9dia de Valor recebido :", None))
        self.lbl_media_vlr_recebido.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Lan\u00e7amento Di\u00e1rio", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es", None))
#if QT_CONFIG(tooltip)
        self.lanc_entrega_bnt_add.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Adicionar Entrega</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lanc_entrega_bnt_add.setText("")
#if QT_CONFIG(tooltip)
        self.lanc_entrega_bnt_delete.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Excluir Entregas.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lanc_entrega_bnt_delete.setText("")
        self.lanc_entrega_combobox_tp_pagamento.setItemText(0, QCoreApplication.translate("MainWindow", u"Dinheiro", None))
        self.lanc_entrega_combobox_tp_pagamento.setItemText(1, QCoreApplication.translate("MainWindow", u"Cr\u00e9dito", None))
        self.lanc_entrega_combobox_tp_pagamento.setItemText(2, QCoreApplication.translate("MainWindow", u"D\u00e9bito", None))
        self.lanc_entrega_combobox_tp_pagamento.setItemText(3, QCoreApplication.translate("MainWindow", u"Pix", None))
        self.lanc_entrega_combobox_tp_pagamento.setItemText(4, QCoreApplication.translate("MainWindow", u"Aplicativo", None))
        self.lanc_entrega_combobox_tp_pagamento.setItemText(5, QCoreApplication.translate("MainWindow", u"Pendente de Pagamento", None))
        self.lanc_entrega_combobox_tp_pagamento.setItemText(6, QCoreApplication.translate("MainWindow", u"Outros", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Forma de Pagamento :", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Hora Inicial :", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Hora Final :", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"QT Horas :", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Total :", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Km Final :", None))
        self.lbl_error_entregas.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Total Recebido :", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Km Inicial :", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Total de Viagens", None))
        self.lbl_total_viagens_detalhamento.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"M\u00e9dia de Valor recebido :", None))
        self.lbl_media_vlr_recebido_detalhamento.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Total Recebido :", None))
        self.lbl_total_recebido_detalhamento.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Detalhamento de viagens", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Quantidade de cadastros:", None))
        self.lbl_total.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.bnt_back_full.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Ir para o primeiro...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_back_full.setText(QCoreApplication.translate("MainWindow", u"<<", None))
#if QT_CONFIG(tooltip)
        self.bnt_back.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Voltar...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_back.setText(QCoreApplication.translate("MainWindow", u"<", None))
#if QT_CONFIG(tooltip)
        self.bnt_next.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pr\u00f3ximo...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_next.setText(QCoreApplication.translate("MainWindow", u">", None))
#if QT_CONFIG(tooltip)
        self.bnt_next_full.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Ir para o fim.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_next_full.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.bnt_alterar.setText(QCoreApplication.translate("MainWindow", u"&Alterar", None))
#if QT_CONFIG(shortcut)
        self.bnt_alterar.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.bnt_adicionar.setText(QCoreApplication.translate("MainWindow", u"&Incluir", None))
#if QT_CONFIG(shortcut)
        self.bnt_adicionar.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+I", None))
#endif // QT_CONFIG(shortcut)
        self.bnt_salvar.setText(QCoreApplication.translate("MainWindow", u"&Salvar", None))
#if QT_CONFIG(shortcut)
        self.bnt_salvar.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.bnt_excluir.setText(QCoreApplication.translate("MainWindow", u"&Excluir", None))
#if QT_CONFIG(shortcut)
        self.bnt_excluir.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+E", None))
#endif // QT_CONFIG(shortcut)
        self.bnt_cancelar.setText(QCoreApplication.translate("MainWindow", u"&Cancelar", None))
#if QT_CONFIG(shortcut)
        self.bnt_cancelar.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
        self.menuCadastro.setTitle(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.menuRelat_rios.setTitle(QCoreApplication.translate("MainWindow", u"Relat\u00f3rios", None))
        self.menuLan_amento.setTitle(QCoreApplication.translate("MainWindow", u"Lan\u00e7amento", None))
        self.menuSistema.setTitle(QCoreApplication.translate("MainWindow", u"Sistema", None))
    # retranslateUi

