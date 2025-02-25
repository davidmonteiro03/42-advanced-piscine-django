#!/usr/bin/python3


class HotBeverage:
    def __init__(self):
        self.price = 0.30
        self.name = "hot beverage"

    def description(self) -> str:
        return "Just some hot water in a cup."

    def __str__(self) -> str:
        template: str = ("name : {name}\n"
                         "price : {price:.2f}\n"
                         "description : {description}")
        return template.format(name=self.name,
                               price=self.price,
                               description=self.description())


class Coffee(HotBeverage):
    def __init__(self):
        self.name = "coffee"
        self.price = 0.40

    def description(self) -> str:
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    def __init__(self):
        self.name = "tea"
        self.price = 0.30


class Chocolate(HotBeverage):
    def __init__(self):
        self.name = "chocolate"
        self.price = 0.50

    def description(self) -> str:
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    def __init__(self):
        self.name = "cappuccino"
        self.price = 0.45

    def description(self) -> str:
        return "Un po' di Italia nella sua tazza!"


def test():
    print(HotBeverage())
    print(Coffee())
    print(Tea())
    print(Chocolate())
    print(Cappuccino())


if __name__ == "__main__":
    test()
