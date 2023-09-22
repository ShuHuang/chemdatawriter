# -*- coding: utf-8 -*-
"""
run_cdw

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This file is used to generate research books using the CDW framework.

author: Shu Huang (sh2009@cam.ac.uk)
"""
import json
import argparse
from chemdatawriter.paraphraser import Paraphraser
from chemdatawriter.title_generator import TitleGenerator
from chemdatawriter.summariser import DistilBartSummariser
from chemdatawriter.retriever import Retriever


def parse_arguments():
    """Parse arguments from CLI or defaults.
    :return: parsed arguments
    """
    parser = argparse.ArgumentParser()

    # Adding all the necessary arguments
    parser.add_argument("--input_path", default=None, type=str, help="Path to folder containing Springer JATS XML files.")
    parser.add_argument("--keywords", default=[], type=str, nargs="*", help="Keywords to screen papers")
    parser.add_argument("--topic_words", default=[], type=str, nargs="*", help="Topic words of each chapter")
    parser.add_argument("--chapter_size", default=50, type=int, help="Number of papers per chapter")
    parser.add_argument("--save_path", default=None, type=str, help="Path to folder to save the corpus.")
    parser.add_argument("--cache_path", default=None, type=str, help="Cache path to store paper to be summarized.")
    parser.add_argument("--title_generator_hf", default='tennessejoyce/titlewave-t5-base', type=str, help="Model name for title generation.")
    
    return parser.parse_args()


def main(args):
    title_generator = TitleGenerator(args.title_generator_hf)
    summariser = DistilBartSummariser()
    paraphraser = Paraphraser('de')

    papers, subpapers = [], []
    with open(args.input_path, 'r', encoding='utf-8') as f:
        for line in f:
            papers.append(json.loads(line))

    keywords = [i.replace("_", " ") for i in args.keywords]
    for i in papers:
        for keyword in keywords:
            if keyword.lower() in i['title'].lower():
                subpapers.append(i)

    docs = []  # For paper retrieval
    for i in subpapers:
        title = i['title'] + "."
        # abstract = i['abstract'][0]
        intro = i['introduction'][-1]
        # conclusion = " ".join(i['conclusion'])
        docs.append(title + " " + intro)

    retriever = Retriever(subpapers)

    topic_words = args.topic_words.replace("_", " ")
    section_index = retriever.retrieve(query=topic_words, cache_path=args.cache_path, chapter_size=args.chapter_size)
    to_save = {}
    id = 1
    for section in section_index:
        title = subpapers[section]['title']

        to_save['id'] = id
        id += 1
        to_save['ref'] = subpapers[section]['reference']
        intro = subpapers[section]['introduction'][0].replace("\n", "")
        to_save['intro'] = intro
        summer = summariser.summarise(intro)
        to_save['sum_intro'] = [summer]
        para = paraphraser.paraphrase(summer)
        to_save['para_intro'] = [para]
        t = title_generator.generate(title)
        para_t = paraphraser.paraphrase(t)
        to_save['short_title'] = t
        to_save['para_title'] = para_t

        summers, paras = [], []
        for intros in subpapers[section]['introduction'][1:]:
            summer = summariser.summarise(intros.replace("\n", ""))
            para = paraphraser.paraphrase(summer)
            summers.append(summer)
            paras.append(para)
        to_save['intros'] = subpapers[section]['introduction'][1:]
        to_save['sum_intros'] = summers
        to_save['para_intros'] = paras

        summers, paras = [], []
        for intros in subpapers[section]['conclusion']:
            summer = summariser.summarise(intros.replace("\n", ""))
            para = paraphraser.paraphrase(summer)
            summers.append(summer)
            paras.append(para)
        to_save['conclusion'] = subpapers[section]['conclusion']
        to_save['sum_conclusion'] = summers
        to_save['para_conclusion'] = paras

        summers, paras = [], []
        for intros in subpapers[section]['abstract']:
            summer = summariser.summarise(intros.replace("\n", ""))
            para = paraphraser.paraphrase(summer)
            summers.append(summer)
            paras.append(para)
        to_save['abstract'] = subpapers[section]['abstract']
        to_save['sum_abstract'] = summers
        to_save['para_abstract'] = paras

        with open(args.save_path, 'a', encoding='utf-8') as f:
            json.dump(to_save, f)
            f.write('\n')


if __name__ == '__main__':
    args = parse_arguments()

    if args.input_path is None:
        raise ValueError('--input_path must be provided via arguments or the '
                         'config file')

    if args.save_path is None:
        raise ValueError('--save_path must be provided via arguments or the '
                         'config file')

    if args.cache_path is None:
        raise ValueError('--cache_path must be provided via arguments or the '
                         'config file')

    if args.keywords is None:
        raise ValueError('--keywords must be provided via arguments or the '
                         'config file')

    if args.topic_words is None:
        raise ValueError('--topic_words must be provided via arguments or the '
                         'config file')

    if args.chapter_size is None:
        raise ValueError('--chapter_size must be provided via arguments or the '
                         'config file')

    main(args)
