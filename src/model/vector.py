from pydantic import StrictStr

from src.model.base import BaseVectorModel


class VectorModel(BaseVectorModel):
    id: int | None = None
    vector: list | None = None
    text: StrictStr | None = None

class GetVectorModel(BaseVectorModel):
    data: list[VectorModel]
