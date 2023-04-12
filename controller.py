import urllib
import openai
from PyQt6 import QtGui
from PyQt6.QtWidgets import QFileDialog


class Controller:
    def __init__(self, app):
        self.app = app

    def setGUI(self, gui):
        self.gui = gui

    def submitButtonClicked(self):
        prompt = self.gui.getPrompt()
        self.gui.setLoading()
        self.app.processEvents()
        image = self.fetchImage(prompt)
        self.gui.setImage(image)
        self.gui.clearPrompt()
        self.gui.activateSaveButton()

    def saveButtonClicked(self):
        result = QFileDialog.getSaveFileName(self.gui,"Save Image", "",
                                          "Images (*.png *.xpm *.jpg)")
        dirPath = result[0]
        self.gui.image.save(dirPath)

    def fetchImage(self, prompt):
        size = "512x512"
        response = openai.Image.create(prompt=prompt,
                                       n=1,
                                       size=size)
        url = response["data"][0]["url"]
        data = urllib.request.urlopen(url).read()
        image = QtGui.QImage()
        image.loadFromData(data)
        return image



