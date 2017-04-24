# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Bot import *
from ConfigManager import *

class EscucharTweetsMainWindows(object):
    def __init__(self):
        app = QApplication(sys.argv)
        qDialogVentanaPrincipal = QDialog()
         #qDialogConfiguracion.setWindowModality(Qt.ApplicationModal)
        
        qDialogVentanaPrincipal.setWindowTitle("Escuchar Tweets")     
        qDialogVentanaPrincipal.setGeometry(500,200,300,50)
          

        self.bot = None
        vbox = QVBoxLayout()
        #print(dir(vbox))
        vbox.setSpacing(20)
        vbox.setMargin(40)
        btnConfigurar = QPushButton(qDialogVentanaPrincipal)
        btnConfigurar.setText("Configuracion")
        btnConfigurar.move(20,20)
        btnConfigurar.clicked.connect(self.btnConfigurar_clicked)

        btnIniciarPausar = QPushButton()
        btnIniciarPausar.setText("Iniciar escucha")
        btnIniciarPausar.clicked.connect(self.btnIniciarPausar_clicked)
 
        btnParar = QPushButton()
        btnParar.setText("Detener")
        btnParar.clicked.connect(self.btnParar_clicked)

        vbox.addWidget(btnConfigurar)
        vbox.addWidget(btnIniciarPausar)
        vbox.addWidget(btnParar)
        qDialogVentanaPrincipal.setLayout(vbox)
        qDialogVentanaPrincipal.show()
        sys.exit(app.exec_())


    def btnConfigurar_clicked(self):
        config = ConfigManager()

        qDialogConfiguracion = QDialog()
        qDialogConfiguracion.setFixedSize(600,500)

        flo = QFormLayout()
        qLineConsumerKey = QLineEdit()
        qLineConsumerKey.setAlignment(Qt.AlignLeft)
        qLineConsumerKey.setText(config.consumer_key)
        #qLineConsumerKey.setFont(QFont("Arial",20))
        flo.addRow("Consumer Key", qLineConsumerKey)

        qLineConsumer_secret = QLineEdit()
        qLineConsumer_secret.setAlignment(Qt.AlignLeft)
        qLineConsumer_secret.setText(config.consumer_secret)
        flo.addRow("Consumer Secret",qLineConsumer_secret)
	
        qLineAccess_token = QLineEdit()
        qLineAccess_token.setAlignment(Qt.AlignLeft)
        qLineAccess_token.setText(config.access_token)
        flo.addRow("Access Token",qLineAccess_token)
	
        qLineAccess_secret = QLineEdit()
        qLineAccess_secret.setAlignment(Qt.AlignLeft)
        qLineAccess_secret.setText(config.access_secret)
        flo.addRow("Access Secret",qLineAccess_secret)
	
        qLineOutputFilePrefix = QLineEdit()
        qLineOutputFilePrefix.setAlignment(Qt.AlignLeft)
        qLineOutputFilePrefix.setText(config.outputfileprefix)
        #qLineOutputFilePrefix.setEchoMode(QLineEdit.Password)
        flo.addRow("Prefijo de archivo",qLineOutputFilePrefix)
	
        qLineHashtags = QTextEdit()
        qLineHashtags.setAlignment(Qt.AlignTop)
        #qLineHashtags.setAlignment(Qt.)
        qLineHashtags.setText("Ingrese los hashtags separados por punto y coma (;)")
        qLineHashtags.setFixedSize(400,200)
        #qLineHashtags.setReadOnly(True)
        flo.addRow("Hashtags",qLineHashtags)
	
        #e5.editingFinished.connect(enterPress)
        qDialogConfiguracion.setLayout(flo)

        btnAceptarConfiguracion = QPushButton("Aceptar",qDialogConfiguracion)
        btnAceptarConfiguracion.setFixedSize(100,30)
        btnParar.clicked.connect(self.btnAceptarConfiguracion_clicked)
        
        btnCancelarConfiguracion = QPushButton("Cancelar",qDialogConfiguracion)
        btnCancelarConfiguracion.setFixedSize(100,30)
        flo.addRow(btnAceptarConfiguracion,btnCancelarConfiguracion)

        qDialogConfiguracion.setWindowTitle("Configuraciones")
        qDialogConfiguracion.setWindowModality(Qt.ApplicationModal)
        qDialogConfiguracion.exec_()
	
    def btnIniciarPausar_clicked(self):
        print "btnIniciarPausar_clicked clicked"
        if(self.bot is None):
            self.bot = Bot()
            self.bot.init()
        else:
            self.bot.InitListening(True)

    def btnParar_clicked(self):
        self.bot.StopListening(True)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action="count",help="increase output verbosity (e.g., -vv is more than -v)")
    args = parser.parse_args()

    debuglevel = logging.WARNING

    if args.verbose == 1:
       debuglevel = logging.WARNING
    elif args.verbose == 2:
      debuglevel = logging.INFO
    elif args.verbose == 3:
     debuglevel = logging.DEBUG

    logging.basicConfig(level=debuglevel)

    EscucharTweetsMainWindows()