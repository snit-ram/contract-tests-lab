import unittest
import mars_rover

class TestLander( unittest.TestCase ):

    def test_lander_initializates_correctly( self ):
        altimeter_stub = object()
        accelerator_stub = object()

        lander = mars_rover.Lander(altimeter=altimeter_stub, accelerator=accelerator_stub)

        self.assertEquals(lander._altimeter, altimeter_stub)
        self.assertEquals(lander._accelerator, accelerator_stub)


if __name__ == '__main__':
    unittest.main()