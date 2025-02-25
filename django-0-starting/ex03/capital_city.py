import sys


def my_capital_city():
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
    ft_tmp = states.get(sys.argv[1])
    if not ft_tmp:
        print("Unknown state")
        exit()
    print(capital_cities[ft_tmp])


if __name__ == '__main__':
    my_capital_city()
