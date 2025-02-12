#!/usr/bin/python3


class Intern:
    class Coffee:
        def __str__(self) -> str:
            return "This is the worst coffee you ever tasted."

    def __init__(self, Name: str = None):
        self.Name = Name if Name is not None \
            else "My name? I'm nobody, an intern, I have no name."

    def __str__(self) -> str:
        return self.Name

    def work(self) -> str:
        raise Exception("I'm just an intern, I can't do that...")

    def make_coffee(self) -> Coffee:
        return Intern.Coffee()


def test():
    unknown = Intern()
    mark = Intern(Name="Mark")
    print(unknown.Name)
    print(mark.Name)
    print(mark.make_coffee())
    try:
        unknown.work()
    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    test()
