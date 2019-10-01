# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kk.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import time
from configparser import ConfigParser

from PyQt5.QtWidgets import QApplication

import threading

import autoThread


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(351, 461)
        MainWindow.setMinimumSize(QtCore.QSize(351, 461))
        MainWindow.setMaximumSize(QtCore.QSize(351, 461))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.model = QtWidgets.QComboBox(self.centralwidget)
        self.model.setGeometry(QtCore.QRect(20, 18, 65, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.model.setFont(font)
        self.model.setObjectName("model")
        self.model.addItem("")
        self.model.addItem("")
        self.model.addItem("")
        self.model.addItem("")
        self.person_self = QtWidgets.QCheckBox(self.centralwidget)
        self.person_self.setGeometry(QtCore.QRect(110, 20, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.person_self.setFont(font)
        self.person_self.setChecked(True)
        self.person_self.setObjectName("person_self")
        self.person_captain = QtWidgets.QCheckBox(self.centralwidget)
        self.person_captain.setGeometry(QtCore.QRect(180, 20, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.person_captain.setFont(font)
        self.person_captain.setObjectName("person_captain")
        self.person_member = QtWidgets.QCheckBox(self.centralwidget)
        self.person_member.setGeometry(QtCore.QRect(250, 20, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.person_member.setFont(font)
        self.person_member.setObjectName("person_member")
        self.task_reject = QtWidgets.QCheckBox(self.centralwidget)
        self.task_reject.setGeometry(QtCore.QRect(20, 50, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.task_reject.setFont(font)
        self.task_reject.setChecked(True)
        self.task_reject.setObjectName("task_reject")
        self.task_accept = QtWidgets.QCheckBox(self.centralwidget)
        self.task_accept.setGeometry(QtCore.QRect(170, 50, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.task_accept.setFont(font)
        self.task_accept.setObjectName("task_accept")
        self.limit = QtWidgets.QCheckBox(self.centralwidget)
        self.limit.setGeometry(QtCore.QRect(20, 80, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.limit.setFont(font)
        self.limit.setObjectName("limit")
        self.limit_num = QtWidgets.QLineEdit(self.centralwidget)
        self.limit_num.setEnabled(False)
        self.limit_num.setGeometry(QtCore.QRect(130, 80, 61, 20))
        self.limit_num.setObjectName("limit_num")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setGeometry(QtCore.QRect(20, 110, 71, 23))
        self.btn_start.setObjectName("btn_start")
        self.log = QtWidgets.QTextBrowser(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(20, 150, 311, 281))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.log.setFont(font)
        self.log.setObjectName("log")
        self.btn_end = QtWidgets.QPushButton(self.centralwidget)
        self.btn_end.setEnabled(False)
        self.btn_end.setGeometry(QtCore.QRect(100, 110, 71, 23))
        self.btn_end.setObjectName("btn_end")
        self.log_flag = QtWidgets.QCheckBox(self.centralwidget)
        self.log_flag.setGeometry(QtCore.QRect(250, 130, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.log_flag.setFont(font)
        self.log_flag.setChecked(True)
        self.log_flag.setObjectName("log_flag")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionb = QtWidgets.QAction(MainWindow)
        self.actionb.setObjectName("actionb")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        """自定义规则"""
        self.person_self.clicked.connect(lambda: self.selfChecked())
        self.person_captain.clicked.connect(lambda: self.captainChecked())
        self.person_member.clicked.connect(lambda: self.memberChecked())
        self.task_accept.clicked.connect(lambda: self.acceptChecked())
        self.task_reject.clicked.connect(lambda: self.rejectChecked())
        self.limit.clicked.connect(lambda: self.limitChecked())
        self.btn_start.clicked.connect(lambda: self.startClick())
        self.btn_end.clicked.connect(lambda: self.endClick())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "齐天大圣 v_1.0"))
        self.model.setItemText(0, _translate("MainWindow", "御魂"))
        self.model.setItemText(1, _translate("MainWindow", "觉醒"))
        self.model.setItemText(2, _translate("MainWindow", "御灵"))
        self.model.setItemText(3, _translate("MainWindow", "探索"))
        self.person_self.setText(_translate("MainWindow", "单人"))
        self.person_captain.setText(_translate("MainWindow", "队长"))
        self.person_member.setText(_translate("MainWindow", "队员"))
        self.task_reject.setText(_translate("MainWindow", "自动拒绝协作"))
        self.task_accept.setText(_translate("MainWindow", "自动接受协作"))
        self.limit.setText(_translate("MainWindow", "限制次数："))
        self.btn_start.setText(_translate("MainWindow", "开始"))
        self.log.setHtml(_translate("MainWindow",
                                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                    "p, li { white-space: pre-wrap; }\n"
                                    "</style></head><body style=\" font-family:\'SimSun\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btn_end.setText(_translate("MainWindow", "停止"))
        self.log_flag.setText(_translate("MainWindow", "存日志"))
        self.actionb.setText(_translate("MainWindow", "b"))

    logStr = ""

    """勾选“单人”后，取消另外两个"""
    def selfChecked(self):
        if self.person_self.isChecked():
            self.person_captain.setChecked(False)
            self.person_member.setChecked(False)
        else:
            self.person_self.setChecked(True)

    """勾选“队长”后，取消另外两个"""
    def captainChecked(self):
        if self.person_captain.isChecked():
            self.person_self.setChecked(False)
            self.person_member.setChecked(False)
        else:
            self.person_captain.setChecked(True)

    """勾选“队员”后，取消另外两个"""
    def memberChecked(self):
        if self.person_member.isChecked():
            self.person_self.setChecked(False)
            self.person_captain.setChecked(False)
        else:
            self.person_member.setChecked(True)

    """勾选“接受协作”后，取消另外一个"""
    def acceptChecked(self):
        if self.task_accept.isChecked():
            self.task_reject.setChecked(False)
        else:
            self.task_accept.setChecked(True)

    """勾选“拒绝协作”后，取消另外一个"""
    def rejectChecked(self):
        if self.task_reject.isChecked():
            self.task_accept.setChecked(False)
        else:
            self.task_reject.setChecked(True)

    """点击“限制次数”后，控制后面的输入框"""
    def limitChecked(self):
        if self.limit.isChecked():
            self.limit_num.setEnabled(True)
        else:
            self.limit_num.setEnabled(False)

    """点击“开始”按钮"""
    def startClick(self):
        self.addMsg("即将开始...")
        checkRes = self.initCheck()
        if checkRes != "ok":
            self.addMsg(checkRes)
            return
        if self.limit.isChecked() and not self.limitNumCheck():
            self.addMsg("限制次数无效，请输入整数")
            return
        model = self.model.currentText()
        person = self.getPerson()
        limitNum = -1 if (not self.limit.isChecked()) else self.limit_num.text().strip()
        if model != "御魂" or person != "self":
            self.addMsg("目前只支持 御魂-单人 ...其他功能正在开发中...")
            return
        self.enableAllFalse()
        self.btn_start.setEnabled(False)
        self.btn_end.setEnabled(True)
        # 启动线程
        autoThread.runFlag = True
        autoThread.taskFlag = self.getDealTask()
        self.__t = threading.Thread(target=autoThread.run, name='autoThread', args=(model, int(limitNum)))
        self.__t.start()

    """点击“停止”按钮"""
    def endClick(self):
        self.enableAllTrue()
        self.btn_end.setEnabled(False)
        self.btn_start.setEnabled(True)

        autoThread.runFlag = False
        self.addMsg("停止")

    """设置其他控件不可用"""
    def enableAllFalse(self):
        self.model.setEnabled(False)
        self.person_self.setEnabled(False)
        self.person_captain.setEnabled(False)
        self.person_member.setEnabled(False)
        self.task_accept.setEnabled(False)
        self.task_reject.setEnabled(False)
        self.limit.setEnabled(False)
        self.limit_num.setEnabled(False)
        self.log_flag.setEnabled(False)

    """设置其他控件可用"""
    def enableAllTrue(self):
        self.model.setEnabled(True)
        self.person_self.setEnabled(True)
        self.person_captain.setEnabled(True)
        self.person_member.setEnabled(True)
        self.task_accept.setEnabled(True)
        self.task_reject.setEnabled(True)
        self.limit.setEnabled(True)
        if self.limit.isChecked():
            self.limit_num.setEnabled(True)
        self.log_flag.setEnabled(True)

    """在log框内添加消息"""
    def addMsg(self, msg):
        log = "[" + time.strftime("%Y-%m-%d %H:%M:%S") + "]\n" + msg + "\n"
        self.logStr += log
        self.log.setText(self.logStr)
        self.log.moveCursor(self.log.textCursor().End)
        QApplication.processEvents()

    """初始化校验"""
    def initCheck(self):
        self.addMsg("初始化校验中...")
        cfg = ConfigParser()
        cfg_file = "config.ini"
        cfg.read(cfg_file)
        fileNames = cfg.get("define", "fileNames").split(",")
        for fileName in fileNames:
            file = cfg.get("resource", fileName)
            isExist = os.path.exists(file)
            if not isExist:
                return "文件\"{}\"不存在，启动失败！".format(file)
        self.addMsg("初始化校验完成")
        return "ok"

    """验证输入的限制次数是否是整数"""
    def limitNumCheck(self):
        limitNum = self.limit_num.text().strip()
        return limitNum.isdigit()

    def getPerson(self):
        if self.person_self.isChecked():
            return "self"
        elif self.person_captain.isChecked():
            return "captain"
        elif self.person_member.isChecked():
            return "member"

    def getDealTask(self):
        if self.task_accept.isChecked():
            return True
        elif self.task_reject.isChecked():
            return False