from PyQt5 import QtCore, QtGui, QtWidgets
from add_new_admin import Ui_Add_admin
from db_func import del_admin_id
from db_func import change_info_admqt5
from sucsessful_wndw import Ui_Sucsessful_windw
from error_wndw import Ui_Error_windw


class Ui_Admins(object):
    def setupUi(self, Admins):
        Admins.setObjectName("Admins")
        Admins.resize(639, 341)
        self.tableWidget = QtWidgets.QTableWidget(Admins)
        self.tableWidget.setGeometry(QtCore.QRect(15, 11, 611, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.btn_add_new_admin = QtWidgets.QPushButton(Admins)
        self.btn_add_new_admin.setGeometry(QtCore.QRect(10, 230, 191, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_add_new_admin.setFont(font)
        self.btn_add_new_admin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add_new_admin.setObjectName("btn_add_new_admin")
        self.btn_change_admin = QtWidgets.QPushButton(Admins)
        self.btn_change_admin.setGeometry(QtCore.QRect(230, 230, 181, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_change_admin.setFont(font)
        self.btn_change_admin.setObjectName("btn_change_admin")
        self.btn_del_admin = QtWidgets.QPushButton(Admins)
        self.btn_del_admin.setGeometry(QtCore.QRect(440, 230, 181, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_del_admin.setFont(font)
        self.btn_del_admin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_del_admin.setObjectName("btn_del_admin")

        self.retranslateUi(Admins)
        QtCore.QMetaObject.connectSlotsByName(Admins)

    def retranslateUi(self, Admins):
        _translate = QtCore.QCoreApplication.translate
        Admins.setWindowTitle(_translate("Admins", "Admins"))
        self.btn_add_new_admin.setText(_translate("Admins", "Добавить нового"))
        self.btn_change_admin.setText(_translate("Admins", "Изменить данные"))
        self.btn_del_admin.setText(_translate("Admins", "Удалить админа"))

        self.btn_add_new_admin.clicked.connect(self.add_new_admin)
        self.btn_del_admin.clicked.connect(self.del_admin)
        self.btn_change_admin.clicked.connect(self.change_admin)

    def add_new_admin(self):
        app2 = QtWidgets.QDialog()
        ui2 = Ui_Add_admin()
        ui2.setupUi(app2)
        app2.show()
        app2.exec_()

    def del_admin(self):
        items = self.tableWidget.selectedItems()
        if items != [] and len(items) >= 4:
            id = items[0].text()
            id = int(id)
            response = del_admin_id(id)
            if response == True:
                sucsess = QtWidgets.QDialog()
                ui2 = Ui_Sucsessful_windw()
                ui2.setupUi(sucsess)
                sucsess.show()
                sucsess.exec_()
                self.btn_add_new_admin.setDisabled(True)
                self.btn_change_admin.setDisabled(True)
                self.btn_del_admin.setDisabled(True)
            else:
                print(response)
                error = QtWidgets.QDialog()
                ui2 = Ui_Error_windw()
                ui2.setupUi(error)
                error.show()
                error.exec_()

    def change_admin(self):
        items = self.tableWidget.selectedItems()
        if items != [] and len(items) >= 4:
            id = items[0].text()
            id = int(id)

            buffer = []

            for x in range(1, len(items)):
                buffer.append(items[x].text())
            response = change_info_admqt5(id, buffer)
            if response == True:
                sucsess = QtWidgets.QDialog()
                ui2 = Ui_Sucsessful_windw()
                ui2.setupUi(sucsess)
                sucsess.show()
                sucsess.exec_()
                self.btn_add_new_admin.setDisabled(True)
                self.btn_change_admin.setDisabled(True)
                self.btn_del_admin.setDisabled(True)
            else:
                print(response)
                error = QtWidgets.QDialog()
                ui2 = Ui_Error_windw()
                ui2.setupUi(error)
                error.show()
                error.exec_()


# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     Admins = QtWidgets.QDialog()
#     ui = Ui_Admins()
#     ui.setupUi(Admins)
#     Admins.show()
#     sys.exit(app.exec_())
