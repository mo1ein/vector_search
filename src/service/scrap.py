from bs4 import BeautifulSoup
import requests

from src.config.config import ScrapConfig
from src.model.vector import VectorModel
from src.repository.vector import Repository
from src.service.nlp import NLPService
from src.utils.decorators.atomic import atomic


class ScrapService:
    def __init__(self) -> None:
        self.repository = Repository()
        self.NLPService = NLPService()

    # Function to scrape a single page
    def scrap(self, url: str) -> list[dict]:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract relevant data from the page
        stories = soup.find_all('tr', class_='athing')

        res = []
        for story in stories:
            title = story.find('span', class_='titleline')
            title = title.find('a')
            if title:
                title = title.text

            res.append(title)
        return res

    def run(self) -> list[str]:
        # Scrape the first 5 pages
        res = []
        for page_num in range(1, 6):
            url = f"{ScrapConfig.SCRAP_URL}?p={page_num}"
            # todo: use log
            print(f"Scraping page {page_num}...")
            page = self.scrap(url)
            res += page

        return res

    @atomic
    def embed(self, data: list[dict]):
        for d in data:
            vector = self.NLPService.encode(d)
            dic = {"text": d, "vector": vector}
            self.repository.create_news(VectorModel(**dic))
