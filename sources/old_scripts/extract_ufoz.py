import zipfile
import os, sys
from os.path import basename

ufozName=sys.argv[1]

#extract ufoz
with zipfile.ZipFile(ufozName, 'r') as zip_ref:
    zip_ref.extractall(".")
