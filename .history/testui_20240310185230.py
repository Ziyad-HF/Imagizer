# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(989, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(20, 30, 201, 521))
        self.toolBox.setObjectName("toolBox")
        self.noise = QtWidgets.QWidget()
        self.noise.setGeometry(QtCore.QRect(0, 0, 201, 428))
        self.noise.setObjectName("noise")
        self.gridLayout = QtWidgets.QGridLayout(self.noise)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radio_uniform = QtWidgets.QRadioButton(self.noise)
        self.radio_uniform.setObjectName("radio_uniform")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radio_uniform)
        self.verticalLayout.addWidget(self.radio_uniform)
        self.radio_gaus = QtWidgets.QRadioButton(self.noise)
        self.radio_gaus.setObjectName("radio_gaus")
        self.buttonGroup.addButton(self.radio_gaus)
        self.verticalLayout.addWidget(self.radio_gaus)
        self.radio_sp = QtWidgets.QRadioButton(self.noise)
        self.radio_sp.setObjectName("radio_sp")
        self.buttonGroup.addButton(self.radio_sp)
        self.verticalLayout.addWidget(self.radio_sp)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.noise)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_intensity = QtWidgets.QWidget()
        self.page_intensity.setObjectName("page_intensity")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_intensity)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.page_intensity)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.uniform_intensity = QtWidgets.QSlider(self.page_intensity)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uniform_intensity.sizePolicy().hasHeightForWidth())
        self.uniform_intensity.setSizePolicy(sizePolicy)
        self.uniform_intensity.setOrientation(QtCore.Qt.Horizontal)
        self.uniform_intensity.setObjectName("uniform_intensity")
        self.verticalLayout_4.addWidget(self.uniform_intensity)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_intensity)
        self.page_gaus = QtWidgets.QWidget()
        self.page_gaus.setObjectName("page_gaus")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_gaus)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.page_gaus)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.gaus_std = QtWidgets.QSlider(self.page_gaus)
        self.gaus_std.setOrientation(QtCore.Qt.Horizontal)
        self.gaus_std.setObjectName("gaus_std")
        self.verticalLayout_3.addWidget(self.gaus_std)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.page_gaus)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.gaus_mean = QtWidgets.QSlider(self.page_gaus)
        self.gaus_mean.setOrientation(QtCore.Qt.Horizontal)
        self.gaus_mean.setObjectName("gaus_mean")
        self.verticalLayout_2.addWidget(self.gaus_mean)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_gaus)
        self.page_sp = QtWidgets.QWidget()
        self.page_sp.setObjectName("page_sp")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_sp)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.page_sp)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.gaus_mean_2 = QtWidgets.QSlider(self.page_sp)
        self.gaus_mean_2.setOrientation(QtCore.Qt.Horizontal)
        self.gaus_mean_2.setObjectName("gaus_mean_2")
        self.verticalLayout_5.addWidget(self.gaus_mean_2)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.page_sp)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.gaus_mean_3 = QtWidgets.QSlider(self.page_sp)
        self.gaus_mean_3.setOrientation(QtCore.Qt.Horizontal)
        self.gaus_mean_3.setObjectName("gaus_mean_3")
        self.verticalLayout_6.addWidget(self.gaus_mean_3)
        self.gridLayout_4.addLayout(self.verticalLayout_6, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_sp)
        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.toolBox.addItem(self.noise, "")
        self.edges = QtWidgets.QWidget()
        self.edges.setGeometry(QtCore.QRect(0, 0, 201, 428))
        self.edges.setObjectName("edges")
        self.toolBox.addItem(self.edges, "")
        self.thresholding = QtWidgets.QWidget()
        self.thresholding.setObjectName("thresholding")
        self.toolBox.addItem(self.thresholding, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 989, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        self.slider_map = {
            
            self.radio_uniform: 0,
            self.radio_gaus: 1,
            self.radio_sp: 2,
             
        }
        
        
        for radio in [self.radio_uniform, self.radio_gaus, self.radio_sp]:
            radio.clicked.connect(self.set_stacked_widget)
        
        
        
        
        
    def set_stacked_widget(self):
        pressed_radio = self.sender()
        self.stackedWidget.setCurrentIndex(self.slider_map[pressed_radio])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radio_uniform.setText(_translate("MainWindow", "Uniform"))
        self.radio_gaus.setText(_translate("MainWindow", "Gaussian"))
        self.radio_sp.setText(_translate("MainWindow", "Salt and Pepper"))
        self.label.setText(_translate("MainWindow", "Intensity:"))
        self.label_2.setText(_translate("MainWindow", "Mean:"))
        self.label_3.setText(_translate("MainWindow", "StandardDev:"))
        self.label_4.setText(_translate("MainWindow", "Salt Probability"))
        self.label_5.setText(_translate("MainWindow", "Pepper Probability"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.noise), _translate("MainWindow", "Noise/Smoothing"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.edges), _translate("MainWindow", "Edges"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.thresholding), _translate("MainWindow", "Thresholding"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
