from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QFileDialog
from PyQt6.QtWidgets import *
from gui import GUI

class GuiBuilder:

    def __init__(self, controller):
        self.controller = controller

    def build(self):
        self.gui = GUI()
        self.gui.setGeometry(300, 300, 400, 400)
        self.gui.setWindowTitle("OpenAI Client")
        image = self.createImageWidget()
        promptForm = self.createPromptForm()
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(image, alignment=Qt.AlignmentFlag.AlignCenter)
        mainLayout.addLayout(promptForm)
        self.gui.setLayout(mainLayout)
        return self.gui

    def createPromptForm(self):
        promptInput = QLineEdit()
        self.gui.promptInput = promptInput
        promptInput.setPlaceholderText("Enter Prompt")
        submitButton = QPushButton("Generate Image")
        submitButton.clicked.connect(self.controller.submitButtonClicked)
        saveButton = QPushButton("Save Image")
        saveButton.clicked.connect(self.controller.saveButtonClicked)
        saveButton.setEnabled(False)
        self.gui.saveButton = saveButton
        promptForm = QHBoxLayout()
        promptForm.addWidget(promptInput)
        promptForm.addWidget(submitButton)
        promptForm.addWidget(saveButton)
        return promptForm

    def createImageWidget(self):
        imageContainer = QLabel()
        imageContainer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.gui.imageContainer = imageContainer
        return imageContainer
