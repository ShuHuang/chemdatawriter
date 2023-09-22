=============================
LatexGenerator
=============================

This module contains a class to generate LaTeX content based on the provided sentences.


Classes
-------

.. class:: chemdatawriter.latex_generator.LatexGenerator

    A generator to produce LaTeX content based on provided sentences.

    .. method:: __init__()

       Initialize the `LatexGenerator` instance.

    .. method:: generate_intros(sents, threshold=0.9)

       Generate introductory sentences ensuring minimal similarity between them.

       :param sents: List of sentences.
       :type sents: list of str
       :param threshold: The similarity threshold, beyond which sentences are considered similar (default is 0.9).
       :type threshold: float
       :return: List of introductory sentences.
       :rtype: list of str

    .. method:: latex_escape(text)

       Escape LaTeX special characters.

       :param text: Text containing special characters.
       :type text: str
       :return: Text with special characters escaped for LaTeX.
       :rtype: str

    .. method:: generate_body(sents, titles)

       Generate the body of the LaTeX document.

       :param sents: List of sentences.
       :type sents: list of str
       :param titles: List of titles corresponding to the sentences.
       :type titles: list of str
       :return: Body of the LaTeX document.
       :rtype: str

    .. method:: generate_references(sents)

       Generate the references section of the LaTeX document.

       :param sents: List of sentences.
       :type sents: list of str
       :return: References section of the LaTeX document.
       :rtype: str

