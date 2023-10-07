.. ChemDataWriter documentation master file, created by
   sphinx-quickstart on Fri Aug 18 21:23:09 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ChemDataWriter's documentation!
==========================================

ChemDataWriter is a transformer-based open-source toolkit, developed in Python, that leverages artificial intelligence to autonomously compile books that encapsulate key research findings.
It serves as a tool for scientists seeking to remain abreast of the newest developments in their fields.

Key Highlights of ChemDataWriter:
   * Automated Book Creation: ChemDataWriter facilitates the generation of comprehensive review books from a collection of research papers. By inputting a corpus of papers and optionally a set of topics for a table of contents, the toolkit crafts an in-depth review with minimal user intervention.
   * Seven-Stage Workflow: The toolkit encompasses a streamlined process with seven distinct stages: downloading of papers, paper screening, topic modeling, text retrieval & re-ranking, summarization, content organization, and the automated generation of references.
   * Focus on Accuracy: Utilizing a conservative summarization technique, ChemDataWriter ensures that the summarized content is both accurate and representative of the original research. Rather than inventing new content, it restructures existing information for clarity and brevity.
   * Integration with BatteryDataExtractor: ChemDataWriter incorporates BatteryDataExtractor for efficient paper downloading, processing HTML/XML documents, and filtering out non-pertinent papers based on keywords.
   * Usage of BERTopic: For nuanced topic generation, BERTopic is employed to cluster research papers semantically and extract unique topic representations.
   * Relevance-Driven Retrieval: With Haystack's retriever module, the toolkit identifies and ranks relevant papers based on the specified topics, ensuring the most pertinent research is included.
   * Structured Output: ChemDataWriter doesn't just summarize; it organizes. The generated content is systematically structured into a book format, complete with an academic-style reference list derived from the metadata of source files.

ChemDataWriter stands as a testament to the fusion of AI and research, making the process of staying updated more streamlined and efficient.

Citing: S.Huang, J. M. Cole, ChemDataWriter: A Transformer-based Toolkit for Auto-generating Books That Summarise Research (2023) DOI: 10.1039/d3dd00159h



.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Contents:

   getting_started/quick_start
   getting_started/reader
   getting_started/finder
   getting_started/retriever
   getting_started/summariser
   getting_started/paraphraser
   getting_started/title_generator
   getting_started/latex_generator



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
