# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qutrubgui.ui'
#
# Created: Mon Sep 28 14:46:07 2009
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

import PyQt4.QtCore
import PyQt4.QtGui
#import PyQt4.QtCore.QString 
##from PyQt4 import QtCore, QtGui
from libqutrub.mosaref_main import *
from qutrub_rc import *
import pyarabic.araby as araby

from setting import *

class Ui_MainWindow(object):
    font_base=None;
    font_result=None;
    result={}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        self.MainWindow=MainWindow;
        QtCore.QDir.setSearchPaths("res", QtCore.QStringList(QtCore.QDir.currentPath()));
        # print repr(list(QtCore.QStringList(QtCore.QDir.searchPaths("res"))));


        self.font_base=None;
        self.result={}
        self.SuggestedVerbList=[];
#-----------------------------------------------
        self.font_base = QtGui.QFont()
        self.font_base.setFamily("KacstOne")
        self.font_base.setPointSize(12)
        self.font_base.setBold(True)
        self.font_result=QtGui.QFont(DefaultFont.family(),DefaultFont.pointSize(),DefaultFont.bold());
        self.BDictOption=1;


        RightToLeft=1;
        MainWindow.setLayoutDirection(RightToLeft)


        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")


        self.Label = QtGui.QLabel(self.centralwidget)
        self.Label.setObjectName("Label")
        self.gridLayout_3.addWidget(self.Label, 1, 1, 1, 1)
        self.Label_2 = QtGui.QLabel(self.centralwidget)


        self.Label_2.setObjectName("Label_2")
        self.gridLayout_3.addWidget(self.Label_2, 2, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")


        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")


        self.BPast = QtGui.QCheckBox(self.centralwidget)
        self.BPast.setEnabled(False)

        self.BPast.setFont(self.font_base)
        self.BPast.setChecked(True)
        self.BPast.setObjectName("BPast")
        self.gridLayout_5.addWidget(self.BPast, 3, 1, 1, 1)
        self.BFuture = QtGui.QCheckBox(self.centralwidget)
        self.BFuture.setEnabled(False)

        self.BFuture.setFont(self.font_base)
        self.BFuture.setChecked(True)
        self.BFuture.setObjectName("BFuture")
        self.gridLayout_5.addWidget(self.BFuture, 3, 2, 1, 1)
        self.BImperative = QtGui.QCheckBox(self.centralwidget)
        self.BImperative.setEnabled(False)

        self.BImperative.setFont(self.font_base)
        self.BImperative.setChecked(True)
        self.BImperative.setObjectName("BImperative")
        self.gridLayout_5.addWidget(self.BImperative, 3, 3, 1, 1)



        self.BPassive = QtGui.QCheckBox(self.centralwidget)
        self.BPassive.setEnabled(False)

        self.BPassive.setFont(self.font_base)
        self.BPassive.setChecked(True)
        self.BPassive.setObjectName("BPassive")
        self.gridLayout_5.addWidget(self.BPassive, 4, 1, 1, 1)


        self.Tverb = QtGui.QLineEdit(self.centralwidget)
        self.Tverb.setEnabled(True)
        self.Tverb.setMaximumSize(QtCore.QSize(200, 40))
        self.Tverb.setFont(self.font_result)

        self.Tverb.setObjectName("Tverb")
        self.gridLayout_5.addWidget(self.Tverb, 0, 0, 1, 1)
        self.gridLayout_5.setColumnStretch(0,3)


        self.CBSuggest = QtGui.QComboBox(self.centralwidget)
        self.CBSuggest.setFont(self.font_result)
        self.CBSuggest.setEditable(True)
        self.CBSuggest.setMaximumSize(QtCore.QSize(200, 40))
        self.CBSuggest.setObjectName("CBSuggest")
        self.CBSuggest.hide()

        self.gridLayout_5.addWidget(self.CBSuggest, 1,0, 1, 1)


        self.CBHarakaLabel = QtGui.QLabel(self.centralwidget)
        self.CBHarakaLabel.setObjectName("CBHarakaLabel")
        #self.CBHarakaLabel.setText(u"حركة عين الثلاثي في المضارع")
        self.CBHarakaLabel.setFont(self.font_base)
        self.CBHarakaLabel.hide()

        self.CBHaraka = QtGui.QComboBox(self.centralwidget)
        self.CBHaraka.setFont(self.font_result)
        self.CBHaraka.setEditable(True)
        self.CBHaraka.setMaximumSize(QtCore.QSize(200, 40))
        self.CBHaraka.setObjectName("CBHaraka")
        self.CBHaraka.addItem(QtCore.QString(u"فتحة"))
        self.CBHaraka.addItem(QtCore.QString(u"ضمة"))
        self.CBHaraka.addItem(QtCore.QString(u"كسرة"))
        self.CBHaraka.setEnabled(False)
        self.CBHaraka.hide()
        self.formLayout_haraka = QtGui.QFormLayout()
        self.formLayout_haraka.setObjectName("formLayout_haraka")

        self.formLayout_haraka.setWidget(1, QtGui.QFormLayout.LabelRole, self.CBHarakaLabel)
        self.formLayout_haraka.setWidget(1, QtGui.QFormLayout.FieldRole, self.CBHaraka)
        self.gridLayout_5.addLayout(self.formLayout_haraka, 1, 2, 1, 1)

        self.BFuture_moode = QtGui.QCheckBox(self.centralwidget)
        self.BFuture_moode.setEnabled(False)

        self.BFuture_moode.setFont(self.font_base)
        self.BFuture_moode.setChecked(True)
        self.BFuture_moode.setObjectName("BFuture_moode")
        self.gridLayout_5.addWidget(self.BFuture_moode, 4, 3, 1, 1)
        self.BConfirmed = QtGui.QCheckBox(self.centralwidget)
        self.BConfirmed.setEnabled(False)

        self.BConfirmed.setFont(self.font_base)
        self.BConfirmed.setChecked(True)
        self.BConfirmed.setObjectName("BConfirmed")
        self.gridLayout_5.addWidget(self.BConfirmed, 4, 2, 1, 1)

# a search on a Transitive
        self.BTransitive = QtGui.QCheckBox(self.centralwidget)
        self.BTransitive.setFont(self.font_base)
        self.BTransitive.setChecked(True)
        self.BTransitive.setObjectName("BTransitive")
        self.gridLayout_5.addWidget(self.BTransitive, 0, 3, 1, 1)
# a more optionss
        self.BMoreOptions = QtGui.QCheckBox(self.centralwidget)
        self.BMoreOptions.setFont(self.font_base)
        self.BMoreOptions.setChecked(False)
        self.BMoreOptions.setObjectName("BMoreOptions")
        #self.BMoreOptions.setText(u"خيارات")
        self.gridLayout_5.addWidget(self.BMoreOptions, 0, 4, 1, 1)
# a search on a dictionary options
        self.BDict = QtGui.QCheckBox(self.centralwidget)
        self.BDict.setFont(self.font_base)
        self.BDict.setChecked(self.BDictOption!=0)
        self.BDict.setObjectName("BDict")
        self.BDict.hide()
        #self.BDict.setText(u"البحث في المعجم")
        self.gridLayout_5.addWidget(self.BDict, 1, 3, 1, 1)

        self.BAll = QtGui.QCheckBox(self.centralwidget)
        self.BAll.setEnabled(True)

        self.BAll.setFont(self.font_base)
        self.BAll.setChecked(True)
        self.BAll.setTristate(False)
        self.BAll.setObjectName("BAll")
        self.gridLayout_5.addWidget(self.BAll, 0, 2, 1, 1)
        self.BConjugate = QtGui.QPushButton(self.centralwidget)

        self.BConjugate.setFont(self.font_base)
        self.BConjugate.setObjectName("BConjugate")
        self.gridLayout_5.addWidget(self.BConjugate, 0, 1, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_5)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.TabVoice = QtGui.QTabWidget(self.centralwidget)

        self.TabVoice.setFont(self.font_base)
        self.TabVoice.setObjectName("TabVoice")
        self.TabActiveVoice = QtGui.QWidget()
        self.TabActiveVoice.setObjectName("TabActiveVoice")
        self.gridLayout_2 = QtGui.QGridLayout(self.TabActiveVoice)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.TabActiveResult = QtGui.QTableWidget(self.TabActiveVoice)

        self.TabActiveResult.setFont(self.font_result)
        self.TabActiveResult.setColumnCount(12)
        self.TabActiveResult.setObjectName("TabActiveResult")
        self.TabActiveResult.setColumnCount(12)
        self.TabActiveResult.setRowCount(14)

        for i in range(14):
			emptyitem = QtGui.QTableWidgetItem()
			self.TabActiveResult.setVerticalHeaderItem(i,  emptyitem)
        for i in range(12):
			emptyitem = QtGui.QTableWidgetItem()
			self.TabActiveResult.setHorizontalHeaderItem(i,  emptyitem)

        self.gridLayout_2.addWidget(self.TabActiveResult, 0, 0, 1, 1)
        self.TabVoice.addTab(self.TabActiveVoice, "")

        self.TabPassiveVoice = QtGui.QWidget()

        self.gridLayout_2p = QtGui.QGridLayout(self.TabPassiveVoice)
        self.gridLayout_2p.setObjectName("gridLayout_2p")
        self.TabPassiveVoice.setObjectName("TabPassiveVoice")
        self.TabPassiveResult = QtGui.QTableWidget(self.TabPassiveVoice)

        self.TabPassiveResult.setFont(self.font_result)
        self.TabPassiveResult.setColumnCount(12)
        self.TabPassiveResult.setObjectName("TabPassiveResult")
        self.TabPassiveResult.setColumnCount(12)
        self.TabPassiveResult.setRowCount(14)
        for i in range(14):
			emptyitem = QtGui.QTableWidgetItem()
			self.TabPassiveResult.setVerticalHeaderItem(i,  emptyitem)
        for i in range(12):
			emptyitem = QtGui.QTableWidgetItem()
			self.TabPassiveResult.setHorizontalHeaderItem(i,  emptyitem)
        self.gridLayout_2p.addWidget(self.TabPassiveResult, 0, 0, 1, 1)

        self.TabVoice.addTab(self.TabPassiveVoice, "")
        self.gridLayout.addWidget(self.TabVoice, 1, 0, 1, 1)

#---------------------------------------
        self.TabVerbAttributs = QtGui.QWidget()

        self.gridLayout_vt = QtGui.QGridLayout(self.TabVerbAttributs)
        self.gridLayout_vt.setObjectName("gridLayout_vt")
        self.TabVerbAttributs.setObjectName("TabVerbAttributs")
        self.TabVerbAttributsResult = QtGui.QTableWidget(self.TabVerbAttributs)

        self.TabVerbAttributsResult.setFont(self.font_result)
        self.TabVerbAttributsResult.setColumnCount(1)
        self.TabVerbAttributsResult.setObjectName("TabVerbAttributsResult")
        self.TabVerbAttributsResult.setRowCount(5)
        emptyitem = QtGui.QTableWidgetItem()
        self.TabVerbAttributsResult.setHorizontalHeaderItem(0, emptyitem)
        self.gridLayout_vt.addWidget(self.TabVerbAttributsResult, 0, 0, 1, 1)

        self.TabVoice.addTab(self.TabVerbAttributs, "")
#---------------------------------------
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar = QtGui.QMenuBar(MainWindow)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 789, 21))
        self.menubar.setObjectName("menubar")

        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtGui.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtGui.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtGui.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
