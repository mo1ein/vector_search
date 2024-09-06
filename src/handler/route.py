from fastapi import status, APIRouter

from src.model.search import SearchModel, OutputSearchModel
from src.service.scrap import ScrapService
from src.service.search import SearchService

routes = APIRouter()


@routes.post("/search", response_model=OutputSearchModel, tags=["search api"], status_code=status.HTTP_200_OK)
def search(request: SearchModel) -> OutputSearchModel:
    return SearchService().process(request)


@routes.post("/", tags=["scrap data"], status_code=status.HTTP_201_CREATED)
def init():
    data = ScrapService()
    data = data.run()
    ScrapService().embed(data)
    return "Text extracted, embedded and saved to db successfully!"
