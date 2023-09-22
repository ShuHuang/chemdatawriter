# -*- coding: utf-8 -*-
"""
tests.test_reader
==========================
This module contains the tests for the reader module.
"""
import os
import unittest
import warnings
from chemdatawriter.reader import Reader


def ignore_warnings(test_func):
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", ResourceWarning)
            test_func(self, *args, **kwargs)

    return do_test


class TestReaderJSONType(unittest.TestCase):
    """Test the Reader class with JSON type"""

    def setUp(self):
        """Set up the test"""
        self.scidata_path = os.path.join(os.path.dirname(__file__), "test_papers", "scidata.json")
        self.scidata_paper = Reader(self.scidata_path, doctype="json")

    def test_json_reader(self):
        """Test the JSON reader"""
        self.assertEqual(self.scidata_paper.title,
                         "A database of battery materials auto-generated using ChemDataExtractor")
        self.assertEqual(self.scidata_paper.doi, "10.1038/s41597-020-00602-2")
        self.assertEqual(self.scidata_paper.abstract,
                         "A database of battery materials is presented which comprises a total of 292,313 data records, with 214,617 unique chemical-property data relations between 17,354 unique chemicals and up to five material properties: capacity, voltage, conductivity, Coulombic efficiency and energy. 117,403 data are multivariate on a property where it is the dependent variable in part of a data series. The database was auto-generated by mining text from 229,061 academic papers using the chemistry-aware natural language processing toolkit, ChemDataExtractor version 1.5, which was modified for the specific domain of batteries. The collected data can be used as a representative overview of battery material information that is contained within text of scientific papers. Public availability of these data will also enable battery materials design and prediction via data-science methods. To the best of our knowledge, this is the first auto-generated database of battery materials extracted from a relatively large number of scientific papers. We also provide a Graphical User Interface (GUI) to aid the use of this database.")


class TestReaderManualInputJSON(unittest.TestCase):

    def setUp(self):
        """Set up the test"""
        path_or_paper = {"title": "BatteryBERT: A Pretrained Language Model for Battery Database Enhancement",
                         "authors": "Shu Huang, Jacqui Cole"}
        self.test_paper = Reader(path_or_paper=path_or_paper, doctype="json")

    def test_manual_input_json(self):
        """Test the manual input JSON"""
        self.assertEqual(self.test_paper.title,
                         "BatteryBERT: A Pretrained Language Model for Battery Database Enhancement")
        self.assertEqual(self.test_paper.authors, "Shu Huang, Jacqui Cole")


