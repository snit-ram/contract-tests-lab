import unittest
import mars_rover

class TestAccelerometer( unittest.TestCase ):

    def test_accelerometer_can_report_acceleration(self):
        accelerometer = mars_rover.Accelerometer()
        accelerometer._acceleration = 5
        acceleration = accelerometer.get_acceleration()

        self.assertEquals(acceleration, 5)

    def test_accelerometer_can_set_acceleration(self):
        accelerometer = mars_rover.Accelerometer()
        acceleration = accelerometer.set_acceleration(5)

        self.assertEquals(accelerometer._acceleration, 5)

if __name__ == '__main__':
    unittest.main()