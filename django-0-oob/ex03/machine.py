#!/usr/bin/python3
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino
import random


class CoffeeMachine:
    class EmptyCup(HotBeverage):
        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90

        def description(self) -> str:
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def __init__(self):
        self.drinks_stock = 10

    def repair(self):
        self.drinks_stock = 10

    def serve(self, drink: HotBeverage) -> HotBeverage:
        if self.drinks_stock <= 0:
            raise CoffeeMachine.BrokenMachineException
        self.drinks_stock -= 1
        random_drink = random.randint(0, 4)
        return drink() if random_drink != 0 else CoffeeMachine.EmptyCup()


def test():
    coffee_machine = CoffeeMachine()
    available_drinks = [Coffee, Tea, Chocolate, Cappuccino]
    for _ in range(50):
        try:
            drink = random.choice(available_drinks)
            served = coffee_machine.serve(drink)
            print(f"served: {served}")
            # print(f"served: {served.name}")
        except CoffeeMachine.BrokenMachineException as e:
            print(f"Machine error: {e}")
            coffee_machine.repair()
        except Exception as e:
            print(f"Fatal error: {e}")


if __name__ == "__main__":
    test()
