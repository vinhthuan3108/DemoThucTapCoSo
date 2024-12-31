import sys,csv
import requests
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 40, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(90, 100, 601, 131))
        self.groupBox.setObjectName("groupBox")
        self.label_mt = QtWidgets.QLabel(parent=self.groupBox)
        self.label_mt.setGeometry(QtCore.QRect(50, 80, 111, 20))
        self.label_mt.setObjectName("label_mt")
        self.inputTenThanhPho = QtWidgets.QLineEdit(parent=self.groupBox)
        self.inputTenThanhPho.setGeometry(QtCore.QRect(170, 80, 113, 22))
        self.inputTenThanhPho.setObjectName("inputTenThanhPho")
        self.buttonNhapThanhPho = QtWidgets.QPushButton(parent=self.groupBox)
        self.buttonNhapThanhPho.setGeometry(QtCore.QRect(370, 80, 121, 28))
        self.buttonNhapThanhPho.setObjectName("buttonNhapThanhPho")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(120, 280, 591, 191))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.label_4.setObjectName("label_4")
        self.cbThanhPho = QtWidgets.QComboBox(parent=self.groupBox_2)
        self.cbThanhPho.setGeometry(QtCore.QRect(110, 30, 91, 22))
        self.cbThanhPho.setObjectName("cbThanhPho")
        self.label_doam = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_doam.setGeometry(QtCore.QRect(310, 100, 55, 16))
        self.label_doam.setObjectName("label_doam")
        self.lineEdit_doam = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_doam.setGeometry(QtCore.QRect(370, 100, 113, 22))
        self.lineEdit_doam.setObjectName("lineEdit_doam")
        self.lineEdit_doam.setReadOnly(True)
        self.label_nhietdo = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_nhietdo.setGeometry(QtCore.QRect(310, 20, 55, 16))
        self.label_nhietdo.setObjectName("label_nhietdo")
        self.lineEdit_nhietdo = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_nhietdo.setGeometry(QtCore.QRect(370, 20, 113, 22))
        self.lineEdit_nhietdo.setObjectName("lineEdit_nhietdo")
        self.lineEdit_nhietdo.setReadOnly(True)
        self.label_tocdogio = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_tocdogio.setGeometry(QtCore.QRect(300, 60, 71, 20))
        self.label_tocdogio.setObjectName("label_tocdogio")
        self.lineEdit_tocdogio = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEdit_tocdogio.setGeometry(QtCore.QRect(370, 60, 113, 22))
        self.lineEdit_tocdogio.setObjectName("lineEdit_tocdogio")
        self.lineEdit_tocdogio.setReadOnly(True)
        self.submitButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.submitButton.setGeometry(QtCore.QRect(240, 150, 93, 28))
        self.submitButton.setObjectName("submitButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Gắn sự kiện
        self.buttonNhapThanhPho.clicked.connect(self.add_city_to_combobox)
        self.submitButton.clicked.connect(self.display_weather_info)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ỨNG DỤNG QUẢN LÝ THỜI TIẾT(Nhập Tay)"))
        self.groupBox.setTitle(_translate("MainWindow", "Nhập thành phố"))
        self.label_mt.setText(_translate("MainWindow", "Tên Thành Phố"))
        self.buttonNhapThanhPho.setText(_translate("MainWindow", "Nhập thành phố"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Thông tin thành phố"))
        self.label_4.setText(_translate("MainWindow", "Thành Phố"))
        self.label_doam.setText(_translate("MainWindow", "Độ ẩm"))
        self.label_nhietdo.setText(_translate("MainWindow", "Nhiệt độ"))
        self.label_tocdogio.setText(_translate("MainWindow", "Tốc độ gió"))
        self.submitButton.setText(_translate("MainWindow", "Hiện kết quả"))

    def kelvin_to_celsius(self, kelvin):
        return kelvin - 273.15

    def add_city_to_combobox(self):
        city = self.inputTenThanhPho.text().strip()
        if city and city not in [self.cbThanhPho.itemText(i) for i in range(self.cbThanhPho.count())]:
            self.cbThanhPho.addItem(city)
            self.inputTenThanhPho.clear()

    def display_weather_info(self):
        API_KEY = "MyAPIKet"  # Thay bằng API key mới chạy được
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
        city = self.cbThanhPho.currentText()
        if not city:
            return
        
        url = BASE_URL + "appid=" + API_KEY + "&q=" + city
        try:
            response = requests.get(url).json()
            if response.get("main"):
                temp_kelvin = response["main"]["temp"]
                temp_celsius = self.kelvin_to_celsius(temp_kelvin)
                humidity = response["main"]["humidity"]
                wind_speed = response["wind"]["speed"]

                self.lineEdit_nhietdo.setText(f"{temp_celsius:.2f} °C")
                self.lineEdit_doam.setText(f"{humidity}%")
                self.lineEdit_tocdogio.setText(f"{wind_speed} m/s")
            else:
                self.lineEdit_nhietdo.setText("Không tìm thấy!")
                self.lineEdit_doam.setText("Không tìm thấy!")
                self.lineEdit_tocdogio.setText("Không tìm thấy!")
        except Exception as e:
            self.lineEdit_nhietdo.setText("Lỗi kết nối!")
            self.lineEdit_doam.setText("Lỗi kết nối!")
            self.lineEdit_tocdogio.setText("Lỗi kết nối!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
