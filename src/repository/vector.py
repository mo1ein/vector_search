from sqlalchemy import select
from src.model.entity import VectorEntity
from src.model.vector import VectorModel, GetVectorModel
from src.utils.orm.sqlalchemy_adapter import SqlAlchemyAdapter


class Repository(SqlAlchemyAdapter):
    def __init__(self) -> None:
        super().__init__()

    def create_news(self, input_model: VectorModel) -> None:
        news = VectorEntity(**input_model.model_dump(exclude_unset=True, exclude_none=True))
        self.create(news)

    def search(self, limit=10) -> GetVectorModel:
        query = select(VectorEntity).limit(limit)
        entities = self.scalars(query).all()
        response_model = [VectorModel.model_validate(q) for q in entities]
        return GetVectorModel(data=response_model)

    def get_vector_by_ids(self, ids: list[int]) -> GetVectorModel:
        query = select(VectorEntity).where(VectorEntity.id.in_(ids))
        entities = self.scalars(query).all()
        response_model = [VectorModel.model_validate(q) for q in entities]
        return GetVectorModel(data=response_model)
