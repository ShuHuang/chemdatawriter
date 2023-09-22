from sentence_transformers import SentenceTransformer, util
from spacy.lang.en import English


class LatexGenerator:
    """A generator to produce LaTeX content based on provided sentences."""

    def __init__(self):
        self.spacy = English()
        self.spacy.add_pipe('sentencizer')  # Add sentencizer to the pipeline during initialization
        self.st_model = SentenceTransformer('all-MiniLM-L6-v2')

    def generate_intros(self, sents, threshold=0.9):
        """Generate introductory sentences ensuring minimal similarity between them."""

        sentences = [list(self.spacy(sent).sents) for sent in sents]
        ed = []

        for index, paper in enumerate(sentences):
            for sent in paper:
                embedding1 = self.st_model.encode(sent.text)

                if any(
                    util.cos_sim(embedding1, self.st_model.encode(existing_sent.text)).tolist()[0][0] > threshold
                    for existing_sent in ed if isinstance(existing_sent, str)
                ):
                    continue
                ed.append(sent)
            ed.append(index)

        return ed

    @staticmethod
    def latex_escape(text):
        """Escape LaTeX special characters."""
        replacements = {
            '%': '\\%',
            '&': '\\&',
            '#': '\\#',
            '_': '\\_',
            '{': '\\{',
            '}': '\\}',
            '~': '\\textasciitilde',
            '^': '\\^',
            '\\': '\\textbackslash',
            '$': '\\$'
        }
        for k, v in replacements.items():
            text = text.replace(k, v)
        return text

    @staticmethod
    def generate_body(sents, titles):
        """Generate the body of the LaTeX document."""
        text = '\\section{Chapter Title}\n'
        for index, sent in enumerate(sents):
            text += '\\subsection{' + titles[index] + '}\n'
            text += LatexGenerator.latex_escape(sent)
            text += '[' + str(index) + ']\n'
        return text

    @staticmethod
    def generate_references(sents):
        """Generate the references section of the LaTeX document."""
        text = '\\section{References}\n'
        for index, sent in enumerate(sents):
            text += '[' + str(index) + '] ' + sent + '\n'
        return text