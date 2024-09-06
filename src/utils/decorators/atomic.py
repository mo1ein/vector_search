from functools import partial
from typing import Any, Callable

from src.utils.orm.session_manager import SessionManager


def atomic(function: Callable | None = None) -> Callable | partial:
    return _atomic(function) if function else partial(_atomic)


def _atomic(function: Callable) -> Callable:
    def wrapper(*args: list[Any], **kwargs: dict[Any, Any]) -> Any:
        session_manager = SessionManager()
        session = session_manager.get_session()
        try:
            if session.in_transaction():
                return function(*args, **kwargs)
            else:
                with session.begin(nested=False):
                    return function(*args, **kwargs)
        except Exception as exception:
            if not session.in_transaction():
                session.rollback()
            raise exception
        finally:
            if not session.in_transaction():
                session_manager.remove_session()

    return wrapper
