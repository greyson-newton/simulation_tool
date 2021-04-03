import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)
from plotter import plotter


# class MplCanvas(FigureCanvasQTAgg):

#     def __init__(self, parent=None, width=5, height=4, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
#         super(MplCanvas, self).__init__(fig)

class WidgetGallery(QDialog):
	def __init__(self, parent=None):
		super(WidgetGallery, self).__init__(parent)

		self.originalPalette = QApplication.palette()

		self.option1 = False
		self.option2 = False
		self.option3 = False

		self.sim_x = QRadioButton("Fractals").setChecked(self.option1)
		self.sim_xx = QRadioButton("Schrodinger").setChecked(self.option2)
		self.sim_xxx = QRadioButton("MC Integration").setChecked(self.option3)
		self.npts_entry = QLineEdit('number of points')
		self.interval_entry = QLineEdit('')
		self.function_entry = QLineEdit('')
		self.sim_option = 0
		self.BLlayout = QGridLayout()
		self.data_option = 0


		self.plott = plotter()

		styleComboBox = QComboBox()
		styleComboBox.addItems(QStyleFactory.keys())
		styleLabel = QLabel("&Style:")
		styleLabel.setBuddy(styleComboBox)
		self.useStylePaletteCheckBox = QCheckBox("&Use style's standard palette")
		self.useStylePaletteCheckBox.setChecked(True)

		disableWidgetsCheckBox = QCheckBox("&Disable widgets")

		self.createTLBox()
		self.createTRBox()
		self.BLBox = QGroupBox("Data Input")
		self.createBRBox()

		styleComboBox.activated[str].connect(self.changeStyle)
		self.useStylePaletteCheckBox.toggled.connect(self.changePalette)


		topLayout = QHBoxLayout()
		topLayout.addWidget(styleLabel)
		topLayout.addWidget(styleComboBox)
		topLayout.addStretch(1)
		topLayout.addWidget(self.useStylePaletteCheckBox)
		topLayout.addWidget(disableWidgetsCheckBox)

		mainLayout = QGridLayout()
		mainLayout.addLayout(topLayout, 0, 0, 1, 2)
		mainLayout.addWidget(self.TLBox, 1, 0)
		mainLayout.addWidget(self.TRBox, 1, 1)
		mainLayout.addWidget(self.BLBox, 2, 0)
		mainLayout.addWidget(self.BRBox, 2, 1)
		mainLayout.setRowStretch(1, 1)
		mainLayout.setRowStretch(2, 1)
		mainLayout.setColumnStretch(0, 1)
		mainLayout.setColumnStretch(1, 1)
		self.setLayout(mainLayout)

		self.setWindowTitle("Styles")
		self.changeStyle('Windows')

	def changeStyle(self, styleName):
		QApplication.setStyle(QStyleFactory.create(styleName))
		self.changePalette()

	def reset_pressed(self):

		self.plott.reset()
		self.sim_x = QRadioButton("Fractals")
		self.sim_xx = QRadioButton("Schrodinger")
		self.sim_xxx = QRadioButton("MC Integration")
		self.sim_option = 0
		self.npts_entry = QLineEdit('')
		self.data_option = 0
		self.option1 = False
		self.option2 = False
		self.option3 = False

	def save_pressed(self):
		self.plott.save()

	def start_calculation(self):

		self.npts = self.npts_entry.text()

		if self.sim_option=='1':
			self.plott.calculate(1,self.npts)
		if self.sim_option=='2':
			self.plott.calculate(2,self.npts)
		if self.sim_option=='3':
			self.plott.calculate(3,self.npts)

	def start_plot(self):
		if self.sim_option=='1':
			self.plott.plot(1,self.npts)
		if self.sim_option=='2':
			self.plott.plot(1,self.npts)
		if self.sim_option=='3':
			self.plott.plot(1,self.npts)

	def data_manager(self):
		if self.data_option == 1: #start data collection
			self.option1=self.sim_x.isChecked()
			self.option2=self.sim_xx.isChecked()
			self.option3=self.sim_xxx.isChecked()
			self.sim_option = self.checkOption()
			if self.sim_option == 1 : #fractals
				self.populateBLBox(1)
				print('populating fractals')
			if self.sim_option == 2 :
				self.populateBLBox(2) # Schrodinger
				print('populating schrodinger')
			if self.sim_option == 3 : 
				self.populateBLBox(3)# MC Integrator
				print('populating MC')
			#disableWidgetsCheckBox.toggled.connect(self.bottomLeftTabWidget.setDisabled)
		elif self.data_option == 2:

			self.npts = int(float(self.npts_entry.text()))
			if self.sim_option == 1 : #fractals
				print('calculating fractals...')
				self.plott.calculate_option1(self.npts,self.a_entry.text(),
					self.b_entry.text(),self.c_entry.text(),self.d_entry.text(),
					self.e_entry.text(),self.f_entry.text(),self.p_entry.text())
				print('done w fractals')
			if self.sim_option == 2 :
				#self.populateBLBox(2) # Schrodinger
				print('populating schrodinger')
			if self.sim_option == 3 : 

				a = float(self.interval[0])
				b = float(self.interval[1])
				print('calculating mc integration')
				self.plott.calculate_option3(self.npts,a,b)
				print('done w mc integration')

		 #save collected data
			self.interval = []
			self.interval = self.interval_entry.text().strip().split(',')
			self.function = self.function_entry.text()

	def changePalette(self):
		if (self.useStylePaletteCheckBox.isChecked()):
			QApplication.setPalette(QApplication.style().standardPalette())
		else:
			QApplication.setPalette(self.originalPalette)


	def createTLBox(self):

		self.TLBox = QGroupBox("Sim Selection")

		self.sim_x = QRadioButton("Fractals")
		self.sim_x.setChecked(False)

		self.sim_xx = QRadioButton("Schrodinger")
		self.sim_xx.setChecked(False)

		self.sim_xxx = QRadioButton("MC Integration")
		self.sim_xxx.setChecked(False)
		layout = QVBoxLayout()
		layout.addWidget(self.sim_x)
		layout.addWidget(self.sim_xx)
		layout.addWidget(self.sim_xxx)

		strt_btn = QPushButton("Select Simulation")
		self.data_option = 1
		strt_btn.clicked.connect(self.data_manager)
		layout.addWidget(strt_btn)
		layout.addStretch(1)
		self.TLBox.setLayout(layout)

	def populateBLBox(self,simoption):		

		if simoption == 1 : # fractals
			self.a_entry = QLineEdit('a constants (,)')
			self.b_entry = QLineEdit('b constants (,)')
			self.c_entry = QLineEdit('c constants (,)')
			self.d_entry = QLineEdit('d constants (,)')
			self.e_entry = QLineEdit('e constants (,)')
			self.f_entry = QLineEdit('f constants (,)')
			self.p_entry = QLineEdit('probabilities (,)')
			self.BLlayout.addWidget(self.npts_entry)
			self.BLlayout.addWidget(self.a_entry)
			self.BLlayout.addWidget(self.b_entry)
			self.BLlayout.addWidget(self.c_entry)
			self.BLlayout.addWidget(self.d_entry)
			self.BLlayout.addWidget(self.e_entry)
			self.BLlayout.addWidget(self.f_entry)
			self.BLlayout.addWidget(self.p_entry)
			self.BLBox.setLayout(self.BLlayout)
		if simoption == 2 : # Schrodinger
			print('schrodingers fill in')
			
		if simoption == 3 : # MC Integrator
		
			self.interval_entry = QLineEdit('a,b')
			self.function_entry = QLineEdit('f(r)=')

			#Saving Data
			self.data_option = 2
			start_button = QPushButton("Save Data", self)
			start_button.clicked.connect(self.data_manager)
			self.BLlayout.addWidget(self.npts_entry)
			self.BLlayout.addWidget(self.interval_entry)
			self.BLlayout.addWidget(self.function_entry)
	
			self.BLlayout.addWidget(start_button)
			self.BLBox.setLayout(self.BLlayout)

	def checkOption(self):

		if self.option1 == self.option2 == self.option3:
			print("select a simulation")
		elif (self.option1 == self.option2) and self.option1:
			print("here")
			return 1
		elif (self.option1 == self.option3) and self.option2:
			return 2
		elif (self.option1 == self.option2) and self.option3:
			return 3
		else:
			print("Choose exactly one simulation")
			return 0

	def resetBottomLeftTabWidget(self):
		if self.sim_option == 1 :
			self.BLGlayout.removeWidget(self.a_entry)
			self.BLGlayout.removeWidget(self.b_entry)
			self.BLGlayout.removeWidget(self.c_entry)
			self.BLGlayout.removeWidget(self.d_entry)
			self.BLGlayout.removeWidget(self.e_entry)
			self.BLGlayout.removeWidget(self.f_entry)
			self.BLGlayout.removeWidget(self.p_entry)

	def createBLBox(self, simoption):
		# which simulation to run
		self.BLBox = QGroupBox("Data Entry")
		self.BLBox.setCheckable(True)
		self.BLBox.setChecked(True)
		self.BLBox.setLayout(self.BLlayout)

	def createBRBox(self):
		self.BRBox = QGroupBox("Simulation Manager")
		layout = QGridLayout()

		start_button = QPushButton("Start Simulation", self)
		start_button.clicked.connect(self.start_plot)

		save_button = QPushButton("Save Results", self)
		save_button.clicked.connect(self.save_pressed)

		reset_button = QPushButton("Reset Simulator", self)
		reset_button.clicked.connect(self.reset_pressed)

		layout.addWidget(start_button)
		layout.addWidget(save_button)
		layout.addWidget(reset_button)
		self.BRBox.setLayout(layout)

	def createTRBox(self):
		self.TRBox = QGroupBox("Group 2")

		defaultPushButton = QPushButton("Default Push Button")
		defaultPushButton.setDefault(True)

		togglePushButton = QPushButton("Toggle Push Button")
		togglePushButton.setCheckable(True)
		togglePushButton.setChecked(True)

		flatPushButton = QPushButton("Flat Push Button")
		flatPushButton.setFlat(True)

		layout = QVBoxLayout()
		layout.addWidget(defaultPushButton)
		layout.addWidget(togglePushButton)
		layout.addWidget(flatPushButton)
		layout.addStretch(1)
		self.TRBox.setLayout(layout)


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_()) 




