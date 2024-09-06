from src.model.vector import GetVectorModel
from src.model.search import SearchModel, OutputSearchModel
from src.repository.vector import Repository
from src.service.nlp import NLPService
from src.utils.decorators.atomic import atomic
from scipy.spatial.distance import cosine
import numpy as np


class SearchService:
    def __init__(self) -> None:
        self.repository = Repository()
        self.NLPService = NLPService()

    @atomic
    def get_data(self):
        res = self.repository.search()
        return res

    def convert_to_vector(self, input_model: SearchModel) -> list[float]:
        vector_query = self.NLPService.encode(input_model.query)
        return vector_query

    def calc_similarity(self, data: list, vector_query: list):
        similarities = []
        for row in data:
            db_vector = np.array(row.vector)
            similarity = self.cosine_similarity(vector_query, db_vector)
            similarities.append((row.id, similarity))

        # Sort by similarity (highest first) and return top results
        similarities.sort(key=lambda x: x[1], reverse=True)
        return similarities[:2]

    @atomic
    def get_vector_by_ids(self, ids: list[int]) -> GetVectorModel:
        res = self.repository.get_vector_by_ids(ids)
        return res

    def process(self, input_model: SearchModel) -> OutputSearchModel:
        data = self.get_data()
        vector_query = self.convert_to_vector(input_model)
        result = self.calc_similarity(data.data, vector_query)
        ids = [item[0] for item in result]
        similar_rows = self.get_vector_by_ids(ids)
        result_string = ' '.join(item.text for item in similar_rows.data)
        output_model = OutputSearchModel(similar_text=result_string)
        return output_model

    @staticmethod
    def cosine_similarity(vec1, vec2):
        return 1 - cosine(vec1, vec2)
