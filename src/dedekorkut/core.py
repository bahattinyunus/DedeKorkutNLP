from .preprocessing import normalize_text, tokenize_text
from .evaluation import calculate_wer, calculate_cer

class DedeKorkut:
    """
    The Visionary Agent for Turkish NLP.
    Connects the past to the future through code.
    """
    def __init__(self):
        self.wisdom = True

    def preprocess(self, text, mode="standard"):
        """
        Processes text with the wisdom of the ancients.
        """
        if mode == "deep_clean":
            # Just a placeholder for the "deep" logic
            return normalize_text(text)
        return normalize_text(text)
