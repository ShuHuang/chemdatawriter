# -*- coding: utf-8 -*-
"""
run_corpus

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This file is to be used for creating a corpus of papers from the Springer JATS XML files.

author: Shu Huang (sh2009@cam.ac.uk)
"""
from os import listdir
from os.path import isfile, join
import json
import argparse
from batterydataextractor import Document
from batterydataextractor.doc.text import Heading1


def parse_arguments():
    """Parse arguments from cli or defaults.
    :return: parsed arguments
    """
    parser = argparse.ArgumentParser()

    # Optional json config to override defaults below
    parser.add_argument("--input_path", default=None, type=str,
                        help="The path to the folder containing the Springer JATS XML files.")

    parser.add_argument("--save_path", default=None, type=str,
                        help="The JSON path to the folder to save the corpus.")

    parse_args = parser.parse_args()

    # Distinguish arguments that were found in sys.argv[1:]
    aux_parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    for arg in vars(parse_args):
        aux_parser.add_argument('--' + arg)
    cli_args, _ = aux_parser.parse_known_args()

    return parse_args


def spr_ref(metadata):
    authors = []
    for i in metadata['authors']:
        given_name, surname = i.split(" ")
        authors.append(surname + ', ' + given_name[0] + ".;")
    authors[-1] = authors[-1].replace(";", ". ")
    title = metadata['title'].rstrip() + '. '
    journal = metadata['journal'] + '. '
    year = metadata['date'][0:4] + ', '
    issue = '(' + metadata['issue'] + '), '
    volume = metadata['volume']
    page = metadata['firstpage'] + '-' + metadata['lastpage'] + ', '
    doi = "DOI: " + metadata['doi']
    ref = " ".join(authors) + title + journal + year + volume + issue + page + doi
    return ref


def main(args):

    paper_files = [f for f in listdir(args.input_path) if isfile(join(args.input_path, f))]

    papers = []
    for file in paper_files:
        path = args.input_path + file
        paper = Document.from_file(path)

        try:
            reference = spr_ref(paper.metadata[0].serialize())
        except:
            continue

        title = paper.metadata[0].serialize()['title'].rstrip()
        date = paper.metadata[0].serialize()['date'].replace("/", "")
        doi = paper.metadata[0].serialize()['doi'].replace("/", "_")

        intro, conclusion, abstract = [], [], []

        try:
            abstract.append(paper.metadata[0].serialize()['abstract'])
        except:
            continue

        heading_index = []
        for index, element in enumerate(paper.elements):
            if type(element) == Heading1:
                heading_index.append(index)

        flag_intro, flag_con = 0, 0

        for index in heading_index:
            if "Introduction" in paper.elements[index].text:
                flag_intro = index + 1
            if "Conclusion" in paper.elements[index].text:
                flag_con = index + 1

        if flag_intro != 0:
            while flag_intro not in heading_index:
                intro.append(paper.elements[flag_intro].text)
                flag_intro += 1

        if flag_con != 0:
            while flag_con not in heading_index:
                conclusion.append(paper.elements[flag_con].text)
                flag_con += 1

        if intro != [] and abstract != []:
            doc = {'title': title, 'abstract': abstract, 'introduction': intro, 'conclusion': conclusion,
                   'reference': reference}
            papers.append(doc)

            with open(args.save_path, 'a') as f:
                json.dump(doc, f, ensure_ascii=False)
                f.write("\n")


if __name__ == '__main__':
    args = parse_arguments()

    if args.input_path is None:
        raise ValueError('--input_path must be provided via arguments or the '
                         'config file')

    if args.save_path is None:
        raise ValueError('--save_path must be provided via arguments or the '
                         'config file')

    main(args)
