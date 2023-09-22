# -*- coding: utf-8 -*-
"""
Module: chemdatawriter.finder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Provides the TopicFinder class for identifying key topics from text.

Author: Shu Huang (sh2009@cam.ac.uk)
"""

# Third-party libraries
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import CountVectorizer
from hdbscan import HDBSCAN
from umap import UMAP


class TopicFinder(BERTopic):
    """
    Extends the BERTopic model for topic identification.

    This model utilizes SentenceTransformer embeddings, UMAP for dimensionality 
    reduction, and HDBSCAN for clustering to identify and represent topics from text.
    """

    def __init__(self,
                 embedding_model: str = None,
                 hdbscan_min_topic_size: int = 10,
                 hdbscan_min_samples: int = 5,
                 umap_n_neighbors: int = 15,
                 umap_n_components: int = 5,
                 umap_min_dist: float = 0.05,
                 n_gram_range: tuple = (1, 2),
                 vectorizer_model=None,
                 *args, **kwargs):
        """
        Initialize the TopicFinder with specified models and parameters.
        """
        super().__init__(*args, **kwargs)

        # Embedding model - Sentence Transformer
        self.embedding_model = embedding_model or SentenceTransformer('all-MiniLM-L6-v2')

        # HDBSCAN clustering model
        self.hdbscan_model = HDBSCAN(
            min_cluster_size=hdbscan_min_topic_size,
            min_samples=hdbscan_min_samples,
            metric='euclidean',
            cluster_selection_method='eom'
        )

        # UMAP dimensionality reduction model
        self.umap_model = UMAP(
            n_neighbors=umap_n_neighbors,
            n_components=umap_n_components,
            min_dist=umap_min_dist,
            metric='cosine'
        )

        # Vectorizer model
        self.vectorizer_model = vectorizer_model or CountVectorizer(stop_words='english', ngram_range=n_gram_range)
