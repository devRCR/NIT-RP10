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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 21))
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
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEditar.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.menuConfiguraci_n.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

