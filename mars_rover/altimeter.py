class Altimeter(object):
    _altitude = 0

    def get_altitude(self):
        return self._altitude

    def set_altitude(self,altitude):
        self._altitude = altitude