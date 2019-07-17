from typing import TypeVar, Generic, List

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self):
        return repr(self._container)


num_discs: int = 3
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()
for i in range(1, num_discs + 1):
    tower_a.push(i)


def hanoiFunc(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        hanoiFunc(begin, temp, end, n - 1)
        hanoiFunc(begin, end, temp, 1)
        hanoiFunc(temp, end, begin, n - 1)


if __name__ == "__main__":
    print("-------Before Game-------")
    print(tower_a)
    print(tower_b)
    print(tower_c)
    hanoiFunc(tower_a, tower_c, tower_b, num_discs)
    print("-------After Game------")
    print(tower_a)
    print(tower_b)
    print(tower_c)
