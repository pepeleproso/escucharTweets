# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Bot import *
from ConfigManager import *
from configJsonSaver import *

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
        self.config = ConfigManager()

        self.qDialogConfiguracion = QDialog()
        self.qDialogConfiguracion.setFixedSize(600,500)

        self.flo = QFormLayout()
        self.qLineConsumerKey = QLineEdit()
        self.qLineConsumerKey.setAlignment(Qt.AlignLeft)
        self.qLineConsumerKey.setText(self.config.consumer_key)
        #qLineConsumerKey.setFont(QFont("Arial",20))
        #self.qLineConsumerKey.setReadOnly(True)

        self.flo.addRow("Consumer Key", self.qLineConsumerKey)

        self.qLineConsumer_secret = QLineEdit()
        self.qLineConsumer_secret.setAlignment(Qt.AlignLeft)
        self.qLineConsumer_secret.setText(self.config.consumer_secret)
        self.qLineConsumer_secret.setReadOnly(True)
        self.flo.addRow("Consumer Secret",self.qLineConsumer_secret)
	
        self.qLineAccess_token = QLineEdit()
        self.qLineAccess_token.setAlignment(Qt.AlignLeft)
        self.qLineAccess_token.setText(self.config.access_token)
        self.qLineAccess_token.setReadOnly(True)
        self.flo.addRow("Access Token",self.qLineAccess_token)
	
        self.qLineAccess_secret = QLineEdit()
        self.qLineAccess_secret.setAlignment(Qt.AlignLeft)
        self.qLineAccess_secret.setText(self.config.access_secret)
        self.qLineAccess_secret.setReadOnly(True)
        self.flo.addRow("Access Secret",self.qLineAccess_secret)
	
        self.qLineOutputFilePrefix = QLineEdit()
        self.qLineOutputFilePrefix.setAlignment(Qt.AlignLeft)
        self.qLineOutputFilePrefix.setText(self.config.outputfileprefix)
        #qLineOutputFilePrefix.setEchoMode(QLineEdit.Password)
        self.flo.addRow("Prefijo de archivo",self.qLineOutputFilePrefix)
	
        self.qLineHashtags = QTextEdit()
        self.qLineHashtags.setAlignment(Qt.AlignTop)
        #qLineHashtags.setAlignment(Qt.)
        self.qLineHashtags.setText(",".join(self.config.keyword_list))
        self.qLineHashtags.setFixedSize(400,200)
        self.flo.addRow("Hashtags",self.qLineHashtags)
	
        #e5.editingFinished.connect(enterPress)
        self.qDialogConfiguracion.setLayout(self.flo)

        self.btnAceptarConfiguracion = QPushButton("Aceptar",self.qDialogConfiguracion)
        self.btnAceptarConfiguracion.setFixedSize(100,30)
        self.btnAceptarConfiguracion.clicked.connect(self.btnAceptarConfiguracion_clicked)

        
        self.btnCancelarConfiguracion = QPushButton("Cancelar",self.qDialogConfiguracion)
        self.btnCancelarConfiguracion.setFixedSize(100,30)
        self.flo.addRow(self.btnAceptarConfiguracion,self.btnCancelarConfiguracion)

        self.qDialogConfiguracion.setWindowTitle("Configuraciones")
        self.qDialogConfiguracion.setWindowModality(Qt.ApplicationModal)
        self.qDialogConfiguracion.exec_()
    
    def btnAceptarConfiguracion_clicked(self):
        print("boton aceptar configuracion")
        print("la cadena es " + self.qLineConsumerKey.text())
        print("la cadena DE HASH es ")
        print(str(self.qLineHashtags.toPlainText()).split(","))
        if not(self.qLineConsumerKey.text()):
            errorMessage = QMessageBox()
            errorMessage.setIcon(QMessageBox.Critical)
            errorMessage.setText("Debe ingresar un consumer key")
            errorMessage.setWindowTitle("Error")
            errorMessage.setStandardButtons(QMessageBox.Ok)
            errorMessage.exec_()
        
        if not(self.qLineConsumer_secret.text()):
            errorMessage = QMessageBox()
            errorMessage.setIcon(QMessageBox.Critical)
            errorMessage.setText("Debe ingresar un consumer secret")
            errorMessage.setWindowTitle("Error")
            errorMessage.setStandardButtons(QMessageBox.Ok)
            errorMessage.exec_()

        if not(self.qLineAccess_token.text()):
            errorMessage = QMessageBox()
            errorMessage.setIcon(QMessageBox.Critical)
            errorMessage.setText("Debe ingresar un access token")
            errorMessage.setWindowTitle("Error")
            errorMessage.setStandardButtons(QMessageBox.Ok)
            #errorMessage.buttonClicked.connect(self.errorAceptar)
            errorMessage.exec_()

        if not(self.qLineAccess_secret.text()):
            errorMessage = QMessageBox()
            errorMessage.setIcon(QMessageBox.Critical)
            errorMessage.setText("Debe ingresar un access secret")
            errorMessage.setWindowTitle("Error")
            errorMessage.setStandardButtons(QMessageBox.Ok)
            #errorMessage.buttonClicked.connect(self.errorAceptar)
            errorMessage.exec_()
        
        if not(self.qLineOutputFilePrefix.text()):
            errorMessage = QMessageBox()
            errorMessage.setIcon(QMessageBox.Critical)
            errorMessage.setText("Debe ingresar el prefijo con el que desea guardar los archivos")
            errorMessage.setWindowTitle("Error")
            errorMessage.setStandardButtons(QMessageBox.Ok)
            #errorMessage.buttonClicked.connect(self.errorAceptar)
            errorMessage.exec_()

        if not(self.qLineHashtags.toPlainText()):
            errorMessage = QMessageBox()
            errorMessage.setIcon(QMessageBox.Critical)
            errorMessage.setText("Debe ingresar al menos un hashtag para comenzar la captura.")
            errorMessage.setWindowTitle("Error")
            errorMessage.setStandardButtons(QMessageBox.Ok)
            #errorMessage.buttonClicked.connect(self.errorAceptar)
            errorMessage.exec_()
        listaHashtag = str(self.qLineHashtags.toPlainText()).split(",")
        saver = configJsonSaver(self.qLineConsumerKey.text,self.qLineConsumer_secret.text,self.qLineAccess_token.text,self.qLineAccess_secret,listaHashtag,self.qLineOutputFilePrefix.text,10)
        print json.dumps(saver, cls=ObjectEncoder, indent=2, sort_keys=True)


        
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