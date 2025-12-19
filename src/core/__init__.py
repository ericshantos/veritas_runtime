from .news_classifier import NewsClassifier
from .predictor import Predictor
from .cleaner import TextCleaner
from .model_loader import ModelLoader

loader = ModelLoader(
    repo_id="ericshantos/veritas-lstm-ptbr",
    model_filename="veritas-lstm-ptbr.keras",
    tokenizer_filename="tokenizer.pkl"
)

text_cleaner = TextCleaner()

new_predictor = Predictor(
    model=loader.model,
    tokenizer=loader.tokenizer
)

classifier = NewsClassifier(
    new_predictor,
    text_cleaner
)

__all__ = ["classifier"]

__author__ = "Eric Santos <ericshantos13@gmail.com>"
