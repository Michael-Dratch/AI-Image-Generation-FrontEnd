from PyQt6.QtWidgets import QApplication, QFileDialog
from PyQt6.QtWidgets import *
from guibuilder import GuiBuilder
from controller import Controller
class App:
    def start(self):
        application = QApplication([])
        controller = Controller(application)
        builder = GuiBuilder(controller)
        gui = builder.build()
        controller.setGUI(gui)
        gui.show()
        application.exec()


if __name__ == '__main__':
    app = App()
    app.start()
