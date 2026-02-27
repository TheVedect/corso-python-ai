from LLMModel import LLMModel
class GPTModel(LLMModel):
    def genera(self, prompt):
        return f"Risposta locale per {prompt}."