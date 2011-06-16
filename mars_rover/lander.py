class Lander(object):
    _accelerator = None
    _altimeter = None

    def __init__(self, accelerator, altimeter):
        self._accelerator = accelerator
        self._altimeter = altimeter