import coffeemaker

class CoffeeMaker(object):
    _water_dispenser = None
    _ground_coffee_dispenser = None

    _water_amount = 5
    _ground_coffee_amount = 5

    def __init__(self, water_dispenser, ground_coffee_dispenser):
        self._water_dispenser = water_dispenser
        self._ground_coffee_dispenser = ground_coffee_dispenser

    def make_coffee(self):
        if not self._water_dispenser.has( self._water_amount ):
            raise coffeemaker.InsufficientResourceException

        if not self._ground_coffee_dispenser.has( self._ground_coffee_amount ):
            raise coffeemaker.InsufficientResourceException
        
        water = self._water_dispenser.get( self._water_amount )
        ground_coffee = self._ground_coffee_dispenser.get( self._ground_coffee_amount )

        concentration = ground_coffee[1] / water[1] 

        return ('coffee', concentration)