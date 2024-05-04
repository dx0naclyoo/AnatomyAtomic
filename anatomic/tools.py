from enum import Enum
from typing import Any
from unittest.mock import Base
from pydantic import ValidationError, BaseModel


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


def redis_to_pydantic(model: BaseModel, redis_item: str):

    new_str = "{" + redis_item.replace("\n", "=Q1") + "}"
    dict_obj = eval(new_str)
    local_model = model.parse_obj(dict_obj)

    for tup_key_val in local_model:
        key, value = tup_key_val

        if isinstance(value, str):
            setattr(local_model, key, value.replace("=Q1", "\n"))

    return local_model
