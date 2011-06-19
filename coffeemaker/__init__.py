from led import Led
from waterdispenser import WaterDispenser
from groundcoffedispenser import GroundCoffeeDispenser
from core import CoffeeMaker

class InsufficientResourceException(Exception):
    pass