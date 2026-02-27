from EmbeddingModel import EmbeddingModel
class OpenAIEmbedding(EmbeddingModel):

    def genera_embedding(self, testo):
        return [10, 0.5, 0.3]