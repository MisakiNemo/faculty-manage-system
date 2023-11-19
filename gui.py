# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog

import database as db
import datetime
import sys

app = QtWidgets.QApplication(sys.argv)


class login_Dialog(QMainWindow):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 90, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 140, 41, 16))
        self.label_2.setObjectName("label_2")
        self.username = QtWidgets.QLineEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(130, 90, 151, 21))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(130, 140, 151, 21))
        self.password.setObjectName("password")
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(140, 220, 101, 41))
        self.loginButton.setObjectName("loginButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "用户名"))
        self.label_2.setText(_translate("Dialog", "密码"))
        self.loginButton.setText(_translate("Dialog", "登录"))

    # 给登录按钮添加事件
    def addloginButton(self):
        self.loginButton.clicked.connect(self.login)

    def login(self):
        username = self.username.text()
        password = self.password.text()
        if db.login(username, password):
            self.close()
            self.ui = Ui_Dialog()
            self.ui.initUi()
            self.ui.show()

        else:
            QtWidgets.QMessageBox.warning(
                self.loginButton, '错误', '用户名或密码错误')


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(931, 529)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(610, 150, 72, 15))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 140, 51, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(260, 140, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 180, 31, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(240, 180, 41, 16))
        self.label_6.setObjectName("label_6")
        self.birth_date = QtWidgets.QDateEdit(Dialog)
        self.birth_date.setGeometry(QtCore.QRect(330, 130, 121, 31))
        self.birth_date.setObjectName("birth_date")
        self.searchButton = QtWidgets.QPushButton(Dialog)
        self.searchButton.setGeometry(QtCore.QRect(660, 140, 93, 28))
        self.searchButton.setObjectName("searchButton")
        self.messageTable = QtWidgets.QTableWidget(Dialog)
        self.messageTable.setGeometry(QtCore.QRect(60, 220, 811, 291))
        self.messageTable.setObjectName("messageTable")
        self.messageTable.setColumnCount(0)
        self.messageTable.setRowCount(0)
        self.staff_id = QtWidgets.QLineEdit(Dialog)
        self.staff_id.setGeometry(QtCore.QRect(120, 140, 113, 21))
        self.staff_id.setObjectName("staff_id")
        self.title = QtWidgets.QLineEdit(Dialog)
        self.title.setGeometry(QtCore.QRect(110, 180, 113, 21))
        self.title.setObjectName("title")
        self.addStaffButton = QtWidgets.QPushButton(Dialog)
        self.addStaffButton.setGeometry(QtCore.QRect(660, 100, 93, 28))
        self.addStaffButton.setObjectName("addStaffButton")
        self.addcourceButton = QtWidgets.QPushButton(Dialog)
        self.deleteStaffButton = QtWidgets.QPushButton(Dialog)
        self.deleteStaffButton.setGeometry(QtCore.QRect(780, 100, 93, 28))
        self.deleteStaffButton.setObjectName("deleteStaffButton")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(660, 180, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.deleteButton = QtWidgets.QPushButton(Dialog)
        self.deleteButton.setGeometry(QtCore.QRect(780, 180, 93, 28))
        self.deleteButton.setObjectName("deleteButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(280, 180, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(250, 20, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(70, 100, 425, 23))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.name = QtWidgets.QLabel(self.widget)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 0, 1, 1)
        self.nameInput = QtWidgets.QLineEdit(self.widget)
        self.nameInput.setText("")
        self.nameInput.setObjectName("nameInput")
        self.gridLayout.addWidget(self.nameInput, 0, 1, 1, 1)
        self.gender = QtWidgets.QLabel(self.widget)
        self.gender.setObjectName("gender")
        self.gridLayout.addWidget(self.gender, 0, 2, 1, 1)
        self.genderBox = QtWidgets.QComboBox(self.widget)
        self.genderBox.setObjectName("genderBox")
        self.genderBox.addItem("")
        self.genderBox.addItem("")
        self.genderBox.addItem("")
        self.gridLayout.addWidget(self.genderBox, 0, 3, 1, 1)
        self.department = QtWidgets.QLabel(self.widget)
        self.department.setObjectName("department")
        self.gridLayout.addWidget(self.department, 0, 4, 1, 1)
        self.departmentBox = QtWidgets.QComboBox(self.widget)
        self.departmentBox.setObjectName("departmentBox")
        self.gridLayout.addWidget(self.departmentBox, 0, 5, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "员工ID"))
        self.label_4.setText(_translate("Dialog", "出生日期"))
        self.label_5.setText(_translate("Dialog", "职位"))
        self.label_6.setText(_translate("Dialog", "工资"))
        self.searchButton.setText(_translate("Dialog", "搜索"))
        self.addStaffButton.setText(_translate("Dialog", "添加员工"))
        # self.addcourceButton.setText(_translate("Dialog", "添加课程"))
        self.deleteStaffButton.setText(_translate("Dialog", "删除员工"))
        self.pushButton_6.setText(_translate("Dialog", "修改信息"))
        self.deleteButton.setText(_translate("Dialog", "删除"))
        self.label.setText(_translate("Dialog", "    教职工管理系统"))
        self.name.setText(_translate("Dialog", "姓名"))
        self.gender.setText(_translate("Dialog", "性别"))
        self.genderBox.setItemText(0, _translate("Dialog", "男"))
        self.genderBox.setItemText(1, _translate("Dialog", "女"))
        self.genderBox.setItemText(2, _translate("Dialog", "不限"))
        self.department.setText(_translate("Dialog", "部门"))

        # 获取员工信息并添加进table中

    def getStaff(self):
        staff = db.getAllStaffs()
        self.messageTable.setColumnCount(6)
        self.messageTable.setRowCount(len(staff))
        self.messageTable.setHorizontalHeaderLabels(['员工ID', '姓名', '性别', '出生日期', '部门', '工资'])
        for i in range(len(staff)):
            for j in range(6):
                item = QtWidgets.QTableWidgetItem(str(staff[i][j]))
                if j == 0:
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.messageTable.setItem(i, j, item)

    # 获取部门信息并添加进下拉框中
    def getDepartment(self):
        department = db.getAllDepartMents()
        for i in range(len(department)):
            self.departmentBox.addItem(str(department[i][1]))

    # 添加员工
    def addStaff(self):
        name = self.nameInput.text()
        print(name)
        gender = self.genderBox.currentText()
        print(gender)
        birth_date = datetime.datetime.strptime(self.birth_date.text(), '%d/%m/%Y').strftime('%Y-%m-%d')
        print(birth_date)
        department = self.departmentBox.currentText()
        print(department)
        salary = self.lineEdit.text()
        print(type(salary))
        db.addStaff(name, gender, birth_date, department, salary)
        self.getStaff()

    # 打印点击的行

    def deleteStaff(self):
        row = self.messageTable.currentRow()
        staff_id = self.messageTable.item(row, 0).text()
        db.deleteStaff(staff_id)
        self.getStaff()

    def updateStaff(self):
        data = self.tableClick(self.messageTable.currentItem())
        print(data)
        db.updateStaff(data[0], data[1], data[2], data[3], data[4], data[5])
        print(data)
        self.getStaff()

    def tableClick(self, item):
        row = item.row()  # 获取行索引
        column_count = self.messageTable.columnCount()  # 获取列数
        data = []  # 用于存储行数据
        for column in range(column_count):
            data.append(self.messageTable.item(row, column).text())  # 获取每列的数据并添加到列表中
        return data

    def searchStaff(self):
        if self.nameInput.text() != '':
            staff = db.getStaffByName(self.nameInput.text())
            print(self.nameInput.text())
        elif self.staff_id.text() != '':
            staff = db.getStaffByID(self.staff_id.text())
        else:
            self.getStaff()
            return
        # 清空表格
        self.messageTable.setColumnCount(6)
        self.messageTable.setRowCount(len(staff))
        self.messageTable.setHorizontalHeaderLabels(['员工ID', '姓名', '性别', '出生日期', '部门', '工资'])
        print(staff)
        for i in range(len(staff)):
            for j in range(6):
                item = QtWidgets.QTableWidgetItem(str(staff[i][j]))
                if j == 0:
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.messageTable.setItem(i, j, item)

    # 给按钮绑定事件
    def bindButton(self):
        self.addStaffButton.clicked.connect(self.addStaff)
        self.messageTable.clicked.connect(self.tableClick)
        self.deleteStaffButton.clicked.connect(self.deleteStaff)
        self.pushButton_6.clicked.connect(self.updateStaff)
        self.searchButton.clicked.connect(self.searchStaff)

    def initUi(self):
        self.setupUi(self)
        self.getStaff()
        self.getDepartment()
        self.bindButton()


if __name__ == '__main__':
    login = login_Dialog()
    login.setupUi(login)
    login.addloginButton()
    login.show()
    sys.exit(app.exec_())
