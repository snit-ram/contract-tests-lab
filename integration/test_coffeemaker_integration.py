import unittest
import coffeemaker

class TestCoffeeMakerIntegration(unittest.TestCase):
    def setUp(self):
        self.water_led = coffeemaker.Led()
        self.coffee_led = coffeemaker.Led()

        self.water_dispenser = coffeemaker.WaterDispenser(self.water_led)
        self.coffee_dispenser = coffeemaker.GroundCoffeeDispenser(self.coffee_led)


    def test_init_empty_coffeemaker_should_turn_on_leds(self):
        cm = coffeemaker.CoffeeMaker(self.water_dispenser, self.coffee_dispenser)

        self.assertTrue(self.water_led.is_on())
        self.assertTrue(self.coffee_led.is_on())


    def test_filling_water_dispenser_with_sufficient_water_sould_turn_off_led(self):
        cm = coffeemaker.CoffeeMaker(self.water_dispenser, self.coffee_dispenser)

        self.water_dispenser.fill(10)

        self.assertFalse(self.water_led.is_on())
        self.assertTrue(self.coffee_led.is_on())


    def test_filling_coffe_dispenser_with_sufficient_coffe_sould_turn_off_led(self):
        cm = coffeemaker.CoffeeMaker(self.water_dispenser, self.coffee_dispenser)

        self.coffee_dispenser.fill(10)

        self.assertFalse(self.coffee_led.is_on())
        self.assertTrue(self.water_led.is_on())


    def test_filling_dispensers_with_insufficient_resources_should_not_turn_off_leds(self):
        cm = coffeemaker.CoffeeMaker(self.water_dispenser, self.coffee_dispenser)

        self.water_dispenser.fill(2)
        self.coffee_dispenser.fill(3) 

        self.assertTrue(self.water_led.is_on())
        self.assertTrue(self.coffee_led.is_on())


    def test_make_coffe_with_empty_water_dispenser_should_raise_exception(self):
        cm = coffeemaker.CoffeeMaker(self.water_dispenser, self.coffee_dispenser)
        self.assertRaises(coffeemaker.InsufficientResourceException, cm.make_coffee)


    def test_make_coffe_with_empty_coffe_dispenser_should_raise_exception(self):
        cm = coffeemaker.CoffeeMaker(self.water_dispenser, self.coffee_dispenser)
        self.water_dispenser.fill(10)

        self.assertRaises(coffeemaker.InsufficientResourceException, cm.make_coffee)


    def test_make_coffe_with_filled_dispensers_should_return_coffee(self):
        cm = coffeemaker.CoffeeMaker(self.water_dispenser, self.coffee_dispenser)

        self.water_dispenser.fill(10)
        self.coffee_dispenser.fill(10)
        coffee = cm.make_coffee()

        self.assertEquals(('coffee', 1), coffee)


    def test_make_coffe_with_that_rests_low_water_should_turn_on_water_led(self):
        cm = coffeemaker.CoffeeMaker(self.water_dispenser, self.coffee_dispenser)

        self.water_dispenser.fill(6)
        self.coffee_dispenser.fill(10)
        coffee = cm.make_coffee()

        self.assertTrue(self.water_led.is_on())
        self.assertFalse(self.coffee_led.is_on())


    def test_make_coffe_with_that_rests_low_coffe_should_turn_on_coffe_led(self):
        cm = coffeemaker.CoffeeMaker(self.water_dispenser, self.coffee_dispenser)

        self.water_dispenser.fill(10)
        self.coffee_dispenser.fill(6)
        coffee = cm.make_coffee()

        self.assertTrue(self.coffee_led.is_on())
        self.assertFalse(self.water_led.is_on())