class TestReaderBDEType(unittest.TestCase):
    """Test the CDCPaperReader class for the BDE type document"""

    @ignore_warnings
    def setUp(self):
        rsc_path = os.path.join(os.path.dirname(__file__), 'test_papers', "rsc_test1.html")
        els_path = os.path.join(os.path.dirname(__file__), 'test_papers', "els_test1.xml")
        spr_path = os.path.join(os.path.dirname(__file__), 'test_papers', "spr_test1.xml")
        self.rsc_paper = Reader(path_or_paper=rsc_path, doctype="bde")
        self.els_paper = Reader(path_or_paper=els_path, doctype="bde")
        self.spr_paper = Reader(path_or_paper=spr_path, doctype="bde")

    def test_rsc_doc_metadata(self):
        metadata = self.rsc_paper.metadata
        actual = {'authors': ['Kai\xa0Qiu', 'Chao\xa0Zhang', 'Mingxia\xa0Yan',
                              'Shouwang\xa0Zhao',
                              'Hongwei\xa0Fan',
                              'Shengli\xa0An',
                              'Xinping\xa0Qiu',
                              'Guixiao\xa0Jia',
                              'Kai\xa0Qiu',
                              'Chao\xa0Zhang',
                              'Mingxia\xa0Yan',
                              'Shouwang\xa0Zhao',
                              'Hongwei\xa0Fan',
                              'Shengli\xa0An',
                              'Xinping\xa0Qiu',
                              'Guixiao\xa0Jia'],
                  'date': '2021/12/22',
                  'doi': '10.1039/D1CP04047B',
                  'firstpage': '551',
                  'html_url': 'https://pubs.rsc.org/en/content/articlelanding/2022/cp/d1cp04047b',
                  'issue': '1',
                  'journal': 'Physical Chemistry Chemical Physics',
                  'language': 'en',
                  'lastpage': '559',
                  'pdf_url': 'https://pubs.rsc.org/en/content/articlepdf/2022/cp/d1cp04047b',
                  'publisher': 'Royal Society of Chemistry',
                  'title': 'Structural transformation and electrochemical properties of a '
                           'nanosized flower-like R-MnO 2 cathode in a sodium battery ',
                  'volume': '24'}
        self.assertEqual(metadata, actual)

    def test_rsc_doc_title(self):
        title = self.rsc_paper.title
        actual = "Structural transformation and electrochemical properties of a nanosized flower-like R-MnO 2 " \
                 "cathode in a sodium battery "
        self.assertEqual(title, actual)

    def test_rsc_doc_doi(self):
        doi = self.rsc_paper.doi
        actual = "10.1039/D1CP04047B"
        self.assertEqual(doi, actual)

    def test_rsc_doc_authors(self):
        authors = self.rsc_paper.authors
        actual = ['Kai\xa0Qiu', 'Chao\xa0Zhang', 'Mingxia\xa0Yan', 'Shouwang\xa0Zhao',
                  'Hongwei\xa0Fan', 'Shengli\xa0An', 'Xinping\xa0Qiu', 'Guixiao\xa0Jia',
                  'Kai\xa0Qiu', 'Chao\xa0Zhang', 'Mingxia\xa0Yan', 'Shouwang\xa0Zhao',
                  'Hongwei\xa0Fan', 'Shengli\xa0An', 'Xinping\xa0Qiu', 'Guixiao\xa0Jia']
        self.assertEqual(authors, actual)

    def test_rsc_doc_date(self):
        date = self.rsc_paper.date
        actual = "2021/12/22"
        self.assertEqual(date, actual)

    def test_rsc_doc_abstract(self):
        abstract = self.rsc_paper.abstract
        actual = "\n High-energy density and low-cost sodium–ion batteries are being sought to meet increasing " \
                 "energy demand. Here, R-MnO2 is chosen as a cathode material of sodium–ion batteries owing to its " \
                 "low cost and high energy density. " \
                 "The structural transformation from the tunnel R-MnO2 to the layered NaMnO2 and electrochemical " \
                 "properties during the charge/discharge are investigated at the atomic level by combining " \
                 "XRD and related electrochemical experiments. " \
                 "Na≤0.04MnO2 has a tunnel R-MnO2 phase structure, Na≥0.42MnO2 has a layered NaMnO2 phase structure, " \
                 "and Na0.04−0.42MnO2 is their mixed phase. Mn3+ 3d4[t2gβ3dz2(1)3dx2−y2(0)] in NaMnO2 loses one 3dz2 " \
                 "electron and the redox couple Mn3+/Mn4+ delivers 206 mA h g−1 during the initial charge. " \
                 "The case that the Fermi energy level difference between R-MnO2 and NaMnO2 is lower than that " \
                 "between the layered Na(12-x)/12MnO2 and NaMnO2 makes the potential plateau of R-MnO2 turning into " \
                 "NaMnO2 lower than that of the layered Na(12−x)/12MnO2 to NaMnO2. This can be confirmed by our " \
                 "experiment from the 1st–2nd voltage capacity profile of R-MnO2 in EC/PC (ethylene " \
                 "carbonate/propylene carbonate) electrolyte. The study would give a new view of the production of " \
                 "sustainable sodium battery cathode materials. \n"
        self.assertEqual(abstract, actual)

    def test_els_doc_metadata(self):
        metadata = self.els_paper.metadata
        actual = {'authors': ['CHEN'],
                  'date': '2021-12-07',
                  'doi': '10.1016/j.est.2021.103685',
                  'firstpage': '103685',
                  'issue': '2352-152X',
                  'journal': 'Journal of Energy Storage',
                  'publisher': '© 2021 Elsevier Ltd. All rights reserved.',
                  'title': 'INVESTIGATIONUSEEXTENDEDSURFACESINPARAFFINWAXPHASECHANGEMATERIALINTHERMALMANAGEMENTACYLI'
                           'NDRICALLITHIUMIONBATTERYAPPLICABLEINAEROSPACEINDUSTRY',
                  'volume': '45'}
        self.assertEqual(metadata, actual)

    def test_els_doc_abstract(self):
        abstract = self.els_paper.abstract
        actual = (' The use of phase change materials (PCMs) for cooling lithium-ion batteries '
                  'is examined in this research. Because of the unique benefits of lithium-ion '
                  'batteries, their use in electric cars has gotten a lot of attention. The '
                  'lithium-ion battery is one of the most extensively utilized components as '
                  'the heart of a hybrid car. These batteries generate a lot of heat while '
                  'charging or discharging. If the batteries are not correctly handled, their '
                  'life will be drastically shortened. In this study, a cylindrical battery is '
                  'submerged in a PCM-filled chamber. Several fins of the same length are '
                  'placed on the battery. The aim is to find the ideal battery compartment size '
                  'and fin count to lower maximum battery temperature during the discharging '
                  'process. COMSOL Multiphysics commercial software is used for the '
                  'simulations. The results show that the battery with 15 fins has the best PCM '
                  'melting performance at the beginning of cooling process. After one third of '
                  'the cooling time, the maximum melting of PCM that is equal to 26.159% takes '
                  'place. Also, in the entire cooling process, the lowest maximum temperature '
                  'and the maximum volume fraction of the liquid occur when the number of fins '
                  'is 9. The battery temperature rises as the number of fins increases beyond '
                  'nine. Furthermore, an enclosure with the lowest maximum temperature is '
                  'supplied to enclosure the lithium-ion battery. ')
        self.assertEqual(abstract, actual)

    def test_spr_doc_metadata(self):
        metadata = self.spr_paper.metadata
        actual = {'abstract': 'Improving the anode properties, including increasing its '
                              'capacity, is one of the basic necessities to improve battery '
                              'performance. In this paper, high-capacity anodes with alloy '
                              'performance are introduced, then the problem of fragmentation of '
                              'these anodes and its effect during the cyclic life is stated. '
                              'Then, the effect of reducing the size to the nanoscale in '
                              'solving the problem of fragmentation and improving the '
                              'properties is discussed, and finally the various forms of '
                              'nanomaterials are examined. In this paper, electrode reduction '
                              'in the anode, which is a nanoscale phenomenon, is described. The '
                              'negative effects of this phenomenon on alloy anodes are '
                              'expressed and how to eliminate these negative effects by '
                              'preparing suitable nanostructures will be discussed. Also, the '
                              'anodes of the titanium oxide family are introduced and the '
                              'effects of Nano on the performance improvement of these anodes '
                              'are expressed, and finally, the quasi-capacitive behavior, which '
                              'is specific to Nano, will be introduced. Finally, the third type '
                              'of anodes, exchange anodes, is introduced and their function is '
                              'expressed. The effect of Nano on the reversibility of these '
                              'anodes is mentioned. The advantages of nanotechnology for these '
                              'electrodes are described. In this paper, it is found that '
                              'nanotechnology, in addition to the common effects such as '
                              'reducing the penetration distance and modulating the stress, '
                              'also creates other interesting effects in this type of anode, '
                              'such as capacitive quasi-capacitance, changing storage mechanism '
                              'and lower volume change.',
                  'authors': ['Majdi',
                              'Latipov',
                              'Borisov',
                              'Yuryevna',
                              'Kadhim',
                              'Suksatan',
                              'Khlewee',
                              'Kianfar'],
                  'date': '20211211',
                  'doi': '10.1186/s11671-021-03631-x',
                  'issue': '1',
                  'journal': 'Nanoscale Research Letters',
                  'publisher': 'Springer US',
                  'title': 'Nano and Battery Anode: A Review',
                  'volume': '16'}
        self.assertEqual(metadata, actual)

    def test_spr_doc_abstract(self):
        abstract = self.spr_paper.abstract
        actual = 'Improving the anode properties, including increasing its capacity, is one of the basic necessities ' \
                 'to improve battery performance. In this paper, high-capacity anodes with alloy performance are ' \
                 'introduced, then the problem of fragmentation of these anodes and its effect during the cyclic ' \
                 'life is stated. Then, the effect of reducing the size to the nanoscale in solving the problem of ' \
                 'fragmentation and improving the properties is discussed, and finally the various forms of ' \
                 'nanomaterials are examined. In this paper, electrode reduction in the anode, which is a ' \
                 'nanoscale phenomenon, is described. The negative effects of this phenomenon on alloy anodes are ' \
                 'expressed and how to eliminate these negative effects by preparing suitable nanostructures will ' \
                 'be discussed. Also, the anodes of the titanium oxide family are introduced and the effects of Nano ' \
                 'on the performance improvement of these anodes are expressed, and finally, the quasi-capacitive ' \
                 'behavior, which is specific to Nano, will be introduced. Finally, the third type of anodes, ' \
                 'exchange anodes, is introduced and their function is expressed. The effect of Nano on the ' \
                 'reversibility of these anodes is mentioned. The advantages of nanotechnology for these electrodes ' \
                 'are described. In this paper, it is found that nanotechnology, in addition to the common effects ' \
                 'such as reducing the penetration distance and modulating the stress, also creates other interesting ' \
                 'effects in this type of anode, such as capacitive quasi-capacitance, changing storage mechanism ' \
                 'and lower volume change.'
        self.assertEqual(abstract, actual)


class TestReaderError(unittest.TestCase):
    """Test the error of Reader class"""

    def test_wrong_doctype_error(self):
        with self.assertRaises(ValueError):
            Reader(path_or_paper="", doctype="other")

    def test_wrong_json_error(self):
        with self.assertRaises(ValueError):
            Reader(path_or_paper="els_test1.xml", doctype="json")


if __name__ == '__main__':
    unittest.main()
