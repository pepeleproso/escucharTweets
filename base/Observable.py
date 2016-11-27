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