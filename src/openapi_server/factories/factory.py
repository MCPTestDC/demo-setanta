from typing import get_origin, get_args, List, Tuple, Set, Dict
from polyfactory.factories.pydantic_factory import ModelFactory
import random
import string

factories = {}

MOCK_BUILTIN_TYPES = {
    str: lambda: ''.join(random.choices(string.ascii_letters, k=random.randint(5, 20))),
    int: lambda: random.randint(-10**random.randint(1, 8), 10**random.randint(1, 8) - 1),
    float: lambda: round(random.uniform(-10**random.randint(1, 8), 10**random.randint(1, 8)), random.randint(1, 5)),
    bool: lambda: random.choice([True, False]),
    bytes: lambda: (''.join(random.choices(string.ascii_letters, k=random.randint(5, 20)))).encode()
}

def generic_mock_model(model_type):
    origin = get_origin(model_type)

    if origin in {list, List}:
        inner_type = get_args(model_type)[0]
        return [generic_mock_model(inner_type) for _ in range(random.randint(1, 10))]

    if origin in {tuple, Tuple}:
        inner_types = get_args(model_type)
        return tuple(generic_mock_model(t) for t in inner_types) if inner_types else ()

    if origin in {set, Set}:
        inner_type = get_args(model_type)[0]
        return {generic_mock_model(inner_type) for _ in range(random.randint(1, 10))}

    if origin in {dict, Dict}:
        key_type, value_type = get_args(model_type)
        return {
            generic_mock_model(key_type): generic_mock_model(value_type)
            for _ in range(random.randint(1, 10))
        }
    
    if model_type is None:
        return None

    if model_type in MOCK_BUILTIN_TYPES:
        return MOCK_BUILTIN_TYPES[model_type]()

    if model_type not in factories:
        MockModelFactory = type(
            f"MockModelFactory{model_type.__name__}",
            (ModelFactory,),
            {"__model__": model_type}
        )
        factories[model_type] = MockModelFactory

    return factories[model_type].build()
