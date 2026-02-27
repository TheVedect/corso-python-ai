from abc import ABC, abstractmethod

class LLMModel(ABC):

    @abstractmethod
    def genera(self, prompt):
        pass