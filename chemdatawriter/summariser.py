# -*- coding: utf-8 -*-
"""
chemdatawriter.summariser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains the Summariser class.
Author: Shu Huang (sh2009@cam.ac.uk)
"""
from abc import ABC, abstractmethod
from transformers import (
    BartTokenizer, BartForConditionalGeneration,
    LEDTokenizer, LEDForConditionalGeneration,
    PegasusTokenizer, PegasusForConditionalGeneration,
    T5Tokenizer, T5ForConditionalGeneration
)
import summa


class Summariser(ABC):
    """Base class for summariser."""

    def __init__(self):
        """Initialize the summariser."""
        self.text = None

    @abstractmethod
    def summarise(self, text, *args, **kwargs):
        """Abstract method to summarize the data."""
        pass

    def read(self, text):
        """Set the text for summarization."""
        self.text = text


class TransformerSummariser(Summariser):
    """Base class for Transformer-based summarisers."""

    def __init__(self, model_name):
        super().__init__()
        self.model_name = model_name
        self.model, self.tokenizer = self._load_model_and_tokenizer()

    def _load_model_and_tokenizer(self):
        """Loads the appropriate model and tokenizer based on the model name."""
        models = {
            "bart": (BartForConditionalGeneration, BartTokenizer),
            "led": (LEDForConditionalGeneration, LEDTokenizer),
            "pegasus": (PegasusForConditionalGeneration, PegasusTokenizer),
            "t5": (T5ForConditionalGeneration, T5Tokenizer)
        }

        model_type = self.model_name.split("/")[1].split("-")[0]
        model_class, tokenizer_class = models[model_type]
        return model_class.from_pretrained(self.model_name), tokenizer_class.from_pretrained(self.model_name)

    def summarise(self, text, max_length=140):
        """Summarize the input text."""
        input_ids = self.tokenizer.encode(text, return_tensors='pt')
        summary_ids = self.model.generate(input_ids, num_beams=4, max_length=max_length, early_stopping=True)
        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)


class TextRankSummariser(Summariser):
    """TextRank summariser using the Summa library."""

    def summarise(self, text):
        """Use TextRank to summarize the input text."""
        return summa.summarizer.summarize(text)

    def keywords(self, text, words=5):
        """Extract keywords from the input text."""
        return summa.keywords.keywords(text, words=words)


# Specific Transformer Summarisers
class LargeBartSummariser(TransformerSummariser):
    """LargeBART summariser for samsum."""
    def __init__(self):
        super().__init__("philschmid/bart-large-cnn-samsum")


class DistilBartSummariser(TransformerSummariser):
    """DistilBART summariser."""
    def __init__(self):
        super().__init__("sshleifer/distilbart-cnn-12-6")


class LargeBookLEDSummariser(TransformerSummariser):
    """LargeBook LED summariser."""
    def __init__(self):
        super().__init__("pszemraj/led-large-book-summary")


class XsumPegasusSummariser(TransformerSummariser):
    """Xsum Pegasus summariser."""
    def __init__(self):
        super().__init__("google/pegasus-xsum")


class LongBookT5Summariser(TransformerSummariser):
    """LongBook T5 summariser."""
    def __init__(self):
        super().__init__("pszemraj/long-t5-tglobal-base-16384-book-summary")
