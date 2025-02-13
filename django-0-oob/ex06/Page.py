#!/usr/bin/python3
from elements import Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, \
    Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Elem, Text


class Page:
    def __init__(self, elem: Elem | Text) -> None:
        if not isinstance(elem, Elem) and type(elem) is not Text:
            raise Elem.ValidationError
        self.elem = elem

    def __str__(self) -> str:
        result = ''
        if isinstance(self.elem, Html):
            result += '<!DOCTYPE html>\n'
        return result + str(self.elem)

    def write_to_file(self, path: str) -> None:
        with open(path, 'w') as filein:
            filein.write(str(self))
            filein.close()

    def is_valid(self) -> bool:
        return self.__recursive_check(self.elem)

    def __recursive_check(self, elem: Elem) -> bool:
        if not (isinstance(elem, (Html, Head, Body, Title, Meta, Img, Table,
                                  Th, Tr, Td, Ul, Ol, Li, H1, H2, P, Div,
                                  Span, Hr, Br, Elem)) or type(elem) is Text):
            return False
        if type(elem) is Text:
            return True
        if elem.tag_type == 'simple':
            return True
        if isinstance(elem, (Title, H1, H2, Li, Th, Td)):
            if sum([type(e) is Text for e in elem.content]) != 1:
                return False
            if len(elem.content) != 1:
                return False
            if all([self.__recursive_check(e) for e in elem.content]):
                return True
        if isinstance(elem, P):
            if not all([type(e) is Text for e in elem.content]):
                return False
            if all([self.__recursive_check(e) for e in elem.content]):
                return True
        if isinstance(elem, Span):
            if not all([type(e) is Text or isinstance(e, P)
                        for e in elem.content]):
                return False
            if all([self.__recursive_check(e) for e in elem.content]):
                return True
        if isinstance(elem, (Ul, Ol)):
            if not all([isinstance(e, Li) for e in elem.content]):
                return False
            if len(elem.content) < 1:
                return False
            if all([self.__recursive_check(e) for e in elem.content]):
                return True
        if isinstance(elem, Tr):
            if not all([isinstance(e, (Th, Td)) for e in elem.content]):
                return False
            if len(elem.content) < 1:
                return False
            if not all([isinstance(e, type(elem.content[0]))
                        for e in elem.content]):
                return False
            if all([self.__recursive_check(e) for e in elem.content]):
                return True
        if isinstance(elem, Table):
            if not all([isinstance(e, Tr) for e in elem.content]):
                return False
            if all([self.__recursive_check(e) for e in elem.content]):
                return True
        if isinstance(elem, Head):
            if sum([type(e) is Title for e in elem.content]) != 1:
                return False
            if len(elem.content) != 1:
                return False
            if all([self.__recursive_check(e) for e in elem.content]):
                return True
        if isinstance(elem, (Body, Div)):
            if not all([isinstance(e, (H1, H2, Div, Table,
                                       Ul, Ol, Span)) or type(e) is Text
                        for e in elem.content]):
                return False
            if all([self.__recursive_check(e) for e in elem.content]):
                return True
        if isinstance(elem, Html):
            if len(elem.content) != 2:
                return False
            if not (isinstance(elem.content[0], Head) and
                    isinstance(elem.content[1], Body)):
                return False
            if all([self.__recursive_check(e) for e in elem.content]):
                return True
        return False


def check_pages(pages: list[Page], width: int) -> None:
    for _ in range(len(pages)):
        print("~" * ((width - 8) // 2),
              "Content",
              "~" * ((width - 8) // 2 - (width % 2 == 0)))
        print(pages[_])
        print("~" * width)
        print(f"is_valid: {pages[_].is_valid()}")
        print()
        pages[_].write_to_file(f"page-{_ + 1}.html")


def test():
    width: int = 100
    try:
        check_pages([
            Page(Html([Head(Title(Text("coisa"))), Body()])),
            Page(Body()),
            Page(Body([
                Div(attr={'id': 'navbar',
                          'class': 'sticky-top'}),
                Div(attr={'id': 'content'}),
                Div(attr={'id': 'modal'}),
                Div(attr={'id': 'footer',
                          'class': 'footer mt-auto'})
            ], attr={
                'class': 'd-flex flex-column vh-100 starfield'
            }))  # something from transcendence :)
        ], width)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)


if __name__ == '__main__':
    test()
