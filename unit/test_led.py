import unittest
import coffeemaker

class TestLed(unittest.TestCase):

    def test_led_can_switch_on(self):
        led = coffeemaker.Led()
        led.on()

        self.assertTrue(led._on)


    def test_led_can_switch_off(self):
        led = coffeemaker.Led()
        led._on = True
        led.off()

        self.assertFalse(led._on)

    def test_led_can_report_on_state(self):
        led = coffeemaker.Led()

        self.assertFalse( led.is_on() )
        led._on = True
        self.assertTrue( led.is_on() )

if __name__ == '__main__':
    unittest.main()