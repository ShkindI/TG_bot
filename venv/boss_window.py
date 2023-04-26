from PyQt5 import QtCore, QtGui, QtWidgets
from db_func import return_table_admins_for_qt5
from db_func import table_dish_for_qt5
from Admins import Ui_Admins
from Statistika_ui import Ui_Statistika
from Stop_list import Ui_Stop_list
from Statistics import return_stat
from All_bots import p1
from All_bots import p2


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(323, 464)
        Dialog.setMouseTracking(True)
        self.btn_on_off_TGbot = QtWidgets.QPushButton(Dialog)
        self.btn_on_off_TGbot.setGeometry(QtCore.QRect(30, 50, 111, 101))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_on_off_TGbot.setFont(font)
        self.btn_on_off_TGbot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_on_off_TGbot.setMouseTracking(False)
        self.btn_on_off_TGbot.setObjectName("btn_on_off_TGbot")
        self.btn_on_off_VKbot = QtWidgets.QPushButton(Dialog)
        self.btn_on_off_VKbot.setGeometry(QtCore.QRect(180, 50, 111, 101))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_on_off_VKbot.setFont(font)
        self.btn_on_off_VKbot.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_on_off_VKbot.setObjectName("btn_on_off_VKbot")
        self.label_TGbot = QtWidgets.QLabel(Dialog)
        self.label_TGbot.setGeometry(QtCore.QRect(34, 20, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_TGbot.setFont(font)
        self.label_TGbot.setAlignment(QtCore.Qt.AlignCenter)
        self.label_TGbot.setObjectName("label_TGbot")
        self.label_VKbot = QtWidgets.QLabel(Dialog)
        self.label_VKbot.setGeometry(QtCore.QRect(180, 20, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_VKbot.setFont(font)
        self.label_VKbot.setAlignment(QtCore.Qt.AlignCenter)
        self.label_VKbot.setObjectName("label_VKbot")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(34, 190, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btn_list_admins = QtWidgets.QPushButton(Dialog)
        self.btn_list_admins.setGeometry(QtCore.QRect(30, 230, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.btn_list_admins.setFont(font)
        self.btn_list_admins.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_list_admins.setMouseTracking(True)
        self.btn_list_admins.setAutoRepeat(False)
        self.btn_list_admins.setObjectName("btn_list_admins")
        self.btn_stoplist = QtWidgets.QPushButton(Dialog)
        self.btn_stoplist.setGeometry(QtCore.QRect(180, 230, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stoplist.setFont(font)
        self.btn_stoplist.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_stoplist.setObjectName("btn_stoplist")
        self.btn_statistic = QtWidgets.QPushButton(Dialog)
        self.btn_statistic.setGeometry(QtCore.QRect(30, 350, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_statistic.setFont(font)
        self.btn_statistic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_statistic.setObjectName("btn_statistic")
        self.btn_unic_statistica = QtWidgets.QPushButton(Dialog)
        self.btn_unic_statistica.setGeometry(QtCore.QRect(180, 350, 111, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_unic_statistica.setFont(font)
        self.btn_unic_statistica.setAutoRepeat(True)
        self.btn_unic_statistica.setObjectName("btn_unic_statistica")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Main_wndw_for_BOSS"))
        self.btn_on_off_TGbot.setText(_translate("Dialog", "Включить бота"))
        self.btn_on_off_VKbot.setText(_translate("Dialog", "Включить бота"))
        self.label_TGbot.setText(_translate("Dialog", "TG_bot"))
        self.label_VKbot.setText(_translate("Dialog", "VK_bot"))
        self.label.setText(_translate("Dialog", "только для TG_bot"))
        self.btn_list_admins.setText(_translate("Dialog", "Админы"))
        self.btn_stoplist.setText(_translate("Dialog", "Стоп лист"))
        self.btn_statistic.setText(_translate("Dialog", "Статистика"))
        self.btn_unic_statistica.setText(_translate("Dialog", "Unic Stat+"))

        self.btn_list_admins.clicked.connect(self.admins)
        self.btn_stoplist.clicked.connect(self.stop_list)
        self.btn_statistic.clicked.connect(self.stata)
        self.btn_unic_statistica.clicked.connect(self.unic_stat)
        self.btn_on_off_TGbot.clicked.connect(self.TG)
        self.btn_on_off_VKbot.clicked.connect(self.VK)

    def stop_list(self):  # Я не знаю почему он отображает не те данные, глянь на принт!
        tbl = table_dish_for_qt5()
        print(tbl[0].fetchall())
        print(tbl[1])

        app_stop_list = QtWidgets.QDialog()
        ui_stop_list = Ui_Stop_list()
        ui_stop_list.setupUi(app_stop_list)
        ui_stop_list.tableWidget.setColumnCount(len(tbl[1]))
        tbl = return_table_admins_for_qt5()
        ui_stop_list.tableWidget.setRowCount(len(tbl[0].fetchall()))
        tbl = return_table_admins_for_qt5()
        ui_stop_list.tableWidget.setHorizontalHeaderLabels(tbl[1])
        tbl = return_table_admins_for_qt5()

        index_row = 0

        for tuuple in tbl[0].fetchall():
            index_cow = 0
            for obj in tuuple:
                ui_stop_list.tableWidget.setItem(index_row, index_cow, QtWidgets.QTableWidgetItem(str(obj)))
                # ui2.tableWidget.setItem(index_row, index_cow, QtWidgets.QTableWidgetItem(str(obj)))
                index_cow += 1
            index_row += 1

        app_stop_list.show()
        app_stop_list.exec_()

    def admins(self):  # А тут все ровно, хотя запросы в таблицу идентичные и разбиты на разные функции...пиздэц
        tbl = return_table_admins_for_qt5()

        app_admins = QtWidgets.QDialog()
        ui_admins = Ui_Admins()
        ui_admins.setupUi(app_admins)
        ui_admins.tableWidget.setColumnCount(len(tbl[1]))
        tbl = return_table_admins_for_qt5()
        ui_admins.tableWidget.setRowCount(len(tbl[0].fetchall()))
        tbl = return_table_admins_for_qt5()
        ui_admins.tableWidget.setHorizontalHeaderLabels(tbl[1])
        tbl = return_table_admins_for_qt5()

        index_row = 0

        for tuuple in tbl[0].fetchall():
            index_cow = 0
            for obj in tuuple:
                ui_admins.tableWidget.setItem(index_row, index_cow, QtWidgets.QTableWidgetItem(str(obj)))
                index_cow += 1
            index_row += 1

        app_admins.show()
        app_admins.exec_()

    def stata(self):
        response = return_stat()
        app_stat = QtWidgets.QDialog()
        ui2 = Ui_Statistika()
        ui2.setupUi(app_stat)
        ui2.textEdit_stat.setText(response)
        app_stat.show()
        app_stat.exec_()

    def unic_stat(self):
        response = return_stat(unic=True)
        app_stat_unic = QtWidgets.QDialog()
        ui2 = Ui_Statistika()
        ui2.setupUi(app_stat_unic)
        ui2.textEdit_stat.setText(response)
        app_stat_unic.show()
        app_stat_unic.exec_()

    def TG(self):
        if self.btn_on_off_TGbot.text() == 'Включить бота':
            p1.start()
            self.btn_on_off_TGbot.setText('Откл. бота')
        else:
            print('отключат поток ты не умеешь, бездарь')
            # self.btn_on_off_TGbot.setText('Включить бота')

    def VK(self):
        if self.btn_on_off_VKbot.text() == 'Включить бота':
            p2.start()
            self.btn_on_off_VKbot.setText('Откл. бота')
        else:
            print('отключат поток ты не умеешь, бездарь')
            # self.btn_on_off_VKbot.setText('Включить бота')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
