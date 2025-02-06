def my_var_to_dict():
    d = [('Hendrix', '1942'),
         ('Allman', '1946'),
         ('King', '1925'),
         ('Clapton', '1945'),
         ('Johnson', '1911'),
         ('Berry', '1926'),
         ('Vaughan', '1954'),
         ('Cooder', '1947'),
         ('Page', '1944'),
         ('Richards', '1943'),
         ('Hammett', '1962'),
         ('Cobain', '1967'),
         ('Garcia', '1942'),
         ('Beck', '1944'),
         ('Santana', '1947'),
         ('Ramone', '1948'),
         ('White', '1975'),
         ('Frusciante', '1970'),
         ('Thompson', '1949'),
         ('Burton', '1939')]
    ft_d_set = {}
    for elem in d:
        ft_d_set[elem[1]] = elem[0]
    for key, value in zip(ft_d_set.keys(), ft_d_set.values()):
        print(key, value, sep=" : ")


if __name__ == '__main__':
    my_var_to_dict()
