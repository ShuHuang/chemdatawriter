# -*- coding: utf-8 -*-
"""
chemdatawriter.title_generator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module provides functionality to generate titles.
Author: Shu Huang (sh2009@cam.ac.uk)
"""
from transformers import pipeline


class TitleGenerator:
    """Generates titles using a specified model."""

    def __init__(self, title_generator_hf='tennessejoyce/titlewave-t5-base'):
        """Initialize the TitleGenerator with the given model."""
        self.model = pipeline("text2text-generation", title_generator_hf)

    def generate(self, text, max_length=30, num_beams=5):
        """Generate a title for the provided text."""
        return self.model(text, max_length=max_length, num_beams=num_beams)[0]['generated_text']
