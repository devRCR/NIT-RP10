# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(1025, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1024, 768))
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.actionAbout_2 = QAction(MainWindow)
        self.actionAbout_2.setObjectName(u"actionAbout_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainLayout = QHBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)

        self.mainLayout.addWidget(self.groupBox)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ZWOSettings = QGroupBox(self.centralwidget)
        self.ZWOSettings.setObjectName(u"ZWOSettings")
        self.ZWOSettings.setEnabled(True)
        sizePolicy.setHeightForWidth(self.ZWOSettings.sizePolicy().hasHeightForWidth())
        self.ZWOSettings.setSizePolicy(sizePolicy)
        self.ZWOSettings.setMaximumSize(QSize(248, 350))
        self.ZWOSettings.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.ZWOSettings.setLayoutDirection(Qt.LeftToRight)
        self.ZWOSettings.setAutoFillBackground(False)
        self.ZWOSettings.setFlat(True)
        self.ZWOSettings.setCheckable(False)
        self.verticalLayoutWidget = QWidget(self.ZWOSettings)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 26, 231, 311))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.cameraGroup = QGroupBox(self.verticalLayoutWidget)
        self.cameraGroup.setObjectName(u"cameraGroup")
        sizePolicy.setHeightForWidth(self.cameraGroup.sizePolicy().hasHeightForWidth())
        self.cameraGroup.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.cameraGroup)

        self.imageGroup = QGroupBox(self.verticalLayoutWidget)
        self.imageGroup.setObjectName(u"imageGroup")
        self.imageGroup.setEnabled(False)
        sizePolicy.setHeightForWidth(self.imageGroup.sizePolicy().hasHeightForWidth())
        self.imageGroup.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.imageGroup)

        self.controlGroup = QGroupBox(self.verticalLayoutWidget)
        self.controlGroup.setObjectName(u"controlGroup")
        self.controlGroup.setEnabled(False)
        sizePolicy.setHeightForWidth(self.controlGroup.sizePolicy().hasHeightForWidth())
        self.controlGroup.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.controlGroup)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 4)

        self.verticalLayout.addWidget(self.ZWOSettings)

        self.TableSettings = QGroupBox(self.centralwidget)
        self.TableSettings.setObjectName(u"TableSettings")
        sizePolicy.setHeightForWidth(self.TableSettings.sizePolicy().hasHeightForWidth())
        self.TableSettings.setSizePolicy(sizePolicy)
        self.TableSettings.setMaximumSize(QSize(248, 350))

        self.verticalLayout.addWidget(self.TableSettings)


        self.mainLayout.addLayout(self.verticalLayout)

        self.mainLayout.setStretch(0, 3)
        self.mainLayout.setStretch(1, 1)

        self.gridLayout.addLayout(self.mainLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1025, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuEditar = QMenu(self.menubar)
        self.menuEditar.setObjectName(u"menuEditar")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        self.menuConfiguraci_n = QMenu(self.menubar)
        self.menuConfiguraci_n.setObjectName(u"menuConfiguraci_n")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menubar.addAction(self.menuConfiguraci_n.menuAction())
        self.menuArchivo.addAction(self.actionQuit)
        self.menuAyuda.addAction(self.actionPreferences)
        self.menuConfiguraci_n.addAction(self.actionAbout)
        self.menuConfiguraci_n.addAction(self.actionAbout_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NIT RP10", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"NIT Help", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.actionAbout_2.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.ZWOSettings.setTitle(QCoreApplication.translate("MainWindow", u"ZWO Settings", None))
        self.cameraGroup.setTitle(QCoreApplication.translate("MainWindow", u"C\u00e1mara", None))
        self.imageGroup.setTitle(QCoreApplication.translate("MainWindow", u"Imagen", None))
        self.controlGroup.setTitle(QCoreApplication.translate("MainWindow", u"Control", None))
        self.TableSettings.setTitle(QCoreApplication.translate("MainWindow", u"Table Settings", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEditar.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.menuConfiguraci_n.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

