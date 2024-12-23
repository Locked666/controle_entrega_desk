import sys
import subprocess
import time
from PySide6.QtCore import QTimer, QTime, Signal, QObject
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel


class TeamViewerMonitor(QObject):
    session_started = Signal()
    session_ended = Signal(str)

    def __init__(self, teamviewer_path, teamviewer_id, teamviewer_password):
        super().__init__()
        self.teamviewer_path = teamviewer_path
        self.teamviewer_id = teamviewer_id
        self.teamviewer_password = teamviewer_password
        self.process = None
        self.start_time = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_session_status)

    def start_teamviewer(self):
        # Inicia o TeamViewer
        command = [
            self.teamviewer_path,
            "--id", self.teamviewer_id,
            "-p", self.teamviewer_password,
        ]
        self.process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.start_time = time.time()
        self.session_started.emit()  # Emite sinal de início de sessão
        self.timer.start(1000)  # Checa o status a cada segundo

    def check_session_status(self):
        # Verifica se o processo ainda está em execução
        if self.process.poll() is not None:
            self.timer.stop()
            end_time = time.time()
            elapsed_time = end_time - self.start_time
            self.session_ended.emit(self.format_elapsed_time(elapsed_time))

    def format_elapsed_time(self, elapsed_seconds):
        hours, remainder = divmod(elapsed_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.monitor = TeamViewerMonitor(r"C:\Program Files (x86)\TeamViewer\TeamViewer.exe", "1351368620", "3vy3cskr")
        self.monitor.session_started.connect(self.on_session_started)
        self.monitor.session_ended.connect(self.on_session_ended)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.status_label = QLabel("Status: Aguardando...")
        self.timer_label = QLabel("Tempo de Conexão: 0h 0m 0s")
        self.start_button = QPushButton("Iniciar TeamViewer")
        self.start_button.clicked.connect(self.start_teamviewer_session)

        layout.addWidget(self.status_label)
        layout.addWidget(self.timer_label)
        layout.addWidget(self.start_button)
        self.setLayout(layout)
        self.setWindowTitle("Monitor de Conexão TeamViewer")

    def start_teamviewer_session(self):
        self.status_label.setText("Status: Conectando...")
        self.timer_label.setText("Tempo de Conexão: 0h 0m 0s")
        self.monitor.start_teamviewer()

    def on_session_started(self):
        self.status_label.setText("Status: Conectado")

    def on_session_ended(self, elapsed_time):
        self.status_label.setText("Status: Desconectado")
        self.timer_label.setText(f"Tempo Total de Conexão: {elapsed_time}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
