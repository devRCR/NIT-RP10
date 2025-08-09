import sys
import asi
import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore
import serial
import serial.tools.list_ports
import os
from PIL import Image

class CameraStreamWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cam_id = 0
        self.width = 2048
        self.height = 1536
        self.img_type = asi.ASI_IMG_RAW16
        self.binning = 2
        self.frame_size = self.width * self.height * 2
        self.gain = 100
        self.exposure_ms = 30
        self.ser = None
        self.baudrate = 115200
        self.serial_port = None
        self.init_camera()
        self.init_ui()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def init_camera(self):
        num_cams = asi.ASIGetNumOfConnectedCameras()
        if num_cams == 0:
            QtWidgets.QMessageBox.critical(self, "Error", "No se detectó ninguna cámara ZWO.")
            sys.exit(1)
        rtn, cam_info = asi.ASIGetCameraProperty(self.cam_id)
        if rtn != asi.ASI_SUCCESS:
            QtWidgets.QMessageBox.critical(self, "Error", "No se pudo obtener la propiedad de la cámara.")
            sys.exit(1)
        asi.ASIOpenCamera(self.cam_id)
        asi.ASIInitCamera(self.cam_id)
        asi.ASISetROIFormat(self.cam_id, self.width, self.height, self.binning, self.img_type)
        asi.ASISetControlValue(self.cam_id, asi.ASI_GAIN, self.gain, asi.ASI_FALSE)
        asi.ASISetControlValue(self.cam_id, asi.ASI_EXPOSURE, self.exposure_ms * 1000, asi.ASI_FALSE)

    def init_ui(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        # --- UART Controls ---
        uart_layout = QtWidgets.QHBoxLayout()
        self.ports_list = QtWidgets.QComboBox()
        uart_layout.addWidget(QtWidgets.QLabel("Puertos UART:"))
        uart_layout.addWidget(self.ports_list)
        self.refresh_btn = QtWidgets.QPushButton("Actualizar Puertos")
        self.refresh_btn.clicked.connect(self.refresh_ports)
        uart_layout.addWidget(self.refresh_btn)
        self.connect_btn = QtWidgets.QPushButton("Conectar")
        self.connect_btn.setCheckable(True)
        self.connect_btn.clicked.connect(self.toggle_connection)
        uart_layout.addWidget(self.connect_btn)
        main_layout.addLayout(uart_layout)
        self.refresh_ports()

        # --- Video Streaming ---
        self.image_label = QtWidgets.QLabel()
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        main_layout.addWidget(self.image_label, stretch=1)

        # --- Camera Controls ---
        controls = QtWidgets.QHBoxLayout()
        # Exposición
        controls.addWidget(QtWidgets.QLabel("Exposición (ms):"))
        self.exposure_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.exposure_slider.setMinimum(1)
        self.exposure_slider.setMaximum(1000)
        self.exposure_slider.setValue(self.exposure_ms)
        self.exposure_slider.valueChanged.connect(self.on_exposure_change)
        controls.addWidget(self.exposure_slider)
        self.exposure_text = QtWidgets.QLineEdit(str(self.exposure_ms))
        self.exposure_text.setFixedWidth(50)
        self.exposure_text.editingFinished.connect(self.on_exposure_text)
        controls.addWidget(self.exposure_text)
        # Ganancia
        controls.addWidget(QtWidgets.QLabel("Ganancia:"))
        self.gain_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.gain_slider.setMinimum(0)
        self.gain_slider.setMaximum(600)
        self.gain_slider.setValue(self.gain)
        self.gain_slider.valueChanged.connect(self.on_gain_change)
        controls.addWidget(self.gain_slider)
        self.gain_text = QtWidgets.QLineEdit(str(self.gain))
        self.gain_text.setFixedWidth(50)
        self.gain_text.editingFinished.connect(self.on_gain_text)
        controls.addWidget(self.gain_text)
        # Formato de imagen
        controls.addWidget(QtWidgets.QLabel("Formato:"))
        self.format_list = QtWidgets.QComboBox()
        self.format_list.addItems(["RAW8", "RAW16"])
        self.format_list.setCurrentIndex(1)
        self.format_list.currentIndexChanged.connect(self.on_format_change)
        controls.addWidget(self.format_list)
        # Binning
        controls.addWidget(QtWidgets.QLabel("Binning:"))
        self.binning_list = QtWidgets.QComboBox()
        self.binning_list.addItems(["BIN1", "BIN2", "BIN3", "BIN4"])
        self.binning_list.setCurrentIndex(1)
        self.binning_list.currentIndexChanged.connect(self.on_binning_change)
        controls.addWidget(self.binning_list)
        # Botón INICIAR
        self.start_btn = QtWidgets.QPushButton("INICIAR")
        self.start_btn.clicked.connect(self.capture_sequence)
        controls.addWidget(self.start_btn)
        main_layout.addLayout(controls)

    def refresh_ports(self):
        self.ports_list.clear()
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if 'ttyACM' in port.device:
                self.ports_list.addItem(port.device)
        if ports:
            self.serial_port = ports[0].device
        else:
            self.serial_port = None

    def toggle_connection(self):
        if self.connect_btn.isChecked():
            port = self.ports_list.currentText()
            try:
                self.ser = serial.Serial(port, self.baudrate, timeout=2)
                self.connect_btn.setText("Desconectar")
                self.serial_port = port
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Error Serial", str(e))
                self.connect_btn.setChecked(False)
        else:
            if self.ser:
                self.ser.close()
                self.ser = None
            self.connect_btn.setText("Conectar")

    def on_exposure_change(self, value):
        self.exposure_ms = value
        self.exposure_text.setText(str(value))
        asi.ASISetControlValue(self.cam_id, asi.ASI_EXPOSURE, self.exposure_ms * 1000, asi.ASI_FALSE)

    def on_exposure_text(self):
        try:
            value = int(self.exposure_text.text())
            self.exposure_slider.setValue(value)
        except ValueError:
            pass

    def on_gain_change(self, value):
        self.gain = value
        self.gain_text.setText(str(value))
        asi.ASISetControlValue(self.cam_id, asi.ASI_GAIN, self.gain, asi.ASI_FALSE)

    def on_gain_text(self):
        try:
            value = int(self.gain_text.text())
            self.gain_slider.setValue(value)
        except ValueError:
            pass

    def on_format_change(self, idx):
        if idx == 0:
            self.img_type = asi.ASI_IMG_RAW8
            self.frame_size = self.width * self.height
        else:
            self.img_type = asi.ASI_IMG_RAW16
            self.frame_size = self.width * self.height * 2
        asi.ASISetROIFormat(self.cam_id, self.width, self.height, self.binning, self.img_type)

    def on_binning_change(self, idx):
        self.binning = idx + 1
        asi.ASISetROIFormat(self.cam_id, self.width, self.height, self.binning, self.img_type)

    def update_frame(self):
        asi.ASIStartExposure(self.cam_id, asi.ASI_FALSE)
        while True:
            rtn, status = asi.ASIGetExpStatus(self.cam_id)
            if status == asi.ASI_EXP_SUCCESS:
                break
            elif status == asi.ASI_EXP_FAILED:
                return
        rtn, frame = asi.ASIGetDataAfterExp(self.cam_id, self.frame_size)
        if rtn == asi.ASI_SUCCESS:
            image = np.frombuffer(frame, dtype=np.uint16 if self.img_type == asi.ASI_IMG_RAW16 else np.uint8).reshape((self.height, self.width))
            if self.img_type == asi.ASI_IMG_RAW16:
                img8 = (image / 256).astype(np.uint8)
            else:
                img8 = image
            qimg = QtGui.QImage(img8.data, self.width, self.height, self.width, QtGui.QImage.Format_Grayscale8)
            pixmap = QtGui.QPixmap.fromImage(qimg)
            self.image_label.setPixmap(pixmap.scaled(self.image_label.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def capture_sequence(self):
        NUM_PHOTOS = 200
        if self.ser is None:
            QtWidgets.QMessageBox.warning(self, "UART", "No hay conexión UART activa.")
            return
        # Crear carpeta TOMOXX
        tomo_number = 1
        while True:
            folder_name = f"TOMO{tomo_number:02d}"
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
                break
            tomo_number += 1
        for i in range(NUM_PHOTOS):
            self.ser.reset_input_buffer()
            self.ser.write(b's\r\n')
            # Esperar OK
            ok = False
            buffer = b''
            for _ in range(100):
                if self.ser.in_waiting:
                    buffer += self.ser.read(self.ser.in_waiting)
                    if b'OK' in buffer:
                        ok = True
                        break
                QtCore.QThread.msleep(10)
            # Captura de imagen
            asi.ASIStartExposure(self.cam_id, asi.ASI_FALSE)
            while True:
                rtn, status = asi.ASIGetExpStatus(self.cam_id)
                if status == asi.ASI_EXP_SUCCESS:
                    break
                elif status == asi.ASI_EXP_FAILED:
                    break
                QtCore.QThread.msleep(1)
            rtn, frame = asi.ASIGetDataAfterExp(self.cam_id, self.frame_size)
            if rtn == asi.ASI_SUCCESS:
                image = np.frombuffer(frame, dtype=np.uint16 if self.img_type == asi.ASI_IMG_RAW16 else np.uint8).reshape((self.height, self.width))
                filename = os.path.join(folder_name, f"foto_{i+1:03d}.tiff")
                im = Image.fromarray(image)
                im.save(filename)
        QtWidgets.QMessageBox.information(self, "Secuencia", f"Secuencia de {NUM_PHOTOS} fotos finalizada en {folder_name}.")

    def closeEvent(self, event):
        asi.ASICloseCamera(self.cam_id)
        if self.ser:
            self.ser.close()
        event.accept()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RP10 Neutron Imaging Tomography Facility")
        self.resize(1000, 800)
        self.viewer = CameraStreamWidget(self)
        self.setCentralWidget(self.viewer)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
