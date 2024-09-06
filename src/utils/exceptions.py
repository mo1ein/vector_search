from typing import Any


class CommonsBaseException(Exception):
    ...


class InvalidEntityTypeException(TypeError):
    def __init__(self, entity: Any, type_: type | list[type]):
        super().__init__(f"INAPPROPRIATE ARGUMENT TYPE, {entity} MUST BE INHERITED FROM {type_}")


class DefinitionException(CommonsBaseException):
    def __init__(self, message: str | None = None):
        super().__init__(message)