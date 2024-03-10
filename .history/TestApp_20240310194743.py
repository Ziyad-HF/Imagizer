from PyQt5.QtCore import Qt
import sys
from testui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
import pyqtgraph as pg
import cv2


class ImageEditor(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ImageEditor, self).__init__()
        self.setupUi(self)
        self.setup_plotwidgets()
        self.loaded_image = None
        self.img_item_input = pg.ImageItem()
        self.wgt_input_img.addItem(self.img_item_input)
        
            
        # Maps the radio button to the correspoiding slider page's index
        self.slider_map = {
            
            self.radio_uniform: 0,
            self.radio_gaus: 1,
            self.radio_sp: 2
        }
        
        # Connect radio buttons to function that sets sliders according to selection
        for radio in [self.radio_uniform, self.radio_gaus, self.radio_sp]:
            radio.toggled.connect(self.set_stacked_widget)
        
        # Connect Openfile Action to its function
        self.actionOpen_Image.triggered.connect(self.open_image)
        
        
        
    #TODO - Rename objects and comment to an appropriate object name
    # Sets the page of the stacked widget based on the radio button selected
    def set_stacked_widget(self):
        pressed_radio = self.toolBox.sender()
        if pressed_radio.isChecked():
            self.stackedWidget.setCurrentIndex(self.slider_map[pressed_radio])    
            
    def open_image(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Images (*.png *.jpg *.bmp *.tif)")
        file_dialog.setWindowTitle("Open Image File")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_() == QFileDialog.Accepted:
            selected_file = file_dialog.selectedFiles()[0]
            self.load_img_file(selected_file)
            
    def load_img_file(self, image_path):
        # Loads the image using imread, converts it to RGB, then rotates it 90 degrees clockwise
        self.loaded_image = cv2.rotate(cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB), cv2.ROTATE_90_CLOCKWISE)
        self.display_image(self.loaded_image)
        
    def display_image(self, image):
        self.img_item_input.setImage(image)
        self.remove_plotwidget_margins()
        
        
    ################################ Misc Functions ################################
    
    def setup_plotwidgets(self):
        for plotwidget in self.findChildren(pg.PlotWidget):
            plotwidget.showAxis('left', False)
            plotwidget.showAxis('bottom', False)
            
    def remove_plotwidget_margins(self):
        plotitem = self.wgt_input_img.getPlotItem()
        # plotitem.getViewBox().setContentsMargins(10,10,10,10)
        plotitem.getViewBox().setDefaultPadding(0)
        
        





app = QApplication(sys.argv)
win = ImageEditor() 
win.show()
app.exec()