#!/usr/bin/python3


class Text(str):
    def __str__(self):
        return super().__str__().replace('<', '&lt;').replace(
            '>', '&gt;').replace('"', '&quot;').replace('\n', '\n<br />\n')


class Elem:
    tag: str
    attr: dict
    content: list
    tag_type: str

    class ValidationError(Exception):
        def __init__(self):
            super().__init__("incorrect behaviour.")

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        self.tag = tag
        self.attr = attr
        self.content = []
        if not (Elem.check_type(content) or content is None):
            raise Elem.ValidationError
        if type(content) is list:
            self.content = content
        elif content is not None:
            self.content.append(content)
        if not (tag_type == 'simple' or tag_type == 'double'):
            raise Elem.ValidationError
        self.tag_type = tag_type

    def __str__(self):
        result = '<{tag}{attr}'.format(tag=self.tag,
                                       attr=self.__make_attr())
        if self.tag_type == 'double':
            result += '>{content}</{tag}>'.format(
                content=self.__make_content(),
                tag=self.tag)
        elif self.tag_type == 'simple':
            result += ' />'
        return result

    def __make_attr(self):
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            if len(str(elem)) > 0:
                result += str(elem) + '\n'
        result = "  ".join(line for line in result.splitlines(True))
        if len(result.strip()) <= 0:
            return ''
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) is list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        return (isinstance(content, Elem) or type(content) is Text or
                (type(content) is list and all([type(elem) is Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))


def test():
    doc = Elem('html',
               content=[
                   Elem('head',
                        content=Elem('title',
                                     content=Text('"Hello ground!"'))),
                   Elem('body',
                        content=[
                            Elem('h1',
                                 content=Text('"Oh no, not again!"')),
                            Elem('img',
                                 attr={'src': "http://i.imgur.com/pfp3T.jpg"},
                                 tag_type='simple')
                        ])
               ])
    print(doc)


if __name__ == '__main__':
    test()
