===========================
Reader
===========================

This module contains the Reader class, which is used to read the paper.

Classes
-------
.. class:: chemdatawriter.reader.Reader(path_or_paper=None, doctype=None)

    Reader class to process and retrieve details from the BDE document.

    .. method:: __init__(path_or_paper=None, doctype=None)

       Initialize the Reader with a path or a paper.

       :param path_or_paper: The path to the document or the paper itself.
       :type path_or_paper: str|dict
       :param doctype: The type of the document ("bde" or "json").
       :type doctype: str

    .. method:: _load_bde()

       Load BDE document.

    .. method:: _load_json()

       Load JSON document.

    .. method:: _get(field, default_value="")

       Generic getter for metadata.

       :param field: Field from metadata to retrieve.
       :type field: str
       :param default_value: Default value to return if field is not present.
       :type default_value: str

    .. attribute:: metadata

        Retrieve the metadata from the document.

    .. attribute:: title

        Retrieve the title.

    .. attribute:: authors

        Retrieve the authors.

    .. attribute:: date

        Retrieve the date.

    .. attribute:: abstract

        Retrieve the abstract.

    .. attribute:: doi

        Retrieve the DOI.

    .. attribute:: body

        Retrieve the body of the document.

