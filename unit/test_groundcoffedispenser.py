import unittest
import coffeemaker
import mock

class TestGroundCoffeeDispenser(unittest.TestCase):
    def setUp(self):
        self.led_mock = mock.Mock(coffeemaker.Led)

    def test_ground_coffee_dispenser_is_correctly_initialized(self):
        dispenser = coffeemaker.GroundCoffeeDispenser(self.led_mock)

        self.assertEquals(self.led_mock, dispenser._led)
        self.assertEquals(self.led_mock.on.call_count, 1)

    def test_ground_coffee_dispenser_can_report_insufficient_amount(self):
        dispenser = coffeemaker.GroundCoffeeDispenser(self.led_mock)

        self.assertFalse(dispenser.has(5))
    
    def test_ground_coffee_dispenser_can_report_sufficient_amount(self):
        dispenser = coffeemaker.GroundCoffeeDispenser(self.led_mock)
        dispenser._amount = 5

        self.assertTrue(dispenser.has(5))

    def test_ground_coffee_dispenser_can_deliver_ground_coffee(self):
        dispenser = coffeemaker.GroundCoffeeDispenser(self.led_mock)
        dispenser._amount = 10

        ground_coffee = dispenser.get(6)

        self.assertEquals( ('groundcoffee', 6,), ground_coffee)
        self.assertEquals(4, dispenser._amount)

    def test_ground_coffee_dispenser_can_be_filled(self):
        dispenser = coffeemaker.GroundCoffeeDispenser(self.led_mock)
        dispenser.fill(10)

        self.assertEquals(10,dispenser._amount)

    def test_ground_coffee_dispenser_can_turn_off_led_when_sufficient_filled(self):
        dispenser = coffeemaker.GroundCoffeeDispenser(self.led_mock)
        dispenser.fill(10)

        self.assertEquals(1,self.led_mock.off.call_count)

    def test_ground_coffee_dispenser_does_not_turn_off_led_when_insufficient_filled(self):
        dispenser = coffeemaker.GroundCoffeeDispenser(self.led_mock)
        dispenser.fill(4)

        self.assertEquals(0,self.led_mock.off.call_count)

    def test_ground_coffee_dispenser_can_turn_off_led_when_resting_a_few(self):
        dispenser = coffeemaker.GroundCoffeeDispenser(self.led_mock)
        dispenser._amount = 10
        dispenser.get(6)

        self.assertEquals(2,self.led_mock.on.call_count)

    def test_ground_coffee_dispenser_does_not_turn_off_led_when_resting_a_lot(self):
        dispenser = coffeemaker.GroundCoffeeDispenser(self.led_mock)
        dispenser._amount = 10
        dispenser.get(2)

        self.assertEquals(1,self.led_mock.on.call_count)
