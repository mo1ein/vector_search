from abc import abstractmethod
from typing import Any, Mapping, Sequence, Type
from uuid import UUID

from sqlalchemy import Executable


_CoreSingleExecuteParams = Mapping[str, Any]
_CoreMultiExecuteParams = Sequence[_CoreSingleExecuteParams]
AnyExecuteParams = _CoreMultiExecuteParams | _CoreSingleExecuteParams


class SqlAlchemyPort:
    @abstractmethod
    def create(self, entity, return_data: bool = False):
        raise NotImplementedError

    @abstractmethod
    def bulk_create(self, entities, return_data: bool = False):
        raise NotImplementedError

    @abstractmethod
    def get_by_uuid(self, entity_type: Type, entity_uuid: UUID):
        raise NotImplementedError

    @abstractmethod
    def delete(self, entity) -> None:
        raise NotImplementedError

    @abstractmethod
    def bulk_delete(self, entities) -> None:
        raise NotImplementedError

    @abstractmethod
    def execute(self, statement: Executable, params: AnyExecuteParams | None = None):
        raise NotImplementedError

    @abstractmethod
    def scalars(self, statement: Executable, params: AnyExecuteParams | None = None):
        raise NotImplementedError