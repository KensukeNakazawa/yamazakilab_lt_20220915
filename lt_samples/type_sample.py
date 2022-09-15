
from typing import Tuple, Type


# x, y, w, h
a = [1, 2, 3, 2]
b = [1, 2, 3, 2]

def compare_bbox_1(a, b):
    if a[3] / a[4] > b[3] / b[4]:
        return True
    return False


def compare_bbox_2(a: Tuple[int, int, int, int], b Tuple[int, int, int, int]) -> bool:
    if a[3] / a[4] > b[3] / b[4]:
        return True
    return False

class BoundingBox:
    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self._x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @property
    def width(self) -> int:
        return self.x2 - self.x1
    
    @property
    def height(self) -> int:
        return self.y2 - self.y1

    @property
    def aspect_ratio(self) -> float:
        return self.width / self.height

    @property
    def x1(self):
        return self._x1

    @x1.setter
    def x1(self, value: int):
        if value > self.x2:
            ValueError('')
            
        if isinstance(value, int):
            self._x1 = value
        else:
            TypeError('')


def compare_bbox_3(a: BoundingBox, b: BoundingBox) -> bool:
    if a.aspect_ratio > b.aspect_ratio:
        return True
    return False
