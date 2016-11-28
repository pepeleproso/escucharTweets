# -*- coding: utf-8 -*-

#    This file is part of escucharTweets.
#
#    escucharTweets is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    emesene is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with escucharTweets; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import gi
from gi.repository import Gio
from gi.repository import GObject


from base import Event
from base import Observable

class GioNetworkChecker(Observable):
    ''' this class does lazy checks for network availability and 
    disconnects if the network goes down '''
    def __init__(self):
        super(GioNetworkChecker, self).__init__()
        self.alert_watcher = Gio.NetworkMonitor.get_default()
        self.alert_watcher.connect("network-changed", self._on_network_changed)
#        print 'acaaa'
#        print self.alert_watcher.get_network_available()

    #Callback functions
    def _on_network_changed(self, monitor, avariable):
#        print 'eventoooo'
#        print avariable
#        print self.alert_watcher.get_network_available()
#        print 'fin evento'
        if not self.alert_watcher.get_network_available():
            self.fire('NetworkDisconnect')
        else:
            self.fire('NetworkConnect')
    
    def iniciar(self):
        print("Iniciando Monitor de Conexion")
        print("-------------------")
  
        loop = GObject.MainLoop()
        loop.run()
