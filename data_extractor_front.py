from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import uic

import os 

class DataExtractorView(QMainWindow):
	def __init__(self):
		super(DataExtractorView, self).__init__()
		uic.loadUi("./data_extractor_front.ui", self)
		self.show()

	def browse_file(self):
		document_name, _ = QFileDialog.getOpenFileName(self, "Selectionnez une facture")
		return document_name
	
	def show_output_information(self, document_json):
		self.output_text.setPlainText()