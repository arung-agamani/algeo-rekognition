from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QFileDialog, QMessageBox
from PyQt5 import QtGui, QtCore
from dialog import Ui_Dialog
import app as appLogic

class AppWindow(QDialog) :
    def __init__ (self) :
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)        
        self.ui.randomizeButton.clicked.connect(self.randomClick)
        self.ui.loadDirectoryButton.clicked.connect(self.pickDirectory)
        self.ui.loadDatabaseButton.clicked.connect(self.pickDatabase)
        self.ui.saveDbButton.clicked.connect(self.saveDatabase)
        self.ui.batchProcessButton.clicked.connect(self.processDirToDb)
        self.ui.cosRadioButton.toggled.connect(lambda:self.matchMethod(self.ui.cosRadioButton))
        self.ui.euclidRadioButton.toggled.connect(lambda:self.matchMethod(self.ui.euclidRadioButton))

        self.curDbDir = 'No Database Loaded'
        self.matchingMethod = 1
        self.dirLoaded = False
        self.db = None
        self.show()

    def matchMethod(self, radio) :
        if radio.text() == 'Cosine Similarity' :
            if radio.isChecked() == True :
                print("Method switched : Cosine Similarity")
                self.matchingMethod = 1
            
        if radio.text() == 'Euclidean Distance' :
            if radio.isChecked() == True :
                print("Method switched : Euclidean Distance")
                self.matchingMethod = 2

    def pickDirectory(self) :
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if (directory != '') :
            self.ui.currentDirLabel.setText(directory)
            self.dirLoaded = True

    def pickDatabase(self) :
        database = str(QFileDialog.getOpenFileName(self, "Select Database", "./", "Pickle file (*.pck)")[0])
        if (database != '') :
            self.ui.currentDbLabel.setText(database)
            self.loadDatabase()
    
    def saveDatabase(self) :
        db_dest = str(QFileDialog.getSaveFileName(self, "Save Database", "./extracted", "PIckle file (*.pck)")[0])
        # print(db_dest)
        if (self.db == None) :
            print("Empty database. Please load database or process a folder first.")
        else :
            print("Database is not empty. Proceeding to save database.")
            appLogic.write_db(self.db, db_dest)
    
    def loadDatabase(self) :
        # loads database to a file on this context
        db_path = self.ui.currentDbLabel.text()
        self.db = appLogic.loadDb(db_path)
        print("Database loaded successfully")

    def processDirToDb(self) :
        if self.dirLoaded :
            currentDir = self.ui.currentDirLabel.text()
            if (currentDir == None) :
                self.showAlertBox("No directory selected. Aborting.")
            else :
                print("Processing...")
                self.db = appLogic.batch_extract(currentDir)
                if (self.db != None) :
                    print("Database has loaded with the current directory.")
                    self.curDbDir = currentDir
                    self.ui.currentDbLabel.setText("Using volatile database.")
        else :
            self.showAlertBox("No directory selected.")
    
    def changeTestImage(self, filename) :
        image_path = filename
        image_profile = QtGui.QImage(image_path)
        image_profile = image_profile.scaled(350, 350, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.ui.testImage.setPixmap(QtGui.QPixmap.fromImage(image_profile))
    
    def randomClick(self):
        if self.dirLoaded :
            image_path = appLogic.random_sampling(self.ui.currentDirLabel.text())
            currentDir = self.curDbDir
            image_profile = QtGui.QImage(image_path)
            stringFormat = ""
            image_profile = image_profile.scaled(350, 350, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
            self.ui.testImage.setPixmap(QtGui.QPixmap.fromImage(image_profile))
            self.matches_arr = None
            if self.matchingMethod == 1 :
                # Cosine similarity == 1
                self.matches_arr = appLogic.match(image_path, self.db)
                stringFormat = "{}%"
            if self.matchingMethod == 2 :
                # Euclidean Distance == 2
                self.matches_arr = appLogic.match_euclid(image_path, self.db)
                stringFormat = "{}"
    
            imgProf = QtGui.QImage(currentDir + '/' + str(self.matches_arr[1][0]))
            image_profile = imgProf.scaled(150, 150, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
            self.ui.resImage.setPixmap(QtGui.QPixmap.fromImage(image_profile))
            self.ui.matchRate.setText(stringFormat.format(int(round(self.matches_arr[1][1]*100))))

            imgProf = QtGui.QImage(currentDir + '/' + str(self.matches_arr[2][0]))
            image_profile = imgProf.scaled(150, 150, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
            self.ui.resImage_2.setPixmap(QtGui.QPixmap.fromImage(image_profile))
            self.ui.matchRate_2.setText(stringFormat.format(int(round(self.matches_arr[2][1]*100))))

            imgProf = QtGui.QImage(currentDir + '/' + str(self.matches_arr[3][0]))
            image_profile = imgProf.scaled(150, 150, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
            self.ui.resImage_3.setPixmap(QtGui.QPixmap.fromImage(image_profile))
            self.ui.matchRate_3.setText(stringFormat.format(int(round(self.matches_arr[3][1]*100))))

            imgProf = QtGui.QImage(currentDir + '/' + str(self.matches_arr[4][0]))
            image_profile = imgProf.scaled(150, 150, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
            self.ui.resImage_4.setPixmap(QtGui.QPixmap.fromImage(image_profile))
            self.ui.matchRate_4.setText(stringFormat.format(int(round(self.matches_arr[4][1]*100))))

            imgProf = QtGui.QImage(currentDir + '/' + str(self.matches_arr[5][0]))
            image_profile = imgProf.scaled(150, 150, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
            self.ui.resImage_5.setPixmap(QtGui.QPixmap.fromImage(image_profile))
            self.ui.matchRate_5.setText(stringFormat.format(int(round(self.matches_arr[5][1]*100))))
        else :
            self.showAlertBox("No directory loaded")

    def showAlertBox(self, msg) :
        alert = QMessageBox()
        alert.setText(msg)
        alert.setWindowTitle("Error")
        alert.setIcon(QMessageBox.Critical)
        alert.setStandardButtons(QMessageBox.Ok)
        alert.exec_()
    


app = QApplication([])
w = AppWindow()
w.show()
app.exec_()