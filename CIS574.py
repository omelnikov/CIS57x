import numpy as np, pandas as pd, nltk, re, matplotlib.pyplot as plt, wikipedia
RED, END = '\033[91m', '\033[0m'
printRed = lambda sTxt: print(RED + sTxt + END)  # lambda function
Assert = lambda bCond=False, sTxt='': printRed(sTxt) if bCond else None
