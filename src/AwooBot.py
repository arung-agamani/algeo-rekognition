from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QFileDialog, QMessageBox
from PyQt5 import QtGui, QtCore
from dialog import Ui_Dialog
import app as appLogic
import os.path

class AppWindow(QDialog) :
    def __init__ (self) :
        """Menghubungkan tiap tombol dalam GUI dengan metode yang akan dilakukan sebagai respon terhadap aksi pengguna."""
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
        self.ui.loadImageButton.clicked.connect(self.loadImageClick)
        self.ui.matchButton.clicked.connect(self.matchClick)

        """Inisialisasi keadaan awal program"""
        self.curDbDir = 'No Database Loaded'
        self.matchingMethod = 1
        self.dirLoaded = False
        self.db = None
        self.show()

        """Mengatur metode pencocokan (dengan cosine similarity atau euclidean distance) sesuai dengan pilihan pengguna."""
    def matchMethod(self, radio) :
        if radio.text() == 'Cosine Similarity' :
            if radio.isChecked() == True :
                print("Method switched : Cosine Similarity")
                self.matchingMethod = 1
            
        if radio.text() == 'Euclidean Distance' :
            if radio.isChecked() == True :
                print("Method switched : Euclidean Distance")
                self.matchingMethod = 2

        """Pemilihan direktori oleh pengguna."""
    def pickDirectory(self) :
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if (directory != '') :
            self.ui.currentDirLabel.setText(directory)
            self.dirLoaded = True

        """Pemilihan database oleh pengguna."""
    def pickDatabase(self) :
        database = str(QFileDialog.getOpenFileName(self, "Select Database", "./", "Pickle file (*.pck)")[0])
        if (database != '') :
            self.ui.currentDbLabel.setText(database)
            self.loadDatabase()
    
        """Penyimpanan database yang sedang digunakan pengguna."""
    def saveDatabase(self) :
        db_dest = str(QFileDialog.getSaveFileName(self, "Save Database", "./extracted", "PIckle file (*.pck)")[0])
        # print(db_dest)
        if (self.db == None) :
            print("Empty database. Please load database or process a folder first.")
        else :
            print("Database is not empty. Proceeding to save database.")
            appLogic.write_db(self.db, db_dest)
    
        """Loading database yang dipilih pengguna."""
    def loadDatabase(self) :
        # loads database to a file on this context
        db_path = self.ui.currentDbLabel.text()
        self.db = appLogic.loadDb(db_path)
        print("Database loaded successfully")

        """Pembuatan database dari suatu database atas perintah Batch Process dari pengguna."""
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
    
        """Mengubah tampilan gambar yang sedang diuji."""
    def changeTestImage(self, filename) :
        image_path = filename
        image_profile = QtGui.QImage(image_path)
        image_profile = image_profile.scaled(350, 350, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        self.ui.testImage.setPixmap(QtGui.QPixmap.fromImage(image_profile))

        """Memilih gambar dengan tombol Load Image."""
    def loadImageClick(self):
        image_path = str(QFileDialog.getOpenFileName(self, "Select Image", "./", "Image file (*.jpg);;Image file (*.png)")[0])
        if os.path.isfile(image_path):
            self.dirLoaded = False
            image_profile = QtGui.QImage(image_path)
            image_profile = image_profile.scaled(350, 350, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
            self.ui.testImage.setPixmap(QtGui.QPixmap.fromImage(image_profile))
            self.ui.currentImageLabel.setText(image_path)

        else:
            self.showAlertBox("No picture selected.")

        """Memilih gambar dan melakukan match sesuai dengan perintah Randomize, kemudian menampilkan hasilnya."""
    def randomClick(self):
        if self.dirLoaded :
            image_path = appLogic.random_sampling(self.ui.currentDirLabel.text())
            self.ui.currentImageLabel.setText(image_path)
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
            if os.path.isfile(currentDir + '/' + str(self.matches_arr[1][0])):
                image_profile = imgProf.scaled(150, 150, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
                self.ui.resImage.setPixmap(QtGui.QPixmap.fromImage(image_profile))
                self.ui.matchRate.setText(stringFormat.format(int(round(self.matches_arr[1][1]*100))))
            else:
                self.showAlertBox("Picture " + str(self.matches_arr[1][0]) + " is not found.")

            imgProf = QtGui.QImage(currentDir + '/' + str(self.matches_arr[2][0]))
            if os.path.isfile(currentDir + '/' + str(self.matches_arr[2][0])):
                image_profile = imgProf.scaled(150, 150, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
                self.ui.resImage_2.setPixmap(QtGui.QPixmap.fromImage(image_profile))
                self.ui.matchRate_2.setText(stringFormat.format(int(round(self.matches_arr[2][1]*100))))
            else:
                self.showAlertBox("Picture " + str(self.matches_arr[2][0]) + " is not found.")

            imgProf = QtGui.QImage(currentDir + '/' + str(self.matches_arr[3][0]))
            if os.path.isfile(currentDir + '/' + str(self.matches_arr[3][0])):
                image_profile = imgProf.scaled(150, 150, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
                self.ui.resImage_3.setPixmap(QtGui.QPixmap.fromImage(image_profile))
                self.ui.matchRate_3.setText(stringFormat.format(int(round(self.matches_arr[3][1]*100))))
            else:
                self.showAlertBox("Picture " + str(self.matches_arr[3][0]) + " is not found.")

            imgProf = QtGui.QImage(currentDir + '/' + str(self.matches_arr[4][0]))
            if os.path.isfile(currentDir + '/' + str(self.matches_arr[4][0])):
                image_profile = imgProf.scaled(150, 150, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
                self.ui.resImage_4.setPixmap(QtGui.QPixmap.fromImage(image_profile))
                self.ui.matchRate_4.setText(stringFormat.format(int(round(self.matches_arr[4][1]*100))))
            else:
                self.showAlertBox("Picture " + str(self.matches_arr[4][0]) + " is not found.")

            imgProf = QtGui.QImage(currentDir + '/' + str(self.matches_arr[5][0]))
            if os.path.isfile(currentDir + '/' + str(self.matches_arr[5][0])):
                image_profile = imgProf.scaled(150, 150, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
                self.ui.resImage_5.setPixmap(QtGui.QPixmap.fromImage(image_profile))
                self.ui.matchRate_5.setText(stringFormat.format(int(round(self.matches_arr[5][1]*100))))
            else:
                self.showAlertBox("Picture " + str(self.matches_arr[5][0]) + " is not found.")
            
        else :
            self.showAlertBox("No directory loaded")

        """Melakukan matching dengan tombol Match."""
    def matchClick(self):
        image_path = self.ui.currentImageLabel.text()
        if os.path.isfile(image_path):
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

            imgProf = QtGui.QImage(currentDir + '/' + str(self.matches_arr[0][0]))
            if os.path.isfile(currentDir + '/' + str(self.matches_arr[0][0])):
                image_profile = imgProf.scaled(150, 150, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
                self.ui.resImage.setPixmap(QtGui.QPixmap.fromImage(image_profile))
                self.ui.matchRate.setText(stringFormat.format(int(round(self.matches_arr[0][1]*100))))
            else:
                self.showAlertBox("Image " + str(self.matches_arr[0][0]) + " is not found.")

            imgProf = QtGui.QImage(currentDir + '/' + str(self.matches_arr[1][0]))
            if os.path.isfile(currentDir + '/' + str(self.matches_arr[1][0])):
                image_profile = imgProf.scaled(150, 150, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
                self.ui.resImage_2.setPixmap(QtGui.QPixmap.fromImage(image_profile))
                self.ui.matchRate_2.setText(stringFormat.format(int(round(self.matches_arr[1][1]*100))))
            else:
                self.showAlertBox("Image " + str(self.matches_arr[1][0]) + " is not found.")

            imgProf = QtGui.QImage(currentDir + '/' + str(self.matches_arr[2][0]))
            if os.path.isfile(currentDir + '/' + str(self.matches_arr[2][0])):
                image_profile = imgProf.scaled(150, 150, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
                self.ui.resImage_3.setPixmap(QtGui.QPixmap.fromImage(image_profile))
                self.ui.matchRate_3.setText(stringFormat.format(int(round(self.matches_arr[2][1]*100))))
            else:
                self.showAlertBox("Image " + str(self.matches_arr[2][0]) + " is not found.")

            imgProf = QtGui.QImage(currentDir + '/' + str(self.matches_arr[3][0]))
            if os.path.isfile(currentDir + '/' + str(self.matches_arr[3][0])):
                image_profile = imgProf.scaled(150, 150, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
                self.ui.resImage_4.setPixmap(QtGui.QPixmap.fromImage(image_profile))
                self.ui.matchRate_4.setText(stringFormat.format(int(round(self.matches_arr[3][1]*100))))
            else:
                self.showAlertBox("Image " + str(self.matches_arr[3][0]) + " is not found.")

            imgProf = QtGui.QImage(currentDir + '/' + str(self.matches_arr[4][0]))
            if os.path.isfile(currentDir + '/' + str(self.matches_arr[4][0])):
                image_profile = imgProf.scaled(150, 150, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
                self.ui.resImage_5.setPixmap(QtGui.QPixmap.fromImage(image_profile))
                self.ui.matchRate_5.setText(stringFormat.format(int(round(self.matches_arr[4][1]*100))))
            else:
                self.showAlertBox("Image " + str(self.matches_arr[4][0]) + " is not found.")
            
        else :
            self.showAlertBox("No image loaded")

        """Menunjukkan pesan peringatan."""
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