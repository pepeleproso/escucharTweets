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
from Event import Event

class Observable(object):
    def __init__(self):
        self.callbacks = []

    def subscribe(self, event, callback):
        self.callbacks.append((event, callback))

    def unsubscribe(self, event, callback):
        self.callbacks.remove((event, callback))

    def fire(self, event, **attrs):
        e = Event()
        e.source = self
        for k, v in attrs.iteritems():
            setattr(e, k, v)
        for evento, fn in self.callbacks:
            if evento == event:
                fn(e)
