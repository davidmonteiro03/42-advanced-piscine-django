import sys


def my_state():
    states = {"Oregon": "OR",
              "Alabama": "AL",
              "New Jersey": "NJ",
              "Colorado": "CO"}
    capital_cities = {"OR": "Salem",
                      "AL": "Montgomery",
                      "NJ": "Trenton",
                      "CO": "Denver"}
    argc = len(sys.argv)
    if argc != 2:
        exit()
    ft_tmp = None
    for key, value in zip(capital_cities.keys(), capital_cities.values()):
        if value == sys.argv[1]:
            ft_tmp = key
    if not ft_tmp:
        print("Unknown capital city")
        exit()
    for key, value in zip(states.keys(), states.values()):
        if value == ft_tmp:
            print(key)


if __name__ == '__main__':
    my_state()
