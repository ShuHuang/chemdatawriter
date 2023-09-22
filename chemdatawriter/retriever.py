# -*- coding: utf-8 -*-
"""
chemdatawriter.retriever

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This module contains the Retriever class.
Author: Shu Huang (sh2009@cam.ac.uk)
"""
from haystack.nodes import TfidfRetriever
from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import PreProcessor, TextConverter
from haystack.pipelines import DocumentSearchPipeline


class Retriever:
    def __init__(self, papers):
        self.paper_list = papers
        self.doc_store = InMemoryDocumentStore()
        
        self.preprocessor = PreProcessor(
            clean_empty_lines=True,
            clean_whitespace=True,
            clean_header_footer=True,
            split_by="word",
            split_length=200,
            split_respect_sentence_boundary=True,
            split_overlap=0
        )
        self.text_converter = TextConverter(
            remove_numeric_tables=True,
            valid_languages=["en"],
            valid_language_prob_threshold=0.99
        )
        self.retriever = TfidfRetriever(document_store=self.doc_store)
        self.pipeline = DocumentSearchPipeline(self.retriever)

    def _write_to_cache(self, cache_path):
        """Writes papers to cache for processing."""
        for index, text in enumerate(self.paper_list):
            with open(f"{cache_path}{index}.txt", "w") as f:
                f.write(text)

    def _load_docs_from_cache(self, cache_path):
        """Loads documents from cache and processes them for retrieval."""
        for index in range(len(self.paper_list)):
            doc = self.text_converter.convert(
                file_path=f"{cache_path}{index}.txt",
                meta={"index": index}
            )
            docs = self.preprocessor.process(doc)
            self.doc_store.write_documents(docs)

    def retrieve(self, query, cache_path, chapter_size):
        """Retrieve relevant sections based on the query."""
        self._write_to_cache(cache_path)
        self._load_docs_from_cache(cache_path)
        
        result = self.pipeline.run(query, params={"Retriever": {"top_k": chapter_size}})
        section_indices = [x.to_dict()["meta"]["index"] for x in result["documents"]]
        
        # Return unique section indices in the order they appeared
        return sorted(set(section_indices), key=section_indices.index)
