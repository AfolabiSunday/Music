import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon


class PickFile(QWidget):

    def __init__(self):
        super().__init__()
        # self.title = 'PyQt5 file dialogs - pythonspot.com'
        # self.left = 10
        # self.top = 10
        # self.width = 640
        # self.height = 480
        #self.initUI()
        self.saveFileDialog()

    # def initUI(self):
    #     self.setWindowTitle('Load Music')
    #     self.setGeometry(10, 10, 640, 480)
    #
    #     self.openFileNameDialog()
    #     self.openFileNamesDialog()
    #     self.saveFileDialog()
    #
    #     self.show()
    #
    # def openFileNameDialog(self):
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     fileName, _ = QFileDialog.getOpenFileName(self, "Load Music", "",
    #                                               "All Files (Music);;Python Files (*.mp3)", options=options)
    #     if fileName:
    #         for files in fileName:
    #             print(files)
    #         print(fileName)
    #         quit(PickFile)
    #
    # def openFileNamesDialog(self):
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
    #                                             "All Files (*);;Python Files (*.py)", options=options)
    #     for file in files:
    #         print(file)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PickFile()
    sys.exit(app.exec_())