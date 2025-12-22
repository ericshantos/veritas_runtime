# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos
Module for preprocessing and cleaning Portuguese text data using spaCy.
"""

from typing import Iterable, Optional
import spacy
from unidecode import unidecode


class TextCleaner:
    """
    Cleans and preprocesses Portuguese text using spaCy.

    Features:
    - Stopword removal
    - Punctuation removal
    - Lemmatization
    - Accent normalization
    - Token length filtering
    """

    def __init__(
        self,
        nlp: Optional[spacy.language.Language] = None,
        remove_stopwords: bool = True,
        remove_punctuation: bool = True,
        remove_accents: bool = True,
        min_token_length: int = 2,
    ):
        self.nlp = nlp or spacy.load(
            "pt_core_news_sm",
            disable=["ner", "parser"]
        )

        self.remove_stopwords = remove_stopwords
        self.remove_punctuation = remove_punctuation
        self.remove_accents = remove_accents
        self.min_token_length = min_token_length

    def _normalize_token(self, token) -> str:
        text = token.lemma_.lower()

        if self.remove_accents:
            text = unidecode(text)

        return text

    def __call__(self, text: str) -> str:
        if not isinstance(text, str) or not text.strip():
            return ""

        doc = self.nlp(text)

        tokens = []
        for token in doc:
            if self.remove_stopwords and token.is_stop:
                continue

            if self.remove_punctuation and token.is_punct:
                continue

            if token.like_num:
                continue

            norm = self._normalize_token(token)

            if len(norm) < self.min_token_length:
                continue

            tokens.append(norm)

        return " ".join(tokens)

    def batch(self, texts: Iterable[str]) -> list[str]:
        """
        Cleans multiple texts efficiently using spaCy's nlp.pipe.
        """
        results = []

        for doc in self.nlp.pipe(texts):
            tokens = [
                unidecode(token.lemma_.lower())
                for token in doc
                if not token.is_stop
                and not token.is_punct
                and not token.like_num
                and len(token.lemma_) >= self.min_token_length
            ]
            results.append(" ".join(tokens))

        return results
