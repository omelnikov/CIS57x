import sys
from IPython.core.interactiveshell import InteractiveShell as IS; IS.ast_node_interactivity = "all" # OK TO DELETE
import numpy as np, pandas as pd, nltk, re, string, matplotlib.pyplot as plt, seaborn as sns, pprint, unicodedata
from collections import Counter

RED, END = '\033[91m', '\033[0m'
printRed = lambda sTxt: print(RED + sTxt + END)  # lambda function
Assert = lambda bCond=False, sTxt='': printRed(sTxt) if not bCond else None
np.set_printoptions(linewidth=10000, precision=4, edgeitems=20, suppress=True)
pd.set_option('max_rows', 100, 'max_columns', 100, 'max_colwidth', 100, 'precision', 2, 'display.max_rows', 8)

def CorpusStats(CorpusName='gutenberg', C=None):
  tmp = nltk.download(CorpusName, quiet=True)  # https://www.nltk.org/book/ch02.html
  def GetSents(C,n):
    try: return len(C.sents(n))
    except: return 0
  Stats=[(n, GetSents(C,n), len(C.words(n)), len(C.raw(n)), ' '.join(C.words(n)[:100])) for n in C.fileids()]
  df = pd.DataFrame(Stats, columns=[CorpusName,'sents','words','char','raw'])
  return df.sort_values('words')

def ShowNLTKCorpora():
  print(CorpusStats('webtext', nltk.corpus.webtext))
  print(CorpusStats('gutenberg', nltk.corpus.gutenberg))
  print(CorpusStats('brown', nltk.corpus.brown))
  print(CorpusStats('reuters', nltk.corpus.reuters))
  print(CorpusStats('inaugural', nltk.corpus.inaugural))
  print(CorpusStats('nps_chat', nltk.corpus.nps_chat))
  print(CorpusStats('names', nltk.corpus.names))
 
# import sys
# if not 'yake' in sys.modules:
#   !pip -q install yake > tmp.log     # https://github.com/LIAAD/yake
#   !pip -q install rake-nltk  > tmp.log   # https://pypi.org/project/rake-nltk # Rapid Automatic Keyword Extraction (RAKE)
#   !pip -q install wikipedia > tmp.log # https://pypi.org/project/wikipedia
#   from yake import KeywordExtractor as YAKE_KEA
#   from rake_nltk import Metric, Rake
#   import wikipedia
