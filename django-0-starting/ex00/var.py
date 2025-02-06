def my_var():
    ft_int = 42
    ft_str = "42"
    ft_str_long = "quarante-deux"
    ft_float = 42.0
    ft_bool = True
    ft_list = [42]
    ft_dict = {42: 42}
    ft_tuple = (42,)
    ft_set = set()
    print(f"{ft_int} has a type {type(ft_int)}")
    print(f"{ft_str} has a type {type(ft_str)}")
    print(f"{ft_str_long} has a type {type(ft_str_long)}")
    print(f"{ft_float} has a type {type(ft_float)}")
    print(f"{ft_bool} has a type {type(ft_bool)}")
    print(f"{ft_list} has a type {type(ft_list)}")
    print(f"{ft_dict} has a type {type(ft_dict)}")
    print(f"{ft_tuple} has a type {type(ft_tuple)}")
    print(f"{ft_set} has a type {type(ft_set)}")


if __name__ == '__main__':
    my_var()
