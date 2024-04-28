from enum import Enum


class SortedMode(str, Enum):
    NAME = "byName"
    ID = "byID"
    CONTENT = "byContent"
