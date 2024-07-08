from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ignorar erros de certificado SSL
        #QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.SslCertificateErrorsAllowed, True)

        # Cria as 4 views
        self.view1 = QWebEngineView()
        self.view2 = QWebEngineView()
        self.view3 = QWebEngineView()
        self.view4 = QWebEngineView()

        # Define as URLs iniciais das 4 views
        self.view1.load(QUrl("https://br.tradingview.com/chart/?symbol=FX_IDC%3AUSDBRL"))
        self.view2.load(QUrl("https://br.tradingview.com/chart/?symbol=BITSTAMP%3ABTCUSD"))
        self.view3.load(QUrl("https://blockchair.com/bitcoin/block/851297"))
        self.view4.load(QUrl("https://coinmarketcap.com/pt-br/crypto-heatmap/"))

        # Cria um splitter para dividir a janela em 4 áreas
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(self.view1)
        splitter1.addWidget(self.view2)
        splitter1.setHandleWidth(10)  # Define a largura da linha do divisor
        splitter1.setMinimumSize(200, 200)  # Define o tamanho mínimo do divisor
        splitter1.setMaximumSize(1000, 1000)  # Define o tamanho máximo do divisor

        splitter2 = QSplitter(Qt.Horizontal)
        splitter2.addWidget(self.view3)
        splitter2.addWidget(self.view4)
        splitter2.setHandleWidth(10)
        splitter2.setMinimumSize(200, 200)
        splitter2.setMaximumSize(1000, 1000)

        splitter3 = QSplitter(Qt.Vertical)
        splitter3.addWidget(splitter1)
        splitter3.addWidget(splitter2)
        splitter3.setHandleWidth(10)
        splitter3.setMinimumSize(400, 400)
        splitter3.setMaximumSize(2000, 2000)

        # Cria um widget central para a janela principal e define o splitter como layout
        widget = QWidget()
        widget.setLayout(QVBoxLayout())
        widget.layout().addWidget(splitter3)
        self.setCentralWidget(widget)

        # Cria uma toolbar para os botões de zoom
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        # Adiciona os botões de zoom na toolbar para cada visualização
        self.add_zoom_buttons(toolbar, self.view1)
        self.add_zoom_buttons(toolbar, self.view2)
        self.add_zoom_buttons(toolbar, self.view3)
        self.add_zoom_buttons(toolbar, self.view4)

    def add_zoom_buttons(self, toolbar, view):
        # Adiciona os botões de zoom na toolbar para a visualização especificada
        zoom_in_button = QAction("+", self)
        zoom_in_button.triggered.connect(lambda: view.setZoomFactor(view.zoomFactor() + 0.1))
        toolbar.addAction(zoom_in_button)

        zoom_out_button = QAction("-", self)
        zoom_out_button.triggered.connect(lambda: view.setZoomFactor(view.zoomFactor() - 0.1))
        toolbar.addAction(zoom_out_button)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
