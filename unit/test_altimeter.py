import unittest
import mars_rover

class TestAltimeter( unittest.TestCase ):

    def test_altimeter_can_report_altitude( self ):
        altimeter = mars_rover.Altimeter()
        altimeter._altitude = 5
        altitude = altimeter.get_altitude()

        self.assertEquals(altitude, 5)


    def test_altimeter_can_set_altitude(self):
        altimeter = mars_rover.Altimeter()
        altitude = altimeter.set_altitude(5)

        self.assertEquals(altimeter._altitude, 5)

if __name__ == '__main__':
    unittest.main()