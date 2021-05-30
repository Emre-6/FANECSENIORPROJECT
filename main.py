import media4

import sys
app = media4.QtWidgets.QApplication(sys.argv)
MainWindow = media4.QtWidgets.QMainWindow()
ui = media4.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())