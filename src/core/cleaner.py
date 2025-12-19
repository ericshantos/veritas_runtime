# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Module for preprocessing and cleaning Portuguese text data using spaCy.
"""

import spacy
from unidecode import unidecode

class TextCleaner:
    """
    Cleans and preprocesses Portuguese text using spaCy.
    Removes stopwords and punctuation, and applies lemmatization and accent normalization.
    """

    def __init__(self):
        """
        Initializes the TextCleaner with the Portuguese spaCy model.
        """
        self.nlp = spacy.load("pt_core_news_sm")

    def __call__(self, text: str) -> str:
        """
        Processes and cleans the given text.

        Steps:
            - Tokenizes the text.
            - Removes stopwords and punctuation.
            - Applies lemmatization.
            - Removes accents from lemmatized tokens.

        Args:
            text (str): Raw input text.

        Returns:
            str: Cleaned and normalized text.
        """
        doc = self.nlp(text)
        tokens = [unidecode(token.lemma_) for token in doc if not token.is_stop and not token.is_punct]
        return ' '.join(tokens)
    