from enum import Enum
from typing import Any

from pydantic import ValidationError


class SortedMode(str, Enum):
    NAME = "byName"
    ID = "byID"
    CONTENT = "byContent"


def convert_pydantic_to_sql(item: Any, table):
    if isinstance(item, table):
        return item
    else:
        try:
            return table(**item.dict())
        except ValidationError as e:
            raise e


def is_sql_table(item: Any, table) -> bool:
    if isinstance(item, table):
        return True
    else:
        return False
