# chemdatawriter
ChemDataWriter is a transformer-based library for automatically generating research books in the chemistry area.

# Features
- ```reader.py``` processes the raw XML/HTML paper files and converts them into a Reader object.
- ```finder.py``` suggests the key topics of the paper corpus
- ```retrieve.py``` retrieves the papers from the corpus based on the key topics
- ```summariser.py``` summarises the papers based on the input text
- ```paraphraser.py``` paraphrases the summarised text
- ```title_generator.py``` generates the short title in terms of the original long title
- ```latex_generator.py``` reorganises the summarised text and converts it into a LaTeX file

# Installation
```pip install chemdatawriter```  

Note: ChemDataWriter has been tested running in Python3.8.

Note: Available once the paper is accepted

# Usage
To create a clean paper file with the title, abstract, introduction, and conclusion from the HTML/XML files, and 
extract the reference information automatically, run:

```bash
python run_corpus.py \
  --input_path <path to the input directory> \
  --output_path <path to the output JSON file>
```

To auto-generate the research book using the output JSON file above, run:

```bash
python run_cdw.py \
  --input_path <path to the input JSON file> \
  --output_path <path to the output JSON file> \
  --cache_path <path to the cache directory> \
  --keywords <keywords to screen the papers> \
  --topic_words <topic words of each chapter> \
  --chapter_size <number of papers in each chapter>
```

# Acknowledgement

This project was financially supported by the [Science and Technology Facilities Council (STFC)](https://www.ukri.org/councils/stfc/), the [Royal Academy of Engineering](https://raeng.org.uk/) (RCSRF1819\7\10) and [Christ's College, Cambridge](https://www.christs.cam.ac.uk/). The Argonne Leadership Computing Facility, which is a [DOE Office of Science Facility](https://science.osti.gov/), is also acknowledged for use of its research resources, under contract No. DEAC02-06CH11357.

# Citation

TBA
