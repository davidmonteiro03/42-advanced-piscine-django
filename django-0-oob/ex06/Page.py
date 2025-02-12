#!/usr/bin/python3
from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, \
    Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Elem, Text


class Page:
    def __init__(self, elem: Elem()) -> None:
        if not isinstance(elem, Elem):
            raise Elem.ValidationError()
        self.elem = elem

    def __str__(self) -> str:
        result = ""
        if isinstance(self.elem, Html):
            result += "<!DOCTYPE html>\n"
        result += str(self.elem)
        return result

    def write_to_file(self, path: str) -> None:
        f = open(path, "w")
        f.write(self.__str__())

    def is_valid(self) -> bool:
        return self.__recursive_check(self.elem)

    def __recursive_check(self, elem: Elem) -> bool:
        return True


def test():
    pages = [
        Page(
            Html([
                Head([
                    Title([
                        Text("textttttttttt")
                    ])
                ]),
                Body([
                    H1([
                        Text("textttttttttt")
                    ]),
                    H2([
                        Text("textttttttttt")
                    ]),
                    Div(),
                    Table([
                        Tr([
                            Th([
                                Text("textttttttttt")
                            ]),
                            Th([
                                Text("textttttttttt")
                            ])
                        ]),
                        Tr([
                            Td([
                                Text("textttttttttt")
                            ]),
                            Td([
                                Text("textttttttttt")
                            ])
                        ])
                    ]),
                    Ul([
                        Li([
                            Text("textttttttttt")
                        ]),
                        Li([
                            Text("textttttttttt")
                        ]),
                        Li([
                            Text("textttttttttt")
                        ])
                    ]),
                    Ol([
                        Li([
                            Text("textttttttttt")
                        ]),
                        Li([
                            Text("textttttttttt")
                        ]),
                        Li([
                            Text("textttttttttt")
                        ])
                    ]),
                    Span([
                        Text("textttttttttt"),
                        P([
                            Text("textttttttttt")
                        ])
                    ]),
                    Text()
                ])
            ])
        )
    ]
    for p in pages:
        print("=" * 100)
        print(p.elem)
        print("-" * 100)
        print(p.is_valid())
        print()


if __name__ == '__main__':
    test()
