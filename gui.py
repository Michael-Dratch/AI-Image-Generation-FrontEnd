from PyQt6 import QtGui
from PyQt6.QtWidgets import QWidget

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.promptInput = None
        self.image = None
        self.imageContainer = None
        self.imageLoaded = False
        self.saveButton = None

    def getPrompt(self):
        return self.promptInput.text()

    def clearPrompt(self):
        self.promptInput.clear()

    def setImage(self, image):
        self.image = image
        pixmap = QtGui.QPixmap(image)
        self.imageContainer.setPixmap(pixmap)
        self.imageLoaded = True

    def activateSaveButton(self):
        self.saveButton.setEnabled(True)

    def setLoading(self):
        self.imageContainer.setText("Loading...")
