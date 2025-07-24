"""Code demostrates the use of DataClasses vs manually writing your own code"""


from dataclasses import dataclass, astuple, asdict


@dataclass(frozen=True, order=True)
class Comment:
    id: int
    text: str




class ManualComment:
    def __init__(self, id: int, text: str) -> None:
        """must be immutable, so that it can be hashable"""
        self.__id: int = id
        self.__text: str = text

    @property
    def id(self):
        return self.__id

    @property
    def text(self):
        return self.__text

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, text={self.text})"

    def __eq__(self, other) -> bool:
        if other.__class__ is self.__class__:
            return (self.id, self.text) == (other.id, other.text)
        else:
            return NotImplemented

    def __ne__(self, other) -> bool:
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result

    def __hash__(self) -> int:
        """Make it hashable so that it can be stored in a dict"""
        return hash((self.__class__, self.id, self.text))

    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) < (other.id, other.text)
        else:
            return NotImplemented

    def __le__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) <= (other.id, other.text)
        else:
            return NotImplemented

    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) > (other.id, other.text)
        else:
            return NotImplemented

    def __ge__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) >= (other.id, other.text)
        else:
            return NotImplemented


def main():
    comment = Comment(1, "I am Root")
    print(comment)
    print(astuple(comment))
    print(asdict(comment))


if __name__ == '__main__':
    main()
