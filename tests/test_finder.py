# -*- coding: utf-8 -*-
"""
tests.test_finder
~~~~~~~~~~~~~~~~~

This module contains the tests for the chemdatacomposer.finder module.
"""

import os
import unittest
import warnings

# Module under test
from chemdatawriter.reader import Reader
from chemdatawriter.finder import TopicFinder


def suppress_warnings(test_func):
    """Decorator to suppress specific warnings during the execution of test cases."""
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ResourceWarning)
            test_func(self, *args, **kwargs)
    return do_test


class TestTopicFinder(unittest.TestCase):

    @suppress_warnings
    def setUp(self):
        """Setup test environment by reading files and initializing the TopicFinder model."""
        test_papers_folder = os.path.join(os.path.dirname(__file__), "test_papers")
        file_paths = [
            os.path.join(test_papers_folder, f) for f in os.listdir(test_papers_folder)
            if os.path.isfile(os.path.join(test_papers_folder, f)) and f.endswith(('.html', '.xml'))
        ]

        self.cdc_papers = [Reader(file, "bde") for file in file_paths]
        self.abstracts = [paper.abstract for paper in self.cdc_papers]
        self.bertopicmodel = TopicFinder()

    def test_topicfinder_init(self):
        """Test the initialization of the TopicFinder model."""
        self.assertIsNotNone(self.bertopicmodel)

    def test_topicfinder_fit_transform(self):
        """Test the fit_transform method of the TopicFinder model."""
        topics, _ = self.bertopicmodel.fit_transform(self.abstracts*100)
        self.assertIsNotNone(topics)
