from IPython.core.interactiveshell import InteractiveShell as IS; IS.ast_node_interactivity = "all" # OK TO DELETE
import numpy as np, pandas as pd, nltk, re, matplotlib.pyplot as plt, seaborn as sns
RED, END = '\033[91m', '\033[0m'
printRed = lambda sTxt: print(RED + sTxt + END)  # lambda function
Assert = lambda bCond=False, sTxt='': printRed(sTxt) if bCond else None
np.set_printoptions(linewidth=10000, precision=4, edgeitems=20, suppress=True)
pd.set_option('max_rows', 100, 'max_columns', 100, 'max_colwidth', 100, 'precision', 2, 'display.max_rows', 8)


# import sys
# if not 'yake' in sys.modules:
#   !pip -q install yake > tmp.log     # https://github.com/LIAAD/yake
#   !pip -q install rake-nltk  > tmp.log   # https://pypi.org/project/rake-nltk # Rapid Automatic Keyword Extraction (RAKE)
#   !pip -q install wikipedia > tmp.log # https://pypi.org/project/wikipedia
#   from yake import KeywordExtractor as YAKE_KEA
#   from rake_nltk import Metric, Rake
#   import wikipedia
