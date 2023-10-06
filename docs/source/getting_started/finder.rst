===========================
TopicFinder
===========================

Provides the TopicFinder class for identifying key topics from text.

Classes
-------
.. class:: chemdatawriter.finder.TopicFinder(embedding_model: str = None, hdbscan_min_topic_size: int = 10, hdbscan_min_samples: int = 5, umap_n_neighbors: int = 15, umap_n_components: int = 5, umap_min_dist: float = 0.05, n_gram_range: tuple = (1, 2), vectorizer_model=None, *args, **kwargs)

    Extends the BERTopic model for topic identification.

    This model utilizes SentenceTransformer embeddings, UMAP for dimensionality
    reduction, and HDBSCAN for clustering to identify and represent topics from text.

    .. attribute:: embedding_model

        An instance of the SentenceTransformer used for embeddings. Default model is `all-MiniLM-L6-v2`.

    .. attribute:: hdbscan_model

        HDBSCAN clustering model. Utilizes parameters like `min_cluster_size`, `min_samples`, metric as 'euclidean', and `cluster_selection_method` as 'eom'.

    .. attribute:: umap_model

        UMAP model used for dimensionality reduction. Configured with parameters like `n_neighbors`, `n_components`, `min_dist`, and metric as 'cosine'.

    .. attribute:: vectorizer_model

        Vectorizer model, defaulted to CountVectorizer with English stop words and the specified `n_gram_range`.

