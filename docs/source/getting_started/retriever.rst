=============================
Retriever
=============================

This module contains the Retriever class.

Classes
-------
.. class:: chemdatawriter.retriever.Retriever(papers)

    Retriever class for processing and retrieving relevant sections.

    .. method:: __init__(papers)

       Initialize the Retriever.

       :param papers: List of papers to process.
       :type papers: list

    .. method:: _write_to_cache(cache_path)

       Writes papers to cache for processing.

       :param cache_path: Path to write papers.
       :type cache_path: str

    .. method:: _load_docs_from_cache(cache_path)

       Loads documents from cache and processes them for retrieval.

       :param cache_path: Path to load papers.
       :type cache_path: str

    .. method:: retrieve(query, cache_path, chapter_size)

       Retrieve relevant sections based on the query.

       :param query: Search query for retrieval.
       :type query: str
       :param cache_path: Path to cache.
       :type cache_path: str
       :param chapter_size: Number of sections to retrieve.
       :type chapter_size: int
       :return: List of indices of relevant sections.
       :rtype: list

