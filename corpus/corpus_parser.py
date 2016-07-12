__author__ = 'linanqiu'

import logging
import os.path
import sys
import pickle

logger = logging.getLogger('corpus_parser')

program = os.path.basename(sys.argv[0])
logger = logging.getLogger(program)
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
logging.root.setLevel(level=logging.INFO)
logger.info("running %s" % ' '.join(sys.argv))


# returns lists of sentence, each sentence is a list of words, lower case.
def parse_wsj():
    import nltk.corpus as corpus
    import re

    pattern = re.compile('\*[^\s]*')

    logger.info('Parsing WSJ Corpus')

    corpus_root = "LDC99T42-Treebank-3/package/treebank_3/parsed/mrg/wsj"
    file_pattern = ".*/wsj_.*\.mrg"

    reader = corpus.BracketParseCorpusReader(corpus_root, file_pattern)

    count = 1

    for fileid in reader.fileids():
        logger.info('Writing wsj_corpus/article_%d.txt' % count)
        # remove annoying stars
        article_lower = [word.lower() for word in reader.words(fileids=fileid) if not pattern.match(word)]
        f_out = open('wsj_corpus/article_%d.txt' % count, 'w')
        f_out.write(' '.join(article_lower))
        f_out.close()
        count += 1

logger.info('Begin Parsing WSJ')
parse_wsj()
