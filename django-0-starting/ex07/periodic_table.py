def ft_parse_element(line: str) -> dict:
    ft_element = [_.strip() for _ in line.split('=')]
    ft_elem_tmp_data = [_.strip() for _ in ft_element[1].split(',')]
    ft_elem_tmp_data = [_.split(':') for _ in ft_elem_tmp_data]
    ft_elem_tmp_data = [[__.strip() for __ in _]
                        for _ in ft_elem_tmp_data]
    ft_elem_data = {}
    ft_elem_data['name'] = str(ft_element[0])
    for _ in ft_elem_tmp_data:
        ft_elem_data[_[0]] = _[1]
    ft_elem_data['position'] = int(ft_elem_data['position'])
    ft_elem_data['number'] = int(ft_elem_data['number'])
    ft_elem_data['small'] = str(ft_elem_data['small'])
    ft_elem_data['molar'] = float(ft_elem_data['molar'])
    ft_elem_data['electron'] = \
        list(map(int, str(ft_elem_data['electron']).split()))
    if ft_elem_data['electron'][-1] == 18:
        ft_elem_data['electron'].append(0)
    ft_elem_data['row'] = len(ft_elem_data['electron']) - 1
    del ft_elem_data['electron']
    return ft_elem_data


def my_periodic_table():
    with open("periodic_table.txt", "r") as filein:
        lines = [_.strip() for _ in filein.readlines()]
        filein.close()
    with open("periodic_table.css", "w") as fileout:
        print("""\
:root {
    --ft-bg-color: #000;
    --ft-text-color: #fff;
}

body {
    height: 100vh;
    width: 100%;
    padding: 0;
    margin: 0;
    background-color: var(--ft-bg-color);
    color: var(--ft-text-color);
}

h4 {
    font-size: 10px;
}

table {
    width: 100%;
    height: 100%;
}

table, tr, td {
    border-collapse: collapse;
}

td {
    width: calc(100% / 18);
    height: calc(100% / 7);
    border: 1px solid var(--ft-text-color);
}

.element {
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
}

.gap {
    border-top: none;
    border-bottom: none;
}

.athom {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.athom-number, .athom-mass {
    padding-top: 3px;
}

.athom-number {
    padding-left: 3px;
    text-align: left;
}

.athom-mass {
    padding-right: 3px;
    text-align: right;
    font-size: 11px;
}

.element-symbol {
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 40px;
}

.element-name {
    text-align: center;
}""", file=fileout)
        fileout.close()
    with open("periodic_table.html", "w") as fileout:
        print("""<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Periodic table of the elements</title>
        <link rel="stylesheet" href="./periodic_table.css">
    </head>
    <body>
        <table>""", file=fileout)
        ft_parsed = [ft_parse_element(_) for _ in lines]
        ft_tmp_dict = {}
        for _ in ft_parsed:
            ft_tmp_dict[_.get('row')] = []
        for _ in ft_parsed:
            ft_tmp_dict[_.get('row')].append(_)
        ft_table = []
        for _ in ft_tmp_dict.values():
            for __ in _:
                del __['row']
            ft_table.append(_)
        for _ in ft_table:
            print("""\
            <tr>""", file=fileout)
            for __ in range(len(_)):
                print(f"""\
                <td>
                    <div class="element">
                        <div class="athom">
                            <div class="athom-number">\
{_[__].get('number')}</div>
                            <div class="athom-mass">{_[__].get('molar')}</div>
                        </div>
                        <div class="element-symbol">{_[__].get('small')}</div>
                        <div class="element-name"><h4>{_[__].get('name')}</h4></div>
                    </div>
                </td>""", file=fileout)
                if __ < len(_) - 1:
                    dif = _[__ + 1].get('position') - _[__].get('position')
                    if dif > 1:
                        print(f"""\
                <td colspan="{dif - 1}" class="gap"></td>""", file=fileout)
            print("""\
            </tr>""", file=fileout)
        print("""\
        </table>
    </body>
</html>""", file=fileout)
        fileout.close()


if __name__ == '__main__':
    my_periodic_table()
