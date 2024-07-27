import random
import json
from typing import Any
example_of_bear_json: dict = {"bear_type": "BLACK", "bear_name": "mikhail", "bear_age": 17.5}

available_types_for_bears: list = ["POLAR", "BROWN", "BLACK", "GUMMY"]
available_name_for_bears: list = ["mikhail", "toptishka", "Mickalich", "GUMMY"]

not_available_types_for_bears: list = ["LAR", 2133, "MAMBA", "SNAKE"]
not_available_name_for_bears: list = ["hgjhdk", "hgdhsi", "hggdhgd", "Gfdyiobb"]


def get_available_bears_json() -> Any:
    out: dict = example_of_bear_json
    out.update(bear_type=random.choice(available_types_for_bears))
    out.update(bear_name=random.choice(available_name_for_bears))
    out.update(bear_age=random.randint(0, 35))
    return json.dumps(out)


def get_broken_bear_json() -> Any:
    out: dict = example_of_bear_json
    out.update(bear_type=random.choice(not_available_types_for_bears))
    out.update(bear_name=random.choice(not_available_name_for_bears))
    out.update(bear_age=random.randint(-1000, 0))
    return json.dumps(out)
