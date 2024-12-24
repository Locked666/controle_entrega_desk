# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LancManutecaoNew.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
    QFrame, QGroupBox, QHBoxLayout, QHeaderView,
    QLCDNumber, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QTabWidget, QTableView, QVBoxLayout, QWidget)
import icons_rc

class Ui_LancManutencao(object):
    def setupUi(self, LancManutencao):
        if not LancManutencao.objectName():
            LancManutencao.setObjectName(u"LancManutencao")
        LancManutencao.resize(780, 739)
        self.verticalLayout = QVBoxLayout(LancManutencao)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(LancManutencao)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 41))
        self.frame_3.setMaximumSize(QSize(16777215, 41))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.lcdNumber = QLCDNumber(self.frame_3)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(10, 10, 64, 23))

        self.verticalLayout.addWidget(self.frame_3)

        self.tabContent = QTabWidget(LancManutencao)
        self.tabContent.setObjectName(u"tabContent")
        self.tabContent.setTabPosition(QTabWidget.North)
        self.tabContent.setTabShape(QTabWidget.Rounded)
        self.tabContent.setElideMode(Qt.ElideNone)
        self.tabContent.setDocumentMode(True)
        self.tabContent.setTabsClosable(False)
        self.tabContent.setMovable(False)
        self.tabContent.setTabBarAutoHide(True)
        self.tab_principal = QWidget()
        self.tab_principal.setObjectName(u"tab_principal")
        self.verticalLayout_3 = QVBoxLayout(self.tab_principal)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.tab_principal)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.dateTimeEdit = QDateTimeEdit(self.groupBox)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setCalendarPopup(True)

        self.verticalLayout_4.addWidget(self.dateTimeEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_4.setIndent(5)
        self.label_4.setOpenExternalLinks(False)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.dateTimeEdit_2 = QDateTimeEdit(self.groupBox)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setCalendarPopup(True)

        self.verticalLayout_5.addWidget(self.dateTimeEdit_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_6.addWidget(self.label_8)

        self.combobox_tipo_combustivel = QComboBox(self.groupBox)
        self.combobox_tipo_combustivel.addItem("")
        self.combobox_tipo_combustivel.addItem("")
        self.combobox_tipo_combustivel.addItem("")
        self.combobox_tipo_combustivel.addItem("")
        self.combobox_tipo_combustivel.setObjectName(u"combobox_tipo_combustivel")
        self.combobox_tipo_combustivel.setMaximumSize(QSize(246, 20))

        self.verticalLayout_6.addWidget(self.combobox_tipo_combustivel)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)


        self.verticalLayout_31.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 9, -1, 9)
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_7.addWidget(self.label_5)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_7.addWidget(self.lineEdit)


        self.horizontalLayout_8.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 9, -1, 9)
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_8.addWidget(self.label_6)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_8.addWidget(self.lineEdit_2)


        self.horizontalLayout_8.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 9, -1, 9)
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_9.addWidget(self.label_7)

        self.lineEdit_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_9.addWidget(self.lineEdit_3)


        self.horizontalLayout_8.addLayout(self.verticalLayout_9)


        self.verticalLayout_13.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_10.addWidget(self.label_9)

        self.lineEdit_4 = QLineEdit(self.groupBox_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)

        self.verticalLayout_10.addWidget(self.lineEdit_4)


        self.horizontalLayout_9.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 9, -1, 9)
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_7.addWidget(self.label_11)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.label_10)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_7.addWidget(self.label_12)


        self.verticalLayout_11.addLayout(self.horizontalLayout_7)

        self.horizontalSlider = QSlider(self.groupBox_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy2)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QSlider.TicksAbove)
        self.horizontalSlider.setTickInterval(10)

        self.verticalLayout_11.addWidget(self.horizontalSlider)


        self.horizontalLayout_9.addLayout(self.verticalLayout_11)


        self.verticalLayout_13.addLayout(self.horizontalLayout_9)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 5, -1, 5)
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_12.addWidget(self.label_13)

        self.lineEdit_5 = QLineEdit(self.groupBox_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_12.addWidget(self.lineEdit_5)


        self.verticalLayout_13.addLayout(self.verticalLayout_12)


        self.verticalLayout_31.addWidget(self.groupBox_2)


        self.verticalLayout_33.addLayout(self.verticalLayout_31)

        self.verticalSpacer = QSpacerItem(20, 128, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer)


        self.horizontalLayout_14.addLayout(self.verticalLayout_33)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setSpacing(10)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(-1, 0, -1, 9)
        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        font = QFont()
        font.setBold(False)
        self.groupBox_3.setFont(font)
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 9)
        self.tabWidget = QTabWidget(self.groupBox_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tabWidget.setDocumentMode(True)
        self.tabWidgetPage1 = QWidget()
        self.tabWidgetPage1.setObjectName(u"tabWidgetPage1")
        self.verticalLayout_32 = QVBoxLayout(self.tabWidgetPage1)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 9, -1, 9)
        self.label_14 = QLabel(self.tabWidgetPage1)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_15.addWidget(self.label_14)

        self.lineEdit_6 = QLineEdit(self.tabWidgetPage1)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_15.addWidget(self.lineEdit_6)


        self.verticalLayout_18.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 5, -1, 5)
        self.label_15 = QLabel(self.tabWidgetPage1)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_16.addWidget(self.label_15)

        self.lineEdit_7 = QLineEdit(self.tabWidgetPage1)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.verticalLayout_16.addWidget(self.lineEdit_7)


        self.verticalLayout_18.addLayout(self.verticalLayout_16)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, 5, -1, 5)
        self.label_16 = QLabel(self.tabWidgetPage1)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_17.addWidget(self.label_16)

        self.lineEdit_8 = QLineEdit(self.tabWidgetPage1)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.verticalLayout_17.addWidget(self.lineEdit_8)


        self.horizontalLayout_10.addLayout(self.verticalLayout_17)

        self.checkBox = QCheckBox(self.tabWidgetPage1)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setTristate(False)

        self.horizontalLayout_10.addWidget(self.checkBox)


        self.verticalLayout_18.addLayout(self.horizontalLayout_10)


        self.verticalLayout_32.addLayout(self.verticalLayout_18)

        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QWidget()
        self.tabWidgetPage2.setObjectName(u"tabWidgetPage2")
        self.tabWidget.addTab(self.tabWidgetPage2, "")

        self.verticalLayout_14.addWidget(self.tabWidget)


        self.verticalLayout_30.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.frame)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_29 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, 9, -1, 9)
        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_21.addWidget(self.label_17)

        self.lineEdit_9 = QLineEdit(self.groupBox_4)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMaximumSize(QSize(149, 20))

        self.verticalLayout_21.addWidget(self.lineEdit_9)


        self.horizontalLayout_11.addLayout(self.verticalLayout_21)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, 9, -1, 9)
        self.label_18 = QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_20.addWidget(self.label_18)

        self.comboBox = QComboBox(self.groupBox_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(179, 20))

        self.verticalLayout_20.addWidget(self.comboBox)


        self.horizontalLayout_11.addLayout(self.verticalLayout_20)


        self.verticalLayout_29.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, 9, -1, 9)
        self.label_19 = QLabel(self.groupBox_4)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_22.addWidget(self.label_19)

        self.lineEdit_10 = QLineEdit(self.groupBox_4)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.verticalLayout_22.addWidget(self.lineEdit_10)


        self.horizontalLayout_12.addLayout(self.verticalLayout_22)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(-1, 9, -1, 9)
        self.label_20 = QLabel(self.groupBox_4)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_23.addWidget(self.label_20)

        self.lineEdit_11 = QLineEdit(self.groupBox_4)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.verticalLayout_23.addWidget(self.lineEdit_11)


        self.horizontalLayout_12.addLayout(self.verticalLayout_23)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(-1, 9, -1, 9)
        self.label_21 = QLabel(self.groupBox_4)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_24.addWidget(self.label_21)

        self.lineEdit_12 = QLineEdit(self.groupBox_4)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.verticalLayout_24.addWidget(self.lineEdit_12)


        self.horizontalLayout_12.addLayout(self.verticalLayout_24)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(-1, 9, -1, 9)
        self.label_22 = QLabel(self.groupBox_4)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_25.addWidget(self.label_22)

        self.lineEdit_13 = QLineEdit(self.groupBox_4)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.verticalLayout_25.addWidget(self.lineEdit_13)


        self.horizontalLayout_12.addLayout(self.verticalLayout_25)


        self.verticalLayout_29.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(-1, 9, -1, 9)
        self.label_24 = QLabel(self.groupBox_4)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_26.addWidget(self.label_24)

        self.dateTimeEdit_3 = QDateTimeEdit(self.groupBox_4)
        self.dateTimeEdit_3.setObjectName(u"dateTimeEdit_3")
        self.dateTimeEdit_3.setCalendarPopup(True)

        self.verticalLayout_26.addWidget(self.dateTimeEdit_3)


        self.horizontalLayout_13.addLayout(self.verticalLayout_26)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(-1, 9, -1, 9)
        self.label_23 = QLabel(self.groupBox_4)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_27.addWidget(self.label_23)

        self.lineEdit_14 = QLineEdit(self.groupBox_4)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.verticalLayout_27.addWidget(self.lineEdit_14)


        self.horizontalLayout_13.addLayout(self.verticalLayout_27)


        self.verticalLayout_29.addLayout(self.horizontalLayout_13)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(-1, 9, -1, 9)
        self.label_25 = QLabel(self.groupBox_4)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_28.addWidget(self.label_25)

        self.lineEdit_15 = QLineEdit(self.groupBox_4)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.verticalLayout_28.addWidget(self.lineEdit_15)


        self.verticalLayout_29.addLayout(self.verticalLayout_28)


        self.verticalLayout_30.addWidget(self.groupBox_4)


        self.horizontalLayout_14.addLayout(self.verticalLayout_30)


        self.verticalLayout_3.addWidget(self.frame)

        self.tabContent.addTab(self.tab_principal, "")
        self.tab_servico = QWidget()
        self.tab_servico.setObjectName(u"tab_servico")
        self.verticalLayout_19 = QVBoxLayout(self.tab_servico)
        self.verticalLayout_19.setSpacing(2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.tab_servico)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 150))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_19.addWidget(self.frame_4)

        self.tableView = QTableView(self.tab_servico)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_19.addWidget(self.tableView)

        self.tabContent.addTab(self.tab_servico, "")
        self.tab_produtos = QWidget()
        self.tab_produtos.setObjectName(u"tab_produtos")
        self.tabContent.addTab(self.tab_produtos, "")

        self.verticalLayout.addWidget(self.tabContent)

        self.frame_2 = QFrame(LancManutencao)
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


        self.verticalLayout.addWidget(self.frame_2)

