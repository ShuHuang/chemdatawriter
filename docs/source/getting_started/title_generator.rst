=============================
TitleGenerator
=============================

This module provides functionality to generate titles.

Classes
-------

.. class:: chemdatawriter.title_generator.TitleGenerator(title_generator_hf='tennessejoyce/titlewave-t5-base')

    Generates titles using a specified model.

    .. method:: __init__(title_generator_hf='tennessejoyce/titlewave-t5-base')

       Initialize the TitleGenerator with the given model.

       :param title_generator_hf: Model name or path to be used for title generation (default is 'tennessejoyce/titlewave-t5-base').
       :type title_generator_hf: str

    .. method:: generate(text, max_length=30, num_beams=5)

       Generate a title for the provided text.

       :param text: The text for which a title needs to be generated.
       :type text: str
       :param max_length: The maximum length of the generated title (default is 30).
       :type max_length: int
       :param num_beams: The number of beams to be used during generation (default is 5).
       :type num_beams: int
       :return: The generated title for the provided text.
       :rtype: str

