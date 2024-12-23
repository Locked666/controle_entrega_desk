# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DisplaySearch.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDialog,
    QFrame, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_DisplaySearch(object):
    def setupUi(self, DisplaySearch):
        if not DisplaySearch.objectName():
            DisplaySearch.setObjectName(u"DisplaySearch")
        DisplaySearch.setWindowModality(Qt.ApplicationModal)
        DisplaySearch.resize(549, 498)
        icon = QIcon()
        icon.addFile(u":/icons/ico.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        DisplaySearch.setWindowIcon(icon)
        DisplaySearch.setSizeGripEnabled(True)
        DisplaySearch.setModal(True)
        self.verticalLayout = QVBoxLayout(DisplaySearch)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.DisplaySearch_2 = QFrame(DisplaySearch)
        self.DisplaySearch_2.setObjectName(u"DisplaySearch_2")
        self.DisplaySearch_2.setMinimumSize(QSize(0, 151))
        self.DisplaySearch_2.setMaximumSize(QSize(16777215, 151))
        self.DisplaySearch_2.setFrameShape(QFrame.StyledPanel)
        self.DisplaySearch_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.DisplaySearch_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.label_4 = QLabel(self.DisplaySearch_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.combo_column_search = QComboBox(self.DisplaySearch_2)
        self.combo_column_search.setObjectName(u"combo_column_search")
        self.combo_column_search.setMinimumSize(QSize(149, 20))

        self.verticalLayout_3.addWidget(self.combo_column_search)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.label_3 = QLabel(self.DisplaySearch_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_5.addWidget(self.label_3)

        self.text_content_search = QLineEdit(self.DisplaySearch_2)
        self.text_content_search.setObjectName(u"text_content_search")
        self.text_content_search.setClearButtonEnabled(True)

        self.verticalLayout_5.addWidget(self.text_content_search)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.bnt_search = QPushButton(self.DisplaySearch_2)
        self.bnt_search.setObjectName(u"bnt_search")
        self.bnt_search.setMinimumSize(QSize(100, 29))
        self.bnt_search.setMaximumSize(QSize(100, 41))
        icon1 = QIcon()
        icon1.addFile(u":/icons/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_search.setIcon(icon1)
        self.bnt_search.setIconSize(QSize(40, 40))
        self.bnt_search.setCheckable(False)
        self.bnt_search.setChecked(False)
        self.bnt_search.setAutoRepeat(False)
        self.bnt_search.setFlat(True)

        self.horizontalLayout_2.addWidget(self.bnt_search)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.groupBox = QGroupBox(self.DisplaySearch_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(220, 52))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radio_codigo = QRadioButton(self.groupBox)
        self.radio_codigo.setObjectName(u"radio_codigo")
        self.radio_codigo.setChecked(True)

        self.horizontalLayout.addWidget(self.radio_codigo)

        self.radio_descricao = QRadioButton(self.groupBox)
        self.radio_descricao.setObjectName(u"radio_descricao")

        self.horizontalLayout.addWidget(self.radio_descricao)

        self.radio_data = QRadioButton(self.groupBox)
        self.radio_data.setObjectName(u"radio_data")

        self.horizontalLayout.addWidget(self.radio_data)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_6.addWidget(self.groupBox)


        self.verticalLayout.addWidget(self.DisplaySearch_2)

        self.frame_2 = QFrame(DisplaySearch)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.table_search_content = QTableView(self.frame_2)
        self.table_search_content.setObjectName(u"table_search_content")
        self.table_search_content.setFrameShape(QFrame.NoFrame)
        self.table_search_content.setFrameShadow(QFrame.Raised)
        self.table_search_content.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_search_content.setDragEnabled(True)
        self.table_search_content.setDragDropMode(QAbstractItemView.InternalMove)
        self.table_search_content.setDefaultDropAction(Qt.TargetMoveAction)
        self.table_search_content.setAlternatingRowColors(True)
        self.table_search_content.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_search_content.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_search_content.setSortingEnabled(True)
        self.table_search_content.verticalHeader().setProperty(u"showSortIndicator", True)

        self.verticalLayout_2.addWidget(self.table_search_content)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(DisplaySearch)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 71))
        self.frame_3.setMaximumSize(QSize(16777215, 71))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 0, -1, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bnt_select = QPushButton(self.frame_3)
        self.bnt_select.setObjectName(u"bnt_select")
        self.bnt_select.setEnabled(True)
        self.bnt_select.setMinimumSize(QSize(100, 30))
        self.bnt_select.setMaximumSize(QSize(131, 41))
        icon2 = QIcon()
        icon2.addFile(u":/icons/adicionar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_select.setIcon(icon2)
        self.bnt_select.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.bnt_select)

        self.bnt_cancelar = QPushButton(self.frame_3)
        self.bnt_cancelar.setObjectName(u"bnt_cancelar")
        self.bnt_cancelar.setMinimumSize(QSize(100, 30))
        self.bnt_cancelar.setMaximumSize(QSize(131, 41))
        icon3 = QIcon()
        icon3.addFile(u":/icons/error.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bnt_cancelar.setIcon(icon3)
        self.bnt_cancelar.setIconSize(QSize(25, 25))
        self.bnt_cancelar.setCheckable(False)
        self.bnt_cancelar.setChecked(False)
        self.bnt_cancelar.setAutoRepeat(False)

        self.horizontalLayout_3.addWidget(self.bnt_cancelar)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer = QSpacerItem(58, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.groupBox_2 = QGroupBox(self.frame_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(251, 61))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 155, 15))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)


        self.horizontalLayout_4.addWidget(self.groupBox_2)


        self.verticalLayout.addWidget(self.frame_3)

        QWidget.setTabOrder(self.text_content_search, self.bnt_search)
        QWidget.setTabOrder(self.bnt_search, self.radio_codigo)
        QWidget.setTabOrder(self.radio_codigo, self.radio_descricao)
        QWidget.setTabOrder(self.radio_descricao, self.radio_data)
        QWidget.setTabOrder(self.radio_data, self.table_search_content)
        QWidget.setTabOrder(self.table_search_content, self.bnt_select)
        QWidget.setTabOrder(self.bnt_select, self.bnt_cancelar)

        self.retranslateUi(DisplaySearch)

        QMetaObject.connectSlotsByName(DisplaySearch)
    # setupUi

    def retranslateUi(self, DisplaySearch):
        DisplaySearch.setWindowTitle(QCoreApplication.translate("DisplaySearch", u"Dialog", None))
        self.label_4.setText(QCoreApplication.translate("DisplaySearch", u"Coluna de pesquisa:", None))
        self.label_3.setText(QCoreApplication.translate("DisplaySearch", u"Conteudo da pesquisa :", None))
        self.bnt_search.setText("")
#if QT_CONFIG(shortcut)
        self.bnt_search.setShortcut(QCoreApplication.translate("DisplaySearch", u"Alt+P", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("DisplaySearch", u"Tipo da Pesquisa :", None))
        self.radio_codigo.setText(QCoreApplication.translate("DisplaySearch", u"Inicia", None))
        self.radio_descricao.setText(QCoreApplication.translate("DisplaySearch", u"Content", None))
        self.radio_data.setText(QCoreApplication.translate("DisplaySearch", u"Data", None))
        self.bnt_select.setText(QCoreApplication.translate("DisplaySearch", u"&Selecionar", None))
#if QT_CONFIG(shortcut)
        self.bnt_select.setShortcut(QCoreApplication.translate("DisplaySearch", u"Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.bnt_cancelar.setText(QCoreApplication.translate("DisplaySearch", u"&Cancelar", None))
#if QT_CONFIG(shortcut)
        self.bnt_cancelar.setShortcut(QCoreApplication.translate("DisplaySearch", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox_2.setTitle(QCoreApplication.translate("DisplaySearch", u"Outras Informa\u00e7\u00f5es :", None))
        self.label.setText(QCoreApplication.translate("DisplaySearch", u"Quantidade de Informa\u00e7\u00f5es :", None))
        self.label_2.setText(QCoreApplication.translate("DisplaySearch", u"0", None))
    # retranslateUi

