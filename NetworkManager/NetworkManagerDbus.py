#!/usr/bin/env python
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright (C) 2010 - 2012 Red Hat, Inc.
#

from base import Event
from base import Observable

import dbus
import dbus.mainloop.glib
from gi.repository import GLib

nm_state = { 0: "Unknown",
            10: "Asleep",
            20: "Disconnected",
            30: "Disconnecting",
            40: "Connecting",
            50: "Connected-Local",
            60: "Connected-Site",
            70: "Connected-Global" }

class DbusNetworkChecker(Observable.Observable):
    ''' this class does lazy checks for network availability and 
    disconnects emesene if the network goes down '''
    def __init__(self):
        super(DbusNetworkChecker, self).__init__()
        self.alert_watcher = None

    def _on_network_changed(self, *args, **kwargs):
#        print 'eventoooo'
        s = args[0]
        ss = nm_state[s]
 #       print "\tNM State:", ss
        avariable = True
        if not s == 70:
            self.fire('NetworkDisconnect')
        else:
            self.fire('NetworkConnect')

    def iniciar(self):
        print("Waiting for signals")
        print("-------------------")
  
        gloop = dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        gloop = GLib.MainLoop()
        self.alert_watcher = dbus.SystemBus()
        self.alert_watcher.add_signal_receiver(self._on_network_changed, "StateChanged",  "org.freedesktop.NetworkManager")
        gloop.run()