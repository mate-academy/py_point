"""
module point
"""


class Point:
    """
    Class represents point in 2D space; w/o dataclasses.
    """

    def __init__(self, frst_num, sec_num) -> None:
        self.frst_num = frst_num
        self.sec_num = sec_num

    def __eq__(self, obj) -> bool:
        return self.frst_num == obj.frst_num and self.sec_num == obj.sec_num

    def __hash__(self) -> int:
        return hash(self.frst_num) + hash(self.sec_num)

    def __str__(self) -> str:
        return f"({self.frst_num}, {self.sec_num})"

    def __repr__(self) -> str:
        return f"Point({self.frst_num}, {self.sec_num})"
