from PyQt5 import QtWidgets
import puqt_sql
import connection




class mywindow(QtWidgets.QMainWindow, puqt_sql.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

    def button_click(self):
        fnstring = self.lineEdit.text()
        lnstring = self.lineEdit_2.text()
        print(fnstring,lnstring)
        request = "INSERT INTO table1 (fn,ln) VALUES('" + fnstring + "','" + lnstring + "');"
        connection.conn(request)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    window.pushButton.clicked.connect(window.button_click)

    sys.exit(app.exec_())