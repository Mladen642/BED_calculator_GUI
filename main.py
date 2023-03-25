#Imports
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
import constructed_gui
from tkinter import messagebox as msgbox
import os

#Directry change
current_file_path = os.path.realpath(__file__)
script_directory = os.path.dirname(current_file_path)
os.chdir(script_directory)

class MyWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = constructed_gui.Ui_MainWindow()
        self.ui.setupUi(self)

        #Icon
        icon = QIcon('img/calc.ico')
        self.setWindowIcon(icon)

        # Buttons
        self.ui.calc_1.clicked.connect(self.calculate_BED1)
        self.ui.calc_2.clicked.connect(self.calculate_BED2)
        self.ui.calc_3.clicked.connect(self.calculate_BED3)
        self.ui.BED_add.clicked.connect(self.calculate_combo_plus)
        self.ui.BED_sub.clicked.connect(self.calculate_combo_minus)

    #Functions
    def calculate_BED1(self):
        try:
            n = self.ui.n_1_value.value()
            d = self.ui.d_1_value.value()
            alpha_beta = self.ui.alfabeta_1_value.value()
            TD = n * d
            BED_1  = round(TD * (1 + d/(alpha_beta)), 2)
            self.ui.result_1.setText(f'{str(BED_1)}'+' Gy')

            return BED_1
        except:
            msgbox.showerror("Error", "Please pick values first and then press calculate.")

    def calculate_BED2(self):
        try:
            n = self.ui.n_2_value.value()
            d = self.ui.d_2_value.value()
            alpha_beta = self.ui.alfabeta_2_value.value()
            TD = n * d
            BED_2 = round(TD * (1 + d/(alpha_beta)), 2)
            self.ui.result_2.setText(f'{str(BED_2)}'+' Gy')

            return BED_2
        except:
            msgbox.showerror("Error", "Please pick values first and then press calculate.")

    def calculate_BED3(self):
        try:
            n = self.ui.n_3_value.value()
            d = self.ui.d_3_value.value()
            alpha_beta = self.ui.alfabeta_3_value.value()
            TD = n * d
            BED_3 = round(TD * (1 + d/(alpha_beta)), 2)
            self.ui.result_3.setText(f'{str(BED_3)}'+' Gy')

            return BED_3
        except:
            msgbox.showerror("Error", "Please pick values first and then press calculate.")

    def calculate_combo_plus(self):
        try:
            x1 = self.calculate_BED1()
            x2 = self.calculate_BED2()
            x3 = self.calculate_BED3()

            if self.ui.check_bed1.isChecked() and self.ui.check_bed2.isChecked() and self.ui.check_bed3.isChecked():

                suma = x1 + x2 + x3
                self.ui.combinations_result_label.setText(f"{suma}"+" Gy")
            
            elif self.ui.check_bed1.isChecked() and self.ui.check_bed2.isChecked():
                suma = x1 + x2
                self.ui.combinations_result_label.setText(f"{suma}"+" Gy")

            elif self.ui.check_bed1.isChecked() and self.ui.check_bed3.isChecked():
                suma = x1+x3
                self.ui.combinations_result_label.setText(f"{suma}"+" Gy")
            
            elif self.ui.check_bed2.isChecked() and self.ui.check_bed3.isChecked():
                suma = x2+x3
                self.ui.combinations_result_label.setText(f"{suma}"+" Gy")
            else:
                msgbox.showwarning("Warning", "Please select which of the BEDs you would like to add together.")

        except:
            msgbox.showerror("Error!", "Please calculate the values first, and then try to add them")

    def calculate_combo_minus(self):
        try:
            x1 = self.calculate_BED1()
            x2 = self.calculate_BED2()
            x3 = self.calculate_BED3()

            if self.ui.check_bed1.isChecked() and self.ui.check_bed2.isChecked() and self.ui.check_bed3.isChecked():

                razlika = x1 - x2 - x3
                self.ui.combinations_result_label.setText(f"{razlika}"+" Gy")
            
            elif self.ui.check_bed1.isChecked() and self.ui.check_bed2.isChecked():
                razlika = x1 - x2
                self.ui.combinations_result_label.setText(f"{razlika}"+" Gy")

            elif self.ui.check_bed1.isChecked() and self.ui.check_bed3.isChecked():
                razlika = x1-x3
                self.ui.combinations_result_label.setText(f"{razlika}"+" Gy")
            
            elif self.ui.check_bed2.isChecked() and self.ui.check_bed3.isChecked():
                razlika = x2-x3
                self.ui.combinations_result_label.setText(f"{razlika}"+" Gy")
            else:
                msgbox.showwarning("Warning", "Please select which of the BEDs you would like to subtract.")

        except:
            msgbox.showerror("Error!", "Please calculate the values first, and then try to subtract them")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()