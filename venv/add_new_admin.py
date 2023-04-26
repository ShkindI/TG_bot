from PyQt5 import QtCore, QtGui, QtWidgets
from sucsessful_wndw import Ui_Sucsessful_windw
from error_wndw import Ui_Error_windw
from db_func import add_new_admin


class Ui_Add_admin(object):
    def setupUi(self, Add_admin):
        Add_admin.setObjectName("Add_admin")
        Add_admin.resize(543, 332)
        font = QtGui.QFont()
        font.setItalic(True)
        Add_admin.setFont(font)
        self.lineEdit_name_admin = QtWidgets.QLineEdit(Add_admin)
        self.lineEdit_name_admin.setGeometry(QtCore.QRect(30, 60, 191, 22))
        self.lineEdit_name_admin.setObjectName("lineEdit_name_admin")
        self.lineEdit_Phone_num = QtWidgets.QLineEdit(Add_admin)
        self.lineEdit_Phone_num.setGeometry(QtCore.QRect(280, 60, 191, 22))
        self.lineEdit_Phone_num.setObjectName("lineEdit_Phone_num")
        self.lineEdit_true_or_false_adm = QtWidgets.QLineEdit(Add_admin)
        self.lineEdit_true_or_false_adm.setGeometry(QtCore.QRect(30, 160, 191, 22))
        self.lineEdit_true_or_false_adm.setObjectName("lineEdit_true_or_false_adm")
        self.lineEdit_TG_id = QtWidgets.QLineEdit(Add_admin)
        self.lineEdit_TG_id.setGeometry(QtCore.QRect(280, 160, 191, 22))
        self.lineEdit_TG_id.setObjectName("lineEdit_TG_id")
        self.btn_confirm_add_admin = QtWidgets.QPushButton(Add_admin)
        self.btn_confirm_add_admin.setGeometry(QtCore.QRect(380, 210, 101, 81))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_confirm_add_admin.setFont(font)
        self.btn_confirm_add_admin.setObjectName("btn_confirm_add_admin")
        self.label_name_new_admin = QtWidgets.QLabel(Add_admin)
        self.label_name_new_admin.setGeometry(QtCore.QRect(30, 20, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_name_new_admin.setFont(font)
        self.label_name_new_admin.setObjectName("label_name_new_admin")
        self.lable_phone = QtWidgets.QLabel(Add_admin)
        self.lable_phone.setGeometry(QtCore.QRect(280, 20, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lable_phone.setFont(font)
        self.lable_phone.setObjectName("lable_phone")
        self.lable_true_false_admin = QtWidgets.QLabel(Add_admin)
        self.lable_true_false_admin.setGeometry(QtCore.QRect(30, 130, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lable_true_false_admin.setFont(font)
        self.lable_true_false_admin.setObjectName("lable_true_false_admin")
        self.label_tg_id = QtWidgets.QLabel(Add_admin)
        self.label_tg_id.setGeometry(QtCore.QRect(284, 130, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_tg_id.setFont(font)
        self.label_tg_id.setObjectName("label_tg_id")
        self.label_any_error = QtWidgets.QLabel(Add_admin)
        self.label_any_error.setGeometry(QtCore.QRect(34, 229, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_any_error.setFont(font)
        self.label_any_error.setText("")
        self.label_any_error.setObjectName("label_any_error")

        self.retranslateUi(Add_admin)
        QtCore.QMetaObject.connectSlotsByName(Add_admin)

    def retranslateUi(self, Add_admin):
        _translate = QtCore.QCoreApplication.translate
        Add_admin.setWindowTitle(_translate("Add_admin", "Add_new_admin"))
        self.btn_confirm_add_admin.setText(_translate("Add_admin", "Подтвердить"))
        self.label_name_new_admin.setText(_translate("Add_admin", "Имя нового администратора:"))
        self.lable_phone.setText(_translate("Add_admin", "Телефонный номер:"))
        self.lable_true_false_admin.setText(_translate("Add_admin", "Старший или младший(0 или 1)"))
        self.label_tg_id.setText(_translate("Add_admin", "Телеграм id (цифры)"))

        self.btn_confirm_add_admin.clicked.connect(self.add_admin)


    def check_phone_num(self):
        if self.lineEdit_Phone_num.text() != '':
            self.lineEdit_Phone_num.setText('')
            if self.lineEdit_Phone_num.text() != '375':
                self.label_any_error.setText('')
                if self.lineEdit_Phone_num.text().isdigit():
                    if len(self.lineEdit_Phone_num.text()) == 12:
                        self.label_any_error.setText('')
                        return True
                    else:
                        self.label_any_error.setText('Мало цифр для номера!')
                        return False
                else:
                    self.label_any_error.setText('Только цифры!!!')
                    return False
            else:
                self.label_any_error.setText('Вы ничего не ввели!')
                return False
        else:
            self.label_any_error.setText('Поле пустое!!!')
            return False


    def add_admin(self):
        self.lineEdit_name_admin.setReadOnly(True)
        self.lineEdit_Phone_num.setReadOnly(True)
        self.lineEdit_true_or_false_adm.setReadOnly(True)
        self.lineEdit_TG_id.setReadOnly(True)
        self.btn_confirm_add_admin.setDisabled(True)
        name = any(x.isdigit() for x in self.lineEdit_name_admin.text())
        # if self.check_phone_num != False: Эта калека отказалась работать, не могу поправить, ибо в корне не одупляю почему(
        if name == False:
            result = []
            result.append(self.lineEdit_name_admin.text())
            result.append(int(self.lineEdit_Phone_num.text()))
            result.append(int(self.lineEdit_true_or_false_adm.text()))
            result.append(int(self.lineEdit_TG_id.text()))
            response = add_new_admin(result)
            if response == True:
                sucsess = QtWidgets.QDialog()
                ui2 = Ui_Sucsessful_windw()
                ui2.setupUi(sucsess)
                sucsess.show()
                sucsess.exec_()
                self.lineEdit_name_admin.setReadOnly(True)
                self.lineEdit_Phone_num.setReadOnly(True)
                self.lineEdit_true_or_false_adm.setReadOnly(True)
                self.lineEdit_TG_id.setReadOnly(True)
                self.btn_confirm_add_admin.setDisabled(True)
            else:
                print(response)
                error = QtWidgets.QDialog()
                ui2 = Ui_Error_windw()
                ui2.setupUi(error)
                error.show()
                error.exec_()

                self.lineEdit_name_admin.setReadOnly(False)
                self.lineEdit_Phone_num.setReadOnly(False)
                self.lineEdit_true_or_false_adm.setReadOnly(False)
                self.lineEdit_TG_id.setReadOnly(False)
                self.btn_confirm_add_admin.setDisabled(False)
        else:
            self.lineEdit_name_admin.setReadOnly(False)
            self.lineEdit_Phone_num.setReadOnly(False)
            self.lineEdit_true_or_false_adm.setReadOnly(False)
            self.lineEdit_TG_id.setReadOnly(False)
            self.btn_confirm_add_admin.setDisabled(False)




# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Add_admin = QtWidgets.QDialog()
#     ui = Ui_Add_admin()
#     ui.setupUi(Add_admin)
#     Add_admin.show()
#     sys.exit(app.exec_())
