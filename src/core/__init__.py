from .cleaner import TextCleaner
from .model_loader import MyModel, MyTokenizer
from .news_classifier import NewsClassifier
from .predictor import Predictor


class Factory:
    @staticmethod
    def create_classifier(repo: str) -> NewsClassifier:
        model = MyModel(repo)
        tokenizer = MyTokenizer(repo)

        text_cleaner = TextCleaner()

        news_predictor = Predictor(
            model=model.instance,
            tokenizer=tokenizer.instance,
        )

        classifier = NewsClassifier(news_predictor, text_cleaner)

        return classifier


__all__ = ["Factory"]

__author__ = "Eric Santos <ericshantos13@gmail.com>"
