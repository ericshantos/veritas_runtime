# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos
Module for preprocessing and cleaning Portuguese text data using spaCy.
"""


class TextCleaner:
    def __call__(self, text: str) -> str:
        return text.strip()
