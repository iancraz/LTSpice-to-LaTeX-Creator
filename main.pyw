import LTspiceToTexConverter as t
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QFileDialog
from userInterface import *
from about import *
import sys

class Logic(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.actionAbout.triggered.connect(self.about)
        self.actionSave.triggered.connect(self.save)
        self.searchFileButton.clicked.connect(self.searchFile)
        self.goButton.clicked.connect(self.resolve)
        # self.clearAllButton.clicked.connect(self.clearAll)
        # self.goButton.clicked.connect(self.resolve)
        # self.eqCreatorsList = [self.eqCreator_1, self.eqCreator_2, self.eqCreator_3, self.eqCreator_4, self.eqCreator_5,
        #                        self.eqCreator_6]
        # self.addButton.clicked.connect(self.addEquation)
        # self.clearAll()
    
    def searchFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.lineEdit.setText(fileName)
    def resolve(self):
        if self.lineEdit.text() is not '':
            temp = t.LtSpiceToLatex(filenameLTspice = self.lineEdit.text(), lt_spice_directory = r'C:\Users\Ian Diaz\Documents\LTspiceXVII\lib\sym')
            _translate = QtCore.QCoreApplication.translate
            temp = temp.replace('\n','<br>')
            self.latexTextEdit.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+temp+"</p></body></html>"))

    def about(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_About()
        self.ui.setupUi(self.window)
        self.window.show()

    def save(self):
        if self.lineEdit.text() != '':
            t.LtSpiceToLatex(filenameLTspice = self.lineEdit.text(), lt_spice_directory = r'C:\Users\Ian Diaz\Documents\LTspiceXVII\lib\sym',fullExample=1,save = True)
        return
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Logic()
    window.show()
    app.exec_()