# -*- coding: utf-8 -*-
"""
chemdatawriter.paraphraser

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains the Paraphraser class.
Author: Shu Huang (sh2009@cam.ac.uk)
"""

from rouge import Rouge
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class Paraphraser:
    """A class to perform paraphrasing using back-translation."""

    def __init__(self, language='de'):
        """Initialize with a specific language for back-translation."""
        prefix = "Helsinki-NLP/opus-mt-"
        language_map = {
            'de': ('facebook/wmt19-en-de', 'Helsinki-NLP/opus-mt-gem-en'),
            'zh': (prefix + 'en-zh', prefix + 'zh-en'),
            'ge': (prefix + 'en-de', prefix + 'de-en'),
            'fr': (prefix + 'en-fr', prefix + 'fr-en'),
            'ru': (prefix + 'en-ru', prefix + 'ru-en'),
            'ar': (prefix + 'en-ar', prefix + 'ar-en'),
            'jap': (prefix + 'en-jap', prefix + 'jap-en')
        }

        if language in language_map:
            self.en_lan, self.lan_en = language_map[language]
        else:
            supported_languages = ', '.join(language_map.keys())
            raise ValueError(f"Please provide one of the following languages for back-translation: {supported_languages}")

        self.forward_tokenizer = AutoTokenizer.from_pretrained(self.en_lan)
        self.backward_tokenizer = AutoTokenizer.from_pretrained(self.lan_en)
        self.forward_model = AutoModelForSeq2SeqLM.from_pretrained(self.en_lan)
        self.backward_model = AutoModelForSeq2SeqLM.from_pretrained(self.lan_en)

    def paraphrase(self, text):
        """Paraphrase a given text using back-translation."""
        forward_inputs = self.forward_tokenizer.encode(text, return_tensors="pt")
        forward_outputs = self.forward_model.generate(**forward_inputs)
        forward_translation = self.forward_tokenizer.decode(forward_outputs[0], skip_special_tokens=True)

        backward_inputs = self.backward_tokenizer.encode(forward_translation, return_tensors="pt")
        backward_outputs = self.backward_model.generate(**backward_inputs)
        backward_translation = self.backward_tokenizer.decode(backward_outputs[0], skip_special_tokens=True)

        return backward_translation

    def score(self, text):
        """Calculate the Rouge score for the paraphrased version of the text."""
        rouge = Rouge()
        paraphrased_text = self.paraphrase(text)
        scores = rouge.get_scores(text, paraphrased_text)
        return scores
