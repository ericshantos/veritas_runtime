# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Module responsible for loading dependencies required for prediction.
"""

import pickle
from huggingface_hub import hf_hub_download
from tensorflow.keras.models import load_model

class ModelLoader:
    """
    Loads a trained Keras model and its corresponding tokenizer from Hugging Face Hub.
    """

    def __init__(self, repo_id: str, model_filename: str, tokenizer_filename: str):
        """
        Initializes the ModelLoader by downloading and loading the model and tokenizer from Hugging Face Hub.

        Args:
            repo_id (str): Repository ID on Hugging Face Hub (e.g., "ericshantos/veritas-lstm-ptbr").
            model_filename (str): Filename of the model file in the repository.
            tokenizer_filename (str): Filename of the tokenizer file in the repository.
        """
        # Download model
        model_path = hf_hub_download(
            repo_id=repo_id,
            filename=model_filename
        )
        self.model = load_model(model_path)
        
        # Download tokenizer
        tokenizer_path = hf_hub_download(
            repo_id=repo_id,
            filename=tokenizer_filename
        )
        with open(tokenizer_path, "rb") as f:
            self.tokenizer = pickle.load(f)
            