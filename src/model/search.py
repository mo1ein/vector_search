from pydantic import StrictStr

from src.model.base import BaseVectorModel


class SearchModel(BaseVectorModel):
    query: StrictStr | None = None


class OutputSearchModel(BaseVectorModel):
    similar_text: StrictStr | None
