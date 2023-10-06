=================================
Quick Start
=================================

Installation
---------------------------------

To get started with ChemDataWriter, you can easily install it using ``pip``. Currently, it's compatible with Python versions below 3.10:

.. code-block:: python

        pip install chemdatawriter

Introduction
---------------------------------
ChemDataWriter provides two main scripts for book generation:

    * ``run_corpus.py``: Generates the corpus of the book.
    * ``run_cdw.py``: Generates the book itself.


Corpus Retrieval
---------------------------------
To generate the corpus, utilize the ``run_corpus.py`` script:

.. code-block:: python

        python run_corpus.py --input_path <path_to_XML_files> --save_path <path_to_save_corpus>

Arguments:

    * input_path : Specifies the directory of XML files
    * save_path : Determines the folder location to save the corpus in JSON format.

The resulting JSON file contains entries, each depicting a paper:

    * title: Title of the paper.
    * abstract: Abstract of the paper.
    * introduction: Introduction section of the paper.
    * conclusion: Conclusion section of the paper.
    * reference: Formatted reference of the paper.


.. note::
    The script emphasizes sections with "Introduction" and "Conclusion" in their titles. Absent these sections, a paper will be excluded from the results.
    The script sequentially appends each paper's details to the output JSON.

Book Generation
---------------------------------
For book generation, employ the ``run_cdw.py`` script:

.. code-block:: python

    python run_cdw.py --input_path <path_to_XML_files> --keywords <keyword1 keyword2> --topic_words <topic_word1 topic_word2> --chapter_size <int> --save_path <path_to_save_corpus> --cache_path <path_to_cache> --title_generator_hf <hf_model_name>

Arguments:

    * input_path: Path to the JSON files of papers.
    * keywords: Keywords to filter and screen papers.
    * topic_words: Topic words that define each chapter.
    * chapter_size: Number of papers included per chapter.
    * save_path: Directory where the generated corpus will be saved.
    * cache_path: Cache directory for storing papers to be summarized.
    * title_generator_hf: Name of the model used for title generation.

The output JSON file consists of entries that represent individual sections of research books. Each section contains:

    * id: Unique identifier.
    * ref: Formatted reference of the paper.
    * intro: Introduction of the paper.
    * sum_intro: Summarized introduction.
    * para_intro: Paraphrased summary of the introduction.
    * short_title: Generated short title for the paper.
    * para_title: Paraphrased short title.
    * intros: All the introductions from the paper.
    * sum_intros: Summaries of all introductions.
    * para_intros: Paraphrased summaries of all introductions.
    * conclusion: Conclusion of the paper.
    * sum_conclusion: Summarized conclusion.
    * para_conclusion: Paraphrased summary of the conclusion.
    * abstract: Abstract of the paper.
    * sum_abstract: Summarized abstract.
    * para_abstract: Paraphrased summary of the abstract.
