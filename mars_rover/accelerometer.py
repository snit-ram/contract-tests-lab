class Accelerometer(object):
    _acceleration = 0

    def get_acceleration(self):
        return self._acceleration


    def set_acceleration(self,acceleration):
        self._acceleration=acceleration