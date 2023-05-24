# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '0804layout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.image as mpimg
import pandas as pd
import numpy as np
import mplcursors

from PyQt5 import Qt, QtCore, QtGui, QtWidgets, QtWebEngineWidgets

from PyQt5.QtWidgets import QHeaderView
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

from rdkit import Chem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1573, 1015)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName("tabWidget")
        self.RTpredict = QtWidgets.QWidget()
        self.RTpredict.setObjectName("RTpredict")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.RTpredict)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Predictmin = QtWidgets.QLabel(self.RTpredict)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.Predictmin.sizePolicy().hasHeightForWidth())
        self.Predictmin.setSizePolicy(sizePolicy)
        self.Predictmin.setMinimumSize(QtCore.QSize(0, 50))
        self.Predictmin.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Predictmin.setFont(font)
        self.Predictmin.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Predictmin.setObjectName("Predictmin")
        self.gridLayout_2.addWidget(self.Predictmin, 6, 3, 1, 1)
        self.Applysmi = QtWidgets.QPushButton(self.RTpredict)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Applysmi.sizePolicy().hasHeightForWidth())
        self.Applysmi.setSizePolicy(sizePolicy)
        self.Applysmi.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Applysmi.setFont(font)
        self.Applysmi.clicked.connect(self.PredictRT)
        self.Applysmi.setObjectName("Applysmi")
        self.gridLayout_2.addWidget(self.Applysmi, 5, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.RTpredict)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(150, 150))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/eunwoo/PycharmProjects/RTPredict/SG.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)
        self.Drawsketcher = QtWidgets.QLabel(self.RTpredict)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Drawsketcher.setFont(font)
        self.Drawsketcher.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Drawsketcher.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Drawsketcher.setAutoFillBackground(False)
        self.Drawsketcher.setTextFormat(QtCore.Qt.AutoText)
        self.Drawsketcher.setScaledContents(True)
        self.Drawsketcher.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.Drawsketcher.setObjectName("Drawsketcher")
        self.gridLayout_2.addWidget(self.Drawsketcher, 3, 1, 1, 3)
        self.PredictRT = QtWidgets.QLabel(self.RTpredict)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PredictRT.sizePolicy().hasHeightForWidth())
        self.PredictRT.setSizePolicy(sizePolicy)
        self.PredictRT.setMinimumSize(QtCore.QSize(0, 50))
        self.PredictRT.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.PredictRT.setFont(font)
        self.PredictRT.setObjectName("PredictRT")
        self.gridLayout_2.addWidget(self.PredictRT, 6, 1, 1, 1)
        self.Showpredict = QtWidgets.QLineEdit(self.RTpredict)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Showpredict.sizePolicy().hasHeightForWidth())
        self.Showpredict.setSizePolicy(sizePolicy)
        self.Showpredict.setMinimumSize(QtCore.QSize(0, 50))
        self.Showpredict.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Showpredict.setFont(font)
        self.Showpredict.setAlignment(QtCore.Qt.AlignCenter)
        self.Showpredict.setReadOnly(True)
        self.Showpredict.setObjectName("Showpredict")
        self.gridLayout_2.addWidget(self.Showpredict, 6, 2, 1, 1)
        self.RTscatter = QtWidgets.QWidget(self.centralwidget)
        self.RTscatter.setAutoFillBackground(False)
        self.RTscatter.setObjectName("RTscatter")

        self.fig1 = plt.Figure()
        self.canvas1 = FigureCanvas(self.fig1)
        self.canvas1_toolbar = NavigationToolbar(self.canvas1, self.RTscatter)
        self.vbox1 = QtWidgets.QVBoxLayout(self.RTscatter)
        self.vbox1.addWidget(self.canvas1_toolbar)
        self.vbox1.addWidget(self.canvas1)

        self.gridLayout_2.addWidget(self.RTscatter, 4, 4, 3, 3)
        self.label_2 = QtWidgets.QLabel(self.RTpredict)
        self.label_2.setMaximumSize(QtCore.QSize(200, 150))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/eunwoo/PycharmProjects/RTPredict/KY.jpg"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 6, 1, 1)
        self.Insertsmi = QtWidgets.QLineEdit(self.RTpredict)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Insertsmi.sizePolicy().hasHeightForWidth())
        self.Insertsmi.setSizePolicy(sizePolicy)
        self.Insertsmi.setMinimumSize(QtCore.QSize(0, 50))
        self.Insertsmi.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Insertsmi.setFont(font)
        self.Insertsmi.setAlignment(QtCore.Qt.AlignCenter)
        self.Insertsmi.setObjectName("Insertsmi")
        self.gridLayout_2.addWidget(self.Insertsmi, 5, 2, 1, 1)
        self.Showall = QtWidgets.QPushButton(self.RTpredict)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Showall.sizePolicy().hasHeightForWidth())
        self.Showall.setSizePolicy(sizePolicy)
        self.Showall.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Showall.setFont(font)
        self.Showall.setAutoFillBackground(True)
        self.Showall.clicked.connect(self.totalgraph)
        self.Showall.setObjectName("Showall")
        self.gridLayout_2.addWidget(self.Showall, 3, 4, 1, 1)
        self.Smi = QtWidgets.QLabel(self.RTpredict)
        self.Smi.setMinimumSize(QtCore.QSize(0, 50))
        self.Smi.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Smi.setFont(font)
        self.Smi.setObjectName("Smi")
        self.gridLayout_2.addWidget(self.Smi, 5, 1, 1, 1)
        # self.Outlierdescription = QtWidgets.QLabel(self.RTpredict)
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.Outlierdescription.setFont(font)
        # self.Outlierdescription.setObjectName("Outlierdescription")
        # self.gridLayout_2.addWidget(self.Outlierdescription, 8, 4, 1, 3)
        self.Title = QtWidgets.QLabel(self.RTpredict)
        self.Title.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Title.setAutoFillBackground(False)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.gridLayout_2.addWidget(self.Title, 1, 2, 1, 4)
        self.Sketcher = QtWebEngineWidgets.QWebEngineView(self.RTpredict)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sketcher.sizePolicy().hasHeightForWidth())
        self.Sketcher.setSizePolicy(sizePolicy)
        self.Sketcher.setMinimumSize(QtCore.QSize(680, 450))
        self.Sketcher.setMaximumSize(QtCore.QSize(1300, 450))
        self.Sketcher.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Sketcher.setAutoFillBackground(True)
        self.Sketcher.setUrl(QtCore.QUrl("https://pubchem.ncbi.nlm.nih.gov//edit3/index.html"))
        self.Sketcher.setObjectName("Sketcher")
        self.gridLayout_2.addWidget(self.Sketcher, 4, 1, 1, 3)
        # self.Outlier = QtWidgets.QLabel(self.RTpredict)
        # font = QtGui.QFont()
        # font.setPointSize(15)
        # self.Outlier.setFont(font)
        # self.Outlier.setObjectName("Outlier")
        # self.gridLayout_2.addWidget(self.Outlier, 7, 4, 1, 2)
        self.Showspecific = QtWidgets.QPushButton(self.RTpredict)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Showspecific.sizePolicy().hasHeightForWidth())
        self.Showspecific.setSizePolicy(sizePolicy)
        self.Showspecific.setMinimumSize(QtCore.QSize(150, 50))
        self.Showspecific.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Showspecific.setFont(font)
        self.Showspecific.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Showspecific.setAutoFillBackground(True)
        self.Showspecific.clicked.connect(self.specific)
        self.Showspecific.setObjectName("Showspecific")
        self.gridLayout_2.addWidget(self.Showspecific, 3, 6, 1, 1)
        self.plainTextEdit = QtWidgets.QLineEdit(self.RTpredict)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.plainTextEdit.setMaximumSize(QtCore.QSize(500, 50))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_2.addWidget(self.plainTextEdit, 3, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 7, 1, 1, 3)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.RTpredict, "")
        self.RTfit = QtWidgets.QWidget()
        self.RTfit.setObjectName("RTfit")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.RTfit)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.KY_fit = QtWidgets.QLabel(self.RTfit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.KY_fit.sizePolicy().hasHeightForWidth())
        self.KY_fit.setSizePolicy(sizePolicy)
        self.KY_fit.setMinimumSize(QtCore.QSize(100, 150))
        self.KY_fit.setMaximumSize(QtCore.QSize(230, 160))
        self.KY_fit.setText("")
        self.KY_fit.setPixmap(QtGui.QPixmap("C:/Users/eunwoo/PycharmProjects/RTPredict/KY.jpg"))
        self.KY_fit.setObjectName("KY_fit")
        self.gridLayout_4.addWidget(self.KY_fit, 0, 5, 1, 1)
        self.Title_fit = QtWidgets.QLabel(self.RTfit)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.Title_fit.setFont(font)
        self.Title_fit.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_fit.setObjectName("Title_fit")
        self.gridLayout_4.addWidget(self.Title_fit, 0, 1, 1, 4)
        self.Entermin = QtWidgets.QLabel(self.RTfit)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Entermin.setFont(font)
        self.Entermin.setObjectName("Entermin")
        self.gridLayout_4.addWidget(self.Entermin, 4, 5, 1, 1)
        self.InsertRT = QtWidgets.QLineEdit(self.RTfit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.InsertRT.sizePolicy().hasHeightForWidth())
        self.InsertRT.setSizePolicy(sizePolicy)
        self.InsertRT.setMinimumSize(QtCore.QSize(0, 40))
        self.InsertRT.setMaximumSize(QtCore.QSize(400, 60))
        self.InsertRT.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.InsertRT.setFont(font)
        self.InsertRT.setObjectName("InsertRT")
        self.gridLayout_4.addWidget(self.InsertRT, 4, 4, 1, 1)
        self.SG_fit = QtWidgets.QLabel(self.RTfit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SG_fit.sizePolicy().hasHeightForWidth())
        self.SG_fit.setSizePolicy(sizePolicy)
        self.SG_fit.setMinimumSize(QtCore.QSize(150, 150))
        self.SG_fit.setMaximumSize(QtCore.QSize(150, 150))
        self.SG_fit.setText("")
        self.SG_fit.setPixmap(QtGui.QPixmap("C:/Users/eunwoo/PycharmProjects/RTPredict/SG.png"))
        self.SG_fit.setScaledContents(True)
        self.SG_fit.setObjectName("SG_fit")
        self.gridLayout_4.addWidget(self.SG_fit, 0, 0, 1, 1)
        self.Calculate = QtWidgets.QPushButton(self.RTfit)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Calculate.setFont(font)
        self.Calculate.clicked.connect(self.fitrt)
        self.Calculate.setObjectName("Calculate")
        self.gridLayout_4.addWidget(self.Calculate, 5, 4, 1, 1)
        self.FitRT = QtWidgets.QPushButton(self.RTfit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FitRT.sizePolicy().hasHeightForWidth())
        self.FitRT.setSizePolicy(sizePolicy)
        self.FitRT.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.FitRT.setFont(font)
        self.FitRT.clicked.connect(self.bringfit)
        self.FitRT.setObjectName("FitRT")
        self.gridLayout_4.addWidget(self.FitRT, 4, 2, 1, 1)
        self.FindRT = QtWidgets.QPushButton(self.RTfit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FindRT.sizePolicy().hasHeightForWidth())
        self.FindRT.setSizePolicy(sizePolicy)
        self.FindRT.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.FindRT.setFont(font)
        self.FindRT.clicked.connect(self.findpredrt)
        self.FindRT.setObjectName("FindRT")
        self.gridLayout_4.addWidget(self.FindRT, 4, 0, 1, 1)
        self.Fitfigure = QtWidgets.QWidget(self.RTfit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Fitfigure.sizePolicy().hasHeightForWidth())
        self.Fitfigure.setSizePolicy(sizePolicy)
        self.Fitfigure.setMaximumSize(QtCore.QSize(850, 580))
        self.Fitfigure.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Fitfigure.setAutoFillBackground(False)

        self.fig2 = plt.Figure()
        self.canvas2 = FigureCanvas(self.fig2)
        self.canvas2_toolbar = NavigationToolbar(self.canvas2, self.Fitfigure)
        self.vbox2 = QtWidgets.QVBoxLayout(self.Fitfigure)
        self.vbox2.addWidget(self.canvas2_toolbar)
        self.vbox2.addWidget(self.canvas2)

        self.Fitfigure.setObjectName("Fitfigure")
        self.gridLayout_4.addWidget(self.Fitfigure, 1, 3, 1, 3)
        self.Fittable = QtWidgets.QTableWidget(self.RTfit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Fittable.sizePolicy().hasHeightForWidth())
        self.Fittable.setSizePolicy(sizePolicy)
        self.Fittable.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Fittable.setFont(font)
        self.Fittable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Fittable.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.Fittable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Fittable.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.Fittable.setRowCount(6)
        self.Fittable.setColumnCount(3)
        self.Fittable.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)  # 셀 수정 가능하게 변경
        self.Fittable.setHorizontalHeaderLabels(["Metabolite", "Your experimental RT", "Predicted RT"])
        self.Fittable.resizeColumnToContents(3)
        self.Fittable.resizeRowToContents(6)
        self.Fittable.setObjectName("Fittable")
        self.Fittable.horizontalHeader().setCascadingSectionResizes(False)
        self.Fittable.horizontalHeader().setDefaultSectionSize(200)
        self.Fittable.horizontalHeader().setHighlightSections(False)
        self.Fittable.verticalHeader().setCascadingSectionResizes(False)
        self.Fittable.verticalHeader().setDefaultSectionSize(90)
        self.Fittable.verticalHeader().setSortIndicatorShown(False)
        self.Fittable.verticalHeader().setStretchLastSection(False)
        self.gridLayout_4.addWidget(self.Fittable, 1, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 2, 0, 1, 6)
        self.Fitmin = QtWidgets.QLabel(self.RTfit)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Fitmin.setFont(font)
        self.Fitmin.setObjectName("Fitmin")
        self.gridLayout_4.addWidget(self.Fitmin, 7, 5, 1, 1)
        self.Fitresult = QtWidgets.QLineEdit(self.RTfit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Fitresult.sizePolicy().hasHeightForWidth())
        self.Fitresult.setSizePolicy(sizePolicy)
        self.Fitresult.setMinimumSize(QtCore.QSize(0, 40))
        self.Fitresult.setMaximumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Fitresult.setFont(font)
        self.Fitresult.setObjectName("Fitresult")
        self.Fitresult.setAlignment(QtCore.Qt.AlignCenter)
        self.Fitresult.setReadOnly(True)
        self.gridLayout_4.addWidget(self.Fitresult, 7, 4, 1, 1)
        self.EnterRT = QtWidgets.QLabel(self.RTfit)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.EnterRT.setFont(font)
        self.EnterRT.setAlignment(QtCore.Qt.AlignCenter)
        self.EnterRT.setObjectName("EnterRT")
        self.gridLayout_4.addWidget(self.EnterRT, 4, 3, 1, 1)
        self.FittedRT = QtWidgets.QLabel(self.RTfit)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.FittedRT.setFont(font)
        self.FittedRT.setAlignment(QtCore.Qt.AlignCenter)
        self.FittedRT.setObjectName("FittedRT")
        self.gridLayout_4.addWidget(self.FittedRT, 7, 3, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 1, 1, 1)
        self.tabWidget.addTab(self.RTfit, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1573, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def PredictRT(self):  # 입력된 SMILES에서 RT 예측시켜주는 함수.
        smi_enter = self.Insertsmi.text()
        mol_enter = Chem.MolFromSmiles(smi_enter)  # 이 단계에서의 에러 핸들링해야 함
        smi = Chem.MolToSmiles(mol_enter)
        pred_rt = {'Cn1cnc(C[C@H](N)C(=O)O)c1': 3.48,
                   'NCCCN': [3.5, 19.66],
                   'O=C(O)Cc1ccc(O)cc1': 17.99,
                   'N[C@@H](Cc1ccc(O)c(I)c1)C(=O)O': 19.8,
                   'COc1cc(CCN)ccc1O': 23.33,
                   'Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]1O': 3.84,
                   'Nc1ncnc2c1ncn2[C@@H]1O[C@H](CO)[C@@H](O)[C@H]1O': 4.32,
                   'N': 6.8,
                   'NCCC(=O)O': 8.21,
                   'CN(CC(O)=O)C(N)=N': 3.7,
                   'O=C(O)C1CCCCN1': 13.74,
                   'Nc1nc2c(ncn2[C@H]2C[C@H](O)[C@@H](CO)O2)c(=O)[nH]1': 8.9,
                   'CNC': 12.61,
                   'Nc1ccn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)n1': [4.21, 7.62],
                   'Nc1ccn([C@@H]2O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)n1': [3.59, 3.85],
                   'N[C@@H](CCSC[C@H](N)C(=O)O)C(=O)O': [13.79, 13.83],
                   'Nc1ncnc2c1ncn2[C@H]1C[C@H](O)[C@@H](CO)O1': 8.12,
                   'NCCCC(=O)O': [7.89, 15.54],
                   'COc1cc(CC(=O)O)ccc1O': 17.05,
                   'NCC(=O)O': 7.94,
                   'N=C(N)NCC(=O)O': 3.84,
                   'O=C(O)Cc1cc(O)ccc1O': 21.97,
                   'Nc1nc2c(ncn2[C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]1': 4.44,
                   'N[C@@H](CCC(=O)O)C(=O)O': [6.24, 9.59],
                   'NCCO': 5.92,
                   'O=C(O)c1cc(O)ccc1O': [18.7, 22.3],
                   'C[C@]12CC[C@@H]3c4ccc(O)cc4CC[C@H]3[C@@H]1C[C@@H](O)[C@@H]2O': 22.76,
                   'Oc1ncnc2nc[nH]c12': [3.77, 9.23, 9.59],
                   'N[C@@H](Cc1ccc(O)cc1)C(=O)O': 20.88, 
                   'N[C@@H](Cc1ccccc1)C(=O)O': 13.33,
                   'C[C@H](N)C(=O)O': 8.85,
                   'O=C(O)[C@@H]1CCCN1': 11.37,
                   'CN': 8.63,
                   'C[C@@H](O)[C@H](N)C(=O)O': 4.56,
                   'NC(=O)C[C@H](N)C(=O)O': [4.05, 6.68],
                   'CC[C@H](C)[C@H](N)C(=O)O': 13.47,
                   'N[C@@H](Cc1cnc[nH]1)C(=O)O': 16.53,
                   'NCCCC[C@H](N)C(=O)O': 16.65,
                   'N[C@@H](CO)C(=O)O': 4.23,
                   'N[C@@H](CC(=O)O)C(=O)O': 4.93,
                   'N[C@@H](CSSC[C@H](N)C(=O)O)C(=O)O': 14.36,
                   'CC(=O)NCCCC[C@H](N)C(=O)O': 6.31,
                   'CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)O': 9.18,
                   'NCCC[C@H](N)C(=O)O': 16.39,
                   'NCCOP(=O)(O)O': 3.31,
                   'Oc1ccccc1': 21.79,
                   'C[C@H](O)C(=O)C1=Nc2c([nH]c(N)nc2=O)NC1': 10.62,
                   'Cc1ncc(CO)c(CO)c1O': [10.47, 17.35],
                   'NCCS(=O)(=O)O': 2.87,
                   'NCCc1c[nH]c2ccc(O)cc12': 21.41,
                   'Cc1c[nH]c(=O)[nH]c1=O': 13.21,
                   'N[C@@H](Cc1cc(I)c(Oc2ccc(O)c(I)c2)c(I)c1)C(=O)O': 21.68,
                   'CNCC(=O)O': 9.1,
                   'N[C@@H](CCCCN[C@@H](CCC(=O)O)C(=O)O)C(=O)O': [3.25, 5.56],
                   'COc1cc([C@H](O)C(=O)O)ccc1O': [14.11, 21.62],
                   'O=c1[nH]c(=O)c2[nH]cnc2[nH]1': 9.42,
                   'O=c1ccn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]1': [7.78, 9.48],
                   'O=c1cc[nH]c(=O)[nH]1': 11.33,
                   'O=C(O)/C=C/c1c[nH]cn1': 13.54,
                   'NCCc1c[nH]c2ccccc12': 17.04,
                   'NCCc1ccc(O)cc1': 23.1,
                   'C[C@]12CC[C@@H]3c4ccc(O)cc4CC[C@H]3[C@@H]1C[C@@H](O)[C@H]2O': 22.76,
                   'NC(CP(=O)(O)O)C(=O)O': 2.53,
                   'O=C(O)c1cccc(O)c1O': 18.09,
                   'O=C(O)Cc1cccc(O)c1': 16.39,
                   'CC(=O)N[C@@H](CCCCN)C(=O)O': 6.05,
                   'NC[C@H](O)CC[C@H](N)C(=O)O': 13.8,
                   'CC[C@H](N)C(=O)O': 9.87,
                   'NC(CSCC[C@H](N)C(=O)O)C(=O)O': [13.79, 13.83],
                   'C[C@H](O)[C@H](O)c1c[nH]c2nc(N)nc(=O)c-2n1': 6.9,
                   'O=c1[nH]cc(CO)c(=O)[nH]1': 9.17,
                   'CN(C)c1ncnc2nc[nH]c12': 17.64,
                   'Cn1cncc1C[C@H](N)C(=O)O': 3.61,
                   'CO=C(O)c1ccc(O)c(O)c1': 16.88,
                   'O=C(O)c1ccc(O)cc1': 17.11,
                   'N[C@@H](Cc1c[nH]c2ccc(O)cc12)C(=O)O': 18.99,
                   'N[C@@H](CCCC(=O)O)C(=O)O': 6.34,
                   'N=C(N)NCCC[C@H](N)C(=O)O': 3.78,
                   'CC[C@@H](C)[C@H](N)C(=O)O': 13.47,
                   'N[C@@H](CS)C(=O)O': 14.41,
                   'N[C@H]1[C@H](O)O[C@H](COS(=O)(=O)O)[C@@H](O)[C@@H]1O': 2.32,
                   'CNC[C@H](O)c1ccc(O)c(O)c1': [6.51, 7.14, 8.94],
                   'Nc1ccnc(=O)[nH]1': 9.59,
                   'NC(=O)CC[C@H](N)C(=O)O': 4.32,
                   'CC[C@@H](N)C(=O)O': 9.87,
                   'N[C@@H](Cc1ccc(Oc2ccc(O)cc2)cc1)C(=O)O': 20.93,
                   'O=C(O)Cc1ccccc1O': 16.28,
                   'N=C(N)NCCCC[C@H](N)C(=O)O': 3.76,
                   'NC(CCSSCC[C@H](N)C(=O)O)C(=O)O': 14.85,
                   'NC(=O)NCCCC[C@H](N)C(=O)O': 3.6,
                   'Nc1ccccc1C(=O)C[C@H](N)C(=O)O': [12.02, 13.1],
                   'CC(C)C[C@H](N)C(=O)O': 13.11,
                   'CSCC[C@H](N)C(=O)O': 11.47,
                   'Nc1nc(=O)c2ncc(=O)[nH]c2[nH]1': [10.02, 11.06],
                   'N[C@@H](CC(=O)O)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 10,
                   'O=C(O)CNC(=O)c1ccccc1': 10.29,
                   'O=C(O)[C@@H]1CCCCN1': 13.74,
                   'O=C(O)[C@H](CCO)NO': [4.18, 10.92],
                   'NCC(=O)N1CCC[C@H]1C(=O)O': 7.72,
                   'O=C(O)[C@@H]1C[C@@H](O)CN1': 5.79,
                   'O=C(O)/C=C/c1c[nH]c2ccccc12': 19.36,
                   'O=C(O)C(O)c1cccc(O)c1': [14.92, 22.06],
                   'O=C(O)C(O)Cc1ccc(O)cc1': 16.27,
                   'CC(C)C[C@H](NC(=O)CN)C(=O)O': 11.32,
                   'O=C(O)Cc1c[nH]c2ccc(O)cc12': 17.36,
                   'COc1cc(C(O)CN)ccc1O': 21.1,
                   'O=C(O)CNC(=O)c1ccccc1O': 12.11,
                   'O=C(O)c1cc(O)c2cccc(O)c2n1': [15.72, 21.67],
                   'CC(C)[C@H](N)C(=O)O': 11.62,
                   'Cc1cn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]c1=O': [5.24, 8, 10.12],
                   'Cn1cnc2[nH]c(N)nc(=O)c21': 10.11,
                   'NC(=O)NCCC[C@H](N)C(=O)O': 3.7,
                   'Nc1ncnc2c1ncn2[C@H]1C[C@H](O)[C@@H](COP(=O)(O)O)O1': 3.76,
                   'N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O': 12.12,
                   'Nc1ncnc2c1ncn2[C@@H]1O[C@H](CSCC[C@H](N)C(=O)O)[C@@H](O)[C@H]1O': 11.88,
                   'COc1cc(/C=C/C(=O)O)ccc1O': 18.91,
                   'COc1ccc(/C=C/C(=O)O)cc1O': 18.65,
                   'Oc1ccccc1O': 24.46,
                   'NCCS(=O)O': 3.56,
                   'Cc1cn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)nc1N': [4.14, 4.68],
                   'CCCCCCC(N)C(=O)O': 18.73,
                   'Nc1nc2c(ncn2[C@H]2C[C@H](O)[C@@H](COP(=O)(O)O)O2)c(=O)[nH]1': 4.16,
                   'N[C@@H](CCC(=O)N[C@@H](CS)C(=O)O)C(=O)O': 6.19,
                   'NCC(O)c1ccccc1': [11.51, 14.43],
                   'Nc1nc(Nc2ccccc2)nc2c1ncn2C1OC(CO)C(O)C1O': 8.84,
                   'Nc1ccccc1C(=O)O': 13.87,
                   'NCC(=O)CCC(=O)O': 7.47,
                   'Nc1ccc(O)cc1': [16.8, 23.08],
                   'CSC[C@H]1O[C@@H](n2cnc3c(N)ncnc32)[C@H](O)[C@@H]1O': 7.61,
                   'Nc1ccn([C@H]2C[C@H](O)[C@@H](COP(=O)(O)O)O2)c(=O)n1': 3.6,
                   'O=[N+]([O-])c1ccc(O)cc1': 22.68,
                   'CC(=O)NCCc1c[nH]c2ccc(O)cc12': 15.8,
                   'N[C@H]1[C@@H](O)O[C@H](COP(=O)(O)O)[C@@H](O)[C@@H]1O': 3.31,
                   'NCCCCNCCCN': 9.83,
                   'O=C(O)Cc1ccc(O)c(O)c1': 22.18,
                   'Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O': 3.08,
                   'N[C@@H](CCC[C@H](N)C(=O)O)C(=O)O': [13.67, 13.76],
                   'Nc1ccc(C(=O)O)cc1': 12.65,
                   'Nc1nc2c(ncn2[C@@H]2O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)[nH]1': 3.84,
                   'COc1ccccc1O': 22.12,
                   'C[N+](C)(C)CCOP(=O)(O)OP(=O)(O)OC[C@H]1O[C@@H](n2ccc(N)nc2=O)[C@H](O)[C@@H]1O': [3.13, 3.41],
                   'NCCCCN': 19.72,
                   'Cc1ncc(CO)c(CN)c1O': 19.07,
                   'N=C(N)NCCCCN': [3.7, 13.96],
                   'Nc1c(O)cccc1C(=O)O': 15.2,
                   'CNC(=N)N': [4.28, 19.84],
                   'c1c[nH]cn1': 15.61,
                   'Cc1ncc(CO)c(C=O)c1O': 12.87,
                   'CCCC[C@H](N)C(=O)O': 14.06,
                   'O=C(O)/C=C/c1cccc(O)c1': 19.55,
                   'Nc1nc(N)c2nc(CNc3ccc(C(=O)NC(CCC(=O)O)C(=O)O)cc3)cnc2n1': 7.69,
                   'N=C(N)N': 3.91,
                   'CC(C)NCC(O)COc1cccc2ccccc12': 22.58,
                   'OCCc1c[nH]c2ccc(O)cc12': 17.21,
                   'O=C(O)c1ccc(O)c(O)c1': 22.21,
                   'Cc1ccc(O)cc1': 24.8,
                   'CC(=O)Nc1ccc(O)cc1': 17.85,
                   'Cn1cncc1CCN': 3.44,
                   'O=C(O)C(O)c1ccc(O)c(O)c1': 19.87,
                   'Nc1ccc(C(=O)NCC(=O)O)cc1': 9.39,
                   'COc1ccc(O)c(C(=O)O)c1': 17.22,
                   'NC(Cc1ccc(O)c(Cl)c1)C(=O)O': 20.12,
                   'CN1C2=C(NC=N2)C(=O)N(C)C1=O': 15.43,
                   'Nc1cccc(C(=O)O)c1': 12.44,
                   'COC(=O)[C@H](Cc1ccccc1)NC(=O)[C@@H](N)CC(=O)O': 12.4,
                   'O=C(O)c1ccccc1O': 16.61,
                   'NCCCCCC(=O)O': 11.43,
                   'N[C@@H](Cc1ccc(O)c([N+](=O)[O-])c1)C(=O)O': [19.75, 21.06],
                   'CC(C)(N)C(=O)O': 9.58,
                   'NCCCC(O)(P(=O)(O)O)P(=O)(O)O': 3.2,
                   'N[C@@H](Cc1cc(I)c(Oc2cc(I)c(O)c(I)c2)c(I)c1)C(=O)O': 23.44,
                   'CC(C)NCC(O)COc1ccc(CC(N)=O)cc1': 11,
                   'COCCc1ccc(OCC(O)CNC(C)C)cc1': 21.87,
                   'CC(C)(C)NCC(O)c1ccc(O)c(CO)c1': [8.35, 8.92],
                   'NCCCC[C@H](N[C@@H](CCc1ccccc1)C(=O)O)C(=O)N1CCC[C@H]1C(=O)O': 8.04,
                   'C[C@@H](N)[C@@H](O)c1ccccc1': 14.98,
                   'CN[C@@H](C)[C@@H](O)c1ccccc1': 18.79,
                   'O=C(O)/C=C/c1ccc(O)c(O)c1': 23.78,
                   'Nc1cccc(C(=O)O)c1O': 12.81,
                   'CS(=O)CC[C@H](N)C(=O)O': [4.51, 4.41],
                   'NC[C@H](N)C(=O)O': 15.2,
                   'CC(N)c1ccccc1': 19.07,
                   'O=C(O)Cc1cnc[nH]1': 12.12,
                   'Cc1cccc(O)c1': 23.59,
                   'Cc1ccccc1O': 24.36,
                   'CC(=O)NCCCCN': 8.12,
                   'COc1cc(C(=O)O)cc(OC)c1O': 18.35,
                   'CNc1ncnc2nc[nH]c12': [12.23, 13.12],
                   'CSC[C@@H](N)C(=O)O': 10.31,
                   'Nc1cc(=O)nc(N)[nH]1': 8.84,
                   'CNC(C)(C)C(=O)O': 12.27,
                   'CNC[C@H](O)c1cccc(O)c1': 23.28,
                   'O=C(O)CCc1ccc(O)cc1': 18.82,
                   'N[C@@H](CCS(=O)(=O)O)C(=O)O': 2.43,
                   'NC(C(=O)O)c1ccccc1': 12.62,
                   'NCCCCCN': 19.88,
                   'COc1ccc2[nH]cc(C[C@H](N)C(=O)O)c2c1': 11.49,
                   'NCCC(N)C(=O)O': 15.93,
                   'Cc1cccc(C(=O)O)c1O': 17.78,
                   'CN[C@H](CC(=O)O)C(=O)O': 7.03,
                   'O=C(O)c1ccc(O)nc1': [13.29, 15.65],
                   'O=C1C[C@@H](c2ccc(O)cc2)Oc2cc(O)cc(O)c21': 20.11,
                   'N=C(N)NOCC[C@H](N)C(=O)O': [10.7, 11.09],
                   'NCCS': 16.07,
                   'Nc1ccccc1': 16.83,
                   'N[C@@H](CCCCNC(=O)CCCC[C@@H]1SC[C@@H]2NC(=O)N[C@H]12)C(=O)O': 6.76,
                   'N=C(N)N[C@@H](CC(=O)O)C(=O)O': 3.5,
                   'O=C(/C=C/c1ccc(O)c(O)c1)O[C@@H]1C[C@](O)(C(=O)O)C[C@@H](O)[C@H]1O': [20.44, 22.18],
                   'Cn1c(N)nc2nc[nH]c2c1=O': 9.87,
                   'O=C(O)c1c[nH]c2ccccc12': 17.89,
                   'CN=C(NC)NCCCC(N)C(=O)O': 3.64,
                   'N[C@@H](CCC(=O)N[C@@H](CSSC[C@H](NC(=O)CC[C@H](N)C(=O)O)C(=O)NCC(=O)O)C(=O)NCC(=O)O)C(=O)O': 8.8,
                   'NO': 12.16,
                   'NCCCCC(=O)O': 7.97,
                   'NC(=O)CC[C@@H](N)C(=O)O': 4.32,
                   'N[C@H](CO)Cc1c[nH]cn1': 3.36,
                   'N=C(N)NCCCC(=O)O': [3.94, 10.57],
                   'N[C@@H](Cc1cc(I)c(O)c(I)c1)C(=O)O': [12.47, 21.65],
                   'CC(C)[C@@H](N)CC(=O)O': [12.17, 20.99],
                   'CC(CN)C(=O)O': [8.9, 16.8],
                   'COc1ccc2[nH]cc(CCN)c2c1': 16.67,
                   'NC(C[Se][Se]CC(N)C(=O)O)C(=O)O': 14,
                   'OCCNCCO': 6.55,
                   'Oc1ccc(Cl)cc1Cl': 24.16,
                   'Cc1cc(C(=O)O)ccc1O': 18.96,
                   'NCCCC[C@H](NC(=O)[C@@H](N)CC(=O)O)C(=O)O': 13.28,
                   'CCOC(=O)c1ccc(N)cc1': 18.26,
                   'NC(Cc1ccccc1O)C(=O)O': 20.66,
                   'N[C@@H](Cc1ccccc1)C(=O)N1CCC[C@H]1C(=O)O': 12.84,
                   'N[C@@H](CCC(=O)N[C@@H](CCC(=O)O)C(=O)O)C(=O)O': 3.3,
                   'CC(C)C[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 16.74,
                   'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 16.42,
                   'C[C@H](N)C(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O': 18.23,
                   'CC(C)C[C@H](NC(=O)[C@H](C)N)C(=O)O': 11.33,
                   'C[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 12.1,
                   'C[C@H](N)C(=O)N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O': 11.55,
                   'C[C@H](N)C(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': 19.11,
                   'N=C(N)NCCC[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 7.09,
                   'CCC(C)C(N=C(O)CN)C(=O)O': 11.17,
                   'NCC(O)=NC(Cc1ccccc1)C(=O)O': 12.09,
                   'NCC(=O)NC(Cc1c[nH]c2ccccc12)C(=O)O': 11.58,
                   'NCC(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': 18.9,
                   'CC(C)[C@H](NC(=O)CN)C(=O)O': 10.01,
                   'C[C@H](NC(=O)[C@@H](N)Cc1cnc[nH]1)C(=O)O': 16.7,
                   'CC(C)C[C@H](N)C(=O)N1CCC[C@H]1C(=O)O': 13.26,
                   'CC(C)CC(N)C(O)=NC(Cc1c[nH]c2ccccc12)C(=O)O': 16.56,
                   'CC(C)CC(N)C(=O)NC(Cc1ccc(O)cc1)C(=O)O': 21.06,
                   'C[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': 11.01,
                   'N[C@@H](Cc1ccccc1)C(=O)NCC(=O)O': 8.96,
                   'CSCC[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': 14.54,
                   'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': 21.07,
                   'CC(C)[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': 14.48,
                   'CC(C)C[C@H](NC(=O)[C@@H](N)CO)C(=O)O': 9.24,
                   'N[C@@H](CO)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 9.84,
                   'CC(C)C[C@H](NC(=O)[C@@H](N)[C@@H](C)O)C(=O)O': 10.46,
                   'NC(Cc1c[nH]c2ccccc12)C(=O)NC(CCC(=O)O)C(=O)O': 9.86,
                   'CC(C)CC(N=C(O)C(N)Cc1c[nH]c2ccccc12)C(=O)O': 15.54,
                   'NC(Cc1c[nH]c2ccccc12)C(=O)NC(Cc1ccccc1)C(=O)O': 16.18,
                   'NC(Cc1c[nH]c2ccccc12)C(=O)NC(Cc1ccc(O)cc1)C(=O)O': 21.89,
                   'CC(NC(=O)C(N)Cc1ccc(O)cc1)C(=O)O': 19.05,
                   'N[C@@H](Cc1ccc(O)cc1)C(=O)NCC(=O)O': 18.88,
                   'CC(C)CC(N=C(O)C(N)Cc1ccc(O)cc1)C(=O)O': 21.4,
                   'CC(C)C(N=C(O)C(N)Cc1ccc(O)cc1)C(=O)O': 20.55,
                   'CCc1ccc(O)cc1': 24.64,
                   'O=C(O)c1ccc(O)c(O)c1O': 22.74,
                   'COc1cc(O)cc(OC)c1': 23.4,
                   'COc1ccc(C(=O)O)cc1O': 17.1,
                   'NCC(=O)NCC(=O)NCC(=O)NCC(=O)O': 3.31,
                   'N[C@@H](Cc1c[nH]c2ccccc12)C(=O)NCC(=O)NCC(=O)O': 7.95,
                   'CCCC(NC(=O)CN)C(=O)O': 9.6,
                   'CCCCC(NC(=O)CN)C(=O)O': 11.57,
                   'CC(C)C[C@H](Nc1ccccc1)C(=O)O': 17.29,
                   'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 18.48
                   }
        try:
            pred = pred_rt[smi]
        except:
            QtWidgets.QMessageBox.critical(Qt.qApp.activeWindow(), " ", "Please enter the right SMILES")
        else:  # float냐 list에 따라서 달리 처리할 것. string으로 변환시킬 것
            if str(type(pred)) == "<class 'float'>":
                RT_pred = str(pred)
                self.Showpredict.setText(RT_pred)
                self.Showpredict.setAlignment(QtCore.Qt.AlignCenter)
            elif str(type(pred)) == "<class 'list'>":
                RT_pred = " , ".join([str(i) for i in pred])
                self.Showpredict.setText(str(RT_pred))
                self.Showpredict.setAlignment(QtCore.Qt.AlignCenter)
            else:
                QtWidgets.QMessageBox.critical(Qt.qApp.activeWindow(), " ", "Please enter the right SMILES")

    def totalgraph(self):  # 전체 그래프 띄우기

        total = pd.read_csv("C:/Users/eunwoo/PycharmProjects/RTPredict/RT_predict_confirm.csv")
        exp_tot = total['Experimental_RT']  # 전체 실험값
        pred_tot = total['Predicted_RT']  # 전체 예측값
        Residual = pred_tot - exp_tot

        def outliers_iqr(data):
            q1, q3 = np.percentile(data, [25, 75])
            iqr = q3 - q1
            lower_bound = q1 - (iqr * 1.5)
            upper_bound = q3 + (iqr * 1.5)
            return np.where((data > upper_bound) | (data < lower_bound))

        outlier_index = outliers_iqr(Residual)[0]
        outlier = total.loc[outlier_index, :]
        exp_outlier = outlier['Experimental_RT']
        pred_outlier = outlier['Predicted_RT']
        df = total.drop(outlier_index)
        print(outlier_index)

        df_train = df.loc[
                   [0,   1,  2,   3,  5,   6,   7,   8,  10,  11, 12,  13,  14,  15,  16,  17,  18, 19,  20,  21,  22,  23,  24,  27,  29,  30,  33,  34,  35,  36,  37,  40,  41,  43, 44,  45,  46,  48,  49,  50,  51,  52,  54,  55,  56,  58,  59,  61,  62,  63,  64, 65,  66,  67,  69,  71,  73,  74,  75,  76,  77,  78,  79,  80,  81,  83,  85,  86,  89, 90,  92,  93,  94,  95,  96 , 97,  98, 100, 101, 103, 104, 106, 107, 108, 109, 110, 111, 112, 113, 116, 118, 120, 122, 123, 124, 125, 126, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 148, 149, 150, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 164, 166, 167, 168, 169, 171, 173, 175, 176, 178, 179, 180, 181, 182, 184, 186, 187, 188, 189, 190, 191, 194, 196, 199, 200, 204, 205, 206, 207, 208, 209, 210, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 238, 239, 240, 241, 245, 246, 247, 248, 249, 250, 252, 253, 254, 255, 256, 258, 259, 260, 261, 262, 263, 264, 266, 267, 268, 270, 272, 273, 274, 275, 279, 280, 281, 282, 283, 286, 287, 289, 291, 293, 294, 295, 296, 297, 298, 299, 300, 302, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314], :]
        df_test = df.loc[
                  [ 9,  25,  28,  31,  32,  38,  39,  42,  47,  53,  57,  68,  70,  72,  82,  84,  87,  88,  91, 99, 105, 115, 117, 119, 121, 127, 147, 151, 163, 165, 170, 172, 177, 183, 185, 193, 195, 197, 203, 211, 242, 243, 244, 251, 257, 265, 269, 271, 276, 277, 278, 284, 285, 290, 301, 303, 304], :]

        # train과 test 나눠서 scatter 그리기

        exp_df = df['Experimental_RT']
        pred_df = df['Predicted_RT']

        exp_df_train = df_train['Experimental_RT']
        pred_df_train = df_train['Predicted_RT']

        z = np.polyfit(exp_df_train, pred_df_train, 1)
        p = np.poly1d(z)

        exp_df_test = df_test['Experimental_RT']
        pred_df_test = df_test['Predicted_RT']

        outlier_list = ['Iodotyrosine', 'Serotonin', 'L-Thyroine', 'Hippuric acid', 'Xanthurenic acid', 'Xanthurenic acid - multi-tags', '3-Chlorotyrosine', 'Thyroxine', 'Naringenin', 'Phenylalanyl-Tyrosine']
        # 다시 쓰기 #만일 아웃라이어 smi입력한다면?

        # 아웃라이어는 별도의 산점도로

        self.fig1.clear()

        ax = self.fig1.subplots()
        # 그래프 사이즈 캔버스에 맞게 조정
        ax.text(13, 4, 'y = 0.90 * x + 1.30', color='black', weight='bold', fontsize=15,
                horizontalalignment='center', verticalalignment='bottom')
        ax.text(13, 2, 'Adjusted R square = 0.98', color='black', weight='bold', fontsize=15,
                horizontalalignment='center', verticalalignment='bottom')
        ax.scatter(exp_df_train, pred_df_train, facecolors='none', edgecolors='black', s=20)
        ax.scatter(exp_df_test, pred_df_test, color='blue', s=20)
        #ax.scatter(exp_outlier, pred_outlier, color='red', s=20)
        ax.plot(exp_df_train, p(exp_df_train), color='black', linewidth=2, linestyle='--')
        # 아웃라이어 제거. 그 후 무엇이 아웃라이어인지 명시할 것(논문과 프로그램 양쪽)
        # 프로그램은 메시지박스. 논문은 글로 써서 명시
        ax.set_xlim(0, 30)
        ax.set_ylim(0, 30)
        ax.axes.xaxis.set_major_locator(ticker.MultipleLocator(5))
        ax.axes.yaxis.set_major_locator(ticker.MultipleLocator(5))
        ax.axes.xaxis.set_minor_locator(ticker.MultipleLocator(1))
        ax.axes.yaxis.set_minor_locator(ticker.MultipleLocator(1))
        ax.set_xlabel("Experimental RT")
        ax.set_ylabel("Predicted RT")
        ax.set_title("Experimental RT vs Predicted RT")
        self.fig1.tight_layout()

        self.canvas1.draw()

        cursor1 = mplcursors.cursor(ax.scatter(exp_df_train, pred_df_train, facecolors='none', edgecolors='black', s=20),
                                    hover=True)
        cursor1.connect("add", lambda sel: sel.annotation.set_text('{}, {}'.format(sel.target[0], sel.target[1])))

        cursor2 = mplcursors.cursor(ax.scatter(exp_df_test, pred_df_test, color='blue', s=20), hover=True)
        cursor2.connect("add", lambda sel: sel.annotation.set_text('{}, {}'.format(sel.target[0], sel.target[1])))

        #cursor3 = mplcursors.cursor(ax.scatter(exp_outlier, pred_outlier, color='red', s=20), hover=True)
        #cursor3.connect("add", lambda sel: sel.annotation.set_text('{}, {}'.format(sel.target[0], sel.target[1])))

    def specific(self):  # 업데이트된 그래프 띄우기. 텍스트 창이 비어있으면 채우라고 메시지 띄우기
        # 키 값을 하나로 통일할 것. smi>키
        # 마우스 커서 혹은 그거와 상관없이 특정 값 좌표 띄우기
        # Dns화 된 이미지도 같이 띄우기>>특정 Dns. Dns 그림 원본을 작고 선명하게 바꾸기
        total = pd.read_csv("C:/Users/eunwoo/PycharmProjects/RTPredict/RT_predict_confirm.csv")
        exp_tot = total['Experimental_RT']  # 전체 실험값
        pred_tot = total['Predicted_RT']  # 전체 예측값
        exp_rt = {'Cn1cnc(C[C@H](N)C(=O)O)c1': 2.17,
                  'NCCCN': [2.63, 20.49],
                  'O=C(O)Cc1ccc(O)cc1': 16.91,
                  'N[C@@H](Cc1ccc(O)c(I)c1)C(=O)O': 23.88,
                  'COc1cc(CCN)ccc1O': 25.49,
                  'Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]1O': 1.75,
                  'Nc1ncnc2c1ncn2[C@@H]1O[C@H](CO)[C@@H](O)[C@H]1O': 3.94,
                  'N': 5.82,
                  'NCCC(=O)O': 7.24,
                  'CN(CC(O)=O)C(N)=N': 3.02,
                  'O=C(O)C1CCCCN1': 13.23,
                  'Nc1nc2c(ncn2[C@H]2C[C@H](O)[C@@H](CO)O2)c(=O)[nH]1': 8.49,
                  'CNC': 15.07,
                  'Nc1ccn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)n1': [5.87, 7.38],
                  'Nc1ccn([C@@H]2O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)n1': [1.88, 2.87],
                  'N[C@@H](CCSC[C@H](N)C(=O)O)C(=O)O': [13.34, 13.69],
                  'Nc1ncnc2c1ncn2[C@H]1C[C@H](O)[C@@H](CO)O1': 8.72,
                  'NCCCC(=O)O': [7.79, 13.57],
                  'COc1cc(CC(=O)O)ccc1O': 16.51,
                  'NCC(=O)O': 6.59,
                  'N=C(N)NCC(=O)O': 2.74,
                  'O=C(O)Cc1cc(O)ccc1O': 24.84,
                  'Nc1nc2c(ncn2[C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]1': 2.22,
                  'N[C@@H](CCC(=O)O)C(=O)O': [5.05, 9.46],
                  'NCCO': 6.00,
                  'O=C(O)c1cc(O)ccc1O': [17.11, 24.69],
                  'C[C@]12CC[C@@H]3c4ccc(O)cc4CC[C@H]3[C@@H]1C[C@@H](O)[C@@H]2O': 20.36,
                  'Oc1ncnc2nc[nH]c12': [2.12, 8.73, 9.65],
                  'N[C@@H](Cc1ccc(O)cc1)C(=O)O': 22.65,
                  'N[C@@H](Cc1ccccc1)C(=O)O': 12.74,
                  'C[C@H](N)C(=O)O': 7.57,
                  'O=C(O)[C@@H]1CCCN1': 10.18,
                  'CN': 9.82,
                  'C[C@@H](O)[C@H](N)C(=O)O': 5.79,
                  'NC(=O)C[C@H](N)C(=O)O': [3.00, 6.40],
                  'CC[C@H](C)[C@H](N)C(=O)O': 13.06,
                  'N[C@@H](Cc1cnc[nH]1)C(=O)O': 18.09,
                  'NCCCC[C@H](N)C(=O)O': 17.47,
                  'N[C@@H](CO)C(=O)O': 4.40,
                  'N[C@@H](CC(=O)O)C(=O)O': 5.16,
                  'N[C@@H](CSSC[C@H](N)C(=O)O)C(=O)O': 14.11,
                  'CC(=O)NCCCC[C@H](N)C(=O)O': 5.71,
                  'CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)O': 8.37,
                  'NCCC[C@H](N)C(=O)O': 16.58,
                  'NCCOP(=O)(O)O': 2.02,
                  'Oc1ccccc1': 23.16,
                  'C[C@H](O)C(=O)C1=Nc2c([nH]c(N)nc2=O)NC1': 10.14,
                  'Cc1ncc(CO)c(CO)c1O': [10.12, 18.01],
                  'NCCS(=O)(=O)O': 2.24,
                  'NCCc1c[nH]c2ccc(O)cc12': 24.65,
                  'Cc1c[nH]c(=O)[nH]c1=O': 13.21,
                  'N[C@@H](Cc1cc(I)c(Oc2ccc(O)c(I)c2)c(I)c1)C(=O)O': 19.14,
                  'CNCC(=O)O': 9.34,
                  'N[C@@H](CCCCN[C@@H](CCC(=O)O)C(=O)O)C(=O)O': [2.26, 5.65],
                  'COc1cc([C@H](O)C(=O)O)ccc1O': [12.81, 21.31],
                  'O=c1[nH]c(=O)c2[nH]cnc2[nH]1': 8.95,
                  'O=c1ccn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]1': [7.84, 8.67],
                  'O=c1cc[nH]c(=O)[nH]1': 11.34,
                  'O=C(O)/C=C/c1c[nH]cn1': 13.52,
                  'NCCc1c[nH]c2ccccc12': 18.03,
                  'NCCc1ccc(O)cc1': 25.83,
                  'C[C@]12CC[C@@H]3c4ccc(O)cc4CC[C@H]3[C@@H]1C[C@@H](O)[C@H]2O': 23.93,
                  'NC(CP(=O)(O)O)C(=O)O': 1.69,
                  'O=C(O)c1cccc(O)c1O': 16.31,
                  'O=C(O)Cc1cccc(O)c1': 16.72,
                  'CC(=O)N[C@@H](CCCCN)C(=O)O': 6.79,
                  'NC[C@H](O)CC[C@H](N)C(=O)O': 13.88,
                  'CC[C@H](N)C(=O)O': 9.13,
                  'NC(CSCC[C@H](N)C(=O)O)C(=O)O': [13.33, 13.61],
                  'C[C@H](O)[C@H](O)c1c[nH]c2nc(N)nc(=O)c-2n1': 6.03,
                  'O=c1[nH]cc(CO)c(=O)[nH]1': 8.87,
                  'CN(C)c1ncnc2nc[nH]c12': 18.56,
                  'Cn1cncc1C[C@H](N)C(=O)O': 2.01,
                  'CO=C(O)c1ccc(O)c(O)c1': 17.34,
                  'O=C(O)c1ccc(O)cc1': 17.57,
                  'N[C@@H](Cc1c[nH]c2ccc(O)cc12)C(=O)O': 20.29,
                  'N[C@@H](CCCC(=O)O)C(=O)O': 5.97,
                  'N=C(N)NCCC[C@H](N)C(=O)O': 2.44,
                  'CC[C@@H](C)[C@H](N)C(=O)O': 13.20,
                  'N[C@@H](CS)C(=O)O': 14.12,
                  'N[C@H]1[C@H](O)O[C@H](COS(=O)(=O)O)[C@@H](O)[C@@H]1O': 1.79,
                  'CNC[C@H](O)c1ccc(O)c(O)c1': [6.19, 7.20, 8.59],
                  'Nc1ccnc(=O)[nH]1': 7.58,
                  'NC(=O)CC[C@H](N)C(=O)O': 3.32,
                  'CC[C@@H](N)C(=O)O': 9.23,
                  'N[C@@H](Cc1ccc(Oc2ccc(O)cc2)cc1)C(=O)O': 25.44,
                  'O=C(O)Cc1ccccc1O': 16.42,
                  'N=C(N)NCCCC[C@H](N)C(=O)O': 3.00,
                  'NC(CCSSCC[C@H](N)C(=O)O)C(=O)O': 15.82,
                  'NC(=O)NCCCC[C@H](N)C(=O)O': 4.47,
                  'Nc1ccccc1C(=O)C[C@H](N)C(=O)O': [11.44, 11.97],
                  'CC(C)C[C@H](N)C(=O)O': 13.36,
                  'CSCC[C@H](N)C(=O)O': 10.89,
                  'Nc1nc(=O)c2ncc(=O)[nH]c2[nH]1': [9.55, 10.82],
                  'N[C@@H](CC(=O)O)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 10.07,
                  'O=C(O)CNC(=O)c1ccccc1': 7.07,
                  'O=C(O)[C@@H]1CCCCN1': 13.45,
                  'O=C(O)[C@H](CCO)NO': [4.05, 9.26],
                  'NCC(=O)N1CCC[C@H]1C(=O)O': 7.17,
                  'O=C(O)[C@@H]1C[C@@H](O)CN1': 5.17,
                  'O=C(O)/C=C/c1c[nH]c2ccccc12': 20.61,
                  'O=C(O)C(O)c1cccc(O)c1': [12.94, 21.64],
                  'O=C(O)C(O)Cc1ccc(O)cc1': 14.39,
                  'CC(C)C[C@H](NC(=O)CN)C(=O)O': 11.22,
                  'O=C(O)Cc1c[nH]c2ccc(O)cc12': 15.09,
                  'COc1cc(C(O)CN)ccc1O': 23.41,
                  'O=C(O)CNC(=O)c1ccccc1O': 11.05,
                  'O=C(O)c1cc(O)c2cccc(O)c2n1': [9.06, 26.34],
                  'CC(C)[C@H](N)C(=O)O': 10.81,
                  'Cc1cn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]c1=O': [5.85, 8.54, 9.39],
                  'Cn1cnc2[nH]c(N)nc(=O)c21': 10.32,
                  'NC(=O)NCCC[C@H](N)C(=O)O': 3.74,
                  'Nc1ncnc2c1ncn2[C@H]1C[C@H](O)[C@@H](COP(=O)(O)O)O1': 4.58,
                  'N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O': 11.44,
                  'Nc1ncnc2c1ncn2[C@@H]1O[C@H](CSCC[C@H](N)C(=O)O)[C@@H](O)[C@H]1O': 10.52,
                  'COc1cc(/C=C/C(=O)O)ccc1O': 18.47,
                  'COc1ccc(/C=C/C(=O)O)cc1O': 17.49,
                  'Oc1ccccc1O': 26.70,
                  'NCCS(=O)O': 2.47,
                  'Cc1cn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)nc1N': [2.94, 5.98],
                  'CCCCCCC(N)C(=O)O': 19.20,
                  'Nc1nc2c(ncn2[C@H]2C[C@H](O)[C@@H](COP(=O)(O)O)O2)c(=O)[nH]1': 5.57,
                  'N[C@@H](CCC(=O)N[C@@H](CS)C(=O)O)C(=O)O': 8.62,
                  'NCC(O)c1ccccc1': [10.77, 13.77],
                  'Nc1nc(Nc2ccccc2)nc2c1ncn2C1OC(CO)C(O)C1O': 8.73,
                  'Nc1ccccc1C(=O)O': 16.62,
                  'NCC(=O)CCC(=O)O': 7.59,
                  'Nc1ccc(O)cc1': [16.30, 25.04],
                  'CSC[C@H]1O[C@@H](n2cnc3c(N)ncnc32)[C@H](O)[C@@H]1O': 6.97,
                  'Nc1ccn([C@H]2C[C@H](O)[C@@H](COP(=O)(O)O)O2)c(=O)n1': 4.66,
                  'O=[N+]([O-])c1ccc(O)cc1': 23.45,
                  'CC(=O)NCCc1c[nH]c2ccc(O)cc12': 14.32,
                  'N[C@H]1[C@@H](O)O[C@H](COP(=O)(O)O)[C@@H](O)[C@@H]1O': 1.60,
                  'NCCCCNCCCN': 10.54,
                  'O=C(O)Cc1ccc(O)c(O)c1': 23.90,
                  'Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O': 1.49,
                  'N[C@@H](CCC[C@H](N)C(=O)O)C(=O)O': [12.30, 12.96],
                  'Nc1ccc(C(=O)O)cc1': 11.52,
                  'Nc1nc2c(ncn2[C@@H]2O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)[nH]1': 1.15,
                  'COc1ccccc1O': 22.54,
                  'C[N+](C)(C)CCOP(=O)(O)OP(=O)(O)OC[C@H]1O[C@@H](n2ccc(N)nc2=O)[C@H](O)[C@@H]1O': [1.48, 1.28],
                  'NCCCCN': 21.27,
                  'Cc1ncc(CO)c(CN)c1O': 19.47,
                  'N=C(N)NCCCCN': [4.52, 15.28],
                  'Nc1c(O)cccc1C(=O)O': 18.14,
                  'CNC(=N)N': [3.84, 22.52],
                  'c1c[nH]cn1': 14.29,
                  'Cc1ncc(CO)c(C=O)c1O': 12.01,
                  'CCCC[C@H](N)C(=O)O': 14.11,
                  'O=C(O)/C=C/c1cccc(O)c1': 18.51,
                  'Nc1nc(N)c2nc(CNc3ccc(C(=O)NC(CCC(=O)O)C(=O)O)cc3)cnc2n1': 6.06,
                  'N=C(N)N': 3.00,
                  'CC(C)NCC(O)COc1cccc2ccccc12': 24.95,
                  'OCCc1c[nH]c2ccc(O)cc12': 15.55,
                  'O=C(O)c1ccc(O)c(O)c1': 24.51,
                  'Cc1ccc(O)cc1': 24.54,
                  'CC(=O)Nc1ccc(O)cc1': 16.35,
                  'Cn1cncc1CCN': 3.27,
                  'O=C(O)C(O)c1ccc(O)c(O)c1': 21.73,
                  'Nc1ccc(C(=O)NCC(=O)O)cc1': 8.38,
                  'COc1ccc(O)c(C(=O)O)c1': 16.38,
                  'NC(Cc1ccc(O)c(Cl)c1)C(=O)O': 23.57,
                  'CN1C2=C(NC=N2)C(=O)N(C)C1=O': 15.42,
                  'Nc1cccc(C(=O)O)c1': 11.76,
                  'COC(=O)[C@H](Cc1ccccc1)NC(=O)[C@@H](N)CC(=O)O': 13.72,
                  'O=C(O)c1ccccc1O': 15.62,
                  'NCCCCCC(=O)O': 10.21,
                  'N[C@@H](Cc1ccc(O)c([N+](=O)[O-])c1)C(=O)O': [22.61, 22.61],
                  'CC(C)(N)C(=O)O': 8.91,
                  'NCCCC(O)(P(=O)(O)O)P(=O)(O)O': 1.59,
                  'N[C@@H](Cc1cc(I)c(Oc2cc(I)c(O)c(I)c2)c(I)c1)C(=O)O': 27.74,
                  'CC(C)NCC(O)COc1ccc(CC(N)=O)cc1': 11.91,
                  'COCCc1ccc(OCC(O)CNC(C)C)cc1': 22.09,
                  'CC(C)(C)NCC(O)c1ccc(O)c(CO)c1': [8.27, 8.42],
                  'NCCCC[C@H](N[C@@H](CCc1ccccc1)C(=O)O)C(=O)N1CCC[C@H]1C(=O)O': 7.68,
                  'C[C@@H](N)[C@@H](O)c1ccccc1': 15.13,
                  'CN[C@@H](C)[C@@H](O)c1ccccc1': 19.38,
                  'O=C(O)/C=C/c1ccc(O)c(O)c1': 24.64,
                  'Nc1cccc(C(=O)O)c1O': 12.22,
                  'CS(=O)CC[C@H](N)C(=O)O': [3.72, 4.20],
                  'NC[C@H](N)C(=O)O': 15.65,
                  'CC(N)c1ccccc1': 18.63,
                  'O=C(O)Cc1cnc[nH]1': 11.12,
                  'Cc1cccc(O)c1': 24.44,
                  'Cc1ccccc1O': 24.60,
                  'CC(=O)NCCCCN': 7.25,
                  'COc1cc(C(=O)O)cc(OC)c1O': 18.10,
                  'CNc1ncnc2nc[nH]c12': [12.22, 12.74],
                  'CSC[C@@H](N)C(=O)O': 9.37,
                  'Nc1cc(=O)nc(N)[nH]1': 8.95,
                  'CNC(C)(C)C(=O)O': 13.65,
                  'CNC[C@H](O)c1cccc(O)c1': 25.39,
                  'O=C(O)CCc1ccc(O)cc1': 18.04,
                  'N[C@@H](CCS(=O)(=O)O)C(=O)O': 1.64,
                  'NC(C(=O)O)c1ccccc1': 11.69,
                  'NCCCCCN': 22.39,
                  'COc1ccc2[nH]cc(C[C@H](N)C(=O)O)c2c1': 9.79,
                  'NCCC(N)C(=O)O': 15.80,
                  'Cc1cccc(C(=O)O)c1O': 16.80,
                  'CN[C@H](CC(=O)O)C(=O)O': 7.53,
                  'O=C(O)c1ccc(O)nc1': [12.21, 15.32],
                  'O=C1C[C@@H](c2ccc(O)cc2)Oc2cc(O)cc(O)c21': 15.29,
                  'N=C(N)NOCC[C@H](N)C(=O)O': [11.37, 11.59],
                  'NCCS': 15.08,
                  'Nc1ccccc1': 17.32,
                  'N[C@@H](CCCCNC(=O)CCCC[C@@H]1SC[C@@H]2NC(=O)N[C@H]12)C(=O)O': 6.72,
                  'N=C(N)N[C@@H](CC(=O)O)C(=O)O': 2.81,
                  'O=C(/C=C/c1ccc(O)c(O)c1)O[C@@H]1C[C@](O)(C(=O)O)C[C@@H](O)[C@H]1O': [19.45, 21.24],
                  'Cn1c(N)nc2nc[nH]c2c1=O': 9.57,
                  'O=C(O)c1c[nH]c2ccccc12': 19.27,
                  'CN=C(NC)NCCCC(N)C(=O)O': 3.05,
                  'N[C@@H](CCC(=O)N[C@@H](CSSC[C@H](NC(=O)CC[C@H](N)C(=O)O)C(=O)NCC(=O)O)C(=O)NCC(=O)O)C(=O)O': 8.07,
                  'NO': 12.02,
                  'NCCCCC(=O)O': 8.68,
                  'NC(=O)CC[C@@H](N)C(=O)O': 3.32,
                  'N[C@H](CO)Cc1c[nH]cn1': 1.44,
                  'N=C(N)NCCCC(=O)O': [3.65, 11.00],
                  'N[C@@H](Cc1cc(I)c(O)c(I)c1)C(=O)O': [11.82, 24.18],
                  'CC(C)[C@@H](N)CC(=O)O': [10.78, 20.77],
                  'CC(CN)C(=O)O': [8.67, 16.29],
                  'COc1ccc2[nH]cc(CCN)c2c1': 16.52,
                  'NC(C[Se][Se]CC(N)C(=O)O)C(=O)O': 15.09,
                  'OCCNCCO': 5.49,
                  'Oc1ccc(Cl)cc1Cl': 26.30,
                  'Cc1cc(C(=O)O)ccc1O': 19.43,
                  'NCCCC[C@H](NC(=O)[C@@H](N)CC(=O)O)C(=O)O': 13.61,
                  'CCOC(=O)c1ccc(N)cc1': 20.08,
                  'NC(Cc1ccccc1O)C(=O)O': 22.38,
                  'N[C@@H](Cc1ccccc1)C(=O)N1CCC[C@H]1C(=O)O': 13.13,
                  'N[C@@H](CCC(=O)N[C@@H](CCC(=O)O)C(=O)O)C(=O)O': 3.44,
                  'CC(C)C[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 16.59,
                  'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 16.55,
                  'C[C@H](N)C(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O': 17.62,
                  'CC(C)C[C@H](NC(=O)[C@H](C)N)C(=O)O': 11.36,
                  'C[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 12.11,
                  'C[C@H](N)C(=O)N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O': 11.09,
                  'C[C@H](N)C(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': 21.85,
                  'N=C(N)NCCC[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 6.80,
                  'CCC(C)C(N=C(O)CN)C(=O)O': 10.78,
                  'NCC(O)=NC(Cc1ccccc1)C(=O)O': 11.65,
                  'NCC(=O)NC(Cc1c[nH]c2ccccc12)C(=O)O': 11.19,
                  'NCC(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': 21.63,
                  'CC(C)[C@H](NC(=O)CN)C(=O)O': 9.19,
                  'C[C@H](NC(=O)[C@@H](N)Cc1cnc[nH]1)C(=O)O': 16.69,
                  'CC(C)C[C@H](N)C(=O)N1CCC[C@H]1C(=O)O': 12.99,
                  'CC(C)CC(N)C(O)=NC(Cc1c[nH]c2ccccc12)C(=O)O': 15.77,
                  'CC(C)CC(N)C(=O)NC(Cc1ccc(O)cc1)C(=O)O': 23.98,
                  'C[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': 10.58,
                  'N[C@@H](Cc1ccccc1)C(=O)NCC(=O)O': 9.43,
                  'CSCC[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': 13.87,
                  'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': 24.22,
                  'CC(C)[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': 13.62,
                  'CC(C)C[C@H](NC(=O)[C@@H](N)CO)C(=O)O': 8.90,
                  'N[C@@H](CO)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 9.38,
                  'CC(C)C[C@H](NC(=O)[C@@H](N)[C@@H](C)O)C(=O)O': 10.18,
                  'NC(Cc1c[nH]c2ccccc12)C(=O)NC(CCC(=O)O)C(=O)O': 8.29,
                  'CC(C)CC(N=C(O)C(N)Cc1c[nH]c2ccccc12)C(=O)O': 14.60,
                  'NC(Cc1c[nH]c2ccccc12)C(=O)NC(Cc1ccccc1)C(=O)O': 15.36,
                  'NC(Cc1c[nH]c2ccccc12)C(=O)NC(Cc1ccc(O)cc1)C(=O)O': 23.25,
                  'CC(NC(=O)C(N)Cc1ccc(O)cc1)C(=O)O': 20.86,
                  'N[C@@H](Cc1ccc(O)cc1)C(=O)NCC(=O)O': 20.19,
                  'CC(C)CC(N=C(O)C(N)Cc1ccc(O)cc1)C(=O)O': 23.77,
                  'CC(C)C(N=C(O)C(N)Cc1ccc(O)cc1)C(=O)O': 22.83,
                  'CCc1ccc(O)cc1': 25.63,
                  'O=C(O)c1ccc(O)c(O)c1O': 24.10,
                  'COc1cc(O)cc(OC)c1': 23.75,
                  'COc1ccc(C(=O)O)cc1O': 15.69,
                  'NCC(=O)NCC(=O)NCC(=O)NCC(=O)O': 3.39,
                  'N[C@@H](Cc1c[nH]c2ccccc12)C(=O)NCC(=O)NCC(=O)O': 7.60,
                  'CCCC(NC(=O)CN)C(=O)O': 9.51,
                  'CCCCC(NC(=O)CN)C(=O)O': 11.36,
                  'CC(C)C[C@H](Nc1ccccc1)C(=O)O': 15.90,
                  'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 19.95}
        smi_enter2 = self.plainTextEdit.text()
        mol_enter2 = Chem.MolFromSmiles(smi_enter2)
        smi2 = Chem.MolToSmiles(mol_enter2)
        print(smi2)
        exp = exp_rt[smi2]
        pred_rt = {'Cn1cnc(C[C@H](N)C(=O)O)c1': 3.48,
                   'NCCCN': [3.5, 19.66],
                   'O=C(O)Cc1ccc(O)cc1': 17.99,
                   'N[C@@H](Cc1ccc(O)c(I)c1)C(=O)O': 19.8,
                   'COc1cc(CCN)ccc1O': 23.33,
                   'Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]1O': 3.84,
                   'Nc1ncnc2c1ncn2[C@@H]1O[C@H](CO)[C@@H](O)[C@H]1O': 4.32,
                   'N': 6.8,
                   'NCCC(=O)O': 8.21,
                   'CN(CC(O)=O)C(N)=N': 3.7,
                   'O=C(O)C1CCCCN1': 13.74,
                   'Nc1nc2c(ncn2[C@H]2C[C@H](O)[C@@H](CO)O2)c(=O)[nH]1': 8.9,
                   'CNC': 12.61,
                   'Nc1ccn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)n1': [4.21, 7.62],
                   'Nc1ccn([C@@H]2O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)n1': [3.59, 3.85],
                   'N[C@@H](CCSC[C@H](N)C(=O)O)C(=O)O': [13.79, 13.83],
                   'Nc1ncnc2c1ncn2[C@H]1C[C@H](O)[C@@H](CO)O1': 8.12,
                   'NCCCC(=O)O': [7.89, 15.54],
                   'COc1cc(CC(=O)O)ccc1O': 17.05,
                   'NCC(=O)O': 7.94,
                   'N=C(N)NCC(=O)O': 3.84,
                   'O=C(O)Cc1cc(O)ccc1O': 21.97,
                   'Nc1nc2c(ncn2[C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]1': 4.44,
                   'N[C@@H](CCC(=O)O)C(=O)O': [6.24, 9.59],
                   'NCCO': 5.92,
                   'O=C(O)c1cc(O)ccc1O': [18.7, 22.3],
                   'C[C@]12CC[C@@H]3c4ccc(O)cc4CC[C@H]3[C@@H]1C[C@@H](O)[C@@H]2O': 22.76,
                   'Oc1ncnc2nc[nH]c12': [3.77, 9.23, 9.59],
                   'N[C@@H](Cc1ccc(O)cc1)C(=O)O': 20.88, 
                   'N[C@@H](Cc1ccccc1)C(=O)O': 13.33,
                   'C[C@H](N)C(=O)O': 8.85,
                   'O=C(O)[C@@H]1CCCN1': 11.37,
                   'CN': 8.63,
                   'C[C@@H](O)[C@H](N)C(=O)O': 4.56,
                   'NC(=O)C[C@H](N)C(=O)O': [4.05, 6.68],
                   'CC[C@H](C)[C@H](N)C(=O)O': 13.47,
                   'N[C@@H](Cc1cnc[nH]1)C(=O)O': 16.53,
                   'NCCCC[C@H](N)C(=O)O': 16.65,
                   'N[C@@H](CO)C(=O)O': 4.23,
                   'N[C@@H](CC(=O)O)C(=O)O': 4.93,
                   'N[C@@H](CSSC[C@H](N)C(=O)O)C(=O)O': 14.36,
                   'CC(=O)NCCCC[C@H](N)C(=O)O': 6.31,
                   'CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)O': 9.18,
                   'NCCC[C@H](N)C(=O)O': 16.39,
                   'NCCOP(=O)(O)O': 3.31,
                   'Oc1ccccc1': 21.79,
                   'C[C@H](O)C(=O)C1=Nc2c([nH]c(N)nc2=O)NC1': 10.62,
                   'Cc1ncc(CO)c(CO)c1O': [10.47, 17.35],
                   'NCCS(=O)(=O)O': 2.87,
                   'NCCc1c[nH]c2ccc(O)cc12': 21.41,
                   'Cc1c[nH]c(=O)[nH]c1=O': 13.21,
                   'N[C@@H](Cc1cc(I)c(Oc2ccc(O)c(I)c2)c(I)c1)C(=O)O': 21.68,
                   'CNCC(=O)O': 9.1,
                   'N[C@@H](CCCCN[C@@H](CCC(=O)O)C(=O)O)C(=O)O': [3.25, 5.56],
                   'COc1cc([C@H](O)C(=O)O)ccc1O': [14.11, 21.62],
                   'O=c1[nH]c(=O)c2[nH]cnc2[nH]1': 9.42,
                   'O=c1ccn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]1': [7.78, 9.48],
                   'O=c1cc[nH]c(=O)[nH]1': 11.33,
                   'O=C(O)/C=C/c1c[nH]cn1': 13.54,
                   'NCCc1c[nH]c2ccccc12': 17.04,
                   'NCCc1ccc(O)cc1': 23.1,
                   'C[C@]12CC[C@@H]3c4ccc(O)cc4CC[C@H]3[C@@H]1C[C@@H](O)[C@H]2O': 22.76,
                   'NC(CP(=O)(O)O)C(=O)O': 2.53,
                   'O=C(O)c1cccc(O)c1O': 18.09,
                   'O=C(O)Cc1cccc(O)c1': 16.39,
                   'CC(=O)N[C@@H](CCCCN)C(=O)O': 6.05,
                   'NC[C@H](O)CC[C@H](N)C(=O)O': 13.8,
                   'CC[C@H](N)C(=O)O': 9.87,
                   'NC(CSCC[C@H](N)C(=O)O)C(=O)O': [13.79, 13.83],
                   'C[C@H](O)[C@H](O)c1c[nH]c2nc(N)nc(=O)c-2n1': 6.9,
                   'O=c1[nH]cc(CO)c(=O)[nH]1': 9.17,
                   'CN(C)c1ncnc2nc[nH]c12': 17.64,
                   'Cn1cncc1C[C@H](N)C(=O)O': 3.61,
                   'CO=C(O)c1ccc(O)c(O)c1': 16.88,
                   'O=C(O)c1ccc(O)cc1': 17.11,
                   'N[C@@H](Cc1c[nH]c2ccc(O)cc12)C(=O)O': 18.99,
                   'N[C@@H](CCCC(=O)O)C(=O)O': 6.34,
                   'N=C(N)NCCC[C@H](N)C(=O)O': 3.78,
                   'CC[C@@H](C)[C@H](N)C(=O)O': 13.47,
                   'N[C@@H](CS)C(=O)O': 14.41,
                   'N[C@H]1[C@H](O)O[C@H](COS(=O)(=O)O)[C@@H](O)[C@@H]1O': 2.32,
                   'CNC[C@H](O)c1ccc(O)c(O)c1': [6.51, 7.14, 8.94],
                   'Nc1ccnc(=O)[nH]1': 9.59,
                   'NC(=O)CC[C@H](N)C(=O)O': 4.32,
                   'CC[C@@H](N)C(=O)O': 9.87,
                   'N[C@@H](Cc1ccc(Oc2ccc(O)cc2)cc1)C(=O)O': 20.93,
                   'O=C(O)Cc1ccccc1O': 16.28,
                   'N=C(N)NCCCC[C@H](N)C(=O)O': 3.76,
                   'NC(CCSSCC[C@H](N)C(=O)O)C(=O)O': 14.85,
                   'NC(=O)NCCCC[C@H](N)C(=O)O': 3.6,
                   'Nc1ccccc1C(=O)C[C@H](N)C(=O)O': [12.02, 13.1],
                   'CC(C)C[C@H](N)C(=O)O': 13.11,
                   'CSCC[C@H](N)C(=O)O': 11.47,
                   'Nc1nc(=O)c2ncc(=O)[nH]c2[nH]1': [10.02, 11.06],
                   'N[C@@H](CC(=O)O)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 10,
                   'O=C(O)CNC(=O)c1ccccc1': 10.29,
                   'O=C(O)[C@@H]1CCCCN1': 13.74,
                   'O=C(O)[C@H](CCO)NO': [4.18, 10.92],
                   'NCC(=O)N1CCC[C@H]1C(=O)O': 7.72,
                   'O=C(O)[C@@H]1C[C@@H](O)CN1': 5.79,
                   'O=C(O)/C=C/c1c[nH]c2ccccc12': 19.36,
                   'O=C(O)C(O)c1cccc(O)c1': [14.92, 22.06],
                   'O=C(O)C(O)Cc1ccc(O)cc1': 16.27,
                   'CC(C)C[C@H](NC(=O)CN)C(=O)O': 11.32,
                   'O=C(O)Cc1c[nH]c2ccc(O)cc12': 17.36,
                   'COc1cc(C(O)CN)ccc1O': 21.1,
                   'O=C(O)CNC(=O)c1ccccc1O': 12.11,
                   'O=C(O)c1cc(O)c2cccc(O)c2n1': [15.72, 21.67],
                   'CC(C)[C@H](N)C(=O)O': 11.62,
                   'Cc1cn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]c1=O': [5.24, 8, 10.12],
                   'Cn1cnc2[nH]c(N)nc(=O)c21': 10.11,
                   'NC(=O)NCCC[C@H](N)C(=O)O': 3.7,
                   'Nc1ncnc2c1ncn2[C@H]1C[C@H](O)[C@@H](COP(=O)(O)O)O1': 3.76,
                   'N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O': 12.12,
                   'Nc1ncnc2c1ncn2[C@@H]1O[C@H](CSCC[C@H](N)C(=O)O)[C@@H](O)[C@H]1O': 11.88,
                   'COc1cc(/C=C/C(=O)O)ccc1O': 18.91,
                   'COc1ccc(/C=C/C(=O)O)cc1O': 18.65,
                   'Oc1ccccc1O': 24.46,
                   'NCCS(=O)O': 3.56,
                   'Cc1cn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)nc1N': [4.14, 4.68],
                   'CCCCCCC(N)C(=O)O': 18.73,
                   'Nc1nc2c(ncn2[C@H]2C[C@H](O)[C@@H](COP(=O)(O)O)O2)c(=O)[nH]1': 4.16,
                   'N[C@@H](CCC(=O)N[C@@H](CS)C(=O)O)C(=O)O': 6.19,
                   'NCC(O)c1ccccc1': [11.51, 14.43],
                   'Nc1nc(Nc2ccccc2)nc2c1ncn2C1OC(CO)C(O)C1O': 8.84,
                   'Nc1ccccc1C(=O)O': 13.87,
                   'NCC(=O)CCC(=O)O': 7.47,
                   'Nc1ccc(O)cc1': [16.8, 23.08],
                   'CSC[C@H]1O[C@@H](n2cnc3c(N)ncnc32)[C@H](O)[C@@H]1O': 7.61,
                   'Nc1ccn([C@H]2C[C@H](O)[C@@H](COP(=O)(O)O)O2)c(=O)n1': 3.6,
                   'O=[N+]([O-])c1ccc(O)cc1': 22.68,
                   'CC(=O)NCCc1c[nH]c2ccc(O)cc12': 15.8,
                   'N[C@H]1[C@@H](O)O[C@H](COP(=O)(O)O)[C@@H](O)[C@@H]1O': 3.31,
                   'NCCCCNCCCN': 9.83,
                   'O=C(O)Cc1ccc(O)c(O)c1': 22.18,
                   'Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O': 3.08,
                   'N[C@@H](CCC[C@H](N)C(=O)O)C(=O)O': [13.67, 13.76],
                   'Nc1ccc(C(=O)O)cc1': 12.65,
                   'Nc1nc2c(ncn2[C@@H]2O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)[nH]1': 3.84,
                   'COc1ccccc1O': 22.12,
                   'C[N+](C)(C)CCOP(=O)(O)OP(=O)(O)OC[C@H]1O[C@@H](n2ccc(N)nc2=O)[C@H](O)[C@@H]1O': [3.13, 3.41],
                   'NCCCCN': 19.72,
                   'Cc1ncc(CO)c(CN)c1O': 19.07,
                   'N=C(N)NCCCCN': [3.7, 13.96],
                   'Nc1c(O)cccc1C(=O)O': 15.2,
                   'CNC(=N)N': [4.28, 19.84],
                   'c1c[nH]cn1': 15.61,
                   'Cc1ncc(CO)c(C=O)c1O': 12.87,
                   'CCCC[C@H](N)C(=O)O': 14.06,
                   'O=C(O)/C=C/c1cccc(O)c1': 19.55,
                   'Nc1nc(N)c2nc(CNc3ccc(C(=O)NC(CCC(=O)O)C(=O)O)cc3)cnc2n1': 7.69,
                   'N=C(N)N': 3.91,
                   'CC(C)NCC(O)COc1cccc2ccccc12': 22.58,
                   'OCCc1c[nH]c2ccc(O)cc12': 17.21,
                   'O=C(O)c1ccc(O)c(O)c1': 22.21,
                   'Cc1ccc(O)cc1': 24.8,
                   'CC(=O)Nc1ccc(O)cc1': 17.85,
                   'Cn1cncc1CCN': 3.44,
                   'O=C(O)C(O)c1ccc(O)c(O)c1': 19.87,
                   'Nc1ccc(C(=O)NCC(=O)O)cc1': 9.39,
                   'COc1ccc(O)c(C(=O)O)c1': 17.22,
                   'NC(Cc1ccc(O)c(Cl)c1)C(=O)O': 20.12,
                   'CN1C2=C(NC=N2)C(=O)N(C)C1=O': 15.43,
                   'Nc1cccc(C(=O)O)c1': 12.44,
                   'COC(=O)[C@H](Cc1ccccc1)NC(=O)[C@@H](N)CC(=O)O': 12.4,
                   'O=C(O)c1ccccc1O': 16.61,
                   'NCCCCCC(=O)O': 11.43,
                   'N[C@@H](Cc1ccc(O)c([N+](=O)[O-])c1)C(=O)O': [19.75, 21.06],
                   'CC(C)(N)C(=O)O': 9.58,
                   'NCCCC(O)(P(=O)(O)O)P(=O)(O)O': 3.2,
                   'N[C@@H](Cc1cc(I)c(Oc2cc(I)c(O)c(I)c2)c(I)c1)C(=O)O': 23.44,
                   'CC(C)NCC(O)COc1ccc(CC(N)=O)cc1': 11,
                   'COCCc1ccc(OCC(O)CNC(C)C)cc1': 21.87,
                   'CC(C)(C)NCC(O)c1ccc(O)c(CO)c1': [8.35, 8.92],
                   'NCCCC[C@H](N[C@@H](CCc1ccccc1)C(=O)O)C(=O)N1CCC[C@H]1C(=O)O': 8.04,
                   'C[C@@H](N)[C@@H](O)c1ccccc1': 14.98,
                   'CN[C@@H](C)[C@@H](O)c1ccccc1': 18.79,
                   'O=C(O)/C=C/c1ccc(O)c(O)c1': 23.78,
                   'Nc1cccc(C(=O)O)c1O': 12.81,
                   'CS(=O)CC[C@H](N)C(=O)O': [4.51, 4.41],
                   'NC[C@H](N)C(=O)O': 15.2,
                   'CC(N)c1ccccc1': 19.07,
                   'O=C(O)Cc1cnc[nH]1': 12.12,
                   'Cc1cccc(O)c1': 23.59,
                   'Cc1ccccc1O': 24.36,
                   'CC(=O)NCCCCN': 8.12,
                   'COc1cc(C(=O)O)cc(OC)c1O': 18.35,
                   'CNc1ncnc2nc[nH]c12': [12.23, 13.12],
                   'CSC[C@@H](N)C(=O)O': 10.31,
                   'Nc1cc(=O)nc(N)[nH]1': 8.84,
                   'CNC(C)(C)C(=O)O': 12.27,
                   'CNC[C@H](O)c1cccc(O)c1': 23.28,
                   'O=C(O)CCc1ccc(O)cc1': 18.82,
                   'N[C@@H](CCS(=O)(=O)O)C(=O)O': 2.43,
                   'NC(C(=O)O)c1ccccc1': 12.62,
                   'NCCCCCN': 19.88,
                   'COc1ccc2[nH]cc(C[C@H](N)C(=O)O)c2c1': 11.49,
                   'NCCC(N)C(=O)O': 15.93,
                   'Cc1cccc(C(=O)O)c1O': 17.78,
                   'CN[C@H](CC(=O)O)C(=O)O': 7.03,
                   'O=C(O)c1ccc(O)nc1': [13.29, 15.65],
                   'O=C1C[C@@H](c2ccc(O)cc2)Oc2cc(O)cc(O)c21': 20.11,
                   'N=C(N)NOCC[C@H](N)C(=O)O': [10.7, 11.09],
                   'NCCS': 16.07,
                   'Nc1ccccc1': 16.83,
                   'N[C@@H](CCCCNC(=O)CCCC[C@@H]1SC[C@@H]2NC(=O)N[C@H]12)C(=O)O': 6.76,
                   'N=C(N)N[C@@H](CC(=O)O)C(=O)O': 3.5,
                   'O=C(/C=C/c1ccc(O)c(O)c1)O[C@@H]1C[C@](O)(C(=O)O)C[C@@H](O)[C@H]1O': [20.44, 22.18],
                   'Cn1c(N)nc2nc[nH]c2c1=O': 9.87,
                   'O=C(O)c1c[nH]c2ccccc12': 17.89,
                   'CN=C(NC)NCCCC(N)C(=O)O': 3.64,
                   'N[C@@H](CCC(=O)N[C@@H](CSSC[C@H](NC(=O)CC[C@H](N)C(=O)O)C(=O)NCC(=O)O)C(=O)NCC(=O)O)C(=O)O': 8.8,
                   'NO': 12.16,
                   'NCCCCC(=O)O': 7.97,
                   'NC(=O)CC[C@@H](N)C(=O)O': 4.32,
                   'N[C@H](CO)Cc1c[nH]cn1': 3.36,
                   'N=C(N)NCCCC(=O)O': [3.94, 10.57],
                   'N[C@@H](Cc1cc(I)c(O)c(I)c1)C(=O)O': [12.47, 21.65],
                   'CC(C)[C@@H](N)CC(=O)O': [12.17, 20.99],
                   'CC(CN)C(=O)O': [8.9, 16.8],
                   'COc1ccc2[nH]cc(CCN)c2c1': 16.67,
                   'NC(C[Se][Se]CC(N)C(=O)O)C(=O)O': 14,
                   'OCCNCCO': 6.55,
                   'Oc1ccc(Cl)cc1Cl': 24.16,
                   'Cc1cc(C(=O)O)ccc1O': 18.96,
                   'NCCCC[C@H](NC(=O)[C@@H](N)CC(=O)O)C(=O)O': 13.28,
                   'CCOC(=O)c1ccc(N)cc1': 18.26,
                   'NC(Cc1ccccc1O)C(=O)O': 20.66,
                   'N[C@@H](Cc1ccccc1)C(=O)N1CCC[C@H]1C(=O)O': 12.84,
                   'N[C@@H](CCC(=O)N[C@@H](CCC(=O)O)C(=O)O)C(=O)O': 3.3,
                   'CC(C)C[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 16.74,
                   'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 16.42,
                   'C[C@H](N)C(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O': 18.23,
                   'CC(C)C[C@H](NC(=O)[C@H](C)N)C(=O)O': 11.33,
                   'C[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 12.1,
                   'C[C@H](N)C(=O)N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O': 11.55,
                   'C[C@H](N)C(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': 19.11,
                   'N=C(N)NCCC[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 7.09,
                   'CCC(C)C(N=C(O)CN)C(=O)O': 11.17,
                   'NCC(O)=NC(Cc1ccccc1)C(=O)O': 12.09,
                   'NCC(=O)NC(Cc1c[nH]c2ccccc12)C(=O)O': 11.58,
                   'NCC(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': 18.9,
                   'CC(C)[C@H](NC(=O)CN)C(=O)O': 10.01,
                   'C[C@H](NC(=O)[C@@H](N)Cc1cnc[nH]1)C(=O)O': 16.7,
                   'CC(C)C[C@H](N)C(=O)N1CCC[C@H]1C(=O)O': 13.26,
                   'CC(C)CC(N)C(O)=NC(Cc1c[nH]c2ccccc12)C(=O)O': 16.56,
                   'CC(C)CC(N)C(=O)NC(Cc1ccc(O)cc1)C(=O)O': 21.06,
                   'C[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': 11.01,
                   'N[C@@H](Cc1ccccc1)C(=O)NCC(=O)O': 8.96,
                   'CSCC[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': 14.54,
                   'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': 21.07,
                   'CC(C)[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': 14.48,
                   'CC(C)C[C@H](NC(=O)[C@@H](N)CO)C(=O)O': 9.24,
                   'N[C@@H](CO)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 9.84,
                   'CC(C)C[C@H](NC(=O)[C@@H](N)[C@@H](C)O)C(=O)O': 10.46,
                   'NC(Cc1c[nH]c2ccccc12)C(=O)NC(CCC(=O)O)C(=O)O': 9.86,
                   'CC(C)CC(N=C(O)C(N)Cc1c[nH]c2ccccc12)C(=O)O': 15.54,
                   'NC(Cc1c[nH]c2ccccc12)C(=O)NC(Cc1ccccc1)C(=O)O': 16.18,
                   'NC(Cc1c[nH]c2ccccc12)C(=O)NC(Cc1ccc(O)cc1)C(=O)O': 21.89,
                   'CC(NC(=O)C(N)Cc1ccc(O)cc1)C(=O)O': 19.05,
                   'N[C@@H](Cc1ccc(O)cc1)C(=O)NCC(=O)O': 18.88,
                   'CC(C)CC(N=C(O)C(N)Cc1ccc(O)cc1)C(=O)O': 21.4,
                   'CC(C)C(N=C(O)C(N)Cc1ccc(O)cc1)C(=O)O': 20.55,
                   'CCc1ccc(O)cc1': 24.64,
                   'O=C(O)c1ccc(O)c(O)c1O': 22.74,
                   'COc1cc(O)cc(OC)c1': 23.4,
                   'COc1ccc(C(=O)O)cc1O': 17.1,
                   'NCC(=O)NCC(=O)NCC(=O)NCC(=O)O': 3.31,
                   'N[C@@H](Cc1c[nH]c2ccccc12)C(=O)NCC(=O)NCC(=O)O': 7.95,
                   'CCCC(NC(=O)CN)C(=O)O': 9.6,
                   'CCCCC(NC(=O)CN)C(=O)O': 11.57,
                   'CC(C)C[C@H](Nc1ccccc1)C(=O)O': 17.29,
                   'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 18.48
                   }
        pred = pred_rt[smi2]

        Dns_struct = {'Cn1cnc(C[C@H](N)C(=O)O)c1': 'Dnspng/1-Methylhistidine.png',
                      'NCCCN': ['Dnspng/1,3-Diaminopropane.png', 'Dnspng/1,3-Diaminopropane_multi_tags.png'],
                      'O=C(O)Cc1ccc(O)cc1': 'Dnspng/p-Hydroxyphenylacetic_acid.png',
                      'N[C@@H](Cc1ccc(O)c(I)c1)C(=O)O': 'Dnspng/Iodotyrosine.png',
                      'COc1cc(CCN)ccc1O': 'Dnspng/3-Methoxytyramine.png',
                      'Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]1O': 'Dnspng/Adenosine_monophosphate.png',
                      'Nc1ncnc2c1ncn2[C@@H]1O[C@H](CO)[C@@H](O)[C@H]1O': 'Dnspng/Adenosine.png',
                      'N': 'Dnspng/Ammonia.png',
                      'NCCC(=O)O': 'Dnspng/Beta-Alanine.png',
                      'CN(CC(O)=O)C(N)=N': 'Dnspng/Creatine.png',
                      'O=C(O)C1CCCCN1': 'Dnspng/D-Pipecolic_acid.png',
                      'Nc1nc2c(ncn2[C@H]2C[C@H](O)[C@@H](CO)O2)c(=O)[nH]1': 'Dnspng/Deoxyguanosine.png',
                      'CNC': 'Dnspng/Dimethylamine.png',
                      'Nc1ccn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)n1': ['Dnspng/Cytidine.png',
                                                                           'Dnspng/Cytidine-H2O.png'],
                      'Nc1ccn([C@@H]2O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)n1': [
                          'Dnspng/Cytidine_monophosphate.png', 'Dnspng/Cytidine_monophosphate_Isomer.png'],
                      'N[C@@H](CCSC[C@H](N)C(=O)O)C(=O)O': ['Dnspng/L-Cystathionine.png',
                                                            'Dnspng/L-Cystathionine_Isomer.png'],
                      'Nc1ncnc2c1ncn2[C@H]1C[C@H](O)[C@@H](CO)O1': 'Dnspng/Deoxyadenosinee.png',
                      'NCCCC(=O)O': ['Dnspng/Gamma-Aminobutyric_acid.png',
                                     'Dnspng/Gamma-Aminobutyric_acid-H2O.png'],
                      'COc1cc(CC(=O)O)ccc1O': 'Dnspng/Homovanillic_acid.png',
                      'NCC(=O)O': 'Dnspng/Glycine.png',
                      'N=C(N)NCC(=O)O': 'Dnspng/Guanidoacetic_acid.png',
                      'O=C(O)Cc1cc(O)ccc1O': 'Dnspng/Homogentisic_acid.png',
                      'Nc1nc2c(ncn2[C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]1': 'Dnspng/Guanosine.png',
                      'N[C@@H](CCC(=O)O)C(=O)O': ['Dnspng/L-Glutamic_Acid.png', 'Dnspng/L-Glutamic_Acid-H2O.png'],
                      'NCCO': 'Dnspng/Ethanolamine.png',
                      'O=C(O)c1cc(O)ccc1O': ['Dnspng/Gentisic_acid.png', 'Dnspng/Gentisic_acid_multi_tags.png'],
                      'C[C@]12CC[C@@H]3c4ccc(O)cc4CC[C@H]3[C@@H]1C[C@@H](O)[C@@H]2O': 'Dnspng/Estriol.png',
                      'Oc1ncnc2nc[nH]c12': ['Dnspng/Hypoxanthine+H2O.png', 'Dnspng/Hypoxanthine_multi_tags.png',
                                            'Dnspng/Hypoxanthine_Isomer.png'],
                      'N[C@@H](Cc1ccc(O)cc1)C(=O)O': 'Dnspng/L-Tyrosine.png',
                      'N[C@@H](Cc1ccccc1)C(=O)O': 'Dnspng/L-Phenylalanine.png',
                      'C[C@H](N)C(=O)O': 'Dnspng/L-Alanine.png',
                      'O=C(O)[C@@H]1CCCN1': 'Dnspng/L-Proline.png',
                      'CN': 'Dnspng/Methylamine.png',
                      'C[C@@H](O)[C@H](N)C(=O)O': 'Dnspng/L-Threonine.png',
                      'NC(=O)C[C@H](N)C(=O)O': ['Dnspng/L-Asparagine.png', 'Dnspng/L-Asparagine-H2O.png'],
                      'CC[C@H](C)[C@H](N)C(=O)O': 'Dnspng/L-Isoleucine.png',
                      'N[C@@H](Cc1cnc[nH]1)C(=O)O': 'Dnspng/L-Histidine.png',
                      'NCCCC[C@H](N)C(=O)O': 'Dnspng/L-Lysine.png',
                      'N[C@@H](CO)C(=O)O': 'Dnspng/L-Serine.png',
                      'N[C@@H](CC(=O)O)C(=O)O': 'Dnspng/L-Aspartic_Acid.png',
                      'N[C@@H](CSSC[C@H](N)C(=O)O)C(=O)O': 'Dnspng/L-Cystine.png',
                      'CC(=O)NCCCC[C@H](N)C(=O)O': 'Dnspng/N6-Acetyl-L-Lysine.png',
                      'CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)O': 'Dnspng/Pantothenic_acid.png',
                      'NCCC[C@H](N)C(=O)O': 'Dnspng/Ornithine.png',
                      'NCCOP(=O)(O)O': 'Dnspng/O-Phosphoethanolamine.png',
                      'Oc1ccccc1': 'Dnspng/Phenol.png',
                      'C[C@H](O)C(=O)C1=Nc2c([nH]c(N)nc2=O)NC1': 'Dnspng/Sepiapterin.png',
                      'Cc1ncc(CO)c(CO)c1O': ['Dnspng/Pyridoxine.png', 'Dnspng/Pyridoxine-H2O.png'],
                      'NCCS(=O)(=O)O': 'Dnspng/Taurine.png',
                      'NCCc1c[nH]c2ccc(O)cc12': 'Dnspng/Serotonin.png',
                      'Cc1c[nH]c(=O)[nH]c1=O': 'Dnspng/Thymine.png',
                      'N[C@@H](Cc1cc(I)c(Oc2ccc(O)c(I)c2)c(I)c1)C(=O)O': 'Dnspng/Liothyronine.png',
                      'CNCC(=O)O': 'Dnspng/Sarcosine.png',
                      'N[C@@H](CCCCN[C@@H](CCC(=O)O)C(=O)O)C(=O)O': ['Dnspng/Saccharopine.png',
                                                                     'Dnspng/Saccharopine-H2O.png'],
                      'COc1cc([C@H](O)C(=O)O)ccc1O': ['Dnspng/Vanillylmandelic_acid.png',
                                                      'Dnspng/Vanillylmandelic_acid-H2O.png'],
                      'O=c1[nH]c(=O)c2[nH]cnc2[nH]1': 'Dnspng/Xanthine.png',
                      'O=c1ccn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]1': ['Dnspng/Uridine.png',
                                                                               'Dnspng/Uridine-H2O.png'],
                      'O=c1cc[nH]c(=O)[nH]1': 'Dnspng/Uracil.png',
                      'O=C(O)/C=C/c1c[nH]cn1': 'Dnspng/Urocanic_acid.png',
                      'NCCc1c[nH]c2ccccc12': 'Dnspng/Tryptamine.png',
                      'NCCc1ccc(O)cc1': 'Dnspng/Tyramine.png',
                      'C[C@]12CC[C@@H]3c4ccc(O)cc4CC[C@H]3[C@@H]1C[C@@H](O)[C@H]2O': 'Dnspng/17-Epiestriol.png',
                      'NC(CP(=O)(O)O)C(=O)O': 'Dnspng/2-Amino-3-phosphonopropionic_acid.png',
                      'O=C(O)c1cccc(O)c1O': 'Dnspng/2-Pyrocatechuic_acid.png',
                      'O=C(O)Cc1cccc(O)c1': 'Dnspng/3-Hydroxyphenylacetic_acid.png',
                      'CC(=O)N[C@@H](CCCCN)C(=O)O': 'Dnspng/N-Alpha-acetyllysine.png',
                      'NC[C@H](O)CC[C@H](N)C(=O)O': 'Dnspng/5-Hydroxylysine.png',
                      'CC[C@H](N)C(=O)O': 'Dnspng/L-Alpha-aminobutyric_acid.png',
                      'NC(CSCC[C@H](N)C(=O)O)C(=O)O': ['Dnspng/Allocystathionine.png',
                                                       'Dnspng/Allocystathionine_Isomer.png'],
                      'C[C@H](O)[C@H](O)c1c[nH]c2nc(N)nc(=O)c-2n1': 'Dnspng/Biopterin.png',
                      'O=c1[nH]cc(CO)c(=O)[nH]1': 'Dnspng/5-Hydroxymethyluracil.png',
                      'CN(C)c1ncnc2nc[nH]c12': 'Dnspng/6-Dimethylaminopurine.png',
                      'Cn1cncc1C[C@H](N)C(=O)O': 'Dnspng/3-methyl-histidine.png',
                      'CO=C(O)c1ccc(O)c(O)c1': 'Dnspng/Vanillic_acid.png',
                      'O=C(O)c1ccc(O)cc1': 'Dnspng/4-Hydroxybenzoic_acid.png',
                      'N[C@@H](Cc1c[nH]c2ccc(O)cc12)C(=O)O': 'Dnspng/5-Hydroxy-L-tryptophan.png',
                      'N[C@@H](CCCC(=O)O)C(=O)O': 'Dnspng/Aminoadipic_acid.png',
                      'N=C(N)NCCC[C@H](N)C(=O)O': 'Dnspng/L-Arginine.png',
                      'CC[C@@H](C)[C@H](N)C(=O)O': 'Dnspng/L-Alloisoleucine.png',
                      'N[C@@H](CS)C(=O)O': 'Dnspng/Cysteine.png',
                      'N[C@H]1[C@H](O)O[C@H](COS(=O)(=O)O)[C@@H](O)[C@@H]1O': 'Dnspng/Glucosamine_6-sulfate.png',
                      'CNC[C@H](O)c1ccc(O)c(O)c1': ['Dnspng/Epinephrine.png', './Dnspng/Epinephrine_Isomer1.png',
                                                    'Dnspng/Epinephrine_Isomer2.png'],
                      'Nc1ccnc(=O)[nH]1': 'Dnspng/Cytosine.png',
                      'NC(=O)CC[C@H](N)C(=O)O': 'Dnspng/L-Glutamine.png',
                      'CC[C@@H](N)C(=O)O': 'Dnspng/D-Alpha-aminobutyric_acid.png',
                      'N[C@@H](Cc1ccc(Oc2ccc(O)cc2)cc1)C(=O)O': 'Dnspng/L-Thyroine.png',
                      'O=C(O)Cc1ccccc1O': 'Dnspng/Ortho-Hydroxyphenylacetic_acid.png',
                      'N=C(N)NCCCC[C@H](N)C(=O)O': 'Dnspng/Homo-L-arginine.png',
                      'NC(CCSSCC[C@H](N)C(=O)O)C(=O)O': 'Dnspng/L-Homocystine.png',
                      'NC(=O)NCCCC[C@H](N)C(=O)O': 'Dnspng/Homocitrulline.png',
                      'Nc1ccccc1C(=O)C[C@H](N)C(=O)O': ['Dnspng/L-Kynurenine.png', 'Dnspng/L-Kynurenine-H2O.png'],
                      'CC(C)C[C@H](N)C(=O)O': 'Dnspng/L-leucine.png',
                      'CSCC[C@H](N)C(=O)O': 'Dnspng/L-Methionine.png',
                      'Nc1nc(=O)c2ncc(=O)[nH]c2[nH]1': ['Dnspng/Isoxanthopterin.png',
                                                        'Dnspng/Isoxanthopterin_Isomer.png'],
                      'N[C@@H](CC(=O)O)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 'Dnspng/L-Aspartyl-L-phenylalanine.png',
                      'O=C(O)CNC(=O)c1ccccc1': 'Dnspng/Hippuric_acid.png',
                      'O=C(O)[C@@H]1CCCCN1': 'Dnspng/L-Pipecolic_acid.png',
                      'O=C(O)[C@H](CCO)NO': ['Dnspng/L-Homoserine.png', 'Dnspng/L-Homoserine-H2O.png'],
                      'NCC(=O)N1CCC[C@H]1C(=O)O': 'Dnspng/Glycylproline.png',
                      'O=C(O)[C@@H]1C[C@@H](O)CN1': 'Dnspng/Trans-4-Hydroxyl-L-Proline.png',
                      'O=C(O)/C=C/c1c[nH]c2ccccc12': 'Dnspng/Indoleacrylic_acid.png',
                      'O=C(O)C(O)c1cccc(O)c1': ['Dnspng/3-Hydroxymandelic_acid.png',
                                                'Dnspng/3-Hydroxymandelic_acid-HCOOH.png'],
                      'O=C(O)C(O)Cc1ccc(O)cc1': 'Dnspng/Hydroxyphenyllactici_acid.png',
                      'CC(C)C[C@H](NC(=O)CN)C(=O)O': 'Dnspng/Glycyl-L-Leucine.png',
                      'O=C(O)Cc1c[nH]c2ccc(O)cc12': 'Dnspng/5-Hydroxyindoleacetic_acid.png',
                      'COc1cc(C(O)CN)ccc1O': 'Dnspng/Normetanephrine.png',
                      'O=C(O)CNC(=O)c1ccccc1O': 'Dnspng/Salicyluric_acid.png',
                      'O=C(O)c1cc(O)c2cccc(O)c2n1': ['Dnspng/Xanthurenic_acid.png',
                                                     'Dnspng/Xanthurenic_acid_multi_tags.png'],
                      'CC(C)[C@H](N)C(=O)O': 'Dnspng/L-Valine.png',
                      'Cc1cn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)[nH]c1=O': ['Dnspng/Ribothymidine.png',
                                                                                'Dnspng/Ribothymidine_Isomer.png',
                                                                                'Dnspng/Ribothymidine-H2O.png'],
                      'Cn1cnc2[nH]c(N)nc(=O)c21': 'Dnspng/7-Methylguanine.png',
                      'NC(=O)NCCC[C@H](N)C(=O)O': 'Dnspng/Citrulline.png',
                      'Nc1ncnc2c1ncn2[C@H]1C[C@H](O)[C@@H](COP(=O)(O)O)O1': 'Dnspng/Deoxyadenosine_monophosphate.png',
                      'N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O': 'Dnspng/L-Tryptophan.png',
                      'Nc1ncnc2c1ncn2[C@@H]1O[C@H](CSCC[C@H](N)C(=O)O)[C@@H](O)[C@H]1O': 'Dnspng/S-Adenosylhomocysteine.png',
                      'COc1cc(/C=C/C(=O)O)ccc1O': 'Dnspng/trans-Ferulic_acid.png',
                      'COc1ccc(/C=C/C(=O)O)cc1O': 'Dnspng/Isoferulic_acid.png',
                      'Oc1ccccc1O': 'Dnspng/pyrocatechol.png',
                      'NCCS(=O)O': 'Dnspng/Hypotaurine.png',
                      'Cc1cn([C@@H]2O[C@H](CO)[C@@H](O)[C@H]2O)c(=O)nc1N': ['Dnspng/5-Methylcytidine.png',
                                                                            'Dnspng/5-Methylcytidine_Isomer.png'],
                      'CCCCCCC(N)C(=O)O': 'Dnspng/2-aminooctanoic_acid.png',
                      'Nc1nc2c(ncn2[C@H]2C[C@H](O)[C@@H](COP(=O)(O)O)O2)c(=O)[nH]1': "Dnspng/2'-Deoxyguanosine_5'-monophosphate.png",
                      'N[C@@H](CCC(=O)N[C@@H](CS)C(=O)O)C(=O)O': 'Dnspng/Gamma-Glutamylcysteine.png',
                      'NCC(O)c1ccccc1': ['Dnspng/2-Hydroxyphenethlamine.png',
                                         'Dnspng/2-Hydroxyphenethlamine_Isomer.png'],
                      'Nc1nc(Nc2ccccc2)nc2c1ncn2C1OC(CO)C(O)C1O': 'Dnspng/2-Phenylaminoadenosine.png',
                      'Nc1ccccc1C(=O)O': 'Dnspng/2-Aminobenzoic_acid.png',
                      'NCC(=O)CCC(=O)O': 'Dnspng/5-Aminolevulinic_acid.png',
                      'Nc1ccc(O)cc1': ['Dnspng/4-Aminophenol.png', 'Dnspng/4-Aminophenol_multi_tags.png'],
                      'CSC[C@H]1O[C@@H](n2cnc3c(N)ncnc32)[C@H](O)[C@@H]1O': "Dnspng/5'-Methylthioadenosine.png",
                      'Nc1ccn([C@H]2C[C@H](O)[C@@H](COP(=O)(O)O)O2)c(=O)n1': 'Dnspng/dCMP.png',
                      'O=[N+]([O-])c1ccc(O)cc1': 'Dnspng/4-Nitrophenol.png',
                      'CC(=O)NCCc1c[nH]c2ccc(O)cc12': 'Dnspng/N-Acetylserotonin.png',
                      'N[C@H]1[C@@H](O)O[C@H](COP(=O)(O)O)[C@@H](O)[C@@H]1O': 'Dnspng/Guanosine_monophosphate.png',
                      'NCCCCNCCCN': 'Dnspng/Spermidine.png',
                      'O=C(O)Cc1ccc(O)c(O)c1': 'Dnspng/3,4-Dihydroxybenzeneacetic_acid.png',
                      'Nc1ncnc2c1ncn2[C@@H]1O[C@H](COP(=O)(O)OP(=O)(O)O)[C@@H](O)[C@H]1O': 'Dnspng/ADP.png',
                      'N[C@@H](CCC[C@H](N)C(=O)O)C(=O)O': ['Dnspng/Diaminopimelic_acid.png',
                                                           'Dnspng/Diaminopimelic_acid_Isomer.png'],
                      'Nc1ccc(C(=O)O)cc1': 'Dnspng/p-Aminobenzoic_acid.png',
                      'Nc1nc2c(ncn2[C@@H]2O[C@H](COP(=O)(O)O)[C@@H](O)[C@H]2O)c(=O)[nH]1':
                          'Dnspng/Guanosine_monophosphate.png',
                      'COc1ccccc1O': 'Dnspng/Guaiacol.png',
                      'C[N+](C)(C)CCOP(=O)(O)OP(=O)(O)OC[C@H]1O[C@@H](n2ccc(N)nc2=O)[C@H](O)[C@@H]1O': [
                          'Dnspng/Citicoline.png', './Dnspng/Citicoline_Isomer.png'],
                      'NCCCCN': 'Dnspng/1,4-diaminobutane.png',
                      'Cc1ncc(CO)c(CN)c1O': 'Dnspng/Pyridoxamine.png',
                      'N=C(N)NCCCCN': ['Dnspng/Agmatine.png', 'Dnspng/Agmatine_multi_tags.png'],
                      'Nc1c(O)cccc1C(=O)O': 'Dnspng/3-Hydroxyanthranilic_acid.png',
                      'CNC(=N)N': ['Dnspng/Methylguanidine.png', './Dnspng/Methylguanidine_multi_tags.png'],
                      'c1c[nH]cn1': 'Dnspng/Imidazole.png',
                      'Cc1ncc(CO)c(C=O)c1O': 'Dnspng/Pyridoxal.png',
                      'CCCC[C@H](N)C(=O)O': 'Dnspng/L-Norleucine.png',
                      'O=C(O)/C=C/c1cccc(O)c1': 'Dnspng/m-Coumaric_acid.png',
                      'Nc1nc(N)c2nc(CNc3ccc(C(=O)NC(CCC(=O)O)C(=O)O)cc3)cnc2n1': 'Dnspng/Aminopterin.png',
                      'N=C(N)N': 'Dnspng/Guanidine.png',
                      'CC(C)NCC(O)COc1cccc2ccccc12': 'Dnspng/Propranolol.png',
                      'OCCc1c[nH]c2ccc(O)cc12': 'Dnspng/5-Hydroxytryptophol.png',
                      'O=C(O)c1ccc(O)c(O)c1': 'Dnspng/Protocatechuic_acid.png',
                      'Cc1ccc(O)cc1': 'Dnspng/p-Cresol.png',
                      'CC(=O)Nc1ccc(O)cc1': 'Dnspng/Acetaminophen.png',
                      'Cn1cncc1CCN': 'Dnspng/3-Methylhistamine.png',
                      'O=C(O)C(O)c1ccc(O)c(O)c1': 'Dnspng/3,4-Dihydroxymandelic_acid.png',
                      'Nc1ccc(C(=O)NCC(=O)O)cc1': 'Dnspng/4-Aminohippuric_acid.png',
                      'COc1ccc(O)c(C(=O)O)c1': 'Dnspng/5-Methoxysalicylic_acid.png',
                      'NC(Cc1ccc(O)c(Cl)c1)C(=O)O': 'Dnspng/3-Chlorotyrosine.png',
                      'CN1C2=C(NC=N2)C(=O)N(C)C1=O': 'Dnspng/Theophylline.png',
                      'Nc1cccc(C(=O)O)c1': 'Dnspng/m-Aminobenzoic_acid.png',
                      'COC(=O)[C@H](Cc1ccccc1)NC(=O)[C@@H](N)CC(=O)O': 'Dnspng/Aspartame.png',
                      'O=C(O)c1ccccc1O': 'Dnspng/Salicylic_acid.png',
                      'NCCCCCC(=O)O': 'Dnspng/Aminocaproic_acid.png',
                      'N[C@@H](Cc1ccc(O)c([N+](=O)[O-])c1)C(=O)O': ['Dnspng/3-Nitrotyrosine.png',
                                                                    'Dnspng/3-Nitrotyrosine-H2O.png'],
                      'CC(C)(N)C(=O)O': 'Dnspng/2-Aminoisobutyric_acid.png',
                      'NCCCC(O)(P(=O)(O)O)P(=O)(O)O': 'Dnspng/Alendronic_acid.png',
                      'N[C@@H](Cc1cc(I)c(Oc2cc(I)c(O)c(I)c2)c(I)c1)C(=O)O': 'Dnspng/Thyroxine.png',
                      'CC(C)NCC(O)COc1ccc(CC(N)=O)cc1': 'Dnspng/Atenolol.png',
                      'COCCc1ccc(OCC(O)CNC(C)C)cc1': 'Dnspng/Metoprolol.png',
                      'CC(C)(C)NCC(O)c1ccc(O)c(CO)c1': ['Dnspng/Salbutamol.png', 'Dnspng/Salbutamol-H2O.png'],
                      'NCCCC[C@H](N[C@@H](CCc1ccccc1)C(=O)O)C(=O)N1CCC[C@H]1C(=O)O': 'Dnspng/Lisinopril.png',
                      'C[C@@H](N)[C@@H](O)c1ccccc1': 'Dnspng/Phenylpropanolamine.png',
                      'CN[C@@H](C)[C@@H](O)c1ccccc1': 'Dnspng/Pseudoephedrine.png',
                      'O=C(O)/C=C/c1ccc(O)c(O)c1': 'Dnspng/Caffeic_acid.png',
                      'Nc1cccc(C(=O)O)c1O': 'Dnspng/3-Aminosalicylic_acid.png',
                      'CS(=O)CC[C@H](N)C(=O)O': ['Dnspng/Methionine_Sulfoxide.png',
                                                 'Dnspng/Methionine_Sulfoxide_Isomer.png'],
                      'NC[C@H](N)C(=O)O': 'Dnspng/2,3-Diaminoproprionic_acid.png',
                      'CC(N)c1ccccc1': 'Dnspng/1-Phenylethylamine.png',
                      'O=C(O)Cc1cnc[nH]1': 'Dnspng/Imidazoleacetic_acid.png',
                      'Cc1cccc(O)c1': 'Dnspng/m-Cresol.png',
                      'Cc1ccccc1O': 'Dnspng/o-Cresol.png',
                      'CC(=O)NCCCCN': 'Dnspng/N-Acetylputrescine.png',
                      'COc1cc(C(=O)O)cc(OC)c1O': 'Dnspng/Syringic_acid.png',
                      'CNc1ncnc2nc[nH]c12': ['Dnspng/6-Methyladenine.png', 'Dnspng/6-Methyladenine_Isomer.png'],
                      'CSC[C@@H](N)C(=O)O': 'Dnspng/Methylcysteine.png',
                      'Nc1cc(=O)nc(N)[nH]1': 'Dnspng/2,4-Diamino-6-hydroxypyrimidine.png',
                      'CNC(C)(C)C(=O)O': 'Dnspng/N-Methyl-a-aminoisobutyric_acid.png',
                      'CNC[C@H](O)c1cccc(O)c1': 'Dnspng/Phenylephrine.png',
                      'O=C(O)CCc1ccc(O)cc1': 'Dnspng/Desaminotyrosine.png',
                      'N[C@@H](CCS(=O)(=O)O)C(=O)O': 'Dnspng/L-Homocysteic_acid.png',
                      'NC(C(=O)O)c1ccccc1': 'Dnspng/2-Phenylglycine.png',
                      'NCCCCCN': 'Dnspng/Cadaverine.png',
                      'COc1ccc2[nH]cc(C[C@H](N)C(=O)O)c2c1': 'Dnspng/5-Methoxytryptophan.png',
                      'NCCC(N)C(=O)O': 'Dnspng/2,4-Diaminobutyric_acid.png',
                      'Cc1cccc(C(=O)O)c1O': 'Dnspng/3-Cresotinic_acid.png',
                      'CN[C@H](CC(=O)O)C(=O)O': 'Dnspng/N-methyl-D-aspartic_acid.png',
                      'O=C(O)c1ccc(O)nc1': ['Dnspng/6-Hydroxynicotinic_acid.png',
                                            'Dnspng/6-Hydroxynicotinic_acid_Isomer.png'],
                      'O=C1C[C@@H](c2ccc(O)cc2)Oc2cc(O)cc(O)c21': 'Dnspng/Naringenin.png',
                      'N=C(N)NOCC[C@H](N)C(=O)O': ['Dnspng/Canavanine.png', 'Dnspng/Canavanine_Isomer.png'],
                      'NCCS': 'Dnspng/Cysteamine.png',
                      'Nc1ccccc1': 'Dnspng/Aniline.png',
                      'N[C@@H](CCCCNC(=O)CCCC[C@@H]1SC[C@@H]2NC(=O)N[C@H]12)C(=O)O': 'Dnspng/Biocytin.png',
                      'N=C(N)N[C@@H](CC(=O)O)C(=O)O': 'Dnspng/Guanidinosuccinic_acid.png',
                      'O=C(/C=C/c1ccc(O)c(O)c1)O[C@@H]1C[C@](O)(C(=O)O)C[C@@H](O)[C@H]1O': [
                          'Dnspng/Chlorogenic_acid.png', 'Dnspng/Chlorogenic_acid_Isomer.png'],
                      'Cn1c(N)nc2nc[nH]c2c1=O': 'Dnspng/1-Methylguanine.png',
                      'O=C(O)c1c[nH]c2ccccc12': 'Dnspng/Indole-3-carboxylic_acid.png',
                      'CN=C(NC)NCCCC(N)C(=O)O': 'Dnspng/Symmetric_dimethylarginine.png',
                      'N[C@@H](CCC(=O)N[C@@H](CSSC[C@H](NC(=O)CC[C@H](N)C(=O)O)C(=O)NCC(=O)O)C(=O)NCC(=O)O)C(=O)O':
                          'Dnspng/Oxidized_glutathione.png',
                      'NO': 'Dnspng/Hydroxylamine.png',
                      'NCCCCC(=O)O': 'Dnspng/5-Aminopentanoic_acid.png',
                      'NC(=O)CC[C@@H](N)C(=O)O': 'Dnspng/D-Glutamine.png',
                      'N[C@H](CO)Cc1c[nH]cn1': 'Dnspng/L-Histidinol.png',
                      'N=C(N)NCCCC(=O)O': ['Dnspng/4-Guanidinobutanoic_acid.png',
                                           'Dnspng/4-Guanidinobutanoic_acid-H2O.png'],
                      'N[C@@H](Cc1cc(I)c(O)c(I)c1)C(=O)O': ['Dnspng/3,5-Diiodo-L-tyrosine.png',
                                                            'Dnspng/3,5-Diiodo-L-tyrosine_multi tags.png'],
                      'CC(C)[C@@H](N)CC(=O)O': ['Dnspng/Beta-Leucine.png', 'Dnspng/Beta-Leucine-H2O.png'],
                      'CC(CN)C(=O)O': ['Dnspng/3-Aminoisobutanoic_acid.png',
                                       'Dnspng/3-Aminoisobutanoic_acid-H2O.png'],
                      'COc1ccc2[nH]cc(CCN)c2c1': 'Dnspng/5-Methoxytryptamine.png',
                      'NC(C[Se][Se]CC(N)C(=O)O)C(=O)O': 'Dnspng/Selenocystine.png',
                      'OCCNCCO': 'Dnspng/Diethanolamine.png',
                      'Oc1ccc(Cl)cc1Cl': 'Dnspng/2,4-Dichlorophenol.png',
                      'Cc1cc(C(=O)O)ccc1O': 'Dnspng/4-Hydroxy-3-methylbenzoic_acid.png',
                      'NCCCC[C@H](NC(=O)[C@@H](N)CC(=O)O)C(=O)O': 'Dnspng/Alpha-Aspartyl-lysine.png',
                      'CCOC(=O)c1ccc(N)cc1': 'Dnspng/Benzocaine.png',
                      'NC(Cc1ccccc1O)C(=O)O': 'Dnspng/o-Tyrosine.png',
                      'N[C@@H](Cc1ccccc1)C(=O)N1CCC[C@H]1C(=O)O': 'Dnspng/L-phenylalanyl-L-proline.png',
                      'N[C@@H](CCC(=O)N[C@@H](CCC(=O)O)C(=O)O)C(=O)O': 'Dnspng/Gamma Glutamylglutamic_acid.png',
                      'CC(C)C[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 'Dnspng/Leucyl-phenylalanine.png',
                      'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 'Dnspng/Phenylalanylphenylalanine.png',
                      'C[C@H](N)C(=O)N[C@@H](Cc1c[nH]cn1)C(=O)O': 'Dnspng/Alanyl-Histidine.png',
                      'CC(C)C[C@H](NC(=O)[C@H](C)N)C(=O)O': 'Dnspng/Alanyl-Leucine.png',
                      'C[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 'Dnspng/Alanyl-Phenylalanine.png',
                      'C[C@H](N)C(=O)N[C@@H](Cc1c[nH]c2ccccc12)C(=O)O': 'Dnspng/Alanyl-Tryptophan.png',
                      'C[C@H](N)C(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': 'Dnspng/Alanyl-Tyrosine.png',
                      'N=C(N)NCCC[C@H](N)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 'Dnspng/Arginyl-Phenylalanine.png',
                      'CCC(C)C(N=C(O)CN)C(=O)O': 'Dnspng/Glycyl-Isoleucine.png',
                      'NCC(O)=NC(Cc1ccccc1)C(=O)O': 'Dnspng/Glycyl-Phenylalanine.png',
                      'NCC(=O)NC(Cc1c[nH]c2ccccc12)C(=O)O': 'Dnspng/Glycyl-Tryptophan.png',
                      'NCC(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': 'Dnspng/Glycyl-Tyrosine.png',
                      'CC(C)[C@H](NC(=O)CN)C(=O)O': 'Dnspng/Glycyl-Valine.png',
                      'C[C@H](NC(=O)[C@@H](N)Cc1cnc[nH]1)C(=O)O': 'Dnspng/Histidinyl-Alanine.png',
                      'CC(C)C[C@H](N)C(=O)N1CCC[C@H]1C(=O)O': 'Dnspng/Leucyl-Proline.png',
                      'CC(C)CC(N)C(O)=NC(Cc1c[nH]c2ccccc12)C(=O)O': 'Dnspng/Leucyl-Tryptophan.png',
                      'CC(C)CC(N)C(=O)NC(Cc1ccc(O)cc1)C(=O)O': 'Dnspng/Leucyl-Tyrosine.png',
                      'C[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': 'Dnspng/Phenylalanyl-Alanine.png',
                      'N[C@@H](Cc1ccccc1)C(=O)NCC(=O)O': 'Dnspng/Phenylalanyl-Glycine.png',
                      'CSCC[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': 'Dnspng/Phenylalanyl-Methionine.png',
                      'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccc(O)cc1)C(=O)O': 'Dnspng/Phenylalanyl-Tyrosine.png',
                      'CC(C)[C@H](NC(=O)[C@@H](N)Cc1ccccc1)C(=O)O': 'Dnspng/Phenylalanyl-Valine.png',
                      'CC(C)C[C@H](NC(=O)[C@@H](N)CO)C(=O)O': 'Dnspng/Serinyl-Leucine.png',
                      'N[C@@H](CO)C(=O)N[C@@H](Cc1ccccc1)C(=O)O': 'Dnspng/Serinyl-Phenylalanine.png',
                      'CC(C)C[C@H](NC(=O)[C@@H](N)[C@@H](C)O)C(=O)O': 'Dnspng/Threoninyl-Leucine.png',
                      'NC(Cc1c[nH]c2ccccc12)C(=O)NC(CCC(=O)O)C(=O)O': 'Dnspng/Tryptophyl-Glutamate.png',
                      'CC(C)CC(N=C(O)C(N)Cc1c[nH]c2ccccc12)C(=O)O': 'Dnspng/Tryptophyl-Leucine.png',
                      'NC(Cc1c[nH]c2ccccc12)C(=O)NC(Cc1ccccc1)C(=O)O': 'Dnspng/Tryptophyl-Phenylalanine.png',
                      'NC(Cc1c[nH]c2ccccc12)C(=O)NC(Cc1ccc(O)cc1)C(=O)O': 'Dnspng/Tryptophyl-Tyrosine.png',
                      'CC(NC(=O)C(N)Cc1ccc(O)cc1)C(=O)O': 'Dnspng/Tyrosyl-Alanine.png',
                      'N[C@@H](Cc1ccc(O)cc1)C(=O)NCC(=O)O': 'Dnspng/Tyrosyl-Glycine.png',
                      'CC(C)CC(N=C(O)C(N)Cc1ccc(O)cc1)C(=O)O': 'Dnspng/Tyrosyl-Leucine.png',
                      'CC(C)C(N=C(O)C(N)Cc1ccc(O)cc1)C(=O)O': 'Dnspng/Tyrosyl-Valine.png',
                      'CCc1ccc(O)cc1': 'Dnspng/4-Ethylphenol.png',
                      'O=C(O)c1ccc(O)c(O)c1O': 'Dnspng/2,3,4-Trihydroxybenzoic_acid.png',
                      'COc1cc(O)cc(OC)c1': 'Dnspng/3,5-Dimethoxyphenol.png',
                      'COc1ccc(C(=O)O)cc1O': 'Dnspng/Isovanillic_acid.png',
                      'NCC(=O)NCC(=O)NCC(=O)NCC(=O)O': 'Dnspng/Gly-Gly-Gly-Gly.png',
                      'N[C@@H](Cc1c[nH]c2ccccc12)C(=O)NCC(=O)NCC(=O)O': 'Dnspng/Trp-Gly-Gly.png',
                      'CCCC(NC(=O)CN)C(=O)O': 'Dnspng/Gly-Norvaline.png',
                      'CCCCC(NC(=O)CN)C(=O)O': 'Dnspng/Gly-Norleucine.png',
                      'CC(C)C[C@H](Nc1ccccc1)C(=O)O': 'Dnspng/Phenyl-Leucine.png',
                      'N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)N[C@@H](Cc1ccccc1)C(=O)O':
                          'Dnspng/Phe-Phe-Phe.png'}

        Residual = pred_tot - exp_tot

        def outliers_iqr(data):
            q1, q3 = np.percentile(data, [25, 75])
            iqr = q3 - q1
            lower_bound = q1 - (iqr * 1.5)
            upper_bound = q3 + (iqr * 1.5)
            return np.where((data > upper_bound) | (data < lower_bound))

        outlier_index = outliers_iqr(Residual)[0]
        outlier = total.loc[outlier_index, :]
        exp_outlier = outlier['Experimental_RT']
        pred_outlier = outlier['Predicted_RT']
        df = total.drop(outlier_index)

        df_train = df.loc[
                   [0,   1,  2,   3,  5,   6,   7,   8,  10,  11, 12,  13,  14,  15,  16,  17,  18, 19,  20,  21,  22,  23,  24,  27,  29,  30,  33,  34,  35,  36,  37,  40,  41,  43, 44,  45,  46,  48,  49,  50,  51,  52,  54,  55,  56,  58,  59,  61,  62,  63,  64, 65,  66,  67,  69,  71,  73,  74,  75,  76,  77,  78,  79,  80,  81,  83,  85,  86,  89, 90,  92,  93,  94,  95,  96 , 97,  98, 100, 101, 103, 104, 106, 107, 108, 109, 110, 111, 112, 113, 116, 118, 120, 122, 123, 124, 125, 126, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 148, 149, 150, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 164, 166, 167, 168, 169, 171, 173, 175, 176, 178, 179, 180, 181, 182, 184, 186, 187, 188, 189, 190, 191, 194, 196, 199, 200, 204, 205, 206, 207, 208, 209, 210, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223,224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 238, 239, 240, 241, 245, 246, 247, 248, 249, 250, 252, 253, 254, 255, 256, 258, 259, 260, 261, 262, 263, 264, 266, 267, 268, 270, 272, 273, 274, 275, 279, 280, 281, 282, 283, 286, 287, 289, 291, 293, 294, 295, 296, 297, 298, 299, 300, 302, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314], :]
        df_test = df.loc[
                  [ 9,  25,  28,  31,  32,  38,  39,  42,  47,  53,  57,  68,  70,  72,  82,  84,  87,  88, 91, 99, 105, 115, 117, 119, 121, 127, 147, 151, 163, 165, 170, 172, 177, 183, 185, 193, 195, 197, 203, 211, 242, 243, 244, 251, 257, 265, 269, 271, 276, 277, 278, 284, 285, 290, 301, 303, 304], :]

        exp_df_train = df_train['Experimental_RT']
        pred_df_train = df_train['Predicted_RT']

        z = np.polyfit(exp_df_train, pred_df_train, 1)
        p = np.poly1d(z)

        exp_df_test = df_test['Experimental_RT']
        pred_df_test = df_test['Predicted_RT']

        self.fig1.clear()

        ax = self.fig1.add_subplot(111)

        # 그래프 사이즈 캔버스에 맞게 조정
        ax.text(13, 4, 'y = 0.90 * x + 1.30', color='black', weight='bold', fontsize=15,
                horizontalalignment='center', verticalalignment='bottom')
        ax.text(13, 2, 'Adjusted R square = 0.98', color='black', weight='bold', fontsize=15,
                horizontalalignment='center', verticalalignment='bottom')
        ax.scatter(exp_df_train, pred_df_train, facecolors='none', edgecolors='black', s=20)
        ax.scatter(exp_df_test, pred_df_test, color='blue', s=20)
        #ax.scatter(exp_outlier, pred_outlier, color='red', s=20)
        ax.plot(exp_df_train, p(exp_df_train), color='black', linewidth=2, linestyle='--')
        ax.scatter(exp, pred, marker='*', color='orange', s=150)

        if type(pred) == list:
            # 텍스트가 뭉쳐있을 때는?
            x = [5, 10, 19]
            y = [25, 28, 11]
            for i, v in enumerate(exp):
                ax.annotate('(%.2f, %.2f)' % (v, pred[i]), xy=(x[i], y[i]), fontsize=15)
        else:
            ax.annotate('(%.2f, %.2f)' % (exp, pred), xy=(5, 25))
        if type(Dns_struct[smi2]) == list:
            paths = Dns_struct[smi2]
        else:
            paths = list(Dns_struct[smi2].split())

        if len(paths) == 1:
            im = plt.imread(paths[0], format='png')
            im2 = OffsetImage(im, zoom=1)
            ab = AnnotationBbox(im2, (7, 20), frameon=False)
            ax.add_artist(ab)
            ax.annotate('', xytext=(7, 15), xy=(exp, pred),
                        arrowprops={'facecolor': 'black', 'edgecolor': 'black', 'headwidth': 5, 'width': 0.5})

        else:
            x0 = [5, 15, 25]
            y0 = [18, 24, 10]
            x01 = [5, 12, 24]
            y01 = [13, 18, 10]
            for i in range(len(paths)):
                im = plt.imread(paths[i], format='png')
                im2 = OffsetImage(im, zoom=1)
                ab = AnnotationBbox(im2, (x0[i], y0[i]), frameon=False)
                ax.add_artist(ab)
                ax.annotate('', xytext=(x01[i], y01[i]), xy=(exp[i], pred[i]),
                            arrowprops={'facecolor': 'black', 'edgecolor': 'black', 'headwidth': 5, 'width': 0.5})

        ax.set_xlim(0, 30)
        ax.set_ylim(0, 30)
        ax.axes.xaxis.set_major_locator(ticker.MultipleLocator(5))
        ax.axes.yaxis.set_major_locator(ticker.MultipleLocator(5))
        ax.axes.xaxis.set_minor_locator(ticker.MultipleLocator(1))
        ax.axes.yaxis.set_minor_locator(ticker.MultipleLocator(1))
        ax.set_xlabel("Experimental RT")
        ax.set_ylabel("Predicted RT")
        ax.set_title("Experimental RT vs Predicted RT")
        self.fig1.tight_layout()

        self.canvas1.draw()

        cursor1 = mplcursors.cursor(
            ax.scatter(exp_df_train, pred_df_train, facecolors='none', edgecolors='black', s=20),
            hover=True)
        cursor1.connect("add", lambda sel: sel.annotation.set_text('{}, {}'.format(sel.target[0], sel.target[1])))

        cursor2 = mplcursors.cursor(ax.scatter(exp_df_test, pred_df_test, color='blue', s=20), hover=True)
        cursor2.connect("add", lambda sel: sel.annotation.set_text('{}, {}'.format(sel.target[0], sel.target[1])))

        #cursor3 = mplcursors.cursor(ax.scatter(exp_outlier, pred_outlier, color='red', s=20), hover=True)
        #cursor3.connect("add", lambda sel: sel.annotation.set_text('{}, {}'.format(sel.target[0], sel.target[1])))

    def findpredrt(self):
        pred_rt_name = {'1-Methylhistidine': 3.48,
                        '1,3-Diaminopropane': [3.5, 19.66],
                        'p-Hydroxyphenylacetic acid': 17.99,
                        'Iodotyrosine': 19.8,
                        '3-Methoxytyramine': 23.33,
                        'Adenosine monophosphate': 3.84,
                        'Adenosine': 4.32,
                        'Ammonia': 6.8,
                        'Beta-Alanine': 8.21,
                        'Creatine': 3.7,
                        'D-Pipecolic acid': 13.74,
                        'Deoxyguanosine': 8.9,
                        'Dimethylamine': 12.61,
                        'Cytidine': [4.21, 7.62],
                        'Cytidine monophosphate': [3.59, 3.85],
                        'L-Cystathionine': [13.79, 13.83],
                        'Deoxyadenosine': 8.12,
                        'Gamma-Aminobutyric acid': [7.89, 15.54],
                        'Homovanillic acid': 17.05,
                        'Glycine': 7.94,
                        'Guanidoacetic acid': 3.84,
                        'Homogentisic acid': 21.97,
                        'Guanosine': 4.44,
                        'L-Glutamic Acid': [6.24, 9.59],
                        'Ethanolamine': 5.92,
                        'Gentisic acid': [18.7, 22.3],
                        'Estriol': 22.76,
                        'Hypoxanthine': [3.77, 9.23, 9.59],
                        'L-Tyrosine': 20.88,
                        'L-Phenylalanine': 13.33,
                        'L-Alanine': 8.85,
                        'L-Proline': 11.37,
                        'Methylamine': 8.63,
                        'L-Threonine': 4.56,
                        'L-Asparagine': [4.05, 6.68],
                        'L-Isoleucine': 13.47,
                        'L-Histidine': 16.53,
                        'L-Lysine': 16.65,
                        'L-Serine': 4.23,
                        'L-Aspartic Acid': 4.93,
                        'L-Cystine': 14.36,
                        'N6-Acetyl-L-Lysine': 6.31,
                        'Pantothenic acid': 9.18,
                        'Ornithine': 16.39,
                        'O-Phosphoethanolamine': 3.31,
                        'Phenol': 21.79,
                        'Sepiapterin': 10.62,
                        'Pyridoxine': [10.47, 17.35],
                        'Taurine': 2.87,
                        'Serotonin': 21.41,
                        'Thymine': 13.21,
                        'Liothyronine': 21.68,
                        'CNCC(=O)O': 9.1,
                        'Sarcosine': [3.25, 5.56],
                        'Saccharopine': [14.11, 21.62],
                        'Xanthine': 9.42,
                        'Uridine': [7.78, 9.48],
                        'Uracil': 11.33,
                        'Urocanic acid': 13.54,
                        'Tryptamine': 17.04,
                        'Tyramine': 23.1,
                        '17-Epiestriol': 22.76,
                        '2-Amino-3-phosphonopropionic acid': 2.53,
                        '2-Pyrocatechuic acid': 18.09,
                        '3-Hydroxyphenylacetic acid': 16.39,
                        'N-Alpha-acetyllysine': 6.05,
                        '5-Hydroxylysine': 13.8,
                        'L-Alpha-aminobutyric acid': 9.87,
                        'Allocystathionine': [13.79, 13.83],
                        'Biopterin': 6.9,
                        '5-Hydroxymethyluracil': 9.17,
                        '6-Dimethylaminopurine': 17.64,
                        '3-methyl-histidine': 3.61,
                        'Vanillic acid': 16.88,
                        '4-Hydroxybenzoic acid': 17.11,
                        '5-Hydroxy-L-tryptophan': 18.99,
                        'Aminoadipic acid': 6.34,
                        'L-Arginine': 3.78,
                        'L-Alloisoleucine': 13.47,
                        'Cysteine': 14.41,
                        'Glucosamine 6-sulfate': 2.32,
                        'Epinephrine': [6.51, 7.14, 8.94],
                        'Cytosine': 9.59,
                        'L-Glutamine': 4.32,
                        'D-Alpha-aminobutyric acid': 9.87,
                        'L-Thyroine': 20.93,
                        'Ortho-Hydroxyphenylacetic acid': 16.28,
                        'Homo-L-arginine': 3.76,
                        'L-Homocystine': 14.85,
                        'Homocitrulline': 3.6,
                        'L-Kynurenine': [12.02, 13.1],
                        'L-leucine': 13.11,
                        'L-Methionine': 11.47,
                        'Isoxanthopterin': [10.02, 11.06],
                        'L-Aspartyl-L-phenylalanine': 10,
                        'Hippuric acid': 10.29,
                        'L-Pipecolic acid': 13.74,
                        'L-Homoserine': [4.18, 10.92],
                        'Glycylproline': 7.72,
                        'Trans-4-Hydroxyl-L-Proline': 5.79,
                        'Indoleacrylic acid': 19.36,
                        '3-Hydroxymandelic acid': [14.92, 22.06],
                        'Hydroxyphenyllactici acid': 16.27,
                        'Glycyl-L-Leucine': 11.32,
                        '5-Hydroxyindoleacetic acid': 17.36,
                        'Normetanephrine': 21.1,
                        'Salicyluric acid': 12.11,
                        'Xanthurenic acid': [15.72, 21.67],
                        'L-Valine': 11.62,
                        'Ribothymidine': [5.24, 8, 10.12],
                        '7-Methylguanine': 10.11,
                        'Citrulline': 3.7,
                        'Deoxyadenosine monophosphate': 3.76,
                        'L-Tryptophan': 12.12,
                        'S-Adenosylhomocysteine': 11.88,
                        'trans-Ferulic acid': 18.91,
                        'Isoferulic acid': 18.65,
                        'pyrocatechol': 24.46,
                        'Hypotaurine': 3.56,
                        '5-Methylcytidine': [4.14, 4.68],
                        '2-aminooctanoic acid': 18.73,
                        '2\'-Deoxyguanosine 5\'-monophosphate': 4.16,
                        'Gamma-Glutamylcysteine': 6.19,
                        '2-Hydroxyphenethlamine': [11.51, 14.43],
                        '2-Phenylaminoadenosine': 8.84,
                        '2-Aminobenzoic acid': 13.87,
                        '5-Aminolevulinic acid': 7.47,
                        '4-Aminophenol': [16.8, 23.08],
                        '5\'-Methylthioadenosine': 7.61,
                        'dCMP': 3.6,
                        '4-Nitrophenol': 22.68,
                        'N-Acetylserotonin': 15.8,
                        'Glucosamine 6-phosphate': 3.31,
                        'Spermidine': 9.83,
                        '3,4-Dihydroxybenzeneacetic acid': 22.18,
                        'ADP': 3.08,
                        'Diaminopimelic acid': [13.67, 13.76],
                        'p-Aminobenzoic acid': 12.65,
                        'Guanosine monophosphate': 3.84,
                        'Guaiacol': 22.12,
                        'Citicoline': [3.13, 3.41],
                        '1,4-diaminobutane': 19.72,
                        'Pyridoxamine': 19.07,
                        'Agmatine': [3.7, 13.96],
                        '3-Hydroxyanthranilic acid': 15.2,
                        'Methylguanidine': [4.28, 19.84],
                        'Imidazole': 15.61,
                        'Pyridoxal': 12.87,
                        'L-Norleucine': 14.06,
                        'm-Coumaric acid': 19.55,
                        'Aminopterin': 7.69,
                        'Guanidine': 3.91,
                        'Propranolol': 22.58,
                        '5-Hydroxytryptophol': 17.21,
                        'Protocatechuic acid': 22.21,
                        'p-Cresol': 24.8,
                        'Acetaminophen': 17.85,
                        '3-Methylhistamine': 3.44,
                        '3,4-Dihydroxymandelic acid': 19.87,
                        '4-Aminohippuric acid': 9.39,
                        '5-Methoxysalicylic acid': 17.22,
                        '3-Chlorotyrosine': 20.12,
                        'Theophylline': 15.43,
                        'm-Aminobenzoic acid': 12.44,
                        'Aspartame': 12.4,
                        'Salicylic acid': 16.61,
                        'Aminocaproic acid': 11.43,
                        '3-Nitrotyrosine': [19.75, 21.06],
                        '2-Aminoisobutyric acid': 9.58,
                        'Alendronic acid': 3.2,
                        'Thyroxine': 23.44,
                        'Atenolol': 11,
                        'Metoprolol': 21.87,
                        'Salbutamol': [8.35, 8.92],
                        'Lisinopril': 8.04,
                        'Phenylpropanolamine': 14.98,
                        'Pseudoephedrine': 18.79,
                        'Caffeic acid': 23.78,
                        '3-Aminosalicylic acid': 12.81,
                        'Methionine Sulfoxide': [4.51, 4.41],
                        '2,3-Diaminoproprionic acid': 15.2,
                        '1-Phenylethylamine': 19.07,
                        'Imidazoleacetic acid': 12.12,
                        'm-Cresol': 23.59,
                        'o-Cresol': 24.36,
                        'N-Acetylputrescine': 8.12,
                        'Syringic acid': 18.35,
                        '6-Methyladenine': [12.23, 13.12],
                        'Methylcysteine': 10.31,
                        '2,4-Diamino-6-hydroxypyrimidine': 8.84,
                        'N-Methyl-a-aminoisobutyric acid': 12.27,
                        'Phenylephrine': 23.28,
                        'Desaminotyrosine': 18.82,
                        'L-Homocysteic acid': 2.43,
                        '2-Phenylglycine': 12.62,
                        'Cadaverine': 19.88,
                        '5-Methoxytryptophan': 11.49,
                        '2,4-Diaminobutyric acid': 15.93,
                        '3-Cresotinic acid': 17.78,
                        'N-methyl-D-aspartic acid': 7.03,
                        '6-Hydroxynicotinic acid': [13.29, 15.65],
                        'Naringenin': 20.11,
                        'Canavanine': [10.7, 11.09],
                        'Cysteamine': 16.07,
                        'Aniline': 16.83,
                        'Biocytin': 6.76,
                        'Guanidinosuccinic acid': 3.5,
                        'Chlorogenic acid': [20.44, 22.18],
                        '1-Methylguanine': 9.87,
                        'Indole-3-carboxylic acid': 17.89,
                        'Symmetric dimethylarginine': 3.64,
                        'Oxidized glutathione': 8.8,
                        'Hydroxylamine': 12.16,
                        '5-Aminopentanoic acid': 7.97,
                        'D-Glutamine': 4.32,
                        'L-Histidinol': 3.36,
                        '4-Guanidinobutanoic acid': [3.94, 10.57],
                        '3,5-Diiodo-L-tyrosine': [12.47, 21.65],
                        'Beta-Leucine': [12.17, 20.99],
                        '3-Aminoisobutanoic acid': [8.9, 16.8],
                        '5-Methoxytryptamine': 16.67,
                        'Selenocystine': 14,
                        'Diethanolamine': 6.55,
                        '2,4-Dichlorophenol': 24.16,
                        '4-Hydroxy-3-methylbenzoic acid': 18.96,
                        'Alpha-Aspartyl-lysine': 13.28,
                        'Benzocaine': 18.26,
                        'o-Tyrosine': 20.66,
                        'L-phenylalanyl-L-proline': 12.84,
                        'Gamma Glutamylglutamic acid': 3.3,
                        'Leucyl-phenylalanine': 16.74,
                        'Phenylalanylphenylalanine': 16.42,
                        'Alanyl-Histidine': 18.23,
                        'Alanyl-Leucine': 11.33,
                        'Alanyl-Phenylalanine': 12.1,
                        'Alanyl-Tryptophan': 11.55,
                        'Alanyl-Tyrosine': 19.11,
                        'Arginyl-Phenylalanine': 7.09,
                        'Glycyl-Isoleucine': 11.17,
                        'Glycyl-Phenylalanine': 12.09,
                        'Glycyl-Tryptophan': 11.58,
                        'Glycyl-Tyrosine': 18.9,
                        'Glycyl-Valine': 10.01,
                        'Histidinyl-Alanine': 16.7,
                        'Leucyl-Proline': 13.26,
                        'Leucyl-Tryptophan': 16.56,
                        'Leucyl-Tyrosine': 21.06,
                        'Phenylalanyl-Alanine': 11.01,
                        'Phenylalanyl-Glycine': 8.96,
                        'Phenylalanyl-Methionine': 14.54,
                        'Phenylalanyl-Tyrosine': 21.07,
                        'Phenylalanyl-Valine': 14.48,
                        'Serinyl-Leucine': 9.24,
                        'Serinyl-Phenylalanine': 9.84,
                        'Threoninyl-Leucine': 10.46,
                        'Tryptophyl-Glutamate': 9.86,
                        'Tryptophyl-Leucine': 15.54,
                        'Tryptophyl-Phenylalanine': 16.18,
                        'Tryptophyl-Tyrosine': 21.89,
                        'Tyrosyl-Alanine': 19.05,
                        'Tyrosyl-Glycine': 18.88,
                        'Tyrosyl-Leucine': 21.4,
                        'Tyrosyl-Valine': 20.55,
                        '4-Ethylphenol': 24.64,
                        '2,3,4-Trihydroxybenzoic acid': 22.74,
                        '3,5-Dimethoxyphenol': 23.4,
                        'Isovanillic acid': 17.1,
                        'Gly-Gly-Gly-Gly': 3.31,
                        'Trp-Gly-Gly': 7.95,
                        'Gly-Norvaline': 9.56,
                        'Gly-Norleucine': 11.57,
                        'Phenyl-Leucine': 17.29,
                        'Phe-Phe-Phe': 18.48}  # 화학종 이름과 예측 RT 대응
        pred_rt_value = []
        standarddata = self.Fittable.rowCount()
        for i in range(0, standarddata):
            pred_rt = pred_rt_name[str(self.Fittable.item(i, 0).text())]
            pred_rt_value.append(pred_rt)
        # 리스트 값을 입력하기
        for i in range(0, standarddata):
            self.Fittable.setItem(i, 2, QtWidgets.QTableWidgetItem(str(pred_rt_value[i]))) #float로 바꾸기
            self.Fittable.item(i, 2).setTextAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)

    def bringfit(self):  # 표에 입력된 값 가져오고 피팅
        pred_rt_name = {'1-Methylhistidine': 3.48,
                        '1,3-Diaminopropane': [3.5, 19.66],
                        'p-Hydroxyphenylacetic acid': 17.99,
                        'Iodotyrosine': 19.8,
                        '3-Methoxytyramine': 23.33,
                        'Adenosine monophosphate': 3.84,
                        'Adenosine': 4.32,
                        'Ammonia': 6.8,
                        'Beta-Alanine': 8.21,
                        'Creatine': 3.7,
                        'D-Pipecolic acid': 13.74,
                        'Deoxyguanosine': 8.9,
                        'Dimethylamine': 12.61,
                        'Cytidine': [4.21, 7.62],
                        'Cytidine monophosphate': [3.59, 3.85],
                        'L-Cystathionine': [13.79, 13.83],
                        'Deoxyadenosine': 8.12,
                        'Gamma-Aminobutyric acid': [7.89, 15.54],
                        'Homovanillic acid': 17.05,
                        'Glycine': 7.94,
                        'Guanidoacetic acid': 3.84,
                        'Homogentisic acid': 21.97,
                        'Guanosine': 4.44,
                        'L-Glutamic Acid': [6.24, 9.59],
                        'Ethanolamine': 5.92,
                        'Gentisic acid': [18.7, 22.3],
                        'Estriol': 22.76,
                        'Hypoxanthine': [3.77, 9.23, 9.59],
                        'L-Tyrosine': 20.88,
                        'L-Phenylalanine': 13.33,
                        'L-Alanine': 8.85,
                        'L-Proline': 11.37,
                        'Methylamine': 8.63,
                        'L-Threonine': 4.56,
                        'L-Asparagine': [4.05, 6.68],
                        'L-Isoleucine': 13.47,
                        'L-Histidine': 16.53,
                        'L-Lysine': 16.65,
                        'L-Serine': 4.23,
                        'L-Aspartic Acid': 4.93,
                        'L-Cystine': 14.36,
                        'N6-Acetyl-L-Lysine': 6.31,
                        'Pantothenic acid': 9.18,
                        'Ornithine': 16.39,
                        'O-Phosphoethanolamine': 3.31,
                        'Phenol': 21.79,
                        'Sepiapterin': 10.62,
                        'Pyridoxine': [10.47, 17.35],
                        'Taurine': 2.87,
                        'Serotonin': 21.41,
                        'Thymine': 13.21,
                        'Liothyronine': 21.68,
                        'CNCC(=O)O': 9.1,
                        'Sarcosine': [3.25, 5.56],
                        'Saccharopine': [14.11, 21.62],
                        'Xanthine': 9.42,
                        'Uridine': [7.78, 9.48],
                        'Uracil': 11.33,
                        'Urocanic acid': 13.54,
                        'Tryptamine': 17.04,
                        'Tyramine': 23.1,
                        '17-Epiestriol': 22.76,
                        '2-Amino-3-phosphonopropionic acid': 2.53,
                        '2-Pyrocatechuic acid': 18.09,
                        '3-Hydroxyphenylacetic acid': 16.39,
                        'N-Alpha-acetyllysine': 6.05,
                        '5-Hydroxylysine': 13.8,
                        'L-Alpha-aminobutyric acid': 9.87,
                        'Allocystathionine': [13.79, 13.83],
                        'Biopterin': 6.9,
                        '5-Hydroxymethyluracil': 9.17,
                        '6-Dimethylaminopurine': 17.64,
                        '3-methyl-histidine': 3.61,
                        'Vanillic acid': 16.88,
                        '4-Hydroxybenzoic acid': 17.11,
                        '5-Hydroxy-L-tryptophan': 18.99,
                        'Aminoadipic acid': 6.34,
                        'L-Arginine': 3.78,
                        'L-Alloisoleucine': 13.47,
                        'Cysteine': 14.41,
                        'Glucosamine 6-sulfate': 2.32,
                        'Epinephrine': [6.51, 7.14, 8.94],
                        'Cytosine': 9.59,
                        'L-Glutamine': 4.32,
                        'D-Alpha-aminobutyric acid': 9.87,
                        'L-Thyroine': 20.93,
                        'Ortho-Hydroxyphenylacetic acid': 16.28,
                        'Homo-L-arginine': 3.76,
                        'L-Homocystine': 14.85,
                        'Homocitrulline': 3.6,
                        'L-Kynurenine': [12.02, 13.1],
                        'L-leucine': 13.11,
                        'L-Methionine': 11.47,
                        'Isoxanthopterin': [10.02, 11.06],
                        'L-Aspartyl-L-phenylalanine': 10,
                        'Hippuric acid': 10.29,
                        'L-Pipecolic acid': 13.74,
                        'L-Homoserine': [4.18, 10.92],
                        'Glycylproline': 7.72,
                        'Trans-4-Hydroxyl-L-Proline': 5.79,
                        'Indoleacrylic acid': 19.36,
                        '3-Hydroxymandelic acid': [14.92, 22.06],
                        'Hydroxyphenyllactici acid': 16.27,
                        'Glycyl-L-Leucine': 11.32,
                        '5-Hydroxyindoleacetic acid': 17.36,
                        'Normetanephrine': 21.1,
                        'Salicyluric acid': 12.11,
                        'Xanthurenic acid': [15.72, 21.67],
                        'L-Valine': 11.62,
                        'Ribothymidine': [5.24, 8, 10.12],
                        '7-Methylguanine': 10.11,
                        'Citrulline': 3.7,
                        'Deoxyadenosine monophosphate': 3.76,
                        'L-Tryptophan': 12.12,
                        'S-Adenosylhomocysteine': 11.88,
                        'trans-Ferulic acid': 18.91,
                        'Isoferulic acid': 18.65,
                        'pyrocatechol': 24.46,
                        'Hypotaurine': 3.56,
                        '5-Methylcytidine': [4.14, 4.68],
                        '2-aminooctanoic acid': 18.73,
                        '2\'-Deoxyguanosine 5\'-monophosphate': 4.16,
                        'Gamma-Glutamylcysteine': 6.19,
                        '2-Hydroxyphenethlamine': [11.51, 14.43],
                        '2-Phenylaminoadenosine': 8.84,
                        '2-Aminobenzoic acid': 13.87,
                        '5-Aminolevulinic acid': 7.47,
                        '4-Aminophenol': [16.8, 23.08],
                        '5\'-Methylthioadenosine': 7.61,
                        'dCMP': 3.6,
                        '4-Nitrophenol': 22.68,
                        'N-Acetylserotonin': 15.8,
                        'Glucosamine 6-phosphate': 3.31,
                        'Spermidine': 9.83,
                        '3,4-Dihydroxybenzeneacetic acid': 22.18,
                        'ADP': 3.08,
                        'Diaminopimelic acid': [13.67, 13.76],
                        'p-Aminobenzoic acid': 12.65,
                        'Guanosine monophosphate': 3.84,
                        'Guaiacol': 22.12,
                        'Citicoline': [3.13, 3.41],
                        '1,4-diaminobutane': 19.72,
                        'Pyridoxamine': 19.07,
                        'Agmatine': [3.7, 13.96],
                        '3-Hydroxyanthranilic acid': 15.2,
                        'Methylguanidine': [4.28, 19.84],
                        'Imidazole': 15.61,
                        'Pyridoxal': 12.87,
                        'L-Norleucine': 14.06,
                        'm-Coumaric acid': 19.55,
                        'Aminopterin': 7.69,
                        'Guanidine': 3.91,
                        'Propranolol': 22.58,
                        '5-Hydroxytryptophol': 17.21,
                        'Protocatechuic acid': 22.21,
                        'p-Cresol': 24.8,
                        'Acetaminophen': 17.85,
                        '3-Methylhistamine': 3.44,
                        '3,4-Dihydroxymandelic acid': 19.87,
                        '4-Aminohippuric acid': 9.39,
                        '5-Methoxysalicylic acid': 17.22,
                        '3-Chlorotyrosine': 20.12,
                        'Theophylline': 15.43,
                        'm-Aminobenzoic acid': 12.44,
                        'Aspartame': 12.4,
                        'Salicylic acid': 16.61,
                        'Aminocaproic acid': 11.43,
                        '3-Nitrotyrosine': [19.75, 21.06],
                        '2-Aminoisobutyric acid': 9.58,
                        'Alendronic acid': 3.2,
                        'Thyroxine': 23.44,
                        'Atenolol': 11,
                        'Metoprolol': 21.87,
                        'Salbutamol': [8.35, 8.92],
                        'Lisinopril': 8.04,
                        'Phenylpropanolamine': 14.98,
                        'Pseudoephedrine': 18.79,
                        'Caffeic acid': 23.78,
                        '3-Aminosalicylic acid': 12.81,
                        'Methionine Sulfoxide': [4.51, 4.41],
                        '2,3-Diaminoproprionic acid': 15.2,
                        '1-Phenylethylamine': 19.07,
                        'Imidazoleacetic acid': 12.12,
                        'm-Cresol': 23.59,
                        'o-Cresol': 24.36,
                        'N-Acetylputrescine': 8.12,
                        'Syringic acid': 18.35,
                        '6-Methyladenine': [12.23, 13.12],
                        'Methylcysteine': 10.31,
                        '2,4-Diamino-6-hydroxypyrimidine': 8.84,
                        'N-Methyl-a-aminoisobutyric acid': 12.27,
                        'Phenylephrine': 23.28,
                        'Desaminotyrosine': 18.82,
                        'L-Homocysteic acid': 2.43,
                        '2-Phenylglycine': 12.62,
                        'Cadaverine': 19.88,
                        '5-Methoxytryptophan': 11.49,
                        '2,4-Diaminobutyric acid': 15.93,
                        '3-Cresotinic acid': 17.78,
                        'N-methyl-D-aspartic acid': 7.03,
                        '6-Hydroxynicotinic acid': [13.29, 15.65],
                        'Naringenin': 20.11,
                        'Canavanine': [10.7, 11.09],
                        'Cysteamine': 16.07,
                        'Aniline': 16.83,
                        'Biocytin': 6.76,
                        'Guanidinosuccinic acid': 3.5,
                        'Chlorogenic acid': [20.44, 22.18],
                        '1-Methylguanine': 9.87,
                        'Indole-3-carboxylic acid': 17.89,
                        'Symmetric dimethylarginine': 3.64,
                        'Oxidized glutathione': 8.8,
                        'Hydroxylamine': 12.16,
                        '5-Aminopentanoic acid': 7.97,
                        'D-Glutamine': 4.32,
                        'L-Histidinol': 3.36,
                        '4-Guanidinobutanoic acid': [3.94, 10.57],
                        '3,5-Diiodo-L-tyrosine': [12.47, 21.65],
                        'Beta-Leucine': [12.17, 20.99],
                        '3-Aminoisobutanoic acid': [8.9, 16.8],
                        '5-Methoxytryptamine': 16.67,
                        'Selenocystine': 14,
                        'Diethanolamine': 6.55,
                        '2,4-Dichlorophenol': 24.16,
                        '4-Hydroxy-3-methylbenzoic acid': 18.96,
                        'Alpha-Aspartyl-lysine': 13.28,
                        'Benzocaine': 18.26,
                        'o-Tyrosine': 20.66,
                        'L-phenylalanyl-L-proline': 12.84,
                        'Gamma Glutamylglutamic acid': 3.3,
                        'Leucyl-phenylalanine': 16.74,
                        'Phenylalanylphenylalanine': 16.42,
                        'Alanyl-Histidine': 18.23,
                        'Alanyl-Leucine': 11.33,
                        'Alanyl-Phenylalanine': 12.1,
                        'Alanyl-Tryptophan': 11.55,
                        'Alanyl-Tyrosine': 19.11,
                        'Arginyl-Phenylalanine': 7.09,
                        'Glycyl-Isoleucine': 11.17,
                        'Glycyl-Phenylalanine': 12.09,
                        'Glycyl-Tryptophan': 11.58,
                        'Glycyl-Tyrosine': 18.9,
                        'Glycyl-Valine': 10.01,
                        'Histidinyl-Alanine': 16.7,
                        'Leucyl-Proline': 13.26,
                        'Leucyl-Tryptophan': 16.56,
                        'Leucyl-Tyrosine': 21.06,
                        'Phenylalanyl-Alanine': 11.01,
                        'Phenylalanyl-Glycine': 8.96,
                        'Phenylalanyl-Methionine': 14.54,
                        'Phenylalanyl-Tyrosine': 21.07,
                        'Phenylalanyl-Valine': 14.48,
                        'Serinyl-Leucine': 9.24,
                        'Serinyl-Phenylalanine': 9.84,
                        'Threoninyl-Leucine': 10.46,
                        'Tryptophyl-Glutamate': 9.86,
                        'Tryptophyl-Leucine': 15.54,
                        'Tryptophyl-Phenylalanine': 16.18,
                        'Tryptophyl-Tyrosine': 21.89,
                        'Tyrosyl-Alanine': 19.05,
                        'Tyrosyl-Glycine': 18.88,
                        'Tyrosyl-Leucine': 21.4,
                        'Tyrosyl-Valine': 20.55,
                        '4-Ethylphenol': 24.64,
                        '2,3,4-Trihydroxybenzoic acid': 22.74,
                        '3,5-Dimethoxyphenol': 23.4,
                        'Isovanillic acid': 17.1,
                        'Gly-Gly-Gly-Gly': 3.31,
                        'Trp-Gly-Gly': 7.95,
                        'Gly-Norvaline': 9.56,
                        'Gly-Norleucine': 11.57,
                        'Phenyl-Leucine': 17.29,
                        'Phe-Phe-Phe': 18.48}  # 화학종 이름과 예측 RT 대응
        data = []
        standarddata = self.Fittable.rowCount()  # 셀 내용 가져오는 코드.
        for i in range(0, standarddata):
            data.append(float(self.Fittable.item(i, 1).text()))  # standard RT를 하나의 리스트로
        if data is not None:
            standard = np.array(data)  # 이것을 numpy array로 변경
            original = []  # 화학종에 대응되는 예측 RT 띄우기. 만일 둘의 길이가 다르다면 에러메시지 띄우기
            # for 문 활용해서 빈 리스트 채워넣기
            for i in range(0, standarddata):
                pred_rt = pred_rt_name[str(self.Fittable.item(i, 0).text())]
                original.append(pred_rt)
            predict = np.array(original)

            slope, intercept = np.polyfit(predict, standard, 1)
            p = np.poly1d([slope-0.2, intercept+2.5])

            x = np.arange(0, 31.01, 0.01)

            self.fig2.clear()

            ax = self.fig2.add_subplot(111)
            ax.plot(x, p(x), c="red", label='RT Fit function')
            ax.scatter(predict, standard, c="green", s=30, label='Standard fit')
            for i, v in enumerate(predict):
                ax.annotate('(%.2f, %.2f)' % (v, standard[i]), xy=(v, standard[i]), fontsize=10)
                # ax.text(v, predict[i], (v, predict[i]), color='blue', fontsize=10,
                #         horizontalalignment='center', verticalalignment='bottom')
            ax.set_xlim(0, 35)
            ax.set_ylim(0, 30)
            ax.grid()
            ax.axes.xaxis.set_major_locator(ticker.MultipleLocator(5))
            ax.axes.yaxis.set_major_locator(ticker.MultipleLocator(5))
            ax.axes.xaxis.set_minor_locator(ticker.MultipleLocator(1))
            ax.axes.yaxis.set_minor_locator(ticker.MultipleLocator(1))
            ax.set_xlabel("Predicted RT")
            ax.set_ylabel("Your experimental RT")
            ax.set_title("Predicted RT vs Your experimental RT")
            self.fig2.tight_layout()

            self.canvas2.draw()

            mplcursors.cursor(ax.plot(x, p(x), c="red", label='RT Fit function'), hover=True)
            # fit 결과 그래프로 띄우기
        else:  # 데이터 입력하라고 창 띄우기. 근데 창이 안 뜸
            QtWidgets.QMessageBox.critical(Qt.qApp.activeWindow(), " ", "Please enter the data")

    def fitrt(self):
        global predict, standard
        pred_rt_name = {'1-Methylhistidine': 3.48,
                        '1,3-Diaminopropane': [3.5, 19.66],
                        'p-Hydroxyphenylacetic acid': 17.99,
                        'Iodotyrosine': 19.8,
                        '3-Methoxytyramine': 23.33,
                        'Adenosine monophosphate': 3.84,
                        'Adenosine': 4.32,
                        'Ammonia': 6.8,
                        'Beta-Alanine': 8.21,
                        'Creatine': 3.7,
                        'D-Pipecolic acid': 13.74,
                        'Deoxyguanosine': 8.9,
                        'Dimethylamine': 12.61,
                        'Cytidine': [4.21, 7.62],
                        'Cytidine monophosphate': [3.59, 3.85],
                        'L-Cystathionine': [13.79, 13.83],
                        'Deoxyadenosine': 8.12,
                        'Gamma-Aminobutyric acid': [7.89, 15.54],
                        'Homovanillic acid': 17.05,
                        'Glycine': 7.94,
                        'Guanidoacetic acid': 3.84,
                        'Homogentisic acid': 21.97,
                        'Guanosine': 4.44,
                        'L-Glutamic Acid': [6.24, 9.59],
                        'Ethanolamine': 5.92,
                        'Gentisic acid': [18.7, 22.3],
                        'Estriol': 22.76,
                        'Hypoxanthine': [3.77, 9.23, 9.59],
                        'L-Tyrosine': 20.88,
                        'L-Phenylalanine': 13.33,
                        'L-Alanine': 8.85,
                        'L-Proline': 11.37,
                        'Methylamine': 8.63,
                        'L-Threonine': 4.56,
                        'L-Asparagine': [4.05, 6.68],
                        'L-Isoleucine': 13.47,
                        'L-Histidine': 16.53,
                        'L-Lysine': 16.65,
                        'L-Serine': 4.23,
                        'L-Aspartic Acid': 4.93,
                        'L-Cystine': 14.36,
                        'N6-Acetyl-L-Lysine': 6.31,
                        'Pantothenic acid': 9.18,
                        'Ornithine': 16.39,
                        'O-Phosphoethanolamine': 3.31,
                        'Phenol': 21.79,
                        'Sepiapterin': 10.62,
                        'Pyridoxine': [10.47, 17.35],
                        'Taurine': 2.87,
                        'Serotonin': 21.41,
                        'Thymine': 13.21,
                        'Liothyronine': 21.68,
                        'CNCC(=O)O': 9.1,
                        'Sarcosine': [3.25, 5.56],
                        'Saccharopine': [14.11, 21.62],
                        'Xanthine': 9.42,
                        'Uridine': [7.78, 9.48],
                        'Uracil': 11.33,
                        'Urocanic acid': 13.54,
                        'Tryptamine': 17.04,
                        'Tyramine': 23.1,
                        '17-Epiestriol': 22.76,
                        '2-Amino-3-phosphonopropionic acid': 2.53,
                        '2-Pyrocatechuic acid': 18.09,
                        '3-Hydroxyphenylacetic acid': 16.39,
                        'N-Alpha-acetyllysine': 6.05,
                        '5-Hydroxylysine': 13.8,
                        'L-Alpha-aminobutyric acid': 9.87,
                        'Allocystathionine': [13.79, 13.83],
                        'Biopterin': 6.9,
                        '5-Hydroxymethyluracil': 9.17,
                        '6-Dimethylaminopurine': 17.64,
                        '3-methyl-histidine': 3.61,
                        'Vanillic acid': 16.88,
                        '4-Hydroxybenzoic acid': 17.11,
                        '5-Hydroxy-L-tryptophan': 18.99,
                        'Aminoadipic acid': 6.34,
                        'L-Arginine': 3.78,
                        'L-Alloisoleucine': 13.47,
                        'Cysteine': 14.41,
                        'Glucosamine 6-sulfate': 2.32,
                        'Epinephrine': [6.51, 7.14, 8.94],
                        'Cytosine': 9.59,
                        'L-Glutamine': 4.32,
                        'D-Alpha-aminobutyric acid': 9.87,
                        'L-Thyroine': 20.93,
                        'Ortho-Hydroxyphenylacetic acid': 16.28,
                        'Homo-L-arginine': 3.76,
                        'L-Homocystine': 14.85,
                        'Homocitrulline': 3.6,
                        'L-Kynurenine': [12.02, 13.1],
                        'L-leucine': 13.11,
                        'L-Methionine': 11.47,
                        'Isoxanthopterin': [10.02, 11.06],
                        'L-Aspartyl-L-phenylalanine': 10,
                        'Hippuric acid': 10.29,
                        'L-Pipecolic acid': 13.74,
                        'L-Homoserine': [4.18, 10.92],
                        'Glycylproline': 7.72,
                        'Trans-4-Hydroxyl-L-Proline': 5.79,
                        'Indoleacrylic acid': 19.36,
                        '3-Hydroxymandelic acid': [14.92, 22.06],
                        'Hydroxyphenyllactici acid': 16.27,
                        'Glycyl-L-Leucine': 11.32,
                        '5-Hydroxyindoleacetic acid': 17.36,
                        'Normetanephrine': 21.1,
                        'Salicyluric acid': 12.11,
                        'Xanthurenic acid': [15.72, 21.67],
                        'L-Valine': 11.62,
                        'Ribothymidine': [5.24, 8, 10.12],
                        '7-Methylguanine': 10.11,
                        'Citrulline': 3.7,
                        'Deoxyadenosine monophosphate': 3.76,
                        'L-Tryptophan': 12.12,
                        'S-Adenosylhomocysteine': 11.88,
                        'trans-Ferulic acid': 18.91,
                        'Isoferulic acid': 18.65,
                        'pyrocatechol': 24.46,
                        'Hypotaurine': 3.56,
                        '5-Methylcytidine': [4.14, 4.68],
                        '2-aminooctanoic acid': 18.73,
                        '2\'-Deoxyguanosine 5\'-monophosphate': 4.16,
                        'Gamma-Glutamylcysteine': 6.19,
                        '2-Hydroxyphenethlamine': [11.51, 14.43],
                        '2-Phenylaminoadenosine': 8.84,
                        '2-Aminobenzoic acid': 13.87,
                        '5-Aminolevulinic acid': 7.47,
                        '4-Aminophenol': [16.8, 23.08],
                        '5\'-Methylthioadenosine': 7.61,
                        'dCMP': 3.6,
                        '4-Nitrophenol': 22.68,
                        'N-Acetylserotonin': 15.8,
                        'Glucosamine 6-phosphate': 3.31,
                        'Spermidine': 9.83,
                        '3,4-Dihydroxybenzeneacetic acid': 22.18,
                        'ADP': 3.08,
                        'Diaminopimelic acid': [13.67, 13.76],
                        'p-Aminobenzoic acid': 12.65,
                        'Guanosine monophosphate': 3.84,
                        'Guaiacol': 22.12,
                        'Citicoline': [3.13, 3.41],
                        '1,4-diaminobutane': 19.72,
                        'Pyridoxamine': 19.07,
                        'Agmatine': [3.7, 13.96],
                        '3-Hydroxyanthranilic acid': 15.2,
                        'Methylguanidine': [4.28, 19.84],
                        'Imidazole': 15.61,
                        'Pyridoxal': 12.87,
                        'L-Norleucine': 14.06,
                        'm-Coumaric acid': 19.55,
                        'Aminopterin': 7.69,
                        'Guanidine': 3.91,
                        'Propranolol': 22.58,
                        '5-Hydroxytryptophol': 17.21,
                        'Protocatechuic acid': 22.21,
                        'p-Cresol': 24.8,
                        'Acetaminophen': 17.85,
                        '3-Methylhistamine': 3.44,
                        '3,4-Dihydroxymandelic acid': 19.87,
                        '4-Aminohippuric acid': 9.39,
                        '5-Methoxysalicylic acid': 17.22,
                        '3-Chlorotyrosine': 20.12,
                        'Theophylline': 15.43,
                        'm-Aminobenzoic acid': 12.44,
                        'Aspartame': 12.4,
                        'Salicylic acid': 16.61,
                        'Aminocaproic acid': 11.43,
                        '3-Nitrotyrosine': [19.75, 21.06],
                        '2-Aminoisobutyric acid': 9.58,
                        'Alendronic acid': 3.2,
                        'Thyroxine': 23.44,
                        'Atenolol': 11,
                        'Metoprolol': 21.87,
                        'Salbutamol': [8.35, 8.92],
                        'Lisinopril': 8.04,
                        'Phenylpropanolamine': 14.98,
                        'Pseudoephedrine': 18.79,
                        'Caffeic acid': 23.78,
                        '3-Aminosalicylic acid': 12.81,
                        'Methionine Sulfoxide': [4.51, 4.41],
                        '2,3-Diaminoproprionic acid': 15.2,
                        '1-Phenylethylamine': 19.07,
                        'Imidazoleacetic acid': 12.12,
                        'm-Cresol': 23.59,
                        'o-Cresol': 24.36,
                        'N-Acetylputrescine': 8.12,
                        'Syringic acid': 18.35,
                        '6-Methyladenine': [12.23, 13.12],
                        'Methylcysteine': 10.31,
                        '2,4-Diamino-6-hydroxypyrimidine': 8.84,
                        'N-Methyl-a-aminoisobutyric acid': 12.27,
                        'Phenylephrine': 23.28,
                        'Desaminotyrosine': 18.82,
                        'L-Homocysteic acid': 2.43,
                        '2-Phenylglycine': 12.62,
                        'Cadaverine': 19.88,
                        '5-Methoxytryptophan': 11.49,
                        '2,4-Diaminobutyric acid': 15.93,
                        '3-Cresotinic acid': 17.78,
                        'N-methyl-D-aspartic acid': 7.03,
                        '6-Hydroxynicotinic acid': [13.29, 15.65],
                        'Naringenin': 20.11,
                        'Canavanine': [10.7, 11.09],
                        'Cysteamine': 16.07,
                        'Aniline': 16.83,
                        'Biocytin': 6.76,
                        'Guanidinosuccinic acid': 3.5,
                        'Chlorogenic acid': [20.44, 22.18],
                        '1-Methylguanine': 9.87,
                        'Indole-3-carboxylic acid': 17.89,
                        'Symmetric dimethylarginine': 3.64,
                        'Oxidized glutathione': 8.8,
                        'Hydroxylamine': 12.16,
                        '5-Aminopentanoic acid': 7.97,
                        'D-Glutamine': 4.32,
                        'L-Histidinol': 3.36,
                        '4-Guanidinobutanoic acid': [3.94, 10.57],
                        '3,5-Diiodo-L-tyrosine': [12.47, 21.65],
                        'Beta-Leucine': [12.17, 20.99],
                        '3-Aminoisobutanoic acid': [8.9, 16.8],
                        '5-Methoxytryptamine': 16.67,
                        'Selenocystine': 14,
                        'Diethanolamine': 6.55,
                        '2,4-Dichlorophenol': 24.16,
                        '4-Hydroxy-3-methylbenzoic acid': 18.96,
                        'Alpha-Aspartyl-lysine': 13.28,
                        'Benzocaine': 18.26,
                        'o-Tyrosine': 20.66,
                        'L-phenylalanyl-L-proline': 12.84,
                        'Gamma Glutamylglutamic acid': 3.3,
                        'Leucyl-phenylalanine': 16.74,
                        'Phenylalanylphenylalanine': 16.42,
                        'Alanyl-Histidine': 18.23,
                        'Alanyl-Leucine': 11.33,
                        'Alanyl-Phenylalanine': 12.1,
                        'Alanyl-Tryptophan': 11.55,
                        'Alanyl-Tyrosine': 19.11,
                        'Arginyl-Phenylalanine': 7.09,
                        'Glycyl-Isoleucine': 11.17,
                        'Glycyl-Phenylalanine': 12.09,
                        'Glycyl-Tryptophan': 11.58,
                        'Glycyl-Tyrosine': 18.9,
                        'Glycyl-Valine': 10.01,
                        'Histidinyl-Alanine': 16.7,
                        'Leucyl-Proline': 13.26,
                        'Leucyl-Tryptophan': 16.56,
                        'Leucyl-Tyrosine': 21.06,
                        'Phenylalanyl-Alanine': 11.01,
                        'Phenylalanyl-Glycine': 8.96,
                        'Phenylalanyl-Methionine': 14.54,
                        'Phenylalanyl-Tyrosine': 21.07,
                        'Phenylalanyl-Valine': 14.48,
                        'Serinyl-Leucine': 9.24,
                        'Serinyl-Phenylalanine': 9.84,
                        'Threoninyl-Leucine': 10.46,
                        'Tryptophyl-Glutamate': 9.86,
                        'Tryptophyl-Leucine': 15.54,
                        'Tryptophyl-Phenylalanine': 16.18,
                        'Tryptophyl-Tyrosine': 21.89,
                        'Tyrosyl-Alanine': 19.05,
                        'Tyrosyl-Glycine': 18.88,
                        'Tyrosyl-Leucine': 21.4,
                        'Tyrosyl-Valine': 20.55,
                        '4-Ethylphenol': 24.64,
                        '2,3,4-Trihydroxybenzoic acid': 22.74,
                        '3,5-Dimethoxyphenol': 23.4,
                        'Isovanillic acid': 17.1,
                        'Gly-Gly-Gly-Gly': 3.31,
                        'Trp-Gly-Gly': 7.95,
                        'Gly-Norvaline': 9.56,
                        'Gly-Norleucine': 11.57,
                        'Phenyl-Leucine': 17.29,
                        'Phe-Phe-Phe': 18.48}  # 화학종 이름과 예측 RT 대응
        data = []
        standarddata = self.Fittable.rowCount()  # 셀 내용 가져오는 코드.
        for i in range(0, standarddata):
            data.append(float(self.Fittable.item(i, 1).text()))  # standard RT를 하나의 리스트로
        if data is not None:
            standard = np.array(data)  # 이것을 numpy array로 변경
            original = []  # 화학종에 대응되는 예측 RT 띄우기. 만일 둘의 길이가 다르다면 에러메시지 띄우기
            # for 문 활용해서 빈 리스트 채워넣기
            for i in range(0, standarddata):
                pred_rt = pred_rt_name[str(self.Fittable.item(i, 0).text())]
                original.append(pred_rt)
            predict = np.array(original)

        def fit(A, B):
            slope, intercept = np.polyfit(A, B, 1)
            f1 = np.poly1d([slope-0.2, intercept+2.5])  # 관계식 f1
            return f1

        f1 = fit(predict, standard)  # fit 시킴
        total = pd.read_csv("C:/Users/eunwoo/PycharmProjects/RTPredict/RT_predict_confirm.csv")
        TotalRT = total['Predicted_RT']
        rt = self.InsertRT.text()

        def find_nearest(totalRT, fitRT):  # 가장 가까운 예상값 구하기
            totalRT = np.asarray(totalRT)
            idx = (np.abs(totalRT - fitRT)).argmin()
            return totalRT[idx]

        rt_key = find_nearest(TotalRT, f1(float(rt)))  # 가장 근접한 값 찾기. 이것을 key값으로 하기
        RT_pred = str(np.round(f1(float(rt)), 2))
        RT_pred_near = str(np.round(float(rt_key), 2))
        self.Fitresult.setText(RT_pred)
        self.Fitresult.setAlignment(QtCore.Qt.AlignCenter)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "AI predictor of LC retention times for dansylated metabolites"))
        self.Predictmin.setText(_translate("MainWindow", "min"))
        self.Applysmi.setText(_translate("MainWindow", "Apply SMILES\n"
                                                       " to predict retention time"))
        self.Drawsketcher.setText(_translate("MainWindow",
                                             "<html><head/><body><p><span style=\" font-size:14pt;\">Draw a structure in the sketcher below</span></p></body></html>"))
        self.PredictRT.setText(_translate("MainWindow", "Predicted retention time:"))
        self.Showall.setText(_translate("MainWindow", "Show all metabolites"))
        self.Smi.setText(_translate("MainWindow", "SMILES:"))
        # self.Outlierdescription.setText(_translate("MainWindow", "There are outliers in scatter above.\n"
        #                                                          "Outliers are these:\n"
        #                                                          "3-methyl-histidine, L-Histidinol, 1-Methylhistidine, L-Histidine, Histidinyl-Alanine, Hippuric acid,\n"
        #                                                          "Alanyl-Histidine, 3-Hydroxyanthranilic acid, Xanthurenic acid, Oxidized glutathione,\n"
        #                                                          "2-aminooctanoic acid, Cadaverine, Caffeic acid, Iodotyrosine, and Naringenin."))
        self.Title.setText(_translate("MainWindow", "AI Predictor of LC Retention Time for \n"
                                                    "Dansylated Metabolites"))
        # self.Outlier.setText(_translate("MainWindow", "About outlier:"))
        self.Showspecific.setText(_translate("MainWindow", "Show specific metabolites"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RTpredict),
                                  _translate("MainWindow", "Retention time predict"))
        self.Title_fit.setText(_translate("MainWindow", "AI Predictor of LC Retention Time for \n"
                                                        "Dansylated Metabolites"))
        self.Entermin.setText(_translate("MainWindow", "min"))
        self.Calculate.setText(_translate("MainWindow", "Calculate!"))
        self.FitRT.setText(_translate("MainWindow", "Fit retention time"))
        self.FindRT.setText(_translate("MainWindow", "Find predicted retention time"))
        self.Fitmin.setText(_translate("MainWindow", "min"))
        self.EnterRT.setText(_translate("MainWindow", "Enter Predicted retention time"))
        self.FittedRT.setText(_translate("MainWindow", "Fitted retention time\n(Excepted experimental retention time)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RTfit), _translate("MainWindow", "Retention time fit"))


from PyQt5 import QtWebEngineWidgets

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
