# -*- coding: utf-8 -*-
"""
tests.test_summariser
==========================
This module contains the tests for the summariser module.
"""
import unittest
from chemdatawriter.summariser import DistilBartSummariser

class TestDistilBartSummariser(unittest.TestCase):
    
    def setUp(self):
        self.text = ("Due to the massive growth of scientific publications, literature mining is becoming "
                     "increasingly popular for researchers to thoroughly explore scientific text and extract such "
                     "data to create new databases or augment existing databases. Efforts in literature-mining "
                     "software design and implementation have improved text-mining productivity, but most of the "
                     "toolkits that mine text are based on traditional machine-learning algorithms which hinder the "
                     "performance of downstream text-mining tasks. Natural language processing (NLP) and text-mining "
                     "technologies have seen a rapid development since the release of transformer models, such as "
                     "bidirectional encoder representations from transformers (BERT). Upgrading rule-based or "
                     "machine-learning-based literature-mining toolkits by embedding transformer models into the "
                     "software is likely to improve the text-mining performance. To this end, we release a "
                     "Python-based literature-mining toolkit for the field of battery materials, BatteryDataExtractor, "
                     "which involves the embedding of BatteryBERT models in its automated data-extraction pipeline. "
                     "This pipeline employs BERT models for token-classification tasks, such as abbreviation detection, "
                     "part-of-speech tagging, and chemical-named-entity recognition, as well as new double-turn "
                     "question-answering data-extraction models for auto-generating repositories of inter-related "
                     "material and property data as well as general information. We demonstrate that BatteryDataExtractor "
                     "exhibits state-of-the-art performance on the evaluation data sets for both token classification and "
                     "automated data extraction. To aid the use of BatteryDataExtractor, its code is provided as open-source "
                     "software, with associated Documentation to serve as a user guide.")

    def test_distilbart_summariser(self):
        summariser = DistilBartSummariser()
        summary = summariser.summarise(self.text)

        expected_summary = ("Literature mining is becoming increasingly popular for researchers to thoroughly explore "
                            "scientific text and extract such data to create new databases or augment existing databases. "
                            "Most of the toolkits that mine text are based on machine-learning algorithms which hinder the "
                            "performance of downstream text-mining tasks. We demonstrate that BatteryDataExtractor "
                            "exhibits state-of-the-art performance on the evaluation data sets.")

        self.assertEqual(summary, expected_summary)

if __name__ == '__main__':
    unittest.main()
