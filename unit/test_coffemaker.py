import unittest
import coffeemaker
import mock

class TestCoffeeMaker(unittest.TestCase):
    def setUp(self):
        self.water_dispenser_mock = mock.Mock(coffeemaker.WaterDispenser)
        self.ground_coffee_dispenser_mock = mock.Mock(coffeemaker.GroundCoffeeDispenser)

    def test_coffeemaker_is_correctly_initialized(self):
        cm = coffeemaker.CoffeeMaker(self.water_dispenser_mock, self.ground_coffee_dispenser_mock)

        self.assertEquals(self.water_dispenser_mock, cm._water_dispenser)
        self.assertEquals(self.ground_coffee_dispenser_mock, cm._ground_coffee_dispenser)

    def test_coffeemaker_can_make_coffee(self):
        self.water_dispenser_mock.has.return_value = True
        self.ground_coffee_dispenser_mock.has.return_value = True

        self.water_dispenser_mock.get.return_value = ('water', 5)
        self.ground_coffee_dispenser_mock.get.return_value = ('ground_coffee', 5)

        cm = coffeemaker.CoffeeMaker(self.water_dispenser_mock, self.ground_coffee_dispenser_mock)
        coffee = cm.make_coffee()

        self.assertEquals( ('coffee', 1), coffee)


    def test_coffeemaker_tries_to_make_coffe_without_sufficient_water_shoul_raise_exception(self):
        self.water_dispenser_mock.has.return_value = False

        cm = coffeemaker.CoffeeMaker(self.water_dispenser_mock, self.ground_coffee_dispenser_mock)

        self.assertRaises( coffeemaker.InsufficientResourceException, cm.make_coffee )

    def test_coffeemaker_tries_to_make_coffe_without_sufficient_ground_coffe_shoul_raise_exception(self):
        self.water_dispenser_mock.has.return_value = True
        self.ground_coffee_dispenser_mock.has.return_value = False

        cm = coffeemaker.CoffeeMaker(self.water_dispenser_mock, self.ground_coffee_dispenser_mock)

        self.assertRaises( coffeemaker.InsufficientResourceException, cm.make_coffee )