# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Bot import *

class EscucharTweetsMainWindows(object):
    def __init__(self):
        app = QApplication(sys.argv)
        w = QWidget()
        w.setWindowTitle("Escuchar Tweets")     
        w.setGeometry(500,200,300,50)
          

        self.bot = None
        vbox = QVBoxLayout()

        btnConfigurar = QPushButton()
        btnConfigurar.setText("Configuracion")
        #btnConfigurar.move(50,20)
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
        w.setLayout(vbox)
        w.show()
        sys.exit(app.exec_())


    def btnConfigurar_clicked(self):
        print "btnConfigurar clicked"
        d = QDialog()
        b1 = QPushButton("Aceptar",d)
        b1.move(50,50)
        d.setWindowTitle("Configuraciones")
        d.setWindowModality(Qt.ApplicationModal)
        d.exec_()
	
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