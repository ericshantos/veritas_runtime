# -*- coding: utf-8 -*-
"""
@Author  : Eric dos Santos (ericshantos13@gmail.com)
Main module for running the fake news prediction pipeline over network connections.
"""

from src import launcher
from dotenv import load_dotenv

load_dotenv()


if __name__ == "__main__":
    launcher.init()
    