# Menu Right to Left
        self.menu.setLayoutDirection(RightToLeft);
        self.menu_2.setLayoutDirection(RightToLeft);
        self.menu_3.setLayoutDirection(RightToLeft);
        self.menu_4.setLayoutDirection(RightToLeft);
        self.menu_5.setLayoutDirection(RightToLeft);

        MainWindow.setMenuBar(self.menubar)
#---------Actions
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.AExport = QtGui.QAction(MainWindow)
        self.AExport.setObjectName("AExport")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res:resources/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AExport.setIcon(icon)
        self.AExit = QtGui.QAction(MainWindow)
        self.AExit.setObjectName("AExit")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res:resources/images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AExit.setIcon(icon)
        self.AFont = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()

        icon.addPixmap(QtGui.QPixmap("res:resources/images/font.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AFont.setIcon(icon)
        self.AFont.setObjectName("AFont")
        self.AAbout = QtGui.QAction(MainWindow)
        self.AAbout.setObjectName("AAbout")
        self.AManual = QtGui.QAction(MainWindow)
        self.AManual.setObjectName("AManual")
        self.ACopy = QtGui.QAction(MainWindow)
        self.ACopy.setObjectName("ACopy")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res:resources/images/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ACopy.setIcon(icon)
        self.AWhoisqutrub = QtGui.QAction(MainWindow)
        self.AWhoisqutrub.setObjectName("AWhoisqutrub")
        self.ASetting = QtGui.QAction(MainWindow)
        self.ASetting.setObjectName("ASetting")
        self.APrint = QtGui.QAction(MainWindow)
        self.APrint.setObjectName("APrint")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res:resources/images/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.APrint.setIcon(icon)
        self.APrintPreview = QtGui.QAction(MainWindow)
        self.APrintPreview.setObjectName("APrintPreview")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res:resources/images/preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.APrintPreview.setIcon(icon)
        self.APagesetup = QtGui.QAction(MainWindow)
        self.APagesetup.setObjectName("APagesetup")
        self.AZoomIn = QtGui.QAction(MainWindow)
        self.AZoomIn.setObjectName("AZoomin")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res:resources/images/zoomin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AZoomIn.setIcon(icon)
        self.AZoomOut = QtGui.QAction(MainWindow)
        self.AZoomOut.setObjectName("AZoomOut")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res:resources/images/zoomout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AZoomOut.setIcon(icon)
#-------Menu--------------------
        self.menu.addAction(self.AExport)
#ToDo1
##        self.menu.addAction(self.APagesetup)
        self.menu.addSeparator()

        self.menu.addAction(self.APrint)

#ToDo1
##        self.menu.addAction(self.APrintPreview)
        self.menu.addAction(self.AExit)
        self.menu_2.addAction(self.AFont)
        self.menu_2.addAction(self.AZoomIn)
        self.menu_2.addAction(self.AZoomOut)
        self.menu_3.addAction(self.AAbout)
        self.menu_3.addAction(self.AManual)
        self.menu_3.addAction(self.AWhoisqutrub)
        self.menu_4.addAction(self.ACopy)
        self.menu_5.addAction(self.ASetting)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.toolBar.addAction(self.AFont)
        self.toolBar.addAction(self.ACopy)
        self.toolBar.addAction(self.AExport)
        self.toolBar.addAction(self.APrint)
#ToDo 2
##        self.toolBar.addAction(self.APrintPreview)
        self.toolBar.addAction(self.AZoomIn)
        self.toolBar.addAction(self.AZoomOut)

        self.TabVoice.setCurrentIndex(0)

        self.Tverb.setText(u"كَتَبَ");

        QtCore.QObject.connect(self.BConjugate, QtCore.SIGNAL("clicked()"), self.display_result)
        QtCore.QObject.connect(self.Tverb, QtCore.SIGNAL("textChanged(QString)"), self.validate_verb)
        QtCore.QObject.connect(self.BAll, QtCore.SIGNAL("clicked()"), self.check_alltenses)
        QtCore.QObject.connect(self.AExit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QObject.connect(self.APrint, QtCore.SIGNAL("triggered()"), self.print_result)
        QtCore.QObject.connect(self.APrintPreview, QtCore.SIGNAL("triggered()"), self.print_preview)
        QtCore.QObject.connect(self.AFont, QtCore.SIGNAL("triggered()"), self.change_font)
        QtCore.QObject.connect(self.AAbout, QtCore.SIGNAL("triggered()"), self.about)
        QtCore.QObject.connect(self.AWhoisqutrub, QtCore.SIGNAL("triggered()"), self.whoisqutrub)
        QtCore.QObject.connect(self.AManual, QtCore.SIGNAL("triggered()"), self.manual)
        QtCore.QObject.connect(self.AExport, QtCore.SIGNAL("triggered()"), self.save_result)
        QtCore.QObject.connect(self.AZoomIn, QtCore.SIGNAL("triggered()"), self.zoomin)
        QtCore.QObject.connect(self.AZoomOut, QtCore.SIGNAL("triggered()"), self.zoomout)
        QtCore.QObject.connect(self.BMoreOptions, QtCore.SIGNAL("clicked()"), self.show_options)
        QtCore.QObject.connect(self.ASetting, QtCore.SIGNAL("triggered()"), self.set_setting)
        QtCore.QObject.connect(self.APagesetup, QtCore.SIGNAL("triggered()"), self.page_setup)
        QtCore.QObject.connect(self.ACopy, QtCore.SIGNAL("triggered()"), self.set_copy)
        QtCore.QObject.connect(self.CBSuggest, QtCore.SIGNAL("activated(int)"), self.selectSuggest)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #---------

        self.BAll.setChecked(True);
        self.BFuture.setEnabled(False);
        self.BPast.setEnabled(False);
        self.BImperative.setEnabled(False);
        self.BPassive.setEnabled(False);
        self.BConfirmed.setEnabled(False);
        self.BFuture_moode.setEnabled(False);

        self.BFuture.hide();
        self.BPast.hide();
        self.BImperative.hide();
        self.BPassive.hide();
        self.BConfirmed.hide();
        self.BFuture_moode.hide();
# disable unallowed actions
        self.AExport.setEnabled(False)
        self.AFont.setEnabled(False)
        self.ACopy.setEnabled(False)
        self.APrint.setEnabled(False)
        self.APrintPreview.setEnabled(False)
        self.APagesetup.setEnabled(False)
        self.AZoomIn.setEnabled(False)
        self.AZoomOut.setEnabled(False)

        self.result={};
        self.TabVoice.hide();
        QtCore.QObject.connect(self.AExit, QtCore.SIGNAL("toggled(bool)"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.readSettings();
        self.applySettings();
        self.translator=QtCore.QTranslator();
        if not self.translator.load(self.getLanguageCode(), "resources/languages/",'_.'):
        # if not self.translator.load(self.getLanguageCode(), "res:resources/languages"):
        	print "failed loading"; 

        QtGui.QApplication.installTranslator(self.translator);
        self.retranslateUi(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res:images/qaf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(icon)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "قطرب: تصريف الأفعال العربية", None, QtGui.QApplication.UnicodeUTF8))
        self.Label.setText(QtGui.QApplication.translate("MainWindow", ",", None, QtGui.QApplication.UnicodeUTF8))
        self.Label_2.setText(QtGui.QApplication.translate("MainWindow", ",", None, QtGui.QApplication.UnicodeUTF8))
        self.BPast.setText(QtGui.QApplication.translate("MainWindow", "الماضي", None, QtGui.QApplication.UnicodeUTF8))
        self.BFuture.setText(QtGui.QApplication.translate("MainWindow", "المضارع", None, QtGui.QApplication.UnicodeUTF8))
        self.BImperative.setText(QtGui.QApplication.translate("MainWindow", "الأمر", None, QtGui.QApplication.UnicodeUTF8))
        self.BPassive.setText(QtGui.QApplication.translate("MainWindow", "المبني للمجهول", None, QtGui.QApplication.UnicodeUTF8))
        self.Tverb.setToolTip(QtGui.QApplication.translate("MainWindow", "<html dir=\'rtl\'>\n"
"<body>\n"
"<ol>\n"
"  <li>اكتب الفعل مشكولا شكلا تاما\n"
"(الحركات والشدة ) في خانة الفعل مثال\n"
":\n"
"كَتَبَ، كَاتَبَ. </li>\n"
"  <li>ملاحظة إذا كان الفعل مهموز\n"
"الأول على وزن فاعل،مثل آخى يرجى كتابته على الشكل ءَاخَى. </li>\n"
"  <li>إذا كان الفعل ثلاثيا حدد\n"
"حركة عين الفعل في المضارع، مثلا كتب يكتُب تأخذ الحركة ضمة في المضارع.\n"
"إذا كان الفعل غير ثلاثي، تجاهل هذه الميزة. </li>\n"
"  <li>حدد اللزوم والتعدي للفعل، </li>\n"
"  <li>اختر الزمن الذي تريد\n"
"التصريف فيه </li>\n"
"  <li>اضغط على \"صرّف الفعل\".</li>\n"
"</ol>\n"
"</body>", None, QtGui.QApplication.UnicodeUTF8))
        self.BFuture_moode.setText(QtGui.QApplication.translate("MainWindow", "المضارع المنصوب والمجزوم", None, QtGui.QApplication.UnicodeUTF8))
        self.BConfirmed.setText(QtGui.QApplication.translate("MainWindow", "المؤكد ", None, QtGui.QApplication.UnicodeUTF8))
        self.BTransitive.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'ae_AlMateen\'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">حدد اللزوم والتعدي للفعل</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.BTransitive.setText(QtGui.QApplication.translate("MainWindow", "متعدي", None, QtGui.QApplication.UnicodeUTF8))
        self.BAll.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'ae_AlMateen\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">اختر الزمن الذي تريد التصريف فيه</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.BAll.setText(QtGui.QApplication.translate("MainWindow", "كل الأزمنة", None, QtGui.QApplication.UnicodeUTF8))
        self.BConjugate.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'ae_AlMateen\'; font-size:18pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">صرف الفعل</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.BConjugate.setText(QtGui.QApplication.translate("MainWindow", "تصريف", None, QtGui.QApplication.UnicodeUTF8))
        self.CBHarakaLabel.setText(QtGui.QApplication.translate("MainWindow","حركة عين الثلاثي في المضارع", None, QtGui.QApplication.UnicodeUTF8))
        self.BMoreOptions.setText(QtGui.QApplication.translate("MainWindow","خيارات", None, QtGui.QApplication.UnicodeUTF8))
        self.BDict.setText(QtGui.QApplication.translate("MainWindow","البحث في المعجم", None, QtGui.QApplication.UnicodeUTF8))

        self.TabVoice.setTabText(self.TabVoice.indexOf(self.TabActiveVoice), QtGui.QApplication.translate("MainWindow", "المبني للمعلوم", None, QtGui.QApplication.UnicodeUTF8))
        self.TabVoice.setTabText(self.TabVoice.indexOf(self.TabPassiveVoice), QtGui.QApplication.translate("MainWindow", "المبني للمجهول", None, QtGui.QApplication.UnicodeUTF8))
        self.TabVoice.setTabText(self.TabVoice.indexOf(self.TabVerbAttributs), QtGui.QApplication.translate("MainWindow", "خصائص الفعل", None, QtGui.QApplication.UnicodeUTF8))
        self.TabVerbAttributsResult.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "القيمة", None, QtGui.QApplication.UnicodeUTF8))

        self.menu.setTitle(QtGui.QApplication.translate("MainWindow", "ملف", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_2.setTitle(QtGui.QApplication.translate("MainWindow", "عرض", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_3.setTitle(QtGui.QApplication.translate("MainWindow", "مساعدة", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_4.setTitle(QtGui.QApplication.translate("MainWindow", "تحرير", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_5.setTitle(QtGui.QApplication.translate("MainWindow", "أدوات", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.AExport.setText(QtGui.QApplication.translate("MainWindow", "ت&صدير", None, QtGui.QApplication.UnicodeUTF8))
        self.AExit.setText(QtGui.QApplication.translate("MainWindow", "&خروج", None, QtGui.QApplication.UnicodeUTF8))
        self.AFont.setText(QtGui.QApplication.translate("MainWindow", "خط", None, QtGui.QApplication.UnicodeUTF8))

        self.AAbout.setText(QtGui.QApplication.translate("MainWindow", "حول البرنامج", None, QtGui.QApplication.UnicodeUTF8))
        self.AManual.setText(QtGui.QApplication.translate("MainWindow", "دليل الاستعمال", None, QtGui.QApplication.UnicodeUTF8))
        self.ACopy.setText(QtGui.QApplication.translate("MainWindow", "نسخ", None, QtGui.QApplication.UnicodeUTF8))
        self.AWhoisqutrub.setText(QtGui.QApplication.translate("MainWindow", "من هو قطرب؟", None, QtGui.QApplication.UnicodeUTF8))
        self.ASetting.setText(QtGui.QApplication.translate("MainWindow", "تفضيلات", None, QtGui.QApplication.UnicodeUTF8))
        self.APrint.setText(QtGui.QApplication.translate("MainWindow", "طباعة...", None, QtGui.QApplication.UnicodeUTF8))
        self.APrintPreview.setText(QtGui.QApplication.translate("MainWindow", "معاينة الطباعة", None, QtGui.QApplication.UnicodeUTF8))
        self.APagesetup.setText(QtGui.QApplication.translate("MainWindow", "إعداد الصفحة", None, QtGui.QApplication.UnicodeUTF8))
        self.AZoomIn.setText(QtGui.QApplication.translate("MainWindow", "تكبير", None, QtGui.QApplication.UnicodeUTF8))
        self.AZoomOut.setText(QtGui.QApplication.translate("MainWindow", "تصغير", None, QtGui.QApplication.UnicodeUTF8))

    def validate_verb(self):
        word = self.Tverb.text();
        self.CBHaraka.setEnabled(False);
        if not word.isEmpty():

            word=unicode(word);
            word = word.strip(' ');
            if not araby.isArabicword(word):

                QtGui.QToolTip.showText(self.Tverb.geometry().bottomRight(),
                            QtGui.QApplication.translate("MainWindow", "الفعل  غير صالح", None, QtGui.QApplication.UnicodeUTF8),self.Tverb)
                self.Tverb.setStyleSheet ("QLineEdit { color: red;}")


            else:
                self.CBHaraka.setEnabled(is_triliteral_verb(word));
                self.Tverb.setStyleSheet ("QLineEdit { color: black;}")
        else:
            self.Tverb.setStyleSheet ("QLineEdit { color: black;}")


    def check_alltenses(self):
        if self.BAll.checkState()!=0:
            check=True;
            self.BFuture.hide();
            self.BPast.hide();
            self.BImperative.hide();
            self.BPassive.hide();
            self.BConfirmed.hide();
            self.BFuture_moode.hide();
        else:
            check=False;
            self.BFuture.show();
            self.BPast.show();
            self.BImperative.show();
            self.BPassive.show();
            self.BConfirmed.show();
            self.BFuture_moode.show();

        self.BFuture.setEnabled(not check);
        self.BPast.setEnabled(not check);
        self.BImperative.setEnabled(not check);
        self.BPassive.setEnabled(not check);
        self.BConfirmed.setEnabled(not check);
        self.BFuture_moode.setEnabled(not check);

        self.BFuture.setChecked(check);
        self.BPast.setChecked(check);
        self.BImperative.setChecked(check);
        self.BPassive.setChecked(check);
        self.BConfirmed.setChecked(check);
        self.BFuture_moode.setChecked(check);

    def show_options(self):
        if self.BMoreOptions.checkState()!=0:
            self.CBHaraka.show();
            self.CBHarakaLabel.show();
            self.BDict.show();
        else:
            self.CBHaraka.hide();
            self.CBHarakaLabel.hide();
            self.BDict.hide();



    def change_font(self):
        newfont,ok = QtGui.QFontDialog.getFont(self.font_result);
        if ok:
            self.font_result=newfont;
            self.TabActiveResult.setFont(self.font_result)
            self.TabActiveResult.update();
            self.TabPassiveResult.setFont(self.font_result)
            self.TabPassiveResult.update();

    def zoomin(self):
        self.font_result.setPointSize(self.font_result.pointSize()+1);
        self.TabActiveResult.setFont(self.font_result)
        self.TabActiveResult.update();
        self.TabPassiveResult.setFont(self.font_result)
        self.TabPassiveResult.update();

    def zoomout(self):
        self.font_result.setPointSize(self.font_result.pointSize()-1);
        self.TabActiveResult.setFont(self.font_result)
        self.TabActiveResult.update();
        self.TabPassiveResult.setFont(self.font_result)
        self.TabPassiveResult.update();

    def set_copy(self):
        if self.result.has_key("TEXT"):
            QtGui.QApplication.clipboard().setText(self.result["TEXT"])


    def page_setup(self):
        pass;
    def print_preview(self):
        if self.result.has_key("HTML"):

            printer = QtGui.QPrinter()

            self.printpreview = QtGui.QPrintPreviewDialog(printer, self.centralwidget)
            QtCore.QObject.connect(self.printpreview, QtCore.SIGNAL("paintRequested(QPrinter *)"), self.generate_preview)
            QtCore.QMetaObject.connectSlotsByName(self.centralwidget)

            self.printpreview.exec_();
        else:
            QtGui.QMessageBox.warning(self.centralwidget,QtGui.QApplication.translate("MainWindow", "خطأ", None, QtGui.QApplication.UnicodeUTF8),
                                QtGui.QApplication.translate("MainWindow", "لا شيء يمكن طبعه، صرّف أولا", None, QtGui.QApplication.UnicodeUTF8))

#ToDo 1
    def generate_preview(self,other):
        #print "working";

        asd=u"""<b>عربي</b>((self.ui.\ntextEdit.toPlainText())"""#.split('\n')
        document = QtGui.QTextDocument("")
        document.setHtml(self.result["TEXT"]);
        asd=document.toPlainText().split("\n");
        self.printpreview.autoFillBackground()
        painter = QtGui.QPainter()
        painter.setLayoutDirection(RightToLeft)
        painter.begin(other)
        x=0
        for s in asd:
            if x == 0:
                pass
            else:
                other.newPage()
            x=1
            painter.setFont(QtGui.QFont('Decorative', 25))       # change font
            painter.drawText(100,100,s)                    # printing point
        painter.end()
        return True;


        document = QtGui.QTextDocument("")
        self.result["HTML"]="u<html dir=rtl><body>"+self.result["HTML"]+"</body></html>"
        document.setHtml(self.result["HTML"]);
        printer = QtGui.QPrinter()

        self.printpreview.autoFillBackground()
        painter = QtGui.QPainter()
        painter.begin(printer)
        printer.newPage();

        painter.drawText(100,100,"document.toPlainText(")
        painter.end()


    def print_result(self):
        if self.result.has_key("HTML"):
            data=QtCore.QFile("res:resources/style.css");
            if (data.open(QtCore.QFile.ReadOnly)):
                mySTYLE_SHEET=QtCore.QTextStream(data).readAll();
    ##            text=unicode(text);
            else:
                mySTYLE_SHEET=u"""
body {
	direction: rtl;
	font-family: Traditional Arabic, "Times New Roman";
	font-size: 16pt;
}
"""
            document = QtGui.QTextDocument("")
            document.setDefaultStyleSheet(mySTYLE_SHEET)
            self.result["HTML"]=u"<html dir=rtl><body dir='rtl'>"+self.result["HTML"]+"</body></html>"
            document.setHtml(self.result["HTML"]);
            printer = QtGui.QPrinter()

            dlg = QtGui.QPrintDialog(printer, self.centralwidget)
            if dlg.exec_() != QtGui.QDialog.Accepted:
                return

            document.print_(printer)
        else:
            QtGui.QMessageBox.warning(self.centralwidget,QtGui.QApplication.translate("MainWindow", "خطأ", None, QtGui.QApplication.UnicodeUTF8),
                               QtGui.QApplication.translate("MainWindow", "لا شيء يمكن طبعه، صرّف أولا", None, QtGui.QApplication.UnicodeUTF8))


##    def set_setting(self):
##        QtGui.QMessageBox.warning(self.centralwidget,U"عذرا",
##                                u"غير متوفر حاليا")
    def set_setting(self):
        init_Dialog=QtGui.QDialog(self.centralwidget)
        Dialog=Ui_Dialog();
        Dialog.setupUi(init_Dialog);
        if init_Dialog.exec_() == QtGui.QDialog.Accepted:
            self.readSettings();
            self.retranslateUi(self.MainWindow)
            self.applySettings();

    def readSettings(self):
        settings = QtCore.QSettings("Arabeyes.org", "Qutrub")
        family=settings.value("font_base_family", QtCore.QVariant(QtCore.QString("Traditional Arabic"))).toString()
        size,ok=settings.value("font_base_size", QtCore.QVariant(12)).toInt();
        if not ok:size=12;
        bold=settings.value("font_base_bold", QtCore.QVariant(True)).toBool()
        self.font_result.setFamily(family)
        self.font_result.setPointSize(size)
        self.font_result.setBold(bold)
        #read of dictsetting options
        dictsetting,ok=settings.value("DictSetting", QtCore.QVariant(1)).toInt();
        if not ok:dictsetting=1;
        self.BDictOption=dictsetting;
        langindex,ok=settings.value("Language", QtCore.QVariant(1)).toInt();
        if not ok:langindex=1;
        self.Language=langindex;
        #print self.Language		
    def applySettings(self):

        self.BDict.setChecked(self.BDictOption!=0)
        self.TabActiveResult.update();
        self.TabPassiveResult.update();
        self.retranslateUi(self.MainWindow)		

    def page_setup(self):
        QtGui.QMessageBox.warning(self.centralwidget,QtGui.QApplication.translate("MainWindow", "عذرا", None, QtGui.QApplication.UnicodeUTF8),
                                QtGui.QApplication.translate("MainWindow", "غير متوفر حاليا", None, QtGui.QApplication.UnicodeUTF8))

    def whoisqutrub(self):
        data=QtCore.QFile("res:resources/languages/"+self.getLanguageCode()+"/qutrub_body.html");
        if (data.open(QtCore.QFile.ReadOnly)):
            textstream=QtCore.QTextStream(data);
            textstream.setCodec("UTF-8");
            text=textstream.readAll();
        else:
            text=QtGui.QApplication.translate("MainWindow", "لا يمكن فتح ملف المساعدة", None, QtGui.QApplication.UnicodeUTF8)

        Dialog=QtGui.QDialog(self.centralwidget)

        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 480)
        Dialog.setWindowTitle(QtGui.QApplication.translate("MainWindow", 'من هو قطرب؟', None, QtGui.QApplication.UnicodeUTF8))
        gridLayout = QtGui.QGridLayout(Dialog)
        gridLayout.setObjectName("gridLayout")
        textBrowser = QtGui.QTextBrowser(Dialog)
        textBrowser.setObjectName("textBrowser")
        gridLayout.addWidget(textBrowser, 0, 0, 1, 1)
        buttonBox = QtGui.QDialogButtonBox(Dialog)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        buttonBox.setObjectName("buttonBox")
        gridLayout.addWidget(buttonBox, 1, 0, 1, 1)
        QtCore.QObject.connect(buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        textBrowser.setText(text)
        RightToLeft=1;
        Dialog.setLayoutDirection(RightToLeft);
        Dialog.show();

    def manual(self):
        data=QtCore.QFile("res:resources/languages/"+self.getLanguageCode()+"/help_body.html");
        if (data.open(QtCore.QFile.ReadOnly)):
            textstream=QtCore.QTextStream(data);
            textstream.setCodec("UTF-8");
            text=textstream.readAll();
        else:
            text=QtGui.QApplication.translate("MainWindow", "لا يمكن فتح ملف المساعدة", None, QtGui.QApplication.UnicodeUTF8)

        Dialog=QtGui.QDialog(self.centralwidget)

        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 480)
        Dialog.setWindowTitle(QtGui.QApplication.translate("MainWindow", "دليل الاستخدام", None, QtGui.QApplication.UnicodeUTF8))
        gridLayout = QtGui.QGridLayout(Dialog)
        gridLayout.setObjectName("gridLayout")
        textBrowser = QtGui.QTextBrowser(Dialog)
        textBrowser.setObjectName("textBrowser")
        gridLayout.addWidget(textBrowser, 0, 0, 1, 1)
        buttonBox = QtGui.QDialogButtonBox(Dialog)
        buttonBox.setOrientation(QtCore.Qt.Horizontal)
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        buttonBox.setObjectName("buttonBox")
        gridLayout.addWidget(buttonBox, 1, 0, 1, 1)


        QtCore.QObject.connect(buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        text2=unicode(text)
        #print type(text2)
        textBrowser.setText(text2)
        RightToLeft=1;
        Dialog.setLayoutDirection(RightToLeft);
        Dialog.show();
    def about(self):
        RightToLeft=1;
        msgBox=QtGui.QMessageBox(self.centralwidget);
        msgBox.setWindowTitle(QtGui.QApplication.translate("MainWindow", "عن برنامج قطرب", None, QtGui.QApplication.UnicodeUTF8));
##          msgBox.setTextFormat(QrCore.QRichText);

        data=QtCore.QFile("res:resources/languages/"+self.getLanguageCode()+"/about.html");
        if (data.open(QtCore.QFile.ReadOnly)):
            textstream=QtCore.QTextStream(data);
            textstream.setCodec("UTF-8");
            text_about=textstream.readAll();
        else:
#            text=u"لا يمكن فتح ملف المساعدة"
            text_about=u"""<h1>فكرة</h1>
يقوم البرنامج
بتصريف الأفعال المدخلة مع بعض المعلومات
الضرورية لتوليد جميع أشكال التصريف في الأزمنة المختلفة.<br>
هدف البرنامج هو تمكين تصريف الأفعال العربية تصريفا آليا مبسطا.<br>
</p>
<b>موقع المشروع</b>
<a href="http://qutrub.arabeyes.org">http://qutrub.arabeyes.org</a><br>
<b>المطور </b>
<a href="mailto:taha_zerrouki@gawab.com">طه زروقي</a><br>
<hr/>
<h3>شكر خاص </h3>
<ul>
  <li>برمجة الويب :مصطفى عمارة  (<a href='http://moustafaemara.wordpress.com/'>moustafaemara.wordpress.com</a>) </li>
  <li>تصميم الشعار : عصام حمود (<a href="http://hamoudart.com/">hamoudart.com/</a>)</li>
<li>عيون العرب <a href='http://www.arabeyes.org'>arabeyes.org</a></li>
<li>التقنيين العرب <a href='http://www.arabtechies.net'>arabtechies.net</a></li>
</ul>

"""
        msgBox.setText(text_about);
        msgBox.setLayoutDirection(RightToLeft);
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok);
        msgBox.setIconPixmap(QtGui.QPixmap("res:resources/images/logo.png"));
        msgBox.setDefaultButton(QtGui.QMessageBox.Ok);
        msgBox.exec_();
##          QtGui.QMessageBox.about(self.centralwidget,U"عن البرنامج",
##                                u"اسم ملف غير مناسب %s"%filename);
    def save_result(self):
        filename = QtGui.QFileDialog.getSaveFileName(self.centralwidget,
        QtGui.QApplication.translate("MainWindow", "حفظ ملف", None, QtGui.QApplication.UnicodeUTF8),"untitled","HTML document (*.html *.htm);;Text file (*.txt);;Text Unicode comma separeted format file (*.csv);;XML file (*.xml);;TeX file (*.tex)");
        if filename:
            filename=unicode(filename)
            tuple=filename.split(".");
            if len(tuple)>=2:
                extention=tuple.pop();
            else:
                extention="html";
                filename+="."+extention
            text=""
            if extention.lower() in ('html','tex','txt','xml','csv'):
                display_format=extention.upper();
            #Add text generation
                if not self.result.has_key(extention.upper()):
                    QtGui.QMessageBox.warning(self.centralwidget,QtGui.QApplication.translate("MainWindow", "خطأ", None, QtGui.QApplication.UnicodeUTF8),
                               QtGui.QApplication.translate("MainWindow", "لا بيانات للتصدير، صرّف أولا", None, QtGui.QApplication.UnicodeUTF8))
                    return None;
                text+=self.result[extention.upper()];
            else:
                QtGui.QMessageBox.warning(self.centralwidget,QtGui.QApplication.translate("MainWindow", "خطأ", None, QtGui.QApplication.UnicodeUTF8),
                               QtGui.QApplication.translate("MainWindow", "اسم ملف غير مناسب %1", None, QtGui.QApplication.UnicodeUTF8).arg(filename))
            try:
                file_saved=open(filename,'w+');
                if file_saved:
                    file_saved.write(text.encode("utf8"));
                    file_saved.flush();
                    file_saved.close();

                else:
                    QtGui.QMessageBox.warning(self.centralwidget,QtGui.QApplication.translate("MainWindow", "خطأ", None, QtGui.QApplication.UnicodeUTF8),
                                QtGui.QApplication.translate("MainWindow", "لا يمكن فتح الملف %1", None, QtGui.QApplication.UnicodeUTF8).arg(filename))
            except:
                QtGui.QMessageBox.warning(self.centralwidget,QtGui.QApplication.translate("MainWindow", "خطأ", None, QtGui.QApplication.UnicodeUTF8),
                                QtGui.QApplication.translate("MainWindow", "لا يمكن حفظ الملف %1", None, QtGui.QApplication.UnicodeUTF8).arg(filename))
    def getLanguageCode(self,):
        languages={ 0:  "ar",  
 1:  "en",  
 2:  "de",  
 3:  "fr",  
 4:  "ur",  
 5:  "fa",  
 6:  "jp", 
 7:  "ms", }
 
        if languages.has_key(self.Language):
        	return languages[self.Language];
        return "ar";
    def getLanguageFile(self,):
        langfile="language_ar.qm";
        languages={ 0:  "ar",  
 1:  "en",  
 2:  "de",  
 3:  "fr",  
 4:  "ur",  
 5:  "fa",  
 6:  "jp", }
        if languages.has_key(self.Language):
        	langfile="language_"+languages[self.Language]+".qm";
        	#print langfile
        return langfile;		

    def get_index_haraka(self,haraka):
        if haraka==u"فتحة":
            iharaka=0;
        elif haraka==u"ضمة":
            iharaka=1;
        elif haraka==u"كسرة":
            iharaka=2;
        else:
            iharaka=0;
        return iharaka;

    def selectSuggest(self):
        index=self.CBSuggest.currentIndex();
        if self.SuggestedVerbList!=None and len(self.SuggestedVerbList)>0:
            suggested_word=self.SuggestedVerbList[index]["verb"]
            suggested_haraka=self.SuggestedVerbList[index]["haraka"]
            suggested_transitive=self.SuggestedVerbList[index]["transitive"]
            self.Tverb.setText(suggested_word);
            self.CBHaraka.setCurrentIndex(self.get_index_haraka(suggested_haraka));
            self.display_result();


    def display_result(self):

        word = self.Tverb.text();
        if not word.isEmpty():

            word=unicode(word);
            word = word.strip(' ');
            if not is_valid_infinitive_verb(word):

                QtGui.QMessageBox.warning(self.centralwidget,QtGui.QApplication.translate("MainWindow", "خطأ", None, QtGui.QApplication.UnicodeUTF8),
                            QtGui.QApplication.translate("MainWindow", "الفعل %1 غير صالح2", None, QtGui.QApplication.UnicodeUTF8).arg(word))
                self.Tverb.clear();
                self.Tverb.setFocus();

            else:
                #=u"فتحة"
                #print self.CBHaraka.currentIndex();
                haraka=unicode(self.CBHaraka.currentText());
##                haraka=u"فتحة"
    ##            display_format =  'HTML';
                display_format =  'CSV';
                all = (self.BAll.checkState()!=0)
                past = (self.BPast.checkState()!=0)
                future = (self.BFuture.checkState()!=0)
                imperative = (self.BImperative.checkState()!=0)
                passive = (self.BPassive.checkState()!=0)
                confirmed = (self.BConfirmed.checkState()!=0)
                future_moode = (self.BFuture_moode.checkState()!=0)
                transitive = (self.BTransitive.checkState()!=0)
##                print "transitive 1", transitive;
##
                if (not all) and (not future) and (not past) and (not imperative) and (not passive) and (not future_moode) and (not confirmed) :
                    QtGui.QMessageBox.warning(self.centralwidget,QtGui.QApplication.translate("MainWindow", "خطأ", None, QtGui.QApplication.UnicodeUTF8),
                           QtGui.QApplication.translate("MainWindow", "اختر زمنا واحدا على الأقل", None, QtGui.QApplication.UnicodeUTF8))
                else:
##            self.WResult.setContent(unicode(result));
##    word = word.strip(' ')
                # suggest is used to give more suggestion for triliteral verbs
                    suggest="";
                    self.CBSuggest.clear()
                    search_triverb_dict=(self.BDict.checkState()!=0)
                    if is_triliteral_verb(word) and search_triverb_dict:
            # search the future haraka for the triliteral verb
##                        db_base_path=os.path.join(_base_directory(req),"libqutrub/");
                        #db_base_path=".";
                        #liste_verb=find_triliteral_verb(db_base_path,word,haraka);
                        liste_verb=find_alltriverb(word,haraka,True);
#                        for v in liste_verb:
#                            print liste_verb[0]['verb'].encode('utf8');
            # if there are more verb forms, select the first one
                        self.SuggestedVerbList=liste_verb;
                        if  liste_verb!=None and len(liste_verb)>0:
                            word=liste_verb[0]["verb"]
                            haraka=liste_verb[0]["haraka"]
                            transitive=liste_verb[0]["transitive"]
                            if len(liste_verb)>1:
                                suggest=u"هل تقصد؟<br/>"
                                self.CBSuggest.show()
##                                self.CBSuggestLabel.show()
            # the other forms are suggested

                            for i in range(0,len(liste_verb)):

                                suggested_word=liste_verb[i]["verb"]
                                suggested_haraka=liste_verb[i]["haraka"]
                                suggested_transitive=liste_verb[i]["transitive"]
                                future_form=get_future_form(suggested_word,suggested_haraka);
            #                    display_format=display_format.decode("utf8");
                                #suggest=u"""<a href='?verb=%s&haraka=%s&transitive=%s&all=1&display_format=HTML'>%s %s</a><br/>"""%(suggested_word,suggested_haraka,suggested_transitive,suggested_word,future_form);
                                suggest=suggested_word+u"-"+future_form+u"(%s)"%suggested_haraka#+"[%s]"%suggested_transitive;
            # if the verb does'nt exist in the triliteral verb dictionary
            #            else:suggest=u"غير وارد في المعجم<br/>"
            #----------show suggest
                                self.CBSuggest.addItem(QtCore.QString(suggest))
                            self.CBSuggest.showPopup();
                        else:
                            if liste_verb==None:
                                QtGui.QMessageBox.critical(self.centralwidget,QtGui.QApplication.translate("MainWindow", "خطأ", None, QtGui.QApplication.UnicodeUTF8),
                                u"مسار قاعدة البيانات غير صحيح %s"%db_base_path)
                                suggest=db_base_path
                            else:

                                QtGui.QMessageBox.critical(self.centralwidget,QtGui.QApplication.translate("MainWindow", "خطأ", None, QtGui.QApplication.UnicodeUTF8),
                                QtGui.QApplication.translate("MainWindow", "الفعل غير موجود في قائمة الأفعال الثلاثية", None, QtGui.QApplication.UnicodeUTF8))
                    else:
                        self.CBSuggest.hide();
                        #self.CBSuggestLabel.hide();

##                    print "transitive 2", transitive;
                    self.CBHaraka.setCurrentIndex(self.get_index_haraka(haraka))
                    self.do_sarf(word,haraka,all,past,future,passive,imperative,future_moode,confirmed,transitive,"TABLE")
                    self.display_result_in_grid();


    def display_result_in_grid(self):

        rslt_tab=self.result["TABLE"];
# display in grid
        self.TabActiveResult.clear();
        self.TabPassiveResult.clear();
##hide all columns
        for j in range(12):
            self.TabActiveResult.hideColumn(j)
            self.TabPassiveResult.hideColumn(j)
# display tenses in columns labels
        for j in range(1,len(rslt_tab[0])):
            self.TabActiveResult.setHorizontalHeaderItem(j-1,QtGui.QTableWidgetItem(rslt_tab[0][j]))
            self.TabPassiveResult.setHorizontalHeaderItem(j-1,QtGui.QTableWidgetItem(rslt_tab[0][j]))
            if rslt_tab[0][j] in TableIndicativeTense:
                self.TabActiveResult.showColumn(j-1)
                self.TabPassiveResult.hideColumn(j-1)
            else:
                self.TabActiveResult.hideColumn(j-1)
                self.TabPassiveResult.showColumn(j-1)

##        # display pronouns in rows labels
        for i in range(1,len(rslt_tab)):
            self.TabActiveResult.setVerticalHeaderItem(i-1,QtGui.QTableWidgetItem(rslt_tab[i][0]))
            self.TabPassiveResult.setVerticalHeaderItem(i-1,QtGui.QTableWidgetItem(rslt_tab[i][0]))
        for i in range(1,15):
          for j in range(1,len(rslt_tab[i])):
                self.TabActiveResult.setItem(i-1,j-1,QtGui.QTableWidgetItem(rslt_tab[i][j]))
                self.TabPassiveResult.setItem(i-1,j-1,QtGui.QTableWidgetItem(rslt_tab[i][j]))
# resize cells to content
        self.TabActiveResult.resizeColumnsToContents();
        self.TabActiveResult.resizeRowsToContents();
        self.TabPassiveResult.resizeColumnsToContents();
        self.TabPassiveResult.resizeRowsToContents();

#---------display verb attributs
        verbattributs=self.verb_attribut;
# display in grid
        self.TabVerbAttributsResult.clear();
##hide all columns

# display tenses in columns labels
        j=0;
        for key in verbattributs.keys():
            self.TabVerbAttributsResult.setVerticalHeaderItem(j,QtGui.QTableWidgetItem(key));
            self.TabVerbAttributsResult.setItem(j,0,QtGui.QTableWidgetItem(verbattributs[key]))
            j+=1;

        self.TabVerbAttributsResult.resizeColumnsToContents();
        self.TabVerbAttributsResult.resizeRowsToContents();

        #show result /
        self.TabVoice.show();
        self.MainWindow.showMaximized();
        self.TabVoice.setCurrentIndex(0);
        self.centralwidget.update();

# enable actions
        self.AExport.setEnabled(True)
        self.AFont.setEnabled(True)
        self.ACopy.setEnabled(True)
        self.APrint.setEnabled(True)
        self.APrintPreview.setEnabled(True)
        self.APagesetup.setEnabled(True)
        self.AZoomIn.setEnabled(True)
        self.AZoomOut.setEnabled(True)
        self.centralwidget.update();


    def do_sarf(self,word,future_type,all=True,past=False,future=False,passive=False,imperative=False,future_moode=False,confirmed=False,transitive=False,display_format="HTML"):
    	valid=is_valid_infinitive_verb(word)
    	listetenses=[];
    	if valid:
    		future_type=get_future_type_by_name(future_type);

    		bab_sarf=0;
    		vb=verbclass(word,transitive,future_type);
    		#vb.verb_class();
    		vb.set_display(display_format);
    	#test the uniformate function
    		if all :
    			if transitive :
##    				print "transitive";
    				listetenses=TableTense
    				result= vb.conjugate_all_tenses();
    			else:
##    				print "intransitive";
    				listetenses=TableIndicativeTense;
##    				print len(TableIndicativeTense)
    				result= vb.conjugate_all_tenses(listetenses);
    		else :
    			listetenses=[];
    			if past : listetenses.append(TensePast);
    			if (past and passive and transitive) : listetenses.append(TensePassivePast)
    			if future : listetenses.append(TenseFuture);
    			if (future and passive and transitive) : listetenses.append(TensePassiveFuture)
    			if (future_moode) :
    				listetenses.append(TenseSubjunctiveFuture)
    				listetenses.append(TenseJussiveFuture)
    			if (confirmed) :
    				if (future):listetenses.append(TenseConfirmedFuture);
    				if (imperative):listetenses.append(TenseConfirmedImperative);
    			if (future and passive and transitive and confirmed) :
    				listetenses.append(TensePassiveConfirmedFuture);
    			if (passive and transitive and future_moode) :
    				listetenses.append(TensePassiveSubjunctiveFuture)
    				listetenses.append(TensePassiveJussiveFuture)
    			if imperative : listetenses.append(TenseImperative)
    			result =vb.conjugate_all_tenses(listetenses);


    		self.result["HTML"]=vb.conj_display.display("HTML",listetenses)
    		self.result["TABLE"]=vb.conj_display.display("TABLE",listetenses)
    		self.result["TEXT"]=vb.conj_display.display("TEXT",listetenses)
    		self.result["TEX"]=vb.conj_display.display("TEX",listetenses)
    		self.result["CSV"]=vb.conj_display.display("CSV",listetenses)
    		self.result["XML"]=vb.conj_display.display("XML",listetenses)
    		self.verb_attribut=vb.conj_display.get_verb_attributs();
    		return result;
    	else: return None;


import qutrub_rc
