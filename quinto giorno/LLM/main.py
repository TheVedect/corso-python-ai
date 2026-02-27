from GPTModel import GPTModel
from LocalEmbedding import  LocalEmbedding
from OpenAIEmbedding import OpenAIEmbedding
from PipelineAI import PipelineAI

pipeline_1 = PipelineAI(GPTModel(), OpenAIEmbedding())
pipeline_2 = PipelineAI(GPTModel(), LocalEmbedding())

result_1 = pipeline_1.esegui("Cosa è il ML?")
result_2 = pipeline_2.esegui("Cosa è il ML?")

print(result_1)
print(result_2)
