import sys


def my_all_in():
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
    ft_input = [s.strip() for s in sys.argv[1].split(",")]
    for i in ft_input:
        if len(i) == 0:
            continue
        ft_tmp = None
        ft_state = None
        for key, value in zip(states.keys(), states.values()):
            if key.lower() == i.lower():
                ft_state = key
                ft_tmp = value
                break
        if ft_tmp:
            print(f"{capital_cities[ft_tmp]} is the capital of {ft_state}")
            continue
        ft_tmp = None
        ft_capital = None
        for key, value in zip(capital_cities.keys(), capital_cities.values()):
            if value.lower() == i.lower():
                ft_tmp = key
                ft_capital = value
                break
        if ft_tmp:
            for key, value in zip(states.keys(), states.values()):
                if value.lower() == ft_tmp.lower():
                    print(f"{ft_capital} is the capital of {key}")
                    break
            continue
        print(f"{i} is neither a capital city nor a state")


if __name__ == '__main__':
    my_all_in()
