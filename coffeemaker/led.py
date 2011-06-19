class Led(object):
    _on = False

    def on(self):
        self._on = True

    def off(self):
        self._on = False

    def is_on(self):
        return self._on