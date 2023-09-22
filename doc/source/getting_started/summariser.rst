=============================
Summariser
=============================

This module contains various Summariser classes.


Classes
-------

.. class:: chemdatawriter.summariser.Summariser

    Base class for summariser.

    .. method:: __init__()

       Initialize the summariser.

    .. method:: summarise(text, *args, **kwargs)

       Abstract method to summarize the data.

       :param text: Text to be summarized.
       :type text: str

    .. method:: read(text)

       Set the text for summarization.

       :param text: Text to be set.
       :type text: str


.. class:: chemdatawriter.summariser.TransformerSummariser(model_name)

    Base class for Transformer-based summarisers.

    .. inheritdoc:: chemdatawriter.summariser.Summariser

    .. method:: __init__(model_name)

       Initialize the TransformerSummariser.

       :param model_name: Name of the transformer model.
       :type model_name: str


.. class:: chemdatawriter.summariser.TextRankSummariser

    TextRank summariser using the Summa library.

    .. inheritdoc:: chemdatawriter.summariser.Summariser

    .. method:: keywords(text, words=5)

       Extract keywords from the input text.

       :param text: Input text for keyword extraction.
       :type text: str
       :param words: Number of keywords to return.
       :type words: int


.. class:: chemdatawriter.summariser.LargeBartSummariser

    LargeBART summariser for samsum.

    .. inheritdoc:: chemdatawriter.summariser.TransformerSummariser


.. class:: chemdatawriter.summariser.DistilBartSummariser

    DistilBART summariser.

    .. inheritdoc:: chemdatawriter.summariser.TransformerSummariser


.. class:: chemdatawriter.summariser.LargeBookLEDSummariser

    LargeBook LED summariser.

    .. inheritdoc:: chemdatawriter.summariser.TransformerSummariser


.. class:: chemdatawriter.summariser.XsumPegasusSummariser

    Xsum Pegasus summariser.

    .. inheritdoc:: chemdatawriter.summariser.TransformerSummariser


.. class:: chemdatawriter.summariser.LongBookT5Summariser

    LongBook T5 summariser.

    .. inheritdoc:: chemdatawriter.summariser.TransformerSummariser