#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.dateTimeEdit)
        self.label_3.setBuddy(self.dateTimeEdit_2)
        self.label_8.setBuddy(self.combobox_tipo_combustivel)
        self.label_24.setBuddy(self.dateTimeEdit)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(LancManutencao)
        self.horizontalSlider.valueChanged.connect(self.label_10.setNum)

        self.tabContent.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(LancManutencao)
    # setupUi

    def retranslateUi(self, LancManutencao):
        LancManutencao.setWindowTitle(QCoreApplication.translate("LancManutencao", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("LancManutencao", u"Lan\u00e7amento", None))
        self.label.setText(QCoreApplication.translate("LancManutencao", u"Inicio da Manuten\u00e7\u00e3o", None))
        self.label_4.setText(QCoreApplication.translate("LancManutencao", u"\u00c0s", None))
        self.label_3.setText(QCoreApplication.translate("LancManutencao", u"Fim da Manuten\u00e7\u00e3o", None))
        self.label_8.setText(QCoreApplication.translate("LancManutencao", u"Tipo do servi\u00e7o:", None))
        self.combobox_tipo_combustivel.setItemText(0, QCoreApplication.translate("LancManutencao", u"Preventiva", None))
        self.combobox_tipo_combustivel.setItemText(1, QCoreApplication.translate("LancManutencao", u"Corretiva", None))
        self.combobox_tipo_combustivel.setItemText(2, QCoreApplication.translate("LancManutencao", u"Preditiva", None))
        self.combobox_tipo_combustivel.setItemText(3, QCoreApplication.translate("LancManutencao", u"Detectiva", None))

#if QT_CONFIG(tooltip)
        self.combobox_tipo_combustivel.setToolTip(QCoreApplication.translate("LancManutencao", u"<html><head/><body><p><span style=\" font-family:'Cabin,Helvetica,sans-serif'; font-size:large; font-weight:600; color:#575756; text-transform:uppercase;\">1 \u2013 Manuten\u00e7\u00e3o preventiva</span></p><p><span style=\" font-family:'Open Sans,sans-serif'; font-size:16px; color:#6f6e6b; background-color:#ffffff;\">Os ve\u00edculos passam por inspe\u00e7\u00e3o para evitar poss\u00edveis falhas e problemas. De acordo com um planejamento que utiliza a Curva de Tempo M\u00e9dio para Falha, \u00e9 poss\u00edvel identificar um tempo estimado para trocar determinada pe\u00e7a do ve\u00edculo e evitar que ela estrague e cause algum problema no autom\u00f3vel.</span></p><p><span style=\" font-family:'Cabin,Helvetica,sans-serif'; font-size:large; font-weight:600; color:#575756; text-transform:uppercase;\">2 \u2013 Manuten\u00e7\u00e3o corretiva</span></p><p><span style=\" font-family:'Open Sans,sans-serif'; font-size:16px; color:#6f6e6b; background-color:#ffffff;\">Quando alguma parte do seu carro j\u00e1 est\u00e1"
                        " quebrada ou com falha, voc\u00ea precisa fazer uma manuten\u00e7\u00e3o corretiva para trocar ou consertar a pe\u00e7a com defeito.</span></p><p><span style=\" font-family:'Cabin,Helvetica,sans-serif'; font-size:large; font-weight:600; color:#575756; text-transform:uppercase;\">3 \u2013 Manuten\u00e7\u00e3o preditiva</span></p><p><span style=\" font-family:'Open Sans,sans-serif'; font-size:16px; color:#6f6e6b; background-color:#ffffff;\">Nesta categoria, o monitoramento segue uma regularidade para avaliar as condi\u00e7\u00f5es mec\u00e2nicas do ve\u00edculo. Para isso, s\u00e3o utilizados instrumentos espec\u00edficos, como c\u00e2meras termogr\u00e1ficas, ultrassons, inspe\u00e7\u00f5es visuais, entre outros.</span></p><p><span style=\" font-family:'Cabin,Helvetica,sans-serif'; font-size:large; font-weight:600; color:#575756; text-transform:uppercase;\">4 \u2013 Manuten\u00e7\u00e3o detectiva</span></p><p><span style=\" font-family:'Open Sans,sans-serif'; font-size:16px; color:#6f6e6b; background-color:#fff"
                        "fff;\">Para garantir a seguran\u00e7a e o bom funcionamento do ve\u00edculo, se busca identificar falhas antes delas acontecerem. Neste procedimento, s\u00e3o realizados testes para avaliar o uso a longo prazo do autom\u00f3vel. Todos os itens s\u00e3o analisados em funcionamento.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("LancManutencao", u"Informa\u00e7\u00f5es do Veiculo", None))
        self.label_5.setText(QCoreApplication.translate("LancManutencao", u"Km Rodados : ", None))
        self.label_6.setText(QCoreApplication.translate("LancManutencao", u"trip - 1 :", None))
        self.label_7.setText(QCoreApplication.translate("LancManutencao", u"trip - 2 :", None))
        self.label_9.setText(QCoreApplication.translate("LancManutencao", u"Media KM/Lt", None))
        self.label_11.setText(QCoreApplication.translate("LancManutencao", u"Quantidade Tanque :", None))
        self.label_10.setText(QCoreApplication.translate("LancManutencao", u"0", None))
        self.label_12.setText(QCoreApplication.translate("LancManutencao", u"%", None))
        self.label_13.setText(QCoreApplication.translate("LancManutencao", u"OBS :", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("LancManutencao", u"Empresa Respons\u00e1vel :", None))
        self.label_14.setText(QCoreApplication.translate("LancManutencao", u"Nome da Empresa : ", None))
        self.label_15.setText(QCoreApplication.translate("LancManutencao", u"Respons\u00e1vel :", None))
        self.label_16.setText(QCoreApplication.translate("LancManutencao", u"Telefone de Contato :", None))
        self.lineEdit_8.setInputMask(QCoreApplication.translate("LancManutencao", u"(00) 0 0000-0000", None))
        self.checkBox.setText(QCoreApplication.translate("LancManutencao", u" WhatsApp", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), QCoreApplication.translate("LancManutencao", u"Principal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage2), QCoreApplication.translate("LancManutencao", u"Outros", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("LancManutencao", u"Financeiro", None))
        self.label_17.setText(QCoreApplication.translate("LancManutencao", u"Conta ", None))
        self.label_18.setText(QCoreApplication.translate("LancManutencao", u"Forna de Pagamento", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("LancManutencao", u"Pix", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("LancManutencao", u"Dinheiro", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("LancManutencao", u"Cart\u00e3o de D\u00e9bito", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("LancManutencao", u"Cart\u00e3o de Cr\u00e9dito", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("LancManutencao", u"Outros", None))

        self.label_19.setText(QCoreApplication.translate("LancManutencao", u"Total :", None))
        self.label_20.setText(QCoreApplication.translate("LancManutencao", u"Desconto :", None))
        self.label_21.setText(QCoreApplication.translate("LancManutencao", u"Acr\u00e9scimo :", None))
        self.label_22.setText(QCoreApplication.translate("LancManutencao", u"Total Final :", None))
        self.label_24.setText(QCoreApplication.translate("LancManutencao", u"Data de Pagamento :", None))
        self.label_23.setText(QCoreApplication.translate("LancManutencao", u"N\u00famero de Recibo", None))
        self.label_25.setText(QCoreApplication.translate("LancManutencao", u"OBS :", None))
        self.tabContent.setTabText(self.tabContent.indexOf(self.tab_principal), QCoreApplication.translate("LancManutencao", u"Principal", None))
        self.tabContent.setTabText(self.tabContent.indexOf(self.tab_servico), QCoreApplication.translate("LancManutencao", u"Servi\u00e7o", None))
        self.tabContent.setTabText(self.tabContent.indexOf(self.tab_produtos), QCoreApplication.translate("LancManutencao", u"Produtos", None))
        self.label_2.setText(QCoreApplication.translate("LancManutencao", u"Quantidade de cadastros:", None))
        self.lbl_total.setText(QCoreApplication.translate("LancManutencao", u"0", None))
#if QT_CONFIG(tooltip)
        self.bnt_back_full.setToolTip(QCoreApplication.translate("LancManutencao", u"<html><head/><body><p>Ir para o primeiro...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_back_full.setText(QCoreApplication.translate("LancManutencao", u"<<", None))
#if QT_CONFIG(tooltip)
        self.bnt_back.setToolTip(QCoreApplication.translate("LancManutencao", u"<html><head/><body><p>Voltar...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_back.setText(QCoreApplication.translate("LancManutencao", u"<", None))
#if QT_CONFIG(tooltip)
        self.bnt_next.setToolTip(QCoreApplication.translate("LancManutencao", u"<html><head/><body><p>Pr\u00f3ximo...</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_next.setText(QCoreApplication.translate("LancManutencao", u">", None))
#if QT_CONFIG(tooltip)
        self.bnt_next_full.setToolTip(QCoreApplication.translate("LancManutencao", u"<html><head/><body><p><span style=\" font-weight:600;\">Ir para o fim.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.bnt_next_full.setText(QCoreApplication.translate("LancManutencao", u">>", None))
        self.bnt_alterar.setText(QCoreApplication.translate("LancManutencao", u"&Alterar", None))
        self.bnt_adicionar.setText(QCoreApplication.translate("LancManutencao", u"&Incluir", None))
#if QT_CONFIG(shortcut)
        self.bnt_adicionar.setShortcut(QCoreApplication.translate("LancManutencao", u"Alt+I", None))
#endif // QT_CONFIG(shortcut)
        self.bnt_salvar.setText(QCoreApplication.translate("LancManutencao", u"&Salvar", None))
#if QT_CONFIG(shortcut)
        self.bnt_salvar.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.bnt_search.setText(QCoreApplication.translate("LancManutencao", u"&Pesquisar", None))
#if QT_CONFIG(shortcut)
        self.bnt_search.setShortcut(QCoreApplication.translate("LancManutencao", u"Alt+P", None))
#endif // QT_CONFIG(shortcut)
        self.bnt_excluir.setText(QCoreApplication.translate("LancManutencao", u"&Excluir", None))
#if QT_CONFIG(shortcut)
        self.bnt_excluir.setShortcut(QCoreApplication.translate("LancManutencao", u"Alt+E", None))
#endif // QT_CONFIG(shortcut)
        self.bnt_cancelar.setText(QCoreApplication.translate("LancManutencao", u"&Cancelar", None))
#if QT_CONFIG(shortcut)
        self.bnt_cancelar.setShortcut(QCoreApplication.translate("LancManutencao", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

