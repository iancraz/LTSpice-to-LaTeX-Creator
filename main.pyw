import LTspiceToTexConverter as t
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QFileDialog,QMessageBox
from userInterface import *
from about import *
import sys

PATH = r'C:\Users\Ian Diaz\Documents\LTspiceXVII\lib\sym'

class Logic(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.path = PATH
        self.actionAbout.triggered.connect(self.about)
        self.actionSave.triggered.connect(self.save)
        self.searchFileButton.clicked.connect(self.searchFile)
        self.goButton.clicked.connect(self.resolve)
        self.copyButton.clicked.connect(self.copyToClipboard)
    
    def searchFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"File Selection", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.lineEdit.setText(fileName)
    
    def resolve(self):
        if self.lineEdit.text() is not '' and self.lineEdit.text()[-3:] == 'asc':
            temp = t.LtSpiceToLatex(filenameLTspice = self.lineEdit.text(), lt_spice_directory = r'C:\Users\Ian Diaz\Documents\LTspiceXVII\lib\sym')
            _translate = QtCore.QCoreApplication.translate
            self.text = temp
            temp = temp.replace('\n','<br>')
            self.latexTextEdit.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"+temp+"</p></body></html>"))
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("Wrong File!")
            self.msg.setInformativeText("The file you have chosen is not '.asc', please choose a correct file.")
            self.msg.setWindowTitle("Error")
            self.msg.exec_()

    def about(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_About()
        self.ui.setupUi(self.window)
        self.window.show()

    def save(self):
        if self.lineEdit.text() is not '' and self.lineEdit.text()[-3:] == 'asc':
            t.LtSpiceToLatex(filenameLTspice = self.lineEdit.text(), lt_spice_directory = self.path,fullExample=1,save = True)
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("Wrong File!")
            self.msg.setInformativeText("The file you have chosen is not '.asc', please choose a correct file.")
            self.msg.setWindowTitle("Error")
            self.msg.exec_()
        return
    
    def copyToClipboard(self):
        if self.latexTextEdit.toPlainText() != "":
            cb = QtWidgets.QApplication.clipboard()
            cb.clear(mode=cb.Clipboard )
            cb.setText(self.latexTextEdit.toPlainText(), mode=cb.Clipboard)
        return
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Logic()
    window.show()
    app.exec_()
