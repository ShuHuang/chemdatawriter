=============================
Paraphraser
=============================

This module contains the Paraphraser class.

Classes
-------

.. class:: chemdatawriter.paraphraser.Paraphraser(language='de')

    A class to perform paraphrasing using back-translation.

    .. method:: __init__(language='de')

       Initialize with a specific language for back-translation.

       :param language: Language for back-translation (default is 'de'). Supported languages: de, zh, ge, fr, ru, ar, jap.
       :type language: str

    .. method:: paraphrase(text)

       Paraphrase a given text using back-translation.

       :param text: The text to be paraphrased.
       :type text: str
       :return: The paraphrased text.
       :rtype: str

    .. method:: score(text)

       Calculate the Rouge score for the paraphrased version of the text.

       :param text: The original text.
       :type text: str
       :return: The Rouge scores comparing the original and the paraphrased text.
       :rtype: dict

