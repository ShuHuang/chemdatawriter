# -*- coding: utf-8 -*-
"""
chemdatawriter.reader
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains the Reader class, which is used to read the paper.
Author: Shu Huang (sh2009@cam.ac.uk)
"""
from abc import ABC
import json
from batterydataextractor import Document
from batterydataextractor.doc.text import Abstract


class Reader(ABC):
    """Reader class to process and retrieve details from the BDE document."""

    def __init__(self, path_or_paper=None, doctype=None):
        """
        Initialize the Reader with a path or a paper.

        Args:
            path_or_paper (str|dict): The path to the document or the paper itself.
            doctype (str): The type of the document ("bde" or "json").
        """
        self.path_or_paper = path_or_paper
        self.doctype = doctype
        self.document = None
        
        if self.doctype == "bde":
            self._load_bde()
        elif self.doctype == "json":
            self._load_json()
        else:
            raise ValueError("Please specify the doctype 'bde' or 'json'")

    def _load_bde(self):
        """Load BDE document."""
        self.document = Document.from_file(self.path_or_paper)

    def _load_json(self):
        """Load JSON document."""
        if isinstance(self.path_or_paper, str) and self.path_or_paper.endswith(".json"):
            with open(self.path_or_paper, "r") as f:
                self.document = json.load(f)
        elif isinstance(self.path_or_paper, dict):
            self.document = self.path_or_paper
        else:
            raise ValueError('The input paper must be a dictionary or path of json files.')

    def _get(self, field, default_value=""):
        """Generic getter for metadata."""
        return self.metadata.get(field, default_value)

    @property
    def metadata(self):
        """Retrieve the metadata from the document."""
        return self.document[0].serialize() if self.doctype == "bde" else self.document

    @property
    def title(self):
        """Retrieve the title."""
        return self._get('title')

    @property
    def authors(self):
        """Retrieve the authors."""
        return self._get('authors')

    @property
    def date(self):
        """Retrieve the date."""
        return self._get('date')

    @property
    def abstract(self):
        """Retrieve the abstract."""
        abstract_text = self._get('abstract')
        if not abstract_text and self.doctype == "bde":
            for element in self.document.elements:
                if isinstance(element, Abstract):
                    return element.text
        return abstract_text

    @property
    def doi(self):
        """Retrieve the DOI."""
        return self._get('doi')

    @property
    def body(self):
        """Retrieve the body of the document."""
        if self.doctype == "json":
            return self._get('body')
        elif self.doctype == "bde":
            return [element.text for element in self.document.elements[1:]]
