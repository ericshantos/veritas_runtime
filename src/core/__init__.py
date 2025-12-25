from dataclasses import dataclass
from .news_classifier import NewsClassifier
from .predictor import Predictor
from .cleaner import TextCleaner
from .model_loader import ModelLoader

class Factory:
    @staticmethod
    def create_classifier(
        repo_id: str, 
        model_filename: str, 
        tokenizer_filename: str
    ) -> NewsClassifier:
        loader = ModelLoader(
            repo_id=repo_id,
            model_filename=model_filename,
            tokenizer_filename=tokenizer_filename
        )

        text_cleaner = TextCleaner()

        news_predictor = Predictor(
            model=loader.model,
            tokenizer=loader.tokenizer
        )

        classifier = NewsClassifier(
            news_predictor,
            text_cleaner
        )

        return classifier


__all__ = ["Factory"]

__author__ = "Eric Santos <ericshantos13@gmail.com>"
