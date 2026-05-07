from PyQt5.QtWidgets import QApplication
from data_extractor_controller import DataExtractorController


app = QApplication([])
controller = DataExtractorController()
app.exec_()